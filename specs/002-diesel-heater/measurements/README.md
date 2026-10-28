# Diesel Heater Module (002) — Measurement records

**Status: measurement workstream, started 2026-10-28. No record exists yet.** This directory holds dated records of physical measurements of the owner's VEVOR XMZ-D2 heater, its mounting plate, its 10 L tank, and the supplied parts. A record here is what turns a value from User-reported or Unknown into **Measured** in [spec.md](../spec.md), [design.md](../design.md), [bom.md](../bom.md), and the CAD model under [cad/](../cad/). A record never makes anything Verified, never establishes a clearance, and never opens a release gate. G1 to G5 in [spec.md §10](../spec.md#10-release-gates) stay closed.

The measurements are static. The heater is not powered, fuelled, or run for any of them.

## 1. Files

| File | Role |
|---|---|
| `README.md` | This file: workflow, evidence rules, instruments and uncertainty, datum conventions, identifier scheme, repeated and conflicting records |
| [`checklist.md`](checklist.md) | The prioritized list of what to measure, with the permanent measurement identifiers |
| [`template.md`](template.md) | Blank record. Copy it for each measuring session |
| `YYYY-MM-DD-<group>.md` | One record per session and component group, for example `2026-11-02-heater-plate.md`. None exist yet |

Photographs are held in the owner's own archive and are referred to by identifier only. No photograph is committed.

## 2. Workflow

1. Pick the next group from [checklist.md](checklist.md), in priority order unless there is a reason not to. A session may stop after one subgroup (Session 1a alone, for example). An incomplete group is fine when the unmeasured identifiers are listed with a reason.
2. Set the component up on its datum as described in §5. Put a small piece of masking tape marked `0` at the datum corner or edge and photograph it with the component, so the record and the photographs agree about which edge is which.
3. Copy `template.md` to `YYYY-MM-DD-<group>.md` with the date of the measuring session.
4. Fill in the header: date, who measured, the datum name, how the component was set up, every instrument with its resolution, and (for HP sessions) which plate axis the heater length runs along, once PLT-14 has been observed.
5. For each identifier in the group, write every reading **exactly as the instrument displayed it** in the raw-readings table, with its unit, the instrument, the instrument's resolution, a provisional plus-or-minus figure (§4), and the two surfaces the reading was taken between, including the axis and its sign. Leave a row blank, with a reason, rather than estimate it.
6. Put anything worked out from readings (a centre, a width, a difference, a converted unit) in the calculated-values table, naming the raw rows it came from and how. Never in the raw table.
7. Record anything you noticed that is not a number (a membrane, a rib, a label, a part already assembled) in the observations list.
8. List what was in the group but not measured, and why.
9. If an identifier was measured in an earlier record, compare and note agreement or discrepancy in the discrepancies section (§7).
10. Commit the record on a `002-` work branch. Tell the planning coordinator which identifiers now have readings. A later, separately approved increment moves the affected rows in `spec.md`, `design.md`, `bom.md`, and `cad/params.py` to Measured with the record file and identifier as the reference. Records are not back-filled into those documents automatically.

Keep the record honest about its limits. A reading taken with the heater already fastened to the plate, or with a part partly assembled, is still a reading; say so in the setup notes.

## 3. Evidence rules for this directory

The repository's evidence tags are in [CLAUDE.md](../../../CLAUDE.md). For this directory:

