# Quickstart Guide: Battery Box v1 Build

**Purpose**: Step-by-step guide for assembling and validating the battery box  
**Prerequisites**: All components procured per [component-interfaces.md](contracts/component-interfaces.md)  
**Safety**: Read entire guide before starting; follow all electrical safety practices  
**Created**: 2026-01-18

---

## Table of Contents

1. [Safety Precautions](#1-safety-precautions)
2. [Tools and Materials](#2-tools-and-materials)
3. [Component Checklist](#3-component-checklist)
4. [Assembly Steps](#4-assembly-steps)
5. [Wiring Diagram](#5-wiring-diagram)
6. [Testing and Validation](#6-testing-and-validation)
7. [Operating Instructions](#7-operating-instructions)
8. [Troubleshooting](#8-troubleshooting)

---

## 1. Safety Precautions

**⚠️ CRITICAL SAFETY WARNINGS**

- **Electrical Shock**: 12V batteries can deliver hundreds of amps - capable of welding metal, melting wires, and causing burns
- **Fire Risk**: Short circuits cause sparks and extreme heat - keep flammable materials away
- **Battery Hazards**: LiFePO4 batteries are safer than other lithium chemistries but can still vent or swell if damaged
- **Tools**: Always use insulated tools when working near battery terminals
- **Jewelry**: Remove rings, watches, bracelets - metal can bridge terminals

**Before Starting:**
- [ ] Read all instructions completely
- [ ] Work in well-ventilated area
- [ ] Have fire extinguisher nearby (Class D or ABC)
- [ ] Wear safety glasses
- [ ] Battery disconnected or terminals covered until ready to wire

**During Build:**
- [ ] Double-check polarity before making connections
- [ ] Verify no metal objects (screws, washers, tools) can bridge terminals
- [ ] Test continuity with multimeter, not by sparking
- [ ] Install fuses LAST (after all wiring complete)

---

## 2. Tools and Materials

### Required Tools

- **Multimeter**: Digital, measures DC voltage (10-20V range) and continuity
- **Wire strippers**: For AWG wire sizes in use (typically 10-16 AWG)
- **Crimping tool**: Ratcheting crimper for ring terminals and connectors
- **Screwdrivers**: Phillips and flathead, various sizes
- **Drill** (if enclosure requires cutouts): Variable speed with step drill bits or hole saw
- **Deburring tool**: Remove sharp edges from drilled holes
- **Heat gun** (optional): For heat-shrink tubing
- **Adjustable wrench or socket set**: For battery terminal bolts (typically 10mm)

### Consumable Materials

- **Wire**: TXL or GXL automotive wire, 105°C rated
  - 10 AWG red (main positive): 1-2 meters
  - 10 AWG black (main negative): 1-2 meters
  - 14 AWG red/black (circuit wiring): As needed per output count
- **Ring terminals**: Sized for wire gauge and terminal post (M6 or M8)
- **Heat-shrink tubing**: Various sizes for insulation
- **Zip ties**: Cable management inside enclosure
- **Adhesive foam padding**: Battery mounting (optional, anti-vibration)
- **Electrical tape**: Temporary insulation, wire bundling
- **Labels**: Wire labels, terminal labels (label maker or write-on labels)

### Specialized Parts (from Component List)

See [Section 3: Component Checklist](#3-component-checklist)

---

## 3. Component Checklist

Verify all components before starting assembly:

### Core Components
- [ ] **Battery**: 12V LiFePO4, 50Ah+ capacity, integrated BMS
- [ ] **Enclosure**: Weatherproof case or plywood box with ventilation
- [ ] **Main Fuse**: ANL or Mega fuse, 50-100A (based on battery rating)
- [ ] **Main Fuse Holder**: Inline ANL holder or fuse block
- [ ] **Circuit Fuses**: Blade ATO/ATC fuses (10A, 15A, 20A, 30A - as needed)
- [ ] **Circuit Fuse Holders**: Inline blade holders or panel-mount blocks

### Connectors
- [ ] **Output Connectors**: Anderson Powerpole PP45 or XT60 (qty per output count)
- [ ] **Charging Connector**: Anderson Powerpole PP30/45 or XT60 (input side)
- [ ] **Panel-mount plates** (if using): For mounting connectors to enclosure

### Monitoring Components
- [ ] **Digital Voltmeter**: Panel-mount, 5-30V range, LED display
- [ ] **Temperature Sensor**: DS18B20 or 10K NTC thermistor (optional for v1)
- [ ] **Status LEDs**: 10mm LEDs - 1× green, 1× yellow, 1× red
- [ ] **LED bezels**: Panel-mount bezels for LEDs
- [ ] **Voltage comparator ICs or transistors**: For LED trigger circuits (or pre-built LED modules)
- [ ] **Resistors**: Current limiting for LEDs (680Ω-1kΩ typical)

### Hardware
- [ ] **Bolts/screws**: For battery mounting, component mounting
- [ ] **Standoffs**: For mounting fuse holders, circuit boards
- [ ] **Cable glands or grommets**: Strain relief for panel penetrations
- [ ] **Mesh screen**: Cover ventilation holes (stainless or plastic)

### External Equipment (Not in Enclosure)
- [ ] **AC Charger**: LiFePO4-compatible, 10A+ output, compatible connector
- [ ] **Test load**: Resistive load or device for testing (12V automotive bulb, heater, etc.)

---

## 4. Assembly Steps

### Step 1: Prepare Enclosure

**1.1 Plan component layout**
- Sketch layout on paper: battery position, connector locations, meter position
- Battery at bottom (low center of gravity)
- Connectors on side or front panel (cable access)
- Voltmeter and LEDs on front panel (visibility)

**1.2 Mark and drill cutouts**
- [ ] Mark voltmeter cutout location (check clearance behind panel for depth)
- [ ] Mark LED holes (5mm or 10mm, depending on LED size)
- [ ] Mark output connector holes (15-25mm depending on connector type)
- [ ] Mark charging connector hole (separate from outputs)
- [ ] Mark ventilation holes: 2× 25mm (1 inch) - one high, one low

**1.3 Drill holes**
- [ ] Use step drill or hole saw for large holes
- [ ] Deburr all holes (remove sharp edges with deburring tool or sandpaper)
- [ ] Test-fit components before proceeding

**1.4 Install ventilation mesh**
- [ ] Cut mesh to cover ventilation holes with 10mm overlap
- [ ] Secure with hot glue, epoxy, or small screws/washers

### Step 2: Mount Battery

**2.1 Position battery**
- [ ] Place battery in enclosure (centered, at bottom)
- [ ] Ensure clearance for wiring and components around battery

**2.2 Secure battery**
- [ ] Option A: Ratchet straps across top of battery (secure to enclosure mounting points)
- [ ] Option B: Foam padding on sides + friction fit (if tight fit)
- [ ] Option C: Mounting brackets bolted to enclosure floor (if battery has mounting holes)
- [ ] Verify battery cannot move when enclosure tilted or shaken

### Step 3: Install Main Fuse Holder

**3.1 Mount fuse holder**
- [ ] Position inline ANL fuse holder near battery positive terminal (within 18 inches per best practice)
- [ ] Secure with zip ties or mounting bracket
- [ ] **DO NOT install fuse yet** (fuse installed last after all wiring complete)

**3.2 Prepare wiring**
- [ ] Cut 10 AWG red wire: Battery positive → Fuse holder input (short, ~150mm)
- [ ] Strip wire ends 10mm
- [ ] Crimp ring terminal on battery end (M6 or M8 to match battery post)
- [ ] Crimp fuse holder terminal on other end (or ring terminal if fuse holder has stud)

### Step 4: Install Distribution Busbar (Optional but Recommended)

**4.1 Busbar option**
- [ ] If multiple outputs: Install busbar (terminal strip) downstream of main fuse
- [ ] Busbar simplifies wiring: Main fuse → Busbar → Individual circuits branch off
- [ ] Alternative: Daisy-chain circuits (more complex wiring)

**4.2 Mount busbar**
- [ ] Secure busbar to enclosure with standoffs or brackets
- [ ] Position centrally for equal wire run lengths to each circuit

### Step 5: Wire Output Circuits

**For each output circuit:**

**5.1 Install circuit fuse holder**
- [ ] Inline blade fuse holder or panel-mount holder
- [ ] Position near busbar (or main fuse output if no busbar)
- [ ] **DO NOT install fuse yet**

**5.2 Positive wire run**
- [ ] Cut red wire: Busbar → Fuse holder input (appropriate length)
- [ ] Busbar end: Ring terminal
- [ ] Fuse holder end: Blade terminal or ring terminal

**5.3 Fuse holder to connector**
- [ ] Cut red wire: Fuse holder output → Output connector positive
- [ ] Crimp Anderson Powerpole contacts or solder XT60 connector
- [ ] Route wire through cable gland (strain relief)

**5.4 Negative wire run**
- [ ] Cut black wire: Battery negative → Output connector negative
- [ ] Battery end: Ring terminal (M6/M8 to match battery post)
- [ ] Connector end: Crimp Anderson Powerpole or solder XT60
- [ ] Route through same cable gland as positive wire

**5.5 Label wires**
- [ ] Label each wire at both ends: "OUT1+", "OUT1-", "OUT2+", "OUT2-", etc.
- [ ] Use wire labels or write on heat-shrink with marker

### Step 6: Wire Charging Circuit

**6.1 Charging fuse holder**
- [ ] Install inline blade fuse holder near battery (separate from output circuits)
- [ ] **DO NOT install fuse yet**

**6.2 Positive wire run**
- [ ] Cut red wire: Battery positive (via busbar or direct) → Charge fuse holder input
- [ ] Fuse holder output → Charge connector positive
- [ ] Crimp/solder connector, route through cable gland

**6.3 Negative wire run**
- [ ] Cut black wire: Battery negative → Charge connector negative
- [ ] Crimp/solder connector, route through same cable gland as positive

**6.4 Reverse polarity protection (if not in charger)**
- [ ] Option A: Schottky diode in series with positive wire (cathode toward battery)
  - Diode rating: 30A+, voltage drop ~0.3-0.5V
- [ ] Option B: MOSFET-based protection circuit (more complex, no voltage drop)
- [ ] If charger has reverse polarity protection and connector is keyed, this may be optional

**6.5 Label wires**
- [ ] Label: "CHG_IN+", "CHG_IN-"

### Step 7: Install Voltage Meter

**7.1 Mount meter**
- [ ] Insert panel meter into cutout from front
- [ ] Secure with mounting clips or bezel (per meter design)

**7.2 Wire meter**
- [ ] Red wire (meter V+): Connect to battery positive (via busbar or solder to positive wire near battery)
- [ ] Black wire (meter V- or GND): Connect to battery negative (solder to negative wire or ring terminal at battery)
- [ ] Wire gauge: 18-22 AWG sufficient (low current)
- [ ] Keep wire runs short to minimize voltage drop in sense lines

### Step 8: Install Status LEDs

**8.1 Mount LEDs**
- [ ] Insert LEDs into bezels, insert bezels into panel holes
- [ ] Secure (snap-fit or threaded bezel, depending on type)
- [ ] Position: Green (Power) | Yellow (Low Batt) | Red (Charging)

**8.2 Build LED trigger circuits**

#### Simple transistor-based LED driver (per LED):

**Power LED (Green, ON when voltage >13.0V):**
```
Battery+ (>13.0V) ───┬─── Resistor (e.g., 680Ω) ───┬─── Green LED (+) ─── Transistor (NPN, collector) ─── GND
                     │                               └─── Anode
                     └─── Voltage divider: R1 (10kΩ) ─── Zener 13V ─── R2 (10kΩ) ─── GND
                              (Tap after Zener) ──── Transistor Base

(When voltage >13V, Zener conducts, base goes high, transistor turns on, LED lights)
```

**Alternative: Use LM339 voltage comparator IC** (more accurate, 4 comparators per IC)
- Set reference voltage with voltage divider
- Connect battery voltage to comparator input
- Comparator output drives LED (via transistor or directly if comparator can sink LED current)

**Note**: If building trigger circuits is too complex for v1, consider:
- **Option A**: Always-on LEDs with manual interpretation (e.g., one LED always shows voltage meter, user interprets)
- **Option B**: Pre-built LED voltage indicator modules (available online, configurable thresholds)
- **Deferred**: Full LED circuit to future enhancement if time-constrained

**8.3 Wire LEDs to battery**
- [ ] Connect LED trigger circuit power to battery positive and negative
- [ ] Verify polarity: LED anode (+) to current-limiting resistor, cathode (-) to ground or transistor

### Step 9: Install Panel Connectors

**9.1 Mount connector plates**
- [ ] If using Anderson Powerpole: Mount connector housings in panel holes (may need custom plate or 3D-printed mount)
- [ ] If using XT connectors: Solder to wires, secure with cable gland and strain relief

**9.2 External labeling**
- [ ] Label each output connector: "OUT1: 12V 30A MAX" (or appropriate rating)
- [ ] Label charge connector: "CHARGE INPUT: 14.4V LiFePO4 ONLY"
- [ ] Use label maker, engraving, or permanent marker

### Step 10: Final Wiring Check (Before Installing Fuses)

**10.1 Visual inspection**
- [ ] All connections tight (ring terminals torqued per spec)
- [ ] No bare wire exposed (heat-shrink or electrical tape on all joints)
- [ ] No wires touching sharp edges (use grommets or edge protection)
- [ ] All wires secured with zip ties (no loose wires that can vibrate)
- [ ] Polarity correct: Red = positive, Black = negative

**10.2 Continuity testing (battery disconnected or fuses out)**
- [ ] Multimeter in continuity/resistance mode
- [ ] Test positive wire continuity: Battery positive terminal → Each output connector positive pin
  - **Expected**: Open circuit (infinite resistance) with fuse NOT installed
  - **Expected**: Low resistance (<1 ohm) with fuse installed (test with spare fuse temporarily)
- [ ] Test negative wire continuity: Battery negative terminal → Each output connector negative pin
  - **Expected**: Low resistance (<1 ohm), continuity beep
- [ ] Test for shorts: Positive bus → Negative bus
  - **Expected**: Open circuit (infinite resistance, no continuity)
  - **If short detected**: Find and fix before proceeding

### Step 11: Install Fuses (LAST STEP)

**11.1 Install main fuse**
- [ ] Insert appropriately rated ANL fuse into main fuse holder
- [ ] Verify fuse is secure (seated fully in holder)

**11.2 Install circuit fuses**
- [ ] Insert appropriately rated blade fuses into each circuit fuse holder
- [ ] Start with lower-rated fuses (e.g., 10A) for initial testing

**11.3 Final check**
- [ ] All fuse holders closed and secured
- [ ] No exposed fuse terminals (should be covered by holder body)

---

## 5. Wiring Diagram

### Simplified Schematic

```
                 ┌──────────────────────────────────────────────────┐
                 │  12V LiFePO4 Battery (with integrated BMS)       │
                 │  Nominal: 12.8V | Range: 10.0V - 14.6V           │
                 └────────┬─────────────────────┬───────────────────┘
                          │ (+)                 │ (-)
                          │                     │
                    ┌─────▼─────┐               │
                    │ Main Fuse │               │
                    │  (ANL 50A)│               │
                    └─────┬─────┘               │
                          │                     │
            ┌─────────────┴──────────────┐      │
            │    Positive Busbar         │      │
            │  (Distribution Point)      │      │
            └─┬────────┬─────────┬───────┘      │
              │        │         │              │
       ───────┼────────┼─────────┼──────────────┼─────── Negative Busbar (Battery -)
              │        │         │              │
         ┌────▼───┐ ┌──▼────┐ ┌─▼──────┐       │
         │Fuse 30A│ │Fuse   │ │ Charge │       │
         │        │ │20A    │ │ Fuse   │       │
         └────┬───┘ └──┬────┘ │ 20A    │       │
              │        │      └─┬──────┘       │
              │        │        │              │
         ┌────▼─────┐  │        │              │
         │  OUT1    │  │   ┌────▼────────┐     │
         │Anderson  │  │   │  CHG INPUT  │     │
         │PP45      │  │   │Anderson PP30│     │
         │12V 30A   ├──┼───┤12V 20A      ├─────┘
         └──────────┘  │   └─────────────┘
                       │
                  ┌────▼─────┐
                  │  OUT2    │
                  │XT60      │
                  │12V 20A   ├────┘
                  └──────────┘

         ┌─────────────────────────────────┐
         │   Voltmeter (Panel Mount)        │
         │   Sense: Bat+ and Bat-           │
         │   Display: 12.8V                 │
         └─────────────────────────────────┘

         ┌───────┬───────┬────────┐
         │ LED   │ LED   │  LED   │
         │Green  │Yellow │ Red    │
         │Power  │LowBatt│Charging│
         └───────┴───────┴────────┘
         (Trigger circuits powered from Bat+/-)
```

### Physical Layout (Top View of Enclosure)

```
┌───────────────────────────────────────────────────────────┐
│                    FRONT PANEL                             │
│                                                            │
│  [ Voltmeter ]   [LED] [LED] [LED]                        │
│    Display       Power LowBt Chrg                         │
│                                                            │
│  [OUT1]  [OUT2]  [CHG_IN]                                 │
│  PP45    XT60    PP30                                     │
│  Label   Label   Label                                    │
└───────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────┐
│                    INTERIOR (Top View)                     │
│                                                            │
│  [Main Fuse] ─┬─ [Busbar] ─┬─ [Fuse Block]               │
│               │             │   OUT1 OUT2 CHG             │
│               │             │                             │
│  ┌────────────┴─────────────┴───────────────┐            │
│  │                                            │            │
│  │        Battery (12V LiFePO4 100Ah)        │            │
│  │                                            │            │
│  │         (Secured with strap)               │            │
│  └────────────────────────────────────────────┘            │
│                                                            │
│  [Vent Hole]                       [Vent Hole]            │
│  (Bottom)                          (Top)                  │
└───────────────────────────────────────────────────────────┘
```

---

## 6. Testing and Validation

### Phase 1: Pre-Power Checks (Fuses Not Installed)

**6.1 Visual inspection**
- [ ] All connections secure, no loose wires
- [ ] No shorts visible (wires not touching opposite polarity)
- [ ] Polarity correct throughout (red = +, black = -)

**6.2 Continuity testing**
- [ ] Battery positive to each output positive (with temporary fuse): Low resistance
- [ ] Battery negative to each output negative: Low resistance
- [ ] Positive bus to negative bus: Open circuit (no short)

### Phase 2: Initial Power-Up (Low-Risk Loads Only)

**6.3 Install main fuse**
- [ ] Insert main fuse, close holder

**6.4 Check voltmeter**
- [ ] Voltmeter powers on and displays voltage
- [ ] Voltage reading reasonable (12.0V - 13.5V for partially charged LiFePO4)
- [ ] Compare to multimeter at battery terminals: Should be within ±0.1V per SC-002

**6.5 Check status LEDs**
- [ ] Power LED (green): Lit if voltage >13.0V, off if <13.0V
- [ ] Low Battery LED (yellow): Lit if voltage <13.0V, off if >13.0V
- [ ] Charging LED (red): Off (no charger connected)
- If LEDs not functioning as expected, troubleshoot trigger circuits

**6.6 Install output circuit fuses**
- [ ] Start with lowest-rated fuses (10A) for initial testing
- [ ] Insert fuses into each output circuit holder

### Phase 3: Load Testing

**6.7 Connect test load (light load first)**
- [ ] Use 12V automotive bulb (5-10W) or resistive load (~1A)
- [ ] Connect to output connector, verify polarity
- [ ] Load should operate (bulb lights)
- [ ] Monitor voltage: Should drop slightly under load but remain >11.5V

**6.8 Increase load gradually**
- [ ] Disconnect light load
- [ ] Connect moderate load (10A - e.g., 12V fan, small heater)
- [ ] Monitor voltage: Should remain stable (voltage sag <0.5V)
- [ ] Monitor temperature: Feel battery case, should be slightly warm but not hot
- [ ] Run for 10 minutes, observe voltmeter for voltage drop over time

**6.9 Heavy load test (if system designed for high current)**
- [ ] Connect 20-30A load (e.g., diesel heater, large inverter)
- [ ] Monitor voltage and temperature closely
- [ ] Run for 5-10 minutes maximum (or until voltage drops to 12.5V)
- [ ] Battery temperature should remain <40°C per SC-006

**6.10 Overcurrent protection test (fuse validation)**
- [ ] Install test fuse (e.g., 10A blade fuse)
- [ ] Gradually increase load beyond fuse rating (use variable resistive load or multiple devices)
- [ ] Fuse should open (blow) when current exceeds rating per manufacturer time-current curve
- [ ] Verify no damage to wiring or battery after fuse opens
- [ ] Replace test fuse with correct rating for circuit

### Phase 4: Charging Validation

**6.11 Connect AC charger**
- [ ] Verify charger is set to LiFePO4 mode (if selectable)
- [ ] Connect charger to AC mains (120V outlet)
- [ ] Connect charger to battery box charge input
- [ ] Verify polarity: Red to red, black to black (or keyed connector)

**6.12 Monitor charging process**
- [ ] Voltmeter should show rising voltage (starting from current SOC voltage)
- [ ] Charging LED (red) should illuminate when voltage >14.0V
- [ ] Monitor battery temperature: Should remain <40°C during charging
- [ ] Allow to charge for 1-2 hours (or until voltage reaches 14.4V)

**6.13 Charge termination**
- [ ] When battery reaches 14.4V, charger should reduce current (constant voltage phase)
- [ ] Voltage may plateau or rise slowly to 14.6V, then charger should terminate or float at 13.6V
- [ ] Disconnect charger after full charge observed
- [ ] Charging LED should turn off when charger disconnected (voltage drops below 14.0V)

### Phase 5: Runtime Validation

**6.14 Full discharge test (optional, time-consuming)**
- [ ] Fully charge battery (14.4V)
- [ ] Connect 10A constant load
- [ ] Record start time and voltage
- [ ] Monitor voltage every 30 minutes, log in test results document
- [ ] Low Battery LED should illuminate when voltage drops below 13.0V (~20% SOC)
- [ ] Disconnect load when voltage reaches 12.0V (avoid BMS cutoff for this test)
- [ ] Calculate runtime: Should achieve ~8+ hours for 100Ah battery per SC-001

**6.15 Document results**
- [ ] Record all test outcomes in `docs/test-results.md`
- [ ] Include: date, ambient temperature, load used, voltage readings, pass/fail status
- [ ] Note any anomalies or observations

---

## 7. Operating Instructions

### Daily/Pre-Use Checks

Before using battery box:
- [ ] Check voltmeter: Voltage should be >12.5V (indicates adequate charge)
- [ ] Verify Power LED is green (system operational)
- [ ] If Yellow LED lit (low battery), recharge before extended use
- [ ] Check enclosure: No damage, ventilation holes clear

### Connecting Loads

1. **Verify load voltage**: Ensure device is rated for 12V DC
2. **Check load current**: Should not exceed output circuit fuse rating
3. **Connect load to output**: Red to positive, black to negative (or use keyed connector)
4. **Turn on load**: Device should operate normally
5. **Monitor voltage**: Voltmeter should remain >11.5V under load
6. **If voltage drops rapidly**: Load may exceed battery capacity or battery is discharged

### Charging Procedure

1. **Disconnect loads**: Remove or turn off all connected devices
2. **Connect charger to AC**: Plug charger into 120V outlet
3. **Connect charger to battery box**: Red to charge input red, black to black
4. **Observe charging LED**: Should illuminate red (voltage >14.0V)
5. **Allow to charge**: Typically 4-10 hours depending on discharge depth and charger current
6. **Disconnect when complete**: Unplug charger from battery box, then from AC outlet

### Monitoring Battery Health

- **Check voltage at rest** (no load, no charging for 10+ minutes):
  - 13.4V or higher = Good charge (80-100% SOC)
  - 13.0V - 13.3V = Moderate charge (20-80% SOC)
  - 12.5V - 12.9V = Low charge (10-20% SOC)
  - <12.5V = Very low, recharge immediately
- **Check temperature**: Feel battery case, should be cool to warm (not hot >40°C)
- **If BMS triggers**: All outputs dead, voltmeter may be off
  - Cause: Over-discharge (<10V), overcurrent, or over-temperature
  - Remedy: Disconnect load, allow battery to rest, recharge

### Storage Guidelines

- **Short-term storage** (days to weeks):
  - Charge to 50-70% SOC (13.2V - 13.4V)
  - Disconnect all loads
  - Store in cool, dry location (15-25°C)
- **Long-term storage** (months):
  - Charge to 50-60% SOC (13.2V - 13.3V)
  - Check voltage monthly, recharge if <13.0V
  - Do not store fully discharged (<12.0V) - causes permanent capacity loss

---

## 8. Troubleshooting

### Issue: Voltmeter Not Displaying

**Possible Causes:**
- Battery voltage too low (<5V, BMS cutoff)
- Voltmeter wiring disconnected
- Voltmeter damaged

**Troubleshooting Steps:**
1. Use external multimeter to measure battery voltage at terminals
2. If battery voltage >11V, check voltmeter wiring connections (sense wires to battery)
3. If wiring intact, voltmeter may be defective - replace

---

### Issue: No Power at Outputs (Voltmeter Shows Voltage)

**Possible Causes:**
- Fuse blown
- BMS protection triggered
- Wiring fault

**Troubleshooting Steps:**
1. Check main fuse: Remove and inspect, replace if blown
2. Check output circuit fuse: Remove and inspect, replace if blown
3. If fuses intact, use multimeter to check voltage at output connector pins
   - If voltage present: Connector or load issue
   - If no voltage: Wiring fault, trace circuit

---

### Issue: Low Battery LED Always On (Even When Charged)

**Possible Causes:**
- LED trigger circuit threshold incorrectly set
- Voltage sensing issue

**Troubleshooting Steps:**
1. Check battery voltage with multimeter: Should be >13.0V when charged
2. If voltage >13.0V but LED still on: LED trigger circuit needs adjustment (adjust voltage divider or comparator threshold)
3. If LED circuit too complex to fix, consider always-on LED with manual voltage interpretation

---

### Issue: Charging LED Not Illuminating When Charger Connected

**Possible Causes:**
- Charger not outputting voltage
- LED trigger circuit threshold incorrect
- Wiring fault

**Troubleshooting Steps:**
1. Check voltage at charge input connector: Should be >14.0V when charger active
2. If voltage >14.0V but LED not lit: LED trigger circuit needs adjustment
3. If no voltage at charge input: Check charger function, verify charger connected to AC and battery box

---

### Issue: Fuse Blows Immediately When Load Connected

**Possible Causes:**
- Short circuit in load or wiring
- Load current exceeds fuse rating

**Troubleshooting Steps:**
1. Disconnect load, replace fuse
2. Use multimeter in continuity mode: Check load for short (positive to negative, should be open or high resistance)
3. If load is shorted, do not reconnect (repair or replace load)
4. If load is OK, check if load current exceeds fuse rating (measure with clamp meter or calculate P=VI)
5. If load current is higher than fuse rating, install higher-rated fuse (ensure wire gauge supports higher current)

---

### Issue: Battery Temperature Exceeds 40°C

**Possible Causes:**
- High discharge current (>50A)
- High ambient temperature
- Insufficient ventilation

**Troubleshooting Steps:**
1. Reduce load current (disconnect high-power devices)
2. Improve ventilation (add larger vent holes, add fan if necessary)
3. Allow battery to cool before resuming use
4. If temperature repeatedly exceeds 40°C under normal use: Battery may be undersized for application

---

### Issue: Voltage Drops Rapidly Under Load

**Possible Causes:**
- Battery discharged (low SOC)
- Battery capacity degraded (end of life)
- Load current too high for battery

**Troubleshooting Steps:**
1. Check resting voltage (no load): Should be >12.8V if charged
2. If resting voltage is low (<12.8V), recharge battery
3. If resting voltage is OK but drops rapidly under load: Battery internal resistance may be high (degraded), or load current exceeds battery rating
4. Test with lighter load (5-10A): If voltage stable with light load, battery may need replacement or load is too high

---

## Appendix A: Voltage-to-SOC Lookup Table (LiFePO4)

| Resting Voltage (no load, 10+ min) | Approximate SOC | Status         |
|-------------------------------------|-----------------|----------------|
| 14.6V                               | 100% (charging) | Fully charged  |
| 14.0V - 14.4V                       | 100%            | Fully charged  |
| 13.4V                               | 90%             | Good           |
| 13.3V                               | 70%             | Good           |
| 13.2V                               | 40%             | Moderate       |
| 13.0V                               | 20%             | Low (recharge) |
| 12.8V                               | 10%             | Very low       |
| 12.0V                               | 5%              | Critical       |
| <11.0V                              | <5%             | BMS cutoff     |

**Note**: Under load, voltage will be lower due to voltage sag (internal resistance). SOC estimation from voltage is approximate (±10%).

---

## Appendix B: Component Replacement Procedure

If a component fails or needs upgrading, refer to [component-interfaces.md](contracts/component-interfaces.md) for interface contracts. Any replacement component must satisfy the electrical, mechanical, and behavioral contracts defined therein.

**Replacement Steps:**
1. Disconnect battery (or remove main fuse)
2. Remove failed component
3. Install replacement component meeting interface contract
4. Verify wiring polarity and connections
5. Test with multimeter (continuity, voltage)
6. Reinstall fuse and perform load testing per Section 6
7. Document replacement in `docs/component-specs.md`

---

## Completion Checklist

- [ ] All assembly steps completed
- [ ] All testing phases completed and passed
- [ ] Test results documented in `docs/test-results.md`
- [ ] Component specifications documented in `docs/component-specs.md`
- [ ] Wiring diagram created and stored in `docs/wiring-diagram.md` (or photo/scan)
- [ ] Operating instructions reviewed and understood
- [ ] Battery box ready for operational use per Constitution Principle V (Documented before Expanded)

**Congratulations! Battery Box v1 is complete and operational. Enjoy safe, portable DC power for your camping and mobile needs.**
