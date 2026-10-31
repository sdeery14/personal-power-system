# CLAUDE.md

Guidance for Claude Code and other AI agents working in this repository.

## Project overview

This is a **hardware documentation project**, not a software codebase. It records the design, build, and evolution of a modular 12 V DC portable power system (currently Battery Box V1, a LiFePO4 battery box). There is no application code. The work product is markdown, plus one small parametric CAD model (Python, CadQuery, with its own tests) under `specs/002-diesel-heater/cad/` that draws preliminary pictures from the specification and is subject to the same evidence rules.

## Governing documents (read first)

1. **`.specify/memory/constitution.md`** — Seven principles that all work must satisfy. Safety First (Principle I) always wins.
2. **`vision.md`** — Purpose, use cases, non-goals, and philosophy: "Simple before smart; Measured before automated; Documented before expanded."

## Document authority

- **`specs/001-battery-box/as-built.md`** is the only authoritative description of the hardware as it exists. **`specs/001-battery-box/verification-and-safety.md`** is the only authoritative record of what has been verified and what safety concerns are open.
- **`specs/001-battery-box/reconciliation-2026-10-25.md`** (R-2026-10-25) records where the snapshot's User-reported and Visually observed claims came from and what no reviewer inspected. Cite it, rather than the photographs, for provenance.
- **`specs/002-diesel-heater/decision-and-order-2026-10-31.md`** is the **current authoritative direction/order record** for Module 002. The owner reports ordering a **Hcalory TB2S+ 6 L Wireless Remote Upgraded** enclosed heater on 2026-10-31, not its receipt or commissioning. The prior VEVOR 2 kW XMZ-D2 split heater is retained for future use; the **TNUTZ frame has not been purchased**, and the aluminum-frame route is **paused**. `spec.md`, `design.md`, `bom.md` and historical shopping lists remain **historical/paused VEVOR frame documents**, not instructions for the purchased Hcalory. All G1-P/G2-D/G1–G5 frame gates remain **closed**; no frame hardware order, assembly or fuel/power/transport/operation is authorized by these records. Do not treat this order as a Battery Box load-connection approval. Hardware evidence rules remain in effect.
- **`specs/002-diesel-heater/cad/`** is a **paused historical** parametric placeholder model of the VEVOR frame concept, marked PRELIMINARY — NOT FOR FABRICATION or ordering. Its parameters carry evidence tags; its outputs are preliminary pictures and schedules rather than safety-approved fabrication drawings. The **historical proposed exception (not presently active)** was an explicitly owner-approved G1-P order of the fixed 18 nominal TNUTZ cut lengths at the owner's accepted nonreturnable financial/fit risk; it does not approve structural assembly or loaded use. A modelled gap is a bounding-box distance, not a clearance. **`specs/002-diesel-heater/measurements/`** holds the measurement workflow and the dated measurement records for the owned heater equipment. A value becomes Measured only through a record there; the records verify nothing, establish no clearance, and open no gate. Do not pre-fill a record, promote an earlier tape figure to Measured without a record, or read geometric fit as evidence of thermal, fire, exhaust, structural, or electrical safety.
- Every other file under `specs/001-battery-box/` is a **historical design document**. It describes the design as planned in Jan–Mar 2026, carries a status notice, and must not be read as a description of the current hardware or as an operating manual. Where it conflicts with the as-built documents, the as-built documents govern.
- `tasks.md` contains the dated build log and lessons learned. That log is the primary historical record and must be preserved as written.

## Working method: AI Development Playbook v1.2 (summary)

Roles:

- **ChatGPT** — planning coordinator, requirements analysis, implementation review.
- **Claude Code** — repository implementation: branches, commits, pull request preparation.
- **Codex** — independent, read-only review of consequential changes.
- **Project owner** — physical verification and final approval. Only the owner can confirm anything about the physical system.

Rules:

- Start each piece of work with a read-only assessment and a proposed plan. Do not create branches, edit files, commit, push, or open pull requests until the plan is approved. Do not merge pull requests without explicit approval. For Module 002, even an approved documentation/merge decision is **not** approval to purchase the precise TNUTZ cart (G1-P) or conduct a cold assembly (G2-D); those require their own dated owner permissions.
- Keep scope to what was approved. Documentation changes are documentation-only: no hardware design decisions, fuse or wire sizing, component selection, or charging recommendations unless explicitly authorized.
- Prefer small, focused commits with the existing prefix style (`docs(001):`, `feat(001):`, `progress(001):`).
- Preserve history. Mark obsolete or unsafe material as withdrawn or historical with a notice at the location; do not delete it.
- Request independent review for changes that affect safety statements, the as-built record, or agent guidance. The proposed G1-P/G2-D split changes safety-gate wording and therefore needs independent review.

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
  decision-and-order-2026-10-31.md Current Hcalory selection and owner-reported order
  spec.md                        Historical VEVOR frame requirements and closed gates (no frame built)
  design.md                      Preliminary frame concept, hazard register, open decisions
  bom.md                         Owned equipment; procurement categories, not purchase-ready
  cad/                           Parametric placeholder model (Python, CadQuery): params, model, build,
                                 tests, committed previews. PRELIMINARY — NOT FOR FABRICATION
  measurements/                  Measurement workflow, datum conventions, identifier checklist,
                                 record template, and dated measurement records (none yet)

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
