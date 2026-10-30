# Member schedule — B1 Compact — PRELIMINARY — NOT FOR FABRICATION

Generated 2026-10-30 by `build.py` from `params.py` (variant `compact`). All lengths in millimetres, nominal, as modelled. Section 2020 (20 × 20 mm, 6 mm slot) for every member (Owner decision 2026-10-29). 18 members (Owner decision 2026-10-30, D-14 adopted): the middle level carries the two lengthwise support rails and the heater crossmembers only; `L2-W1` and `L2-W2` are removed. Schedules generated before 2026-10-30 listed 20 members.

**This is not a cut list.** Every length is a nominal model length under the joint assumption below and the illustrative level heights and tank position; none is an approved fabrication dimension until the G1(e) review and the owner's purchase approval. Every member's placement and connection is provisional; the Basis column names what each depends on. Gates G1–G5 in spec.md §10 are closed.

Joint assumption: Uprights are continuous over the full height; every horizontal member butts between uprights or between the middle lengthwise rails. The joint system is one inside corner bracket at each of the 28 horizontal member ends (TNUTZ CBK-020-A kit: one 2-hole bracket, two M5 drop-in T-nuts, two M5 x 8 mm screws), with no doubled brackets and no base joining plates (Owner decision 2026-10-30, D-01; the 2026-10-29 selection of doubled brackets and plates is superseded). Brackets do not change member lengths, so the butt geometry stands. The bracket arrangement is treated as sufficiently rigid as a working engineering assumption for geometry and procurement planning only; it is not verified joint strength or stability (MR-05, A-04, SR-10 open). Member lengths derived from it are nominal model lengths, not approved cut lengths, until the G1(e) review and the owner's purchase approval (spec section 10).

Tank assumption: The two tank rails lie in the plane of the X-min perimeter members and butt between the uprights like them, so their inside face is 20 mm from the outside of the frame. The tank hangs on that face with the two lower points on the lower rail and the upper point, centred between them, on the upper rail. Which wall carries the tank (D-03), the tank's height (SR-01), the upper point's horizontal position, and the rail-to-upright connector are all open.

Layout: Tank drawn beside the heater with separate horizontal footprints, its lower part overlapping the heater's upper part in height only. Horizontal separation alone establishes no spill, fire, or thermal clearance; SR-01 and SR-02 remain open and the modelled gaps are bounding-box distances, not clearances.

