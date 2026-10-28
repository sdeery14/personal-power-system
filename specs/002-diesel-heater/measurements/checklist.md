# Measurement checklist — Diesel Heater Module (002)

Prioritized list of what to measure, with the permanent identifiers (README §6). Record readings in a copy of [template.md](template.md), not here. This file is amended only to add identifiers; it never holds a reading.

Everything is measured cold, unpowered, unfuelled, and unconnected. Instruments: tape, steel rule, digital calipers, a scale for the masses. Conventions, datums, and the plus-or-minus rules are in [README.md](README.md).

The "Why" column names the open item in [spec.md](../spec.md) or [design.md](../design.md) the reading feeds. It never means the reading will settle that item; most of them also need VEVOR or an engineering review.

## Before the first session

- Decide the HP datum corner (README §5.1): one plate corner, tape marked `0`. The suggested choice is the plate corner nearest the end of the heater that carries the hot-air outlet, on the same side as the exhaust stub, but any corner works if the record says which.
- Note the assembly state found before touching anything (`DOC-03`). bom.md records that some components were partly assembled; this is where that gets written down.
- Have the photograph identifiers ready (`P-YYYYMMDD-nn`).

## Priority 1 — plate interface and B1 feasibility

### Session 1a: mounting plate (PLT), datum HP

If the heater is fastened to the plate, measure what is reachable and list the rest under "Not measured".

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| PLT-01 | Plate length along X (the longer edge) | Edge to edge | Rule or calipers | Replaces the User-reported 6 11/16 in or 5 7/16 in; cad PLATE_ALONG / PLATE_ACROSS |
| PLT-02 | Plate width along Y (the shorter edge) | Edge to edge | Rule or calipers | As above |
| PLT-03 | Plate thickness | At two places, away from any bend | Calipers | cad PLATE_T is illustrative |
| PLT-04 | Plate shape | Rectangle or not; corner radii; any flange, bend, tab, or raised rim and its size | Observation, calipers | Plate-to-crossmember seat (MR-03, D-02) |
| PLT-05 | Number of fixing holes and anything else through the plate | Count; which are holes, slots, or studs | Observation | Q-03 |
| PLT-06 | Fixing hole H1 (nearest corner 0) | X near, X far, Y near, Y far; diameter | Rule, calipers | Q-03; fastening to the crossmembers |
| PLT-07 | Fixing hole H2 (next clockwise from above) | As PLT-06 | | |
| PLT-08 | Fixing hole H3 | As PLT-06 | | |
| PLT-09 | Fixing hole H4 | As PLT-06 | | |
| PLT-10 | Underside opening shape | Round, rectangular, slotted, several openings; describe | Observation | MR-07 |
| PLT-11 | Underside opening extents | X min, X max, Y min, Y max of the opening (or centre and diameter if round); note each edge reading | Rule, calipers | MR-07; which stubs pass through it (see HTR-12 to HTR-14) |
| PLT-12 | Seal or gasket | Present or not; fitted or loose; material; thickness; whether it sits above or below the plate | Observation, calipers | C7, MR-07 |
| PLT-13 | Other plate features | Any cut-out, slot, embossing, or marking not covered above | Observation | |
| PLT-14 | Heater orientation on the plate | Whether the heater length runs along the X (long) edge or the Y (short) edge | Observation | Resolves which plate side runs along the heater; cad PLATE_ALONG |

### Session 1b: heater on its plate (HTR), datum HP

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| HTR-01 | Heater length | X of the end face nearest corner 0 and X of the far end face, from the plate X = 0 edge; length is the difference | Rule, tape | C21 says 340 mm; records the body against the plate frame |
| HTR-02 | Heater width | Y of the near side face and Y of the far side face from the plate Y = 0 edge | Rule | C21 says 115 mm; heater position on the plate |
| HTR-03 | Heater height | Z of the top of the body above the plate underside; also height above the plate top face if easier to read | Rule | C21 says 140 mm; level spacing |
| HTR-04 | Overhang | Whether the body extends past any plate edge, and by how much on each side | Rule | Crossmember spacing and plate seat |
| HTR-05 | Hot-air outlet end | Which end carries the hot-air outlet, in the HP frame (the X = 0 end or the far end) | Observation | D-03, D-08; cad outlet cue end |
| HTR-06 | Hot-air outlet stub | Outside diameter; inside diameter if reachable; protrusion beyond the body end face; Y and Z of its centre (near and far readings) | Calipers, rule | C23 says 76.5 mm ID; duct connection; end-gap in B1 |
| HTR-07 | Heating-air inlet | Which face it is on; opening shape and size (diameter, or width and height); Y and Z of its centre; whether a grille or filter covers it | Observation, calipers, rule | SR-05, SR-07, SR-11; C25 |
| HTR-08 | Heating-air inlet protrusion | Any inlet stub, lip, or guard beyond the body face, and its length | Calipers | End-gap in B1 |
| HTR-09 | Controller and harness exits | Where cables leave the body (face, X, Y, Z); connector types in words | Observation, rule | D-09 |
| HTR-10 | Other body protrusions | Anything else outside the C21 box: brackets, bosses, labels standing proud, a fan guard | Observation, calipers | Envelope |
| HTR-11 | Underside fixing studs or screws | Count; what protrudes below the plate underside and by how much; approximate thread size by caliper on the major diameter; how they engage the plate holes | Observation, calipers | Q-03; MR-03 |
| HTR-12 | Combustion-air intake stub | X near, X far, Y near, Y far of the stub where it meets the plate plane; outside diameter; protrusion below the plate underside; direction (straight down, or angled, and toward which axis); whether it passes through the plate opening (PLT-11), through a hole, or lies outside the plate outline | Rule, calipers | MR-07, SR-07, C14; intake pipe route in L1 |
| HTR-13 | Exhaust stub | As HTR-12 | Rule, calipers | MR-07, SR-03, C16; exhaust route in L1; the main B1 feasibility question |
| HTR-14 | Fuel inlet stub | As HTR-12; also the barb size | Rule, calipers | MR-07; fuel line route; SR-02 |
| HTR-15 | Spacing between the stubs | Centre-to-centre between each pair, read directly as a cross-check on HTR-12 to HTR-14 | Calipers or rule | Cross-check |
| HTR-16 | Seal between heater and plate | Whether one is fitted; compressed thickness if readable | Observation, calipers | C7, MR-07 |

