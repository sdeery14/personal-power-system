# Diesel Heater Module (002) — CAD-as-code proof of concept

**PRELIMINARY — NOT FOR FABRICATION.** This directory holds an editable, parametric placeholder model of the frame concept in [design.md](../design.md). It exists to show that geometry and previews can be regenerated from the specification. It does not open any release gate: G1 to G5 in [spec.md §10](../spec.md#10-release-gates) remain closed, nothing here is a cut list, and nothing here demonstrates clearance, stability, or structural adequacy.

## What the model is

- Twenty 20 × 40 mm rectangular members: four continuous uprights, three perimeter levels of four, two heater crossmembers at the middle level, two tank rails on one inside wall (MR-01).
- Bounding-box placeholders for the heater body (manufacturer size, C21), its mounting plate (owner tape measure), and the upright fuel tank (owner tape measure), plus three cylinder markers at the reported mounting-point spacing and a filler-neck cue.
- Every part has a stable identifier (`U1`, `L2-W1`, `HX2`, `TR-lower`, `fuel_tank`, `tank_hole_upper`, and so on) that appears in the Python, the member schedule, and the STEP file.

Units are millimetres throughout. Inch values from the specification are converted once, in `params.py`, and nowhere else.

## What the model is not

- The extrusion is a plain box, not a T-slot profile. The heater and tank have no real shape, ports, or bosses.
- Level heights, the tank's wall and height, the heater's position along the frame, the crossmember spacing, the joint arrangement, and the hole size are **illustrative**. Each is tagged `illustrative` in `params.py` and in the schedule, with the open design item it stands in for.
- The tank is drawn entirely above the heater only to picture the manufacturer's instruction (C12). That placement does **not** address the keep-away warning (C1); SR-01 stays unreconciled.
- The test that bounding boxes do not overlap is a placement sanity check. It says nothing about exhaust routing, spill paths, intake separation, or interference in a real assembly.
- STEP is an interchange file. A receiving CAD application gets geometry only, not an editable feature history. The Python source is the editable model.

## Files

| File | Role |
|---|---|
| `params.py` | Every dimension, evidence-tagged; the joint and tank-wall assumptions in words |
| `model.py` | Builds the named parts and the CadQuery assembly |
| `build.py` | Regenerates all outputs |
| `tests/test_geometry.py` | Counts, nominal sizes, mounting relationships, STEP round trip |
| `pyproject.toml`, `uv.lock`, `.python-version` | Pinned environment: CadQuery 2.8.0 on Python 3.12 |
| `out/isometric.png`, `out/tank-side.png`, `out/isometric.svg`, `out/member-schedule.md` | Committed outputs |
| `out/heater-module.step` | Generated on demand; not committed |

## Install and regenerate

Requires `uv` and a Python 3.12 that `uv` can find or download. Everything installs into `.venv` inside this directory; the global Python is untouched. The dependency set (OCP kernel, VTK, and their requirements) is about 1.1 GB on disk.

```text
cd specs/002-diesel-heater/cad
uv sync
uv run python build.py
uv run pytest
```

`build.py` prints the size of each output. The PNG renders use VTK off-screen; if that fails on a machine, the script reports the failure and still writes the STEP, SVG, and schedule.

## Viewing

- `out/isometric.png` and `out/tank-side.png` open anywhere. The SVG opens in a browser or in VS Code's preview.
- `out/heater-module.step` opens in FreeCAD, Onshape, Fusion, or any STEP viewer. Each component appears under its identifier. Nothing here installs a viewer.
- To edit: change a value in `params.py`, run `build.py`, run `pytest`.

## Checks performed by the tests

Member counts by role (4, 6, 6, 2, 2); unique and expected identifiers; envelope 508 × 609.6 × 965.2 mm from the origin; every member 20 × 40 mm with the length the schedule reports; uprights full height; heater, plate, and tank at their nominal sizes; plate resting on both crossmembers; heater resting on the plate; lower holes level and 173.0 mm apart; upper hole 200.0 mm above them; lower holes on the lower rail and the upper hole on the upper rail; markers passing through rail and tank; tank upright with the filler at the top; pairwise non-overlap of nominal boxes; STEP export reopens with the same number of solids and keeps every component name.

## Observations from the illustrative placement

These are things the picture makes visible. They are not findings and do not change the design documents.

- With a 406 mm tall tank and a 140 mm tall heater on a 965 mm frame, drawing the tank entirely above the heater forces the middle level low: here at 350 mm, with the tank bottom at 535 mm and its filler neck just under the top members. Any higher middle level would push the tank above the envelope or beside the heater.
- The crossmembers span the full inside width and pass under the tank's wall zone. Whether that is wanted depends on D-07 (exhaust exit side) and D-03 (tank wall).

## Licences

CadQuery is Apache 2.0. The OCP kernel wraps Open CASCADE Technology, LGPL 2.1 with exception. VTK is BSD 3-clause. Only this directory's source files are part of this repository; the dependencies live in `.venv` and are not committed.
