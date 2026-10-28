"""Regenerate every output of the PRELIMINARY Diesel Heater Module (002) model.

    uv run python build.py                      # all three variants and the comparison
    uv run python build.py --variant adjusted   # one variant only

Writes to ./out/<variant>/: heater-module.step (not committed), isometric.svg,
PNG views, member-schedule.md; and to ./out/: comparison.png, comparison.md.

Exit status is non-zero if any PNG render fails. A PNG that is about to be
rendered is deleted first, and after rendering the file is checked to be a
complete, decodable PNG (VTK writer error codes are checked too), so a failed
render leaves no file under that name and an old or partial image can never
pass for the current build's output.
PRELIMINARY — NOT FOR FABRICATION.
"""

from __future__ import annotations

import argparse
import datetime as dt
import math
import sys
from pathlib import Path

import cadquery as cq

import params as P
from model import BANNER, MEMBER_ROLES, Part, build_assembly, build_parts, members

OUT = Path(__file__).parent / "out"

# Per-variant PNG views: (file name, camera position direction, view-up, parallel projection, caption)
VIEWS = {
    "original": [
        ("isometric.png", (1.0, -1.0, 0.8), (0, 0, 1), False,
         "View from +X/-Y: heater (orange) on crossmembers (blue); tank (cream) on rails (green) at the far wall"),
        ("tank-side.png", (-1.0, -1.0, 0.7), (0, 0, 1), False,
         "View from -X/-Y: tank wall; red marks are the three reported mounting points on the rails"),
    ],
    "compact": [
        ("isometric.png", (1.0, 1.0, 0.8), (0, 0, 1), False,
         "View from +X/+Y: tank (cream) on the far X-min wall beside the heater (orange); yellow = outlet cue (+Y end)"),
        ("top.png", (0.0, 0.0, 1.0), (0, 1, 0), True,
         "Top view, parallel projection: separate horizontal footprints of tank (left) and heater (right)"),
        ("front-elevation.png", (0.0, -1.0, 0.0), (0, 0, 1), True,
         "Elevation from -Y, parallel projection: tank bottom above the plate, overlapping the heater in height only"),
    ],
    "adjusted": [
        ("isometric.png", (1.0, 1.0, 0.8), (0, 0, 1), False,
         "View from +X/+Y: tank (cream) on the far wall beside the heater (orange); red = reported plate holes"),
        ("top.png", (0.0, 0.0, 1.0), (0, 1, 0), True,
         "Top view, parallel: separate footprints; plate hole markers on the crossmember lines"),
        ("front-elevation.png", (0.0, -1.0, 0.0), (0, 0, 1), True,
         "Elevation from -Y, parallel: tank bottom above the heater top by the D-15 gap (not a clearance)"),
    ],
}
COMPARISON_VIEW = ((0.55, -1.0, 0.5), (0, 0, 1))  # camera direction and view-up; always parallel projection
COMPARISON_GAP = 300.0  # mm between adjacent frames along X in the comparison scene


def write_step(assy: cq.Assembly, path: Path) -> None:
    assy.export(str(path))


def write_svg(assy: cq.Assembly, path: Path, variant: P.Variant, direction=(1.0, 1.0, 0.75)) -> None:
    cq.exporters.export(
        assy.toCompound(), str(path), exportType="SVG",
        opt={"width": 1000, "height": 800, "marginLeft": 20, "marginTop": 20,
             "projectionDir": direction, "showAxes": True, "strokeWidth": 0.8,
             "showHidden": False},
    )
    text = path.read_text(encoding="utf-8")
    label = (f'<text x="20" y="30" font-family="sans-serif" font-size="22" fill="#c00000">'
             f'{BANNER} — {variant.title}: bounding-box placeholders, illustrative placement</text>\n')
    open_tag_end = text.index(">", text.index("<svg")) + 1  # end of the opening <svg ...> tag
    path.write_text(text[:open_tag_end] + "\n" + label + text[open_tag_end:], encoding="utf-8")


