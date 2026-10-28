# Diesel Heater Module (002) — CAD-as-code proof of concept

**PRELIMINARY — NOT FOR FABRICATION.** This directory holds an editable, parametric placeholder model of the frame concept in [design.md](../design.md), in two layout variants for visual comparison. It exists to show that geometry and previews can be regenerated from the specification and to support design iteration in a viewer. It does not open any release gate: G1 to G5 in [spec.md §10](../spec.md#10-release-gates) remain closed, nothing here is a cut list, and nothing here demonstrates clearance, stability, or structural adequacy.

## Two layout variants

| Variant | Key | Envelope (in) | Layout | Status of the envelope |
|---|---|---|---|---|
| **A Original** | `original` | 20 × 24 × 38 | Tank entirely above the heater; heater body along X | MR-02 in spec.md (Owner decision, preliminary) |
| **B1 Compact** | `compact` | 20 × 22 × 28 | Tank beside the heater on the X-min wall; heater body along Y, raised on its plate about 7 in above ground; tank bottom about 8 in | Owner-proposed starting values from the 2026-10-28 brief; **not in spec.md or design.md**, which are unchanged |

Both variants share the component sizes, the hole pattern, the 20 × 40 mm profile, and the same 20-member frame concept: four continuous uprights, three perimeter levels, two widthwise heater crossmembers, two lengthwise tank rails. They differ only in the placement values held by the `Variant` records in `params.py`. B1 adds one part, a hot-air outlet direction cue at the heater's +Y end.

Neither variant resolves SR-01 (tank-above-heater instruction versus keep-away warning) or SR-02 (spill paths). In B1 the tank and heater have separate horizontal footprints, and the tank's lower part overlaps the heater's upper part in height only. **Horizontal separation alone establishes no fuel-spill, fire, or thermal clearance**, and the modelled gaps in `out/comparison.md` are bounding-box distances between placeholders, not clearances.

## What the model is

- Twenty 20 × 40 mm rectangular members with stable identifiers (`U1`, `L2-W1`, `HX2`, `TR-lower`, and so on) that appear in the Python, the member schedules, and the STEP files.
- Bounding-box placeholders for the heater body (manufacturer size, C21), its mounting plate (owner tape measure), and the upright fuel tank (owner tape measure), plus three cylinder markers at the reported mounting-point spacing, a filler-neck cue near a top corner of the tank, and (B1 only) an outlet cue at the manufacturer's outlet inner diameter (C23).

Units are millimetres throughout. Inch values are converted once, in `params.py`, and nowhere else.

## What the model is not

- The extrusion is a plain box, not a T-slot profile. The heater and tank have no real shape, ports, or bosses. No exhaust, fuel line, combustion-air intake, or duct is modelled.
- Level heights, the tank's wall and height, the heater's position and orientation, the crossmember spacing, which plate side runs along the heater, the joint arrangement, the hole size, the filler corner, and the outlet end are **illustrative**. Each is tagged in `params.py` and in the schedules, with the open design item it stands in for.
- The test that bounding boxes do not overlap is a placement sanity check. It says nothing about exhaust routing, spill paths, intake separation, or interference in a real assembly.
- STEP is an interchange file. The Python source is the editable model.

## Files

| File | Role |
|---|---|
| `params.py` | Shared evidence-tagged dimensions; `Variant` records `ORIGINAL` and `COMPACT`; the joint, tank-wall, and layout assumptions in words |
| `model.py` | Builds the named parts and the CadQuery assembly for a variant |
| `build.py` | Regenerates all outputs for one or both variants and the comparison |
| `preview.py` | Pushes a variant to the VS Code OCP CAD Viewer |
| `tests/test_geometry.py` | Counts, sizes, orientation, mounting relationships, layout relationships, STEP round trip, for both variants |
| `pyproject.toml`, `uv.lock`, `.python-version` | Pinned environment: CadQuery 2.8.0 on Python 3.12; `ocp-vscode` in the `viewer` dependency group |
| `out/original/` | A Original: `isometric.png`, `tank-side.png`, `isometric.svg`, `member-schedule.md` (committed); `heater-module.step` (generated, not committed) |
| `out/compact/` | B1 Compact: `isometric.png`, `top.png`, `front-elevation.png`, `isometric.svg`, `member-schedule.md` (committed); `heater-module.step` (not committed) |
| `out/comparison.png`, `out/comparison.md` | Both variants at the same scale; envelope, component positions, and modelled bounding-box gaps side by side |

## Install and regenerate

Requires `uv` and a Python 3.12 that `uv` can find or download. Everything installs into `.venv` inside this directory; the global Python is untouched. The dependency set (OCP kernel, VTK, and their requirements) is about 1.1 GB on disk.

```text
cd specs/002-diesel-heater/cad
uv sync
uv run python build.py                     # both variants and the comparison
uv run python build.py --variant compact   # one variant; comparison outputs untouched
uv run pytest
```

`build.py` prints the size of each output. The PNG renders use VTK off-screen; if that fails on a machine, the script reports the failure and still writes the STEP, SVG, and schedules. Building one variant writes only to its own `out/<variant>/` directory.

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
uv run python preview.py --variant original
uv run python preview.py --variant compact
```

Each run replaces the model in the viewer and reframes it, so switching between the two commands compares the layouts. Rerun after changing `params.py` or `model.py`. Drag to rotate, scroll to zoom, right-drag to pan; the tree on the left shows or hides each component by identifier. If no viewer is open, the script says so and exits without sending anything.

Colours: grey frame members, blue heater crossmembers, green tank rails, dark plate, orange heater, cream tank and filler cue, red mounting-point markers, yellow outlet cue.

The viewer dependency lives in the `viewer` dependency group of `pyproject.toml`, which `uv sync` installs by default. `build.py` and the tests never import it; `uv sync --no-group viewer` gives an environment that still regenerates STEP, SVG, PNG, and the schedules. The extension's own Quickstart setup is not needed and installs packages outside the lockfile; if it was run, `uv sync` restores the locked set.

## Checks performed by the tests

For each variant: member counts by role (4, 6, 6, 2, 2) and 20 members; unique and expected identifiers; part count (27 original, 28 compact); frame envelope equal to the variant's values and everything inside it; every member 20 × 40 mm with the length the schedule reports; uprights full height; heater, plate, and tank at their nominal sizes with the heater body along the variant's axis; plate resting on both crossmembers, crossmembers at the middle level spanning between the depth members; heater centred on the plate; open space under the plate with nothing but the crossmembers in it; lower holes level and 173.0 mm apart; upper hole 200.0 mm above them; lower holes on the lower rail and the upper hole on the upper rail; markers passing through rail and tank; rails spanning between uprights; tank upright against the X-min rails with the filler cue near its Y-min top corner; relative elevations (original: tank above the heater; compact: tank bottom between the heater's bottom and top, plate at 7 in, tank bottom at 8 in); outlet cue on the correct heater end at the C23 diameter; pairwise non-overlap of nominal boxes; STEP export reopens with the same number of solids and keeps every component name; schedules and comparison carry the banner. For B1 only: heater length parallel to the tank's broad face; tank, plate, heater, and outlet cue footprints separate with the tank at X-min; modelled gaps positive (reported, not clearances).

## Observations from the illustrative placements

These are things the pictures and `out/comparison.md` make visible. They are not findings and do not change the design documents.

- **A Original**: with a 406 mm tall tank and a 140 mm tall heater on a 965 mm frame, drawing the tank entirely above the heater forces the middle level to about 350 mm. The heater body end lies 7.8 mm from the inside face of the X-max members, so there is no room along X for an outlet stub; that is why the original carries no outlet cue. The filler cue rises into the top-member band (clear of the members in plan). The tank's footprint is beside, not over, the heater's even in this layout; the vertical gap between them is 2.3 mm.
- **B1 Compact**: the plate at 7 in puts the crossmembers' bottom face at 137.8 mm, so the middle perimeter level is low and the frame above it is open. The crossmembers span the full width and pass 25.4 mm beneath the tank. Tank-to-heater bounding-box gap along X is 216.6 mm; tank-to-plate 188.9 mm. The heater's +Y end (outlet cue) and its -Y end (where the heating-air inlet is assumed) each have about 89 mm to the inside of the end members. Headroom from the filler cue to the top members is 41 mm. The supplied plate (138 mm along the heater) rests on crossmembers 100 mm apart, closer than the original's 130 mm, because the plate is turned with the heater.
- In both, which end of the heater carries the hot-air outlet and which wall the duct and exhaust leave are open (D-03, D-07, D-08, D-13); the cue only marks the end chosen for the picture.

## Licences

CadQuery is Apache 2.0. The OCP kernel wraps Open CASCADE Technology, LGPL 2.1 with exception. VTK is BSD 3-clause. Only this directory's source files are part of this repository; the dependencies live in `.venv` and are not committed.
