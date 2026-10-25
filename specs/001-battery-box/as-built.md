# Battery Box V1 — As-Built Configuration

**Status**: Authoritative description of the V1 prototype as it physically exists
**Snapshot date**: 2026-10-25
**Readiness**: Bench prototype. **Not ready for transport or deployment** — see [verification-and-safety.md](verification-and-safety.md)
**Supersedes**: The design-phase documents in this directory (spec, plan, research, data-model, quickstart, contracts, docs/) for any question about the current hardware. Those files remain as the design history.
**Provenance**: Every User-reported and Visually observed claim dated 2026-10-25 traces to [reconciliation-2026-10-25.md](reconciliation-2026-10-25.md) (record R-2026-10-25).

---

## 1. How to read this document

Every hardware claim carries an evidence tag. A claim with no tag inherits the tag of its table row or paragraph.

| Tag | Meaning | Source for this snapshot |
|---|---|---|
| **Historical** | Recorded in the repository during the Jan–Mar 2026 build | `tasks.md` build log, `docs/shopping-list.md`, commit history on `001-battery-box` |
| **User-reported** | Stated by the project owner from memory or inspection, not independently checked | Owner's reconciliation with ChatGPT, delivered in the 2026-10-25 session brief and one follow-up clarification. Claim-by-claim provenance: [R-2026-10-25 §3.1](reconciliation-2026-10-25.md#31-claims-as-stated-in-the-brief) |
| **Visually observed** | Seen in the owner's photographs | Photographs taken by the owner in October 2026, retained by the owner outside the repository, reviewed by the owner with ChatGPT and summarized in the 2026-10-25 brief. Neither the photographs nor a claim-by-claim attribution were supplied to Claude Code or Codex; the tag records the implementer's attribution, pending owner confirmation. See [R-2026-10-25 §3](reconciliation-2026-10-25.md#3-attribution-of-claims) and verification item V22 |
| **Measured** | A dated numeric reading with the instrument or method recorded | Only the entries listed in [verification-and-safety.md §4](verification-and-safety.md#4-historical-measurements-on-record) |
| **Verified** | Independently confirmed after this document was created, with a dated record | **None yet.** Nothing in this document is Verified. |
| **Unknown** | No evidence either way, or evidence conflicts | — |

Nothing here is inferred from design documents alone. Where the design and the build diverge, §7 records it.

## 2. Summary

The V1 prototype is a VEVOR 12.8 V 200 Ah LiFePO4 battery feeding a Blue Sea Systems 5026 fuse block through a 100 A ANL main fuse, with a Victron BMV-712 shunt in the negative trunk. Five fused branches leave the fuse block: two large gray SB50-style panel sockets, two smaller red/black Powerpole-style panel connections, and a Nilight accessory panel. The original Greenmade 27-gallon tote was abandoned; one tote wall now serves as the component mounting panel, and two cam-buckle straps hold the battery and panel together. Electrical connections are exposed. There is no master disconnect and no enclosure.

The system was first powered on 2026-03-07 and the Victron display and Nilight panel have been seen operating. No polarity, continuity, voltage-drop, load, thermal, charging, or state-of-charge calibration records exist in the repository. The documented operating history demonstrates function, not safety, and does not authorize continued operation; see the readiness statement in [verification-and-safety.md](verification-and-safety.md).

## 3. Main power path

| Segment | Description | Evidence |
|---|---|---|
| Battery positive → main fuse | 4 AWG red to a 100 A ANL fuse in a BOJACK-brand inline holder | User-reported (Oct 2026). Consistent with Historical T021 (2026-03-07). Holder brand is User-reported only; ANL fuse manufacturer and interrupt rating Unknown |
| Main fuse → positive bus | 4 AWG red to the Blue Sea 5026 positive busbar | User-reported; consistent with Historical T023 |
| Battery negative → shunt | 4 AWG black to the Victron BMV-712 shunt, battery side | User-reported; consistent with Historical T025 |
| Shunt → negative bus | 4 AWG black from the shunt system side to the Blue Sea 5026 negative bus | User-reported; consistent with Historical T026 |
| Shunt sensing | Small red wire from the shunt to battery positive; white RJ12 cable from the shunt to the BMV-712 display | Visually observed (attribution pending, R-2026-10-25 R4). **Inline fuse on the red sensing wire: Unknown.** The owner reports it has not been visually verified, and the design documents do not mention it. The manufacturer's installation manual describes the supplied sense cable as carrying an inline fuse; whether that cable was used, and whether a fuse is present, is not recorded. See verification S4 |
| Master disconnect | None installed | User-reported |
| Battery terminal protection | Unknown. Connections described as exposed | User-reported |

Design intent was that every branch negative returns to the Blue Sea negative bus so all current passes through the shunt. Whether all five branch negatives actually land on that bus has not been traced (**Unknown**).

## 4. Distribution circuits

### 4.1 Populated fuse positions

Blue Sea 5026 positions and installed blade fuses, as seen in the owner's photographs:

| Physical position | Installed fuse |
|---|---|
| 8 | 30 A |
| 9 | 30 A |
| 10 | 15 A |
| 11 | 30 A |
| 12 | 20 A |

Evidence: Visually observed (Oct 2026). Positions 1–7 are reported empty (User-reported). Fuse manufacturer: blade-fuse assortment kit purchased 2026-01-19 (Historical); specific brand Unknown.

### 4.2 Branches

| Branch | Reported protection | Wiring | Evidence |
|---|---|---|---|
| Large gray SB50-style panel socket, #1 | 30 A | 10 AWG, direct to contacts | Connector: Visually observed. Protection and wiring: User-reported |
| Large gray SB50-style panel socket, #2 | 30 A | 10 AWG, direct to contacts | Same |
| Smaller red/black Powerpole-style panel connection, #1 | 30 A | 10 AWG, direct to contacts | Same |
| Smaller red/black Powerpole-style panel connection, #2 | 15 A | 10 AWG, direct to contacts | Same |
| Nilight 4-in-1 accessory panel | 20 A | 10 AWG to spade terminals | Protection: User-reported. Wiring: Historical T046–T048 (2026-03-07) |

The design documents specified 12 AWG pigtails between the 10 AWG branch wire and the connector contacts. The owner reports the build has **no pigtails**; 10 AWG lands directly on the contacts (User-reported, not visually confirmed on every branch).

### 4.3 Connector-to-position mapping — PROVISIONAL

**No branch has been physically traced from its fuse position to its connector.** The owner's reported fuse ratings per branch (above) and the observed fuses per position (4.1) are consistent with each other, which allows this inference only:

- Position 10 (the only 15 A) would feed the 15 A Powerpole-style branch.
- Position 12 (the only 20 A) would feed the Nilight panel.
- Positions 8, 9 and 11 (all 30 A) cannot be distinguished without tracing.

This is inference, tagged **Unknown/proposed**. Do not label, operate, or modify any branch on the basis of this mapping until tracing is recorded.

### 4.4 Branch assignments

**No connector has been assigned or validated for charging, refrigeration, heating, or any other load.** The design documents' allocation (charge input, heater, fridge, USB panel, two spares on positions 1–6) does not correspond to the built circuits and must not be read onto them.

**Charge path: Unknown. No dedicated charge input has been identified or verified.** The design called for a dedicated charge input on Blue Sea circuit 1 with a charger adapter cable; no record shows that work (tasks T066–T078) was done, and the owner's 2026-10-25 reconciliation did not identify a charge connection. How the battery has been charged since March 2026, if at all, is not recorded.

## 5. Component inventory

| Component | Identity | Evidence | Notes |
|---|---|---|---|
| Battery | VEVOR 12.8 V 200 Ah LiFePO4, product ID 010230251465 | Historical (shopping list, component-selection); User-reported confirms | Integrated 100 A BMS per manufacturer listing (Historical, unverified). Receipt voltage 13.34 V on 2026-01-19 (Measured). Serial number never recorded |
| Main fuse | 100 A ANL | Historical (7-pack purchased 2026-01-19); User-reported | Manufacturer, DC voltage rating, and interrupt rating: Unknown |
| Main fuse holder | BOJACK inline ANL holder | User-reported | Model and ratings Unknown. Shopping list recorded only "ANL fuse holder (inline)" |
| Fuse block | Blue Sea Systems 5026, 12-circuit ST blade, with negative bus | Historical (purchased 2026-01-20); Visually observed | Busbar rating 100 A per manufacturer (Historical) |
| Battery monitor | Victron BMV-712 Smart with 500 A / 50 mV shunt and panel display | Historical (purchased 2026-01-20); Visually observed | Build log T051 (2026-03-07) records the configuration as 200 Ah capacity, 14.4 V charged voltage, and "4 A" tail current (Historical). **Unit discrepancy:** the manufacturer's manual defines tail current as a percentage of battery capacity (default 4.00 %, range 0.50–10.00 %), not in amperes ([Victron BMV-712 settings](https://www.victronenergy.com/media/pg/BMV-712_Smart/en/all-features-and-settings.html)). The historical "4 A" entry is preserved as written; the value actually entered on the device is **Unknown** pending a documented settings readback (verification V20). Alarms enabled per T052 (Historical; values not read back, V14). No completed SOC synchronization is documented (T053 open); current status Unknown; SOC % must be treated as uncalibrated |
| Accessory panel | Nilight 4-in-1 (USB-C, USB-A, 12 V socket, voltmeter, on/off switch) | Historical; operation User-reported | Exact model, port ratings, and internal protection Unknown. Design docs disagree with each other on its specifications |
| Panel sockets, gray | Two SB50-compatible panel-mount sockets | User-reported (procurement); Visually observed | Supplied with a later purchase of two SB50-compatible panel-mount socket kits, separate from the KarlKers units. Manufacturer, part number, contact rating, and wire-gauge acceptance: **Unknown** |
| Panel connections, red/black | Two smaller Powerpole-style panel connections | Visually observed | Whether these are the KarlKers units (ASIN B0F4L5FYQ2, purchased 2026-01-24, Historical) is **Unknown**. Contact rating Unknown |
| Trunk wire | 4 AWG red and black | Historical; User-reported | Insulation type/temperature rating not recorded |
| Branch wire | 10 AWG red and black | Historical; User-reported | As above |
| 4 AWG terminals | TKDMR 5/16" and 3/8" stud, XHF 1/4" stud | Historical (ordered 2026-02-07) | Stud sizes measured 2026-02-07: battery M8, ANL holder M8, Blue Sea ~4 mm, shunt M10 (Measured) |
| Crimp tools | iCrimp battery-lug crimper (4 AWG); Knoweasy Powerpole crimper | Historical | Sanuke hydraulic crimper and SC25-8 terminals returned after failed crimps (Historical, 2026-02-07) |
| Mounting panel | One wall cut from the Greenmade tote | User-reported | Relationship to the 3/4" plywood panel recorded in the build log (8"→5" tapered × 12", mounted 2026-03-07) is Unknown |
| Battery base | 3/4" plywood 15" × 25" with four strap loops | Historical (2026-01-24/25) | Whether still in use: Unknown |
| Straps | Two cam-buckle straps around battery and panel | User-reported; Visually observed | |
| Cushioning | VEVOR shipping foam retained around battery | Historical (2026-01-19); User-reported | |
| Enclosure | **None.** Greenmade 27-gal tote abandoned (too bulky and heavy) | User-reported | |
| Charger (external) | VEVOR 20 A LiFePO4 charger, model 010889683485 | Historical | 14.64 V no-load on 2026-01-19 (Measured). Not part of the box. No record of an adapter cable to the box being built; status Unknown |

## 6. Mechanical configuration

- The tote is no longer used. One of its walls was cut out and is the component mounting panel (User-reported).
- The battery keeps its white foam cushioning (Historical; User-reported).
- Two cam-buckle straps wrap the entire battery-and-panel assembly (User-reported; Visually observed). Nothing anchors the assembly to a base or enclosure (User-reported).
- Electrical connections are exposed (User-reported).
- No record shows the design's ventilation holes and mesh were made (Historical: T016, T017 open); they are moot without an enclosure.
- No labeling record was found (Historical: T037, T043, T044, T136 open). Current labeling status is unverified; the 2026-10-25 reconciliation did not address it.
- A permanent enclosure redesign is deferred by the owner. The immediate safety concerns are listed in [verification-and-safety.md](verification-and-safety.md).

## 7. Deviations from the design documents

| Topic | Design documents said | As built | Evidence |
|---|---|---|---|
| Enclosure | Greenmade 27-gal tote with lid, vents, mesh | No enclosure; tote wall reused as panel | User-reported |
| Circuits | Six circuits on positions 1–6 (charge 30 A, heater 10 A, fridge 15 A, USB 20 A, spares 20/15 A) | Five circuits on positions 8–12 (30/30/15/30/20 A), unassigned | Visually observed; User-reported |
| Fuses installed 2026-03-07 | 30 A, 10 A, 20 A on positions 1, 2, 4 (Historical T098) | No 10 A fuse present; positions 1–7 empty | Visually observed. When and why this changed is not recorded |
| Connectors | Two KarlKers Powerpole panel units, generic PP45 for later circuits | Two gray SB50-style sockets from a separate later purchase, plus two Powerpole-style connections | User-reported; Visually observed |
| Branch wiring | 10 AWG with 12 AWG pigtails to contacts | 10 AWG direct, no pigtails | User-reported |
| 4 AWG crimping | Sanuke hydraulic crimper, 25 mm² die | iCrimp AWG crimper with AWG terminals after Sanuke crimps failed pull tests | Historical (2026-02-07, 2026-03-07) |
| Charge input | Blue Sea circuit 1, KarlKers connector, adapter cable | No dedicated charge input identified or verified; charge path Unknown | Historical (T066–T078 open); User-reported |
| Battery restraint | Two ratchet straps bolted through the tote floor | Cam-buckle straps around battery and panel | Historical; User-reported |
| Status indication | Design-phase 3-LED system (deferred) | Nilight switch LED and Victron display only | Historical |
| Victron SOC | Synchronize after first full charge | No completed synchronization documented; current status Unknown | Historical (T053 open) |
| KarlKers hole size | 1-1/8" (28.6 mm) | Drilled 1-1/4" per build log | Historical (T013–T015 vs quickstart) |
| Master disconnect | Not specified; emergency shutdown by pulling the ANL fuse (T134, not written) | None installed | User-reported |

## 8. Superseded and withdrawn material

The following historical procedures are withdrawn as current guidance. Their text is preserved in place with a notice. Details and reasons are in [verification-and-safety.md §5](verification-and-safety.md#5-withdrawn-procedures).

- `quickstart.md` §4.5 Sanuke/Solsop crimping procedure
- `quickstart.md` §4.6 energization sequence (contradicts testing Phase 2.1; uses the ANL fuse as the energizing switch)
- `quickstart.md` orphaned charging block (6.1–6.5 between Steps 7 and 8)
- `quickstart.md` §3.4 Test 4 and `research.md` §10 Test 4 destructive fuse tests; `tasks.md` T040–T042 and T113–T117
- `quickstart.md` §7 Operating Instructions and §8 Troubleshooting (reference status LEDs that are not recorded as built; not operating instructions for the current prototype)
- `contracts/component-interfaces.md` Contract Validation Checklist (ticked without evidence)

## 9. Open questions

- Which fuse position feeds which connector (requires tracing).
- Identity, manufacturer, and contact ratings of all four panel connectors.
- Whether all branch negatives return via the Blue Sea negative bus and the shunt.
- Whether the Victron sensing wire is fused.
- Main fuse manufacturer and interrupt rating.
- How, and whether, the battery has been charged since 2026-03-07.
- Whether the plywood panel and base from the build log are still part of the assembly.
- The Victron BMV-712 settings actually in effect, in particular the tail current: the build log's "4 A" conflicts with the manual's percentage unit (§5; verification V20).
- Whether any labels have been applied since the build log (§6; verification S10).
- Which 2026-10-25 claims were read from photographs rather than stated ([R-2026-10-25 §6](reconciliation-2026-10-25.md#6-open-attribution-items); verification V22).

## Change log

| Date | Change |
|---|---|
| 2026-10-25 | Created from the owner's reconciliation and the repository's historical records. No new measurements taken. |
| 2026-10-25 | PR #1 review corrections: provenance link to R-2026-10-25; Visually observed tag marked attribution-pending; Victron tail-current unit discrepancy recorded, device setting Unknown; categorical absence statements (synchronization, labels, charge input, vents, adapter cable, LEDs) reworded to distinguish documented absence from unknown status; open questions extended. No new measurements taken. |
