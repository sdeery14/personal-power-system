<!--
SYNC IMPACT REPORT
==================
Version Change: Template → 1.0.0
Change Type: INITIAL RATIFICATION

Modifications:
- PROJECT_NAME: Personal Power System
- Derived 7 enforceable principles from vision.md
- Added Safety Compliance, Design Evolution, and Governance sections
- All placeholders resolved with concrete, measurable rules

Template Consistency:
✅ plan-template.md: Constitution check section compatible with principle structure
✅ spec-template.md: User scenarios align with practical utility principle
✅ tasks-template.md: Phase structure supports incremental evolution principle
✅ No agent-specific references found requiring updates

Follow-up Actions:
- None: All placeholders resolved, no deferred items
-->

# Personal Power System Constitution

## Core Principles

### I. Safety First (NON-NEGOTIABLE)

Electrical protection (fusing, isolation, monitoring) MUST be present in every design.

The system MUST fail safely:
- Short circuits MUST trigger protection before thermal damage
- Overcurrent conditions MUST be detected and interrupted
- All charging sources MUST include reverse polarity protection
- Ground fault paths MUST be eliminated or monitored

No design MAY introduce risk to people, vehicles, or buildings:
- All connections MUST be rated for expected current plus 25% margin
- Enclosures containing batteries MUST allow thermal management
- AC integration MUST remain isolated; grid backfeeding is PROHIBITED
- Any modification affecting safety MUST be reviewed before implementation

**Rationale**: Electrical systems can cause fire, injury, and property damage. Safety constraints are non-negotiable and take precedence over convenience, cost, or performance.

### II. Modularity

Every major component (battery, charger, inverter, load, controller, enclosure) MUST be independently replaceable without redesigning the entire system.

Interfaces between components MUST use standardized connectors:
- Anderson Powerpole (15A, 30A, 45A) for DC power distribution
- XT60/XT90 for high-current battery connections where appropriate
- USB-C PD, cigarette lighter, or standard AC outlets for loads
- Clear labeling (voltage, polarity, max current) at every interface point

New components MUST document:
- Electrical specifications (voltage range, current rating, power consumption)
- Physical constraints (dimensions, weight, thermal requirements)
- Compatibility requirements with existing components

**Rationale**: Technology evolves, components fail, and requirements change. Modularity prevents vendor lock-in and avoids expensive system-wide rebuilds when upgrading a single component.

### III. Transparency & Observability

Power usage, battery state, and system health MUST be measurable, not estimated.

All monitoring systems MUST log:
- Battery voltage (per-cell if multi-cell packs)
- Current draw (loads) and current input (charging sources)
- Temperature at critical points (battery enclosure, power electronics)
- State transitions (charging started/stopped, load connected/disconnected)

Data MUST be:
- Time-stamped with sufficient precision (minimum 1-second resolution)
- Retained for analysis (minimum 30 days of historical data)
- Accessible without specialized tools (CSV export, local dashboard, or API)

Any automation or control logic MUST be observable:
- Decision criteria MUST be logged before actions are taken
- Manual override MUST be available for any automated behavior
- Failure modes MUST be detectable and logged

**Rationale**: Guesswork leads to dead batteries, damaged equipment, and unsafe conditions. Observability enables debugging, optimization, and continuous learning.

### IV. Incremental Evolution

Features and capabilities MUST be added one at a time.

Before implementing a new feature:
- Current functionality MUST be tested and working
- New feature MUST be specified with clear success criteria
- Safety implications MUST be documented

Early versions MUST prioritize:
- Simplicity over sophistication
- Reliability over features
- Manual operation over automation

Advanced capabilities (automation, optimization, prediction) MAY be added only after:
- Manual workflows are understood and documented
- Baseline data has been collected (minimum 10 operational cycles)
- Safety constraints have been verified under load

**Rationale**: Complex systems built all at once are difficult to debug, test, and trust. Incremental evolution reduces risk, enables validation at each step, and builds institutional knowledge.

### V. Documentation & Learning

All design decisions MUST be documented with:
- Problem statement: what issue is being solved
- Rationale: why this approach was chosen
- Alternatives considered: what was rejected and why
- Implementation details: wiring, configuration, software

Experiments and modifications MUST be recorded:
- Date and system state before modification
- Expected outcome and actual outcome
- Measured data supporting conclusions
- Follow-up actions or changes required

Mistakes and failures MUST be documented:
- What happened (sequence of events)
- Root cause (why it happened)
- Corrective action (what changed)
- Prevention (how to avoid recurrence)

Every component specification MUST be referenced:
- Manufacturer part number or model
- Datasheet location (URL or local path)
- Rated specifications used in design calculations

