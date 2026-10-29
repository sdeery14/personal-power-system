# Diesel Heater Module (002) — Specification

**Status**: Draft specification. **The heater, its supplied components, and a Greenmade 12-gallon tote are already owned, and the owner has partially assembled some heater components. No aluminum frame has been purchased or fabricated. No complete heater installation has been approved, commissioned, or verified.**
**Date**: 2026-10-27; envelope amended 2026-10-28 (MR-02)
**Companions**: [design.md](design.md) (preliminary mechanical concept, hazard register, open decisions), [bom.md](bom.md) (existing equipment and preliminary procurement list), [cad/](cad/README.md) (placeholder model of the layouts), [measurements/](measurements/README.md) (measurement workflow; no record yet)
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
| **M2** | VEVOR product page for product 010806799987, <https://www.vevor.com/diesel-heater-c_10321/vevor-diesel-air-heater-12v-2kw-bluetooth-app-lcd-display-for-car-bus-rv-indoors-p_010806799987> | 2026-10-27 | Identifies the model as XMZ-D2. A "Product specification" table (size, net weight, outlet pipe inner diameter, working temperature, electrical and fuel figures) and a customer Q&A section. Q&A answers are less authoritative than M1 |

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
- Overnight operation and unattended operation. Both are unresolved operating-policy questions (SR-12, Q-10). Neither is approved.

## 5. Existing equipment

| Item | Identity | Evidence |
|---|---|---|
| Heater | VEVOR 12 V diesel air heater, product 010806799987, model XMZ-D2, "split type" (separate tank, pump, and controller) | User-reported (product ID); Manufacturer-stated (model and type, M2; M1 p.2, p.9) |
| Heater product size | 13.4 × 4.5 × 5.5 in (340 × 115 × 140 mm) | Manufacturer-stated (M2 product specification, C21). The owner's tape measure gave the same 13.4 in length (User-reported; not Verified) |
| Heater net weight | 11 lb / 5 kg | Manufacturer-stated (M2, C22). **Scope unknown**: M2 does not say whether this is the heater alone or the kit. Not to be used as the standalone heater mass until clarified (Q-11) |
| Assembly state | Some heater components have been partially assembled by the owner; which ones, and to what state, is not recorded | User-reported (2026-10-27) |
| Heater mounting plate | Supplied metal plate, 5 7/16 × 6 11/16 in. Four fixing holes, each about 1/4 in diameter, with about 1/8 in from each hole's outside edge to its two adjacent plate edges (hole centres therefore about 1/4 in from each adjacent edge, derived). Thickness estimated at about 1/32 in, below 1/16 in | User-reported: outline by tape measure, date not established; holes and edge clearance reported 2026-10-28, not measured; thickness an owner estimate 2026-10-28, not measured. None of these is Measured; the measurement identifiers are PLT-01 to PLT-09 in [measurements/checklist.md](measurements/checklist.md). M1 p.9 shows the plate with a seal and "double head screw nut" fixings; M1 p.8 lists "machine fixing piece" ×1 and "machine fixing screws" ×4 |
| Fuel tank | Supplied 10 L (2.6 gal) tank, approximately 16 × 16 × 3 in excluding filler neck | Manufacturer-stated capacity (M2; M1 p.8 "fuel tank" ×1); User-reported dimensions, tape measure, date not established |
| Tank mounting points | Three recessed points: two lower points horizontally aligned about 6 13/16 in apart; one upper point about 7 7/8 in above the lower row. **Hole state, owner's established description (2026-10-29):** all three points are through-mounting passages closed by a thin plastic membrane that is meant to be pierced at installation. This reconciles the 2026-10-27 membrane report and the 2026-10-28 through-hole report, which described the same feature, and the owner is not asked to repeat it. The state of each point as found is still recorded under TNK-10 to TNK-12 when measured; the fastener, the membrane-opening method, sealing, plastic bearing strength, and mounting safety remain engineering questions (Q-04, Q-05, MR-04), and no hole preparation is authorized (G2) | User-reported, tape measure, date not established; hole state User-reported 2026-10-27 and 2026-10-28, clarified by the owner 2026-10-29. M1 p.9 shows screws on the tank and the text "use this screw to tighten the fuel tank fixed to the metal plate of the vehicle"; M1 p.8 lists "oil tank accessories" ×1 (contents not itemized) |
| Supplied accessories | Intake pipe, exhaust pipe, silencer with fixing piece, blowpipe (hot-air duct), rotary tuyere, clamps, pipe clips, air filter element, oil pipe, oil filter, pulse fuel pump with sheath, LCD switch, remote, power cord | Manufacturer-stated packing list (M1 p.7–8). **Not yet inventoried by the owner against the box** (Q-02) |
| Greenmade 12-gallon tote | Purchased by the owner; not the operating enclosure | User-reported (owned); Owner decision 2026-10-27 (not the enclosure) |
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
| C20 | "Do not use cigarette lighter for startup" | M1 p.4, Safety Instruction 4 |
| C21 | Product size "13.4×4.5×5.5 inch/340×115×140 mm" | M2, product specification |
| C22 | Net weight "11 lbs/5 kg". M2 does not state what the weight covers (heater alone or kit) | M2, product specification |
| C23 | "Air Outlet Pipe Inner Diameter" "3 in/76.5 mm" | M2, product specification |
| C24 | Working temperature printed as "-104℉-104℉/-40℃-40℃". The Fahrenheit figures are identical at both ends and do not correspond to the Celsius figures (−40 °C is −40 °F; 40 °C is 104 °F). **Unreliable pending clarification** (Q-11). M1 p.4 gives only "above −40" with the unit garbled | M2, product specification; M1 p.4 |
| C25 | The internal-structure diagram labels a heating-air "Air inlet", an "Air fan", and an "Air outlet" on the heater body, separate from the combustion chamber. The installation diagram labels the combustion "air intake" (intake pipe with air filter element) and the "escape-pipe (Combustion emissions)" separately | M1 p.5, p.9 |

