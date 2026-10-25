# Battery Box V1 — Verification Status and Open Safety Concerns

**Status**: Authoritative record of what has and has not been verified on the V1 prototype
**Snapshot date**: 2026-10-25
**Companion**: [as-built.md](as-built.md) describes the hardware; this file describes its evidence state.

**Readiness statement: the V1 prototype is a bench prototype with exposed conductors and no verified protection records. It must not be transported or deployed, and loads other than those already observed on the bench should not be connected, until the items in §2 and §3 are closed.**

This document records concerns and evidence gaps. It does not prescribe hardware changes, select components, or define test procedures; those require engineering review and owner approval before they are written.

---

## 1. Evidence rules

- Evidence tags are defined in [as-built.md §1](as-built.md#1-how-to-read-this-document).
- A verification item is **closed** only by a dated record stating who performed it, the method and instrument, the value or observation, and the pass/fail judgement. Memory of having done a check does not close an item.
- Historical observations (§4) stay in §4. New evidence goes in §6 and is never merged into the historical record.
- Nothing in this document may be marked passed on the strength of a design document, a checklist tick, or an inference.

## 2. Open safety concerns

Each concern lists what is known, why it matters, and what would close it. None are closed.

| # | Concern | Evidence state | Why it matters | What closes it |
|---|---|---|---|---|
| S1 | **Exposed conductors and terminals.** No enclosure; battery terminals, bus bars, and wiring are accessible | User-reported (2026-10-25) | A dropped tool or stray metal across a 200 Ah LiFePO4 battery or the 100 A bus is a short-circuit and burn hazard. Spec FR-006 and FR-008 are unmet | Owner-approved mechanical and electrical protection, then a recorded inspection |
| S2 | **No master disconnect.** The only way to de-energize the bus is to remove the 100 A ANL fuse | User-reported | Removing a fuse under load is not a switching method and risks arcing at the holder. Task T134's draft idea of "pull the ANL fuse" for emergency shutdown is **not endorsed** | Engineering review of an isolation method, owner approval, then recorded installation |
| S3 | **Insecure mounting.** Battery and panel held together only by two cam-buckle straps; nothing anchors the assembly | User-reported; Visually observed | Movement during handling can strain 4 AWG terminations and bring conductors into contact | Owner-approved mounting, then recorded inspection |
| S4 | **Victron sensing-wire protection unknown.** The small red wire from the shunt to battery positive has not been checked for an inline fuse | Visually observed (wire present); fuse Unknown | An unfused sense wire on a 200 Ah battery is an unprotected conductor if it chafes | Visual confirmation of a fuse and its rating, recorded with a photograph reference |
| S5 | **Main fuse specifications unknown.** The 100 A ANL fuse's manufacturer, DC voltage rating, and interrupt rating are not recorded; the BOJACK holder's ratings are not recorded | Historical (generic "100A ANL fuse" purchase); User-reported (holder brand) | The main fuse must be able to interrupt the battery's short-circuit current. No record shows it can | Recorded part identification and datasheet reference, then engineering review |
| S6 | **Connector ratings unknown.** The two SB50-style sockets and two Powerpole-style connections have no recorded manufacturer, part number, or contact rating | User-reported procurement origin; Visually observed | Branch fuses are 30 A on three connectors whose contact ratings are not on record | Recorded part identification, then engineering review |
| S7 | **Fuse-to-connector margin needs engineering review.** Three branches carry 30 A fuses. The constitution requires connections rated for expected current plus 25 % margin. Whether the installed connectors meet that cannot be judged until S6 is closed | Derived from S6 | A 30 A fuse on a connector rated at or below 30 A would leave the connector as the weakest element. **This is not recorded as a violation**; it is recorded as unreviewed | S6 closed, then a written engineering review of each branch's fuse, wire, and connector ratings |
| S8 | **Charge path undefined.** No connector is designated for charging and no adapter cable is recorded | Historical (T066–T078 open); User-reported | Any charging done since March 2026 used an unrecorded connection with unknown protection and polarity safeguards | Owner statement of how charging has been done, then design review before any charge connection is documented as approved |
| S9 | **Branch negatives not traced.** Design intent routes all negatives through the shunt via the Blue Sea negative bus; the built wiring has not been traced | Unknown | A negative that bypasses the shunt makes the Victron current and SOC readings wrong and may leave a conductor outside the intended return path | De-energized tracing, recorded per branch |
| S10 | **No labels.** No connector, fuse position, or terminal is labelled | Historical (T037, T043, T136 open) | Spec FR-009 unmet; a user cannot tell a 15 A branch from a 30 A branch or identify polarity | Recorded labelling after S9 and the mapping in as-built §4.3 are closed |
| S11 | **Victron SOC uncalibrated.** Synchronization after a full charge (T053) never performed | Historical | The SOC % and time-to-go shown on the display are not trustworthy; the design relies on them for safe heater runtime | Recorded synchronization event after a recorded full charge |

## 3. Verification backlog

| # | Item | Status | Evidence on record | What closes it |
|---|---|---|---|---|
| V1 | Polarity at every connector and bus | **Unknown** | Owner recalls some multimeter checks; no values, dates, or points recorded | Dated per-point record |
| V2 | Continuity of main path (battery → ANL → bus; battery → shunt → bus) | **Unknown** | None | Dated resistance or continuity record per segment, battery disconnected |
| V3 | Continuity and routing of each branch, including negatives (see S9) | **Unknown** | None | Dated per-branch record |
| V4 | Short check, positive bus to negative bus | **Unknown** | None | Dated record |
| V5 | Crimp integrity, 4 AWG terminations | **Historical pass, not re-verified** | Manual pull tests passed with iCrimp crimper and AWG terminals, 2026-03-07 (pass/fail only, no force value) | Recorded re-inspection if any termination has been disturbed since |
| V6 | Crimp integrity, 10 AWG branch terminations and connector contacts | **Unknown** | None | Dated record per termination |
| V7 | Terminal torque at battery, ANL holder, shunt, bus | **Unknown** | None | Dated record |
| V8 | Voltage at bus and at each connector, no load | **Unknown** | 2026-03-07 power-up: "Victron displaying correctly, Nilight functional" (no values) | Dated per-point record |
| V9 | Voltage drop under load | **Unknown** | None | Deferred until S1–S3 are closed; requires an approved procedure |
| V10 | Load test | **Unknown** | None | As V9 |
| V11 | Thermal check under load | **Unknown** | None | As V9 |
| V12 | Charging validation | **Unknown** | None; charge path undefined (S8) | Deferred until S8 is closed |
| V13 | Victron SOC synchronization | **Not done** | T053 open | See S11 |
| V14 | Victron alarm settings | **Historical, unverified** | T052 marked complete 2026-03-07; values not recorded in the log | Recorded screenshot or readback of settings |
| V15 | Fuse interruption (SC-003) | **Procedure withdrawn** | None | A non-destructive validation method must be defined and approved before this item can be scheduled |
| V16 | Sensing-wire fuse presence | **Unknown** | None | See S4 |
| V17 | Main fuse and holder ratings | **Unknown** | None | See S5 |
| V18 | Connector identification and ratings | **Unknown** | None | See S6 |
| V19 | Position-to-connector mapping | **Unknown** | None | De-energized tracing; updates as-built §4.3 |

## 4. Historical measurements on record

These are the only dated measurements in the repository. They describe the system at the date given, not today.

| Date | Measurement | Value | Source |
|---|---|---|---|
| 2026-01-19 | Battery terminal voltage on receipt, multimeter | 13.34 V | tasks.md build log, T001 |
| 2026-01-19 | Charger no-load output, multimeter | 14.64 V | tasks.md build log, T002 |
| 2026-01-19 | Tote external dimensions | 30.4" × 20.4" × 14.7" | tasks.md build log, T003 (tote since abandoned) |
| 2026-02-07 | Stud sizes: battery posts, ANL holder, Blue Sea busbar, Victron shunt | M8, M8, ~4 mm, M10 | tasks.md Lessons Learned; shopping-list.md |
| 2026-02-07 | 4 AWG crimps with Sanuke crimper and SC25-8 terminals, manual pull test | Fail (wire pulled out) | tasks.md Lessons Learned |
| 2026-03-07 | 4 AWG crimps with iCrimp crimper and TKDMR/XHF terminals, manual pull test | Pass (no force value) | tasks.md build log |
| 2026-03-07 | Drilled holes: Nilight 4 × 1-1/4", Victron 52 mm square, KarlKers 2 × 1-1/4" | As stated | tasks.md build log, T013–T015 |
| 2026-03-07 | First power-up | Victron display on, Nilight functional, "no issues detected"; no values | tasks.md build log, T099–T100 |

Owner recollection (2026-10-25): some multimeter checks were performed at an unrecorded time; details not remembered. Recorded here as User-reported and **not** counted as verification.

## 5. Withdrawn procedures

The following historical instructions are withdrawn as current guidance. The text remains in its original file under a notice so the design history is preserved.

| Location | What it instructs | Why withdrawn |
|---|---|---|
| quickstart.md §4.5 | Crimp 4 AWG with the Sanuke/Solsop hydraulic crimper, 25 mm² die | The method failed pull tests on 2026-02-07; tool and terminals were returned. Following it produces unsafe terminations |
| quickstart.md §4.6 Phase 2 and testing Phase 2.1 | "Connect negative first" and "connect positive first" respectively | Contradictory energization sequences in one document |
| quickstart.md §4.6 Phase 5 | Insert the 100 A ANL fuse as the step that energizes the system; "may spark slightly - normal" | Uses the main fuse as a switch and normalizes arcing at the holder. Contradicts Step 12 and Phase 2 (fuses in, then connect battery) |
| quickstart.md orphaned block 6.1–6.5 (between Steps 7 and 8) | Separate inline charge fuse holder, Schottky diode, "crimp/solder", charge negative wired to battery negative | Leftover from an earlier draft; contradicts the Blue Sea circuit approach and routes a negative around the shunt |
| quickstart.md §3.4 Test 4; research.md §10 Phase 3 Test 4; tasks.md T040–T042 and T113–T117; spec.md SC-003 and User Story 1 scenario 2 | Deliberately overload an assembled circuit to 150 % of the fuse rating until the fuse blows | Destructive testing of the assembled system is withdrawn. A validation approach for SC-003 is an open design question |
| quickstart.md §7 Operating Instructions | Pre-use checks and charging procedure keyed to green/yellow/red status LEDs; "red to charge input red" | The LEDs were deferred and never built; no charge input exists. Not operating instructions for the current prototype |
| quickstart.md §8 Troubleshooting (LED items) | Adjust LED trigger-circuit thresholds | Circuits do not exist |
| quickstart.md testing Phase 6.2 | Pass/fail list keyed to SC-004, SC-005, SC-007, SC-009, SC-010 | Numbering does not match spec.md; results recorded against it would be mis-mapped |
| contracts/component-interfaces.md Contract Validation Checklist and "Satisfies Contract" lists | Ticked compliance for every component | Ticked at design time without records; several items describe hardware that never existed (mesh vents, ratchet straps bolted to the tote, grommets, labels) |
| tasks.md T134 (unexecuted draft) | Emergency shutdown by pulling the 100 A ANL fuse | Not endorsed as a switching or shutdown method; see S2 |

No replacement procedures are written here. New procedures require engineering review and owner approval first.

## 6. New verification records

Append new evidence below. One row per record. Do not edit §4.

| Date | Item (S# / V#) | Performed by | Method and instrument | Result | Closes item? |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

## Change log

| Date | Change |
|---|---|
| 2026-10-25 | Created. All items open. No new measurements taken. |
