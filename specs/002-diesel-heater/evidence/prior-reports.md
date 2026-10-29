# Prior owner-reported dimensions and observations — reconciliation, not a measurement record

**Status:** the figures and observations the owner stated in earlier conversations (October 2026), gathered in one place so later work cites one record. Each is **User-reported** unless tagged otherwise. Nothing here is a dated measurement session; no instrument, resolution, datum, or uncertainty is stated because none was recorded at the time, and none is invented here. The formal workflow is [`../measurements/`](../measurements/README.md); the photographs are indexed in [photo-index.md](photo-index.md). Where this file and [spec.md §5](../spec.md#5-existing-equipment) differ, spec.md governs and the difference is listed in §3 below.

Tags used: **Manufacturer-stated** (M1 manual or M2 product page, as cited in spec.md); **User-reported** (stated by the owner, not independently checked); **Visually observed** (seen in a committed photograph, cited by E-nn); **Calculated** (arithmetic on named source values, the same as "derived from User-reported" in `cad/params.py`); **Unknown**.

## 1. Heater and supplied plate

| Item | Earlier report | Tag and date | What remains open |
|---|---|---|---|
| Heater model | VEVOR 12 V 2 kW diesel air heater, XMZ-D2 | Manufacturer-stated (M2) | — |
| Heater product size | 340 × 115 × 140 mm (13.4 × 4.5 × 5.5 in) | Manufacturer-stated (M2, C21) | Mounting footprint on the plate (HTR-01 to HTR-04) |
| Heater length by owner's tape | About 13.4 in, the same figure as the manufacturer's | User-reported, date not established; E-02 shows a tape alongside the heater but no reading is taken from it | Not independent confirmation of C21 |
| Net weight | 11 lb / 5 kg | Manufacturer-stated (M2, C22); **scope unknown**, heater alone or kit (Q-11) | Standalone heater mass: **Unknown** (MAS-01) |
| Heater on plate | Upright on the supplied metal plate; the intake, exhaust, and fuel connections leave downward through the plate region | Manufacturer-stated arrangement (M1 p.9); E-01 and E-02 show two tubular stubs and a small fitting at the plate centre (Visually observed) | Stub positions, protrusions, which is which (HTR-12 to HTR-14) |
| Plate outline | About 5 7/16 × 6 11/16 in | User-reported, tape, date not established (spec.md §5); E-03 and E-04 show tapes along each side, readings not taken | PLT-01, PLT-02 |
| Plate orientation on the heater | Not stated by the owner | Visually observed (E-03, E-04): the shorter side runs along the heater's length | PLT-14 in a dated record |
| Corner holes | Four, one near each corner, about 1/4 in diameter, about 1/8 in from each hole's outside edge to its two adjacent plate edges | User-reported 2026-10-28; holes visible in E-01 and E-05 (Visually observed), sizes not readable | PLT-05 to PLT-09; fit with Interface B hardware |
| Hole centre inset and pitches | Centre about 1/4 in (6.35 mm) from each adjacent edge; centre-to-centre about 4 15/16 in (125.4 mm) along the 5 7/16 in side and about 6 3/16 in (157.2 mm) along the 6 11/16 in side | **Calculated** from the User-reported outline, diameter, and edge margin (`cad/params.py` PLATE_HOLE_INSET, PLATE_HOLE_PITCH_ALONG, PLATE_HOLE_PITCH_ACROSS) | Actual centre coordinates (PLT-06 to PLT-09). A calculation inherits every uncertainty of its inputs |
| Plate thickness | About 1/32 in, below 1/16 in | User-reported **estimate** 2026-10-28, explicitly not measured; not readable from any photograph | PLT-03; D-16 adequacy is a separate question from the thickness |
| Heater-to-plate fixings (Interface A) | Not described by the owner; M1 p.8 lists four machine fixing screws and one machine fixing piece, M1 p.9 shows a seal and "double head screw nut" fixings | Manufacturer-stated; E-01 and E-02 show four threaded studs with hex nuts on the plate's outer face around the stubs (Visually observed) | Whether these are the complete Interface A; seal present or not (HTR-11, HTR-16, PLT-12); load path (D-16) |

## 2. Fuel tank

| Item | Earlier report | Tag and date | What remains open |
|---|---|---|---|
| Capacity | 10 L | Manufacturer-stated (M2; M1 p.8); molded `10L` visible in E-06 and E-07 | — |
| External size | About 16 × 16 × 3 in excluding the filler neck | User-reported, tape, date not established (spec.md §5) | TNK-01 to TNK-05 |
| Mounting points | Three recessed factory points, two lower and one upper | User-reported; three recesses visible on one face in E-06 and E-07 (Visually observed) | Recess and hole geometry, local wall thickness (TNK-10 to TNK-14) |
| Lower-point spacing | About 6 13/16 in horizontally between the two lower points | User-reported, tape, date not established (spec.md §5); not readable from E-07 (foreshortened) | TNK-10, TNK-11, TNK-13 |
| Upper-point rise | About 7 7/8 in above the lower row | User-reported, tape, date not established; not readable from E-07 | TNK-12, TNK-13 |
| Hole state | 2026-10-27: some holes appeared to have thin plastic membranes. 2026-10-28: described as three through-holes | User-reported on two dates, **conflicting; both stand**. E-08 shows a dark centre, E-09 a metallic-looking centre with concentric marks (Visually observed); neither resolves the conflict and E-09 raises a third possibility, an insert | TNK-10 to TNK-12 hole-state observation. Not to be resolved by guess, and **no hole is to be opened, drilled, or modified** without the Q-05 method on record (MR-04, G2) |
| Hole diameters, fastener, boss capacity | Not reported | **Unknown** | Q-04, Q-05, TNK-14, TNK-16 |
| Fuel outlet | Not reported | **Unknown**; the dark cylindrical object beyond the tank edge in E-06 and E-07 is not established as a tank fitting | TNK-15 |
| Tank empty mass | Not reported | **Unknown** | MAS-03 |

## 3. Discrepancies between the package as received and the repository record

| Topic | Package (received 2026-10-29) | Repository record | Handling |
|---|---|---|---|
| Date of the plate outline report | "User-reported Oct 28" | spec.md §5: tape measure, **date not established**; only the holes, edge margin, and thickness estimate are dated 2026-10-28 | spec.md wording kept above; the package date is not adopted |
| Dates of the tank size and point-spacing reports | "Oct 2026" and "Oct 27–28" | spec.md §5: tape measure, date not established | As above |
| E-07 | "Opposite broad-face view of the tank" | Same face as E-06, rotated (photo-index.md §2) | Corrected; the file renamed to `fuel-tank-upright-three-point-view.jpg`; no photograph of the other face exists |
| E-06 | "side outlet protrusion" | A dark cylindrical object beyond the tank edge, not established as a tank fitting | Corrected; TNK-15 stays Unknown |
| Heater length | "Approximate length 13.4 in, owner tape report" | spec.md §5: the owner's tape gave the same figure as C21; User-reported, not Verified | Kept, with the note that it is not independent confirmation |

## 4. What this file does not do

- It does not turn any prior tape figure into a **Measured** value; that needs a dated record under [`../measurements/`](../measurements/README.md) with the identifier named above.
- It does not claim that the photographs show crossmember compatibility, clearance, thermal or carbon-monoxide safety, tank-point strength, or fastening adequacy.
- It does not change any requirement, CAD parameter, decision, or gate, and does not close Q-03, Q-04, Q-05, Q-06, Q-08, D-04, D-12, D-16, D-17, MR-04, MR-05, SR-01, SR-02, or G1–G5.
- It does not authorize fuel, power, fabrication, transport, or operation.