**Not stated in M1 or M2** (each is therefore Unknown): the standalone heater mass (C22 is a net weight of unstated scope); permitted mounting orientation and tilt; clearance distances from the heater body, exhaust, silencer, or hot-air outlet to surrounding materials; required separation between the exhaust termination and either air inlet; fuel pump mounting angle and orientation; maximum fuel line length or lift; maximum tank height above the heater; exhaust and combustion-intake pipe diameters and maximum lengths, and the maximum hot-air duct run (only the outlet inner diameter, C23, is given); the supplied fuse rating and wire gauge; a usable ambient operating temperature range (C24 is internally inconsistent); any carbon-monoxide guidance beyond C2 and C6.

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

The heater has three separate air paths, and the requirements below name them deliberately (C25):

- **Combustion-air intake**: the intake pipe with air filter element, drawing air into the combustion chamber.
- **Heating-air inlet**: the fan inlet on the heater body, drawing the air that is heated and delivered through the hot-air outlet and duct into the shelter.
- **Combustion exhaust**: the escape pipe and silencer carrying combustion products.

Exhaust drawn into the heating-air inlet is delivered directly into the shelter. That path, and exhaust entering through the shelter's openings, are the module's principal carbon-monoxide hazards (H-07).

| ID | Requirement | Source |
|---|---|---|
| SR-01 | **RECONCILE.** The tank shall be placed above the heater as the manufacturer instructs for pump operation (C12) **and** the heater shall be kept away from fuel tanks and flammable objects (C1). The design shall state, with engineering review, what vertical and horizontal separation, shielding, or spill control satisfies both before the layout is approved. Neither statement alone resolves the other | C1, C12 |
| SR-02 | No credible fuel spill path, from the filler neck, tank seams, mounting points, fittings, oil filter, or pump, shall reach the heater body, the exhaust, or the silencer. Refuelling spills shall be considered as well as leaks in operation | C1, C3, C5, C15; constitution I |
| SR-03 | The exhaust shall run horizontally or downward from the heater, never upward, and shall terminate outside the frame envelope and outside any shelter | C6, C16 |
| SR-04 | The exhaust pipe and silencer shall be kept clear of the tank, fuel lines, wiring, ground cover, and anything flammable, with a clearance distance that is set by engineering review since the manufacturer gives none | C15; §6 "not stated" |
| SR-05 | The heater unit, tank, exhaust, combustion-air intake, and heating-air inlet shall be outside the shelter. Only the hot-air duct may enter it. The module shall not be operated in a closed or unventilated place | C2, C6, C25 |
| SR-06 | An appropriate, working carbon-monoxide alarm inside the occupied shelter is **mandatory** for first operation and for every operation after it. The alarm is a last line of defence: it does not replace safe exhaust and inlet arrangements (SR-03, SR-04, SR-11), and its presence does not relax any of them | Constitution I; review decision 2026-10-27 |
| SR-07 | The combustion-air intake and the heating-air inlet shall each be unobstructed in every configuration, including with the duct, tank, and any weather cover fitted | C14, C25 |
| SR-08 | The power supply shall not be interrupted during operation or during the 3–5 minute cool-down after shutdown. Any disconnect, fuse, low-voltage cutoff, or battery protection on the supply shall be reviewed against this before it is specified | C4, C8 |
| SR-09 | No fuel shall be added while the heater is running | C3 |
| SR-10 | With the tank full and the module standing on the worst-case ground it is specified for, it shall resist tipping under a handling push, a duct pull, and wind, to criteria set at engineering review | Constitution I; design.md §10 |
| SR-11 | An engineering review shall demonstrate, for the intended installation and under foreseeable wind conditions, that combustion exhaust cannot be drawn into the heating-air inlet and cannot enter the occupied shelter through its openings (door, vents, duct entry). The review's accepted protective measures (exhaust termination position and direction, separation, shielding, placement of the module relative to the shelter and prevailing wind) shall be recorded before first operation. No separation distance is specified here because the manufacturer gives none | C6, C15, C25; constitution I |
| SR-12 | Overnight operation and unattended operation are **unresolved operating-policy questions** (Q-10). Neither is approved. Nothing in this specification implies that either is acceptable | Review decision 2026-10-27 |

