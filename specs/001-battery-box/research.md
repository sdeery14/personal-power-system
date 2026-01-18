# Research: Battery Box v1

**Purpose**: Document technical research and design decisions for core portable DC power module  
**Created**: 2026-01-18  
**Feature**: [spec.md](spec.md) | [plan.md](plan.md)

## Research Questions Addressed

This document resolves all technical uncertainties identified during planning to enable Phase 1 design with confidence.

---

## 1. Battery Chemistry Selection

### Decision: LiFePO4 (Lithium Iron Phosphate)

**Rationale:**
- **Safety**: Most thermally stable lithium chemistry; will not enter thermal runaway under typical abuse conditions
- **Cycle life**: 2000-5000 cycles to 80% capacity (far exceeds lead-acid's 300-500 cycles)
- **Flat discharge curve**: Maintains ~13.3V for majority of discharge cycle, providing consistent power delivery
- **Temperature tolerance**: Operates safely 0°C to 45°C (discharge), appropriate for camping use
- **Depth of discharge tolerance**: Can safely discharge to 100% DOD without significant degradation

**Alternatives Considered:**
- **Lead-acid (AGM)**: Rejected - heavier (3x weight per Ah), limited cycle life, voltage sag under load, sulfation if stored discharged
- **NMC/NCA lithium**: Rejected - higher energy density but thermal safety concerns, more complex BMS requirements, higher cost
- **LTO (Lithium Titanate)**: Rejected - excellent safety/cycle life but lower voltage (2.4V/cell vs 3.2V/cell) requires more cells, significantly higher cost

**Key Specifications for 12V LiFePO4:**
- Nominal voltage: 12.8V (4 cells × 3.2V)
- Fully charged: 14.4V (4 cells × 3.6V)
- Safe minimum (0% SOC): 10.0V (4 cells × 2.5V)
- Recommended minimum for longevity (20% SOC): ~12.8V (resting voltage)
- Storage voltage: 13.2V - 13.4V (50-60% SOC)

---

## 2. Battery Management System (BMS) Requirements

### Decision: Integrated BMS with 12V LiFePO4 Battery Pack

**Rationale:**
- Most 12V LiFePO4 batteries sold for RV/marine use include integrated BMS
- BMS handles cell balancing, over-voltage protection, under-voltage protection, over-current protection
- Eliminates need for external BMS design and reduces failure points
- Constitution Principle VII (Bounded Complexity): Use manufacturer-integrated protection where available

**BMS Must Provide:**
- **Over-voltage protection**: Disconnect charging at 14.6V (or per manufacturer spec)
- **Under-voltage protection**: Disconnect loads at 10.0V to prevent cell damage
- **Over-current protection**: Disconnect at manufacturer-specified continuous current limit
- **Cell balancing**: Passive or active balancing during charge to equalize cell voltages
- **Temperature monitoring**: Some BMS include temperature cutoff (verify if available)

**Fallback Strategy:**
- If battery does not include integrated BMS, external BMS required (e.g., Daly, JBD, Orion BMS)
- External BMS adds complexity but provides same protections
- Document BMS choice in component specifications (FR-025)

---

## 3. Fusing and Overcurrent Protection

### Decision: Automotive ANL Fuse or Mega Fuse on Main Battery Output

**Rationale:**
- Constitution Principle I (Safety First): Fusing is mandatory, non-negotiable
- ANL/Mega fuses handle high current (30A-300A range), suitable for battery disconnect
- Readily available, low resistance, fast-acting under severe overcurrent
- Individual circuit fusing (e.g., blade fuses) on each output circuit for load-specific protection

**Fusing Strategy:**
- **Main battery fuse**: 50A-100A ANL fuse (based on battery BMS continuous rating and wire gauge)
- **Individual output fuses**: 10A, 15A, 20A, 30A blade or ATO fuses per circuit (125% of expected load)
- **Charge input fuse**: 20A-30A fuse on charging circuit (based on charger output current)

**Wire Gauge for Fuse Protection:**
- 10 AWG: 30A fuse (typical for main distribution)
- 12 AWG: 20A fuse
- 14 AWG: 15A fuse
- 16 AWG: 10A fuse
- All wire rated for at least 105°C (TXL or GXL automotive wire)

**Time-Current Characteristics:**
- Blade/ATO fuses: ~10 seconds at 135% rated current, <1 second at 200% rated current
- ANL fuses: <10 seconds at 150% rated current per manufacturer datasheet
- SC-003 validation: Use manufacturer datasheet as reference

---

## 4. Connector Standards

### Decision: Anderson Powerpole PP45 for Main Output, XT60 Alternative Acceptable

**Rationale:**
- **Anderson Powerpole**: Genderless, polarity-keyed, 45A continuous rating, widely used in amateur radio, RV, emergency power
- **XT60**: 60A continuous rating, compact, anti-spark design, very common in RC/drone community, lower cost
- Both meet Constitution Principle II (Modularity) requirement for standardized connectors
- Both mechanically keyed to prevent reverse polarity

**Connector Selection by Circuit:**
- **Main battery output**: Anderson PP45 or XT60 (document choice in FR-031)
- **Charging input**: Anderson PP30/45 or XT60 to match charger connector
- **Auxiliary outputs**: Cigarette lighter socket (12V accessories), USB-C PD (phone charging if added)
- **Fused blade fuse holders**: Standard automotive ATO/ATC fuse holder with screw terminals

**Non-Standard Connector Documentation (if used):**
- Ring terminals inside enclosure (battery-to-busbar): Document wire gauge, ring terminal size, torque spec
- Barrier strips (if used for distribution): Document terminal block model, wire size, torque
- Per constitution: Any non-standard connector requires rationale and replacement strategy (FR-011)

---

## 5. Voltage Measurement and Monitoring

### Decision: Panel-Mount Digital Voltmeter (0.36" or 0.56" LED Display)

**Rationale:**
- Constitution Principle III (Transparency): Voltage measurement mandatory without disassembly
- Digital panel meters provide ±0.1V accuracy (meets SC-002 requirement)
- Powered directly from battery (low quiescent current ~10-20mA)
- Visible from 2 meters (meets SC-005 requirement)
- Cost-effective (~$5-15 per unit)

**Meter Specifications:**
- Voltage range: 5-30V DC (covers 12V LiFePO4 range 10V-14.6V)
- Accuracy: ±0.1V or better
- Display: Red or blue LED, 0.36" or 0.56" character height
- Quiescent current: <20mA to minimize parasitic drain

**State of Charge (SOC) Estimation (FR-016):**
- **Method**: Voltage-based lookup table for LiFePO4 at rest (no load)
- **Under load**: Voltage drops due to internal resistance; SOC estimation approximate
- **Lookup table** (resting voltage after 10 minutes no load):
  - 14.4V = 100% SOC
  - 13.4V = 90% SOC
  - 13.3V = 70% SOC
  - 13.2V = 40% SOC
  - 13.0V = 20% SOC (low battery warning)
  - 12.8V = 10% SOC
  - <12.0V = Critical, approaching BMS cutoff

**Limitations:**
- Voltage-based SOC is approximate (±10% accuracy)
- Load affects voltage reading (voltage sag under current)
- Temperature affects voltage (higher temp = slightly lower voltage at same SOC)
- More accurate SOC requires coulomb counting (shunt + integrator), deferred to future feature

---

## 6. Temperature Monitoring

### Decision: Adhesive-Backed Thermistor or DS18B20 Digital Sensor

**Rationale:**
- Constitution Principle III: Temperature monitoring mandatory for safety
- Battery thermal management critical to prevent degradation and hazards
- Simple sensor mounted to battery case or inside enclosure near battery

**Sensor Options:**
- **NTC Thermistor (10K @ 25°C)**: Analog, requires voltage divider and ADC or analog meter; simple, low cost
- **DS18B20**: Digital 1-Wire sensor, ±0.5°C accuracy, easy to interface with Raspberry Pi/Arduino; slightly higher cost
- **Thermal indicator sticker**: Passive, irreversible color change at threshold (e.g., 45°C); no power required but no real-time reading

**Implementation Strategy for v1:**
- **Simple approach**: Adhesive thermistor or DS18B20 with digital readout or data logger
- **Minimum viable**: Manual check with infrared thermometer before/after use (document procedure in FR-015)
- **Future enhancement**: Continuous logging to Raspberry Pi with alert threshold

**Temperature Thresholds:**
- Operating range (discharge): 0°C to 45°C per typical LiFePO4 spec
- Operating range (charge): 0°C to 45°C (some batteries require >0°C for charging)
- Warning threshold: 40°C (SC-006 validation target)
- Critical shutdown: 50°C (if automation added in future)

---

## 7. AC Charging Implementation

### Decision: External LiFePO4-Specific AC Charger (Not Integrated)

**Rationale:**
- Constitution Principle IV (Incremental Evolution): Use proven external charger for v1
- Eliminates design complexity and safety risk of building AC-to-DC charger from scratch
- LiFePO4 chargers widely available, UL-listed, match battery chemistry (14.4V bulk, 14.6V absorption, 13.6V float)
- Modularity: Charger can be upgraded independently

**Charger Specifications (FR-022):**
- **Chemistry match**: LiFePO4 profile (14.4V-14.6V charge voltage, not lead-acid 14.7V)
- **Charge current**: 10A minimum for reasonable charge time (100Ah / 10A = 10 hours to 100%)
- **Input**: 120V AC, standard NEMA 5-15 plug
- **Output connector**: Anderson Powerpole, XT60, or barrel jack to match battery box charge input
- **Protection**: Over-voltage, over-current, reverse polarity, short circuit protection (UL/CE listed)

**Recommended Charger Examples:**
- Victron Blue Smart IP65 (12V 10A, LiFePO4 mode, Bluetooth monitoring)
- Renogy 12V 20A DC-DC charger (with AC adapter if needed)
- NOCO Genius (verify LiFePO4 mode availability)
- Document selected charger model in FR-022 and FR-028

**Charging Interface on Battery Box:**
- Input connector: Anderson PP30/45 or XT60
- Inline fuse: 20A-30A (based on charger output current)
- Reverse polarity protection: Schottky diode or MOSFET-based (if not in charger already)
- Status LED: Charging indicator (driven by charger if available, or voltage-sensing circuit)

---

## 8. Status Indicators (Visual Feedback)

### Decision: Three-LED Status System (Power, Low Battery, Charging)

**Rationale:**
- Constitution Principle III (Transparency): Visual indicators required for system state
- SC-005: Must be identifiable from 2 meters in typical lighting
- Simple, no software required, minimal power consumption

**LED Configuration:**
- **Green LED (Power/Ready)**: Lit when voltage >13.0V (system operational)
- **Yellow LED (Low Battery)**: Lit when voltage <13.0V (20% SOC warning)
- **Red LED (Charging)**: Lit when charge voltage detected (>14.0V)

**Implementation:**
- **Power LED**: Voltage comparator or simple transistor circuit with 13.0V threshold
- **Low battery LED**: Voltage comparator with 13.0V threshold (opposite logic of Power LED)
- **Charging LED**: Voltage comparator with 14.0V threshold (detects charger presence)
- **Current limiting resistors**: Sized for 10-20mA per LED, minimize quiescent current
- **LED size**: 10mm or larger for visibility at 2 meters

**Future Enhancement:**
- RGB LED with microcontroller for more granular status (5 SOC levels, fault codes)
- Deferred to future feature per Constitution Principle IV (Incremental Evolution)

---

## 9. Enclosure Selection

### Decision: Weatherproof Plastic Case or Plywood Box with Ventilation

**Rationale:**
- Constitution Principle I (Safety): Enclosure must protect battery and prevent accidental shorts
- FR-023: Thermal management required (ventilation holes or passive cooling)
- SC-008: Must be portable by one person with reasonable effort

**Enclosure Options:**
- **Option A: Weatherproof plastic case** (e.g., Pelican-style, Harbor Freight Apache case)
  - Pros: Durable, water-resistant, handles included, professional appearance
  - Cons: Higher cost ($50-150), may require drilling for connectors/meters
  - Recommended for mobile/camping use (vibration, weather exposure)

- **Option B: Plywood box (1/2" or 3/4" plywood)**
  - Pros: Low cost, easy to customize, adequate protection for stationary use
  - Cons: Heavier, not weather-resistant, less durable
  - Recommended for home/garage backup use, less mobile

**Enclosure Requirements:**
- **Ventilation**: Drill 1" holes with mesh screen (prevent debris entry, allow air circulation)
- **Battery mounting**: Secure with ratchet straps, foam padding, or mounting brackets (FR-025)
- **Component mounting**: Panel-mount voltmeter, fuse holders, connector plates on exterior
- **Cable management**: Strain relief for all external connections
- **Labeling**: Voltage, polarity, current ratings on all terminals (FR-009)

**Portability:**
- 100Ah LiFePO4 battery: ~13kg (29 lbs)
- Enclosure + components: ~2-5kg (4-11 lbs)
- Total weight: 15-18kg (33-40 lbs) - manageable by one person with handles (SC-008)

---

## 10. Testing and Validation Strategy

### Decision: Phased Testing with Documented Results

**Rationale:**
- Constitution Principle V (Documentation): Mistakes and outcomes must be recorded
- SC-003, SC-010: Safety validation critical before operational use

**Test Phases:**

#### Phase 1: Component Bench Testing (Pre-Assembly)
- Verify battery voltage, capacity (discharge test at 10A to cutoff)
- Verify BMS operation (trigger over-voltage, under-voltage protection with adjustable supply)
- Verify fuse interruption (gradually increase current until fuse blows, document time)
- Verify charger operation (charge battery from 50% to 100%, monitor voltage profile)

#### Phase 2: Integration Testing (Post-Assembly)
- Voltage measurement accuracy (compare panel meter to calibrated multimeter across SOC range)
- Temperature monitoring (compare sensor reading to infrared thermometer)
- Status LED operation (verify thresholds: power at 13.0V, low battery at 13.0V, charging at 14.0V)
- Connector continuity (verify polarity, no shorts)

#### Phase 3: Load Testing
- Light load (5A for 1 hour): Monitor voltage sag, temperature rise
- Moderate load (15A for 2 hours): Monitor voltage sag, temperature rise, verify <40°C (SC-006)
- Heavy load (30A for 15 minutes): Verify fuse does not nuisance-trip, verify connector heat dissipation
- Runtime validation (10A until low battery warning): Should achieve 8+ hours with 100Ah battery (SC-001)

#### Phase 4: Protection Validation (Controlled Fault Testing)
- Overcurrent test: Apply 150% fuse rating, verify fuse opens per manufacturer spec (SC-003)
- Reverse polarity test (if applicable): Verify protection prevents damage
- Over-discharge test: Discharge to BMS cutoff, verify BMS opens circuit at 10V
- Charging validation: Charge from 20% to 95% SOC, verify time ~8 hours at 10A (SC-004)

**Documentation:**
- Test results logged in `specs/001-battery-box/docs/test-results.md`
- Include: date, conditions (ambient temp), load used, measurements, pass/fail, observations
- Failures documented with root cause and corrective action per Constitution Principle V

---

## Summary of Research-Driven Design Decisions

| Decision Area | Choice | Rationale |
|---------------|--------|-----------|
| Battery Chemistry | 12V LiFePO4 (100Ah) | Safety, cycle life, flat discharge curve |
| BMS | Integrated with battery pack | Simplicity, reliability, bounded complexity |
| Main Fuse | 50A-100A ANL fuse | High current, fast-acting, safety compliance |
| Circuit Fuses | 10A-30A blade fuses | Load-specific protection, readily available |
| Main Connector | Anderson PP45 or XT60 | Standardized, high current, polarity-keyed |
| Voltage Meter | Digital panel meter (LED) | ±0.1V accuracy, visible at 2m, low cost |
| Temperature Sensor | DS18B20 or thermistor | Simple, accurate, low cost |
| Charger | External LiFePO4 charger | Proven, UL-listed, modular, incremental approach |
| Status LEDs | 3-LED system (power, low, charging) | Simple, no software, meets transparency requirement |
| Enclosure | Weatherproof case or plywood | Portable, protective, allows thermal management |
| Testing Strategy | 4-phase validation | Safety-critical, documented outcomes |

**Ready for Phase 1 Design**: All technical unknowns resolved. Proceeding to data model, component contracts, and quickstart guide generation.
