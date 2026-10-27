# Diesel Heater Module (002) — Preliminary Mechanical Design

**Status**: Preliminary concept for review. **Not approved for fabrication. No cut lengths are approved. The heater and its supplied parts are owned, and some are partially assembled; no frame material has been purchased and nothing has been fabricated.**
**Date**: 2026-10-27
**Companions**: [spec.md](spec.md) (requirements, manufacturer constraints C1–C25, release gates G1–G5), [bom.md](bom.md)
**Evidence tags**: as defined in [spec.md §1](spec.md#1-how-to-read-this-document). Manufacturer sources M1 (manual) and M2 (product page) are identified in [spec.md §2](spec.md#2-manufacturer-sources).

---

## 1. Concept summary

An open, portable, three-level rectangular frame of aluminum T-slot extrusion. The heater sits on its supplied metal plate at the middle level. The supplied 10 L tank hangs upright, broad face inward, on two lengthwise rails along one inside wall, fixed through its three factory mounting points. The lower level is open for the intake, exhaust, fuel line, and electrical connections. The frame stands on its own; stabilization, possibly deployable outriggers, is to be evaluated.

Everything in this section is an **Owner decision (2026-10-27)** except where marked. The owner and ChatGPT developed the concept; this document organizes it and records what remains open.

## 2. Envelope and conventions

| Item | Value | Evidence |
|---|---|---|
| Width (W) | about 20 in | Owner decision, preliminary |
| Depth (D) | about 24 in | Owner decision, preliminary |
| Height (H) | about 38 in | Owner decision, preliminary |
| Extrusion | Aluminum T-slot, 20 × 40 mm where suitable | Owner decision |

Conventions used below: *widthwise* members run across W; *lengthwise* members run along D; the *tank wall* is the one inside wall carrying the tank rails. Levels are numbered from the ground: L1 bottom, L2 middle, L3 top. The envelope is an outside dimension of the frame; **cut lengths depend on the joint method (D-01) and are not derived here**.

## 3. Member schedule (preliminary count: 20)

| # | Members | Orientation | Role | Qty |
|---|---|---|---|---|
| U | Uprights | Vertical, continuous full height | Corners | 4 |
| P-W | Perimeter widthwise | Horizontal across W | One pair per level, L1–L3 | 6 |
| P-D | Perimeter lengthwise | Horizontal along D | One pair per level, L1–L3 | 6 |
| H-X | Heater crossmembers | Horizontal across W, at L2 | Carry the supplied mounting plate | 2 |
| T-R | Tank rails | Horizontal along D, on the tank wall | Carry the tank through its three points | 2 |
| | | | **Total** | **20** |

Notes:

- Which way the 20 × 40 section is oriented in each member (40 mm vertical for bending stiffness, or 40 mm horizontal for a wider mounting face) is open (D-02).
- The heater crossmembers' spacing must suit the plate's 5 7/16 × 6 11/16 in footprint (User-reported) and the plate's fixing pattern, which is not yet recorded (Q-03).
- The tank rails' vertical spacing must suit the boss geometry: lower pair about 6 13/16 in apart horizontally, upper point about 7 7/8 in above the lower row (User-reported). Whether two rails can meet all three points, or whether the upper point needs a short vertical or a bracket, is open (D-04).
- The two tank rails are in addition to the perimeter lengthwise members on that wall. Whether a perimeter member at L2 or L3 can serve as one of the rails, reducing the count, is open (D-04).

## 4. Level layout

| Level | Contents | Evidence |
|---|---|---|
| L1 (bottom, open) | Intake pipe and air filter element; exhaust pipe and silencer exiting the frame; pulse fuel pump and oil filter (position open, D-05); electrical connections | Owner decision (open level); M1 p.9 for the parts |
| L2 (middle) | Heater on its supplied plate on H-X; the plate's seal and fixings per M1 p.9; hot-air outlet facing the duct side | Owner decision; M1 p.9 |
| L3 (top) | Not assigned. Candidates: controller mount, duct stowage, nothing | Open (D-06) |
| Tank wall | Tank on T-R, upright, filler at top. Height of the tank relative to L2 is **open and governed by SR-01** | Owner decision (position); height Unknown |

The tank is 16 × 16 × 3 in (User-reported) on a 24 in deep wall, leaving about 8 in of wall length free. Where the tank sits along the wall relative to the heater and exhaust affects SR-02 and SR-04.

## 5. Heater mounting

- Heater product size 13.4 × 4.5 × 5.5 in / 340 × 115 × 140 mm (Manufacturer-stated, C21; the 13.4 in length also User-reported by tape measure). Net weight 11 lb / 5 kg of unstated scope (C22, Q-11); the standalone heater mass remains Unknown.
- The supplied metal plate (5 7/16 × 6 11/16 in, User-reported) mounts on H-X. M1 p.9 shows a seal between the heater and the plate and "double head screw nut" fixings; M1 p.8 lists four machine fixing screws and one machine fixing piece. The fixing pattern and hole sizes are not recorded (Q-03).
- The intake, exhaust, and fuel connections leave the heater through the plate downward (M1 p.9 diagram), into L1. The plate needs clear space below it.
- M1 p.4 item 11 says to seal all gaps between the mounting plate and the car body. In a vehicle that separates the cabin from the combustion side. In an open frame there is no cabin; whether any sealing or splash shielding is needed is for engineering review (MR-07).
- **Orientation**: M1 draws the heater upright on its plate and gives no tilt limits. Any orientation other than upright, and the tilt a portable frame tolerates, are Unknown (A-02, Q-06).
- **Clearances around the heater body and hot-air outlet**: not stated by the manufacturer. Unknown (Q-06).

## 6. Fuel tank mounting

| Topic | What is known | What is not |
|---|---|---|
| Mounting points | Three recessed points; two lower, one upper (User-reported geometry). Some holes have thin plastic membranes | Whether the membranes are meant to be pierced, drilled, or left; the boss thread or through-hole size; the manufacturer's intended fastener |
| Manufacturer method | "Use this screw to tighten the fuel tank fixed to the metal plate of the vehicle" (M1 p.9); "oil tank accessories" ×1 in the packing list (M1 p.8) | What the accessory kit contains (Q-02); the load the bosses are rated for (Q-04) |
| Load | Full tank: about 8.2–8.5 kg of fuel (A-05, Proposed) plus the tank's own mass (Unknown) | Dynamic loads in transport; fatigue of plastic bosses under vibration |
| Position | Upright, cap at top, broad face against the rails (Owner decision) | Height relative to the heater (SR-01); separation from the exhaust (SR-04) |

**Nothing about the bosses, the fasteners, or the rails is assumed adequate** (MR-04, MR-05). A tank shelf is not to be added unless this assessment shows the bosses cannot carry the tank (§16).

## 7. Fuel pump and fuel line

- M1 p.9 shows the fuel path tank → oil pipe → oil filter → pulse fuel pump in its sheath → oil pipe → heater, with 12 oil pipe clips and 12 ribbons (cable ties) supplied (M1 p.8).
- M1 states no pump mounting angle, orientation, height relative to tank or heater, or maximum line length. All are Unknown (Q-08). Diesel pulse pumps commonly have manufacturer-specified inclination ranges; **this manual does not give one, so none is assumed here**.
- The only positional instruction is C12: tank above the heater, to facilitate pump operation. This pulls the tank upward in the frame while C1 pulls it away from the heater. See SR-01.
- The pump position (L1 is the natural candidate) is open (D-05).

## 8. Air paths: combustion intake, heating-air inlet, hot-air outlet, and exhaust

The heater has three separate air paths ([spec.md §7.2](spec.md#72-safety), C25). They must be kept distinct in every layout decision:

| Path | Parts | Where on the frame | Governing requirements |
|---|---|---|---|
| Combustion-air intake | Intake pipe with air filter element, from the heater's underside (M1 p.9 "air intake") | L1 | SR-07, C14 |
| Heating-air inlet | Fan inlet on the heater body (M1 p.5 "Air inlet", "Air fan"); draws the air that is heated and ducted into the shelter | L2, at the heater | SR-05, SR-07, SR-11 |
| Hot-air outlet and duct | "Air outlet" (M1 p.5), inner diameter 3 in / 76.5 mm (C23); blowpipe and rotary tuyere | L2 to the shelter | FR-03, SR-05 |
| Combustion exhaust | Escape pipe and silencer, "(To the outside)" (M1 p.9) | Leaves L1; terminates outside the envelope | SR-03, SR-04, SR-11 |

The heating-air inlet sits at L2 beside the heater. Whatever air surrounds the heater at L2 is what the duct delivers into the shelter. The exhaust termination must therefore be placed and directed, with wind considered, so that exhaust cannot reach the heating-air inlet or the shelter's openings. SR-11 requires an engineering review to demonstrate this and to record the accepted protective measures. **No separation distance is proposed here** because the manufacturer gives none (D-07, D-13).

- Exhaust: heater → escape pipe → silencer, "(To the outside)" (M1 p.9). It must run horizontally or downward, never upward (C16), be kept clear of anything flammable and of cargo on the ground (C15), and terminate outside (C6).
- In this frame the exhaust leaves the heater downward into L1 and must exit the envelope. The exit side, the pipe length, where the silencer sits, and how the pipe is restrained are open (D-07).
- Clearance from the exhaust and silencer to the tank, fuel line, wiring, extrusion, and ground cover is **not given by the manufacturer** and must be set by engineering review (SR-04). The surface temperature of the exhaust and silencer is not stated.
- Intake: intake pipe with air filter element in L1; must stay open and clear (C14). The intake and exhaust terminations must be separated so exhaust is not drawn in; the manufacturer gives no distance (Q-06).
- Hot-air outlet: inner diameter 3 in / 76.5 mm (C23); blowpipe and rotary tuyere (M1 p.7). The maximum duct run is not stated (Q-02 covers measuring the supplied parts).

## 9. Hot-air ducting to the shelter

The duct is the only part of the system that enters the shelter (SR-05). It carries whatever the heating-air inlet draws at L2 (§8), so the shelter end of the duct and the exhaust termination are to be considered together under SR-11. Its route from L2 to the shelter wall, its support, and how it is prevented from pulling the frame over (SR-10) are open (D-08). No duct extension is specified.

## 10. Stability and tip resistance

- Footprint 20 × 24 in; height 38 in; the tank, when full, adds about 8–9 kg (A-05) high on one wall, and the heater's mass is unknown (A-06). The center of gravity will be high and off-center toward the tank wall.
- SR-10 requires a tip assessment with the tank full on the worst-case ground, under handling push, duct pull, and wind. The criteria are to be set at engineering review.
- Options to evaluate (none selected): deployable outriggers on the tank side, a wider L1 footprint, ballast at L1, lowering the tank (in tension with C12), or adjustable feet. **Paracord staking is not a substitute for a self-supporting frame** (Owner decision 2026-10-27); it may be considered only as a supplement in wind.

## 11. Electrical

- Supply: 12 V, at least 15 A capability at start (C9); input window 9–18 V (C17); rating 12 V/40 W (C11) and 3 A running (C18); 13 A starting reported in the product Q&A (C19, less authoritative).
- The supplied power cord carries a fuse in a holder (M1 p.9). Its rating and the cord gauge are to be read from the parts (Q-07) before any supply cable is sized.
- Power must not be cut during operation or the 3–5 minute cool-down (C4, C8). This rules out, until reviewed, any upstream device that could open the circuit during cool-down: a low-voltage disconnect, a battery protection trip, a switched branch, or a connector that can be unplugged under load (SR-08).
- The heater is **not** to be connected to Battery Box V1. The V1 fuse block has no assigned branch ([as-built.md §4.4](../001-battery-box/as-built.md#44-branch-assignments)) and the box carries open safety concerns. The interface is a Battery Box V2 requirement (ER-03). The controller's engineering mode shows supply voltage (M1 p.14), which will help characterize cable drop when that work is done.
- The heater must not be started from a cigarette-lighter socket or plug (C20, ER-05). No supply cable, fuse, or connector has been selected; that selection belongs to the Battery Box V2 interface and gate G3.
- Where the controller and its cable are mounted on the frame, and how the harness is protected from the exhaust, are open (D-09).

## 12. Weather protection

The manufacturer describes vehicle-interior or under-vehicle installation only (C10) and warns of splashing under a vehicle. The exposure limits of the controller, the harness connectors, the pump, and the intake filter in rain, snow, and sub-freezing conditions are Unknown (TR-01). A plastic operating enclosure and a full backplate are excluded by owner decision; any weather measure must be something else (a partial cover, orientation, or placement) and must not block the intake (SR-07) or trap exhaust. Open (D-10).

## 13. Transport, restraint, and lifting

- Whether the tank travels full, part-full, or empty is undecided (TR-02). A full tank on the bosses in a moving vehicle is a different load case from static use (MR-05).
- Tie-down points and lifting handles are undefined (MR-06). The frame's total mass is unknown (TR-03).
- Open (D-11).

## 14. Hazard register

Each hazard the owner listed as unresolved on 2026-10-27 appears here. **None is closed.** "Closes when" describes the record needed, not a procedure.

| ID | Hazard | Related requirements | Status | Closes when |
|---|---|---|---|---|
| H-01 | Tank mounting bosses or fasteners fail; tank drops or leaks | MR-04, MR-05 | Open | Boss load capacity and fastener method established with the manufacturer's kit contents known (Q-02, Q-04, Q-05) and a written review |
| H-02 | Frame tips with a full tank; fuel spill, hot exhaust contact | SR-10, A-05, A-06 | Open | Masses recorded; tip assessment recorded; stabilization chosen |
| H-03 | Fuel spill or leak reaches the heater, exhaust, or silencer; fire | SR-01, SR-02 | Open | Written reconciliation of C1 and C12 with the layout; spill path review |
| H-04 | Exhaust routed upward, blocked, or too close to flammables or the tank | SR-03, SR-04 | Open | Routing and clearance fixed at engineering review |
| H-05 | Heater mounted in an orientation or with clearances the manufacturer does not support | A-02, MR-07 | Open | Manufacturer confirmation or documented engineering judgement (Q-06) |
| H-06 | Fuel pump mounted outside its working orientation or line too long; flame-out or fuel starvation | §7 | Open | Pump requirements established (Q-08) |
| H-07 | Combustion exhaust is drawn into the heating-air inlet and delivered through the duct, or enters the occupied shelter through its openings; carbon-monoxide exposure | SR-05, SR-06, SR-07, SR-11, SR-12 | Open | The SR-11 engineering review is documented, reviewed, and its protective measures accepted and recorded for the intended installation and foreseeable wind, and the CO alarm (SR-06) is in place and working. Recording a placement rule alone does not close it; the alarm alone does not close it |
| H-08 | Power interrupted during cool-down; overheat | SR-08, ER-01 | Open | Supply design reviewed at V2 |
| H-09 | Weather damages controller, harness, or pump; or a weather cover blocks the intake | TR-01, SR-07, D-10 | Open | Exposure limits established and the measure reviewed |
| H-10 | Module shifts or falls in transport; lifting injury | TR-02, TR-03, MR-06 | Open | Restraint and lifting points defined; transport fuel state decided |
| H-11 | Extrusion frame or joints inadequate for the loads | A-04, MR-05 | Open | Structural review recorded |

Which release gate each hazard blocks is mapped in [spec.md §10.1](spec.md#101-hazard-to-gate-mapping). An open hazard that applies to the intended configuration blocks that gate.

## 15. Open decisions and questions

### 15.1 Decisions (design choices still to be made)

| ID | Decision | Depends on |
|---|---|---|
| D-01 | Joint method for the extrusion (corner brackets, end-tapped bolts, gussets) and therefore the cut-length derivation | MR-05 |
| D-02 | Section orientation of each member | D-01, MR-05 |
| D-03 | Which wall is the tank wall and which side the duct leaves | SR-01, SR-04, D-07, D-08 |
| D-04 | Tank rail arrangement: two rails only, or an added short member or bracket for the upper point; whether a perimeter member doubles as a rail | Q-04, Q-05 |
| D-05 | Pump and oil filter position | Q-08 |
| D-06 | Use of L3 | None; may stay empty |
| D-07 | Exhaust exit side, pipe route, silencer location, pipe restraint | SR-03, SR-04 |
| D-08 | Duct route and strain relief | SR-10 |
| D-09 | Controller and harness mounting | SR-08, TR-01 |
| D-10 | Weather measure, if any | TR-01 |
| D-11 | Transport restraint, lifting, fuel state in transit | TR-02, MR-06 |
| D-12 | Stabilization method (outriggers, footprint, ballast, feet) | SR-10 |
| D-13 | Exhaust termination position and direction relative to the heating-air inlet, the shelter's openings, and prevailing wind | SR-11, D-07, D-08 |

### 15.2 Questions (information needed; who can answer)

| ID | Question | Who |
|---|---|---|
| Q-01 | Does the manual in the owner's box match M1? Record its revision marks, if any, and any differences on the installation diagram and safety pages | Owner |
| Q-02 | Inventory the supplied parts against M1 p.7–8. Record the contents of "oil tank accessories" and "machine fixing piece", pipe diameters, blowpipe length, and the masses of the heater and the empty tank | Owner |
| Q-03 | The mounting plate's fixing hole pattern and sizes, and how the heater's seal and double-head screw nuts engage it | Owner |
| Q-04 | What are the tank bosses rated to carry, and is vertical hanging on three points the intended installation? | VEVOR support; otherwise engineering review |
| Q-05 | How are the membrane-covered holes meant to be prepared, and with what fastener? | VEVOR support; owner inspection of the accessory kit |
| Q-06 | Permitted mounting orientation and tilt of the heater; clearance distances around the heater body, exhaust, silencer, and hot-air outlet; required separation of intake and exhaust terminations | VEVOR support; otherwise engineering review |
| Q-07 | Rating of the supplied in-line fuse and the gauge of the supplied power cord | Owner |
| Q-08 | Fuel pump mounting angle, orientation, maximum height difference, and maximum fuel line length | VEVOR support; otherwise engineering review |
| Q-09 | Which CO alarm will be used in the shelter (SR-06 makes one mandatory), and what placement of the module relative to the shelter is acceptable to the owner as the starting point for the SR-11 review? | Owner |
| Q-10 | Will overnight or unattended operation be permitted at all, and under what conditions? Unresolved; neither is approved (SR-12) | Owner, with engineering review |
| Q-11 | What does the M2 net weight of 11 lb / 5 kg cover, and what is the correct working-temperature range, given the inconsistent figures on M2 (C22, C24)? | VEVOR support |

## 16. Alternatives considered and rejected

Recorded per constitution Principle V. Each rejection stands unless a structural or safety finding under §14 shows a specific need, in which case the finding is to be written up before the element is reconsidered.

| Alternative | Reason rejected | Date |
|---|---|---|
| Fuel-tank shelf under the tank | Unnecessary if the factory bosses carry the tank (to be established, H-01); adds a surface that could collect spilled fuel | Owner decision 2026-10-27 |
| Full backplate on the tank wall | Not needed for the concept; adds mass and a flat surface; a partial plate would only be justified by H-01 or H-09 findings | Owner decision 2026-10-27 |
| Wooden mock-up before the aluminum frame | Owner prefers to go to the aluminum frame once the design is approved; mock-up adds a step without resolving the open questions, which are about loads and manufacturer limits rather than fit | Owner decision 2026-10-27 |
| Plastic operating enclosure, including the Greenmade 12-gallon tote | Open frame chosen for ventilation, access, and heat; an enclosure would conflict with C2 and C14 unless designed with ventilation, which is not wanted | Owner decision 2026-10-27 |
| Paracord staking as the primary stability method | Not a self-supporting solution; frame must stand on its own (SR-10) | Owner decision 2026-10-27 |

## Change log

| Date | Change |
|---|---|
| 2026-10-27 | Created from the owner's 2026-10-27 brief and the VEVOR manual and product page retrieved the same day. Concept recorded as decided; all hazards open; no cut lengths; nothing built or purchased. |
| 2026-10-27 | PR #4 review corrections: §8 rewritten around the three air paths with the manual's labels; H-07 closure now requires the SR-11 review and accepted measures plus the CO alarm; D-13, Q-10, Q-11 added; manufacturer size, net weight (scope unknown), and outlet diameter recorded; cigarette-lighter prohibition noted; status corrected (heater owned and partly assembled, no frame purchased). Mechanical concept unchanged. |