### Session 1c: exhaust pipe and silencer (EXH), loose parts

Do not force the pipe into a bend to see how far it goes. Record it as supplied.

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| EXH-01 | Exhaust pipe outside diameter | At two places | Calipers | Route in L1; clamps |
| EXH-02 | Exhaust pipe inside diameter | At an end | Calipers | Fit to the heater stub (HTR-13) |
| EXH-03 | Exhaust pipe length as supplied | End to end, following the pipe | Tape | D-07; exit side |
| EXH-04 | Pipe construction | Rigid, flexible corrugated, or layered; material as marked; any printed marking | Observation | D-07 |
| EXH-05 | Pipe shape as supplied | Straight, or already coiled or bent; if bent, the approximate radius of the bend it was supplied in, measured, and a note that this is the supplied shape, not a permitted minimum | Tape | D-07. The manufacturer gives no bend radius (Q-06); none is inferred from this |
| EXH-06 | Silencer body | Overall length; outside diameter or width and height; shape | Calipers, rule | D-07, SR-04 |
| EXH-07 | Silencer inlet and outlet | Outside diameter of each; which is which if marked; direction (in line, or angled) | Calipers, observation | D-07 |
| EXH-08 | Silencer fixing piece | Shape; hole positions and sizes; the two screws as supplied | Calipers, observation | D-07; restraint |
| EXH-09 | Exhaust clamps | Count; closed and open diameter range as read | Calipers | Which joints they serve |
| EXH-10 | Fit to the heater stub | Whether the pipe slides over or into the stub; any mark or stop for insertion depth | Observation | HTR-13 |

### Session 2a: fuel tank outer shape and filler (TNK), datum TK

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| TNK-01 | Tank width along Y | Left edge to right edge across the mounting face, at the bottom, at mid-height, and at the top | Tape | Replaces the User-reported 16 in; cad TANK_Y |
| TNK-02 | Tank height | Z of the top face, at the left edge, the centre, and the right edge | Rule or tape | cad TANK_Z; filler headroom in B1 |
| TNK-03 | Tank thickness along X | X of the far face from the mounting face, at the bottom, mid-height, and top, excluding the filler | Calipers or rule | cad TANK_X |
| TNK-04 | Mounting face flatness and features | Ribs, draft, a recessed panel, feet, or anything that keeps the face off a flat plate; the reference plane used for X = 0 | Observation, rule | MR-04; rail contact |
| TNK-05 | Bottom face | Flat or not; feet or ribs and their height; does the tank stand stably on its own | Observation | Setup validity; D-04 |
| TNK-06 | Filler neck position | Y near and far from the left edge; X near and far from the mounting face; centre | Rule | cad filler cue is illustrative; B1 headroom |
| TNK-07 | Filler neck | Outside diameter; height above the local top face without cap; height above the standing surface (Z) of the neck top | Calipers, rule | B1 headroom (41 mm in the illustrative model) |
| TNK-08 | Filler cap | Outside diameter; height above the standing surface with the cap on; cap type (vented or not as marked; tether; thread or bayonet) | Calipers, rule, observation | B1 headroom; SR-02 refuelling |
| TNK-09 | Other top-face or side features | Vent, breather, graduations, labels, handle | Observation | SR-02 |

## Priority 2 — frame concept

