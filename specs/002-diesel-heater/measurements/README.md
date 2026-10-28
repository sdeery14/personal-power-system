# Diesel Heater Module (002) — Measurement records

**Status: measurement workstream, started 2026-10-28. No record exists yet.** This directory holds dated records of physical measurements of the owner's VEVOR XMZ-D2 heater, its mounting plate, its 10 L tank, and the supplied parts. A record here is what turns a value from User-reported or Unknown into **Measured** in [spec.md](../spec.md), [design.md](../design.md), [bom.md](../bom.md), and the CAD model under [cad/](../cad/). A record never makes anything Verified, never establishes a clearance, and never opens a release gate. G1 to G5 in [spec.md §10](../spec.md#10-release-gates) stay closed.

The measurements are static. The heater is not powered, fuelled, or run for any of them.

## 1. Files

| File | Role |
|---|---|
| `README.md` | This file: workflow, evidence rules, datum conventions, identifier scheme, recording instructions |
| [`checklist.md`](checklist.md) | The prioritized list of what to measure, with the permanent measurement identifiers |
| [`template.md`](template.md) | Blank record. Copy it for each measuring session |
| `YYYY-MM-DD-<group>.md` | One record per session and component group, for example `2026-11-02-heater-plate.md`. None exist yet |

Photographs are held in the owner's own archive and are referred to by identifier only. No photograph is committed.

## 2. Workflow

1. Pick the next group from [checklist.md](checklist.md), in priority order unless there is a reason not to.
2. Set the component up on its datum as described in §5. Put a small piece of masking tape marked `0` at the datum corner or edge and photograph it with the component, so the record and the photographs agree about which edge is which.
3. Copy `template.md` to `YYYY-MM-DD-<group>.md` with the date of the measuring session.
4. Fill in the header: date, who measured, the datum name, how the component was set up, and every instrument with its resolution.
5. For each identifier in the group, write the reading **exactly as read** from the instrument, its unit, the instrument, a plus-or-minus figure (§4), the surfaces the reading was taken between, and the photograph identifier if there is one. Leave a row blank, with a reason, rather than estimate it.
6. Record anything you noticed that is not a number (a membrane, a rib, a label, a part already assembled) in the observations list.
7. List what was in the group but not measured, and why.
8. Commit the record on a `002-` work branch. Tell the planning coordinator which identifiers now have readings. A later, separately approved increment moves the affected rows in `spec.md`, `design.md`, `bom.md`, and `cad/params.py` to Measured with the record file and identifier as the reference. Records are not back-filled into those documents automatically.

Keep the record honest about its limits. A reading taken with the heater already fastened to the plate, or with a part partly assembled, is still a reading; say so in the setup notes.

## 3. Evidence rules for this directory

The repository's evidence tags are in [CLAUDE.md](../../../CLAUDE.md). For this directory:

