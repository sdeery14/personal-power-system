# Measurement checklist — Diesel Heater Module (002)

Prioritized list of what to measure, with the permanent identifiers (README §6). Record readings in a copy of [template.md](template.md), not here. This file is amended only to add identifiers; it never holds a reading.

Everything is measured cold, unpowered, unfuelled, and unconnected. Instruments: tape, steel rule, digital calipers, a scale for the masses. Conventions, datums, signed coordinates, the minimum/maximum rule, and the provisional ± figures are in [README.md](README.md).

**A session may stop at any point.** Session 1a alone is a complete session. Identifiers not reached go in the record's "Not measured" list with the reason.

Reading the "Record" column: items marked **raw** are instrument readings written as displayed; items marked **calc** are worked out afterwards in the calculated-values table from the lettered raw rows. "X min" and "X max" are the smallest and largest coordinate of the feature along that axis, signed, whichever way the plate faces (README §5.1). The "Why" column names the open item in [spec.md](../spec.md) or [design.md](../design.md) the reading feeds; it never means the reading will settle that item, and most of them also need VEVOR or an engineering review.

## Before the first session

- Choose the HP datum corner (README §5.1): one physical plate corner, tape marked `0`, described in words in the record and photographed. The CAD model's drawing of the heater on its plate is one possibility and is not a reason to choose a corner or to expect a particular orientation.
- Note the assembly state found before touching anything (`DOC-03`). bom.md records that some components were partly assembled; this is where that gets written down.
- Have the photograph identifiers ready (`P-YYYYMMDD-nn`).

## Priority 1 — plate interface and B1 feasibility

### Session 1a: mounting plate (PLT), datum HP

If the heater is fastened to the plate, measure what is reachable and list the rest under "Not measured".

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| PLT-01 | Plate length along X (the longer edge) | raw: edge to edge, twice | Rule or calipers | Replaces the User-reported 6 11/16 in or 5 7/16 in; cad PLATE_ALONG / PLATE_ACROSS |
| PLT-02 | Plate width along Y (the shorter edge) | raw: edge to edge, twice | Rule or calipers | As above |
| PLT-03 | Plate thickness | raw: at two places away from any bend (a, b) | Calipers | cad PLATE_T is illustrative |
| PLT-04 | Plate shape | observation: rectangle or not; corner radii; any flange, bend, tab, or raised rim; raw: its size | Observation, calipers | Plate-to-crossmember seat (MR-03, D-02) |
| PLT-05 | Number of fixing holes and anything else through the plate | observation: count; which are holes, slots, or studs | Observation | Q-03 |
| PLT-06 | Fixing hole H1 (nearest corner 0) | raw: X min (a), X max (b), Y min (c), Y max (d) of the hole edge; caliper diameter (e). calc: centre X, centre Y, diameter from b−a and d−c | Rule, calipers | Q-03; fastening to the crossmembers |
| PLT-07 | Fixing hole H2 (next clockwise from above) | As PLT-06 | | |
| PLT-08 | Fixing hole H3 | As PLT-06 | | |
| PLT-09 | Fixing hole H4 | As PLT-06 | | |
| PLT-10 | Underside opening shape | observation: round, rectangular, slotted, several openings; describe | Observation | MR-07 |
| PLT-11 | Underside opening extents | raw: X min (a), X max (b), Y min (c), Y max (d) of the opening edge; for a round opening also caliper diameter (e). calc: centre and size | Rule, calipers | MR-07; which stubs pass through it (HTR-12 to HTR-14) |
| PLT-12 | Seal or gasket | observation: present or not; fitted or loose; material; above or below the plate. raw: thickness | Observation, calipers | C7, MR-07 |
| PLT-13 | Other plate features | observation: any cut-out, slot, embossing, or marking not covered above; raw: positions if relevant | Observation, rule | |
| PLT-14 | Heater orientation on the plate | observation: whether the heater length runs along the X (long) edge or the Y (short) edge. This sets the record header `L = X, T = Y` or `L = Y, T = X` for every HTR row | Observation | Resolves which plate side runs along the heater; cad PLATE_ALONG; defines L and T |

### Session 1b: heater on its plate (HTR), datum HP

