# Personal Power System

A long-term, modular project to build, understand, and evolve a self-managed 12 V DC power platform for camping, vehicle use, and portable backup. See [vision.md](vision.md) for purpose and philosophy and [.specify/memory/constitution.md](.specify/memory/constitution.md) for the governing principles. Safety First is the first principle and overrides everything else.

## Project status (2026-10-25)

**Battery Box V1 is a working bench prototype. It is not ready for transport or deployment.**

- The system powered on for the first time on 2026-03-07. The Victron monitor and Nilight accessory panel have been observed or reported operating. That history demonstrates function, not safety, and does not authorize continued operation.
- Electrical connections are exposed, there is no enclosure, no master disconnect, and the assembly is held together only by two cam-buckle straps.
- No polarity, continuity, voltage-drop, load, thermal, or charging validation records exist in the repository. Undocumented checks are not counted as passed.
- No dedicated charge input has been identified or verified. Connector-to-fuse mapping has not been traced.

The full list of open safety concerns and the verification backlog is in [verification-and-safety.md](specs/001-battery-box/verification-and-safety.md).

## Authoritative documentation

For any question about the hardware as it exists today, use these three files and nothing else. The first two describe the hardware and its verification state; the third records where the evidence came from.

| Document | Purpose |
|---|---|
| [specs/001-battery-box/as-built.md](specs/001-battery-box/as-built.md) | Canonical description of the V1 hardware: power path, fuse positions, branches, component inventory, mechanical configuration, and deviations from the design. Every claim carries an evidence tag. |
| [specs/001-battery-box/verification-and-safety.md](specs/001-battery-box/verification-and-safety.md) | Open safety concerns, verification backlog, the historical measurements on record, and the list of withdrawn procedures. |
| [specs/001-battery-box/reconciliation-2026-10-25.md](specs/001-battery-box/reconciliation-2026-10-25.md) | Provenance of the 2026-10-25 snapshot: what the owner stated, what was attributed to photographs, and what no reviewer inspected. The photographs are held by the owner outside the repository. |

## Historical design documents

The remaining files under `specs/001-battery-box/` were written in January–March 2026 with the SpecKit methodology and describe the design as planned, not the build as it exists. They are preserved as the design record and carry a status notice at the top. Where they conflict with the as-built documents, the as-built documents govern.

| Document | Role |
|---|---|
| [spec.md](specs/001-battery-box/spec.md) | Requirements and success criteria |
| [plan.md](specs/001-battery-box/plan.md), [research.md](specs/001-battery-box/research.md) | Technical approach and design rationale |
| [data-model.md](specs/001-battery-box/data-model.md), [contracts/component-interfaces.md](specs/001-battery-box/contracts/component-interfaces.md) | Component model and interface contracts |
| [quickstart.md](specs/001-battery-box/quickstart.md) | Design-phase assembly guide. **Superseded; not an operating manual.** Several sections are withdrawn. |
| [tasks.md](specs/001-battery-box/tasks.md) | Task list and the dated **build log and lessons learned**, which remain the primary historical record |
| [docs/component-selection.md](specs/001-battery-box/docs/component-selection.md), [docs/shopping-list.md](specs/001-battery-box/docs/shopping-list.md) | Component decisions and purchase history |

## Diesel Heater Module (002)

**Specification phase only. Nothing has been built, purchased, or approved for fabrication.** A portable T-slot aluminum frame for the owner's VEVOR 12 V 2 kW diesel air heater (model XMZ-D2) and its supplied 10 L tank, for winter camping. All safety hazards are open; the frame envelope and rail count are preliminary; Battery Box V1 is not approved to power it.

| Document | Purpose |
|---|---|
| [specs/002-diesel-heater/spec.md](specs/002-diesel-heater/spec.md) | Requirements, manufacturer constraints with manual page citations, unsupported assumptions, acceptance criteria, and the purchase, fabrication, and first-operation gates (all closed). |
| [specs/002-diesel-heater/design.md](specs/002-diesel-heater/design.md) | Preliminary frame concept, member schedule without cut lengths, hazard register, open decisions and questions, rejected alternatives. |
| [specs/002-diesel-heater/bom.md](specs/002-diesel-heater/bom.md) | Owned equipment and the manufacturer's packing list; procurement categories marked not purchase-ready. |

## How work is done

The project follows the AI Development Playbook v1.1, summarized in [CLAUDE.md](CLAUDE.md): evidence-based verification, scoped implementation, independent review when justified, and human approval. ChatGPT coordinates planning and review, Claude Code implements repository changes, Codex performs independent read-only review of consequential changes, and the project owner performs physical verification and gives final approval.

Hardware claims use six evidence categories: Historical/documented, User-reported, Visually observed, Measured, Verified, and Unknown/proposed. Nothing is recorded as verified without a dated record.

## Repository layout

```text
README.md                         This file
vision.md                         Project purpose and philosophy
CLAUDE.md                         Guidance for AI agents working in this repository
.specify/memory/constitution.md   Governing principles (v1.0.0)
specs/001-battery-box/            Battery Box V1: as-built, verification, and design history
specs/002-diesel-heater/          Diesel Heater Module: specification, preliminary design, BOM (nothing built)
.specify/, .github/, .claude/     SpecKit tooling retained from the original methodology (historical)
```

## Branches

`main` is the baseline and contains the reconciled Battery Box V1 documentation (integrated 2026-10-25 through [PR #1](https://github.com/sdeery14/personal-power-system/pull/1) and [PR #2](https://github.com/sdeery14/personal-power-system/pull/2)). New work branches from and targets `main`.

Two branches are retained as history and are not to be deleted or built on:

| Branch | Role |
|---|---|
| `001-battery-box` | Battery Box V1 design and build history, January–March 2026, plus the reconciliation merged in PR #1 |
| `001-v1-as-built` | The reconciliation work itself, as reviewed in PR #1 |
