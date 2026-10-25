# Personal Power System

A long-term, modular project to build, understand, and evolve a self-managed 12 V DC power platform for camping, vehicle use, and portable backup. See [vision.md](vision.md) for purpose and philosophy and [.specify/memory/constitution.md](.specify/memory/constitution.md) for the governing principles. Safety First is the first principle and overrides everything else.

## Project status (2026-10-25)

**Battery Box V1 is a working bench prototype. It is not ready for transport or deployment.**

- The system powered on for the first time on 2026-03-07. The Victron monitor and Nilight accessory panel have been observed operating.
- Electrical connections are exposed, there is no enclosure, no master disconnect, and the assembly is held together only by two cam-buckle straps.
- No polarity, continuity, voltage-drop, load, thermal, or charging validation records exist. Undocumented checks are not counted as passed.
- The charging path is undefined. Connector-to-fuse mapping has not been traced.

The full list of open safety concerns and the verification backlog is in [verification-and-safety.md](specs/001-battery-box/verification-and-safety.md).

## Authoritative documentation

For any question about the hardware as it exists today, use these two files and nothing else:

| Document | Purpose |
|---|---|
| [specs/001-battery-box/as-built.md](specs/001-battery-box/as-built.md) | Canonical description of the V1 hardware: power path, fuse positions, branches, component inventory, mechanical configuration, and deviations from the design. Every claim carries an evidence tag. |
| [specs/001-battery-box/verification-and-safety.md](specs/001-battery-box/verification-and-safety.md) | Open safety concerns, verification backlog, the historical measurements on record, and the list of withdrawn procedures. |

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
.specify/, .github/, .claude/     SpecKit tooling retained from the original methodology (historical)
```

## Branches

`main` holds the project framework. Battery Box V1 documentation lives on `001-battery-box` and is being reconciled on `001-v1-as-built`; integration into `main` follows review.