| Tag | What it takes here |
|---|---|
| **Measured** | A reading in a dated record with the instrument, its resolution, the reference surfaces, and who took it |
| **Manufacturer-stated** | A figure from M1 or M2 as cited in [spec.md §2](../spec.md#2-manufacturer-sources). A measurement that agrees with it is still recorded separately; the two are not merged |
| **User-reported** | The earlier tape-measure figures (plate 5 7/16 × 6 11/16 in, tank about 16 × 16 × 3 in, lower holes 6 13/16 in apart, upper hole 7 7/8 in above). They stay User-reported until the same feature appears in a record. They are not copied into a record as if they had been read in a session |
| **Illustrative** | Values the CAD model needed to draw a picture (plate thickness, hole diameter, filler position, every placement, and which plate edge the heater runs along). None of them is evidence of anything, and none of them is to be written into a record or used to decide a datum |
| **Verified** | Not available from this workflow. Verification is an independent confirmation after the fact, with its own dated record |

Rules that follow:

- **No guessed values.** A record contains readings taken in that session and nothing else. A blank cell with "not measured" is correct; a plausible number is not.
- **No silent promotion.** The earlier tape figures do not become Measured because they are close to a new reading. The new reading is recorded under its identifier and the old figure is retired by the later document update, which cites the record.
- **Raw is raw.** A reading is written as displayed. Anything calculated from readings is kept apart and traceable to them (§4).
- **Fit is not safety.** A stub that passes through an opening, a pipe that reaches a wall, a tank that clears a member: each is a geometric fact and nothing more. None of them says anything about thermal, fire, exhaust, carbon-monoxide, structural, or electrical safety. SR-01, SR-02, SR-04, SR-10, SR-11, MR-04, and MR-05 stay open regardless of what is measured.
- **Observed is not approved.** How far a pipe bends by hand, which way a pump happens to be oriented in its sheath, or how the heater happens to sit on its plate are observations. The manufacturer's bend radius, pump angle and lift, orientation and tilt limits, clearance distances, and boss rating are not measurable here and come only from VEVOR or an engineering review (Q-04, Q-05, Q-06, Q-08, Q-11). A record never states or implies one of these.
- **No assumption about the plate opening.** Whether each underside stub passes through the plate opening, through a hole, or lies outside the plate outline is recorded per stub. Until then the relationship is Unknown.
- **No assumption about the heater's orientation.** Which plate edge the heater length runs along is an observation (PLT-14), not something taken from the CAD model, which only drew one possibility.
- **No readings from a running, powered, or fuelled heater.** Everything in this directory is measured cold and disconnected. Nothing here is a test.

## 4. Instruments, resolution, uncertainty, units, and calculated values

Three instruments cover the checklist: a tape measure, a steel rule, and digital calipers. Record which was used for every reading.

**Raw readings.** Write the number exactly as the instrument displayed it, in the unit it displayed, with all the digits it showed. Calipers showing `22.63 mm` are recorded as `22.63`, not `22.6`. A tape read as `13 7/16 in` is recorded as `13 7/16`. Do not round, convert, or average in the raw table.

**Resolution and uncertainty are two different columns.**

- *Resolution* is what the instrument can display or what its finest marking is: 0.01 mm or 0.0005 in for typical digital calipers, 1 mm or 1/32 in for a steel rule, 1 mm or 1/16 in for a tape. It is a property of the instrument and is copied from it.
- *Provisional ±* is your estimate, on the day, of how far the true dimension might be from the reading, given the instrument, how well the datum could be held, and the feature. It is an estimate for later users of the value. It is **not** a statement of instrument accuracy, and none of the instruments is calibrated. The table below gives starting figures; widen them whenever the setup was worse than the description, and say why in the Notes.

| Instrument | Use it for | Starting provisional ± |
|---|---|---|
| Digital calipers | Diameters, thicknesses, hole and recess sizes, short distances up to the jaw length | ±0.1 mm on a hard, clean feature; ±0.5 mm on plastic, a curved surface, a soft seal, or anything the jaws can compress |
| Steel rule | Distances from an edge to a feature under about 300 mm | ±0.5 mm (or ±1/32 in) between two hard edges; ±1 mm when one end is the edge of a hole or a round stub |
| Tape measure | Overall sizes, pipe lengths, cable lengths | ±1 mm (or ±1/16 in) between two hard edges; ±2 mm when hooking the tape on a rounded edge |

**Repeats.** Anything the design hangs on (stub positions, plate holes, boss positions, filler height) is measured twice from the datum, with the component lifted and re-seated between readings. Both readings are kept, written in the same cell separated by a slash (`41.0 / 41.5`). Two readings that agree show the setup was repeatable; they do not show the reading is accurate, and the provisional ± is not reduced because of them. If the repeats differ by more than the provisional ±, widen it to cover both and say why.

**Calculated values.** A centre, a width taken as a difference, a length taken as the difference of two end positions, a mean of repeats, or a unit conversion is a calculated value, not a reading. It goes in the record's calculated-values table with: the identifier, what it is, the value, the raw rows it was computed from (by their identifiers), and how (the formula, and which repeat or the mean was used). A calculated value with no named raw rows is not usable downstream.

**Centres.** To locate the centre of a hole, stub, or boss along an axis, record as raw readings the **minimum** and the **maximum** coordinate of the feature along that axis (§5.1 says how to read them), and the caliper width across the feature. The centre is then a calculated value, the mean of the minimum and the maximum, and the maximum minus the minimum is a calculated width that should agree with the caliper width within the provisional ± figures. If it does not, say so; do not pick one.

**Units.** Raw readings stay in the unit the instrument displayed. A record contains no converted figure except as a calculated value, clearly labelled with the factor used. The conversion that feeds the CAD model is done once, in `cad/params.py`, where the parameter cites the record file and identifier and multiplies inches by 25.4; that is the documented calculation, and it is not duplicated in the record.

**Setup.** Write down what the component was resting on, whether it was level, whether anything was fastened, and anything that prevented a clean reading (a seal in the way, a part already fitted, a hole you could not see into).

## 5. Datum conventions

Every reading is taken from a named datum so it can be transferred into the CAD model without guessing. The datums are local to each component. How a component sits in the frame is a separate placement decision held in `cad/params.py`; nothing here fixes it.

### 5.1 HP: heater and mounting plate

Used for every heater and plate feature, including the underside stubs.

**Setup.** The heater is seated on its plate as supplied, with whatever seal or fixing is already in place. The setup notes say whether the heater is fastened to the plate, whether the seal is fitted, and whether anything was loosened to take a reading. Do not disassemble anything only to measure it; if you choose to, record it.

**Axes.**

- **Origin, corner 0**, is one physical corner of the plate, marked with tape and photographed. The record says which corner was chosen in words (for example "the corner nearest the end of the heater with the large round stub, on the side where the smallest underside stub is"). Any corner works; the choice is permanent for that session and should be reused in later HP sessions so records compare directly.
- **X runs along the longer plate edge** from corner 0. **Y runs along the shorter plate edge** from corner 0. In each case the positive direction is the direction in which the plate extends away from corner 0 along that edge. So the plate itself occupies X from 0 to its length and Y from 0 to its width.
- **Z = 0 is the plate's underside**, the face that would rest on the frame crossmembers. Z is positive upward, into the heater. Protrusions below the plate have negative Z. Writing "protrusion below the plate underside 18.2 mm" in the reference column with the reading is acceptable, because the sign is then unambiguous; a bare `18.2` under Z is not.
- The plate's own features (outline, thickness, fixing holes, underside opening) are recorded in X, Y, Z. The holes are numbered H1 to H4 starting at the hole nearest corner 0 and going around the plate clockwise when viewed from above.
- If the plate is not a rectangle, or has a flange, bend, or tab, describe it in the observations and choose the two straight edges that meet at a corner as the X and Y edges, saying which.

**Signed coordinates.** Features can extend past the two edges that meet at corner 0: a heater end face can overhang the X = 0 edge, a stub can lie outside the plate outline. Such a feature has a negative coordinate, and the negative value is what is recorded, not an unsigned "overhang". Two practical ways to read one:

- *Offset rule.* Lay the rule along the axis with a round mark, say the 100 mm mark, exactly at the plate edge instead of the zero mark. Read the feature on the rule and record the reading as the raw value with "rule offset: 100 mm mark at the X = 0 edge" in the reference column. The signed coordinate is then a calculated value, reading minus 100, so a feature read at `88` is at X = −12.
- *Overhang reading.* Measure outward from the plate edge to the feature with the rule or calipers and record the distance as the raw reading with "outward from the X = 0 edge, beyond the plate" in the reference column. The signed coordinate is a calculated value, the negative of the reading.

Either way the raw cell holds what was read, and the sign is applied in the calculated-values table where the method is named.

**Minimum and maximum, not near and far.** Along a given axis, every feature has a smallest coordinate and a largest coordinate: `X min` and `X max`, `Y min` and `Y max`, `Z min` and `Z max`. These are numbers on the axis and do not depend on where the person measuring is standing or which way the plate happens to face. "The side of the stub closest to the X = 0 edge" is `X min` when the stub is on the positive side of the edge; when the stub lies beyond the edge, that same physical side is `X max`, because it is the less negative value. If in doubt, write both coordinates down with their signs and let the numbers decide which is which.

**The heater's longitudinal and transverse axes, L and T.** The heater body is longer in one direction than the other, and which plate edge that long direction runs along is an observation (PLT-14), not an assumption. To keep the heater rows readable whichever way it sits:

- **L** is the heater's long axis. PLT-14 states whether L is HP X or HP Y. **T** is the heater's short horizontal axis, the other one of X and Y.
- L and T are **descriptive aliases**, nothing more. They do not create a third coordinate system, and the CAD model does not use them. Every L or T reading is also an X or Y reading, and the record header states the mapping (`L = X, T = Y` or `L = Y, T = X`) so every value can be transferred into X, Y, Z without a second look at the heater.
- The positive direction of L is the positive direction of the HP axis it stands for; likewise T. So `L min` is the heater end face with the smaller X (if L = X) or smaller Y (if L = Y), and the heater's outlet end is recorded both as a physical description and as the HP direction it faces (+X, −X, +Y, or −Y).
- Openings on the heater body are located in the two axes that lie in the face they are on: an opening on an **end face** (a face perpendicular to L) is located by **T and Z**, and its position along L is the end face's own L coordinate; an opening on a **side face** (perpendicular to T) is located by **L and Z**; an opening on the top is located by L and T. The reference column names the face.
- Underside stubs lie in the plate plane and are recorded directly in X and Y, so they compare with the plate opening (PLT-11) without any mapping.

### 5.2 TK: fuel tank

Used for every tank feature: outer shape, bosses, filler, fuel outlet.

- The tank stands upright on its bottom face on a flat, level surface, empty, with its cap on unless a reading says otherwise. The broad face with the three recessed mounting points is the **mounting face** and is vertical.
- **Z = 0 is the surface the tank stands on.** Z is positive upward.
- **Y runs horizontally along the mounting face** from the tank's **left vertical edge as seen by someone facing the mounting face**. Mark that edge with tape labelled `L` and photograph it. Positive Y is toward the right edge.
- **X is perpendicular to the mounting face**, zero at the mounting face itself, positive into the tank body, away from where the frame would be. Thickness readings and the filler position across the tank are X readings.
- Minimum and maximum coordinates, signed values, and the separation of raw readings from calculated centres apply exactly as in §5.1. A feature that stands proud of the mounting face (a boss rim, a rib) has negative X.
- The three mounting points are **B1 (lower left), B2 (lower right), and B3 (upper)**, as seen facing the mounting face. Each has a moulded recess and, somewhere in it, a mounting hole or a membrane or a blind bottom. The recess and the hole are located separately; the hole is not assumed to be concentric with the recess. If the mounting face is not flat enough to define X = 0 cleanly (ribs, draft, a recessed panel), say what was used as the reference plane.
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
- Within a record, the several raw readings that belong to one feature are told apart by a lowercase letter after the identifier: `HTR-13a`, `HTR-13b`, `HTR-13c`. The checklist says what each letter is for where it matters; otherwise the record's Feature column says. Calculated values use the bare identifier with a short name, for example `HTR-13 centre X`, and name the lettered raw rows they came from.
- A feature measured again in a later session keeps its identifier; the new record is a new file. Which record a downstream value comes from is decided as in §7, never by date alone.
- A feature the checklist did not anticipate takes the next free number in its group, added to `checklist.md` in the same commit as the record.
- Non-numeric observations (a membrane, a marking, a direction) use the same identifiers as the features they describe.

Photograph identifiers are `P-YYYYMMDD-nn`, assigned by the owner in the owner's archive. A record cites them; the repository never holds them.

## 7. Repeated and conflicting records

Every record is kept. A later record never replaces, edits, or supersedes an earlier one, and the identifier stays the same across them. What changes is which record a downstream document or CAD parameter cites, and that choice is written down.

- **First, comparable.** Two readings are compared only when they are of the same physical feature under the same identifier, taken from the appropriate datum with consistent reference surfaces, on the component in the same configuration (same parts fitted, same fastening state), and in the same unit. If a unit conversion is needed to compare them, both raw readings stay untouched and the converted comparison is written as a calculated value naming them and the factor. Readings that differ in feature definition, reference surface, configuration, or setup are not compatible and not discrepant; they need a documented investigation in the "Discrepancies" section before either is used, and that investigation is treated like a reconciliation note.
- **One threshold.** For two comparable readings with values `a` and `b` and provisional uncertainties `u1` and `u2`:
  - **Compatible provisional intervals:** `abs(a − b) <= u1 + u2`.
  - **Discrepancy requiring reconciliation:** `abs(a − b) > u1 + u2`.

  Every pair falls into exactly one of these. A hypothetical pair, not a real reading: A = 100.0 ± 1.0 mm and B = 101.5 ± 1.0 mm give a difference of 1.5 mm against a combined provisional uncertainty of 2.0 mm, so they are compatible. Had B been 102.5 ± 1.0 mm, the difference of 2.5 mm would exceed 2.0 mm and the pair would be a discrepancy. A difference exactly equal to the combined uncertainty is compatible.
- **Compatible.** Either reading may be cited downstream. The document or parameter update that cites one says which record and identifier it used; citing the record with the better setup or the smaller provisional ± is the natural choice, and the reason is stated in a few words. Compatibility means the two readings are consistent under their provisional uncertainty estimates. It is not accuracy, calibration, verification, or proof that either is correct.
- **Discrepancy.** When comparable readings of the same identifier exceed the threshold, the newer record flags it in its "Discrepancies with earlier records" section, naming both records, the identifier, the two values, the two uncertainties, and the difference. From that moment the identifier is **in dispute**: it is not cited by `spec.md`, `design.md`, `bom.md`, or `cad/params.py`, and any existing citation stays on the record it already cites and is marked as disputed in the next document update.
- **Reconciliation.** A disputed identifier is released for downstream use only by a short dated reconciliation note: which record is selected, why (a setup fault found, a third measurement, a misread unit, a feature that was moved or disassembled between sessions), and what remains uncertain. The note lives in the record that resolves it (the "Discrepancies" section of a new record, when a re-measurement settled it) or in a file named `YYYY-MM-DD-reconciliation.md` when no new reading was needed. The downstream citation then names the reconciliation note as well as the selected record.
- **Newer is not better.** Both records are kept. A later reading does not win because it is later, and a reading with a tighter provisional ± does not win because it is tighter if the two are discrepant. Until reconciled, neither is used.
- **Stronger evidence stays.** A Measured value already cited downstream is not replaced by a new reading without the above; it is certainly not replaced by a User-reported or Illustrative figure.

This is a paper process. There is no database and no approval form; the audit trail is the records, the discrepancy sections, the reconciliation notes, and the citations in the documents and parameters.

## 8. Priorities

The order in `checklist.md` follows the Phase 2 assessment of 2026-10-28:

1. **Priority 1, feasibility of the B1 Compact layout and the plate interface**: the plate, the heater on its plate including its underside stubs, the exhaust pipe and silencer, and the tank's outer shape and filler. These decide whether the exhaust can leave the heater downward and run horizontally or down within the lower level, and whether the tank fits the proposed envelope.
2. **Priority 2, the frame concept**: the heater's end faces and inlet, the tank bosses and fuel outlet, the pump and filter, and the masses.
3. **Priority 3, later gates**: intake pipe and filter, blowpipe and tuyere, electrical parts, the paper manual.

The first session is Priority 1 for the heater, plate, and exhaust. The tank is the second session. Any session may stop early; a partial record with its "Not measured" list is a valid record.

## 9. What these records change, and what they do not

- They change the evidence tag of specific figures, through a later documented update, from User-reported or Unknown to Measured.
- They let the CAD model draw real features (plate opening and holes, stubs, inlet, filler, bosses, fuel outlet) in place of cues, in a later, separately approved increment that preserves both the A Original and B1 Compact layouts.
- They do not select any fastener, extrusion length, clamp, or component; do not derive a cut length; do not resolve SR-01 or SR-02; do not set any clearance; do not establish the suitability of the tank bosses (MR-04); do not confirm any orientation, angle, bend radius, or lift (Q-06, Q-08); do not call for any membrane to be pierced or any hole to be opened; and do not change the heater's governing specification. Those remain for VEVOR, engineering review, and the owner.