### Session 2b: tank bosses and fuel outlet (TNK continued), datum TK

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| TNK-10 | Boss B1 (lower left) | Y near and far, Z near and far of the recess; centre; recess outside diameter; recess depth from the mounting face; hole state (open, membrane, blind); hole diameter if open; any thread or insert visible | Rule, calipers, observation | Replaces the User-reported 6 13/16 in spacing; MR-04; Q-04, Q-05 |
| TNK-11 | Boss B2 (lower right) | As TNK-10 | | |
| TNK-12 | Boss B3 (upper) | As TNK-10 | | Replaces the User-reported 7 7/8 in rise |
| TNK-13 | Boss spacings read directly | B1 to B2 centre to centre; B3 height above the B1–B2 line; B3 offset along Y from the midpoint | Rule or tape | Cross-check on TNK-10 to TNK-12; cad HOLE_LOWER_SPACING, HOLE_UPPER_RISE |
| TNK-14 | Tank wall thickness | Wherever it can be read without opening anything: at an open hole, at the filler neck, at a vent | Calipers | MR-04; H-01 |
| TNK-15 | Fuel outlet | Which face; position in the TK frame (near and far readings); fitting type; outside diameter; direction it points; any shut-off or strainer | Observation, calipers, rule | Fuel line route; SR-02; C13 |
| TNK-16 | Tank accessory kit | Contents of "oil tank accessories" (M1 p.8): each item named, counted, and its key dimension (screw thread and length, grommet size) | Observation, calipers | Q-02, Q-05; MR-04 |

### Session 3: pump, filter, fuel line (PMP, FLT, FUL), loose parts

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| PMP-01 | Pump body | Length; outside diameter | Calipers | D-05; L1 placement |
| PMP-02 | Pump inlet and outlet | Barb outside diameter at each end; which end is inlet as marked (arrow or label) | Calipers, observation | Fuel line |
| PMP-03 | Pump markings | Model, voltage, any arrow, any angle or orientation marking, exactly as printed | Observation | Q-08. A marking is recorded verbatim, not interpreted |
| PMP-04 | Sheath and screw | Sheath length and inside diameter; mounting hole or slot size; screw thread and length | Calipers | D-05 |
| PMP-05 | Pump cable | Length from the pump body to its connector; connector type in words | Tape, observation | D-05, D-09 |
| FLT-01 | Oil filter | Length; outside diameter; barb outside diameter each end; flow-direction marking as printed | Calipers, observation | D-05 |
| FUL-01 | Oil pipe | Outside diameter; inside diameter; supplied length; material or stiffness as observed | Calipers, tape | Q-08 (line length), SR-02 |
| FUL-02 | Oil pipe clips and cable ties | Counts; clip size range | Calipers | |

### Session 4: masses (MAS)

Record the scale, its resolution, and a zero check.

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| MAS-01 | Heater body alone | Without the plate, exhaust, intake, or duct; say what was attached | Scale | A-06, C22, Q-11; TR-03; SR-10 |
| MAS-02 | Mounting plate alone | If it can be separated; otherwise heater and plate together, stated | Scale | TR-03 |
| MAS-03 | Fuel tank, empty, cap on | | Scale | A-05 note; TR-03; H-02 |
| MAS-04 | Pump with sheath; oil filter | Together or separately, stated | Scale | TR-03 |
| MAS-05 | Exhaust pipe and silencer | | Scale | TR-03 |

## Priority 3 — later gates

### Session 5: intake, duct, electrical, manual (INT, DUC, ELC, DOC)

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| INT-01 | Intake pipe | Outside diameter; inside diameter; supplied length; construction | Calipers, tape | SR-07, C14 |
| INT-02 | Air filter element | Overall size; how it attaches to the pipe | Calipers, observation | SR-07 |
| INT-03 | Fit to the heater stub | Over or into the stub (HTR-12) | Observation | |
| DUC-01 | Blowpipe | Outside diameter; inside diameter; supplied length; construction | Calipers, tape | FR-03, D-08; C23 |
| DUC-02 | Blowpipe clamps | Count; diameter range | Calipers | |
| DUC-03 | Rotary tuyere | Overall size; connection diameter | Calipers | FR-03 |
| ELC-01 | Power cord | Length; printed markings on the jacket, verbatim (gauge, type) | Tape, observation | Q-07, ER-03 |
| ELC-02 | In-line fuse | Rating and type as printed on the fuse; holder type | Observation | Q-07. Recorded, not endorsed |
| ELC-03 | Controller | Overall size; cable length to the heater connector | Calipers, tape | D-09 |
| ELC-04 | Harness | Connectors and their count in words; lengths between them | Observation, tape | D-09 |
| ELC-05 | Remote control | Present; battery type as marked | Observation | |
| DOC-01 | Paper manual | Any revision mark, date, or code printed on it | Observation | Q-01, A-01 |
| DOC-02 | Differences from M1 | Pages that differ from M1, in particular the installation diagram and safety pages; describe, do not paraphrase safety text | Observation | Q-01 |
| DOC-03 | Assembly state found and inventory | Which items were already assembled and to what; count every packing-list item (M1 p.7–8) present or missing | Observation | Q-02; bom.md §1 |

## Identifiers added after the first version

None yet. Add a row here, in the right group, for any feature a session finds that the list above does not cover.