L is the heater's long axis and T its short horizontal axis, each being HP X or HP Y as PLT-14 found (README §5.1). Every L or T reading is written with the HP axis it stands for in the Reference column. Coordinates are signed: an end face or stub beyond a corner-0 edge has a negative value.

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| HTR-01 | Heater end faces along L | raw: L min end face position (a) and L max end face position (b), each from the corresponding plate edge, twice, with the offset or overhang method noted if either lies beyond the edge. calc: heater length b−a | Rule, tape | C21 says 340 mm; records the body against the plate frame |
| HTR-02 | Heater side faces along T | raw: T min side face position (a) and T max side face position (b). calc: heater width b−a; position on the plate | Rule | C21 says 115 mm; heater position on the plate |
| HTR-03 | Heater height | raw: Z of the top of the body above the plate underside (a); height above the plate top face (b) if easier to read | Rule | C21 says 140 mm; level spacing |
| HTR-04 | Overhang | observation: whether the body extends past any plate edge, and which. raw: the distance beyond each such edge, measured outward and labelled as such. calc: the signed coordinate | Rule | Crossmember spacing and plate seat |
| HTR-05 | Hot-air outlet end | observation: which physical end carries the hot-air outlet (describe it), whether that is the L min or L max end, and the HP direction it faces (+X, −X, +Y, or −Y) | Observation | D-03, D-08; cad outlet cue end |
| HTR-06 | Hot-air outlet stub | raw: outside diameter (a); inside diameter if reachable (b); protrusion beyond the end face along L (c); on that end face, T min (d), T max (e), Z min (f), Z max (g) of the stub. calc: centre T, centre Z | Calipers, rule | C23 says 76.5 mm ID; duct connection; end-gap in B1 |
| HTR-07 | Heating-air inlet | observation: which face it is on (L min end, L max end, T min side, T max side, top); opening shape; whether a grille or filter covers it. raw: min and max of the opening along the two axes lying in that face (T and Z for an end face, L and Z for a side face, L and T for the top) (a–d); diameter or width and height by caliper (e, f). calc: centre | Observation, calipers, rule | SR-05, SR-07, SR-11; C25 |
| HTR-08 | Heating-air inlet protrusion | raw: any inlet stub, lip, or guard beyond the body face, and its length | Calipers | End-gap in B1 |
| HTR-09 | Controller and harness exits | observation: which face each cable leaves and the connector type in words. raw: its position in the two axes of that face and Z | Observation, rule | D-09 |
| HTR-10 | Other body protrusions | observation and raw: anything else outside the C21 box (brackets, bosses, labels standing proud, a fan guard), with the face and size | Observation, calipers | Envelope |
| HTR-11 | Underside fixing studs or screws | observation: count; how they engage the plate holes. raw: protrusion below the plate underside; major diameter by caliper | Observation, calipers | Q-03; MR-03 |
| HTR-12 | Combustion-air intake stub | raw, in HP X and Y where the stub meets the plate plane: X min (a), X max (b), Y min (c), Y max (d); outside diameter by caliper (e); protrusion below the plate underside (f). observation: direction (straight down, or angled and toward which axis); whether it passes through the plate opening (PLT-11), through a hole, or lies outside the plate outline. calc: centre X, centre Y, width b−a and d−c | Rule, calipers | MR-07, SR-07, C14; intake pipe route in L1 |
| HTR-13 | Exhaust stub | As HTR-12 | Rule, calipers | MR-07, SR-03, C16; exhaust route in L1; the main B1 feasibility question |
| HTR-14 | Fuel inlet stub | As HTR-12; raw: also the barb outside diameter (g) | Rule, calipers | MR-07; fuel line route; SR-02 |
| HTR-15 | Spacing between the stubs | raw: centre-to-centre between each pair, read directly with calipers or rule (a: intake–exhaust, b: intake–fuel, c: exhaust–fuel). Compared afterwards with the calculated centres of HTR-12 to HTR-14; a mismatch beyond the provisional ± is noted, not resolved | Calipers or rule | Cross-check |
| HTR-16 | Seal between heater and plate | observation: whether one is fitted. raw: compressed thickness if readable | Observation, calipers | C7, MR-07 |

### Session 1c: exhaust pipe and silencer (EXH), loose parts

Do not force the pipe into a bend to see how far it goes. Record it as supplied.

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| EXH-01 | Exhaust pipe outside diameter | raw: at two places (a, b) | Calipers | Route in L1; clamps |
| EXH-02 | Exhaust pipe inside diameter | raw: at an end | Calipers | Fit to the heater stub (HTR-13) |
| EXH-03 | Exhaust pipe length as supplied | raw: end to end, following the pipe | Tape | D-07; exit side |
| EXH-04 | Pipe construction | observation: rigid, flexible corrugated, or layered; material as marked; any printed marking verbatim | Observation | D-07 |
| EXH-05 | Pipe shape as supplied | observation: straight, or already coiled or bent. raw: if bent, the approximate radius of the bend it was supplied in, with a note that this is the supplied shape, not a permitted minimum | Tape | D-07. The manufacturer gives no bend radius (Q-06); none is inferred from this |
| EXH-06 | Silencer body | raw: overall length (a); outside diameter, or width and height (b, c). observation: shape | Calipers, rule | D-07, SR-04 |
| EXH-07 | Silencer inlet and outlet | raw: outside diameter of each (a, b). observation: which is which if marked; direction (in line, or angled) | Calipers, observation | D-07 |
| EXH-08 | Silencer fixing piece | observation: shape; the two screws as supplied. raw: hole positions and sizes | Calipers, observation | D-07; restraint |
| EXH-09 | Exhaust clamps | observation: count. raw: closed and open diameter range as read | Calipers | Which joints they serve |
| EXH-10 | Fit to the heater stub | observation: whether the pipe slides over or into the stub; any mark or stop for insertion depth | Observation | HTR-13 |