| Tag | What it takes here |
|---|---|
| **Measured** | A reading in a dated record with the instrument, its resolution, the reference surfaces, and who took it |
| **Manufacturer-stated** | A figure from M1 or M2 as cited in [spec.md §2](../spec.md#2-manufacturer-sources). A measurement that agrees with it is still recorded separately; the two are not merged |
| **User-reported** | The earlier tape-measure figures (plate 5 7/16 × 6 11/16 in, tank about 16 × 16 × 3 in, lower holes 6 13/16 in apart, upper hole 7 7/8 in above). They stay User-reported until the same feature appears in a record. They are not copied into a record as if they had been read in a session |
| **Illustrative** | Values the CAD model needed to draw a picture (plate thickness, hole diameter, filler position, every placement). None of them is evidence of anything, and none of them is to be written into a record |
| **Verified** | Not available from this workflow. Verification is an independent confirmation after the fact, with its own dated record |

Rules that follow:

- **No guessed values.** A record contains readings taken in that session and nothing else. A blank cell with "not measured" is correct; a plausible number is not.
- **No silent promotion.** The earlier tape figures do not become Measured because they are close to a new reading. The new reading is recorded under its identifier and the old figure is retired by the later document update, which cites the record.
- **Fit is not safety.** A stub that passes through an opening, a pipe that reaches a wall, a tank that clears a member: each is a geometric fact and nothing more. None of them says anything about thermal, fire, exhaust, carbon-monoxide, structural, or electrical safety. SR-01, SR-02, SR-04, SR-10, SR-11, MR-04, and MR-05 stay open regardless of what is measured.
- **Observed is not approved.** How far a pipe bends by hand, which way a pump happens to be oriented in its sheath, or how the heater happens to sit on its plate are observations. The manufacturer's bend radius, pump angle and lift, orientation and tilt limits, clearance distances, and boss rating are not measurable here and come only from VEVOR or an engineering review (Q-04, Q-05, Q-06, Q-08, Q-11). A record never states or implies one of these.
- **No assumption about the plate opening.** Whether each underside stub passes through the plate opening, through a hole, or lies outside the plate outline is recorded per stub. Until then the relationship is Unknown.
- **No readings from a running, powered, or fuelled heater.** Everything in this directory is measured cold and disconnected. Nothing here is a test.

## 4. Instruments, resolution, units, and uncertainty

Three instruments cover the checklist: a tape measure, a steel rule, and digital calipers. Record which was used for every reading.

| Instrument | Use it for | Resolution to record | Plus-or-minus to record unless you have a reason to widen it |
|---|---|---|---|
| Digital calipers | Diameters, thicknesses, hole and recess sizes, short distances up to the jaw length | What the display shows, usually 0.01 mm or 0.0005 in; record to 0.1 mm or 1/64 in, never finer | ±0.1 mm on a hard, clean feature; ±0.5 mm on plastic, a curved surface, a soft seal, or anything the jaws can compress |
| Steel rule | Distances from an edge to a feature under about 300 mm | 1 mm or 1/32 in | ±0.5 mm (or ±1/32 in) between two hard edges; ±1 mm when one end is the middle of a hole or a stub |
| Tape measure | Overall sizes, pipe lengths, cable lengths | 1 mm or 1/16 in | ±1 mm (or ±1/16 in) between two hard edges; ±2 mm when hooking the tape on a rounded edge or sighting a centre |

**Units.** Write the reading in the unit the instrument displayed. Do not convert in the record. Conversions happen once, in `cad/params.py`, where inches are multiplied by 25.4 and nowhere else. If a converted figure helps you on the day, put it in the Notes column, labelled "converted", not in the Reading column.

**Centres.** To locate the centre of a hole, stub, or boss from a datum edge, measure from the edge to the near side of the feature and to the far side, record both, and let the centre be the mean and the width be the difference. Cross-check the width with calipers across the feature. Record all three numbers, not only the centre.

**Repeats.** Anything the design hangs on (stub positions, plate holes, boss positions, filler height) is measured twice from the datum, with the component lifted and re-seated between readings. Record both readings. If they differ by more than the plus-or-minus figure in the table, widen the plus-or-minus to cover both and say why.

**Setup.** Write down what the component was resting on, whether it was level, whether anything was fastened, and anything that prevented a clean reading (a seal in the way, a part already fitted, a hole you could not see into).

## 5. Datum conventions

Every reading is taken from a named datum so it can be transferred into the CAD model without guessing. The datums are local to each component. How a component sits in the frame is a separate placement decision held in `cad/params.py`; nothing here fixes it.

### 5.1 HP: heater and mounting plate

Used for every heater and plate feature, including the underside stubs.

- The heater is seated on its plate as supplied, with whatever seal or fixing is already in place. The setup notes say whether the heater is fastened to the plate, whether the seal is fitted, and whether anything was loosened to take a reading. Do not disassemble anything only to measure it; if you choose to, record it.
- **Z = 0 is the plate's underside**, the face that would rest on the frame crossmembers. Z is positive upward, into the heater. A stub protruding below the plate is recorded as "protrusion below the plate underside" with its magnitude, so there are no signs to get wrong.
- **Corner 0** is one corner of the plate, marked with tape. **X runs along the longer plate edge** from corner 0, and **Y runs along the shorter plate edge** from corner 0. The record says which physical corner was chosen (for example "the corner nearest the heater's hot-air outlet, on the side of the exhaust stub") and the photograph shows the tape.
- Every heater feature is located by its X and Y from the two plate edges that meet at corner 0, and its Z from the plate underside. The heater body itself is located the same way: the X of each end face and the Y of each side face, measured from the plate edges, give the heater's position on the plate and its length and width in the same frame.
- The plate's own features (outline, thickness, fixing holes, underside opening) are recorded in the same frame. The holes are numbered H1 to H4 starting at the hole nearest corner 0 and going around the plate clockwise when viewed from above.
- If the plate is not a rectangle, or has a flange, bend, or tab, describe it in the observations and choose the two straight edges that meet at a corner as the X and Y edges, saying which.

### 5.2 TK: fuel tank

Used for every tank feature: outer shape, bosses, filler, fuel outlet.

- The tank stands upright on its bottom face on a flat, level surface, empty, with its cap on unless a reading says otherwise. The broad face with the three recessed mounting points is the **mounting face** and is vertical.
- **Z = 0 is the surface the tank stands on.** Z is positive upward.
- **Y runs horizontally along the mounting face** from the tank's **left vertical edge as seen by someone facing the mounting face**. Mark that edge with tape labelled `L` and photograph it.
- **X is perpendicular to the mounting face**, zero at the mounting face itself, positive into the tank body, away from where the frame would be. Thickness readings and the filler position across the tank are X readings.
- The three mounting points are **B1 (lower left), B2 (lower right), and B3 (upper)**, as seen facing the mounting face. Each is located by the Y and Z of its centre. If the mounting face is not flat enough to define X = 0 cleanly (ribs, draft, a recessed panel), say what was used as the reference plane.
- Features on the top face (filler neck, vent, anything else) are located by Y from the left edge and X from the mounting face, with their heights given as Z above the standing surface and, separately, as height above the local top face.

### 5.3 Loose parts

The exhaust pipe, silencer, intake pipe, air filter, fuel pump and sheath, oil filter, oil pipe, blowpipe, rotary tuyere, clamps, power cord, controller, and harness have no datum frame. They are recorded by overall dimensions: lengths, outside and inside diameters, barb and stub diameters, mounting-hole sizes, and the lengths of cables between their ends. Say which end is which when it matters (the pump has an inlet and an outlet; the silencer has an inlet and an outlet).

### 5.4 Masses

Masses are recorded with the scale used, its resolution, a note that it read zero with nothing on it, and exactly what was on the scale (for example "heater body with its seal, without the plate, without the exhaust pipe"). The heater and the tank are weighed separately. The tank is weighed empty.

## 6. Identifiers

Each feature has a permanent identifier of the form `<GROUP>-<nn>`, assigned in [checklist.md](checklist.md). The identifier is the link between a record, the documents that cite it, and the CAD parameter that consumes it.

| Group | Covers |
|---|---|
| `PLT` | Mounting plate: outline, thickness, fixing holes, underside opening, seal |
| `HTR` | Heater body on its plate: extents, position on the plate, hot-air outlet, heating-air inlet, underside stubs, cable exits |
| `EXH` | Exhaust pipe, silencer, silencer fixing piece, exhaust clamps |
| `TNK` | Fuel tank: outer shape, bosses, filler neck and cap, fuel outlet, other features |
| `PMP` | Pulse fuel pump, its sheath and screw, its cable |
| `FLT` | Oil filter |
| `FUL` | Oil pipe, oil pipe clips, cable ties |
| `INT` | Combustion-air intake pipe and air filter element |
| `DUC` | Blowpipe, blowpipe clamps, rotary tuyere |
| `ELC` | Power cord, in-line fuse and holder, controller, harness, remote |
| `MAS` | Masses |
| `DOC` | Paper manual revision and differences from M1; inventory against the packing list; assembly state found |

Rules:

- Identifiers are never renumbered or reused. A feature that turns out not to exist keeps its identifier with "not present" in the record.
- A feature measured again in a later session keeps its identifier; the new record is a new file. The most recent record governs, and the later document update says which record it cites.
- A feature the checklist did not anticipate takes the next free number in its group, added to `checklist.md` in the same commit as the record.
- Non-numeric observations (a membrane, a marking, a direction) use the same identifiers as the features they describe.

Photograph identifiers are `P-YYYYMMDD-nn`, assigned by the owner in the owner's archive. A record cites them; the repository never holds them.

## 7. Priorities

The order in `checklist.md` follows the Phase 2 assessment of 2026-10-28:

1. **Priority 1, feasibility of the B1 Compact layout and the plate interface**: the plate, the heater on its plate including its underside stubs, the exhaust pipe and silencer, and the tank's outer shape and filler. These decide whether the exhaust can leave the heater downward and run horizontally or down within the lower level, and whether the tank fits the proposed envelope.
2. **Priority 2, the frame concept**: the heater's end faces and inlet, the tank bosses and fuel outlet, the pump and filter, and the masses.
3. **Priority 3, later gates**: intake pipe and filter, blowpipe and tuyere, electrical parts, the paper manual.

The first session is Priority 1 for the heater, plate, and exhaust. The tank is the second session.

## 8. What these records change, and what they do not

- They change the evidence tag of specific figures, through a later documented update, from User-reported or Unknown to Measured.
- They let the CAD model draw real features (plate opening and holes, stubs, inlet, filler, bosses, fuel outlet) in place of cues, in a later, separately approved increment that preserves both the A Original and B1 Compact layouts.
- They do not select any fastener, extrusion length, clamp, or component; do not derive a cut length; do not resolve SR-01 or SR-02; do not set any clearance; do not establish the suitability of the tank bosses (MR-04); do not confirm any orientation, angle, bend radius, or lift (Q-06, Q-08); and do not change the heater's governing specification. Those remain for VEVOR, engineering review, and the owner.
