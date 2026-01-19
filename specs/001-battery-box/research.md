# Research: Battery Box v1

**Purpose**: Document technical research and design decisions for core portable DC power module  
**Created**: 2026-01-18  
**Feature**: [spec.md](spec.md) | [plan.md](plan.md)

## Research Questions Addressed

This document resolves all technical uncertainties identified during planning to enable Phase 1 design with confidence.

---

## 1. Battery Chemistry Selection

### Decision: LiFePO4 (Lithium Iron Phosphate) - VEVOR 200Ah 12V

**Selected Product**: VEVOR 200Ah 12V Deep Cycle LiFePO4 Battery  
**Model**: 010230251465  
**Key Specifications**:
- Capacity: 200Ah (2560Wh @ 12.8V nominal)
- Continuous discharge: 100A (1280W)
- Integrated BMS with OVP/UVP/OCP/SCP/temperature protection
- Dimensions: 520mm × 238mm × 218mm (20.5" × 9.4" × 8.6")
- Weight: ~25kg (55 lbs)
- Purchased: 2026-01-18 from VEVOR.com (~$450-550)

**Rationale:**
- **Safety**: Most thermally stable lithium chemistry; will not enter thermal runaway under typical abuse conditions
- **Cycle life**: 2000-5000 cycles to 80% capacity (far exceeds lead-acid's 300-500 cycles)
- **Flat discharge curve**: Maintains ~13.3V for majority of discharge cycle, providing consistent power delivery
- **Temperature tolerance**: Operates safely 0°C to 45°C (discharge), appropriate for camping use
- **Depth of discharge tolerance**: Can safely discharge to 100% DOD without significant degradation
- **Capacity for multi-day use**: 200Ah provides 40+ hours diesel heater runtime (5A average), enabling 2-3 nights winter camping without recharge

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

### Decision: Integrated BMS with VEVOR 200Ah Battery

**BMS Specifications** (VEVOR integrated):
- **Continuous discharge limit**: 100A
- **Over-voltage protection (OVP)**: ~14.6-14.8V disconnect
- **Under-voltage protection (UVP)**: ~10.0V disconnect
- **Over-current protection (OCP)**: 100A continuous limit
- **Short-circuit protection (SCP)**: Instant disconnect
- **Temperature protection**: Built-in (cutoff thresholds per manufacturer spec)
- **Cell balancing**: Integrated (4-cell pack balancing during charge)

**Rationale:**
- Most 12V LiFePO4 batteries sold for RV/marine use include integrated BMS
- BMS handles cell balancing, over-voltage protection, under-voltage protection, over-current protection
- Eliminates need for external BMS design and reduces failure points
- Constitution Principle VII (Bounded Complexity): Use manufacturer-integrated protection where available

**Protection Architecture**:
- BMS provides first line of defense (cell-level protection)
- 100A ANL main fuse provides second line (wire/connection protection)
- Individual circuit fuses provide third line (load-specific protection)
- Multi-layer protection aligns with Constitution Principle I (Safety First)

---

## 3. Fusing and Overcurrent Protection

### Decision: 100A ANL Main Fuse + Blue Sea 5026 Fuse Block

**Selected Components**:
- **Main fuse**: 100A ANL fuse (matches VEVOR 100A BMS rating)
- **Fuse block**: Blue Sea Systems 5026 (12 circuits, 100A busbar, marine-grade)
- **Circuit fuses**: ST blade (ATO/ATC) - 10A, 15A, 20A, 30A per circuit

**Circuit Allocation** (6 circuits allocated, 6 spare for future):
1. Charge input: 30A (VEVOR 20A charger with margin)
2. Diesel heater: 10A (3-8A typical load)
3. Fridge/cooler: 15A (5-10A typical load)
4. Nilight USB panel: 20A (USB-C PD + USB-A + 12V outlet)
5. Spare output #1: 20A (future inverter/high-power)
6. Spare output #2: 15A (future device)
7-12. Open for expansion (solar, lights, accessories)

**Rationale:**
- Constitution Principle I (Safety First): Fusing is mandatory, non-negotiable
- ANL fuse: 100A matches BMS, handles high current, readily available, low resistance
- Blue Sea 5026: Centralized fuse management, marine-grade quality, common ground bus, professional appearance
- Individual circuit fusing: Load-specific protection, easy troubleshooting
- 6 spare circuits: Supports future expansion (Constitution Principle IV)

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

### Decision: Anderson Powerpole-Compatible PP45 for High-Power, Nilight Panel for Convenience

**Selected Products**:
- **High-power outputs**: Anderson Powerpole-compatible PP45 (45A, genderless, polarized)
  * Amazon: 45A Quick Connect Battery Connector (10 pairs, AWG10-12 compatible)
  * Quantity: 10 bonded red+black pairs (5 circuits × 2 ends)
  * Crimping: Knoweasy Powerpole crimper ($30-50, PP15/30/45 compatible)
- **Convenience panel**: Nilight 4-in-1 (USB-C PD, USB-A QC 3.0, 12V outlet, integrated voltmeter)

**Connector Allocation**:
1. Charge input: 1× PP45 (connects to VEVOR charger via adapter cable)
2. Diesel heater output: 1× PP45 (10A circuit)
3. Fridge/cooler output: 1× PP45 (15A circuit)
4. Spare outputs: 2× PP45 (20A and 15A circuits)
5. USB/12V panel: Nilight 4-in-1 (20A circuit, hardwired to fuse block)

**Rationale:**
- **Anderson Powerpole**: Genderless, polarity-keyed, 45A continuous rating, widely used in amateur radio, RV, emergency power
- **Nilight panel**: Integrated solution (USB-C PD + USB-A + 12V + voltmeter + ON/OFF switch) eliminates separate components
- Both meet Constitution Principle II (Modularity) requirement for standardized connectors
- Powerpole mechanically keyed to prevent reverse polarity
- Nilight ON/OFF switch prevents parasitic drain during storage

---

## 5. Voltage Measurement and Monitoring

### Decision: Dual Monitoring - Victron BMV-712 (Professional) + Nilight Panel (Quick Check)

**Selected Products**:
- **Primary monitor**: Victron BMV-712 Smart Battery Monitor with 500A shunt
  * Coulomb counting for accurate SOC (±1% after calibration)
  * Bluetooth monitoring via VictronConnect app
  * Runtime predictions, historical data, configurable alarms
  * Price: $200-250
- **Secondary display**: Nilight 4-in-1 panel integrated voltmeter
  * LED voltmeter (blue illumination, ±0.1-0.2V typical)
  * Quick visual check without phone/app
  * Backup if Bluetooth unavailable

**Rationale:**
- Constitution Principle III (Transparency): Voltage measurement mandatory without disassembly
- **LiFePO4 flat discharge curve problem**: Voltage stays ~13.2V from 80% SOC down to 30% SOC - can't estimate remaining capacity from voltage alone
- **Victron BMV-712 solution**: Tracks every amp-hour in/out via shunt, provides accurate SOC% and runtime remaining
- **Critical for winter camping**: Know exact diesel heater runtime remaining vs guessing from voltage (safety-critical when heater is life-support)
- **Nilight panel**: Provides instant voltage check, validates BMV-712 reading, works during Bluetooth outage

**BMV-712 Implementation**:
- **Shunt placement**: On negative side between battery negative and system ground
- **All grounds through shunt**: Blue Sea negative bus → Shunt system side → Battery negative
- **Display location**: Front panel (52mm square cutout near Nilight panel)
- **Configuration**: 200Ah capacity, 14.4V charged voltage, 4A tail current, 1.05 Peukert exponent
- **Alarms**: 30% SOC warning, 20% SOC critical

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

### Decision: Manual IR Thermometer for v1, Victron Sensor Optional, Digital Sensor Deferred to v2

**v1 Approach (Incremental Evolution)**:
- **Primary method**: Manual infrared thermometer (~$15-30)
  * Check battery surface temperature before/after use
  * Check Blue Sea fuse block, wire connections for hotspots
  * Document procedure in quickstart.md operating instructions
- **Optional enhancement**: Victron BMV-712 temperature sensor
  * BMV-712 kit includes optional battery temperature sensor
  * Attach to battery case, monitor continuous temperature via VictronConnect app
  * Useful for cold-weather camping (monitor battery temperature drop)
  * Not critical for v1 (battery has internal temperature protection in BMS)

**v2 Consideration: Integrated Digital Sensor**
- DS18B20 digital temperature sensor (1-Wire, ±0.5°C accuracy)
- NTC thermistor with ADC (analog, requires calibration)
- Embedded microcontroller (ESP32/Arduino) for datalogging
- **Rationale for deferral**: Constitution Principle IV (Incremental Evolution)
  * v1 focuses on safe power delivery (multi-layer fusing, Victron SOC monitoring)
  * Temperature monitoring can be validated manually
  * BMS includes internal temperature protection (over-temp cutoff)
  * Add complexity only after field testing proves manual monitoring inadequate

**Temperature Thresholds (Reference)**:
- LiFePO4 optimal operating range: 0°C to 45°C
- Charging restriction: Do not charge below 0°C (lithium plating risk)
- VEVOR BMS over-temperature protection: Likely 60-65°C cutoff (internal sensor)
- Wire insulation (TXL/GXL): 105°C rated, target <40°C rise during 30A load (SC-006)

---

## 7. AC Charging Implementation

### Decision: VEVOR 20A LiFePO4 Charger (External, Brand-Matched)

**Selected Product**: VEVOR 12V 20A Lithium Battery Charger  
**Model**: 010889683485  
**Key Specifications**:
- Output voltage: 14.6V (LiFePO4 absorption voltage)
- Output current: 20A
- Chemistry: LiFePO4 dedicated (may have selectable modes)
- Input: 100-120V AC, 50/60Hz
- Output connector: Alligator clips + ring terminals
- Protections: OVP, OCP, SCP, reverse polarity, over-temperature
- Certifications: CE
- Price: $57 (purchased 2026-01-18 from VEVOR.com)

**Charge Time Calculations**:
- 200Ah battery from 20% to 95% SOC: 75% × 200Ah = 150Ah to replace
- At 20A charge rate: 150Ah / 20A = **7.5 hours**
- Full charge from empty: 200Ah / 20A = **10 hours** (not recommended)
- Charge rate: 0.1C (gentle, extends battery life per Constitution Principle IV)

**Rationale:**
- Constitution Principle IV (Incremental Evolution): Use proven external charger for v1
- Eliminates design complexity and safety risk of building AC-to-DC charger from scratch
- **Brand match**: Same manufacturer as battery (likely tested together, warranty compatibility)
- **Appropriate charge rate**: 20A = 0.1C rate (gentle, recommended for longevity)
- **Correct voltage**: 14.6V is proper LiFePO4 absorption voltage (not lead-acid 14.7V)
- LiFePO4 chargers widely available, proven, match battery chemistry
- Modularity: Charger can be upgraded independently

**Charging Interface on Battery Box:**
- Input connector: Anderson PP45 (matches output connectors)
- **Adapter cable required**: Alligator clips (charger) → 12 AWG wire → PP45 (battery box)
- Inline fuse: 30A blade fuse (protects against charger malfunction)
- Wire gauge: 10 AWG from charge input to Blue Sea fuse block
- Reverse polarity protection: Mechanical (Powerpole keying prevents reverse connection)
- Panel location: Side or rear panel (separate from load outputs to avoid confusion)

---

## 8. Status Indicators and User Interface

### Decision: v1 Uses Nilight Panel + Victron BMV-712 Display, 3-LED System Deferred to v2

**v1 Status Indicators (Already Selected Components)**:
1. **Nilight 4-in-1 Panel**:
   - ON/OFF switch with power indicator LED (red or blue illumination)
   - Integrated voltmeter display (LED, shows system voltage)
   - Provides instant "power on" confirmation
   - Prevents parasitic drain during storage (switch OFF = no quiescent current)

2. **Victron BMV-712 Display**:
   - Comprehensive status: Voltage, SOC%, current flow, amp-hours consumed
   - Time-to-go prediction ("12.5 hours remaining at 5A load")
   - Alarm indicators: Low SOC warning (30%), critical (20%)
   - Bluetooth: VictronConnect app shows detailed history, graphs

**v1 Status Coverage**:
- Power status: Nilight ON/OFF switch LED
- Voltage: Nilight voltmeter (quick check) + Victron (precise)
- SOC: Victron BMV-712 (coulomb counting, accurate runtime prediction)
- Charging: Visual check VEVOR charger has LED indicators, Victron shows positive current
- Alarms: Victron configurable alarms (30% SOC warning, 20% critical)

**v2 Consideration: Dedicated 3-LED Status System**
- **Original research concept**: Power (green), Low Battery (yellow 30%), Charging (blue)
- **Rationale for deferral**: Constitution Principle IV (Incremental Evolution)
  * Nilight + Victron already provide comprehensive status
  * 3-LED system adds wiring complexity (voltage comparator circuits or microcontroller)
  * Field testing v1 will reveal if instant LED indicators more useful than Victron display
  * Avoid over-engineering (Principle VII: Bounded Complexity)
- **Add in v2 if**: Field testing shows need for instant visual status without looking at displays (e.g., checking battery from across campsite)

**Meets Constitution Requirements**:
- Principle III (Transparency): Voltage/SOC visible without disassembly via Nilight + Victron
- Principle VII (Bounded Complexity): Use purchased components, defer custom LED circuits

---

## 9. Enclosure Selection

### Decision: Greenmade 27-Gallon Storage Tote (v1), Upgrade Path to Pelican or Custom

**Selected Product: Greenmade 27-Gallon Professional Storage Tote**
- **Model**: 27-gallon black/yellow storage tote with snap-lock latches
- **External Dimensions**: 30.4" L × 20.4" W × 14.7" H
- **Internal Dimensions**: ~28" L × 18" W × 13" H (estimate, verify when received)
- **Material**: High-density polyethylene (weatherproof, impact-resistant)
- **Features**: Snap-lock latches, stackable, molded handles
- **Price**: $10-20 (purchased from Walmart)
- **Weight capacity**: 50+ lbs (sufficient for ~28-30kg total system weight)

**Battery Fit Verification**:
- Battery dimensions: 520mm × 238mm × 218mm = 20.5" L × 9.4" W × 8.6" H
- Tote internal: ~28" L × 18" W × 13" H
- **Clearances**: 7.5" length, 8.5" width, 4.5" height (excellent fit)
- Sufficient space for Blue Sea fuse block, wiring, Victron shunt alongside battery

**Required Modifications**:
1. **Nilight 4-in-1 panel**: Cutout dimensions TBD when panel received (estimated 4-6" × 2-3")
   - Location: Front panel, centered horizontally, upper third vertically
   - Tools: Drill pilot holes, jigsaw or rotary tool for rectangular cutout
2. **Victron BMV-712 display**: 52mm × 52mm square cutout
   - Location: Front panel, right of Nilight panel (ergonomic viewing together)
   - Tools: Drill 52mm hole saw or 4× corner holes + jigsaw
3. **Anderson Powerpole outputs**: 4-5× 32mm diameter holes
   - Location: Side panel (left), vertical row, 3-4" spacing
   - Labels: "HEATER 10A", "FRIDGE 15A", "SPARE 20A", "SPARE 15A", "CHARGE IN 30A"
   - Tools: 32mm step drill bit or hole saw
4. **Ventilation holes**: 4× 25-30mm diameter with mesh screening
   - Location: Top corners (2 front, 2 rear for airflow)
   - Purpose: Prevent hydrogen off-gassing accumulation (minimal with LiFePO4 but good practice)
   - Mesh: Stainless steel or aluminum, 1/8" or 1/4" grid, epoxy or grommet mount

**Component Mounting Strategy**:
- **Battery**: Secured with 2× ratchet straps (over top, anchored to tote bottom via drilled holes + bolts)
- **Blue Sea 5026 fuse block**: Mounted to side wall with self-tapping screws (Blue Sea includes mounting flanges)
- **Victron shunt**: Mounted to side wall near battery negative terminal (minimize wire length)
- **Wire routing**: Zip ties anchored to tote walls/bottom, strain relief at connectors
- **Cable glands**: Rubber grommets at Powerpole holes (strain relief, weather seal)

**Rationale for v1 Tote**:
- Constitution Principle IV (Incremental Evolution): **Cheap v1 for testing layout/connector placement**
- $10-20 tote vs $100-200 Pelican case: Test design before investing in premium enclosure
- Easy to drill/modify (polyethylene vs aluminum)
- Sufficient protection for indoor/vehicle use (testing environment)
- **Upgrade criteria**: After field testing, upgrade to Pelican or custom aluminum box if:
  * Tote shows UV degradation (outdoor use)
  * Need better impact protection (rough transport)
  * Want waterproof rating (IP65+, kayak camping)
  * Layout validated, ready to commit to permanent enclosure

**v2 Enclosure Options (Future)**:
- Pelican or SKB hard case (IP65+ waterproof, crush-proof)
- Custom aluminum case with CNC cutouts (professional appearance)
- Weatherproof polymer enclosure (NEMA 3R)
- Port layout, wiring, component placement proven in v1 tote can be replicated exactly

**Portability**:
- Total weight: 25kg battery + 3-5kg components/tote = **28-30kg** (62-66 lbs)
- Within one-person carry limit (meets SC-004: easily transported by one person)
- Greenmade handles rated for weight

---

## 10. Testing and Validation Strategy

### Decision: 6-Phase Physical Integration Testing (No Software Unit Tests)

**Phase 0: Pre-Assembly Verification (Bench Testing)**
- **VEVOR 200Ah battery**: 
  * Measure voltage with multimeter (expect 13.2-13.4V storage voltage)
  * Verify dimensions 520×238×218mm match spec
  * Inspect for shipping damage, case cracks, swelling
  * Document serial number, purchase date, initial voltage
- **Blue Sea 5026 fuse block**: 
  * Verify 12-circuit configuration, 100A busbar rating
  * Inspect for shipping damage, verify mounting flanges intact
  * Test blade fuse insertion/removal (should be snug, not loose)
- **Victron BMV-712**: 
  * Verify kit includes 500A/50mV shunt, display, RJ12 cable, temperature sensor
  * Power up display with 12V bench supply, verify boot screen
- **VEVOR 20A charger**: 
  * Connect to 120V AC, measure output voltage no-load (expect 14.4-14.6V)
  * Verify output current rating sticker matches 20A spec
  * Check polarity: Red = positive, Black = negative

**Phase 1: Pre-Power Wiring Inspection**
- **Visual inspection**: All crimps tight (tug-test Anderson Powerpoles), no exposed copper, heat-shrink coverage
- **Continuity checks** (multimeter, battery disconnected):
  * Battery+ → 100A ANL fuse → Blue Sea busbar (expect <0.1Ω)
  * Battery- → Victron shunt battery side (expect <0.1Ω)
  * Victron shunt system side → Blue Sea negative bus (expect <0.1Ω)
  * Each circuit: Blue Sea positive terminal → Powerpole output red (expect <0.5Ω for 10 AWG)
- **Polarity verification**: Red wire = positive, Black = negative throughout
- **Fuse verification**: 100A ANL in main holder, correct blade fuse ratings in Blue Sea (30A charge, 10A heater, 15A fridge, 20A USB)

**Phase 2: Initial Power-Up (No-Load)**
- **Connect battery**: Positive first (via 100A ANL fuse), then negative last (to Victron shunt battery side)
- **Expect**: Victron BMV-712 display powers on, shows voltage ~13.2V
- **Measure voltages**: 
  * Battery terminals: 13.2-13.4V
  * Blue Sea busbar: Should match battery voltage (±0.1V)
  * Each Powerpole output: Should match busbar (±0.1V)
- **Nilight panel test**: 
  * Press ON switch, verify illumination (blue LED)
  * Check voltmeter reading vs multimeter (±0.2V acceptable)
  * Test USB-C PD output with phone (expect charging indication)
  * Test 12V outlet with 12V LED bulb or multimeter (expect 12-13V)
- **Victron BMV-712 configuration**:
  * Connect via Bluetooth, VictronConnect app
  * Set battery capacity: 200Ah
  * Set charged voltage: 14.4V
  * Set tail current: 4A (2% of capacity)
  * Set Peukert exponent: 1.05 (LiFePO4 typical)
  * Enable alarms: 30% SOC warning, 20% SOC critical
  * **Synchronize SOC**: Charge battery to 14.4V+, wait for current <4A, press "Sync" in app (sets SOC to 100%)

**Phase 3: Progressive Load Testing**
- **Test 1: Light load (5A diesel heater simulation)**:
  * Connect electronic load or 60W 12V load (5A)
  * Monitor: Victron current reading (~5A), voltage (expect 13.2V stable), temperature (battery/Blue Sea/wire <40°C)
  * Duration: 1 hour
  * Success criteria: Voltage stable, no overheating, Victron shows 5Ah consumed
  
- **Test 2: Medium load (10A fridge simulation)**:
  * Connect 120W 12V load or 10A electronic load
  * Monitor: Victron current reading (~10A), voltage (expect 13.1-13.2V), Blue Sea fuse block temperature (IR thermometer)
  * Duration: 30 minutes
  * Success criteria: Voltage drop <0.3V, 10 AWG wire temperature <40°C rise
  
- **Test 3: High load (20-30A multi-device simulation)**:
  * Connect diesel heater (8A) + fridge (10A) + USB panel (5A phone charging) = 23A combined
  * Monitor: Victron current reading (~23A), voltage (expect 13.0-13.2V), all connections for hotspots
  * Duration: 15 minutes (sufficient to heat wiring to steady-state)
  * Success criteria: SC-006 validated (all components <40°C rise), voltage >12.8V at 23A load

- **Test 4: Fuse interruption (protection validation)**:
  * Install 10A blade fuse in spare circuit, load with 15A (150% rating)
  * Expect: Fuse opens within 10 seconds (blade fuse I²t characteristics)
  * Inspect: Fuse element melted cleanly, Blue Sea holder undamaged
  * Success criteria: SC-003 validated (fuse interrupts overcurrent, no damage to fuse block)

**Phase 4: Charging Validation**
- **Connect VEVOR 20A charger** via adapter cable (alligator clips → Powerpole charge input)
- **Monitor charging**: 
  * Victron BMV-712 shows positive current (~18-20A during bulk phase)
  * Battery voltage rises: 13.2V → 14.2V (bulk) → 14.6V (absorption)
  * Blue Sea circuit 1 (30A fuse) carries charge current (verify with clamp meter)
  * Temperature: VEVOR charger, Blue Sea fuse block, 10 AWG charge wire (expect warm <50°C)
- **Charge duration**: From 50% SOC (100Ah consumed) to 95% SOC (90Ah replaced at 20A = 4.5 hours)
- **Success criteria**: SC-005 validated (full charge in <12 hours from 20%), Victron SOC reaches 95%+

**Phase 5: Runtime Validation (Real-World Load)**
- **Deploy with diesel heater** (actual use case, winter camping simulation)
- **Load profile**: 5A average (diesel heater steady-state), 8A peaks (startup)
- **Monitor**: Victron time-to-go prediction, SOC% decay, voltage curve
- **Duration**: Run until 30% SOC (140Ah consumed = 28 hours at 5A)
- **Success criteria**: SC-001 validated (8+ hours runtime at 10A load, here 28+ hours at 5A exceeds requirement)
- **Data collection**: 
  * VictronConnect app: Export historical data (voltage, current, SOC, time)
  * Screenshot: Lowest SOC reached, total runtime, amp-hours consumed
  * Observations: Any unexpected shutdowns, Victron alarm triggers, user experience

**Phase 6: Documentation and Lessons Learned**
- **Test results document**: `specs/001-battery-box/docs/test-results.md`
  * Date, ambient temperature, test loads used
  * Measurements: Voltages, currents, temperatures, runtime
  * Pass/fail for each success criterion (SC-001 through SC-010)
  * Photos: Assembly, component layout, Victron display screenshots
- **Lessons learned**: 
  * Any issues encountered (poor crimps, undersized wire, connector fit)
  * Victron BMV-712 SOC accuracy vs voltage-based estimates (validate flat curve problem)
  * Greenmade tote durability, modification ease, upgrade recommendations
  * Improvements for v2: Temperature sensor needs, status LEDs useful?, solar input demand?
- **Constitution Principle V**: Document all mistakes and fixes (e.g., "Forgot to crimp one Powerpole contact, discovered during tug-test Phase 1, re-crimped successfully")

**No Software Unit Tests**:
- This is a hardware project (battery box, physical components)
- Testing is physical integration: Measure voltages, load currents, temperatures
- No source code to unit-test (no embedded firmware in v1)
- If v2 adds microcontroller (ESP32 for status LEDs, datalogging), add software unit tests then

---

## Summary of Research-Driven Design Decisions

| Decision Area | Choice | Rationale |
|---------------|--------|-----------|
| Battery Chemistry | VEVOR 200Ah 12V LiFePO4 (model 010230251465) | Safety, cycle life, flat discharge curve, 100A BMS |
| BMS | Integrated with VEVOR battery | Simplicity, multi-layer protection (OVP/UVP/OCP/SCP/temp), bounded complexity |
| Main Fuse | 100A ANL fuse | Matches BMS rating, fast-acting, safety compliance |
| Circuit Fuses | Blue Sea 5026 (12 circuits, blade fuses 10-30A) | Centralized, marine-grade, common ground bus, future expansion |
| Main Connector | Anderson Powerpole-compatible PP45 | Standardized, 45A, genderless, polarity-keyed, widely used |
| Convenience Panel | Nilight 4-in-1 (USB-C, USB-A, 12V, voltmeter, ON/OFF) | Integrated solution, eliminates separate voltmeter, prevents parasitic drain |
| Battery Monitor | Victron BMV-712 Smart with 500A shunt | Coulomb counting (±1% SOC), runtime predictions, critical for LiFePO4 flat curve, Bluetooth |
| Temperature Monitoring | Manual IR thermometer (v1), Victron sensor optional | Incremental evolution, BMS has internal protection, defer digital sensor to v2 |
| Charger | VEVOR 20A LiFePO4 charger (model 010889683485) | External, brand-matched, 0.1C rate, 14.6V absorption, proven |
| Status Indicators | Nilight panel LED + Victron display | Comprehensive coverage, defer custom 3-LED system to v2, avoid over-engineering |
| Enclosure | Greenmade 27gal tote (30.4×20.4×14.7 inches) | Test layout in cheap v1, upgrade to Pelican/aluminum v2 after validation |
| Wire Sizing | 4 AWG main trunks, 10 AWG circuits, 12 AWG pigtails | Current capacity, voltage drop <3%, safety margin, TXL/GXL 105°C |
| Testing Strategy | 6-phase validation (bench, wiring, power-up, load, charge, runtime) | Safety-critical, documented outcomes, Constitution Principle V |

**All Technical Unknowns Resolved**: Component-specific details documented. Ready for assembly task generation.

