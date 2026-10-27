# CLAUDE.md

Guidance for Claude Code and other AI agents working in this repository.

## Project overview

This is a **hardware documentation project**, not a software codebase. It records the design, build, and evolution of a modular 12 V DC portable power system (currently Battery Box V1, a LiFePO4 battery box). There is no application code, build system, or test suite. All work product is markdown.

## Governing documents (read first)

1. **`.specify/memory/constitution.md`** — Seven principles that all work must satisfy. Safety First (Principle I) always wins.
2. **`vision.md`** — Purpose, use cases, non-goals, and philosophy: "Simple before smart; Measured before automated; Documented before expanded."

## Document authority

- **`specs/001-battery-box/as-built.md`** is the only authoritative description of the hardware as it exists. **`specs/001-battery-box/verification-and-safety.md`** is the only authoritative record of what has been verified and what safety concerns are open.
- **`specs/001-battery-box/reconciliation-2026-10-25.md`** (R-2026-10-25) records where the snapshot's User-reported and Visually observed claims came from and what no reviewer inspected. Cite it, rather than the photographs, for provenance.
- **`specs/002-diesel-heater/`** (`spec.md`, `design.md`, `bom.md`) is a **specification in progress** for a subsystem that has not been built or purchased. Its figures are Manufacturer-stated, User-reported, Owner decision, Proposed, or Unknown as tagged; no cut length, fastener, or load path is approved; the gates in `spec.md §10` are closed. Do not record anything there as built, measured, or verified without a dated record.
- Every other file under `specs/001-battery-box/` is a **historical design document**. It describes the design as planned in Jan–Mar 2026, carries a status notice, and must not be read as a description of the current hardware or as an operating manual. Where it conflicts with the as-built documents, the as-built documents govern.
- `tasks.md` contains the dated build log and lessons learned. That log is the primary historical record and must be preserved as written.

## Working method: AI Development Playbook v1.1 (summary)

Roles:

- **ChatGPT** — planning coordinator, requirements analysis, implementation review.
- **Claude Code** — repository implementation: branches, commits, pull request preparation.
- **Codex** — independent, read-only review of consequential changes.
- **Project owner** — physical verification and final approval. Only the owner can confirm anything about the physical system.

Rules:

- Start each piece of work with a read-only assessment and a proposed plan. Do not create branches, edit files, commit, push, or open pull requests until the plan is approved. Do not merge pull requests without explicit approval.
- Keep scope to what was approved. Documentation changes are documentation-only: no hardware design decisions, fuse or wire sizing, component selection, or charging recommendations unless explicitly authorized.
- Prefer small, focused commits with the existing prefix style (`docs(001):`, `feat(001):`, `progress(001):`).
- Preserve history. Mark obsolete or unsafe material as withdrawn or historical with a notice at the location; do not delete it.
- Request independent review for changes that affect safety statements, the as-built record, or agent guidance.

## Evidence requirements

Every hardware claim carries one of these tags:

| Tag | Meaning |
|---|---|
| **Historical/documented** | Recorded in the repository during the build |
| **User-reported** | Stated by the owner, not independently checked |
| **Visually observed** | Seen in the owner's photographs (cite the source and date) |
| **Measured** | A dated numeric reading with method or instrument recorded |
| **Verified** | Independently confirmed after the fact, with a dated record |
| **Unknown/proposed** | No evidence, conflicting evidence, or inference |

- Never record a test as passed, a component as compliant, or a value as measured without a dated record stating who, how, and what. A ticked checkbox is not evidence. An owner's recollection of a check is User-reported, not Verified.
- Never infer the current hardware from design documents. Where design and build diverge, record the deviation in `as-built.md §7`.
- Do not present inferred circuit mappings or connector assignments as verified.
- Do not write that an undocumented activity never happened. Say what the record shows: *documented absence* (no record), *owner-confirmed absence* (the owner stated it, with the date), or *unknown status*.
- Do not write energized test procedures or prescribe electrical modifications without engineering review and owner approval.

## Safety constraints on documentation

- The V1 prototype is not ready for transport or deployment. Do not write anything that implies otherwise.
- Do not recommend using the main ANL fuse as an on/off or emergency switch.
- Do not reintroduce withdrawn procedures (destructive fuse tests, the Sanuke crimping method, the LED-based operating instructions). The list is in `verification-and-safety.md §5`.
- Matching fuse and connector ratings are recorded as needing engineering review, not as proven violations.

## Repository structure

```text
specs/001-battery-box/
  as-built.md                    Authoritative hardware description
  verification-and-safety.md     Authoritative verification and safety status
  reconciliation-2026-10-25.md   Provenance record for the 2026-10-25 snapshot (R-2026-10-25)
  spec.md, plan.md, research.md, data-model.md, quickstart.md,
  contracts/, checklists/, docs/ Historical design documents (Jan–Mar 2026)
  tasks.md                       Historical task list; build log and lessons learned

specs/002-diesel-heater/
  spec.md                        Requirements, manufacturer constraints, gates (nothing built)
  design.md                      Preliminary frame concept, hazard register, open decisions
  bom.md                         Owned equipment; procurement categories, not purchase-ready

.specify/memory/constitution.md  Governing principles
.specify/, .github/agents/, .github/prompts/, .claude/commands/
                                 SpecKit tooling from the original methodology. Retained as history;
                                 not the active workflow. Do not run its scripts or prompts to create
                                 new specs unless asked.
```

## Git conventions

- `main` is the baseline. New work branches from the current `origin/main`, and pull requests target `main`.
- Work branches are named `<NNN>-<topic>` (e.g. `001-post-integration-cleanup`). `001` is Battery Box V1; the next numbered system or major piece of work takes the next number.
- `001-battery-box` and `001-v1-as-built` are retained historical branches (Battery Box V1 design, build, and reconciliation through 2026-10-25). Do not delete them, branch from them, or target them with pull requests.
