# Proposed cut schedule and stock order — B1 Adjusted — PRELIMINARY — NOT FOR FABRICATION

Generated 2026-10-29 by `build.py` from `params.py` (variant `adjusted`). Millimetres. Section 2020 (20 × 20 mm, 6 mm slot) throughout (Owner decision 2026-10-29).

**Proposed, not approved.** The lengths are nominal model lengths from the member schedule plus the two proposed foot bars. They become fabrication dimensions only when the G1(e) review records a reviewed cut list and the owner approves the purchase (spec.md §10); nothing is to be cut from this file. The stock packing is an estimate to size an order; it assumes a saw kerf per cut and does not rely on square stock ends, and the supplier states neither a cut tolerance nor end squareness.

Assumptions: stock length 2000 mm (longest listed pre-cut length, ZYLtech EXT-2020, read 2026-10-29; supplier cut tolerance not stated); kerf allowance 3 mm per cut (assumed); every piece gets its own cut; no trim allowance beyond the kerf.

## Pieces by nominal length

| Nominal length (mm) | Qty | Pieces | Roles (basis per piece in the member schedule) |
|---|---|---|---|
| 889.0 | 4 | U1, U2, U3, U4 | upright |
| 708.0 | 2 | FB1, FB2 | foot bar (proposed, design section 10, D-12; not modelled) |
| 518.8 | 8 | L1-D1, L1-D2, L2-D1, L2-D2, L3-D1, L3-D2, TR-lower, TR-upper | perimeter_depth, tank_rail |
| 468.0 | 8 | L1-W1, L1-W2, L2-W1, L2-W2, L3-W1, L3-W2, HX1, HX2 | heater_crossmember, perimeter_width |

Pieces: 22 (20 modelled members plus 2 proposed foot bars). Total nominal length: 12866.4 mm (12.866 m) before kerf and waste.

## Stock packing into 2000 mm bars (fewest bars; exact search)

| Bar | Pieces (mm) | Used incl. kerf (mm) | Offcut (mm) |
|---|---|---|---|
| 1 | 889.0 + 889.0 | 1784.0 | 216.0 |
| 2 | 889.0 + 889.0 | 1784.0 | 216.0 |
| 3 | 708.0 + 708.0 + 518.8 | 1943.8 | 56.2 |
| 4 | 518.8 + 518.8 + 518.8 | 1565.4 | 434.6 |
| 5 | 518.8 + 518.8 + 468.0 + 468.0 | 1985.6 | 14.4 |
| 6 | 518.8 + 518.8 + 468.0 + 468.0 | 1985.6 | 14.4 |
| 7 | 468.0 + 468.0 + 468.0 + 468.0 | 1884.0 | 116.0 |

**Proposed order: 7 × 2000 mm** (14.0 m), of which 12.866 m becomes pieces and 1.134 m is kerf and offcut (8 %). A spare bar for cutting errors is a separate owner choice. The shorter listed lengths (300 to 1200 mm) would reduce cutting but their individual prices are not shown on the supplier page, so no comparison is made here.

Not in this schedule: the attachment of the foot bars and the leveling feet (D-12), any member added at the MR-05 review, and any change to the envelope (MR-02, preliminary 34 to 36 in).