def _add_actors(ren, parts: list[Part], offset=(0.0, 0.0, 0.0)) -> None:
    import vtk

    for p in parts:
        shape = p.shape.translate(cq.Vector(*offset)) if any(offset) else p.shape
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(shape.toVtkPolyData(0.5, 0.2))
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(*p.color)
        actor.GetProperty().EdgeVisibilityOn()
        actor.GetProperty().SetEdgeColor(0.2, 0.2, 0.2)
        ren.AddActor(actor)


def _render(ren, path: Path, view_from, view_up, parallel: bool, size=(1400, 1600), text=""):
    """Render ``ren`` off screen to ``path``; returns (window, renderer) so callers can inspect the camera."""
    import vtk

    banner = vtk.vtkTextActor()
    banner.SetInput(text)
    banner.GetTextProperty().SetFontSize(26)
    banner.GetTextProperty().SetColor(0.75, 0, 0)
    banner.SetPosition(20, size[1] - 100)
    ren.AddViewProp(banner)
    cam = ren.GetActiveCamera()
    cam.SetPosition(*view_from)
    cam.SetFocalPoint(0, 0, 0)
    cam.SetViewUp(*view_up)
    cam.SetParallelProjection(1 if parallel else 0)
    ren.ResetCamera()  # frame the whole scene for this direction
    win = vtk.vtkRenderWindow()
    win.SetOffScreenRendering(1)
    win.AddRenderer(ren)
    win.SetSize(*size)
    win.Render()
    w2i = vtk.vtkWindowToImageFilter()
    w2i.SetInput(win)
    w2i.Update()
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(str(path))
    writer.SetInputConnection(w2i.GetOutputPort())
    writer.Write()
    # vtkPNGWriter reports failure (for example an unwritable destination) through its
    # error code, not a Python exception.
    code = writer.GetErrorCode()
    if code != 0:
        raise RenderError(f"vtkPNGWriter error {code} ({vtk.vtkErrorCode.GetStringFromErrorCode(code)}) writing {path.name}")
    return win, ren


class RenderError(RuntimeError):
    """A PNG was not produced, or the file on disk is not a valid image."""


def validate_png(path: Path) -> None:
    """Raise RenderError unless ``path`` is a complete, decodable PNG with non-zero size.

    Uses Pillow (a dependency of CadQuery through matplotlib). VTK's own PNG reader is
    not used because it crashes the process on a truncated file.
    """
    from PIL import Image

    if not path.is_file():
        raise RenderError(f"{path.name} was not created")
    if path.stat().st_size == 0:
        raise RenderError(f"{path.name} is empty")
    try:
        with Image.open(path) as im:
            im.verify()  # header and chunk CRCs
        with Image.open(path) as im:
            im.load()  # full decode; a truncated IDAT stream fails here
            fmt, size = im.format, im.size
    except Exception as exc:  # any decode failure means the file is not a valid output
        raise RenderError(f"{path.name} is not a valid PNG: {exc!r}") from exc
    if fmt != "PNG" or min(size) < 1:
        raise RenderError(f"{path.name} is not a PNG image (format {fmt}, size {size})")


def write_png(parts: list[Part], path: Path, variant: P.Variant, view_from, view_up, parallel, caption):
    """Shaded render through VTK's off-screen renderer, camera looking from ``view_from``."""
    import vtk  # provided by the cadquery dependency set

    ren = vtk.vtkRenderer()
    ren.SetBackground(1, 1, 1)
    _add_actors(ren, parts)
    return _render(ren, path, view_from, view_up, parallel,
                   text=f"{BANNER} — {variant.title}\nBounding-box placeholders; illustrative placement; gates G1-G5 closed\n{caption}")


def comparison_offsets(keys: list[str]) -> dict[str, float]:
    """X offset of each variant's origin in the comparison scene."""
    offsets, x = {}, 0.0
    for key in keys:
        offsets[key] = x
        x += P.VARIANTS[key].envelope_w + COMPARISON_GAP
    return offsets


