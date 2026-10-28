"""Regenerate every output of the PRELIMINARY Diesel Heater Module (002) model.

    uv run python build.py

Writes to ./out: heater-module.step (not committed), isometric.svg,
isometric.png, tank-side.png, member-schedule.md. PRELIMINARY — NOT FOR FABRICATION.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import cadquery as cq

import params as P
from model import BANNER, build_assembly, build_parts, members

OUT = Path(__file__).parent / "out"


def write_step(assy: cq.Assembly, path: Path) -> None:
    assy.export(str(path))


def write_svg(assy: cq.Assembly, path: Path, direction=(1.0, 1.0, 0.75)) -> None:
    cq.exporters.export(
        assy.toCompound(), str(path), exportType="SVG",
        opt={"width": 1000, "height": 800, "marginLeft": 20, "marginTop": 20,
             "projectionDir": direction, "showAxes": True, "strokeWidth": 0.8,
             "showHidden": False},
    )
    text = path.read_text(encoding="utf-8")
    label = (f'<text x="20" y="30" font-family="sans-serif" font-size="22" fill="#c00000">'
             f'{BANNER} — bounding-box placeholders, illustrative placement</text>\n')
    open_tag_end = text.index(">", text.index("<svg")) + 1  # end of the opening <svg ...> tag
    path.write_text(text[:open_tag_end] + "\n" + label + text[open_tag_end:], encoding="utf-8")


def write_png(parts, path: Path, view_from=(1.0, -1.0, 0.8), caption="") -> None:
    """Shaded render through VTK's off-screen renderer, camera looking from ``view_from``."""
    import vtk  # provided by the cadquery dependency set

    ren = vtk.vtkRenderer()
    ren.SetBackground(1, 1, 1)
    for p in parts:
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(p.shape.toVtkPolyData(0.5, 0.2))
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(*p.color)
        actor.GetProperty().EdgeVisibilityOn()
        actor.GetProperty().SetEdgeColor(0.2, 0.2, 0.2)
        ren.AddActor(actor)
    banner = vtk.vtkTextActor()
    banner.SetInput(f"{BANNER}\nBounding-box placeholders; illustrative placement; gates G1-G5 closed\n{caption}")
    banner.GetTextProperty().SetFontSize(26)
    banner.GetTextProperty().SetColor(0.75, 0, 0)
    banner.SetPosition(20, 1500)
    ren.AddViewProp(banner)
    cam = ren.GetActiveCamera()
    cam.SetPosition(*view_from)
    cam.SetFocalPoint(0, 0, 0)
    cam.SetViewUp(0, 0, 1)
    ren.ResetCamera()  # frame the whole model for this direction
    win = vtk.vtkRenderWindow()
    win.SetOffScreenRendering(1)
    win.AddRenderer(ren)
    win.SetSize(1400, 1600)
    win.Render()
    w2i = vtk.vtkWindowToImageFilter()
    w2i.SetInput(win)
    w2i.Update()
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(str(path))
    writer.SetInputConnection(w2i.GetOutputPort())
    writer.Write()


def write_schedule(parts, path: Path) -> None:
    lines = [
        f"# Member schedule — {BANNER}",
        "",
        f"Generated {dt.date.today().isoformat()} by `build.py` from `params.py`. All lengths in millimetres, nominal, as modelled.",
        "",
        "**This is not a cut list.** Every length depends on the joint assumption below, which the design has not chosen (D-01, D-02), and on illustrative level heights and tank position. Gates G1–G5 in spec.md §10 are closed.",
        "",
        f"Joint assumption: {P.JOINT_ASSUMPTION}",
        "",
        f"Tank assumption: {P.TANK_WALL_ASSUMPTION}",
        "",
        "| ID | Role | Axis | Nominal length (mm) | Section (mm) | Illustrative placement | Note |",
        "|---|---|---|---|---|---|---|",
    ]
    for p in members(parts):
        lines.append(f"| {p.id} | {p.role} | {p.axis} | {p.length:.1f} | {P.PROFILE_MINOR:.0f} × {P.PROFILE_MAJOR:.0f} | "
                     f"{'yes' if p.illustrative else 'no'} | {p.note} |")
    lines += [
        "",
        f"Members: {len(members(parts))}. Other components (placeholders): "
        + ", ".join(p.id for p in parts if p.role not in ("upright", "perimeter_width", "perimeter_depth", "heater_crossmember", "tank_rail"))
        + ".",
        "",
        "## Parameters",
        "",
        "| Parameter | Value (mm) | Tag | Source |",
        "|---|---|---|---|",
    ]
    for q in P.PARAMS:
        lines.append(f"| {q.name} | {q.value:.1f} | {q.tag} | {q.source} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    parts = build_parts()
    assy = build_assembly(parts)
    write_step(assy, OUT / "heater-module.step")
    write_svg(assy, OUT / "isometric.svg")
    write_schedule(parts, OUT / "member-schedule.md")
    views = [
        ("isometric.png", (1.0, -1.0, 0.8), "View from +X/-Y: heater (orange) on crossmembers (blue); tank (cream) on rails (green) at the far wall"),
        ("tank-side.png", (-1.0, -1.0, 0.7), "View from -X/-Y: tank wall; red marks are the three reported mounting points on the rails"),
    ]
    for name, direction, caption in views:
        try:
            write_png(parts, OUT / name, direction, caption)
        except Exception as exc:  # report, never substitute
            print(f"PNG render failed for {name}: {exc!r}")
    for f in sorted(OUT.iterdir()):
        print(f"{f.name:22s} {f.stat().st_size:>10,d} bytes")


if __name__ == "__main__":
    main()
