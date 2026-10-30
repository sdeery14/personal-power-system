# Proposed custom-cut piece schedule — B1 Adjusted — PRELIMINARY — NOT FOR FABRICATION

Generated 2026-10-30 by `build.py` from `params.py` (variant `adjusted`). Millimetres. Section 2020 (20 × 20 mm, 6 mm slot) throughout (Owner decision 2026-10-29). 18 members (Owner decision 2026-10-30, D-14 adopted: `L2-W1` and `L2-W2` removed). Schedules generated before 2026-10-30 listed 20 members, 11,450.4 mm, and a six-bar stock packing; those figures are superseded.

**Proposed, not approved.** The lengths are the nominal model lengths of the 18 members in the member schedule. They become fabrication dimensions only when the G1(e) review records a reviewed cut list and the owner approves the purchase (spec.md §10); nothing is to be cut or ordered from this file. The supply direction (Owner decision 2026-10-30) is custom cutting by the supplier to the exact millimetre lengths: the order names the nearest listed inch length and the buyer notes state the millimetres (TNUTZ FAQ, read 2026-10-29). Custom-cut extrusion is nonreturnable (TNUTZ FAQ). The supplier states no numeric cut tolerance; delivered lengths are to be measured and recorded before assembly.

## Pieces by nominal length

| Nominal length (mm) | Qty | Nearest listed length (1/16 in steps) | Pieces | Roles (basis per piece in the member schedule) |
|---|---|---|---|---|
| 889.0 | 4 | 35 in (889.0 mm listed; state 889.0 mm in the buyer notes) | U1, U2, U3, U4 | upright |
| 518.8 | 8 | 20 7/16 in (519.1 mm listed; state 518.8 mm in the buyer notes) | L1-D1, L1-D2, L2-D1, L2-D2, L3-D1, L3-D2, TR-lower, TR-upper | perimeter_depth, tank_rail |
| 468.0 | 6 | 18 7/16 in (468.3 mm listed; state 468.0 mm in the buyer notes) | L1-W1, L1-W2, L3-W1, L3-W2, HX1, HX2 | heater_crossmember, perimeter_width |

Pieces: 18 (the 18 modelled members of MR-01 as amended 2026-10-30). Total nominal length: 10514.4 mm (10.514 m). Cuts: 18, one per piece.

## Joint hardware count (one bracket per horizontal member end)

Horizontal member ends: 28 (14 horizontal members × 2; the four continuous uprights have no bracketed ends). One TNUTZ CBK-020-A corner-bracket kit per end (Owner decision 2026-10-30): **28 kits**, each stated by the supplier to contain one 2-hole inside corner bracket, two M5 drop-in T-nuts, and two M5 × 8 mm button-head screws, so 56 T-nuts and 56 screws in the kits. No doubled brackets, no base joining plates (the 2026-10-29 selection of 40 brackets and 8 plates is superseded). Additional T-nuts for the heater-plate and tank-rail interfaces and spares are an owner decision recorded in bom.md §2.2, not derived from the model. This count is for procurement planning under the working engineering assumption that the bracket arrangement is sufficiently rigid; it is not verified joint strength or stability (MR-05, A-04, SR-10 open).

## Superseded alternative on record: home cutting from 2000 mm stock (general packer, fewest bars by exact search; no preferred pattern is defined for this member schedule)

**Superseded (Owner decision 2026-10-30): the supply is custom-cut by the supplier; nothing is to be home-cut.** The packing below is kept only so the alternative stays sized on record. Assumptions: stock length 2000 mm (the longest pre-cut length the earlier ZYLtech plan listed, read 2026-10-29); kerf allowance 3 mm per cut (assumed); every piece gets its own cut; **no separate allowance for trimming an out-of-square stock end**. The six-bar preferred pattern approved on 2026-10-29 belonged to the 20-member schedule and no longer applies; the general packer sizes this alternative.

| Bar | Pieces (mm) | Used incl. kerf (mm) | Offcut (mm) |
|---|---|---|---|
| 1 | 889.0 + 889.0 | 1784.0 | 216.0 |
| 2 | 889.0 + 889.0 | 1784.0 | 216.0 |
| 3 | 518.8 + 518.8 + 518.8 | 1565.4 | 434.6 |
| 4 | 518.8 + 518.8 + 518.8 | 1565.4 | 434.6 |
| 5 | 518.8 + 518.8 + 468.0 + 468.0 | 1985.6 | 14.4 |
| 6 | 468.0 + 468.0 + 468.0 + 468.0 | 1884.0 | 116.0 |

**Alternative order, not proposed: 6 × 2000 mm** (12.0 m), of which 10.514 m would become pieces and 1.486 m kerf and offcut (12 %).

**Margin:** the tightest bar holds 1973.6 mm of pieces in 4 pieces and, after 4 kerfs of 3 mm, leaves 14.4 mm. For a full, untrimmed 2000 mm bar the kerf can therefore be at most 6.6 mm (exactly 3 + 14.4 / 4 = 6.6000 mm, shown rounded down). With a delivered shortfall s, an end-trimming allowance t (for example to square a stock end), and a real kerf k, the pattern fits only while s + t + 4 × (k − 3) ≤ 14.4 mm. If the measured bars or blade exceeded that, the packing would be recalculated with the measured stock length, trim, and kerf (`select_packing`, which uses the general packer), which may or may not need another bar; it is not to be patched by assuming an extra bar.

Not in this schedule: the two middle widthwise members `L2-W1` and `L2-W2` (removed, Owner decision 2026-10-30, D-14 adopted); stabilization hardware of any kind, which is excluded from the initial purchase and build and kept as a potential future enhancement (design.md section 10, D-12); any member added at the MR-05 review; and any change to the envelope (MR-02, preliminary 34 to 36 in).
