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

---

## Contract Validation Checklist

Before declaring a component "contract-compliant," verify the following:

### Battery Module
- [ ] Voltage range: 10.0V - 14.6V ✓
- [ ] Continuous current rating: ≥30A ✓
- [ ] BMS protections present: OVP, UVP, OCP, SCP ✓
- [ ] Chemistry: LiFePO4 ✓
- [ ] Mounting secure, no movement during transport ✓

### Fuses
- [ ] DC voltage rating: ≥32V ✓
- [ ] Current rating: 125% of expected load ✓
- [ ] Time-current characteristics documented ✓
- [ ] Accessible for user replacement ✓

### Connectors (Output and Charging)
- [ ] Current rating matches or exceeds circuit fuse ✓
- [ ] Polarity protection (mechanical keying or diode) ✓
- [ ] Labeled with voltage, current, polarity ✓
- [ ] Mounted externally with strain relief ✓

### Monitoring System
- [ ] Voltmeter accuracy: ±0.1V ✓
- [ ] Voltmeter visible from 2 meters ✓
- [ ] Temperature measurement method documented ✓
- [ ] Status LEDs functional (power, low batt, charging) ✓

### Enclosure
- [ ] Ventilation holes with mesh: ≥2× 25mm ✓
- [ ] Battery secured against movement ✓
- [ ] All components accessible for maintenance ✓
- [ ] Total weight allows one-person portability ✓

### Wiring
- [ ] Wire gauge meets current rating ✓
- [ ] Insulation rating: ≥105°C ✓
- [ ] Color coding: Red (+), Black (-) ✓
- [ ] Terminations: Crimped ring terminals or soldered connectors ✓
- [ ] Strain relief on all panel-mount connections ✓

---

## Summary

These interface contracts define the "API" between battery box components, enabling modular design per Constitution Principle II. Any component replacement or upgrade must satisfy these contracts to maintain:

1. **Safety**: Electrical protection, proper ratings, fail-safe behavior
2. **Interoperability**: Standard connectors, voltage/current compatibility
3. **Observability**: Measurement interfaces, status indication
4. **Maintainability**: User-replaceable components, documented specifications

**Next Phase**: Generate quickstart assembly guide referencing these contracts.
