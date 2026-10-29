# Diesel Heater Module (002) — Preliminary Mechanical Design

**Status**: Preliminary concept for review. **Not approved for fabrication. No cut lengths are approved. The heater and its supplied parts are owned, and some are partially assembled; no frame material has been purchased and nothing has been fabricated.**
**Date**: 2026-10-27; B1 Adjusted layout recorded 2026-10-28; G1 structural concept and readiness ledger recorded 2026-10-29
**Companions**: [spec.md](spec.md) (requirements, manufacturer constraints C1–C25, release gates G1–G5), [bom.md](bom.md), [cad/](cad/README.md) (placeholder model of the three layouts, `out/comparison.md`), [measurements/](measurements/README.md)
**Evidence tags**: as defined in [spec.md §1](spec.md#1-how-to-read-this-document). Manufacturer sources M1 (manual) and M2 (product page) are identified in [spec.md §2](spec.md#2-manufacturer-sources).

---

## 1. Concept summary

An open, portable, three-level rectangular frame of aluminum T-slot extrusion. The heater sits on its supplied metal plate at the middle level. The supplied 10 L tank hangs upright, broad face inward, on two lengthwise rails along one inside wall, fixed through its three factory mounting points. The lower level is open for the intake, exhaust, fuel line, and electrical connections. The frame stands on its own; stabilization, possibly deployable outriggers, is to be evaluated.

Everything in this section is an **Owner decision (2026-10-27)** except where marked. The owner and ChatGPT developed the concept; this document organizes it and records what remains open.

**Preferred preliminary layout, B1 Adjusted (Owner decision 2026-10-28).** Footprint about 20 × 22 in; height about 35 in (preliminary range 34 to 36 in). The heater stands upright on its plate with the plate underside about 7 in above the base, carried by two crossmembers that slide along the middle-level depth members. The tank stands upright beside the heater on the opposite wall, hung on two rails that slide on the uprights, with its bottom above the heater body's top by a provisional gap (D-15). This is a conservative geometric reading of the manufacturer's tank-above instruction (C12) combined with horizontal separation from the heater (C1). **It is not evidence that fuel delivery, spill protection, hot-surface separation, or the tank mounting are adequate**; SR-01 remains to be reconciled in writing (§6), every hazard in §14 stays open, and gates G1 to G5 stay closed. Two earlier layouts, A Original (tank entirely above the heater in a 38 in frame) and B1 Compact (28 in, tank overlapping the heater in height), are retained as alternatives in §16 and in the CAD model. Nothing here is a cut length.

## 2. Envelope and conventions

| Item | Value | Evidence |
|---|---|---|
| Width (W) | about 20 in | Owner decision 2026-10-28, preliminary (unchanged from 2026-10-27) |
| Depth (D) | about 22 in | Owner decision 2026-10-28, preliminary (was about 24 in, 2026-10-27; retained in A Original) |
| Height (H) | about 35 in, range 34 to 36 in | Owner decision 2026-10-28, preliminary (was about 38 in, 2026-10-27; retained in A Original) |
| Extrusion | Aluminum T-slot, 20 × 40 mm where suitable, subject to review (MR-05) | Owner decision |

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

- **Joint system, preferred preliminary approach for D-01 (Owner direction 2026-10-29; not a structural decision).** Interior corner brackets with sliding T-nuts at every member end, two brackets per end on the four loaded members (the two heater crossmembers and the two tank rails), and flat gusset plates across the eight corners of the base rectangle. Reasons: no drilling or tapping of extrusion ends, cut-length error is absorbed in the joint, the crossmembers and rails can slide to the real plate pitch and boss rise, and all parts come from one supplier family. End-tapped blind fasteners remain the alternative if the supplier's bracket data proves weak; they need accurate cuts and access holes. **Load paths under this approach:** heater through Interface A and B (§5) into the crossmembers, through their brackets into the middle-level depth members, into the uprights and the feet; tank through its three mounting points into the rail T-nuts, through the rail brackets into the uprights; lateral loads through the gusseted base rectangle and the top rectangle. **Suspected governing concerns, to be investigated at the MR-05 review:** the rotational stiffness of bracket joints under a handling push (racking), the slip resistance of the T-nuts carrying the crossmembers and rails, and the plastic tank mounting points (§6). With the illustrative masses in §10 the bending moments in the crossmembers and rails are expected to be small, but member bending strength and deflection are **not excluded**: no support model, load case, supplier section properties, or calculation exists yet, and the review must cover them for every loaded member. MR-05 and A-04 stay open, and the supplier evidence listed in [bom.md §2.1](bom.md#21-supplier-compatibility-criteria-evidence-to-obtain-before-g1) is required before any adequacy statement.
- **Section orientation, preferred starting choices for D-02 (2026-10-29; not confirmed adequacy).** Uprights with the 40 mm face along the depth, so the faces toward the tank and toward the heater each carry two slots for rail and crossmember brackets at any height; heater crossmembers with the 40 mm face horizontal for a wide seat and two slots under the plate; tank rails with the 40 mm face vertical, facing the tank. Racking stiffness comes mainly from the joints rather than from upright bending, so these choices are driven by mounting convenience and are reversible at the supplier-specific review. The CAD model still draws every member 40 mm vertical.
- **18-member candidate (D-14, deprioritized 2026-10-29).** Omitting the two middle-level widthwise members (`L2-W1`, `L2-W2`) is recorded as an alternative only. It is not to be investigated further unless a structural finding makes the 20-member frame unsuitable. MR-01 stands at 20 members and the CAD model draws 20.
- The heater crossmembers' spacing must suit the plate's fixing pattern. The owner reports (2026-10-28, not measured) four holes about 1/4 in diameter with about 1/8 in from each hole's outside edge to its two adjacent plate edges, so the hole centres are about 1/4 in in from each edge and the centre-to-centre pitch is about 4 15/16 in along the 5 7/16 in side and about 6 3/16 in along the 6 11/16 in side. Which side runs along the heater is not recorded (PLT-14), so which pitch sets the crossmember spacing is open; the CAD model uses the shorter pitch (125.4 mm). Q-03 stays open until measured.
- The tank rails' vertical spacing must suit the boss geometry: lower pair about 6 13/16 in apart horizontally, upper point about 7 7/8 in above the lower row (User-reported). Whether two rails can meet all three points, or whether the upper point needs a short vertical or a bracket, is open (D-04).
- The two tank rails are in addition to the perimeter lengthwise members on that wall. Whether a perimeter member at L2 or L3 can serve as one of the rails, reducing the count, is open (D-04).

## 4. Level layout

| Level | Contents | Evidence |
|---|---|---|
| L1 (bottom, open) | Intake pipe and air filter element; exhaust pipe and silencer exiting the frame; pulse fuel pump and oil filter (position open, D-05); electrical connections | Owner decision (open level); M1 p.9 for the parts |
| L2 (middle) | Heater on its supplied plate on H-X, plate underside about 7 in above the base in the B1 layouts; the plate's seal and fixings per M1 p.9; hot-air outlet facing the duct side | Owner decision 2026-10-28 (about 7 in, preliminary); M1 p.9 |
| L3 (top) | Not assigned. Candidates: controller mount, duct stowage, nothing. The top rectangle is kept for stiffness and as the natural lifting location (§13) | Open (D-06) |
| Tank wall | Tank on T-R, upright, filler at top, beside the heater on the X-min wall. In B1 Adjusted the tank bottom is above the heater body's top by a provisional gap (D-15). **SR-01 remains to be reconciled in writing** (§6) | Owner decision 2026-10-28 (position); gap Proposed |

The tank is 16 × 16 × 3 in (User-reported). Its 16 in width lies along the tank wall, the X-min wall, which runs along the frame's nominal 22 in depth (the Y axis). Nominally 6 in of wall length remain; between the inside faces of the two uprights, where the rails run, the usable length is 478.8 mm, leaving about 72 mm (2.9 in). Where the tank sits along the wall relative to the heater and exhaust affects SR-02 and SR-04.

**B1 Adjusted height stack-up (Proposed; geometry only, from `cad/out/comparison.md`).** Plate underside 177.8 mm (7 in); plate top 178.6 mm with the owner's 1/32 in thickness estimate; heater top 318.3 mm (C21 height); tank bottom 368.3 mm with the 50 mm provisional gap; tank top 774.7 mm with the User-reported 16 in height; top-member band 849.0 to 889.0 mm (35 in). The crossmembers under the plate occupy 137.8 to 177.8 mm, leaving about 98 mm between them and the base members and about 138 mm under the plate between the crossmembers for the heater's downward connections, whose protrusions are Unknown.

The largest gap each frame height allows follows from the same stack-up: tank top = 177.8 + 0.8 + 139.7 + gap + 406.4 = 724.7 mm + gap. With the 50 mm filler and cap allowance kept below the 40 mm top-member band, gap = H − 40 − 50 − 724.7 = H − 814.7 mm; with the allowance permitted to rise to the frame top (into the band, clear of the members in plan), gap = H − 50 − 724.7 = H − 774.7 mm. Values rounded to 0.1 mm.

| Frame height H | Largest gap, allowance below the top-member band | Largest gap, allowance up to the frame top |
|---|---|---|
| 34 in (863.6 mm) | 48.9 mm | 88.9 mm |
| 35 in (889.0 mm) | 74.3 mm | 114.3 mm |
| 36 in (914.4 mm) | 99.7 mm | 139.7 mm |

The CAD uses 35 in with a 50 mm placeholder gap, which leaves 24.3 mm between the allowance and the top-member band; that is the 74.3 mm maximum less the 50 mm placeholder. The filler neck and cap height is Unknown (TNK-07, TNK-08); the 50 mm allowance is a placeholder. At 35 in with the 50 mm gap, the modelled headroom from the tank top plus that placeholder to the underside of the top members is 24 mm. **Filler cap access:** the filler sits inside the top rectangle in plan, about 38 mm in from the inside face of the tank-wall top member, so it is reachable from above through the open top; whether a fuel can or spout can be used there at about 800 mm height beside a 40 mm member, with the heater off and cold (C3, SR-09), is for review (D-15). None of these figures is a clearance; the gap value is a placeholder for the SR-01 review, not a safe distance.

## 5. Heater mounting

- Heater product size 13.4 × 4.5 × 5.5 in / 340 × 115 × 140 mm (Manufacturer-stated, C21; the 13.4 in length also User-reported by tape measure). Net weight 11 lb / 5 kg of unstated scope (C22, Q-11); the standalone heater mass remains Unknown.
- The supplied metal plate (5 7/16 × 6 11/16 in, User-reported) mounts on H-X. M1 p.9 shows a seal between the heater and the plate and "double head screw nut" fixings; M1 p.8 lists four machine fixing screws and one machine fixing piece. The owner reports (2026-10-28, not measured) four holes about 1/4 in diameter about 1/8 in from each adjacent edge, and a thickness of about 1/32 in, below 1/16 in. Q-03 stays open until these are Measured (PLT-03 to PLT-09).
- **Two mechanical interfaces, one unresolved load path (D-16).** *Interface A, heater to its supplied plate*: the factory fixing arrangement, M1's seal and "double head screw nut" fixings with four machine fixing screws (M1 p.8, p.9). Its geometry, where it bears on the plate, and how it transfers the heater's load into the plate are incompletely established (Q-03; HTR-11, HTR-16, PLT-12). *Interface B, plate to frame*: provisionally, the plate's four corner holes (User-reported 2026-10-28) bolted into T-nuts in the two crossmembers with T-slot hardware. The CAD places the crossmembers under those corner holes. It does not establish that the heater's own fixings coincide with the corner holes, and the two interfaces are **not assumed to share fasteners**. The plate's thickness of about 1/32 in is an owner estimate, not an engineering adequacy determination. Whether the plate, Interface A, Interface B, and the crossmembers together carry the heater under static, handling, and transport loads is **unresolved** until the interfaces, the connection details, and the loads have been assessed (MR-03, MR-05).
- **Adjustable plate mounting (proposed, Interface B).** The crossmembers slide along the middle-level depth members to the plate's hole pitch. With the hole centres about 6.4 mm in from the plate edge and a 20 mm slot face centred under them, each crossmember extends about 3.7 mm beyond the plate edge on that side; this is a geometric consequence of the derived pitch, recorded and not assessed. Sliding solves alignment only; it says nothing about fastener strength or the load path (MR-05, D-16).
- The intake, exhaust, and fuel connections leave the heater through the plate downward (M1 p.9 diagram), into L1. The plate needs clear space below it. Whether the three underside stubs and the plate's underside opening fall between the two crossmembers at the derived pitch, or foul one, is Unknown and is the one fit question that decides the crossmember arrangement (HTR-12 to HTR-14 and PLT-10, PLT-11). It is not assumed.
- **Fit check before purchase (dry fit; nothing fastened, nothing powered, no fuel).** The minimum observation that settles Interface A and B and the crossmember pitch: (1) with the heater seated on its plate, whether the four corner holes are clear of the heater base so Interface B bolts could be fitted with the heater in place, and where the heater's own fixings (Interface A) sit relative to the corners; (2) with two 20 mm wide strips laid under the plate at the derived pitch of about 125 mm, then at about 157 mm, whether the three stubs and the plate's opening fall between the strips or foul one; (3) the stub protrusions below the plate and the exhaust pipe's outside diameter and construction; (4) whether the plate stays flat on the strips with the heater on it, as an observation, not a result. Readings go into a dated measurement record under their identifiers (§15.3). Neither the plate nor the heater base is presumed to span anything until the D-16 assessment is written.
- M1 p.4 item 11 says to seal all gaps between the mounting plate and the car body. In a vehicle that separates the cabin from the combustion side. In an open frame there is no cabin; whether any sealing or splash shielding is needed is for engineering review (MR-07).
- **Orientation**: M1 draws the heater upright on its plate and gives no tilt limits. Any orientation other than upright, and the tilt a portable frame tolerates, are Unknown (A-02, Q-06).
- **Clearances around the heater body and hot-air outlet**: not stated by the manufacturer. Unknown (Q-06). **Q-06 at gate G1:** with VEVOR not contacted, G1(a) requires a dated engineering judgement replacing Q-06 before purchase; it cannot be deferred past G1. What that judgement must contain: the orientation adopted (upright on the plate, the only orientation M1 documents) with the tilt the module will be limited to by a placement rule; provisional clearance distances from the heater body, hot-air outlet, exhaust, and silencer to the tank, fuel line, wiring, and extrusion, chosen conservatively with the basis stated, since the manufacturer gives none; and the statement that these provisional values are to be confirmed against the measured surface temperatures at commissioning (G5, SR-04) and may require shielding. No such judgement exists yet.

## 6. Fuel tank mounting

| Topic | What is known | What is not |
|---|---|---|
| Mounting points | Three recessed points; two lower, one upper (User-reported geometry). Reported 2026-10-27 as having thin plastic membranes on some holes and 2026-10-28 as three through-holes; both reports stand until each hole is recorded as found (TNK-10 to TNK-12) | Whether any membrane is meant to be pierced, drilled, or left; the hole or boss size; the manufacturer's intended fastener |
| Manufacturer method | "Use this screw to tighten the fuel tank fixed to the metal plate of the vehicle" (M1 p.9); "oil tank accessories" ×1 in the packing list (M1 p.8) | What the accessory kit contains (Q-02); the load the bosses are rated for (Q-04) |
| Load | Full tank: about 8.2–8.5 kg of fuel (A-05, Proposed) plus the tank's own mass (Unknown) | Dynamic loads in transport; fatigue of plastic bosses under vibration |
| Position | Upright, cap at top, broad face against the rails, beside the heater on the X-min wall, bottom above the heater top (Owner decision 2026-10-28) | The gap value (D-15, SR-01); separation from the exhaust (SR-04) |
| Rails | Two rails on brackets that slide in the upright slots, so the tank height follows the chosen gap and the upper rail follows the real boss rise (proposed, D-04) | Bracket type and count; whether a perimeter member can double as a rail (D-04) |

**Nothing about the bosses, the fasteners, or the rails is assumed adequate** (MR-04, MR-05). Geometric fit on the rails establishes nothing about the strength of the plastic mounting points. VEVOR is not being contacted at this stage (owner decision 2026-10-28), so Q-04 and Q-05 close only by a documented engineering assessment. What that assessment needs: each boss's recess and hole geometry and the local wall thickness (TNK-10 to TNK-14), the accessory kit contents (TNK-16), which is the strongest available evidence of the manufacturer's intended fastening, the empty tank mass (MAS-03) with the A-05 fuel mass, and a load case that includes handling and transport. The load case is set at the review; as an outline only, it would cover the static full-tank load, a handling factor, and a road-transport factor with the tank in the state TR-02 decides, and would check each point for shear, bearing on the plastic, and pull-out from the prying moment that the tank's thickness produces at the upper point. Two rules apply to any fastener considered: the plastic is loaded in bearing through a large washer or the supplied grommet, never point-loaded by a bolt head; and no hole is opened, enlarged, or otherwise modified without the Q-05 method on record. A proof-load approach, if chosen, is to be designed and approved at that review, not here, and **a simple proof-load test alone is not sufficient evidence of adequacy**: it does not cover vibration, fatigue of plastic, temperature, or transport shock. A tank shelf is not to be added unless this assessment shows the bosses cannot carry the tank (§16).

**Spill path along the crossmembers (D-17, unresolved alternative; SR-02 open).** The two full-width heater crossmembers pass beneath the tank zone, so a drip from the tank bottom could land on them and run toward the plate. Rotating the crossmembers to run along the depth, under the heater footprint only, would remove that route, but the owner has declined it for this phase (2026-10-29) because the supports would then bear on the plate's other pitch and could create an unfavourable load path through the thin supplied plate, whose load-bearing arrangement is unverified (D-16). D-17 therefore stays open. Candidate measures for the SR-02 review that do not depend on the plate carrying load, none selected: a drip edge or small channel on the crossmember top faces under the tank zone, directing any run-off back toward the tank side and off the frame; shortening the crossmembers to span only the heater side by adding a short intermediate depth member, which changes the member count (MR-01) and needs its own joint review; a removable drip deflector under the tank bottom, noting the §16 rejection of a shelf that could collect fuel; and the refuelling rule that the heater is off and cold (C3, SR-09) with the filler spill path checked at review. The rails, uprights, and base members remain further candidate routes for the same review.

**SR-01 reconciliation (Proposed, for engineering review; not closed).** C12 says the tank "should be properly placed above the main engine to facilitate the operation of the fuel pump"; C1 says to keep the heater away from fuel tanks. The B1 Adjusted layout reads C12 conservatively, with the tank's bottom above the heater body's top, and follows the direction of C1 by placing the tank on a separate horizontal footprint beside the heater. Spill paths along the structural members are **unassessed**: the two full-width crossmembers pass beneath the tank zone and could carry a spill toward the heater, and the rails, uprights, and base members are further candidate routes; SR-02 requires their review. What a review must still decide before SR-01 is closed: the vertical gap and horizontal separation values (D-15), using the heater body, exhaust, and silencer surface temperatures, which the manufacturer does not state and which would have to be established; whether a shield between tank and heater is needed; and the refuelling spill path (SR-02). Until that is written, this layout is a candidate that both instructions can be read to permit, not a reconciliation.

## 7. Fuel pump and fuel line

- M1 p.9 shows the fuel path tank → oil pipe → oil filter → pulse fuel pump in its sheath → oil pipe → heater, with 12 oil pipe clips and 12 ribbons (cable ties) supplied (M1 p.8).
- M1 states no pump mounting angle, orientation, height relative to tank or heater, or maximum line length. All are Unknown (Q-08). Diesel pulse pumps commonly have manufacturer-specified inclination ranges; **this manual does not give one, so none is assumed here**.
- The only positional instruction is C12: tank above the heater, to facilitate pump operation. This pulls the tank upward in the frame while C1 pulls it away from the heater. See SR-01.
- The pump position (L1 is the natural candidate) is open (D-05). In B1 Adjusted a pump in L1 sits below the tank outlet, whose position on the tank is Unknown (TNK-15); that is a geometric observation, not evidence that the pump will operate.
- **The supplied fuel line's length does not establish the pump's permitted maximum line length, lift, or inclination.** Those remain Unknown (Q-08). With VEVOR not being contacted, Q-08 closes only by a documented engineering assessment that records the pump's own markings (PMP-03), the supplied line length (FUL-01), the modelled tank-outlet-to-pump and pump-to-heater heights, and the basis for any limit it adopts.

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
- In this frame the exhaust leaves the heater downward into L1 and must exit the envelope. The exit side, the pipe length, where the silencer sits, and how the pipe is restrained are open (D-07). Proposal for review (2026-10-28, refined 2026-10-29): the exhaust turns horizontal or downward under the plate, exits through the wall opposite the tank (the +X wall) below the middle level, and terminates pointing away from the frame in +X, so that in plan it points neither at the heating-air inlet end (−Y) nor at the shelter, which lies on the duct side (+Y). The silencer sits outside the envelope on that side or low inside L1 with only the tail outside, to be decided at D-07. The intake pipe and filter run low under the heater toward −Y, and the pump and filter stay low on the tank side (D-05). The duct leaves the heater's +Y end above the middle-level member and out of the +Y end face. Whether the exhaust pipe can make its turn in the roughly 98 mm between the crossmembers and the base members depends on the exhaust stub's protrusion and the pipe's diameter and construction (HTR-13, EXH-01 to EXH-05). This is a plausible arrangement only; no clearance is claimed, and SR-03, SR-04, SR-07, SR-11, and the CO requirements are unchanged.
- Clearance from the exhaust and silencer to the tank, fuel line, wiring, extrusion, and ground cover is **not given by the manufacturer** and must be set by engineering review (SR-04). The surface temperature of the exhaust and silencer is not stated.
- Intake: intake pipe with air filter element in L1; must stay open and clear (C14). The intake and exhaust terminations must be separated so exhaust is not drawn in; the manufacturer gives no distance (Q-06).
- Hot-air outlet: inner diameter 3 in / 76.5 mm (C23); blowpipe and rotary tuyere (M1 p.7). The maximum duct run is not stated (Q-02 covers measuring the supplied parts).

## 9. Hot-air ducting to the shelter

The duct is the only part of the system that enters the shelter (SR-05). It carries whatever the heating-air inlet draws at L2 (§8), so the shelter end of the duct and the exhaust termination are to be considered together under SR-11. Its route from L2 to the shelter wall, its support, and how it is prevented from pulling the frame over (SR-10) are open (D-08). No duct extension is specified.

## 10. Stability and tip resistance

- Footprint 20 × 22 in; height about 35 in; the tank, when full, adds about 8–9 kg (A-05) high on one wall, and the heater's mass is unknown (A-06). The center of gravity will be high and off-center toward the tank wall, and higher in B1 Adjusted than in B1 Compact by the amount the tank was raised.
- SR-10 requires a tip assessment with the tank full on the worst-case ground, under handling push, duct pull, and wind. The criteria are to be set at engineering review.
- **Illustrative centre-of-gravity outline (Proposed; not the SR-10 assessment).** With assumed masses only, since none is Measured: frame about 12 kg (about 11 m of 20 × 40 extrusion at a typical 1.1 kg/m, vendor unknown), heater 5 kg (the C22 figure, scope unknown, A-06), tank with fuel 10 kg (A-05 plus an assumed 1.5 kg empty tank), the combined centre of gravity sits roughly 50 mm from the frame's centreline toward the tank wall and roughly 470 mm above the ground. The static tip angle on level ground would then be roughly 24 degrees toward the tank wall and roughly 30 degrees in the other directions. These numbers show what the assessment will look like and which direction governs; they are not to be cited as a result.
- **Stabilization options compared (2026-10-29).** The tank wall runs along the 22 in depth, so tipping toward it is across the 20 in width, the governing direction. The push figures below use the illustrative masses above and are **not evidence of anything**; they only rank the options.

  | Option | Base toward the tank wall | Illustrative top push that tips the module | Cost, complexity, portability |
  |---|---|---|---|
  | Standard leveling feet at the four corners | about 508 mm | about 60 N | Lowest; envelope unchanged |
  | Fixed foot bars across the width, extending about 100 mm beyond each side, with leveling feet at their ends | about 708 mm | about 95 N | Two short members, four brackets, four feet; ground footprint about 28 in wide; the module no longer passes through a 20 in gap and takes more floor space in a vehicle |
  | Deployable outriggers on the tank side, about 200 mm reach | about 900 mm | about 125 N | Hinges or slides with locks; more parts; tips if used undeployed |

- **Preferred preliminary direction for D-12 (Owner direction 2026-10-29; not an approved structural design):** fixed foot bars with leveling feet, accepting the roughly 28 in ground footprint and the loss of a 20 in pass-through; ballast rejected as mass to carry; outriggers held as the fallback if the SR-10 criterion is not met; pump, filter, silencer, and controller kept low in L1. The two foot bars are additional stabilization members, about 708 mm each, outside the 20 primary members of MR-01, which is unchanged. **What D-12 needs at G1 and what belongs to G5 are different things.** At G1, D-12 is recorded as decided when the stabilization concept is selected and documented on the basis of the mass estimates or measurements available (MAS-01 to MAS-03 and the supplier's mass per metre, or stated estimates where a reading does not yet exist), the stability criteria set at engineering review (a top push, a ground slope, a duct pull at heater height, a wind case), and a prospective tip assessment against those criteria (SR-10 at concept level, as G1(e) requires). At G5, the built and installed module is validated under its actual physical and operating conditions, including a tilt check; that validation is not a prerequisite for the G1 concept decision. D-12 is not yet decided. **Paracord staking is not a substitute for a self-supporting frame** (Owner decision 2026-10-27); it may be considered only as a supplement in wind.

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
- Tie-down points and lifting handles are undefined (MR-06). The frame's total mass is unknown (TR-03). Proposal for review (2026-10-28): lift by the top rectangle, which is why it is retained in the 18-member candidate, and tie down at the four base corners.
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
| D-01 | Joint method for the extrusion (corner brackets, end-tapped bolts, gussets) and therefore the cut-length derivation. Preferred preliminary approach 2026-10-29 (§3): interior corner brackets with T-nuts at every joint, doubled on the loaded members, gussets at the base corners. **Open**: decided only when the supplier-specific review in bom.md §2.1 is recorded | MR-05 |
| D-02 | Section orientation of each member. Preferred starting choices 2026-10-29 in §3; not confirmed adequacy. **Open** | D-01, MR-05 |
| D-03 | Which wall is the tank wall and which side the duct leaves. Proposal 2026-10-28: tank on the X-min wall as drawn, the wall that runs along the 22 in depth; duct from the heater's +Y end; exhaust exits the wall opposite the tank pointing +X (§8). **Open** until SR-01 is reconciled | SR-01, SR-04, D-07, D-08 |
| D-04 | Tank rail arrangement: two rails only, or an added short member or bracket for the upper point; whether a perimeter member doubles as a rail. Preferred preliminary approach 2026-10-29: two adjustable rails on sliding brackets (§6). **Open** until the mounting points are inspected and the Q-04/Q-05 assessment exists | Q-04, Q-05 |
| D-05 | Pump and oil filter position | Q-08 |
| D-06 | Use of L3 | None; may stay empty |
| D-07 | Exhaust exit side, pipe route, silencer location, pipe restraint | SR-03, SR-04 |
| D-08 | Duct route and strain relief | SR-10 |
| D-09 | Controller and harness mounting | SR-08, TR-01 |
| D-10 | Weather measure, if any | TR-01 |
| D-11 | Transport restraint, lifting, fuel state in transit | TR-02, MR-06 |
| D-12 | Stabilization method (outriggers, footprint, ballast, feet). Preferred preliminary direction 2026-10-29: fixed foot bars with leveling feet (§10). **Open** until the masses are recorded and the tip calculation against review criteria exists | SR-10 |
| D-13 | Exhaust termination position and direction relative to the heating-air inlet, the shelter's openings, and prevailing wind | SR-11, D-07, D-08 |
| D-14 | Whether to adopt the 18-member simplification (omit `L2-W1`, `L2-W2`) in place of MR-01's 20 members. Recorded alternative, deprioritized 2026-10-29 (§3); not adopted, not under investigation | MR-01, MR-05, D-01 |
| D-15 | The vertical gap between the heater body's top and the tank's bottom, and the horizontal separation, in B1 Adjusted. The CAD placeholder is 50 mm; the value is for the SR-01 engineering review and is not a clearance. Includes filler cap access (§4) | SR-01, SR-02, SR-04 |
| D-16 | The two mechanical interfaces and their combined load path (§5): Interface A, heater to its supplied plate by the factory fixing arrangement; Interface B, plate to the crossmembers, provisionally through the four corner holes with T-slot hardware; whether the two share any fastener (not assumed); whether the plate's underside opening and the three stubs clear the crossmembers at the derived pitch. The load path is unresolved until assessed; the dry-fit check in §5 is the first input | MR-03, MR-05, MR-07, Q-03 |
| D-17 | Spill route along the full-width heater crossmembers beneath the tank zone (§6). Rotating the crossmembers to run under the heater only was declined for this phase (owner, 2026-10-29) because it would load the unverified plate on its other pitch; candidate measures that do not rely on the plate are listed in §6. **Unresolved alternative**; SR-02 open | SR-02, D-16, MR-01 |

### 15.2 Questions (information needed; who can answer)

| ID | Question | Who |
|---|---|---|
| Q-01 | Does the manual in the owner's box match M1? Record its revision marks, if any, and any differences on the installation diagram and safety pages | Owner |
| Q-02 | Inventory the supplied parts against M1 p.7–8. Record the contents of "oil tank accessories" and "machine fixing piece", pipe diameters, blowpipe length, and the masses of the heater and the empty tank | Owner |
| Q-03 | The mounting plate's fixing hole pattern and sizes, and how the heater's seal and double-head screw nuts engage it. Pattern and sizes User-reported 2026-10-28 (§5), not Measured; engagement still unknown | Owner |
| Q-04 | What are the tank bosses rated to carry, and is vertical hanging on three points the intended installation? | VEVOR support; otherwise engineering review |
| Q-05 | How are the membrane-covered holes meant to be prepared, and with what fastener? | VEVOR support; owner inspection of the accessory kit |
| Q-06 | Permitted mounting orientation and tilt of the heater; clearance distances around the heater body, exhaust, silencer, and hot-air outlet; required separation of intake and exhaust terminations. The replacing judgement is required at G1 and its required contents are in §5 | VEVOR support; otherwise engineering review |
| Q-07 | Rating of the supplied in-line fuse and the gauge of the supplied power cord | Owner |
| Q-08 | Fuel pump mounting angle, orientation, maximum height difference, and maximum fuel line length | VEVOR support; otherwise engineering review |
| Q-09 | Which CO alarm will be used in the shelter (SR-06 makes one mandatory), and what placement of the module relative to the shelter is acceptable to the owner as the starting point for the SR-11 review? | Owner |
| Q-10 | Will overnight or unattended operation be permitted at all, and under what conditions? Unresolved; neither is approved (SR-12) | Owner, with engineering review |
| Q-11 | What does the M2 net weight of 11 lb / 5 kg cover, and what is the correct working-temperature range, given the inconsistent figures on M2 (C22, C24)? | VEVOR support |

The owner does not intend to contact VEVOR at this stage (2026-10-28). Where a question lists VEVOR, the alternative route in gate G1(a) applies: the question is recorded as unanswered and a dated engineering judgement that replaces it is written and reviewed. No such judgement exists yet for Q-04, Q-05, Q-06, Q-08, or Q-11.

### 15.3 Measurements that a concrete decision needs (deliberately few)

The measurement workflow and identifiers are in [measurements/](measurements/README.md). Only these readings are needed to settle a fit, structural, or safety decision for B1 Adjusted; everything else in the checklist is deferred until a decision asks for it.

| Decision | Readings | Identifiers |
|---|---|---|
| Crossmember pitch and whether the stubs and plate opening clear the crossmembers (D-16, MR-07) | Plate orientation on the heater; underside opening extents; stub positions, diameters, and protrusions | PLT-10, PLT-11, PLT-14; HTR-12 to HTR-14 |
| Interface A geometry, heater to plate (D-16) | Fixing stud or screw count, position, protrusion, and thread; seal | HTR-11, HTR-16, PLT-12 |
| Exhaust turn under the plate and exit side (D-07) | Exhaust stub protrusion; pipe outside diameter, construction, shape as supplied | HTR-13; EXH-01, EXH-04, EXH-05 |
| Frame height and filler access (D-15) | Filler position, neck and cap height | TNK-06 to TNK-08 |
| Tank mounting method (MR-04, Q-04, Q-05) | Each mounting point as found, wall thickness, accessory kit | TNK-10 to TNK-14, TNK-16 |
| Stability outline (SR-10) and transport (TR-03) | Heater, plate, and empty tank masses | MAS-01 to MAS-03 |

Also read during the same session, because they are G1(a) conditions and cost nothing extra: the in-line fuse rating and cord markings (Q-07; ELC-01, ELC-02), the paper manual's revision marks (Q-01; DOC-01), and the inventory and assembly state (Q-02; DOC-03).

Deferred: the heater's end faces and inlet (HTR-05 to HTR-10), the plate outline and thickness (PLT-01 to PLT-04, PLT-06 to PLT-09; the reported figures are enough for the concept), the silencer, intake, duct, and the rest of the electrical group, and the tank's outer shape, until a decision needs them. The earlier User-reported figures stay User-reported.

### 15.4 G1 readiness ledger (2026-10-29)

The conditions are those of gate G1 in [spec.md §10](spec.md#10-release-gates), unchanged. This ledger says only what kind of work each needs and where it stands. A preferred preliminary approach does not close a condition.

| G1 condition | Kind of work | Status and path |
|---|---|---|
| (a) Q-01 manual, Q-07 fuse and cord | Physical check, cheap | Read during the §5 dry-fit session; record dated |
| (a) Q-02 inventory and masses | Physical check; affects purchase | Same session; masses feed the SR-10 outline and TR-03 |
| (a) Q-03 plate pattern and Interface A engagement | Physical check; affects purchase | The §5 dry fit; then the D-16 assessment |
| (a) Q-05 membrane or through-hole preparation | Physical check, then judgement | Each point as found (TNK-10 to TNK-12) and the kit (TNK-16); a dated judgement if the kit does not settle it |
| (a) Q-04 boss rating | Engineering assessment | §6 evidence, then a dated judgement note; a proof load alone is not sufficient |
| (a) Q-06 orientation, tilt, clearances | Engineering judgement, required at G1 | Contents listed in §5; provisional clearances confirmed at G5 |
| (a) Q-08 pump | Engineering assessment | §7 evidence, then a dated judgement note |
| (b) SR-01 reconciled; tank wall and height fixed (D-03) | Engineering assessment | Proposed text in §6; needs the D-15 values and the D-17 review |
| (c) MR-04 mounting method established (H-01) | Follows Q-04 and Q-05 | After the tank inspection and assessment |
| (d) D-01, D-02, D-04, D-12 decided | Owner decisions after supplier and physical evidence | Preferred approaches recorded in §3, §6, §10; none decided. D-12 at G1 means the concept with a prospective tip assessment (§10), not the G5 validation |
| (e) Concept reviewed to a purchase-ready cut list and compatible hardware | Engineering assessment | After (a) to (d) and the supplier criteria in bom.md §2.1; bracket joints make member lengths follow from the envelope, but no length is derived yet. **Compatible hardware at G1 means purchasing specifications**: the joining hardware, the plate fasteners (Interface B), the tank fasteners, and the stabilization hardware with their sizes, thread compatibility with the chosen supplier system, fit with the reported plate holes and the tank points as found, and quantities, established far enough to buy. The tank fasteners stay unselectable until (c) |
| (f) Owner approval to purchase | Owner | Last |

What G1 does not include, as spec.md §10 already places them: the final structural adequacy review (MR-05 final), fabrication detail and installation, and the tank-hole preparation method before any hole is opened (G2); the supply cable, fuse, connector, and the cool-down interlock question (G3); tie-down and lifting detail, the transport fuel state, and the total mass (G4); exhaust termination and clearances, the SR-11 review, the CO alarm, weather measures, validation of the built module's stability, and any operating procedure (G5). Fastener purchasing specifications are a G1 matter, as (e) says; their final adequacy is G2.

## 16. Alternatives considered and rejected

Recorded per constitution Principle V. Each rejection stands unless a structural or safety finding under §14 shows a specific need, in which case the finding is to be written up before the element is reconsidered.

| Alternative | Reason rejected | Date |
|---|---|---|
| Fuel-tank shelf under the tank | Unnecessary if the factory bosses carry the tank (to be established, H-01); adds a surface that could collect spilled fuel | Owner decision 2026-10-27 |
| Full backplate on the tank wall | Not needed for the concept; adds mass and a flat surface; a partial plate would only be justified by H-01 or H-09 findings | Owner decision 2026-10-27 |
| Wooden mock-up before the aluminum frame | Owner prefers to go to the aluminum frame once the design is approved; mock-up adds a step without resolving the open questions, which are about loads and manufacturer limits rather than fit | Owner decision 2026-10-27 |
| Plastic operating enclosure, including the Greenmade 12-gallon tote | Open frame chosen for ventilation, access, and heat; an enclosure would conflict with C2 and C14 unless designed with ventilation, which is not wanted | Owner decision 2026-10-27 |
| Paracord staking as the primary stability method | Not a self-supporting solution; frame must stand on its own (SR-10) | Owner decision 2026-10-27 |

### 16.1 Layouts retained as alternatives (superseded as the preferred direction, not rejected)

| Layout | Description | Status |
|---|---|---|
| A Original | 20 × 24 × 38 in; tank entirely above the heater, middle level about 350 mm; the 2026-10-27 concept and the original MR-02 envelope | Superseded by B1 Adjusted on 2026-10-28; kept in the CAD model (`original`) and in `cad/out/comparison.md` |
| B1 Compact | 20 × 22 × 28 in; heater plate about 7 in, tank bottom about 8 in, tank beside the heater overlapping it in height; the owner's 2026-10-28 starting point | Superseded the same day by B1 Adjusted because the tank bottom sat below the heater top, which does not match the conservative reading of C12; kept in the CAD model (`compact`) |
| B1 Adjusted | 20 × 22 × about 35 in; as A Original's tank-above reading combined with B1 Compact's footprint and separate footprints | **Preferred preliminary layout** (Owner decision 2026-10-28); CAD default (`adjusted`) |

## Change log

| Date | Change |
|---|---|
| 2026-10-27 | Created from the owner's 2026-10-27 brief and the VEVOR manual and product page retrieved the same day. Concept recorded as decided; all hazards open; no cut lengths; no aluminum frame built or purchased (the heater and its supplied parts were already owned). |
| 2026-10-27 | PR #4 review corrections: §8 rewritten around the three air paths with the manual's labels; H-07 closure now requires the SR-11 review and accepted measures plus the CO alarm; D-13, Q-10, Q-11 added; manufacturer size, net weight (scope unknown), and outlet diameter recorded; cigarette-lighter prohibition noted; status corrected (heater owned and partly assembled, no frame purchased). Mechanical concept unchanged. |
| 2026-10-29 | G1 structural concept (Owner direction 2026-10-29, nothing closed): preferred joint system, section orientations, load paths, and what governs (§3); D-14 deprioritized; dry-fit check and the required contents of the Q-06 judgement (§5); tank load-case outline, fastener rules, and the D-17 spill-route alternative with plate-independent candidate measures (§6); routing refinement (§8); stabilization options compared and fixed foot bars preferred with the 28 in footprint trade-off (§10); D-01, D-02, D-04, D-12 rows marked open with their preferred approaches; D-17 added; §15.3 session additions; §15.4 G1 readiness ledger. G1 conditions unchanged; gates closed; no cut length; hazards all open. Codex corrections the same day: §3 member bending and deflection not excluded (no model or calculation yet); §10 D-12 split into the G1 concept decision with a prospective assessment and the G5 validation of the built module, foot bars as two additional members outside MR-01; §15.4 fastener purchasing specifications are a G1 matter, final adequacy G2. |
| 2026-10-28 | B1 Adjusted recorded as the preferred preliminary layout (Owner decision): 20 × 22 × about 35 in, plate about 7 in, tank beside the heater with its bottom above the heater top; A Original and B1 Compact retained (§16.1). Height stack-up and filler access check (§4); owner-reported plate holes, edge clearance, and thickness estimate, the two fastening interfaces with their unresolved load path, and the adjustable mounting proposal (§5, D-16); adjustable tank rails, boss-strength evidence, and a Proposed SR-01 reconciliation for review (§6); fuel-line statement (§7); exhaust exit proposal (§8); illustrative centre-of-gravity outline and stabilization strategy (§10); lifting proposal (§13); proposals under D-01 to D-04 and D-12; D-14 (18-member candidate), D-15 (gap), D-16 (plate fastening) added; §15.3 lists the few measurements a decision needs. Hazards all open; no cut lengths; gates G1–G5 closed. |