### 7.3 Mechanical

| ID | Requirement | Source |
|---|---|---|
| MR-01 | The frame shall be an open three-level rectangular frame of **2020 (20 × 20 mm, 6 mm slot) aluminum T-slot extrusion for every member**, with four continuous uprights, three perimeter rectangles, two widthwise heater crossmembers, and two lengthwise tank rails (20 members), joined with metal 90-degree corner brackets and M5 T-slot hardware, with flat reinforcement plates at the lower corners. Supplemental stabilization hardware (foot bars, feet, outriggers) is excluded from the initial purchase and build and kept as a potential future enhancement (Owner decision 2026-10-29, design.md §10); the basic stability verification of SR-10 still precedes fuelled operation (G5). The earlier "20 × 40 mm where suitable" basis is withdrawn and is not to be revisited. An 18-member simplification that omits the two middle-level widthwise members is a recorded alternative, deprioritized ([design.md D-14](design.md#151-decisions-design-choices-still-to-be-made)). The adequacy of the section and joints is not decided by this requirement (MR-05, A-04) | Owner decision 2026-10-27 (frame form); Owner decision 2026-10-29 (2020 section, joint hardware, foot bars) |
| MR-02 | The external envelope shall be about 20 in wide × 22 in deep × about 35 in tall (preliminary range 34 to 36 in), the **B1 Adjusted** layout: heater upright on its plate about 7 in above the base, tank upright beside the heater with its bottom above the heater body's top. **This is a preliminary envelope, not a set of cut lengths.** The previous envelope, about 20 × 24 × 38 in with the tank entirely above the heater (Owner decision 2026-10-27, "A Original"), is superseded as the preferred direction and retained as an alternative in design.md §16, as is the 20 × 22 × 28 in "B1 Compact" starting point of 2026-10-28 | Owner decision 2026-10-28, preliminary; supersedes Owner decision 2026-10-27 |
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
| ER-05 | The heater shall not be powered through a cigarette-lighter socket or plug (C20). The supply shall be a dedicated, fused connection whose cable, fuse, and connector have **not yet been selected**; they are to be specified and reviewed at the Battery Box V2 interface (ER-03) | C20; constitution I, II |

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
| A-04 | 2020 (20 × 20 mm) extrusion with 90-degree corner brackets, M5 hammer nuts, and base joining plates, standing on its four upright ends without supplemental stabilization, is stiff and strong enough for a frame about 35 in tall carrying these loads | Unknown; MR-05. The 2020 section is much less stiff in bending than the 20 × 40 mm section assumed before 2026-10-29, so upright bending and racking stiffness must be covered at the MR-05 review; the profile choice itself is an owner decision and is not reopened by this assumption |
| A-05 | A 10 L fill of diesel has a mass of about 8.2–8.5 kg, from a density of 0.82–0.85 kg/L | Proposed estimate from general reference values; not measured; tank mass not included |
| A-06 | The standalone heater mass is no more than the 11 lb / 5 kg net weight in C22 | Unknown; the scope of the M2 figure is not stated (Q-11). Not to be used in load or stability calculations until clarified |

## 9. Acceptance criteria

### 9.1 For this documentation phase

- AC-D1 Every requirement in §7 is traceable to a constraint in §6, a constitution principle, or a dated owner decision.
- AC-D2 Every hardware figure carries an evidence tag; owner dimensions are User-reported; nothing is Measured or Verified.
- AC-D3 The hazard register in design.md §14 contains each item the owner listed as unresolved on 2026-10-27, none closed.
- AC-D4 bom.md states that no custom structural material is purchase-ready and restates the same G1 conditions as §10.
- AC-D5 Links and anchors resolve; the Battery Box V1 documents are unchanged.

### 9.2 For the eventual physical module (outcomes only; procedures to be written and approved separately)

- AC-P1 A written engineering review has closed SR-01, SR-02, SR-04, SR-10, MR-04, and MR-05 with dated records.
- AC-P2 The owner has inventoried the supplied parts against M1 p.7–8 and recorded the fuse rating, pipe diameters, and masses.
- AC-P3 A dated measurement record exists for the plate, tank, and boss dimensions.
- AC-P4 A tip-resistance assessment with the tank full exists and is satisfied.
- AC-P5 The electrical interface meets ER-01 through ER-03 with a dated record.
- AC-P6 First operation is preceded by an approved procedure that satisfies SR-03 through SR-11, with a working CO alarm in the shelter (SR-06) and the SR-11 review on record.
- AC-P7 The overnight and unattended operating policy (SR-12, Q-10) is decided and recorded before any such operation; until then neither is permitted.

## 10. Release gates

Five gates separate the paper design from purchase, fabrication, power, transport, and operation. **None is open.** A gate opens only when every condition listed is met by a dated record and the owner approves that gate explicitly. An unresolved hazard that applies to the intended configuration blocks the gate for that configuration, and no gate can be bypassed by opening a later one.

| Gate | Releases | Conditions |
|---|---|---|
| **G1 Custom structural materials** | Purchase of extrusion, joining hardware, plate and tank fasteners, and stabilization hardware for the frame | (a) Q-01 to Q-08 answered, or recorded as unanswerable with the engineering judgement that replaces each; (b) SR-01 reconciled in writing and the tank wall and height fixed (D-03); (c) tank mounting method established (MR-04, H-01); (d) D-01, D-02, D-04, D-12 decided; (e) footprint, material section, structural load path, mounting method, and stability concept reviewed far enough to produce a purchase-ready cut list and compatible hardware (MR-05 and SR-10 at concept level); (f) the owner's explicit approval to purchase. Full structural acceptance and operating validation are not conditions here; they belong to G2 and G5 |
| **G2 Fabrication** | Cutting, assembly, and opening the tank's membrane-covered holes | G1; the reviewed cut list; MR-05 final structural review recorded (H-11); the hole-preparation method from Q-05 recorded before any hole is opened (H-01); MR-07 mounting and sealing interface designed |
| **G3 Power connection** | Connecting the heater to any power source | ER-01 to ER-05 satisfied by a dated record; SR-08 reviewed (H-08); fuse rating and cord gauge recorded (Q-07); the Battery Box V2 interface approved. **Battery Box V1 remains unapproved and is not a path through this gate** |
| **G4 Transport** | Moving the assembled module in a vehicle | G2; TR-02 fuel-state decision; TR-03 mass recorded; MR-06 restraint and lifting points defined (H-10) |
| **G5 First operation** | Fuel in the tank on the frame; ignition | G2 and G3, and G4 if the module is transported first; SR-02 to SR-05, SR-07, SR-09 satisfied; SR-11 review recorded with accepted protective measures (H-07); SR-06 CO alarm present and working in the shelter; TR-01 weather suitability established (H-09); MR-07 installed interface reviewed (H-05); SR-10 tip assessment recorded (H-02); SR-04 exhaust clearance set (H-04); an approved operating procedure; SR-12 policy recorded, with overnight and unattended operation excluded unless separately approved |

Purchases that are not custom structural materials (a CO alarm, hand tools, consumables) are not gated by G1. The CO alarm is required before G5.

### 10.1 Hazard-to-gate mapping

| Hazard | Blocks |
|---|---|
| H-01 tank bosses and fasteners | G1 (method), G2 (hole preparation) |
| H-02 tip with full tank | G1 (concept), G5 (assessment) |
| H-03 fuel spill reaching hot surfaces | G1 (SR-01 reconciled), G5 |
| H-04 exhaust routing and clearance | G5 |
| H-05 heater orientation, clearances, mounting interface | G2 (design), G5 (installed) |
| H-06 fuel pump placement | G1 (Q-08), G5 |
| H-07 exhaust into heating-air inlet or shelter; CO | G5 |
| H-08 power interruption during cool-down | G3 |
| H-09 weather exposure | G5 |
| H-10 transport and lifting | G4 |
| H-11 frame and joint adequacy | G1 (concept), G2 (final) |

### 10.2 Requirement-to-gate mapping

| Gate | Requirements that must be satisfied |
|---|---|
| G1 | MR-01, MR-02 (reviewed envelope), MR-04, SR-01; MR-05 and SR-10 at concept level |
| G2 | MR-03, MR-05 (final), MR-07 (design) |
| G3 | ER-01, ER-02, ER-03, ER-05, SR-08 |
| G4 | TR-02, TR-03, MR-06 |
| G5 | FR-01 to FR-05, SR-02, SR-03, SR-04, SR-05, SR-06, SR-07, SR-09, SR-10, SR-11, SR-12, TR-01, MR-07 (installed) |

## 11. Constitution compliance check

| Principle | Status |
|---|---|
| I Safety First | Hazards registered, none closed. No fuel, fire, or energized procedure is written. Electrical protection for the supply is deferred to V2 with requirements stated (ER-01, ER-05, SR-08). A working CO alarm is mandatory for operation (SR-06) and does not substitute for the exhaust and inlet review (SR-11) |
| II Modularity | Heater, tank, and frame are separable; electrical connector to be a documented standard type at V2 (ER-03). Non-standard items: the supplied VEVOR harness connectors (documented in bom.md as supplied) |
| III Transparency | Runtime and current are to be measured at V2, not estimated (ER-04). The controller's engineering mode displays supply voltage (M1 p.14), which can support later logging |
| IV Incremental Evolution | This phase is specification only. Purchase and fabrication follow G1–G2; approved power connection follows G3; transport follows G4; first operation follows G5 |
| V Documentation | Sources, decisions, alternatives (design.md §16), and open questions carry IDs and dates |
| VI Practical Utility | Named use case: winter camping heat |
| VII Bounded Complexity | Open frame, manual operation, no automation. Rejected elements are listed with the owner's reasons |

## Change log

| Date | Change |
|---|---|
| 2026-10-27 | Created from the owner's 2026-10-27 brief and the VEVOR manual and product page retrieved the same day. No aluminum frame built or purchased (the heater and its supplied parts were already owned); nothing measured or verified. |
| 2026-10-27 | PR #4 review corrections: three air paths named and SR-11 added; CO alarm made mandatory (SR-06) without substituting for exhaust and inlet review; overnight and unattended operation recorded as unresolved (SR-12); cigarette-lighter prohibition added (C20, ER-05); product-page size, net weight (scope unknown), outlet diameter, and inconsistent working temperature recorded (C21–C24); air-path labels from the manual (C25); "not stated" list revised; gates restructured as G1–G5 with hazard and requirement mappings; status corrected to distinguish owned heater equipment from the unpurchased frame. |
| 2026-10-28 | Owner decision: B1 Adjusted layout (20 × 22 × about 35 in, tank beside the heater with its bottom above the heater top) replaces the 2026-10-27 envelope in MR-02; the earlier envelope and the B1 Compact starting point are retained as alternatives. MR-01 unchanged at 20 members with the 18-member simplification noted as a candidate (D-14). §5 records the owner's 2026-10-28 reports of the plate's four 1/4 in holes, their 1/8 in edge clearance, the plate's estimated 1/32 in thickness, and the tank's three through-holes, all User-reported and none Measured. A-04 height updated. Requirements, hazards, assumptions, acceptance criteria, and gates otherwise unchanged; G1–G5 closed. |
| 2026-10-29 | Owner decision: 2020 (20 × 20 mm, 6 mm slot) T-slot extrusion for every member with metal 90-degree corner brackets, M5 T-slot hardware, flat reinforcement plates at the lower corners, and two foot bars (MR-01 amended; the 20 × 40 mm basis withdrawn; A-04 restated with the stiffness caveat). Tank mounting points: the owner's established description recorded, three membrane-closed through-passages meant to be pierced at installation, reconciling the two earlier reports (§5). Requirements, hazards, acceptance criteria, and gates otherwise unchanged; G1–G5 closed; no hole preparation authorized. |
| 2026-10-29 | Owner decision: supplemental stabilization hardware (foot bars, leveling feet, outriggers and their brackets) excluded from the initial purchase and build and kept as a potential future enhancement; MR-01 and A-04 restated for the bare 20-member frame. SR-10 unchanged: a basic stability verification still precedes fuelled operation at G5, and stabilizer hardware is not a prerequisite for purchasing or assembling the frame. No other requirement, decision, or gate changed. |
