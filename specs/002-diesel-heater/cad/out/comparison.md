# Layout comparison — PRELIMINARY — NOT FOR FABRICATION

Generated 2026-10-30 by `build.py`. Millimetres unless stated. Positions are modelled bounding boxes of placeholders.

**The bounding-box gaps below are modelled distances between placeholder boxes. They do not establish safe fuel-spill, fire, thermal, exhaust, or intake clearances.** The manufacturer states no fuel-spill or fire separation (spec §6 "not stated"); the 10 cm ventilation space, 4 in air-inlet gap, and 2 in exhaust ground clearance of the 2026 manual M3 (spec C27–C29) are installation figures for vehicles and buildings, checked against this model in design.md §5 and §8, not clearances established here. SR-01, SR-02, SR-04, SR-11 and the hazard register remain open, and gates G1–G5 are closed for every layout. B1 Adjusted is the preferred preliminary layout (Owner decision 2026-10-28; spec MR-02 as amended). A Original (the 2026-10-27 envelope) and B1 Compact (the 2026-10-28 starting point) are retained alternatives (design.md §16). Plate thickness and hole positions are owner-reported, not measured. Every member is 2020 (20 × 20 mm) section (Owner decision 2026-10-29); figures generated before that date used 20 × 40 mm. Every variant has 18 members (Owner decision 2026-10-30, D-14 adopted: `L2-W1` and `L2-W2` removed); outputs before that date had 20.

| Quantity | A Original | B1 Compact | B1 Adjusted |
|---|---|---|---|
| Envelope W × D × H (in) | 20 × 24 × 38 | 20 × 22 × 28 | 20 × 22 × 35 |
| Envelope W × D × H (mm) | 508.0 × 609.6 × 965.2 | 508.0 × 558.8 × 711.2 | 508.0 × 558.8 × 889.0 |
| Envelope tag | Owner decision, preliminary | Proposed/illustrative | Owner decision 2026-10-28, preliminary |
| Layout | stacked | beside | beside-above |
| Members / parts | 18 / 25 | 18 / 26 | 18 / 30 |
| Level member bottom faces Z | 0.0, 350.0, 945.2 | 0.0, 157.8, 691.2 | 0.0, 157.8, 869.0 |
| Heater axis (13.4 in length) | X | Y | Y |
| Plate underside Z (open height above the bottom members in brackets) | 370.0 (350.0) | 177.8 (157.8) | 177.8 (157.8) |
| Plate top face Z | 370.8 | 178.6 | 178.6 |
| Crossmember spacing, centre to centre (basis) | 130.0 (illustrative) | 100.0 (illustrative) | 125.4 (reported plate hole pitch, not measured) |
| Heater body X | 139.8–480.2 | 332.8–447.2 | 332.8–447.2 |
| Heater body Y | 247.6–362.0 | 109.2–449.6 | 109.2–449.6 |
| Heater body Z | 370.8–510.5 | 178.6–318.3 | 178.6–318.3 |
| Outlet cue end | none (D-07/D-08 open) | +Y | +Y |
| Tank X | 20.0–96.2 | 20.0–96.2 | 20.0–96.2 |
| Tank Y | 101.6–508.0 | 76.2–482.6 | 76.2–482.6 |
| Tank Z | 535.0–941.4 | 203.2–609.6 | 368.3–774.7 |
| Tank bottom minus heater top Z | +24.5 | -115.1 | +50.0 |
| Rail centre Z (lower, upper) | 595.0, 795.0 | 263.2, 463.2 | 428.3, 628.3 |
| Filler neck centre (X, Y) | 58.1, 151.6 | 58.1, 126.2 | 58.1, 126.2 |
| Top-level bottom face Z minus filler top Z (negative: filler rises into the top-member band, clear of the members in plan) | -16.6 | +61.2 | +73.9 |
| Top-level bottom face Z minus (tank top + 50 mm filler/cap allowance; neck and cap not measured) | -46.2 | +31.6 | +44.3 |
| Filler cue centre X minus X-min top member inside face (reach past the member from above) | +38.1 | +38.1 | +38.1 |
| Bounding-box gap tank → heater body (mm) | dx 43.6, dy 0.0, dz 24.5; min 50.0 | dx 236.6, dy 0.0, dz 0.0; min 236.6 | dx 236.6, dy 0.0, dz 50.0; min 241.9 |
| Bounding-box gap tank → heater plate (mm) | dx 144.7, dy 0.0, dz 164.2; min 218.9 | dx 208.9, dy 0.0, dz 24.6; min 210.3 | dx 208.9, dy 0.0, dz 189.7; min 282.2 |
| Bounding-box gap tank → crossmember HX1 (mm) | dx 0.0, dy 0.0, dz 165.0; min 165.0 | dx 0.0, dy 0.0, dz 25.4; min 25.4 | dx 0.0, dy 0.0, dz 190.5; min 190.5 |
| Bounding-box gap heater body → nearest X-max member L2-D2 (mm) | dx 7.8, dy 0.0, dz 0.8; min 7.9 | dx 40.8, dy 0.0, dz 0.8; min 40.9 | dx 40.8, dy 0.0, dz 0.8; min 40.9 |

Layout notes:

- **A Original**: Tank drawn entirely above the heater to picture the manufacturer's C12 instruction. This does not address the keep-away warning (C1); SR-01 is unreconciled.
- **B1 Compact**: Tank drawn beside the heater with separate horizontal footprints, its lower part overlapping the heater's upper part in height only. Horizontal separation alone establishes no spill, fire, or thermal clearance; SR-01 and SR-02 remain open and the modelled gaps are bounding-box distances, not clearances.
- **B1 Adjusted**: Tank drawn beside the heater with separate horizontal footprints and its bottom above the heater body's top by a provisional gap (D-15). This is a conservative geometric reading of the manufacturer's tank-above instruction (C12); it does not establish fuel delivery, spill control, hot-surface separation, or mounting adequacy. SR-01 and SR-02 remain open; the modelled gaps are bounding-box distances, not clearances.
