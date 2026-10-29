# Diesel Heater Module (002) — CAD-as-code proof of concept

**PRELIMINARY — NOT FOR FABRICATION.** This directory holds an editable, parametric placeholder model of the frame concept in [design.md](../design.md), in three layout variants for visual comparison. It exists to show that geometry and previews can be regenerated from the specification and to support design iteration in a viewer. It does not open any release gate: G1 to G5 in [spec.md §10](../spec.md#10-release-gates) remain closed, nothing here is a cut list, and nothing here demonstrates clearance, stability, or structural adequacy.

## Three layout variants

| Variant | Key | Envelope (in) | Layout | Status of the envelope |
|---|---|---|---|---|
| **A Original** | `original` | 20 × 24 × 38 | Tank entirely above the heater; heater body along X | The 2026-10-27 MR-02 envelope; superseded 2026-10-28 and retained as an alternative (design.md §16.1) |
| **B1 Compact** | `compact` | 20 × 22 × 28 | Tank beside the heater on the X-min wall; heater body along Y, plate about 7 in above ground; tank bottom about 8 in, overlapping the heater in height | Owner-proposed starting values from the 2026-10-28 brief; superseded the same day and retained as an alternative |
| **B1 Adjusted** | `adjusted` (default) | 20 × 22 × 35 | As B1 Compact, but the tank bottom is above the heater body's top by a provisional 50 mm gap (D-15) and the frame is taller; crossmember spacing derived from the owner-reported plate hole pitch; the four reported plate holes drawn as markers | **Preferred preliminary layout**, MR-02 as amended 2026-10-28 (Owner decision, preliminary; range 34 to 36 in) |

All three share the component sizes, the tank hole pattern, the 2020 (20 × 20 mm, 6 mm slot) profile (Owner decision 2026-10-29; outputs before that date used 20 × 40 mm), and the same 20-member frame concept of MR-01: four continuous uprights, three perimeter levels, two widthwise heater crossmembers, two lengthwise tank rails. The 18-member simplification discussed in design.md (D-14) is a candidate under assessment and is **not** modelled. Under the documented joint assumption every horizontal member butts face-to-face against another member at both ends; the tank rails lie in the plane of the X-min perimeter members and butt between the uprights like them, with the tank hanging on their inside face. The variants differ only in the placement values held by the `Variant` records in `params.py`. The B1 variants add a hot-air outlet direction cue at the heater's +Y end; B1 Adjusted adds four plate hole markers.

No variant resolves SR-01 (tank-above-heater instruction versus keep-away warning) or SR-02 (spill paths). In the B1 layouts the tank and heater have separate horizontal footprints; in B1 Adjusted the tank bottom is also above the heater top. **Neither horizontal separation nor the vertical gap establishes a fuel-spill, fire, or thermal clearance**, and the modelled gaps in `out/comparison.md` are bounding-box distances between placeholders, not clearances. The gap value is a placeholder for the SR-01 review.

## What the model is

- Twenty 20 × 20 mm square members with stable identifiers (`U1`, `L2-W1`, `HX2`, `TR-lower`, and so on) that appear in the Python, the member schedules, and the STEP files. For the default variant, `out/adjusted/cut-schedule.md` packs the 20 nominal lengths into 2000 mm stock: a **proposed** order-sizing estimate, not an approved cut list. No stabilization member is modelled or scheduled (excluded from the initial build, design.md §10).
- Bounding-box placeholders for the heater body (manufacturer size, C21), its mounting plate (owner tape measure; thickness an owner estimate of about 1/32 in, not measured), and the upright fuel tank (owner tape measure), plus three cylinder markers at the reported tank mounting-point spacing, a filler-neck cue near a top corner of the tank, (B1 layouts) an outlet cue at the manufacturer's outlet inner diameter (C23), and (B1 Adjusted) four markers at the owner-reported plate hole positions, 1/4 in diameter with centres 1/4 in from each adjacent edge, not measured.

Units are millimetres throughout. Inch values are converted once, in `params.py`, and nowhere else.

## What the model is not

- The extrusion is a plain box, not a T-slot profile. The heater and tank have no real shape, ports, or bosses. No exhaust, fuel line, combustion-air intake, or duct is modelled.
- Level heights, the tank's wall and height, the heater's position and orientation, the crossmember spacing (except in B1 Adjusted, where it is derived from the reported hole pitch), which plate side runs along the heater, the joint arrangement, the tank hole size, the filler corner, the filler and cap allowance, the tank gap, and the outlet end are **illustrative** or **Proposed**. Each parameter is tagged in `params.py`, and every member's row in the schedules carries a Basis column naming what its size and placement depend on. No member is presented as settled: all of them depend on the joint assumption and on evidence-tagged or illustrative values, and the rail-to-upright and member-to-member connectors are not modelled (D-01, D-02, MR-04).
- The test that bounding boxes do not overlap is a placement sanity check. It says nothing about exhaust routing, spill paths, intake separation, or interference in a real assembly.
- STEP is an interchange file. The Python source is the editable model.

## Files

| File | Role |
|---|---|
| `params.py` | Shared evidence-tagged dimensions, including the owner-reported plate holes and thickness estimate; `Variant` records `ORIGINAL`, `COMPACT`, and `ADJUSTED` (default); the joint, tank-wall, and layout assumptions in words |
| `model.py` | Builds the named parts and the CadQuery assembly for a variant |
| `build.py` | Regenerates all outputs for one or all variants and the comparison; for the default variant also the proposed cut schedule and stock packing (`cut_pieces`, `pack_stock`, `write_cut_schedule`) |
| `preview.py` | Pushes a variant to the VS Code OCP CAD Viewer |
| `tests/test_geometry.py` | Counts, sizes, orientation, member end-face contact, mounting relationships, layout relationships, STEP round trip, comparison projection, build failure handling, for both variants |
| `pyproject.toml`, `uv.lock`, `.python-version` | Pinned environment: CadQuery 2.8.0 on Python 3.12; `ocp-vscode` in the `viewer` dependency group |
| `out/original/` | A Original: `isometric.png`, `tank-side.png`, `isometric.svg`, `member-schedule.md` (committed); `heater-module.step` (generated, not committed) |
| `out/compact/` | B1 Compact: `isometric.png`, `top.png`, `front-elevation.png`, `isometric.svg`, `member-schedule.md` (committed); `heater-module.step` (not committed) |
| `out/adjusted/` | B1 Adjusted: the same five files (committed); `heater-module.step` (not committed) |
| `out/comparison.png`, `out/comparison.md` | All three variants at the same scale; envelope, component positions, headroom, and modelled bounding-box gaps side by side |

## Install and regenerate

Requires `uv` and a Python 3.12 that `uv` can find or download. Everything installs into `.venv` inside this directory; the global Python is untouched. The dependency set (OCP kernel, VTK, and their requirements) is about 1.1 GB on disk.

```text
cd specs/002-diesel-heater/cad
uv sync
uv run python build.py                     # all three variants and the comparison
uv run python build.py --variant adjusted  # one variant; comparison outputs untouched
uv run pytest
```

`build.py` prints the size of each output and ends with `BUILD OK`, exit status 0, only when every requested PNG was produced and decodes as a complete image. The PNG renders use VTK off-screen. Each PNG is deleted before its render starts; after the render the VTK writer's error code is checked and the file is opened and fully decoded with Pillow (a CadQuery dependency through matplotlib), so a writer that fails silently, a missing file, or a truncated or corrupt file all count as failures. A failed output is removed, the script still writes the STEP, SVG, and schedules, lists the failed outputs on stderr, prints `BUILD FAILED`, and exits with status 1. The same check covers the comparison image. Building one variant writes only to its own `out/<variant>/` directory. The comparison image is a parallel projection, so one millimetre is the same number of pixels for both frames.

## Viewing

- The PNGs open anywhere. The SVGs open in a browser or in VS Code's preview.
- `out/<variant>/heater-module.step` opens in FreeCAD, Onshape, Fusion, or any STEP viewer. Each component appears under its identifier; the root is named `diesel_heater_module_<variant>_PRELIMINARY`.
- To edit: change a value in `params.py` (shared constants or a `Variant` field), run `build.py`, run `pytest`.

### Interactive viewing in VS Code

The [OCP CAD Viewer](https://github.com/bernhard-42/vscode-ocp-cad-viewer) extension (tested with 4.2.0) shows the assembly in a rotatable, zoomable panel with every component listed under its identifier and drawn in its colour.

1. Install the extension, then select this directory's `.venv` as the Python interpreter (Command Palette: "Python: Select Interpreter").
2. Open the panel: Command Palette, "OCP CAD Viewer: Open Viewer".
3. In a terminal:

```text
cd specs/002-diesel-heater/cad
uv run python preview.py                     # B1 Adjusted
uv run python preview.py --variant original
uv run python preview.py --variant compact
```

Each run replaces the model in the viewer and reframes it, so switching between the commands compares the layouts. Rerun after changing `params.py` or `model.py`. Drag to rotate, scroll to zoom, right-drag to pan; the tree on the left shows or hides each component by identifier. If no viewer is open, the script says so and exits without sending anything.

Colours: grey frame members, blue heater crossmembers, green tank rails, dark plate, orange heater, cream tank and filler cue, red tank mounting-point and plate hole markers, yellow outlet cue.

The viewer dependency lives in the `viewer` dependency group of `pyproject.toml`, which `uv sync` installs by default. `build.py` and the tests never import it; `uv sync --no-group viewer` gives an environment that still regenerates STEP, SVG, PNG, and the schedules. The extension's own Quickstart setup is not needed and installs packages outside the lockfile; if it was run, `uv sync` restores the locked set.

## Checks performed by the tests

For each variant: member counts by role (4, 6, 6, 2, 2) and 20 members; unique and expected identifiers; part count (27 original, 28 compact, 32 adjusted); every part is either a member with an axis and length or a placeholder, with a basis and note; frame envelope equal to the variant's values and everything inside it; the profile is 2020 square with a 6 mm slot; every member 20 × 20 mm with the scheduled length along its stated axis; uprights full height; heater, plate, and tank at their nominal sizes with the heater body along the variant's axis; **every horizontal member's end faces coplanar with and fully inside a face of the member it butts against** (edge-only contact fails); tank rails butting between the X-min uprights with full end-face contact; plate on both crossmembers with the plate inside the crossmember's X extent and, for the illustrative-spacing variants, the crossmember inside the plate's Y extent, or, for B1 Adjusted, the crossmember centre line under the reported hole line 6.35 mm in from the plate edge with a 16.35 mm contact width; crossmembers at the middle level spanning between the depth members; heater centred on the plate; open space under the plate with nothing but the crossmembers in it; lower holes level and 173.0 mm apart; upper hole 200.0 mm above them; lower holes on the lower rail and the upper hole on the upper rail; markers passing through rail and tank; tank's broad face on the rails' inside face with each rail within the tank's height and the filler cue near its Y-min top corner; relative elevations (original: tank above the heater; compact: tank bottom between the heater's bottom and top, plate at 7 in, tank bottom at 8 in; adjusted: plate at 7 in and tank bottom above the heater top by exactly the gap parameter); outlet cue on the correct heater end at the C23 diameter; pairwise non-overlap of nominal boxes; STEP export reopens with the same number of solids, has exactly one PRODUCT per component plus the root with no extras, one assembly occurrence per component, and every re-imported solid matches some component's bounding box (these are independent checks; which name is bound to which solid is not verified yet). Build checks: schedules and comparison carry the banner and no member is marked non-provisional; the comparison image uses parallel projection and a 100 mm segment at the near and far corner of each frame projects to the same pixel length within half a pixel; a renderer that raises, one that returns without creating a file, one that writes a corrupt or truncated file, a missing or invalid comparison image, and a real VTK write to an unwritable path each return exit status 1 with nothing left under the failed name and the other outputs kept; a build whose mocked renders produce valid PNGs returns 0; the validator rejects absent, empty, and header-only files and accepts a real render. For both B1 layouts: heater length parallel to the tank's broad face; tank, plate, heater, and outlet cue footprints separate with the tank at X-min; modelled gaps positive (reported, not clearances). For B1 Adjusted only: the crossmember spacing equals the derived hole pitch (5 7/16 in minus twice 1/4 in) and the plate thickness is the 1/32 in estimate; the four hole markers sit at the reported inset from each adjacent edge, pass through the plate, and each lands on exactly one crossmember's centre line; the tank top plus the 50 mm filler and cap allowance stays below the top members and the filler cue is inside the top rectangle in plan (geometric reach only; usability is for review); the frame keeps the same 20 member identifiers as B1 Compact; the nominal lengths are 889.0 (uprights), 468.0 (widthwise), and 518.8 mm (depthwise) for the 2020 section. Cut schedule: exactly the 20 members and no foot bar, 11,450.4 mm in all; the exact packer respects the stock length and one kerf per piece and finds 6 bars where first-fit-decreasing needs 7; the written schedule carries the banner, "Proposed, not approved", and no 20 × 40 reference; the margin arithmetic of the tightest pattern (1973.6 mm in four pieces, 14.4 mm left after four 3 mm kerfs, kerf at most 6.6 mm on a full bar, s + t + 4 (k − 3) ≤ 14.4) is checked against the pattern directly, and a packing past that limit is recalculated rather than assumed to need a seventh bar. 95 tests in all.

## Observations from the illustrative placements

These are things the pictures and `out/comparison.md` make visible. They are not findings and do not change the design documents.

- **A Original**: with a 406 mm tall tank and a 140 mm tall heater on a 965 mm frame, drawing the tank entirely above the heater forces the middle level to about 350 mm. The heater body end lies 7.8 mm from the inside face of the X-max members, so there is no room along X for an outlet stub; that is why the original carries no outlet cue. The filler cue rises into the top-member band (clear of the members in plan). The tank's footprint is beside, not over, the heater's even in this layout: 43.6 mm apart along X, with a vertical gap of 24.5 mm now that the members are 20 mm deep (4.5 mm with the earlier 40 mm members).
- **B1 Compact**: the plate at 7 in puts the crossmembers' bottom face at 157.8 mm, so the middle perimeter level is low and the frame above it is open. The crossmembers span the full width and pass 25.4 mm beneath the tank. Tank-to-heater bounding-box gap along X is 236.6 mm; tank-to-plate 208.9 mm. The heater's +Y end (outlet cue) and its -Y end (where the heating-air inlet is assumed) each have about 109 mm to the inside of the 20 mm end members. Headroom from the filler cue to the top members is 61 mm. The supplied plate (138 mm along the heater) rests on crossmembers 100 mm apart, closer than the original's 130 mm, because the plate is turned with the heater.
- **B1 Adjusted**: raising the tank so its bottom is 50 mm above the heater top puts the tank at 368 to 775 mm and the rails at 428 and 628 mm, both within the uprights. At 35 in the top members start at 869 mm, leaving 94 mm above the tank top, or 44 mm after the 50 mm filler and cap placeholder, and the filler cue sits 38 mm inside the tank-wall top member in plan. With the 2020 section the depth members and rails are 518.8 mm long between 20 mm uprights, 40 mm longer than with the withdrawn 20 × 40 mm section; the width members stay 468.0 mm. The crossmembers at the derived 125.4 mm pitch each overhang the 138.1 mm plate edge by 3.65 mm so that their slot lines sit under the reported hole lines; whether the heater's underside stubs and the plate's opening clear the crossmembers at that pitch is not modelled and not assumed (design.md D-16). The tank clears the crossmembers by 190 mm and the heater body by 50 mm vertically and 237 mm horizontally; none of these is a clearance.
- Changing the plate thickness from the earlier 3 mm illustrative value to the owner's 1/32 in estimate moved the plate top, heater, and the A Original and B1 Compact gap figures by about 2.2 mm; those layouts are otherwise as before.
- Changing the section from 20 × 40 mm to 2020 on 2026-10-29 kept every plate, heater, tank, and rail height in the B1 layouts (they are set from the plate underside at 7 in), raised the underside of the top members by 20 mm, lengthened every depthwise member by 40 mm, and in A Original (whose middle level is set from the member bottom face) lowered the plate and heater by 20 mm.
- In all three, the tank rails sit in the same plane as the X-min perimeter members, so the tank's broad face is 20 mm inside the frame's outer face and the rail ends land on the uprights' inside faces. How those ends are actually connected, and whether a rail in that plane suits the tank bosses, are open (D-01, D-02, MR-04).
- In all three, which end of the heater carries the hot-air outlet and which wall the duct and exhaust leave are open (D-03, D-07, D-08, D-13); the cue only marks the end chosen for the picture.

## Licences

CadQuery is Apache 2.0. The OCP kernel wraps Open CASCADE Technology, LGPL 2.1 with exception. VTK is BSD 3-clause. Only this directory's source files are part of this repository; the dependencies live in `.venv` and are not committed.