**Rationale**: Learning requires memory. Undocumented systems cannot be debugged, improved, or safely modified. Documentation transforms individual projects into institutional knowledge.

### VI. Practical Utility

Every feature MUST solve a real, defined problem:
- "Stay warm while winter camping" (diesel heater operation)
- "Keep food cold in summer" (refrigerator operation)
- "Power personal electronics" (phone/laptop charging)
- "Provide limited backup power" (inverter for essential AC loads)

Features without identified use cases MUST NOT be implemented.

Convenience features MAY be added only if they:
- Do not compromise safety (Principle I)
- Are fully observable (Principle III)
- Have been manually validated first (Principle IV)

Compute workloads are treated as electrical loads:
- Power consumption MUST be measured and bounded
- Thermal output MUST be managed within enclosure limits
- Work MUST be interruptible for safety or energy management
- Compute loads MUST NOT interfere with primary use cases (heating, cooling, charging)

**Rationale**: Feature creep and over-engineering lead to complexity, cost, and maintenance burden. Every capability must justify its existence by solving a practical problem.

### VII. Bounded Complexity

All designs MUST operate within manufacturer ratings and documented electrical standards.

Design simplicity MUST be prioritized:
- **Simple before smart**: Manual switches before automation
- **Measured before automated**: Baseline data before optimization logic
- **Documented before expanded**: Current state recorded before new features

Any complexity MUST be justified:
- Why is the simpler approach insufficient?
- What problem does this complexity solve?
- Can it be decomposed into simpler incremental steps?

Compute workloads as loads MUST respect:
- Thermal constraints (battery and enclosure temperatures)
- Electrical constraints (voltage limits, current limits, discharge rates)
- Safety constraints (graceful shutdown, fault detection)
- Energy budgets (discharge to no less than battery safe minimum SOC)

Automation MUST NOT obscure system state:
- Current operating mode MUST be observable
- Manual override MUST be available
- Automation decisions MUST be logged

**Rationale**: Complexity is a liability. Systems that cannot be explained simply are difficult to debug, extend, and trust. Bounded complexity ensures maintainability and safety.

## Safety Compliance

All electrical work MUST adhere to:
- Component manufacturer ratings (voltage, current, temperature)
- Industry standards for wiring (AWG sizing for current + temperature)
- National Electrical Code (NEC) where applicable to mobile/portable DC systems

This project explicitly does NOT:
- Permanently modify household electrical systems
- Backfeed power into the grid
- Replace licensed electrical work
- Violate local codes or regulations

All AC/grid interaction MUST:
- Use isolated, UL-listed inverters or chargers
- Be reversible without permanent modifications
- Be clearly documented in terms of grid isolation

## Design Evolution

This repository represents a living system subject to change:
- Hardware will be replaced or upgraded
- Software will evolve with new capabilities
- Requirements will shift based on use case experience

The guiding principle is **intentional evolution**, not perfection.

Changes MUST:
- Be backward compatible where possible (modular interfaces)
- Preserve safety constraints (Principle I always applies)
- Be documented (Principle V applies to all modifications)

Future versions MAY include:
- Improved energy storage (higher capacity, better chemistry)
- Expanded renewable inputs (more solar, vehicle alternator optimization)
- Smarter load management (prioritization, scheduling, automation)
- Better observability (real-time dashboards, predictive analytics)
- Safer, more refined enclosures (better thermal, improved accessibility)

Each version MUST leave the system better understood than before.

## Governance

**Authority**: This constitution supersedes all other practices, preferences, or conventions unless explicitly stated otherwise. All project decisions MUST align with the Core Principles.

**Amendment Process**:
- Amendments MUST document which principle(s) are being modified
- Rationale for change MUST be provided with supporting evidence
- Affected templates, docs, and code MUST be updated for consistency
- Version MUST be incremented according to semantic versioning:
  - **MAJOR**: Backward-incompatible principle removal or fundamental redefinition
  - **MINOR**: New principle added or material expansion of guidance
  - **PATCH**: Clarifications, wording improvements, typo fixes

**Compliance Verification**:
- All design proposals MUST reference applicable principles
- All specifications MUST include constitution compliance check
- All modifications MUST be validated against safety principles
- Violations MUST be justified with documented reasoning

**Conflict Resolution**:
- When principles conflict, **Safety First (Principle I)** ALWAYS takes precedence
- When in doubt, choose the simpler, more observable, more documented approach
- Complexity must be justified; simplicity does not require justification

**Living Document**:
- This constitution applies to the current system state and future evolution
- Retrospective application is not required (existing systems are grandfathered)
- New work MUST comply; legacy work SHOULD be updated when modified

**Version**: 1.0.0 | **Ratified**: 2026-01-18 | **Last Amended**: 2026-01-18
