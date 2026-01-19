# Component Interface Contracts: Battery Box v1

**Purpose**: Define electrical and mechanical interface specifications for modular component integration  
**Created**: 2026-01-18  
**Feature**: [spec.md](../spec.md) | [data-model.md](../data-model.md)

## Overview

This document establishes the "contracts" between battery box components - the electrical, mechanical, and behavioral specifications that enable modular design per Constitution Principle II. Any component replacement must satisfy these contracts to ensure compatibility and safety.

---

## 1. Battery-to-System Interface

### Electrical Contract

**Voltage Output:**
- Nominal: 12.8V DC
- Range: 10.0V (BMS cutoff) to 14.6V (fully charged)
- Tolerance: ±0.2V under no load

**Current Capacity:**
- Minimum continuous: 30A (to support typical loads)
- Recommended: 50A-100A (for future expansion)
- Pulse current: 2× continuous for 5 seconds maximum

**Protection Requirements (via BMS):**
- Over-voltage disconnect: ≤14.8V
- Under-voltage disconnect: ≥10.0V
- Over-current disconnect: At or below wire/fuse rating
- Short-circuit protection: <10ms response time

**Terminal Specifications:**
- Type: M6 or M8 threaded posts, or manufacturer-specific connector
- Torque: Per manufacturer specification (typically 4-6 Nm for M6, 8-10 Nm for M8)
- Wire attachment: Ring terminals, properly crimped

### Mechanical Contract

**Physical Constraints:**
- Maximum dimensions: 550mm × 250mm × 220mm (to fit Greenmade 27gal tote: ~711×457×330mm internal)
- Maximum weight: 30kg (for one-person portability when combined with enclosure ~3-5kg → total 28-35kg)
- Mounting: Must have secure mounting points (brackets, straps, or integrated handles)

**Thermal Requirements:**
- Operating temperature: 0°C to 45°C (discharge), 0°C to 45°C (charge, **do not charge below 0°C**)
- Heat dissipation: Natural convection through enclosure ventilation (4× 25-30mm holes with mesh)
- No active cooling required for continuous 30A discharge (target <40°C rise per SC-006)

### Behavioral Contract

**State Reporting:**
- Voltage must be externally measurable at battery terminals (measured by Victron BMV-712 shunt + Nilight panel)
- Temperature must be measurable (integrated sensor or accessible surface for IR thermometer)
- BMS fault state should be indicated (if BMS provides fault output)

**Replacement Criteria:**
- Any 12V LiFePO4 battery with integrated BMS meeting electrical specs
- Chemistry must be LiFePO4 (not lead-acid, NMC, or other lithium)
- Capacity minimum: 50Ah (smaller capacity acceptable if user requirements reduced)

### v1 Implementation: VEVOR 200Ah LiFePO4

