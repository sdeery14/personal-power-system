# Diesel Heater Module (002) — Bill of Materials

**Status**: Inventory of owned equipment and a preliminary procurement list. The heater, its supplied components, and a Greenmade 12-gallon tote are owned, and some heater components are partially assembled. **No frame material has been purchased, and no custom structural item in §2 is purchase-ready.** No rail length, bracket, or fastener has been specified or approved.
**Date**: 2026-10-27
**Companions**: [spec.md](spec.md), [design.md](design.md)
**Evidence tags**: as defined in [spec.md §1](spec.md#1-how-to-read-this-document). Manufacturer sources M1 and M2 as in [spec.md §2](spec.md#2-manufacturer-sources).

---

## 1. Existing equipment

### 1.1 Heater system (owned)

| Item | Identity | Qty | Evidence | Notes |
|---|---|---|---|---|
| Diesel air heater, main unit | VEVOR product 010806799987; model XMZ-D2, split type; 12 V; 2 kW | 1 | User-reported (product ID); Manufacturer-stated (M2; M1 p.2, p.7, p.9) | Product size 13.4 × 4.5 × 5.5 in / 340 × 115 × 140 mm (Manufacturer-stated, M2; the 13.4 in length also User-reported by tape). Net weight 11 lb / 5 kg (Manufacturer-stated, M2) of unstated scope; standalone heater mass Unknown (Q-11). Ratings 12 V/40 W (M1 p.7); 3 A running (M2); supply ≥15 A at start (M1 p.4); no cigarette-lighter startup (M1 p.4) |
| Heater mounting plate | Supplied metal plate | 1 | User-reported dimensions 5 7/16 × 6 11/16 in, tape measure, date not established; four fixing holes about 1/4 in diameter with about 1/8 in edge clearance (User-reported 2026-10-28, not measured); thickness estimated about 1/32 in (owner estimate 2026-10-28, not measured) | Listed as "machine fixing piece" (M1 p.8). Fixing pattern User-reported, not Measured (Q-03; checklist PLT-03 to PLT-09). The plate is thin sheet, not a structural carrier ([design.md §5](design.md#5-heater-mounting)) |
| Fuel tank | Supplied 10 L (2.6 gal) tank | 1 | Manufacturer-stated capacity (M2, M1 p.8); User-reported size about 16 × 16 × 3 in excluding filler neck | Three recessed mounting points, reported as membrane-covered on some holes (2026-10-27) and as three through-holes (2026-10-28); unresolved until recorded (TNK-10 to TNK-12). Empty mass Unknown |
| Tank mounting accessories | "Oil tank accessories" | 1 set | Manufacturer-stated (M1 p.8) | Contents not itemized in M1; not yet inventoried (Q-02) |
| Pulse fuel pump with sheath and screw | Supplied | 1 | Manufacturer-stated (M1 p.8, p.9) | Mounting angle and orientation not stated (Q-08) |
| Oil filter | Supplied | 1 | M1 p.8 | |
| Oil pipe | Supplied | 1 | M1 p.8 | Length not stated |
| Oil pipe clips; ribbons (cable ties) | Supplied | 12; 12 | M1 p.8 | |
| Intake pipe; air filter element | Supplied | 1; 1 | M1 p.7–8 | Diameter and length not stated |
| Exhaust pipe; silencer with fixing piece and 2 screws | Supplied | 1; 1 | M1 p.7 | Diameter and length not stated |
| Clamps; pipe clips | Supplied | 4; 2 | M1 p.7 | |
| Blowpipe (hot-air duct); blowpipe clamps; rotary tuyere | Supplied | 1; 2; 1 | M1 p.7–8 | Diameter and length not stated |
| Machine fixing screws; nuts; screws for lock catch | Supplied | 4; 5; 4 | M1 p.8 | Sizes not stated |
| Power cord with in-line fuse, fuse protector, and cover | Supplied | 1 | M1 p.8, p.9 | Fuse rating and cord gauge not stated (Q-07) |
| LCD controller ("liquid crystal switch"); remote control | Supplied | 1; 1 | M1 p.7–8 | Bluetooth app "airHeaterBle" (M1 p.16) |
| User manual (paper, as supplied) | Revision unknown | 1 | M1 p.8 | Not yet compared with M1 (Q-01) |
| Assembly state | Some heater components partially assembled by the owner; which, and to what state, not recorded | — | User-reported (2026-10-27) | To be recorded during the Q-02 inventory |

The quantities above are the manufacturer's packing list for the XMZ-D2 (M1 p.7–8). **The owner has not yet confirmed them against the box** (Q-02). Any item found missing, different, or additional is to be recorded here with the date.

### 1.2 Other owned items

| Item | Status | Evidence |
|---|---|---|
| Greenmade 12-gallon tote | Purchased by the owner. **Not** the operating enclosure | User-reported (owned); Owner decision 2026-10-27 |
| Battery Box V1 (12.8 V 200 Ah LiFePO4) | Bench prototype; **not approved** to power the heater | [as-built.md](../001-battery-box/as-built.md); [verification-and-safety.md](../001-battery-box/verification-and-safety.md) |

## 2. Preliminary procurement list — NOT PURCHASE-READY

This list names categories so the design can be costed and reviewed. Rows gated **G1** are custom structural materials for the frame: **no quantity, length, part number, or supplier for them is approved for purchase.** They are blocked by gate G1 in [spec.md §10](spec.md#10-release-gates) and become purchasable only when G1's conditions are met and the owner explicitly approves the purchase. Rows gated otherwise are not structural materials and are not blocked by G1; the owner may buy them at any time, and the CO alarm in particular may be bought before G1. Each is required before the gate named.

| Category | Preliminary description | Qty | Readiness | Gate | Blocked by |
|---|---|---|---|---|---|
| T-slot aluminum extrusion | 20 × 40 mm profile, 20 members per [design.md §3](design.md#3-member-schedule-preliminary-count-20) (an 18-member candidate is under assessment, D-14), for the B1 Adjusted envelope of about 20 × 22 × 35 in (MR-02 as amended 2026-10-28) | 20, **lengths not derived** | Not purchase-ready | G1 | D-01, D-02, D-14, MR-05 concept review; envelope preliminary |
| Extrusion joining hardware | Interior corner brackets with sliding T-nuts at every joint and gussets at the base corners are the proposed concept (D-01, design.md §3); end-tapped fasteners the alternative. Sliding brackets also carry the heater crossmembers and the tank rails so their positions can be adjusted to the plate holes and the tank bosses | Not counted | Not purchase-ready | G1 | D-01, D-02, D-04, MR-05 concept review |
| Heater plate fasteners | Fasteners from the plate to the H-X crossmembers | Not counted | Not purchase-ready | G1 | Q-03 |
| Tank fasteners | Fasteners through the three tank points to the T-R rails | Not counted | **Not purchase-ready; not to be selected** until boss suitability and hole preparation are established | G1 | Q-02, Q-04, Q-05, MR-04 |
| Stabilization hardware | Outriggers, adjustable feet, or other method | None selected | Not purchase-ready | G1 | D-12, SR-10 concept |
| Exhaust restraint and shielding | Pipe clamps to the frame; heat shield if engineering review requires | None selected | Not purchase-ready | G5 | D-07, SR-04 |
| Duct support | Strain relief for the blowpipe at the frame | None selected | Not purchase-ready | G5 | D-08 |
| Weather measure | Partial cover or none | None selected | Not purchase-ready | G5 | D-10, TR-01 |
| Transport restraint and lifting | Tie-down points, handles | None selected | Not purchase-ready | G4 | D-11, MR-06 |
| Carbon-monoxide alarm for the shelter | **Mandatory** for operation (SR-06); not a substitute for the exhaust and inlet review (SR-11) | 1 | Not G1-gated; may be bought at any time | G5 | Q-09 (which alarm) |
| Electrical supply cable, connector, fuse | Deferred to Battery Box V2; none selected (ER-05) | — | Out of scope here | G3 | ER-03, ER-05 |

**Deliberately absent**: tank shelf, full backplate, wooden mock-up materials, plastic enclosure (owner decisions 2026-10-27; [design.md §16](design.md#16-alternatives-considered-and-rejected)).

## 3. What must happen before custom structural materials are bought (gate G1)

These are the conditions of gate G1 in [spec.md §10](spec.md#10-release-gates), restated here so the two documents cannot drift. They apply to the G1 rows in §2 only.

1. Q-01 to Q-08 answered (Q-01, Q-02, Q-03, Q-07 by owner inspection; Q-04, Q-05, Q-06, Q-08 by VEVOR support), or recorded as unanswerable with the engineering judgement that replaces each, with dates in design.md.
2. SR-01 reconciled in writing; the tank wall and height fixed (D-03).
3. Tank mounting method established (MR-04, H-01).
4. D-01, D-02, D-04, D-12 decided.
5. Footprint, material section, structural load path, mounting method, and stability concept reviewed far enough to produce a purchase-ready cut list and compatible hardware (MR-05 and SR-10 at concept level). Full structural acceptance is gate G2; operating validation is gate G5.
6. The owner explicitly approves the purchase.

No cut list is produced in this document.

## Change log

| Date | Change |
|---|---|
| 2026-10-27 | Created. Existing equipment per the owner's brief and the manufacturer's packing list; procurement list is categories only; nothing purchase-ready. |
| 2026-10-27 | PR #4 review corrections: status distinguishes owned heater equipment (partly assembled) from the unpurchased frame; manufacturer size and net weight (scope unknown) recorded; §2 rows carry their gate, separating G1 custom structural materials from other supplies; §3 restates the G1 conditions from spec.md. |
| 2026-10-28 | Plate hole pattern, edge clearance, and thickness estimate recorded as User-reported; tank hole state recorded as reported on two dates, unresolved. Extrusion row refers to the B1 Adjusted envelope and the 18-member candidate; joining-hardware row names the sliding-bracket concept. Nothing purchase-ready; G1 conditions in §3 unchanged. |
