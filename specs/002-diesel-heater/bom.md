# Diesel Heater Module (002) — Bill of Materials

**Status**: Inventory of owned equipment and a preliminary procurement list. The heater, its supplied components, and a Greenmade 12-gallon tote are owned, and some heater components are partially assembled. **No frame material has been purchased, and no custom structural item in §2 is purchase-ready.** A **proposed** purchase package with supplier part numbers, quantities, and prices read on 2026-10-29 is in §2.2, following the owner's 2026-10-29 selection of 2020 extrusion and the ZYLtech M5 hardware system; it is not reviewed or approved, and no length is an approved cut length.
**Date**: 2026-10-27
**Companions**: [spec.md](spec.md), [design.md](design.md)
**Evidence tags**: as defined in [spec.md §1](spec.md#1-how-to-read-this-document). Manufacturer sources M1 and M2 as in [spec.md §2](spec.md#2-manufacturer-sources).

---

## 1. Existing equipment

### 1.1 Heater system (owned)

| Item | Identity | Qty | Evidence | Notes |
|---|---|---|---|---|
| Diesel air heater, main unit | VEVOR product 010806799987; model XMZ-D2, split type; 12 V; 2 kW | 1 | User-reported (product ID); Manufacturer-stated (M2; M1 p.2, p.7, p.9) | Product size 13.4 × 4.5 × 5.5 in / 340 × 115 × 140 mm (Manufacturer-stated, M2; the 13.4 in length also User-reported by tape). Net weight 11 lb / 5 kg (Manufacturer-stated, M2) of unstated scope; standalone heater mass Unknown (Q-11). Ratings 12 V/40 W (M1 p.7); 3 A running (M2); supply ≥15 A at start (M1 p.4); no cigarette-lighter startup (M1 p.4) |
| Heater mounting plate | Supplied metal plate | 1 | User-reported dimensions 5 7/16 × 6 11/16 in, tape measure, date not established; four fixing holes about 1/4 in diameter with about 1/8 in edge clearance (User-reported 2026-10-28, not measured); thickness estimated about 1/32 in (owner estimate 2026-10-28, not measured) | Listed as "machine fixing piece" (M1 p.8). Fixing pattern User-reported, not Measured (Q-03; checklist PLT-03 to PLT-09). The heater-to-plate and plate-to-frame interfaces and their combined load path are unresolved ([design.md §5](design.md#5-heater-mounting), D-16) |
| Fuel tank | Supplied 10 L (2.6 gal) tank | 1 | Manufacturer-stated capacity (M2, M1 p.8); User-reported size about 16 × 16 × 3 in excluding filler neck | Three recessed mounting points, each a through-mounting passage covered by a thin plastic membrane intended to be pierced at installation (owner's established description, User-reported 2026-10-29, reconciling the 2026-10-27 and 2026-10-28 reports; [spec.md §5](spec.md#5-existing-equipment)). Passage and boss dimensions, local wall thickness, fastener, membrane-opening method, sealing, and bearing strength remain open (TNK-10 to TNK-14; Q-04, Q-05, MR-04); no hole preparation authorized. Empty mass Unknown |
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
| T-slot aluminum extrusion | **2020 (20 × 20 mm, 6 mm slot) for every member** (Owner decision 2026-10-29, MR-01 as amended; the 20 × 40 mm quantities recorded before that date are withdrawn and do not apply). Proposed supply: ZYLtech EXT-2020 (§2.2). B1 Adjusted envelope of about 20 × 22 × 35 in (MR-02). **Primary structure**: the 20 members of MR-01 per [design.md §3](design.md#3-member-schedule-preliminary-count-20): 4 uprights at 889.0 mm, 8 widthwise members at 468.0 mm, 8 depthwise members at 518.8 mm, about 11.45 m as the sum of the nominal modelled lengths (`cad/out/adjusted/member-schedule.md`; with a 20 mm section the depth members and rails are 40 mm longer than under the withdrawn assumption). **No stabilization members**: foot bars are excluded from the initial purchase and build (Owner decision 2026-10-29, design.md §10). **Initial build total**: 20 pieces, **11.45 m nominal** before kerf and offcut. **Proposed stock order**: 6 × 2000 mm (12.0 m, about 5 % kerf and offcut) in the preferred arrangement of 4 bars of 889 + 518.8 + 518.8 and 2 bars of 4 × 468, which leaves 64.4 mm on its tightest bars at the assumed 3 mm kerf (delivered length and real kerf still to be checked) per `cad/out/adjusted/cut-schedule.md`, a sizing estimate, not a cut list. Nominal model lengths are not approved fabrication dimensions until the G1(e) review and owner approval | 20 pieces, 11.45 m nominal; 6 × 2000 mm proposed | Not purchase-ready | G1 | MR-05 concept review of the 2020 section and joints; envelope preliminary |
| Extrusion joining hardware | **Selected system (Owner decision 2026-10-29, D-01; adequacy open, MR-05):** ZYLtech 2020, 6 mm slot, M5. Metal 90-degree corner brackets (2028 type, 20 × 28 × 28 mm) with M5 hammer nuts and M5 button-head screws; flat 90-degree joining plates (60 × 60 × 4 mm, five M5 holes) at the base corners. **Counting basis**: 16 horizontal members with 32 ends, one bracket per end plus one additional at each end of the four loaded members gives **40 primary brackets**; 8 joining plates, two per base corner. No stabilization attachments (excluded, see the stabilization row). Screws and nuts per connection are allocated in §2.2 from the kit contents; the kit's 12 three-way connectors are not used. End caps for the four upright tops are optional (not in the kit) | 40 brackets, 8 plates, screws and nuts per §2.2 | Proposed package in §2.2; not purchase-ready | G1 | MR-05 concept review; bracket thickness and T-nut data not stated by the supplier (§2.1) |
| Heater plate fasteners (Interface B) | Four M5 button-head screws from the kit with M5 flat washers into M5 hammer nuts in the crossmember top slots, through the plate's four reported 1/4 in corner holes (radial clearance about 0.7 mm if the holes are as reported). **Screw length is not fixed by the kit's 8 mm and 10 mm sizes**: it follows from the plate thickness (owner estimate about 1/32 in, PLT-03) plus the washer and the nut engagement, set at the dry fit against the plate as found (PLT-06 to PLT-09, design.md §5). Interface A (the heater's own fixings) is the supplied factory arrangement and is not a purchase item | 4 screws, 4 washers, 4 hammer nuts (from §2.2 stock) | Not purchase-ready | G1 | Q-03, D-16 (dry fit); PLT-03, PLT-06 |
| Tank fasteners | Rail side: three M5 hammer nuts in the rail slots (Owner decision 2026-10-29, the same system as every joint). Tank side: **not selectable**. The bolt length, the large washer or supplied grommet that spreads the load on the plastic, the membrane-opening method, and sealing are to be engineered to the tank's three membrane-closed passages (design.md §6, owner's established description 2026-10-29), not forced to fit the kit's screws or hammer bolts | 3 hammer nuts (from §2.2 stock); bolts and washers not counted | **Not purchase-ready; tank-side parts not to be selected** until boss suitability and hole preparation are established | G1 | Q-02, Q-04, Q-05, MR-04 |
| Stabilization hardware | **Excluded from the initial purchase and build (Owner decision 2026-10-29, D-12; design.md §10).** No foot bar, leveling foot, outrigger, ballast, or attachment bracket is in the package. Kept as a potential future enhancement, reconsidered only if the SR-10 stability verification before fuelled operation (G5) requires it; the options and the 2026-10-29 catalogue check (no 2020-compatible leveling foot at ZYLtech) are on record in design.md §10 | None | Not in the package | G5 (verification), not G1 | SR-10 verification of the built module |
| Exhaust restraint and shielding | Pipe clamps to the frame; heat shield if engineering review requires | None selected | Not purchase-ready | G5 | D-07, SR-04 |
| Duct support | Strain relief for the blowpipe at the frame | None selected | Not purchase-ready | G5 | D-08 |
| Weather measure | Partial cover or none | None selected | Not purchase-ready | G5 | D-10, TR-01 |
| Transport restraint and lifting | Tie-down points, handles | None selected | Not purchase-ready | G4 | D-11, MR-06 |
| Carbon-monoxide alarm for the shelter | **Mandatory** for operation (SR-06); not a substitute for the exhaust and inlet review (SR-11) | 1 | Not G1-gated; may be bought at any time | G5 | Q-09 (which alarm) |
| Electrical supply cable, connector, fuse | Deferred to Battery Box V2; none selected (ER-05) | — | Out of scope here | G3 | ER-03, ER-05 |

**Deliberately absent**: tank shelf, full backplate, wooden mock-up materials, plastic enclosure (owner decisions 2026-10-27; [design.md §16](design.md#16-alternatives-considered-and-rejected)).

### 2.1 Supplier compatibility criteria (evidence to obtain before G1)

Profiles sold as "2020" differ between suppliers in slot width, wall thickness, alloy, and the bracket and T-nut families that fit them. Extrusion, brackets, T-nuts, plates, and foot hardware are to come from one compatible family (ZYLtech, Owner decision 2026-10-29), and the following are to be obtained and recorded in design.md before G1(e) is reviewed. None of it is assumed. The status column records what the ZYLtech product pages stated when read on 2026-10-29; "not stated" means a supplier inquiry, a drawing, or a measured sample is still needed.

| Item | Why it is needed | Status from the ZYLtech pages, 2026-10-29 |
|---|---|---|
| Alloy and temper (6063-T5 or T6 is usual; confirm) and the section drawing with slot width and wall thickness | Fit of T-nuts and brackets; the MR-05 review | **Not stated** on the EXT-2020 page (it gives "20mm x 20mm T slot", a 5 mm centre bore "designed for 1/4-20 NC and M6-1.0 thread", silver or black anodized). The 6 mm slot is stated on the hardware-kit page, not the extrusion page |
| Section properties (area, second moments about both axes, mass per metre) | Frame mass for the SR-10 outline and TR-03; the MR-05 review | **Not stated** |
| T-nut type (drop-in or slide-in), thread, recommended bolt torque, and any published slip or pull-out load | The joints and the sliding crossmembers and rails carry load only through T-nut clamping; D-01, D-16, and the Interface B fit with the 1/4 in plate holes | Hammer nuts (drop-in, rotate to lock), M5 (or M4) for 2020, **stated**; torque and loads **not stated** |
| Corner bracket material, dimensions, thickness, and any rated load | D-01; racking stiffness is a joint property | "Aluminum", 20 × 28 × 28 mm **stated**; thickness, alloy, and load **not stated** (the screw length for the brackets depends on the thickness, §2.2) |
| Joining plate dimensions and hole pattern | Base-corner racking stiffness | 60 × 60 mm, 4 mm aluminum, M5, screws and nuts not included **stated**; hole count not stated (five implied by the SKU) |
| Foot attachment and leveling foot thread and load rating; whether feet need tapped extrusion ends | Only if stabilization hardware is later added (D-12 excluded it from the initial build) | Not needed for the initial purchase. For the record: **no 2020-compatible leveling foot listed**; the 2020 bore is stated to suit an M6 tap |
| Cutting service tolerance and whether ends are square | Bracket joints absorb small errors; the cut list at G1(e) depends on it | **Not stated** for the pre-cut lengths |

Supplier figures are Manufacturer-stated when recorded and do not by themselves establish adequacy; the MR-05 review does.

### 2.2 Proposed purchase package (ZYLtech 2020; prices read 2026-10-29)

**Proposed, not approved.** Prices are list prices read from the ZYLtech product pages on 2026-10-29 and are dated estimates, not specifications; they exclude shipping, tax, and quantity discounts, and they change. The package is to be reviewed under G1(e) and approved by the owner (G1(f)) before anything is ordered. The hardware kit was shown **out of stock** on 2026-10-29.

| # | Item | Supplier SKU and link | Qty | List price 2026-10-29 | Role in the frame |
|---|---|---|---|---|---|
| 1 | 2020 6 mm-slot hardware kit, 632 pieces, silver | HW-2020-EXTHWKIT-SLVR, <https://www.zyltech.com/2020-6mm-slot-t-slot-v-groove-aluminum-extrusion-hardware-kit-632-pcs/> | 1 | $59.95 (out of stock when read) | Contents as listed by the supplier: 48 × 2028 90° brackets, 12 × 3-way connectors, 100 × M5 hammer nuts, 100 × M5×8 and 50 × M5×10 button-head screws, 20 × M5×16 hammer bolts, 100 × M5 flat washers, 100 × M5 lock washers, 100 × M5 hex nuts, container. Supplies the 40 brackets and most screws and nuts |
| 2 | M5 hammer nuts for 2020, 100-pack | HW-20-HAMMER-P (M5 variant), <https://www.zyltech.com/100x-zyltech-hammer-nuts-t-slot-for-2020-aluminum-extrusion-m4-or-m5/> | 1 | $9.95 | Brings the hammer-nut count to 200 against 127 allocated below plus spares |
| 3 | 2020 90° T joining plate, black, 60 × 60 × 4 mm, M5 | HW-2020-T5HOLE-BRKT-BLK, <https://www.zyltech.com/2020-90-degree-t-joining-plate-black/> | 8 | $2.95 each, $23.60 | Two per base corner (screws and nuts not included) |
| 4 | 2020 T-slot extrusion, 2000 mm | EXT-2020, <https://www.zyltech.com/2020-t-slot-aluminum-extrusion-pre-cut-lengths-300mm-2000mm/> | 6 | **Per-length price not displayed**; the page lists $5.94 to $33.54 across 300 to 2000 mm, so at most about $201.24 for six if $33.54 is the 2000 mm price (inference, to be confirmed in the cart) | The proposed stock order of `cad/out/adjusted/cut-schedule.md` for the 20 members; a spare bar is a separate owner choice |
| 5 | End caps for 2020, 10-pack (optional) | HW-2020-CAP, <https://www.zyltech.com/2020-end-cap-cover-10-pack/> | 1 | $5.45 | Four upright tops; cosmetic |

Stabilization hardware is not in the package (Owner decision 2026-10-29; design.md §10).

**Estimated cost, dated 2026-10-29, excluding shipping and tax:** items 1 to 3 total $93.50; with the optional end caps $98.95; with the extrusion at the inferred upper bound, about $295 to $300. If the kit stays out of stock, its brackets, screws, and nuts would have to be bought separately (for example 12-packs of 2028 brackets, SKU HW-2020ANGBR-REG-90DEG-LG-12x at $9.95, four packs for 48), which changes the cost and is not priced here.

**Screw and hammer-nut allocation from the kit (provisional; lengths to be confirmed, not assumed):**

| Connection | Count | Screws | Hammer nuts | Washers | Length basis and caveat |
|---|---|---|---|---|---|
| 2028 corner brackets, primary joints | 40 brackets, 80 screw positions | 80 × M5×8 (kit) | 80 | — | The bracket thickness is not stated by the supplier. M5×8 is provisional for a bracket up to about 3 mm thick; a thicker bracket needs M5×10, of which the kit has only 50, 40 of them allocated to the plates. **Measure a delivered bracket before finalizing** |
| Joining plates, base corners | 8 plates, 40 positions | 40 × M5×10 (kit) | 40 | — | Through the 4 mm plate an M5×10 projects 6 mm and an M5×8 projects 4 mm (less any washer). **Projection is not engagement**: the thread actually engaged inside the hammer nut is the projection minus the slot lip and clearance above the nut's thread, which depends on the nut geometry the supplier does not state. M5×10 is proposed; the real engagement, any bottoming of the screw on the slot floor, and the fit are to be verified on a sample joint before the plates are fitted |
| Interface B, heater plate to crossmembers | 4 | 4 × M5, length per the dry fit (M5×8 provisional) | 4 | 4 flat (kit) | Plate about 0.8 mm (estimate) plus washer; confirm against the plate as found |
| Tank points, rail side | 3 | **not selectable** | 3 | per the tank-side engineering | Tank side engineered to the tank (design.md §6) |
| **Totals allocated** | | 84 × M5×8 of 100; 40 × M5×10 of 50 | 127 of 200 | 4 of 100 flat | Kit spares: 16 × M5×8, 10 × M5×10, 20 × M5×16 hammer bolts, 8 brackets, 12 three-way connectors; 73 hammer nuts |

The allocation shows that the kit's two screw lengths are not assumed to suit every connection: the bracket length depends on an unstated thickness, the Interface B length on the plate as found, and the tank side is not selected at all. For every screw, the projection beyond the clamped part is distinct from the thread engaged in the hammer nut; engagement, bottoming, and fit are to be verified on a sample joint for each connection type before assembly.

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
| 2026-10-29 | G1 hardware categories refined with provisional counts for costing only: one supplier family, interior corner brackets doubled on the loaded members, gussets, Interface B bolts (M5 through the 1/4 in holes), fixed foot bars with leveling feet as the preferred stabilization direction (about 28 in footprint). §2.1 added: supplier compatibility criteria and the evidence to obtain before G1(e). Nothing purchase-ready; no length derived; G1 conditions in §3 unchanged. Codex corrections the same day: extrusion row separates the 20 primary members (about 11.13 m, modelled nominal lengths) from the two proposed foot bars (about 1.42 m) and gives the combined 22 members at about 12.55 m before allowances; bracket, gusset, and T-nut counting basis stated (40 primary brackets from 32 member ends plus 8 on the loaded members; 8 gussets as two per base corner; about 127 T-nuts itemized plus spares); M5 stated as a proposed selection subject to the supplier system with the plate-hole fit to be checked. |
| 2026-10-29 | Owner decisions: 2020 (20 × 20 mm, 6 mm slot) extrusion for every member and the ZYLtech M5 hardware system. §2 rows rewritten for 2020: 22 pieces at 12.87 m nominal (the 20 × 40 mm quantities withdrawn), 7 × 2000 mm proposed stock order from the CAD cut schedule, 44 corner brackets and 8 joining plates, Interface B hardware named with the screw length left to the dry fit, tank fasteners M5 on the rail side only, feet not selected because the supplier lists no 2020-compatible leveling foot. §2.1 gains a status column for what the supplier pages state. §2.2 added: the proposed purchase package with SKUs, links, dated list prices (kit out of stock when read), and the screw and hammer-nut allocation. Nothing purchase-ready; G1 conditions in §3 unchanged. |
| 2026-10-29 | Owner decision: stabilization hardware excluded from the initial purchase and build. Extrusion row reduced to the 20 members of MR-01 (11.45 m nominal, 6 × 2000 mm proposed order); joining-hardware row 40 brackets; stabilization row marked excluded and kept as a future enhancement; §2.2 package and allocation without feet or foot-bar brackets (extrusion qty 6; 127 of 200 hammer nuts; 84 of 100 M5×8). Nothing purchase-ready. |
