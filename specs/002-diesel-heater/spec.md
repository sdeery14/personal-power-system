# Diesel Heater Module (002) — Specification

**Status**: Draft specification. **Nothing has been built, purchased, or approved for fabrication.**
**Date**: 2026-10-27
**Companions**: [design.md](design.md) (preliminary mechanical concept, hazard register, open decisions), [bom.md](bom.md) (existing equipment and preliminary procurement list)
**Governing documents**: [constitution](../../.specify/memory/constitution.md) v1.0.0, [vision.md](../../vision.md)
**Related system**: [Battery Box V1](../001-battery-box/as-built.md), which is **not approved** to power this module

---

## 1. How to read this document

Every hardware statement carries an evidence tag. The tags follow [as-built.md §1](../001-battery-box/as-built.md#1-how-to-read-this-document) with two additions for a subsystem that has not yet been built:

| Tag | Meaning in this specification |
|---|---|
| **Manufacturer-stated** | Taken from a VEVOR document, cited with page or URL and the retrieval date. Not independently checked |
| **User-reported** | Stated by the project owner. Tape-measure dimensions are User-reported, not Measured, because the measurement dates and method records are not all established |
| **Owner decision** | A design choice the owner has made, dated. Binding on the design unless a safety or structural finding reopens it |
| **Proposed** | A value, approach, or estimate put forward in this specification for review. Not approved |
| **Unknown** | No evidence, conflicting evidence, or a question the manufacturer documentation does not answer |

Nothing in this specification is Measured or Verified. Requirements marked **RECONCILE** contain manufacturer statements that pull in different directions and must be resolved in writing before the design is approved.

## 2. Manufacturer sources

| ID | Source | Retrieved | Notes |
|---|---|---|---|
| **M1** | VEVOR user manual "Diesel Heater", models XMZ-D1 and XMZ-D2, 22 printed pages, hosted by VEVOR at <https://d2v0huudrf11kh.cloudfront.net/vevor-center-goods/VEVOR-Diesel-Heater_1691547766381.pdf> | 2026-10-27 | No revision number or date is printed in the document. The file name's numeric suffix corresponds to 2023-08-09 if read as a Unix millisecond timestamp (Proposed inference). Page 2 states the product appearance may differ from the manual. **The revision supplied in the owner's box has not been compared with this file** (see Q-01 in design.md) |
| **M2** | VEVOR product page for product 010806799987, <https://www.vevor.com/diesel-heater-c_10321/vevor-diesel-air-heater-12v-2kw-bluetooth-app-lcd-display-for-car-bus-rv-indoors-p_010806799987> | 2026-10-27 | Identifies the model as XMZ-D2. Specification figures and a customer Q&A section. Q&A answers are less authoritative than M1 |

Citations below use the form M1 p.N (printed page number) or M2.

## 3. Problem statement and use case

The owner winter-camps and needs a reliable source of heated air in a tent or similar shelter. The constitution names "stay warm while winter camping (diesel heater operation)" as a defined use case (Principle VI), and vision.md lists diesel heater operation in cold weather as an intended mobile use. The heater exists; what is missing is a safe, portable, self-supporting way to carry, set up, and operate it with its fuel tank, exhaust, intake, and ducting outside the shelter.

The module is a frame that holds the heater and its supplied fuel tank in a fixed, serviceable arrangement that can be moved as a unit, stood on uneven ground, and connected to a power source and a hot-air duct.

## 4. Scope

### 4.1 In scope for this specification

- Requirements for a portable frame carrying the VEVOR XMZ-D2 heater, its supplied 10 L tank, fuel pump, intake, exhaust, and hot-air outlet.
- Requirements that the manufacturer documentation imposes on mounting, routing, ventilation, and power supply.
- Safety, stability, transport, and weather requirements that must be satisfied before first operation.
- Gates that must be passed before materials are purchased, before fabrication, and before first operation.

### 4.2 Out of scope (owner decisions, 2026-10-27, and project rules)

- A fuel-tank shelf, a full backplate, a wooden mock-up, or a plastic operating enclosure. These are not to be added unless a specific structural or safety need is demonstrated in writing (see design.md §16).
- Use of the Greenmade 12-gallon tote as an operating enclosure.
- Any modification to the heater, its fuel system, or its supplied electrical harness.
- Connecting the heater to Battery Box V1. The battery box has no approved load connector and open safety concerns ([verification-and-safety.md](../001-battery-box/verification-and-safety.md)). The electrical interface is specified here only as requirements on a future Battery Box V2.
- Operating procedures, energized tests, and any instruction that involves fuel or fire. Those require engineering review and owner approval and are not written in this PR.
- Indoor or in-tent placement of the heater unit itself. The heater is to be placed outside the shelter with only the hot-air duct entering it (SR-05).

## 5. Existing equipment

| Item | Identity | Evidence |
|---|---|---|
| Heater | VEVOR 12 V diesel air heater, product 010806799987, model XMZ-D2, "split type" (separate tank, pump, and controller) | User-reported (product ID); Manufacturer-stated (model and type, M2; M1 p.2, p.9) |
| Heater body size | approximately 13.4 × 4.5 × 5.5 in | User-reported; source of the figure not stated. M2 does not list dimensions |
| Heater mounting plate | Supplied metal plate, 5 7/16 × 6 11/16 in | User-reported, tape measure, date not established. M1 p.9 shows the plate with a seal and "double head screw nut" fixings; M1 p.8 lists "machine fixing piece" ×1 and "machine fixing screws" ×4 |
| Fuel tank | Supplied 10 L (2.6 gal) tank, approximately 16 × 16 × 3 in excluding filler neck | Manufacturer-stated capacity (M2; M1 p.8 "fuel tank" ×1); User-reported dimensions, tape measure, date not established |
| Tank mounting points | Three recessed points: two lower points horizontally aligned about 6 13/16 in apart; one upper point about 7 7/8 in above the lower row. Some holes have thin plastic membranes | User-reported, tape measure, date not established. M1 p.9 shows screws on the tank and the text "use this screw to tighten the fuel tank fixed to the metal plate of the vehicle"; M1 p.8 lists "oil tank accessories" ×1 (contents not itemized) |
| Supplied accessories | Intake pipe, exhaust pipe, silencer with fixing piece, blowpipe (hot-air duct), rotary tuyere, clamps, pipe clips, air filter element, oil pipe, oil filter, pulse fuel pump with sheath, LCD switch, remote, power cord | Manufacturer-stated packing list (M1 p.7–8). **Not yet inventoried by the owner against the box** (Q-02) |
| Greenmade 12-gallon tote | Owned; not the operating enclosure | Owner decision (2026-10-27) |
| Battery Box V1 | 12.8 V 200 Ah LiFePO4 bench prototype | Historical; see [as-built.md](../001-battery-box/as-built.md). Not approved for this load |

Full detail and the procurement list are in [bom.md](bom.md).

## 6. Manufacturer constraints on record

These are the statements in M1 and M2 that bear on the design. They are quoted or closely paraphrased so the requirements in §7 can be traced.

| Ref | Statement | Source |
|---|---|---|
| C1 | Not for use "in places where they may form flammable vapor or dust"; "keep away from fuel tanks, compression tanks, fire extinguishers, clothes, or other flammable objects" | M1 p.3–4, Safety Instruction 3 |
| C2 | "Do not use the heater in closed and/or unventilated places" | M1 p.4, item 5 |
| C3 | "The heaters shall be turned off when filling fuel" | M1 p.4, item 6 |
| C4 | "Do not cut off the electric power in operation"; "it is forbidden to cut off the electric power directly to stop the heater from working"; after turning off, do not disconnect the power supply; "it takes 3–5 minutes for the machine to stop working completely" | M1 p.4, items 7, 10, 13 |
| C5 | On a fuel leak or discharge, contact VEVOR for repair | M1 p.4, item 8 |
| C6 | "Place the exhaust outlet outside to prevent any penetration of exhaust fumes" | M1 p.4, item 9 |
| C7 | "Seal all gaps between the mounting plate and the car body" | M1 p.4, item 11 |
| C8 | After over-temperature protection stops heating, do not power off; restart after natural cool-down | M1 p.4, item 12 |
| C9 | "When the heater is just started, the current is relatively high, so an adapter with a voltage of 12V and a current of 15A or greater is required for the power supply" | M1 p.4, item 15; "≥15A" on the p.9 and p.10–11 diagrams |
| C10 | The heater "is mainly installed in the passenger room or baggage room of the vehicle. If it cannot be installed, fix the heater under the underside of the vehicle, but be ware of splashing" | M1 p.6 |
| C11 | XMZ-D2 ratings "12V/40W"; power "2/5/8KW" (the family table; M2 states 2 kW for this product) | M1 p.7; M2 |
| C12 | "During installation, the oil tank should be properly placed above the main engine to facilitate the operation of the fuel pump" | M1 p.9 |
| C13 | Fuel path in the diagram: tank → oil pipe → oil filter → pulse fuel pump (in its sheath) → oil pipe → heater. Exhaust: heater → escape pipe → silencer "(To the outside)". Intake: intake pipe with air filter element. A fuse, fuse protector, and fuse box cover sit in the positive supply lead | M1 p.9 diagram |
| C14 | "The air inlet shall not be blocked, and keep the inlet open and clear" | M1 p.11, Warning 1 |
| C15 | "Keep the exhaust pipe clear. The exhaust pipe outlet shall be kept away from anything flammable, and avoid heating and igniting the flammable goods and loading cargo on the ground" | M1 p.11, Warning 2 |
| C16 | "The smoke exhaust pipe cannot be placed upward, but must be placed horizontally or downward" | M1 p.11–12, Warning 3 and diagram |
| C17 | Fault E-01 "Abnormal voltage": supply must not be higher than 18 V or lower than 9 V | M1 p.15 |
| C18 | Operating consumption 12 V / 3 A; fuel consumption 0.12–0.26 L/h; up to 38 h per 10 L fill; overheat protection up to 270 °C | M2 (specification section) |
| C19 | Starting current 13 A; rated current 3 A | M2, customer Q&A. **Less authoritative than C9.** Design to C9 |

**Not stated anywhere in M1 or M2** (each is therefore Unknown): heater dimensions and mass; permitted mounting orientation and tilt; clearance distances from the heater body, exhaust, or silencer to surrounding materials; fuel pump mounting angle and orientation; maximum fuel line length or lift; maximum tank height above the heater; exhaust, intake, and duct pipe diameters and maximum lengths; the supplied fuse rating and wire gauge; ambient operating temperature limits (the only figure is "above −40" on M1 p.4 with the unit garbled); any carbon-monoxide guidance beyond C2 and C6.

## 7. Requirements

Requirement IDs are stable. "Source" names the constraint, principle, or decision each requirement comes from.

### 7.1 Functional

| ID | Requirement | Source |
|---|---|---|
| FR-01 | The module shall carry the heater, its supplied tank, fuel pump, oil filter, intake pipe with filter, exhaust pipe with silencer, and the controller as a single unit that can be set up without tools | Problem statement; Owner decision (frame concept, 2026-10-27) |
| FR-02 | The module shall stand on its own on level and moderately uneven ground without external anchoring | Owner decision 2026-10-27 (paracord staking is not a substitute for a stable frame) |
| FR-03 | The hot-air outlet shall accept the supplied blowpipe and rotary tuyere and allow a duct run to the shelter | C13; M1 p.7 packing list |
| FR-04 | The lower level shall remain open for access to the intake, exhaust, fuel-line, and electrical connections | Owner decision 2026-10-27 |
| FR-05 | The tank shall be mounted upright with its filler cap at the top, broad face against the mounting rails, using its three factory mounting points | Owner decision 2026-10-27; C12 and C13 |

### 7.2 Safety

| ID | Requirement | Source |
|---|---|---|
| SR-01 | **RECONCILE.** The tank shall be placed above the heater as the manufacturer instructs for pump operation (C12) **and** the heater shall be kept away from fuel tanks and flammable objects (C1). The design shall state, with engineering review, what vertical and horizontal separation, shielding, or spill control satisfies both before the layout is approved. Neither statement alone resolves the other | C1, C12 |
| SR-02 | No credible fuel spill path, from the filler neck, tank seams, mounting points, fittings, oil filter, or pump, shall reach the heater body, the exhaust, or the silencer. Refuelling spills shall be considered as well as leaks in operation | C1, C3, C5, C15; constitution I |
| SR-03 | The exhaust shall run horizontally or downward from the heater, never upward, and shall terminate outside the frame envelope and outside any shelter | C6, C16 |
| SR-04 | The exhaust pipe and silencer shall be kept clear of the tank, fuel lines, wiring, ground cover, and anything flammable, with a clearance distance that is set by engineering review since the manufacturer gives none | C15; §6 "not stated" |
| SR-05 | The heater unit, tank, exhaust, and intake shall be outside the shelter. Only the hot-air duct may enter it. The module shall not be operated in a closed or unventilated place | C2, C6 |
| SR-06 | A carbon-monoxide alarm inside the shelter is a proposed requirement for first operation, to be confirmed at the first-operation gate | Proposed; constitution I |
| SR-07 | The combustion-air inlet shall be unobstructed in every configuration, including with the duct, tank, and any weather cover fitted | C14 |
| SR-08 | The power supply shall not be interrupted during operation or during the 3–5 minute cool-down after shutdown. Any disconnect, fuse, low-voltage cutoff, or battery protection on the supply shall be reviewed against this before it is specified | C4, C8 |
| SR-09 | No fuel shall be added while the heater is running | C3 |
| SR-10 | With the tank full and the module standing on the worst-case ground it is specified for, it shall resist tipping under a handling push, a duct pull, and wind, to criteria set at engineering review | Constitution I; design.md §10 |

### 7.3 Mechanical

| ID | Requirement | Source |
|---|---|---|
| MR-01 | The frame shall be an open three-level rectangular frame of aluminum T-slot extrusion, 20 × 40 mm where suitable, with four continuous uprights, three perimeter rectangles, two widthwise heater crossmembers, and two lengthwise tank rails | Owner decision 2026-10-27 |
| MR-02 | The external envelope shall be about 20 in wide × 24 in deep × 38 in tall. **This is a preliminary envelope, not a set of cut lengths** | Owner decision 2026-10-27, preliminary |
| MR-03 | The heater shall mount on its supplied metal plate, which shall be carried by the two widthwise crossmembers at the middle level | Owner decision 2026-10-27; M1 p.9 |
| MR-04 | The tank shall be mounted through its three factory points to the two lengthwise rails. The suitability of the plastic bosses, the preparation of the membrane-covered holes, and the fastener type shall be established before any fastener is chosen or any hole is opened | Owner decision 2026-10-27; §6 "not stated"; Q-04, Q-05 |
| MR-05 | Every load-bearing member, joint, and fastener shall be shown adequate for the heater, the full tank, handling loads, and transport loads before fabrication. No member, joint, boss, or fastener is assumed adequate | Constitution I, VII; owner instruction 2026-10-27 |
| MR-06 | Lifting points or handles and vehicle tie-down points shall be defined | Constitution I; design.md §13 |
| MR-07 | The mounting plate interface shall be designed so that the heater's intake, exhaust, and fuel connections pass below the plate into the open lower level, and the sealing instruction (C7), written for a vehicle floor, shall be interpreted for an open frame at engineering review | C7, C13 |

### 7.4 Electrical

| ID | Requirement | Source |
|---|---|---|
| ER-01 | The supply shall be nominal 12 V, capable of at least 15 A at start, and shall hold the heater's input between 9 V and 18 V under start and running conditions including cable drop | C9, C17 |
| ER-02 | The supplied power cord and its in-line fuse shall be used as delivered. The fuse rating and wire gauge shall be read from the supplied parts and recorded before the supply cable is sized | C13; Q-07 |
| ER-03 | Connection to the project's battery system is deferred to Battery Box V2. The V2 interface shall provide a dedicated, fused branch meeting ER-01 and SR-08, with a connector documented per constitution Principle II | Constitution I, II; [as-built.md §4.4](../001-battery-box/as-built.md#44-branch-assignments) |
| ER-04 | Running draw (3 A, C18) and starting draw (≥15 A capability, C9; 13 A reported, C19) shall both be recorded in any runtime estimate; the 2026 battery-box runtime estimates that assumed 3–8 A are historical and not to be reused without re-derivation | C9, C18, C19; [component-selection.md](../001-battery-box/docs/component-selection.md) (historical) |

### 7.5 Environmental and transport

| ID | Requirement | Source |
|---|---|---|
| TR-01 | The module shall be specified for outdoor exposure during operation: rain, snow, condensation, and sub-freezing temperatures. The manufacturer documents vehicle-interior or under-vehicle installation only (C10), so the exposure limits of the controller, electrical connections, intake, and pump are Unknown and shall be established | C10; §6 "not stated" |
| TR-02 | Whether the tank travels full, partially full, or empty, and how the module is restrained in a vehicle, shall be decided and recorded before first transport | Constitution I |
| TR-03 | The module's total mass shall be recorded once the heater and tank masses are known | Constitution II |

### 7.6 Documentation

| ID | Requirement | Source |
|---|---|---|
| DR-01 | Every manufacturer-derived requirement cites M1 page or M2 with retrieval date | Constitution V; CLAUDE.md |
| DR-02 | Owner dimensions are tagged User-reported until a dated measurement record exists | CLAUDE.md evidence rules |
| DR-03 | Decisions, alternatives rejected, and open questions are kept in design.md with stable IDs | Constitution V |
| DR-04 | Nothing is recorded as verified, tested, or adequate without a dated record | CLAUDE.md evidence rules |

## 8. Unsupported assumptions

Listed so they are visible, not so they are accepted.

| ID | Assumption | Status |
|---|---|---|
| A-01 | The VEVOR-hosted manual (M1) matches the manual supplied with the owner's unit | Unknown; Q-01 |
| A-02 | The heater is intended to be mounted upright on its plate, as drawn on M1 p.9, and tolerates the small tilts a portable frame will see | Unknown; M1 states no orientation or tilt limits |
| A-03 | The tank's three bosses were designed to carry the full tank hanging on a vertical surface | Unknown; M1 p.9 shows the tank fixed to "the metal plate of the vehicle" without load guidance |
| A-04 | 20 × 40 mm extrusion with proprietary corner hardware is stiff enough for a 38 in tall frame carrying these loads | Unknown; MR-05 |
| A-05 | A 10 L fill of diesel has a mass of about 8.2–8.5 kg, from a density of 0.82–0.85 kg/L | Proposed estimate from general reference values; not measured; tank mass not included |
| A-06 | The heater's own mass is a few kilograms | Unknown; neither M1 nor M2 states it |

## 9. Acceptance criteria

### 9.1 For this documentation phase

- AC-D1 Every requirement in §7 is traceable to a constraint in §6, a constitution principle, or a dated owner decision.
- AC-D2 Every hardware figure carries an evidence tag; owner dimensions are User-reported; nothing is Measured or Verified.
- AC-D3 The hazard register in design.md §14 contains each item the owner listed as unresolved on 2026-10-27, none closed.
- AC-D4 bom.md states that no rail length or hardware item is purchase-ready.
- AC-D5 Links and anchors resolve; the Battery Box V1 documents are unchanged.

### 9.2 For the eventual physical module (outcomes only; procedures to be written and approved separately)

- AC-P1 A written engineering review has closed SR-01, SR-02, SR-04, SR-10, MR-04, and MR-05 with dated records.
- AC-P2 The owner has inventoried the supplied parts against M1 p.7–8 and recorded the fuse rating, pipe diameters, and masses.
- AC-P3 A dated measurement record exists for the plate, tank, and boss dimensions.
- AC-P4 A tip-resistance assessment with the tank full exists and is satisfied.
- AC-P5 The electrical interface meets ER-01 through ER-03 with a dated record.
- AC-P6 First operation is preceded by an approved procedure that satisfies SR-03 through SR-09.

## 10. Gates

| Gate | Opens when | Blocks |
|---|---|---|
| **G1 Materials purchase** | Q-01 through Q-08 in design.md are answered; SR-01 and MR-04 are resolved on paper; the member schedule carries reviewed cut lengths | Buying extrusion, brackets, fasteners, tank hardware |
| **G2 Fabrication** | G1 passed; MR-05 structural review and SR-10 stability assessment recorded | Cutting, assembly, opening membrane holes |
| **G3 First operation** | G2 passed; SR-02 through SR-09 satisfied; ER-01/ER-02 recorded; an approved operating procedure exists; a CO alarm decision (SR-06) is recorded | Fuel in the tank on the frame; any ignition |

**None of these gates is open.**

## 11. Constitution compliance check

| Principle | Status |
|---|---|
| I Safety First | Hazards registered, none closed. No fuel, fire, or energized procedure is written. Electrical protection for the supply is deferred to V2 with requirements stated (ER-01, SR-08) |
| II Modularity | Heater, tank, and frame are separable; electrical connector to be a documented standard type at V2 (ER-03). Non-standard items: the supplied VEVOR harness connectors (documented in bom.md as supplied) |
| III Transparency | Runtime and current are to be measured at V2, not estimated (ER-04). The controller's engineering mode displays supply voltage (M1 p.14), which can support later logging |
| IV Incremental Evolution | This phase is specification only. Build follows G1–G2; operation follows G3 |
| V Documentation | Sources, decisions, alternatives (design.md §16), and open questions carry IDs and dates |
| VI Practical Utility | Named use case: winter camping heat |
| VII Bounded Complexity | Open frame, manual operation, no automation. Rejected elements are listed with the owner's reasons |

## Change log

| Date | Change |
|---|---|
| 2026-10-27 | Created from the owner's 2026-10-27 brief and the VEVOR manual and product page retrieved the same day. Nothing built, purchased, measured, or verified. |