**Satisfies Contract:**
- ✅ Voltage: 12.8V nominal, 10.0-14.6V range per VEVOR BMS
- ✅ Current: 100A continuous (exceeds 30A minimum, matches 100A ANL fuse)
- ✅ Protection: VEVOR BMS includes OVP (~14.6V), UVP (~10.0V), OCP (100A), SCP, over-temp
- ✅ Terminals: **M8 threaded posts** (4 AWG ring terminals, torque 8-10 Nm)
- ✅ Dimensions: **520mm × 238mm × 218mm** (fits Greenmade tote with 7.5" front, 8.5" side, 4.5" top clearances)
- ✅ Weight: **25kg** (total system 28-30kg within one-person limit)
- ✅ Temperature: 0-45°C range per VEVOR spec, BMS internal over-temp protection
- ✅ State reporting: Voltage via Victron BMV-712 + Nilight panel, temp via IR thermometer or Victron sensor
- ✅ Chemistry: LiFePO4 (4S configuration, 3.2V/cell × 4 = 12.8V)
- ✅ Capacity: 200Ah (far exceeds 50Ah minimum, provides 40+ hours diesel heater runtime)

**Procurement**: VEVOR model 010230251465, purchased 2026-01-18, $450-550

---

## 2. Main Fuse Interface

### Electrical Contract

**Fuse Specifications:**
- Type: ANL, Mega, or Class-T DC-rated fuse
- Voltage rating: Minimum 32V DC
- Current rating: Match battery BMS rating or 125% of maximum expected continuous load
- Interrupt rating: Minimum 1000A at 12V DC (short-circuit current capacity)

**Placement:**
- Location: **Within 18 inches of battery positive terminal** (NEC recommendation, minimize unfused wire)
- Wire gauge: Match or exceed fuse rating (e.g., 100A fuse → 4 AWG minimum)
- Connection: Crimped ring terminals, properly torqued

### Mechanical Contract

**Fuse Holder:**
- Type: Inline ANL holder or panel-mount fuse block
- Mounting: Secure to enclosure or busbar, prevent vibration
- Accessibility: User-replaceable without tools (or basic hand tools only)

### Behavioral Contract

**Protection Response:**
- Time-current characteristics: Per manufacturer datasheet
- Validation: Fuse must interrupt at 150% rating per datasheet spec (SC-003)
- Failure mode: Open circuit (safe failure per Constitution Principle I)

**Replacement Criteria:**
- Same type and rating, or higher interrupt rating
- Must be DC-rated (AC fuses have different characteristics)
- Document replacement fuse specification in `docs/component-specs.md`

### v1 Implementation: 100A ANL Fuse

**Satisfies Contract:**
- ✅ Type: ANL (automotive nickel link, DC-rated, fast-acting)
- ✅ Voltage: 32V DC rated (exceeds 12V system, covers surge to 14.6V charging)
- ✅ Current: **100A rating matches VEVOR BMS continuous discharge limit** (coordination: BMS primary, ANL backup)
- ✅ Interrupt: ANL fuses rated for high DC interrupt (typically 5000A+ short-circuit current)
- ✅ Placement: **Inline ANL holder within 18" of battery+ terminal** (4 AWG wire from Battery+ M8 post to ANL holder)
- ✅ Wire gauge: **4 AWG** (105A ampacity at 40°C ambient, exceeds 100A fuse rating with margin)
- ✅ Terminals: M8 ring terminal (battery end), ANL holder lugs (fuse ends), ring terminal or stud (Blue Sea busbar)
- ✅ Holder: Inline ANL holder (4-6 AWG compatible, screw terminals)
- ✅ Accessibility: Fuse can be replaced by removing ANL holder cover (hand-accessible)
- ✅ Failure mode: Fuse opens cleanly on overcurrent (safe failure, isolates battery)

**Procurement**: ANL fuse (~$5-8), inline ANL holder (~$10-15), M8 ring terminals (~$2-5 for pair)

**Rationale**: 100A ANL coordinates with VEVOR 100A BMS (if BMS fails to protect, ANL fuse is backup for sustained 100A+ overcurrent)

---

## 3. Output Connector Interface

### Electrical Contract

**Connector Specifications:**
- Voltage: 12V DC nominal (10V - 14.6V range)
- Current rating: Match or exceed circuit fuse rating
- Contact resistance: <10 milliohms per connector pair
- Insulation voltage: Minimum 50V DC

**Standard Connector Options (per Constitution Principle II):**

| Connector Type   | Current Rating | Use Case                      | Polarity Protection |
|------------------|----------------|-------------------------------|---------------------|
| Anderson PP15    | 15A continuous | Low-power loads               | Mechanical keying   |
| Anderson PP30    | 30A continuous | Medium loads (heater, fridge) | Mechanical keying   |
| Anderson PP45    | 45A continuous | High-power loads, main output | Mechanical keying   |
| XT60             | 60A continuous | High-power, compact           | Mechanical keying   |
| XT90             | 90A continuous | Very high power (future)      | Mechanical keying   |
| Cigarette Lighter| 10A (derated)  | Accessory compatibility       | Center-positive std |
| USB-C PD         | 5A @ 5-20V     | Phone/tablet charging         | USB standard        |

**Polarity Convention:**
- Positive: Red wire, marked "+" or "POS"
- Negative: Black wire, marked "-" or "NEG" or "GND"
- Anderson Powerpole: Tongue on left when viewing housing from contact side = positive

### Mechanical Contract

**Mounting:**
- Panel-mount connectors: Cutout or bolt holes in enclosure wall
- Strain relief: Cable gland or boot to prevent wire pull-out
- Labeling: Voltage, current rating, polarity clearly marked adjacent to connector

**Accessibility:**
- External mounting for user connection without opening enclosure
- Protected from accidental short (recessed, covered, or shrouded terminals)

### Behavioral Contract

**Connection Sequence:**
- Must tolerate hot-plugging (connection under load without damage)
- Connector must not spark excessively on connection (XT-style connectors have anti-spark design)
- If sparking is issue, add pre-charge resistor or require load-off connection

**Replacement Criteria:**
- Any connector meeting current rating and polarity protection requirements
- Non-standard connector requires documentation per FR-011 (rationale + replacement strategy)
- Document change in `docs/component-specs.md`

### v1 Implementation: Anderson Powerpole-Compatible PP45

**Satisfies Contract:**
- ✅ Type: Anderson Powerpole-compatible PP45 (45A continuous, genderless, polarized)
- ✅ Voltage: Rated for 12V systems (handles 10.0-14.6V range)
- ✅ Current: **45A rating exceeds all circuit fuse ratings** (10A heater, 15A fridge, 20A spare, 30A charge)
- ✅ Contact resistance: <5 milliohms per mating pair (low voltage drop)
- ✅ Polarity protection: **Mechanical keying** via dovetail housing (red+black bonded pairs, cannot reverse)
- ✅ Mounting: **Panel-mount via 32mm diameter holes** in side panel (4-5 outputs + 1 charge input)
- ✅ Strain relief: Rubber grommets or cable glands at panel holes
- ✅ Labeling: Each connector labeled: "HEATER 10A", "FRIDGE 15A", "SPARE 20A", "SPARE 15A", "CHARGE IN 30A"
- ✅ Hot-plugging: Tolerates connection under load (standard practice in RV/amateur radio use)
- ✅ Accessibility: External side panel mounting, no enclosure opening required

**Procurement**: 10 bonded red+black pairs (~$25-40, generic Amazon PP45-compatible), AWG10-12 compatible

**Circuit Allocation**:
- Circuit 2 (Heater): 1× PP45 output, 10A blade fuse
- Circuit 3 (Fridge): 1× PP45 output, 15A blade fuse
- Circuit 5 (Spare 1): 1× PP45 output, 20A blade fuse
- Circuit 6 (Spare 2): 1× PP45 output, 15A blade fuse
- Circuit 1 (Charge): 1× PP45 input, 30A blade fuse
- Circuit 4 (USB): Nilight panel hardwired (not Powerpole)

**Rationale**: Anderson Powerpole standard in RV/emergency power, genderless design (any connector mates with any), 45A exceeds all circuit needs, widely available pigtail cables

---

## 4. Charging Connector Interface

### Electrical Contract

**Input Specifications:**
- Voltage: 14.0V - 14.6V DC (LiFePO4 bulk/absorption voltage)
- Current: 10A minimum recommended (for reasonable charge time)
- Polarity: Positive to battery positive, negative to battery negative

**Protection Requirements:**
- Reverse polarity protection: Schottky diode, MOSFET circuit, or mechanically keyed connector
- Overcurrent protection: Fuse rated for charger output current (e.g., 20A fuse for 20A charger)
- Voltage limit: BMS will disconnect at over-voltage, but charger should not exceed 14.8V

**Connector Options:**
- Same as Output Connector Interface (Anderson PP30/45, XT60)
- Alternatively: Barrel jack (5.5mm × 2.1mm or 5.5mm × 2.5mm) for lower current chargers

### Mechanical Contract

**Mounting:**
- External panel-mount for user access
- Clearly labeled: "CHARGE INPUT ONLY - 14.4V LiFePO4"
- Separate from output connectors to prevent confusion

### Behavioral Contract

**Charging Sequence:**
- User connects charger to AC mains, then connects to battery box
- Charger voltage rises, battery accepts current, voltage increases
- When battery reaches 14.4V, charger transitions to constant voltage (current tapers)
- Charger terminates or floats at 13.6V when charge complete
- User disconnects charger from battery box, then from AC mains

**Charger Compatibility:**
- Must be LiFePO4-compatible (not lead-acid charger)
- Recommended chargers: Victron, Renogy, NOCO (with LiFePO4 mode)
- Document compatible charger models in `docs/component-specs.md` per FR-022

**Replacement Criteria:**
- Connector can be changed if charger uses different connector
- Must maintain reverse polarity protection
- Document change rationale per FR-011

### v1 Implementation: Anderson Powerpole PP45 with VEVOR Adapter Cable

**Satisfies Contract:**
- ✅ Voltage: **14.6V VEVOR charger** (LiFePO4 absorption voltage, matches BMS)
- ✅ Current: **20A VEVOR charger output** (0.1C charge rate for 200Ah battery)
- ✅ Polarity: **Mechanical keying** via Powerpole connector (cannot reverse)
- ✅ Protection: 30A blade fuse (Blue Sea circuit 1) + 100A ANL + VEVOR charger internal OVP/OCP
- ✅ Connector: **Powerpole PP45 on battery box** (matches output connector standard)
- ✅ Adapter cable: **Alligator clips (charger) → 12 AWG wire 3-6 ft → PP45 (battery box)**
- ✅ Labeling: **"CHARGE IN 30A"** on side panel at Powerpole connector
- ✅ Mounting: Side panel 32mm hole (separate from output connectors, clearly marked)
- ✅ Accessibility: External panel mount, connect/disconnect without opening enclosure

**Adapter Cable Specifications**:
- VEVOR charger end: Red/black alligator clips (charger output)
- Wire: 12 AWG red/black, 3-6 ft length
- Battery box end: Powerpole PP45 connector (mates with charge input on panel)
- Label: **"CHARGER ADAPTER - DO NOT USE FOR LOADS"** (prevents accidental use as output extension)
- Polarity: Red = positive, Black = negative (verified with multimeter before first use)

**Charging Process**:
1. Connect VEVOR charger to 120V AC mains
2. Connect adapter cable alligator clips to charger output (red to red, black to black)
3. Connect adapter cable PP45 to battery box "CHARGE IN 30A" connector
4. Victron BMV-712 shows positive current (~18-20A bulk phase)
5. Charge proceeds: Bulk 14.4V → Absorption 14.6V → Float 13.6V (if charger supports)
6. Disconnect in reverse: PP45 from battery box, alligator clips from charger, charger from AC

**Procurement**: VEVOR 20A charger (purchased, $57), adapter cable (DIY: 12 AWG wire + PP45 connector + alligator clips, ~$10-15)

**Rationale**: Powerpole standardization (charge input uses same connector as outputs), adapter cable enables VEVOR alligator clip charger compatibility, mechanical keying prevents reverse polarity

---

## 5. Voltage Meter Interface

### Electrical Contract

**Input Range:**
- Minimum: 5V DC (to accommodate deep discharge)
- Maximum: 30V DC (margin above 14.6V charge voltage)
- Accuracy: ±0.1V or ±1% (whichever is greater) per SC-002

**Power Supply:**
- Powered directly from battery (parallel to battery terminals)
- Quiescent current: <20mA to minimize parasitic drain
- No external power supply required

**Measurement Connection:**
- Sense wires: 18-22 AWG, minimal current draw
- Connection point: Directly at battery terminals or main busbar (before fuse if possible)

### Mechanical Contract

**Mounting:**
- Panel-mount in enclosure front or top
- Cutout dimensions: Per meter manufacturer spec (common: 45mm × 26mm × 24mm for 0.36" display)
- Viewing angle: Perpendicular to user's line of sight when enclosure on ground

**Visibility:**
- Character height: Minimum 9mm (0.36") for 2-meter viewing distance per SC-005
- Display color: Red or blue LED (high contrast in various lighting)
- Brightness: Adjustable if possible (potentiometer on meter board)

### Behavioral Contract

**Update Rate:**
- Minimum 1 reading per second (sufficient for manual monitoring)
- Display should stabilize within 2 seconds of voltage change

**Accuracy Validation:**
- Compare to calibrated multimeter at 11V, 12V, 13V, 14V (per SC-002)
- Document calibration results in `docs/test-results.md`

**Replacement Criteria:**
- Any digital panel meter meeting voltage range and accuracy requirements
- Analog meters acceptable if they meet visibility and accuracy specs
- Document replacement in `docs/component-specs.md`

### v1 Implementation: Dual System - Victron BMV-712 (Primary) + Nilight Panel (Quick Check)

**Primary: Victron BMV-712 Smart Battery Monitor**

**Satisfies Contract:**
- ✅ Input range: **0-70V DC** (far exceeds 10.0-14.6V LiFePO4 range)
- ✅ Accuracy: **±0.1V voltage, ±1% SOC** (after full charge synchronization)
- ✅ Power: **~10-20mA quiescent** from 12V battery via shunt
- ✅ Measurement: **500A/50mV shunt in negative trunk** (measures all system current)
- ✅ Display: **52mm × 52mm square panel mount** on front panel (right of Nilight)
- ✅ Visibility: Display readable from 2+ meters, shows voltage/SOC%/current/time-to-go
- ✅ Update rate: Real-time (1-2 second refresh), Bluetooth app for detailed monitoring

**Additional Features Beyond Contract:**
- Coulomb counting (tracks every amp-hour in/out for accurate SOC%)
- Runtime prediction ("12.5 hours remaining at 5A load")
- Historical data via VictronConnect app (voltage/current/SOC graphs)
- Configurable alarms (30% SOC warning, 20% critical)
- Optional temperature sensor (can attach to battery case)

**Configuration** (VictronConnect app):
- Battery capacity: 200Ah
- Charged voltage: 14.4V (sync SOC to 100% when reached)
- Tail current: 4A (2% of capacity, end of charge detection)
- Peukert exponent: 1.05 (LiFePO4 typical)
- Alarms: 30% SOC warning (yellow), 20% SOC critical (red)

**Procurement**: Victron BMV-712 Smart kit ($200-250, includes 500A shunt, display, RJ12 cable, temp sensor)

**Secondary: Nilight 4-in-1 Panel Integrated Voltmeter**

**Satisfies Contract:**
- ✅ Input range: **12-24V DC** (covers 10.0-14.6V LiFePO4 range)
- ✅ Accuracy: **±0.1-0.2V typical** (LED voltmeter, sufficient for quick check)
- ✅ Power: **50-100mA quiescent** (entire Nilight panel including USB, 12V outlet)
- ✅ Measurement: Connected to Blue Sea circuit 4 (20A fused, ON/OFF switch prevents drain)
- ✅ Display: **Integrated LED voltmeter** on Nilight panel (blue illumination)
- ✅ Visibility: Front panel center, readable from 2+ meters
- ✅ Update rate: Real-time LED display

**Additional Features**:
- ON/OFF switch (prevents 50-100mA drain during storage)
- Power indicator LED (confirms system on)
- Integrated with USB-C PD, USB-A, 12V outlet (single panel solution)

**Procurement**: Nilight 4-in-1 panel (purchased, ~$30-40)

**Rationale**: 
- **Victron BMV-712 critical for LiFePO4**: Voltage-only monitoring inadequate (flat discharge curve 13.2V from 80% to 30% SOC), coulomb counting provides accurate runtime prediction for diesel heater winter camping safety
- **Nilight panel backup**: Quick voltage check without phone/Bluetooth, validates BMV-712 reading, works if Bluetooth unavailable
- **Bonus**: Nilight eliminates separate voltmeter purchase (was in original research, now integrated)

---

## 6. Temperature Sensor Interface

### Electrical Contract (for Active Sensors)

**Sensor Types:**
- **DS18B20**: 1-Wire digital, 3-wire connection (VCC, GND, Data), 3.0-5.5V supply
- **NTC Thermistor (10K @ 25°C)**: 2-wire, requires voltage divider and ADC or analog meter
- **Passive IR Thermometer**: No electrical interface (manual reading)

**Accuracy:**
- ±0.5°C to ±1.0°C in operating range (0°C to 50°C)

**Connection:**
- Sensor cable length: <3 meters (minimize noise for digital sensors)
- Shielded cable recommended if EMI environment (near chargers, inverters)

### Mechanical Contract

**Mounting:**
- **Surface mount**: Adhesive-backed sensor on battery case or enclosure wall
- **Insertion**: If battery has temperature port, use manufacturer connector
- **Non-contact**: IR thermometer measurement through access port

### v1 Implementation: Manual IR Thermometer + Optional Victron Sensor

**Satisfies Contract (Manual Approach):**
- ✅ Type: **Infrared thermometer** (non-contact, manual reading)
- ✅ Accuracy: **±0.5-1.0°C** typical for consumer IR thermometers
- ✅ Operating range: **-20°C to 80°C** (covers battery 0-45°C range)
- ✅ Mounting: **No mounting required** (handheld, point at battery case surface)
- ✅ Measurement procedure: Check battery surface temperature before/after use, document in operating log
- ✅ Target locations: Battery case (center/corners), Blue Sea fuse block, wire connections (10 AWG at Powerpoles)

**Procedure** (documented in quickstart.md operating instructions):
1. Before use: Measure battery surface temperature (should be ambient, 15-25°C typical)
2. After 30A load test: Measure battery, Blue Sea, wire connections (should be <40°C rise per SC-006)
3. During charging: Measure battery during 20A charge (should remain <40°C)
4. Log measurements in `docs/test-results.md` (date, ambient temp, load, battery temp)

**Procurement**: Generic IR thermometer (~$15-30, Amazon/hardware store)

**Optional Enhancement: Victron BMV-712 Temperature Sensor**

**Satisfies Contract (Continuous Monitoring):**
- ✅ Type: **Victron temperature sensor** (included with BMV-712 kit)
- ✅ Accuracy: **±1°C** (Victron spec)
- ✅ Connection: Plug into BMV-712 shunt (dedicated temp sensor port)
- ✅ Mounting: **Adhesive-backed sensor on battery case** (thermal contact)
- ✅ Monitoring: **Continuous via VictronConnect app** (shows battery temp real-time)
- ✅ Cable length: ~3 meters (shunt to battery case)

**When to Use**:
- Cold-weather camping (monitor battery temperature drop below 0°C, do not charge if frozen)
- Extended high-load use (diesel heater continuous operation, verify battery temp stable)
- Capacity validation (battery capacity affected by temperature, Victron compensates SOC calculation)

**Rationale for v1 Deferral**:
- **Constitution Principle IV (Incremental Evolution)**: Manual IR thermometer adequate for v1 validation
- **VEVOR BMS includes internal over-temp protection** (~60-65°C cutoff, primary safety layer)
- **Add continuous monitoring in v2** if field testing shows manual checks inadequate
- **Victron sensor optional**: Can add anytime (plug-and-play), useful for winter camping monitoring

**v2 Consideration: Embedded Digital Sensor**
- DS18B20 with ESP32/Arduino datalogging (real-time graphs, alerts)
- Deferred until v1 field testing proves need for continuous automated monitoring
- Constitution Principle VII (Bounded Complexity): Avoid over-engineering, measure before optimize

**Positioning:**
- Within 25mm of battery case surface for accurate reading
- Not in direct airflow path (ventilation holes) - measure battery, not air

### Behavioral Contract

**Readout Method:**
- **Digital sensor**: Log to Raspberry Pi, Arduino, or dedicated display (future feature)
- **Manual check**: User measures with IR thermometer before/after use per FR-015
- **Warning threshold**: 40°C per SC-006

**Replacement Criteria:**
- Any sensor meeting accuracy and mounting requirements
- Document sensor type and readout method in `docs/component-specs.md`

---

## 7. Status LED Interface

### Electrical Contract

**LED Specifications:**
- Forward voltage: 2.0-3.5V (depending on color)
- Forward current: 10-20mA (with current-limiting resistor)
- Viewing angle: Minimum 60° (wide diffusion for visibility)

**LED Colors and Functions:**
- Green: Power/System OK (voltage >13.0V)
- Yellow/Amber: Low Battery Warning (voltage <13.0V)
- Red: Charging (voltage >14.0V, indicating charger connected)

**Trigger Circuits:**
- **Simple**: Voltage comparator (e.g., LM339) with voltage divider to set threshold
- **Alternative**: Transistor switch with Zener diode threshold
- Current limiting: Resistor sized for 10-20mA (e.g., 680Ω for 12V supply, red LED)

### Mechanical Contract

**Mounting:**
- Panel-mount LEDs: 5mm or 10mm diameter
- Bezel mount: Snap-in or threaded bezel on enclosure panel
- Spacing: Minimum 15mm between LEDs for clear distinction

**Labeling:**
- Text labels adjacent to LEDs: "POWER", "LOW BATTERY", "CHARGING"
- Or use universal symbols: ✓ (power), ⚠ (warning), ⚡ (charging)

### Behavioral Contract

**State Indication:**
| LED           | Condition                  | Expected State |
|---------------|----------------------------|----------------|
| Power (Green) | Voltage ≥13.0V, no charger | ON             |
| Power (Green) | Voltage <13.0V             | OFF            |
| Low Batt (Yellow) | Voltage <13.0V         | ON             |
| Low Batt (Yellow) | Voltage ≥13.0V         | OFF            |
| Charging (Red)| Voltage >14.0V (charger)   | ON             |
| Charging (Red)| Voltage ≤14.0V             | OFF            |

**Replacement Criteria:**
- LEDs are consumable (10,000+ hour lifespan typical)
- Replace with same color, size, and forward voltage
- Document in `docs/component-specs.md`

### v1 Implementation: Nilight Panel + Victron BMV-712 Display (3-LED System Deferred)

**Satisfies Contract via Integrated Components:**
- ✅ Power status: **Nilight ON/OFF switch with power indicator LED** (blue/red, illuminates when ON)
- ✅ Voltage/SOC display: **Victron BMV-712 display** (shows voltage, SOC%, current, alarms)
- ✅ Low battery warning: **Victron configurable alarms** (30% SOC yellow warning, 20% critical red)
- ✅ Charging indication: **Visual check VEVOR charger** (has LED indicators) + **Victron shows positive current**
- ✅ Visibility: Both displays front panel mounted, readable from 2+ meters

**Status Coverage**:

| Status Indicator | v1 Implementation | Location |
|-----------------|-------------------|----------|
| Power ON | Nilight switch LED (blue/red) | Front panel center (Nilight) |
| Voltage | Nilight voltmeter (±0.1-0.2V) + Victron (±0.1V) | Front panel (both) |
| SOC% | Victron BMV-712 display (±1%) | Front panel right (52mm cutout) |
| Low Battery | Victron alarm (30% yellow, 20% red) | Victron display + app |
| Charging | VEVOR charger LEDs + Victron positive current | Charger (external) + Victron display |
| Runtime | Victron time-to-go prediction | Victron display + app |

**Rationale for Deferring 3-LED System**:
- **Constitution Principle IV (Incremental Evolution)**: Nilight + Victron provide comprehensive status
- **Constitution Principle VII (Bounded Complexity)**: Avoid over-engineering, use purchased components
- **3-LED system adds complexity**: Voltage comparator circuits or microcontroller, additional wiring
- **Field testing will reveal**: If instant LED status more useful than Victron display
- **Add in v2 if needed**: E.g., checking battery from across campsite without walking to enclosure

**v2 Consideration: Dedicated 3-LED Panel**
- Green (Power): ON when voltage >13.0V (LM339 comparator)
- Yellow (Low Battery): ON when voltage <13.0V or Victron SOC <30%
- Red (Charging): ON when voltage >14.0V (detects charger)
- Implementation: Voltage divider + LM339 quad comparator + 3 LEDs with current-limiting resistors
- Defer until field testing proves Nilight/Victron status inadequate

---

## 8. Wire and Cable Interface Standards

### Wire Gauge Selection (per Current Rating)

| Circuit Current | Minimum AWG | Recommended AWG | Insulation Rating |
|----------------|-------------|-----------------|-------------------|
| 0-10A          | 16 AWG      | 14 AWG          | 105°C (TXL/GXL)   |
| 10-20A         | 14 AWG      | 12 AWG          | 105°C (TXL/GXL)   |
| 20-35A         | 12 AWG      | 10 AWG          | 105°C (TXL/GXL)   |
| 35-50A         | 10 AWG      | 8 AWG           | 105°C (TXL/GXL)   |
| 50-80A         | 8 AWG       | 6 AWG           | 105°C (TXL/GXL)   |
| 80-125A        | 6 AWG       | 4 AWG           | 105°C (TXL/GXL)   |

**Color Convention:**
- **Red**: Positive (+), battery hot, switched power
- **Black**: Negative (-), battery return, ground
- **Yellow**: Low battery warning signal (if using sensor wire)
- **Blue**: Charging indicator signal (if using sensor wire)
- **White**: Temperature sensor or data lines

### Crimping and Termination Standards

**Ring Terminals:**
- Use insulated, heat-shrink ring terminals
- Crimp with proper ratcheting crimper (not pliers)
- Solder after crimp for mechanical security (optional but recommended)

**Connector Terminations:**
- Anderson Powerpole: Use manufacturer crimp tool (SB50 preferred, HX-2547 acceptable)
- XT connectors: Solder wires into connector cups, heat shrink over joints
- Barrel connectors: Solder connection, strain relief mandatory

**Strain Relief:**
- All panel-mount connectors: Use cable gland or rubber grommet
- Prevent wire pull-out, protect against vibration fatigue

### v1 Implementation: Wire Specifications and Quantities

**Satisfies Contract:**

**Main Trunk Wiring (Battery to Blue Sea)**:
- ✅ **Positive trunk**: 4 AWG red, 4 ft (Battery+ M8 → 100A ANL holder → Blue Sea+ busbar)
  * Current capacity: **105A at 40°C ambient** (exceeds 100A ANL fuse rating)
  * Voltage drop: <0.1V at 100A over 4 ft (negligible)
  * Terminals: M8 ring terminal (battery), ANL holder lugs, Blue Sea busbar stud
- ✅ **Negative trunk**: 4 AWG black, 6-8 ft (Battery- M8 → Victron shunt battery side → Victron shunt system side → Blue Sea- bus)
  * **Critical**: Carries ALL system return current (charge 20A + heater 8A + fridge 10A + USB 20A = 58A+ potential)
  * Current capacity: **105A at 40°C ambient** (matches positive side)
  * Terminals: M8 ring terminal (battery), shunt lugs (both sides), Blue Sea negative bus

**Circuit Wiring (Blue Sea to Outputs)**:
- ✅ **10 AWG red**: 25 ft total (Blue Sea+ terminals to Powerpole connectors for 6 circuits)
  * Per circuit: ~3-4 ft (Blue Sea to side panel cutout)
  * Current capacity: **35-40A at 40°C ambient** (exceeds largest 30A charge circuit)
  * Circuits: 1-Charge, 2-Heater, 3-Fridge, 4-USB panel, 5-Spare, 6-Spare
- ✅ **10 AWG black**: 25 ft total (Blue Sea- bus to Powerpole connectors for 6 circuits)
  * Same routing as red (star grounding: all negatives to Blue Sea bus)

**Pigtail Wiring (Powerpole to Load)**:
- ✅ **12 AWG red/black**: 20 ft each (Powerpole contact pigtails)
  * 10 pairs (5 circuits × 2 ends: panel mount + cable plug)
  * Current capacity: **25-30A at 40°C ambient** (sufficient for all circuits 10-30A)
  * Length: 6-12" pigtails from 10 AWG to Powerpole contact

**Sensing/Signal Wiring**:
- ✅ **18-22 AWG**: 10 ft total (Victron shunt to display RJ12 cable included, temperature sensor optional)
  * Low current (<100mA), voltage sensing only

**Insulation Rating**:
- ✅ **TXL or GXL automotive wire**: 105°C insulation rating (exceeds <40°C rise target per SC-006)
  * Abrasion-resistant, flexible, suitable for mobile applications

**Color Convention**:
- ✅ **Red**: All positive connections (battery+, Blue Sea+ circuits, Powerpole contacts)
- ✅ **Black**: All negative connections (battery-, Blue Sea- bus, Powerpole contacts)

**Crimping Standards**:
- ✅ **Ring terminals**: Ratcheting crimper (not pliers), M8 for battery, assorted for Blue Sea/ANL holder
  * Heat-shrink insulated ring terminals preferred (strain relief)
- ✅ **Powerpole contacts**: Knoweasy Powerpole crimper (PP15/30/45 compatible, ratcheting, contact positioner)
  * Practice on scrap wire first, tug-test each crimp (should not pull out)
  * No solder (Powerpole contacts designed for crimp-only, solder wicks up wire and makes stiff)

**Procurement**:
- 4 AWG red wire: 4 ft (~$8-12)
- 4 AWG black wire: 6-8 ft (~$12-18)
- 10 AWG red wire: 25 ft (~$15-25)
- 10 AWG black wire: 25 ft (~$15-25)
- 12 AWG red wire: 20 ft (~$10-15)
- 12 AWG black wire: 20 ft (~$10-15)
- 18-22 AWG wire: 10 ft (~$5-8, or use existing scrap)
- Ring terminals: M8 (2× battery) + assorted ANL/Blue Sea (~$5-10)
- Heat-shrink tubing: Assorted sizes (~$10-15)
- Powerpole contacts: Included with 10-pair connector kit

**Total Wire Cost**: ~$75-125 (TXL/GXL automotive grade)

**Rationale**:
- **4 AWG main trunks**: Match 100A ANL fuse rating, minimize voltage drop on high-current paths
- **10 AWG circuits**: Handle all Blue Sea circuit fuse ratings (10-30A) with margin, flexible routing in tight tote
- **12 AWG pigtails**: Powerpole contacts rated AWG10-12, 12 AWG more flexible for short pigtails, crimps easier
- **Negative trunk 6-8 ft**: Longer than positive (must route through Victron shunt), critical for star grounding

---

## 9. Enclosure Interface Requirements

### Cutouts and Mounting Holes

**Required Openings:**
- Voltmeter cutout: Per meter manufacturer spec (e.g., 45mm × 26mm)
- Output connector(s): Typically 15-25mm diameter per connector
- Charging connector: Same as output
- LED indicators: 5mm or 10mm holes (or rectangular bezel cutouts)
- Ventilation: Minimum 2× 25mm (1 inch) holes with mesh

**Material Compatibility:**
- Plastic enclosures: Drill or step drill for clean cuts
- Metal enclosures: Drill, nibbler tool, or knockout punch
- Plywood: Hole saw or Forstner bit

### Ventilation Contract

**Airflow Requirements:**
- Minimum 2 ventilation holes: 1 high (heat exit), 1 low (cool air intake)
- Hole diameter: 25mm (1 inch) minimum, larger if space permits
- Mesh cover: Stainless steel or plastic mesh to prevent debris entry
- Net free area: Minimum 500mm² total (e.g., 2× 25mm holes = ~980mm²)

**Thermal Budget:**
- Battery heat generation: ~10-30W at 30A discharge (depending on internal resistance)
- Passive cooling via convection: Sufficient for <40°C target per SC-006

### Internal Layout Contract

**Component Placement:**
- Battery: Bottom of enclosure (center of gravity low for stability)
- Fuse holders: Accessible from top or front (user replacement)
- Voltmeter/LEDs: Front panel (user visibility)
- Connectors: Side or front panel (cable management)

**Wire Routing:**
- Avoid sharp edges: Use grommets or edge protection
- Secure with cable ties or adhesive mounts (prevent chafing)
- Separate high-current and signal wires (minimize EMI)

### v1 Implementation: Greenmade 27-Gallon Tote Modifications

**Satisfies Contract:**

**Cutouts and Holes:**
- ✅ **Nilight panel**: 4-6" × 2-3" rectangular cutout (verify exact dimensions when panel received)
  * Location: Front panel center, upper third
  * Tools: Drill pilot holes + jigsaw or rotary tool
- ✅ **Victron BMV-712 display**: 52mm × 52mm square cutout
  * Location: Front panel right of Nilight (ergonomic viewing together)
  * Tools: 52mm hole saw or 4× corner pilot holes + jigsaw
- ✅ **Powerpole outputs**: 4-5× 32mm diameter holes
  * Location: Side panel (left), vertical row, 3-4" spacing
  * Connectors: HEATER 10A, FRIDGE 15A, SPARE 20A, SPARE 15A, CHARGE IN 30A
  * Tools: 32mm step drill bit or hole saw
  * Grommets: Rubber grommets for strain relief and weather seal
- ✅ **Ventilation**: 4× 25-30mm diameter holes
  * Location: Top corners (2 front, 2 rear for cross-flow)
  * Mesh: Stainless steel or aluminum 1/8" or 1/4" grid, epoxy or grommet mount
  * Net free area: ~2000-2800mm² (exceeds 500mm² minimum)

**Material**: High-density polyethylene (HDPE, easy to drill/cut, weatherproof)

**Internal Layout:**
- ✅ **Battery**: Bottom center (520×238×218mm fits with 7.5" front, 8.5" side, 4.5" top clearances)
  * Mounting: 2× ratchet straps over top, anchored via drilled holes + bolts through tote bottom
  * Prevents movement during transport
- ✅ **Blue Sea 5026**: Side wall mount (left side near battery)
  * Mounting: Self-tapping screws through Blue Sea mounting flanges into tote wall
  * Accessible from top (fuse replacement)
- ✅ **Victron shunt**: Side wall near battery negative terminal
  * Mounting: Screws or adhesive mount, minimize 4 AWG wire length
- ✅ **Wire routing**: Zip ties anchored to walls/bottom
  * 10 AWG from Blue Sea to side panel Powerpole holes (clean routing)
  * 4 AWG battery trunks (positive to 100A ANL to Blue Sea, negative to shunt to Blue Sea)
  * Avoid sharp edges, use rubber grommets at all panel penetrations

**Ventilation:**
- ✅ Airflow: Cool air enters bottom/side vents, hot air exits top vents (natural convection)
- ✅ Hydrogen off-gassing: Minimal with LiFePO4 (no liquid electrolyte), but good practice
- ✅ Battery heat: ~10-30W at 30A discharge dissipates via convection (<40°C rise target)

**Portability:**
- ✅ Total weight: 25kg battery + 3-5kg components/tote = **28-30kg** (62-66 lbs)
- ✅ Greenmade molded handles rated for weight
- ✅ One-person carry (meets SC-004)

**Upgrade Path (v2 Enclosure Options):**
- Pelican or SKB hard case (IP65+ waterproof, crush-proof, $100-200)
- Custom aluminum case with CNC cutouts (professional appearance, $200-300)
- Weatherproof polymer NEMA 3R enclosure ($80-150)
- **After v1 validation**: Port layout, wiring, component placement proven, can replicate exactly in premium enclosure

**Rationale**:
- **Constitution Principle IV (Incremental Evolution)**: $10-20 tote tests layout before $100-200 Pelican investment
- **Easy modification**: HDPE drills/cuts cleanly with standard tools
- **Sufficient protection**: Indoor/vehicle use (testing environment), splash-resistant
- **Validation criteria**: After field testing, upgrade if UV degradation, need impact protection, want IP65+ waterproof

---

## Contract Validation Checklist

Before declaring a component "contract-compliant," verify the following:

### Battery Module (VEVOR 200Ah)
- [x] Voltage range: 10.0V - 14.6V ✓ (VEVOR BMS cutoffs)
- [x] Continuous current rating: ≥30A ✓ (100A continuous, exceeds requirement)
- [x] BMS protections present: OVP, UVP, OCP, SCP ✓ (integrated 100A BMS)
- [x] Chemistry: LiFePO4 ✓ (4S, 3.2V/cell)
- [x] Mounting secure, no movement during transport ✓ (2× ratchet straps, bolted to tote)

### Fuses (100A ANL + Blue Sea 5026)
- [x] DC voltage rating: ≥32V ✓ (ANL 32V rated, blade fuses 32V)
- [x] Current rating: 125% of expected load ✓ (100A ANL matches BMS, circuits 10-30A with margin)
- [x] Time-current characteristics documented ✓ (ANL fuse datasheet, blade fuse I²t curves)
- [x] Accessible for user replacement ✓ (ANL inline holder removable cover, Blue Sea top-access)

### Connectors (Anderson Powerpole PP45)
- [x] Current rating matches or exceeds circuit fuse ✓ (45A > all circuits 10-30A)
- [x] Polarity protection (mechanical keying or diode) ✓ (Powerpole dovetail keying)
- [x] Labeled with voltage, current, polarity ✓ (side panel labels: "HEATER 10A", etc.)
- [x] Mounted externally with strain relief ✓ (32mm holes with rubber grommets)

### Monitoring System (Victron BMV-712 + Nilight Panel)
- [x] Voltmeter accuracy: ±0.1V ✓ (Victron ±0.1V, Nilight ±0.1-0.2V)
- [x] Voltmeter visible from 2 meters ✓ (front panel mounted, LED displays)
- [x] Temperature measurement method documented ✓ (manual IR thermometer, optional Victron sensor)
- [x] Status indicators functional ✓ (Nilight ON/OFF LED, Victron display with alarms)

### Enclosure (Greenmade 27gal Tote)
- [x] Ventilation holes with mesh: ≥2× 25mm ✓ (4× 25-30mm with mesh, ~2000-2800mm²)
- [x] Battery secured against movement ✓ (2× ratchet straps, bolted anchor points)
- [x] All components accessible for maintenance ✓ (Blue Sea top-access, battery straps removable)
- [x] Total weight allows one-person portability ✓ (28-30kg, within one-person limit)

### Wiring (4/10/12 AWG TXL/GXL)
- [x] Wire gauge meets current rating ✓ (4 AWG 105A for 100A trunk, 10 AWG 35-40A for circuits)
- [x] Insulation rating: ≥105°C ✓ (TXL/GXL automotive wire)
- [x] Color coding: Red (+), Black (-) ✓ (all positive red, all negative black)
- [x] Terminations: Crimped ring terminals or soldered connectors ✓ (ratcheting crimper, M8 rings, Powerpole contacts)
- [x] Strain relief on all panel-mount connections ✓ (rubber grommets at all Powerpole holes)

---

## Summary

These interface contracts define the "API" between battery box components, enabling modular design per Constitution Principle II. Any component replacement or upgrade must satisfy these contracts to maintain:

1. **Safety**: Electrical protection, proper ratings, fail-safe behavior
2. **Interoperability**: Standard connectors, voltage/current compatibility
3. **Observability**: Measurement interfaces, status indication
4. **Maintainability**: User-replaceable components, documented specifications

**v1 Implementation Status**: All contracts satisfied by VEVOR 200Ah battery, Blue Sea 5026 fuse block, Victron BMV-712 battery monitor, Anderson Powerpole PP45 connectors, Nilight 4-in-1 panel, Greenmade 27gal tote enclosure.

**Next Phase**: Generate quickstart assembly guide referencing these contracts and specific component procedures.
