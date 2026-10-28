# Layout comparison — PRELIMINARY — NOT FOR FABRICATION

Generated 2026-10-28 by `build.py`. Millimetres unless stated. Positions are modelled bounding boxes of placeholders.

**The bounding-box gaps below are modelled distances between placeholder boxes. They do not establish safe fuel-spill, fire, thermal, exhaust, or intake clearances.** The manufacturer states none (spec C-list, "not stated"); SR-01, SR-02, SR-04, SR-11 and the hazard register remain open, and gates G1–G5 are closed for both layouts. The B1 Compact envelope is an owner-proposed starting value from the 2026-10-28 brief, not the MR-02 envelope in spec.md, which is unchanged.

| Quantity | A Original | B1 Compact |
|---|---|---|
| Envelope W × D × H (in) | 20 × 24 × 38 | 20 × 22 × 28 |
| Envelope W × D × H (mm) | 508.0 × 609.6 × 965.2 | 508.0 × 558.8 × 711.2 |
| Envelope tag | Owner decision, preliminary | Proposed/illustrative |
| Layout | stacked | beside |
| Members / parts | 20 / 27 | 20 / 28 |
| Level member bottom faces Z | 0.0, 350.0, 925.2 | 0.0, 137.8, 671.2 |
| Heater axis (13.4 in length) | X | Y |
| Plate top face Z | 393.0 | 180.8 |
| Heater body X | 139.8–480.2 | 332.8–447.2 |
| Heater body Y | 247.6–362.0 | 109.2–449.6 |
| Heater body Z | 393.0–532.7 | 180.8–320.5 |
| Outlet cue end | none (D-07/D-08 open) | +Y |
| Tank X | 20.0–96.2 | 20.0–96.2 |
| Tank Y | 101.6–508.0 | 76.2–482.6 |
| Tank Z | 535.0–941.4 | 203.2–609.6 |
| Tank bottom minus heater top Z | +2.3 | -117.3 |
| Rail centre Z (lower, upper) | 595.0, 795.0 | 263.2, 463.2 |
| Filler neck centre (X, Y) | 58.1, 151.6 | 58.1, 126.2 |
| Top-level bottom face Z minus filler top Z (negative: filler rises into the top-member band, clear of the members in plan) | -36.6 | +41.2 |
| Bounding-box gap tank → heater body (mm) | dx 43.6, dy 0.0, dz 2.3; min 43.7 | dx 236.6, dy 0.0, dz 0.0; min 236.6 |
| Bounding-box gap tank → heater plate (mm) | dx 144.7, dy 0.0, dz 142.0; min 202.8 | dx 208.9, dy 0.0, dz 22.4; min 210.1 |
| Bounding-box gap tank → crossmember HX1 (mm) | dx 0.0, dy 0.0, dz 145.0; min 145.0 | dx 0.0, dy 0.0, dz 25.4; min 25.4 |
| Bounding-box gap heater body → nearest X-max member L2-D2 (mm) | dx 7.8, dy 0.0, dz 3.0; min 8.4 | dx 40.8, dy 0.0, dz 3.0; min 41.0 |

Layout notes:

- **A Original**: Tank drawn entirely above the heater to picture the manufacturer's C12 instruction. This does not address the keep-away warning (C1); SR-01 is unreconciled.
- **B1 Compact**: Tank drawn beside the heater with separate horizontal footprints, its lower part overlapping the heater's upper part in height only. Horizontal separation alone establishes no spill, fire, or thermal clearance; SR-01 and SR-02 remain open and the modelled gaps are bounding-box distances, not clearances.