| ID | Role | Axis | Nominal length (mm) | Section (mm) | Basis (what the size and placement depend on) | Note |
|---|---|---|---|---|---|---|
| U1 | upright | Z | 711.2 | 20 × 20 | envelope height (Proposed/illustrative); joint assumption | 2020 square section; no orientation choice (D-02 closed 2026-10-29) |
| U2 | upright | Z | 711.2 | 20 × 20 | envelope height (Proposed/illustrative); joint assumption | 2020 square section; no orientation choice (D-02 closed 2026-10-29) |
| U3 | upright | Z | 711.2 | 20 × 20 | envelope height (Proposed/illustrative); joint assumption | 2020 square section; no orientation choice (D-02 closed 2026-10-29) |
| U4 | upright | Z | 711.2 | 20 × 20 | envelope height (Proposed/illustrative); joint assumption | 2020 square section; no orientation choice (D-02 closed 2026-10-29) |
| L1-W1 | perimeter_width | X | 468.0 | 20 × 20 | envelope (Proposed/illustrative); joint assumption | level at the envelope top or bottom |
| L1-W2 | perimeter_width | X | 468.0 | 20 × 20 | envelope (Proposed/illustrative); joint assumption | level at the envelope top or bottom |
| L1-D1 | perimeter_depth | Y | 518.8 | 20 × 20 | envelope (Proposed/illustrative); joint assumption | level at the envelope top or bottom |
| L1-D2 | perimeter_depth | Y | 518.8 | 20 × 20 | envelope (Proposed/illustrative); joint assumption | level at the envelope top or bottom |
| L2-D1 | perimeter_depth | Y | 518.8 | 20 × 20 | envelope (Proposed/illustrative); joint assumption; illustrative middle-level height | middle support rail; level height illustrative; no widthwise member at this level (D-14 adopted 2026-10-30) |
| L2-D2 | perimeter_depth | Y | 518.8 | 20 × 20 | envelope (Proposed/illustrative); joint assumption; illustrative middle-level height | middle support rail; level height illustrative; no widthwise member at this level (D-14 adopted 2026-10-30) |
| L3-W1 | perimeter_width | X | 468.0 | 20 × 20 | envelope (Proposed/illustrative); joint assumption | level at the envelope top or bottom |
| L3-W2 | perimeter_width | X | 468.0 | 20 × 20 | envelope (Proposed/illustrative); joint assumption | level at the envelope top or bottom |
| L3-D1 | perimeter_depth | Y | 518.8 | 20 × 20 | envelope (Proposed/illustrative); joint assumption | level at the envelope top or bottom |
| L3-D2 | perimeter_depth | Y | 518.8 | 20 × 20 | envelope (Proposed/illustrative); joint assumption | level at the envelope top or bottom |
| HX1 | heater_crossmember | X | 468.0 | 20 × 20 | envelope width; joint assumption; illustrative middle-level height, heater position, and spacing | spacing illustrative (plate fixing pattern not used, Q-03); butts between the middle support rails L2-D1 and L2-D2; spans the full width and passes beneath the tank zone |
| HX2 | heater_crossmember | X | 468.0 | 20 × 20 | envelope width; joint assumption; illustrative middle-level height, heater position, and spacing | spacing illustrative (plate fixing pattern not used, Q-03); butts between the middle support rails L2-D1 and L2-D2; spans the full width and passes beneath the tank zone |
| TR-lower | tank_rail | Y | 518.8 | 20 × 20 | envelope depth; joint assumption; illustrative tank height and hole position | height follows the illustrative tank position (SR-01 open); butts between the uprights |
| TR-upper | tank_rail | Y | 518.8 | 20 × 20 | envelope depth; joint assumption; illustrative tank height and hole position | height follows the illustrative tank position (SR-01 open); butts between the uprights |

Members: 18. Other components (placeholders): heater_plate, heater_body, heater_outlet_cue, fuel_tank, tank_filler_neck, tank_hole_lower_a, tank_hole_lower_b, tank_hole_upper.

## Parameters