def write_comparison_png(parts_by_key: dict[str, list[Part]], path: Path):
    """All variants in one scene, side by side along X, in parallel projection so one world
    millimetre is the same number of pixels for every frame. Returns (window, renderer)."""
    import vtk

    ren = vtk.vtkRenderer()
    ren.SetBackground(1, 1, 1)
    offsets = comparison_offsets(list(parts_by_key))
    labels = []
    for key, parts in parts_by_key.items():
        v = P.VARIANTS[key]
        _add_actors(ren, parts, offset=(offsets[key], 0.0, 0.0))
        labels.append(f"{v.title} {v.envelope_w / P.IN:.0f} x {v.envelope_d / P.IN:.0f} x {v.envelope_h / P.IN:.0f} in")
    view_from, view_up = COMPARISON_VIEW
    return _render(ren, path, view_from, view_up, True, size=(2600, 1400),
                   text=f"{BANNER}\nParallel projection, same scale, same component colours; left to right: " + " | ".join(labels)
                        + "\nBounding-box placeholders; illustrative placement; gates G1-G5 closed")


def write_schedule(parts: list[Part], path: Path, variant: P.Variant) -> None:
    lines = [
        f"# Member schedule — {variant.title} — {BANNER}",
        "",
        f"Generated {dt.date.today().isoformat()} by `build.py` from `params.py` (variant `{variant.key}`). All lengths in millimetres, nominal, as modelled.",
        "",
        "**This is not a cut list.** Every length depends on the joint assumption below, which the design has not chosen (D-01, D-02), and on illustrative level heights and tank position. Every member's placement and connection is provisional; the Basis column names what each depends on. Gates G1–G5 in spec.md §10 are closed.",
        "",
        f"Joint assumption: {P.JOINT_ASSUMPTION}",
        "",
        f"Tank assumption: {P.TANK_WALL_ASSUMPTION}",
        "",
        f"Layout: {P.LAYOUT_NOTE[variant.layout]}",
        "",
        "| ID | Role | Axis | Nominal length (mm) | Section (mm) | Basis (what the size and placement depend on) | Note |",
        "|---|---|---|---|---|---|---|",
    ]
    for p in members(parts):
        lines.append(f"| {p.id} | {p.role} | {p.axis} | {p.length:.1f} | {P.PROFILE_MINOR:.0f} × {P.PROFILE_MAJOR:.0f} | "
                     f"{p.basis} | {p.note} |")
    lines += [
        "",
        f"Members: {len(members(parts))}. Other components (placeholders): "
        + ", ".join(p.id for p in parts if p.role not in MEMBER_ROLES)
        + ".",
        "",
        "## Parameters",
        "",
        "| Parameter | Value | Tag | Source |",
        "|---|---|---|---|",
    ]
    for q in variant.params() + P.SHARED_PARAMS:
        lines.append(f"| {q.name} | {q.value:.1f} {q.unit} | {q.tag} | {q.source} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ------------------------------------------------------------- comparison table

def _gap(a, b) -> tuple[float, float, float, float]:
    """Per-axis bounding-box gaps (0 where the boxes overlap on that axis) and the straight-line gap."""
    gx = max(0.0, a.xmin - b.xmax, b.xmin - a.xmax)
    gy = max(0.0, a.ymin - b.ymax, b.ymin - a.ymax)
    gz = max(0.0, a.zmin - b.zmax, b.zmin - a.zmax)
    return gx, gy, gz, math.sqrt(gx * gx + gy * gy + gz * gz)


def _rng(b, ax: str) -> str:
    lo, hi = getattr(b, f"{ax}min"), getattr(b, f"{ax}max")
    return f"{lo:.1f}–{hi:.1f}"


def comparison_rows(parts_by_key: dict[str, list[Part]]) -> list[tuple[str, dict[str, str]]]:
    rows: list[tuple[str, dict[str, str]]] = []

    def add(label, fn):
        rows.append((label, {k: fn(P.VARIANTS[k], parts) for k, parts in parts_by_key.items()}))

    bbs = {k: {p.id: p.shape.BoundingBox() for p in parts} for k, parts in parts_by_key.items()}

    def bb(v, pid):
        return bbs[v.key][pid]

    add("Envelope W × D × H (in)", lambda v, _: f"{v.envelope_w / P.IN:.0f} × {v.envelope_d / P.IN:.0f} × {v.envelope_h / P.IN:.0f}")
    add("Envelope W × D × H (mm)", lambda v, _: f"{v.envelope_w:.1f} × {v.envelope_d:.1f} × {v.envelope_h:.1f}")
    add("Envelope tag", lambda v, _: v.envelope_tag)
    add("Layout", lambda v, _: v.layout)
    add("Members / parts", lambda v, p: f"{len(members(p))} / {len(p)}")
    add("Level member bottom faces Z", lambda v, _: ", ".join(f"{z:.1f}" for z in v.level_z))
    add("Heater axis (13.4 in length)", lambda v, _: v.heater_axis)
    add("Plate underside Z (open height above the bottom members in brackets)",
        lambda v, _: f"{bb(v, 'heater_plate').zmin:.1f} ({bb(v, 'heater_plate').zmin - P.PROFILE_MAJOR:.1f})")
    add("Plate top face Z", lambda v, _: f"{bb(v, 'heater_plate').zmax:.1f}")
    add("Crossmember spacing, centre to centre (basis)",
        lambda v, _: f"{v.crossmember_spacing:.1f} ({'reported plate hole pitch, not measured' if v.plate_holes else 'illustrative'})")
    add("Heater body X", lambda v, _: _rng(bb(v, "heater_body"), "x"))
    add("Heater body Y", lambda v, _: _rng(bb(v, "heater_body"), "y"))
    add("Heater body Z", lambda v, _: _rng(bb(v, "heater_body"), "z"))
    add("Outlet cue end", lambda v, _: v.outlet_end or "none (D-07/D-08 open)")
    add("Tank X", lambda v, _: _rng(bb(v, "fuel_tank"), "x"))
    add("Tank Y", lambda v, _: _rng(bb(v, "fuel_tank"), "y"))
    add("Tank Z", lambda v, _: _rng(bb(v, "fuel_tank"), "z"))
    add("Tank bottom minus heater top Z", lambda v, _: f"{bb(v, 'fuel_tank').zmin - bb(v, 'heater_body').zmax:+.1f}")
    add("Rail centre Z (lower, upper)", lambda v, _: f"{bb(v, 'TR-lower').center.z:.1f}, {bb(v, 'TR-upper').center.z:.1f}")
    add("Filler neck centre (X, Y)", lambda v, _: f"{bb(v, 'tank_filler_neck').center.x:.1f}, {bb(v, 'tank_filler_neck').center.y:.1f}")
    add("Top-level bottom face Z minus filler top Z (negative: filler rises into the top-member band, clear of the members in plan)",
        lambda v, _: f"{v.level_z[2] - bb(v, 'tank_filler_neck').zmax:+.1f}")
    add(f"Top-level bottom face Z minus (tank top + {P.FILLER_CAP_ALLOWANCE:.0f} mm filler/cap allowance; neck and cap not measured)",
        lambda v, _: f"{v.level_z[2] - (bb(v, 'fuel_tank').zmax + P.FILLER_CAP_ALLOWANCE):+.1f}")
    add("Filler cue centre X minus X-min top member inside face (reach past the member from above)",
        lambda v, _: f"{bb(v, 'tank_filler_neck').center.x - P.PROFILE_MINOR:+.1f}")

    def gap_row(label, pa, pb):
        def fn(v, _):
            gx, gy, gz, g = _gap(bb(v, pa), bb(v, pb))
            return f"dx {gx:.1f}, dy {gy:.1f}, dz {gz:.1f}; min {g:.1f}"
        add(label, fn)

    gap_row("Bounding-box gap tank → heater body (mm)", "fuel_tank", "heater_body")
    gap_row("Bounding-box gap tank → heater plate (mm)", "fuel_tank", "heater_plate")
    gap_row("Bounding-box gap tank → crossmember HX1 (mm)", "fuel_tank", "HX1")
    gap_row("Bounding-box gap heater body → nearest X-max member L2-D2 (mm)", "heater_body", "L2-D2")
    return rows


def write_comparison_md(parts_by_key: dict[str, list[Part]], path: Path) -> None:
    keys = list(parts_by_key)
    lines = [
        f"# Layout comparison — {BANNER}",
        "",
        f"Generated {dt.date.today().isoformat()} by `build.py`. Millimetres unless stated. Positions are modelled bounding boxes of placeholders.",
        "",
        "**The bounding-box gaps below are modelled distances between placeholder boxes. They do not establish safe fuel-spill, fire, thermal, exhaust, or intake clearances.** The manufacturer states none (spec C-list, \"not stated\"); SR-01, SR-02, SR-04, SR-11 and the hazard register remain open, and gates G1–G5 are closed for every layout. B1 Adjusted is the preferred preliminary layout (Owner decision 2026-10-28; spec MR-02 as amended). A Original (the 2026-10-27 envelope) and B1 Compact (the 2026-10-28 starting point) are retained alternatives (design.md §16). Plate thickness and hole positions are owner-reported, not measured.",
        "",
        "| Quantity | " + " | ".join(P.VARIANTS[k].title for k in keys) + " |",
        "|---|" + "---|" * len(keys),
    ]
    for label, vals in comparison_rows(parts_by_key):
        lines.append(f"| {label} | " + " | ".join(vals[k] for k in keys) + " |")
    lines += ["", "Layout notes:", ""]
    for k in keys:
        lines.append(f"- **{P.VARIANTS[k].title}**: {P.LAYOUT_NOTE[P.VARIANTS[k].layout]}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ------------------------------------------------------------------------ main

def _render_or_record(fn, target: Path, failures: list[str], *args) -> None:
    """Delete ``target``, call ``fn(*args)`` to create it, then validate the file on disk.

    Success is recorded only if ``fn`` returns without raising AND ``target`` is a valid PNG.
    A Python exception, a VTK writer error code, a missing file, or an undecodable file are
    all recorded as failures, and nothing is left under ``target``.
    """
    try:
        target.unlink(missing_ok=True)  # never leave an old image under the name of a render that may fail
        fn(*args)
        validate_png(target)
    except Exception as exc:  # noqa: BLE001 — recorded and reported as a failed build; never substituted
        failures.append(f"{target.relative_to(OUT).as_posix()}: {exc!r}")
        try:
            target.unlink(missing_ok=True)  # a partial or invalid file is not an output either
        except OSError:
            pass


def build_variant(variant: P.Variant, failures: list[str]) -> list[Part]:
    out = OUT / variant.key
    out.mkdir(parents=True, exist_ok=True)
    parts = build_parts(variant)
    assy = build_assembly(parts, variant)
    write_step(assy, out / "heater-module.step")
    write_svg(assy, out / "isometric.svg", variant)
    write_schedule(parts, out / "member-schedule.md", variant)
    for name, direction, up, parallel, caption in VIEWS[variant.key]:
        _render_or_record(write_png, out / name, failures, parts, out / name, variant, direction, up, parallel, caption)
    for f in sorted(out.iterdir()):
        print(f"{variant.key + '/' + f.name:32s} {f.stat().st_size:>10,d} bytes")
    return parts


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--variant", choices=[*P.VARIANTS, "all"], default="all")
    args = ap.parse_args(argv)
    keys = list(P.VARIANTS) if args.variant == "all" else [args.variant]
    OUT.mkdir(exist_ok=True)
    failures: list[str] = []
    parts_by_key = {k: build_variant(P.VARIANTS[k], failures) for k in keys}
    if len(parts_by_key) == len(P.VARIANTS):
        write_comparison_md(parts_by_key, OUT / "comparison.md")
        _render_or_record(write_comparison_png, OUT / "comparison.png", failures, parts_by_key, OUT / "comparison.png")
        for name in ("comparison.md", "comparison.png"):
            if (OUT / name).exists():
                print(f"{name:32s} {(OUT / name).stat().st_size:>10,d} bytes")
    else:
        print("Comparison outputs are written only when all variants are built.")
    if failures:
        print(f"BUILD FAILED: {len(failures)} PNG render(s) failed and were removed; STEP, SVG, and schedules were written.",
              file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        return 1
    print("BUILD OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