### Session 2a: fuel tank outer shape and filler (TNK), datum TK

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| TNK-01 | Tank width along Y | raw: left edge to right edge across the mounting face at the bottom (a), mid-height (b), and top (c) | Tape | Replaces the User-reported 16 in; cad TANK_Y |
| TNK-02 | Tank height | raw: Z of the top face at the left edge (a), the centre (b), and the right edge (c) | Rule or tape | cad TANK_Z; filler headroom in B1 |
| TNK-03 | Tank thickness along X | raw: X of the far face from the mounting face at the bottom (a), mid-height (b), and top (c), excluding the filler | Calipers or rule | cad TANK_X |
| TNK-04 | Mounting face flatness and features | observation: ribs, draft, a recessed panel, feet, or anything that keeps the face off a flat plate; the reference plane used for X = 0. raw: how far any such feature stands proud (negative X) | Observation, rule | MR-04; rail contact |
| TNK-05 | Bottom face | observation: flat or not; feet or ribs; does the tank stand stably on its own. raw: foot or rib height | Observation | Setup validity; D-04 |
| TNK-06 | Filler neck position | raw: Y min (a), Y max (b) of the neck from the left edge; X min (c), X max (d) from the mounting face. calc: centre Y, centre X | Rule | cad filler cue is illustrative; B1 headroom |
| TNK-07 | Filler neck | raw: outside diameter (a); height above the local top face without cap (b); Z of the neck top above the standing surface (c) | Calipers, rule | B1 headroom (41 mm in the illustrative model) |
| TNK-08 | Filler cap | raw: outside diameter (a); Z of the cap top above the standing surface with the cap on (b). observation: cap type (vented or not as marked; tether; thread or bayonet) | Calipers, rule, observation | B1 headroom; SR-02 refuelling |
| TNK-09 | Other top-face or side features | observation: vent, breather, graduations, labels, handle. raw: positions if relevant | Observation | SR-02 |

## Priority 2 — frame concept

### Session 2b: tank bosses and fuel outlet (TNK continued), datum TK

Each mounting point has a moulded recess and, somewhere in it, a hole, a membrane, or a blind bottom. The recess and the hole are located separately; the hole is not assumed to be central in the recess. Nothing is pierced, drilled, or opened to take a reading. A membrane or a blind bottom is recorded as found.

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| TNK-10 | Boss B1 (lower left) | raw, recess: Y min (a), Y max (b), Z min (c), Z max (d) of the recess rim; recess diameter by caliper (e); recess depth from the mounting face (f). raw, hole, if visible: Y min (g), Y max (h), Z min (i), Z max (j) of the hole edge; hole diameter by caliper (k). observation: hole state, one of open, membrane-covered, blind, threaded (thread or insert visible), or inaccessible; what the membrane or bottom looks like. calc: recess centre Y and Z; hole centre Y and Z; offset of the hole centre from the recess centre | Rule, calipers, observation | Replaces the User-reported 6 13/16 in spacing; MR-04; Q-04, Q-05 |
| TNK-11 | Boss B2 (lower right) | As TNK-10 | | |
| TNK-12 | Boss B3 (upper) | As TNK-10 | | Replaces the User-reported 7 7/8 in rise |
| TNK-13 | Boss spacings read directly | raw: B1 to B2 recess centre to centre (a); B3 recess height above the B1–B2 line (b); B3 offset along Y from the midpoint of B1–B2 (c); the same three for the hole centres where visible (d, e, f). Compared afterwards with the calculated centres of TNK-10 to TNK-12 | Rule or tape | Cross-check; cad HOLE_LOWER_SPACING, HOLE_UPPER_RISE |
| TNK-14 | Tank wall thickness | raw: wherever it can be read without opening anything (at an open hole, at the filler neck, at a vent), each place named | Calipers | MR-04; H-01 |
| TNK-15 | Fuel outlet | observation: which face; fitting type; direction it points; any shut-off or strainer. raw: min and max along the two axes of that face (a–d); outside diameter (e). calc: centre | Observation, calipers, rule | Fuel line route; SR-02; C13 |
| TNK-16 | Tank accessory kit | observation: contents of "oil tank accessories" (M1 p.8), each item named and counted. raw: its key dimension (screw thread major diameter and length, grommet size) | Observation, calipers | Q-02, Q-05; MR-04 |

