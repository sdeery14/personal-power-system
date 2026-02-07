# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **hardware documentation project** — not a software codebase. It designs, specifies, and tracks the build of a modular 12V DC portable power system (LiFePO4 battery box) for camping, vehicle use, and backup power. There is no application code, no build system, and no tests to run.

All work product is structured markdown: specifications, plans, research, data models, task lists, and assembly documentation.

## Governing Documents (Read These First)

1. **`.specify/memory/constitution.md`** — The supreme authority. Seven enforceable principles that ALL work must comply with. Safety First (Principle I) always wins conflicts between principles.
2. **`vision.md`** — Project purpose, use cases, non-goals, and design philosophy: "Simple before smart; Measured before automated; Documented before expanded."

## Speckit Framework

The project uses a structured specification workflow managed by agent templates in `.github/agents/` with corresponding prompts in `.github/prompts/`. The workflow is:

1. **Specify** (`speckit.specify`) — Write user stories + functional requirements → `spec.md`
2. **Plan** (`speckit.plan`) — Technical approach with constitution compliance check → `plan.md` + `research.md`
3. **Analyze** (`speckit.analyze`) — Deep technical research → additions to `research.md`
4. **Tasks** (`speckit.tasks`) — Phase-based task breakdown → `tasks.md`
5. **Checklist** (`speckit.checklist`) — Validate specification quality → `checklists/requirements.md`
6. **Implement** (`speckit.implement`) — Guide physical assembly steps

PowerShell automation scripts live in `.specify/scripts/powershell/`:
- `create-new-feature.ps1` — Scaffold a new feature branch with spec templates
- `update-agent-context.ps1` — Regenerate `.github/agents/copilot-instructions.md` from feature plans
- `check-prerequisites.ps1` — Validate environment setup
- `setup-plan.ps1` — Initialize project structure

## Repository Structure

```
specs/<feature-id>/          # One directory per feature (e.g., 001-battery-box)
  spec.md                    # User stories + functional requirements
  plan.md                    # Technical approach + constitution check
  research.md                # Technical deep-dives and decision rationale
  data-model.md              # Entity models, attributes, state machines
  tasks.md                   # Phased task breakdown with progress tracking
  quickstart.md              # Assembly procedures
  contracts/                 # Component interface specifications
  checklists/                # Quality validation checklists
  docs/                      # Supporting docs (component-selection, shopping-list, wiring-diagram, etc.)

.specify/memory/constitution.md   # Project constitution (v1.0.0)
.specify/templates/               # Markdown templates for specs, plans, tasks, checklists
.github/agents/                   # Speckit agent role definitions
.github/prompts/                  # Prompt templates for each agent
```

## Branching Convention

Each feature gets its own branch named `<NNN>-<feature-name>` (e.g., `001-battery-box`). The main branch is `main`.

## Commit Message Convention

Commits use a prefix style: `docs(001):`, `feat(001):`, `progress(001):` where the number references the feature ID.

## Key Constraints When Contributing

- **Every design decision must be documented** with problem statement, rationale, alternatives considered, and implementation details (Constitution Principle V).
- **Safety is non-negotiable** — all connections rated for expected current + 25% margin, all circuits fused, fail-safe design required (Principle I).
- **No feature without a use case** — features without identified practical problems must not be implemented (Principle VI).
- **Incremental only** — one feature at a time, manual before automation, baseline data before optimization (Principle IV).
- **Standardized connectors** — Anderson Powerpole for DC distribution, XT60/XT90 for high-current battery connections, USB-C PD for loads. Non-standard connectors require documented rationale (Principle II).

## Current State (001-battery-box)

The first feature is a portable 12V battery box built around a VEVOR 200Ah LiFePO4 battery in a Greenmade 27gal tote. Key components: Blue Sea 5026 fuse block, Victron BMV-712 monitor, Nilight 4-in-1 panel, 100A ANL main fuse. Full component details are in `specs/001-battery-box/data-model.md` and `specs/001-battery-box/docs/shopping-list.md`. Task progress is tracked in `specs/001-battery-box/tasks.md`.