| Parameter | Value | Tag | Source |
|---|---|---|---|
| ENVELOPE_W | 508.0 mm | Proposed/illustrative | owner brief 2026-10-28 (B1 starting values); not in spec.md, MR-02 unchanged |
| ENVELOPE_D | 558.8 mm | Proposed/illustrative | owner brief 2026-10-28 (B1 starting values); not in spec.md, MR-02 unchanged |
| ENVELOPE_H | 711.2 mm | Proposed/illustrative | owner brief 2026-10-28 (B1 starting values); not in spec.md, MR-02 unchanged |
| LEVEL_Z[1] | 157.8 mm | illustrative | middle-level height is open (design section 4); plate underside about 7 in in B1 layouts (owner brief 2026-10-28) |
| HEATER_AXIS | 1.0 0=X,1=Y | illustrative | heater orientation in the frame is open |
| HEATER_CENTER_X | 390.0 mm | illustrative | heater position in the frame is open |
| HEATER_CENTER_Y | 279.4 mm | illustrative | heater position in the frame is open |
| CROSSMEMBER_SPACING | 100.0 mm | illustrative | plate fixing pattern not used in this variant (Q-03) |
| TANK_BOTTOM_Z | 203.2 mm | illustrative | tank height is open; SR-01 unreconciled |
| PROFILE_MINOR | 20.0 mm | Owner decision 2026-10-29 | spec MR-01 as amended: 2020 (20 x 20 mm) T-slot, 6 mm slot, every member |
| PROFILE_MAJOR | 20.0 mm | Owner decision 2026-10-29 | as above; square section |
| SLOT_WIDTH | 6.0 mm | Manufacturer-stated | TNUTZ EXM-2020 page: slot opening approx. 1/4 in or 6 mm, read 2026-10-29 |
| ORDER_LENGTH_STEP | 1.6 mm | Manufacturer-stated | TNUTZ length selector in 1/16 in steps, read 2026-10-30; the exact millimetres go in the buyer notes (FAQ) |
| STOCK_LENGTH | 2000.0 mm | Superseded | home-cutting alternative from 2000 mm ZYLtech stock (2026-10-29), superseded by TNUTZ custom cutting (Owner decision 2026-10-30); on record only |
| KERF_ALLOWANCE | 3.0 mm | Proposed/illustrative | assumed saw kerf per cut; home-cutting alternative only |
| HEATER_L | 340.4 mm | Manufacturer-stated | spec C21: 13.4 in (owner tape agrees, User-reported) |
| HEATER_W | 114.3 mm | Manufacturer-stated | spec C21: 4.5 in |
| HEATER_H | 139.7 mm | Manufacturer-stated | spec C21: 5.5 in |
| PLATE_ALONG | 138.1 mm | User-reported | spec section 5: 5 7/16 in, tape measure; which plate side runs along the heater is not recorded |
| PLATE_ACROSS | 169.9 mm | User-reported | spec section 5: 6 11/16 in, tape measure; as above |
| OUTLET_D | 76.5 mm | Manufacturer-stated | spec C23: air outlet pipe inner diameter 3 in / 76.5 mm |
| TANK_Y | 406.4 mm | User-reported | spec section 5: about 16 in, tape measure |
| TANK_Z | 406.4 mm | User-reported | spec section 5: about 16 in, tape measure |
| TANK_X | 76.2 mm | User-reported | spec section 5: about 3 in excluding filler neck |
| HOLE_LOWER_SPACING | 173.0 mm | User-reported | spec section 5: about 6 13/16 in |
| HOLE_UPPER_RISE | 200.0 mm | User-reported | spec section 5: about 7 7/8 in |
| PLATE_T | 0.8 mm | User-reported (estimate) | owner estimate 2026-10-28: about 1/32 in, below 1/16 in; not measured (checklist PLT-03) |
| PLATE_HOLE_D | 6.3 mm | User-reported | four fixing holes about 1/4 in diameter, owner-reported 2026-10-28; not measured (checklist PLT-06 to PLT-09) |
| PLATE_HOLE_EDGE_CLEAR | 3.2 mm | User-reported | about 1/8 in from each hole's outside edge to its two adjacent plate edges, owner-reported 2026-10-28 |
| PLATE_HOLE_INSET | 6.3 mm | derived from User-reported | hole centre from each adjacent plate edge: edge clearance + half the hole diameter |
| PLATE_HOLE_PITCH_ALONG | 125.4 mm | derived from User-reported | hole centre to centre along the 5 7/16 in side |
| PLATE_HOLE_PITCH_ACROSS | 157.2 mm | derived from User-reported | hole centre to centre along the 6 11/16 in side |
| TANK_GAP_ABOVE_HEATER | 50.0 mm | Proposed/illustrative | B1 Adjusted tank bottom above the heater body top; placeholder for engineering review (D-15); not a clearance |
| FILLER_CAP_ALLOWANCE | 50.0 mm | Proposed/illustrative | height allowed above the tank top for the filler neck and cap until measured (TNK-07, TNK-08) |
| TANK_HOLE_ABOVE_BOTTOM | 60.0 mm | illustrative | hole position on the tank face not recorded |
| HOLE_DIA | 8.0 mm | illustrative | boss hole size not recorded (Q-05) |
| FILLER_D | 40.0 mm | illustrative | filler neck size not recorded; orientation cue only |
| FILLER_H | 20.0 mm | illustrative | as above |
| FILLER_CORNER_INSET | 50.0 mm | illustrative | filler near a top corner per owner brief 2026-10-28; corner, angle, and size unknown |
| OUTLET_CUE_L | 20.0 mm | illustrative | direction cue only; the outlet stub length is not recorded |