### Session 3: pump, filter, fuel line (PMP, FLT, FUL), loose parts

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| PMP-01 | Pump body | raw: length (a); outside diameter (b) | Calipers | D-05; L1 placement |
| PMP-02 | Pump inlet and outlet | raw: barb outside diameter at each end (a, b). observation: which end is inlet as marked (arrow or label) | Calipers, observation | Fuel line |
| PMP-03 | Pump markings | observation: model, voltage, any arrow, any angle or orientation marking, exactly as printed | Observation | Q-08. A marking is recorded verbatim, not interpreted |
| PMP-04 | Sheath and screw | raw: sheath length (a) and inside diameter (b); mounting hole or slot size (c); screw major diameter and length (d, e) | Calipers | D-05 |
| PMP-05 | Pump cable | raw: length from the pump body to its connector. observation: connector type in words | Tape, observation | D-05, D-09 |
| FLT-01 | Oil filter | raw: length (a); outside diameter (b); barb outside diameter each end (c, d). observation: flow-direction marking as printed | Calipers, observation | D-05 |
| FUL-01 | Oil pipe | raw: outside diameter (a); inside diameter (b); supplied length (c). observation: material or stiffness as observed | Calipers, tape | Q-08 (line length), SR-02 |
| FUL-02 | Oil pipe clips and cable ties | observation: counts. raw: clip size range | Calipers | |

### Session 4: masses (MAS)

Record the scale, its resolution, and a zero check.

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| MAS-01 | Heater body alone | raw: without the plate, exhaust, intake, or duct; say what was attached | Scale | A-06, C22, Q-11; TR-03; SR-10 |
| MAS-02 | Mounting plate alone | raw: if it can be separated; otherwise heater and plate together, stated | Scale | TR-03 |
| MAS-03 | Fuel tank, empty, cap on | raw | Scale | A-05 note; TR-03; H-02 |
| MAS-04 | Pump with sheath; oil filter | raw: together or separately, stated | Scale | TR-03 |
| MAS-05 | Exhaust pipe and silencer | raw | Scale | TR-03 |

## Priority 3 — later gates

### Session 5: intake, duct, electrical, manual (INT, DUC, ELC, DOC)

| ID | Feature | Record | Instrument | Why |
|---|---|---|---|---|
| INT-01 | Intake pipe | raw: outside diameter (a); inside diameter (b); supplied length (c). observation: construction | Calipers, tape | SR-07, C14 |
| INT-02 | Air filter element | raw: overall size. observation: how it attaches to the pipe | Calipers, observation | SR-07 |
| INT-03 | Fit to the heater stub | observation: over or into the stub (HTR-12) | Observation | |
| DUC-01 | Blowpipe | raw: outside diameter (a); inside diameter (b); supplied length (c). observation: construction | Calipers, tape | FR-03, D-08; C23 |
| DUC-02 | Blowpipe clamps | observation: count. raw: diameter range | Calipers | |
| DUC-03 | Rotary tuyere | raw: overall size (a); connection diameter (b) | Calipers | FR-03 |
| ELC-01 | Power cord | raw: length. observation: printed markings on the jacket, verbatim (gauge, type) | Tape, observation | Q-07, ER-03 |
| ELC-02 | In-line fuse | observation: rating and type as printed on the fuse; holder type | Observation | Q-07. Recorded, not endorsed |
| ELC-03 | Controller | raw: overall size (a); cable length to the heater connector (b) | Calipers, tape | D-09 |
| ELC-04 | Harness | observation: connectors and their count in words. raw: lengths between them | Observation, tape | D-09 |
| ELC-05 | Remote control | observation: present; battery type as marked | Observation | |
| DOC-01 | Paper manual | observation: any revision mark, date, or code printed on it | Observation | Q-01, A-01 |
| DOC-02 | Differences from M1 and M3 | observation: cover models; pages that differ from M1 and from M3 (the owner-supplied 2026 manual, spec.md §2), in particular the installation diagram, the fuel-tank installation page, and the safety pages; describe, do not paraphrase safety text | Observation | Q-01, Q-12 |
| DOC-03 | Assembly state found and inventory | observation: which items were already assembled and to what; count every packing-list item (M1 p.7–8) present or missing | Observation | Q-02; bom.md §1 |

## Identifiers added after the first version

None yet. Add a row here, in the right group, for any feature a session finds that the list above does not cover.
