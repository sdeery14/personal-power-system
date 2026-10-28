# Member schedule — PRELIMINARY — NOT FOR FABRICATION

Generated 2026-10-28 by `build.py` from `params.py`. All lengths in millimetres, nominal, as modelled.

**This is not a cut list.** Every length depends on the joint assumption below, which the design has not chosen (D-01, D-02), and on illustrative level heights and tank position. Gates G1–G5 in spec.md §10 are closed.

Joint assumption: Uprights are continuous over the full height; every horizontal member butts between uprights or between perimeter members, with the 40 mm side vertical. This is one of several possible joint arrangements (design D-01, D-02 open). Member lengths derived from it are illustrative, not cut lengths.

Tank assumption: The tank hangs on the X-min inside wall with the two lower points on the lower rail and the upper point, centred between them, on the upper rail. Which wall carries the tank (D-03), the tank's height (SR-01), and the upper point's horizontal position are all open.

| ID | Role | Axis | Nominal length (mm) | Section (mm) | Illustrative placement | Note |
|---|---|---|---|---|---|---|
| U1 | upright | Z | 965.2 | 20 × 40 | no | section orientation illustrative (D-02) |
| U2 | upright | Z | 965.2 | 20 × 40 | no | section orientation illustrative (D-02) |
| U3 | upright | Z | 965.2 | 20 × 40 | no | section orientation illustrative (D-02) |
| U4 | upright | Z | 965.2 | 20 × 40 | no | section orientation illustrative (D-02) |
| L1-W1 | perimeter_width | X | 468.0 | 20 × 40 | no | joint assumption; see params |
| L1-W2 | perimeter_width | X | 468.0 | 20 × 40 | no | joint assumption; see params |
| L1-D1 | perimeter_depth | Y | 529.6 | 20 × 40 | no | joint assumption; see params |
| L1-D2 | perimeter_depth | Y | 529.6 | 20 × 40 | no | joint assumption; see params |
| L2-W1 | perimeter_width | X | 468.0 | 20 × 40 | yes | level height illustrative |
| L2-W2 | perimeter_width | X | 468.0 | 20 × 40 | yes | level height illustrative |
| L2-D1 | perimeter_depth | Y | 529.6 | 20 × 40 | yes | level height illustrative |
| L2-D2 | perimeter_depth | Y | 529.6 | 20 × 40 | yes | level height illustrative |
| L3-W1 | perimeter_width | X | 468.0 | 20 × 40 | no | joint assumption; see params |
| L3-W2 | perimeter_width | X | 468.0 | 20 × 40 | no | joint assumption; see params |
| L3-D1 | perimeter_depth | Y | 529.6 | 20 × 40 | no | joint assumption; see params |
| L3-D2 | perimeter_depth | Y | 529.6 | 20 × 40 | no | joint assumption; see params |
| HX1 | heater_crossmember | X | 468.0 | 20 × 40 | yes | spacing illustrative (plate fixing pattern, Q-03) |
| HX2 | heater_crossmember | X | 468.0 | 20 × 40 | yes | spacing illustrative (plate fixing pattern, Q-03) |
| TR-lower | tank_rail | Y | 529.6 | 20 × 40 | yes | height follows the illustrative tank position (SR-01 open) |
| TR-upper | tank_rail | Y | 529.6 | 20 × 40 | yes | height follows the illustrative tank position (SR-01 open) |

Members: 20. Other components (placeholders): heater_plate, heater_body, fuel_tank, tank_filler_neck, tank_hole_lower_a, tank_hole_lower_b, tank_hole_upper.

## Parameters

| Parameter | Value (mm) | Tag | Source |
|---|---|---|---|
| ENVELOPE_W | 508.0 | Owner decision, preliminary | spec MR-02: 20 in |
| ENVELOPE_D | 609.6 | Owner decision, preliminary | spec MR-02: 24 in |
| ENVELOPE_H | 965.2 | Owner decision, preliminary | spec MR-02: 38 in |
| PROFILE_MINOR | 20.0 | Owner decision | spec MR-01: 20 x 40 mm T-slot |
| PROFILE_MAJOR | 40.0 | Owner decision | spec MR-01: 20 x 40 mm T-slot |
| HEATER_L | 340.4 | Manufacturer-stated | spec C21: 13.4 in (owner tape agrees, User-reported) |
| HEATER_W | 114.3 | Manufacturer-stated | spec C21: 4.5 in |
| HEATER_H | 139.7 | Manufacturer-stated | spec C21: 5.5 in |
| PLATE_X | 138.1 | User-reported | spec section 5: 5 7/16 in, tape measure |
| PLATE_Y | 169.9 | User-reported | spec section 5: 6 11/16 in, tape measure |
| TANK_Y | 406.4 | User-reported | spec section 5: about 16 in, tape measure |
| TANK_Z | 406.4 | User-reported | spec section 5: about 16 in, tape measure |
| TANK_X | 76.2 | User-reported | spec section 5: about 3 in excluding filler neck |
| HOLE_LOWER_SPACING | 173.0 | User-reported | spec section 5: about 6 13/16 in |
| HOLE_UPPER_RISE | 200.0 | User-reported | spec section 5: about 7 7/8 in |
| LEVEL_Z[1] | 350.0 | illustrative | middle-level height is open (design section 4) |
| PLATE_T | 3.0 | illustrative | plate thickness not recorded (Q-03) |
| CROSSMEMBER_SPACING | 130.0 | illustrative | plate fixing pattern not recorded (Q-03) |
| HEATER_CENTER_X | 310.0 | illustrative | heater position along the frame is open |
| TANK_BOTTOM_Z | 535.0 | illustrative | tank height is open; SR-01 unreconciled |
| TANK_HOLE_ABOVE_BOTTOM | 60.0 | illustrative | hole position on the tank face not recorded |
| HOLE_DIA | 8.0 | illustrative | boss hole size not recorded (Q-05) |
| FILLER_D | 40.0 | illustrative | filler neck size not recorded; orientation cue only |
| FILLER_H | 20.0 | illustrative | as above |
