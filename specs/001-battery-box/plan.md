# Implementation Plan: Battery Box v1

**Branch**: `001-battery-box` | **Date**: 2026-01-18 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-battery-box/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a portable 12V DC power module (battery box) that safely delivers power to camping and mobile loads (diesel heater, refrigerator, electronics) with built-in monitoring and AC charging capability. The design prioritizes safety (fusing, thermal management, proper connectors), observability (voltage/temperature measurement, status indicators), and modularity (standardized interfaces for future expansion). This is v1 - establishing the core power delivery foundation before adding advanced charging sources (solar, alternator) or automation.

## Technical Context

**Language/Version**: N/A (hardware/physical implementation with Victron VictronConnect app for BMV-712 monitoring)  
**Primary Dependencies**: 
- Battery: VEVOR 200Ah 12V LiFePO4 with integrated BMS (100A continuous discharge)
- Charger: VEVOR 20A LiFePO4 charger (14.6V absorption voltage)
- Fuse block: Blue Sea Systems 5026 (12 circuits, 100A busbar, marine-grade)
- Battery monitor: Victron BMV-712 Smart with 500A shunt (Bluetooth, coulomb counting)
- Connectors: Anderson Powerpole-compatible PP45 (45A, genderless, polarized)
- Panel: Nilight 4-in-1 (USB-C PD, USB-A QC 3.0, 12V outlet, integrated voltmeter, ON/OFF switch)
- Enclosure: Greenmade 27gal storage tote (30.4"×20.4"×14.7")

**Storage**: Physical documentation (wiring diagrams, component specs, operating procedures) stored in `specs/001-battery-box/docs/`; Victron BMV-712 historical data logged via VictronConnect app (Bluetooth)  
**Testing**: Physical integration testing (6-phase protocol: pre-power checks, initial power-up, load testing 5A→30A, charging validation, runtime validation, results documentation); no automated unit tests for hardware  
**Target Platform**: Portable enclosure for camping/vehicle use; AC charging from 120V mains via VEVOR 20A charger; DC output for 12V loads (diesel heater 3-8A, fridge 5-10A, USB devices, accessories)  
**Project Type**: Physical hardware build (not software) - documentation-driven with assembly/wiring procedures  
**Performance Goals**: 
- Runtime: 40+ hours diesel heater at 5A average (200Ah capacity)
- Voltage regulation: 10.0V-14.6V (LiFePO4 BMS limits)
- Charging: 20%-95% SOC (150Ah) in ~7.5 hours at 20A charge rate
- Monitoring accuracy: SOC ±1%, voltage ±0.1V (Victron BMV-712 specifications)
- Temperature: Battery surface <40°C under 30A continuous load

**Constraints**: 
- All components within manufacturer ratings (100A BMS, 45A connectors, 20A circuits)
- Blue Sea 5026 fusing: 6 circuits allocated (charge 30A, heater 10A, fridge 15A, USB panel 20A, 2× spare 15-20A)
- 100A ANL main fuse matches battery BMS rating
- Thermal management via ventilation (4× 25-30mm holes with mesh)
- Portable: One person, ~28-30kg total weight (battery 25kg + components/enclosure 3-5kg)
- Reversible assembly: No permanent modifications to purchased components

**Scale/Scope**: Single battery box unit; 3 user stories (power delivery P1, monitoring P2, charging P3); 6 fused circuits with 6 spare for future expansion (solar, inverter, lighting); focus on manual operation and safety validation before future automation

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Principle I: Safety First (NON-NEGOTIABLE)
✅ **PASS** - Specification includes:
- FR-005 to FR-009: Fusing, short circuit protection, safe failure modes, enclosure protection, terminal labeling
- SC-003: Fuse interruption validation with no damage
- SC-010: Zero safety incidents requirement
- Edge cases address: deep discharge, overcurrent, temperature extremes, reverse polarity

### Principle II: Modularity
✅ **PASS** - Specification includes:
- FR-010 to FR-012: Standardized connectors (Anderson Powerpole, XT60) with documentation requirement for non-standard choices
- FR-013: Reverse polarity protection on charging interface
- Battery, enclosure, output circuit, charging circuit, monitoring system all documented as replaceable entities

### Principle III: Transparency & Observability
✅ **PASS** - Specification includes:
- FR-014 to FR-017: Voltage measurement, temperature measurement, SOC estimation, visual status indicators
- SC-002: Voltage accuracy within ±0.1V
- SC-005: Status identification from 2 meters
- All monitoring without disassembly required

### Principle IV: Incremental Evolution
✅ **PASS** - v1 scope appropriately bounded:
- AC charging only (solar and alternator deferred)
- Manual operation only (automation deferred)
- Basic monitoring (advanced logging/analytics deferred)
- Single battery configuration (expansion deferred)

### Principle V: Documentation & Learning
✅ **PASS** - Specification includes:
- FR-025 to FR-031: Battery specs, discharge limits, charger specs, fuse ratings, wiring diagram, operating instructions all mandatory
- Documentation stored in `specs/001-battery-box/docs/`
- Success criteria include documentation completeness (SC-007)

### Principle VI: Practical Utility
✅ **PASS** - Solves real problems:
- P1: Power delivery for diesel heater, refrigerator (winter camping, summer cooling)
- P2: State monitoring prevents unexpected shutdowns
- P3: AC charging enables battery maintenance between trips
- No feature-for-feature's-sake additions

### Principle VII: Bounded Complexity
✅ **PASS** - Design constrained:
- All components within manufacturer ratings (FR-001, constraints documented)
- Simple manual operation (no automation in v1)
- Measured approach (monitoring before optimization)
- Complexity justified by safety requirements only

**GATE RESULT: ✅ ALL CHECKS PASS - Proceeding to Phase 0 Research**

No violations to justify. All seven principles satisfied by specification.

## Project Structure

### Documentation (this feature)

```text
specs/001-battery-box/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
│   └── component-interfaces.md
├── docs/                # Implementation artifacts
│   ├── component-selection.md    # ✅ Created: Component decisions with procurement details
│   ├── shopping-list.md           # ✅ Created: Consolidated procurement with budget tracking
│   ├── wiring-diagram.md (or .pdf/.png)
│   ├── assembly-procedure.md
│   ├── operating-instructions.md
│   └── test-results.md
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Physical Implementation (not in repository - documentation only)

This is a hardware build, not a software project. The repository contains:
- Documentation of design decisions
- Component specifications and datasheets (links or local copies)
- Wiring diagrams and assembly procedures
- Test procedures and validation results
- Operating instructions and safety guidelines

The actual physical implementation consists of:
- Enclosure with mounted battery
- Wiring harness with fused output circuits
- Monitoring instrumentation (voltmeter, temperature sensor, status LEDs)
- Charging interface with reverse polarity protection
- Load output terminals with appropriate connectors

**Structure Decision**: Documentation-driven hardware project. All technical information stored in `specs/001-battery-box/docs/` directory. No source code directory structure needed for v1 (future monitoring software will be separate feature).
