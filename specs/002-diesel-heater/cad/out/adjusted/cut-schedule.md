# Proposed cut schedule and stock order — B1 Adjusted — PRELIMINARY — NOT FOR FABRICATION

Generated 2026-10-29 by `build.py` from `params.py` (variant `adjusted`). Millimetres. Section 2020 (20 × 20 mm, 6 mm slot) throughout (Owner decision 2026-10-29).

**Proposed, not approved.** The lengths are the nominal model lengths of the 20 members in the member schedule. They become fabrication dimensions only when the G1(e) review records a reviewed cut list and the owner approves the purchase (spec.md §10); nothing is to be cut from this file. The stock packing is an estimate to size an order; it takes one kerf per piece and **no separate allowance for trimming an out-of-square stock end**, so any squaring cut must come out of the bar's margin below, and the supplier states neither a cut tolerance nor end squareness.

Assumptions: stock length 2000 mm (longest listed pre-cut length, ZYLtech EXT-2020, read 2026-10-29; supplier cut tolerance not stated); kerf allowance 3 mm per cut (assumed); every piece gets its own cut; no trim allowance beyond the kerf.

## Pieces by nominal length

| Nominal length (mm) | Qty | Pieces | Roles (basis per piece in the member schedule) |
|---|---|---|---|
| 889.0 | 4 | U1, U2, U3, U4 | upright |
| 518.8 | 8 | L1-D1, L1-D2, L2-D1, L2-D2, L3-D1, L3-D2, TR-lower, TR-upper | perimeter_depth, tank_rail |
| 468.0 | 8 | L1-W1, L1-W2, L2-W1, L2-W2, L3-W1, L3-W2, HX1, HX2 | heater_crossmember, perimeter_width |

Pieces: 20 (the 20 modelled members of MR-01). Total nominal length: 11450.4 mm (11.450 m) before kerf and waste.

## Stock packing into 2000 mm bars (preferred pattern)

The preferred pattern for this member schedule is 4 bars of 889 + 518.8 + 518.8 and 2 bars of 4 × 468 (Owner approval 2026-10-29 after Codex review): it uses the same six bars as the fewest-bars search but leaves the largest margin on its tightest bar. It is applied only after a check that it conserves every piece and fits the stock and kerf assumptions; if the member schedule, stock length, or kerf change so that it no longer does, the general packer takes over and this heading says so.

| Bar | Pieces (mm) | Used incl. kerf (mm) | Offcut (mm) |
|---|---|---|---|
| 1 | 889.0 + 518.8 + 518.8 | 1935.6 | 64.4 |
| 2 | 889.0 + 518.8 + 518.8 | 1935.6 | 64.4 |
| 3 | 889.0 + 518.8 + 518.8 | 1935.6 | 64.4 |
| 4 | 889.0 + 518.8 + 518.8 | 1935.6 | 64.4 |
| 5 | 468.0 + 468.0 + 468.0 + 468.0 | 1884.0 | 116.0 |
| 6 | 468.0 + 468.0 + 468.0 + 468.0 | 1884.0 | 116.0 |

**Proposed order: 6 × 2000 mm** (12.0 m), of which 11.450 m becomes pieces and 0.550 m is kerf and offcut (5 %). A spare bar for cutting errors is a separate owner choice. The shorter listed lengths (300 to 1200 mm) would reduce cutting but their individual prices are not shown on the supplier page, so no comparison is made here.

**Margin:** the tightest bar holds 1926.6 mm of pieces in 3 pieces and, after 3 kerfs of 3 mm, leaves 64.4 mm. For a full, untrimmed 2000 mm bar the kerf can therefore be at most 24.4 mm (exactly 3 + 64.4 / 3 = 24.4667 mm, shown rounded down). With a delivered shortfall s, an end-trimming allowance t (for example to square a stock end), and a real kerf k, the pattern fits only while s + t + 3 × (k − 3) ≤ 64.4 mm. If the measured bars or blade exceed that, the packing is to be recalculated with the measured stock length, trim, and kerf (`select_packing`, which falls back to the general packer), which may or may not need another bar; it is not to be patched by assuming a seventh bar. Measure the delivered bars and the kerf before cutting; this is one reason the schedule is not a cut list.

Not in this schedule: stabilization hardware of any kind, which is excluded from the initial purchase and build and kept as a potential future enhancement (design.md section 10, D-12); any member added at the MR-05 review; and any change to the envelope (MR-02, preliminary 34 to 36 in).
