# Data Model: Battery Box v1

**Purpose**: Define physical components, their attributes, relationships, and state transitions  
**Created**: 2026-01-18  
**Feature**: [spec.md](spec.md) | [plan.md](plan.md) | [research.md](research.md)

## Component Entities

This data model describes the physical components of the battery box system, their specifications, and how they interact.

---

### 1. Battery Module

**Description**: Core energy storage component providing 12V DC power

**Attributes:**
- `chemistry`: String - "LiFePO4" (Lithium Iron Phosphate)
- `nominalVoltage`: Number - 12.8V (4 cells × 3.2V)
- `capacity`: Number - **200 Ah** (VEVOR model 010230251465)
- `maxContinuousCurrent`: Number - **100A** (per VEVOR BMS rating)
- `maxPulseCurrent`: Number - **120A** (estimated, short duration)
- `voltageRange`: Object
  - `max`: 14.6V (fully charged, per BMS cutoff)
  - `nominal`: 12.8V (resting voltage ~50% SOC)
  - `min`: 10.0V (BMS low-voltage cutoff)
  - `warningThreshold`: 13.0V (20% SOC, user warning via Victron alarm)
- `temperatureRange`: Object
  - `dischargeMin`: 0°C
  - `dischargeMax`: 45°C
  - `chargeMin`: 0°C (do not charge below freezing)
  - `chargeMax`: 45°C
  - `warningThreshold`: 40°C
- `cycleLife`: Number - 4000+ cycles to 80% capacity (per VEVOR spec)
- `weight`: Number - **25 kg** (55 lbs)
- `dimensions`: Object - **length: 520mm, width: 238mm, height: 218mm** (20.5" × 9.4" × 8.6")
- `manufacturer`: String - "VEVOR"
- `model`: String - "010230251465" (200Ah 12V LiFePO4)
- `terminalType`: String - "M8 threaded posts" (requires M8 ring terminals)
- `bmsIntegrated`: Boolean - **true** (100A BMS included)
- `serialNumber`: String (document upon receipt)
- `purchaseDate`: String - "2026-01-18"
- `purchasePrice`: Number - $450-550

**Relationships:**
- **Houses** → BMS (integrated 100A BMS)
- **Powers** → Output Circuits (via Blue Sea 5026 fuse block)
- **Charged by** → Charging Circuit (VEVOR 20A charger)
- **Monitored by** → Monitoring System (Victron BMV-712, Nilight panel)
- **Protected by** → Main Fuse (100A ANL)

**State Transitions:**
```
States: {charging, discharging, idle, fault}

Transitions:
  idle → charging: When charger connected and voltage rises above 13.5V
  charging → idle: When charger disconnected or voltage reaches 14.4V
  idle → discharging: When load connected and current flows
  discharging → idle: When load disconnected
  discharging → fault: When BMS triggers (under-voltage, over-current, over-temp)
  charging → fault: When BMS triggers (over-voltage, over-current, over-temp)
  fault → idle: Manual reset or BMS auto-recovery after fault cleared
```

---

### 2. Battery Management System (BMS)

**Description**: Protection and balancing system for LiFePO4 cells

**Attributes:**
- `type`: String - **"integrated"** (within VEVOR battery)
- `cellCount`: Number - **4** (for 12V system, 4S configuration)
- `maxContinuousCurrent`: Number - **100A** (VEVOR BMS rating)
- `balancingCurrent`: Number - **50-100mA** (estimated, typical for integrated BMS)
- `protections`: Array of Strings
  - "over-voltage" (**~14.6-14.8V**, disconnects charging)
  - "under-voltage" (**~10.0V**, disconnects loads)
  - "over-current-discharge" (**100A continuous**)
  - "over-current-charge" (**likely 30-50A limit**)
  - "over-temperature" (**~60-65°C cutoff**, internal sensor)
  - "short-circuit" (instant disconnection)
- `cutoffVoltages`: Object
  - `overVoltage`: **14.6V** (disconnect charging)
  - `underVoltage`: **10.0V** (disconnect loads)
- `temperatureSensor`: Boolean - **true** (BMS includes internal temp monitoring)
- `manufacturer`: String - **"VEVOR"** (integrated with battery)
- `model`: String - **"Integrated 100A BMS"** (part of battery module 010230251465)

**Relationships:**
- **Integrated with** → Battery Module (VEVOR 200Ah)
- **Protects** → Battery Module (primary protection layer)
- **Backed up by** → Main Fuse (100A ANL, secondary protection)
- **Backed up by** → Circuit Fuses (10-30A blade fuses, tertiary protection)

**State Transitions:**
```
States: {normal, balancing, protection_triggered}

Transitions:
  normal → balancing: During charging when cell voltage differences exceed threshold
  balancing → normal: When cells balanced (ΔV < 10mV)
  normal → protection_triggered: When any protection threshold exceeded
  protection_triggered → normal: Fault condition cleared and manual/auto reset
```

---

### 3. Enclosure

**Description**: Physical housing protecting battery and electrical components

**Attributes:**
- `material`: String - **"high-density polyethylene"** (HDPE, weatherproof plastic)
- `dimensions`: Object
  - `external`: **length: 30.4", width: 20.4", height: 14.7"** (772mm × 518mm × 373mm)
  - `internal`: **length: ~28", width: ~18", height: ~13"** (711mm × 457mm × 330mm, approximate)
- `weight`: Number - **~3-5 kg** empty (tote + components, excluding battery)
- `totalSystemWeight`: Number - **~28-30 kg** (including 25kg battery)
- `weatherproof`: Boolean - **true** (HDPE splash-resistant, not IP-rated submersible)
- `manufacturer`: String - **"Greenmade"**
- `model`: String - **"27-Gallon Professional Storage Tote"** (black/yellow)
- `features`: Array of Strings - ["snap-lock latches", "stackable", "molded handles", "recessed lid"]
- `purchasePrice`: Number - **$10-20** (from Walmart)
- `ventilationHoles`: Number - **4** (to be drilled, 25-30mm diameter)
- `holeDiameter`: Number - **25-30mm** (1 inch, with mesh screen)
- `meshCover`: Boolean - **true** (stainless/aluminum 1/8" or 1/4" grid, prevents debris)
- `handles`: Boolean - **true** (molded, rated for total weight)
- `cutouts`: Array of Objects
  - {`type`: "Nilight_panel", `dimensions`: "4-6\" × 2-3\"", `location`: "front panel center"}
  - {`type`: "Victron_display", `dimensions`: "52mm × 52mm square", `location`: "front panel right"}
  - {`type`: "Powerpole_outputs", `count`: 4-5, `diameter`: "32mm each", `location`: "side panel left, vertical row"}
  - {`type`: "ventilation", `count`: 4, `diameter`: "25-30mm", `location`: "top corners with mesh"}
- `mountingPoints`: Array of Objects
  - {`type`: "battery", `method`: "ratchet straps × 2", `location`: "bottom, anchored via drilled holes + bolts"}
  - {`type`: "fuse_block", `method`: "Blue Sea mounting flanges + self-tapping screws", `location`: "side wall"}
  - {`type`: "victron_shunt", `method`: "wall mount screws", `location`: "side wall near battery negative"}
  - {`type`: "wire_routing", `method`: "zip ties", `location`: "walls/bottom"}

**Battery Clearances** (Battery: 520×238×218mm in Tote: ~711×457×330mm internal):
- Length: 711mm - 520mm = **191mm (7.5")** front clearance
- Width: 457mm - 238mm = **219mm (8.6")** side clearance
- Height: 330mm - 218mm = **112mm (4.4")** top clearance

**Relationships:**
- **Contains** → Battery Module (VEVOR 200Ah), Protection Devices (Blue Sea 5026, 100A ANL), Monitoring System (Victron BMV-712, Nilight panel)
- **Provides access to** → Output Circuits (Anderson Powerpole panel mounts), Charging Circuit (Powerpole charge input)

**Physical Constraints:**
- Total weight (28-30 kg) within one-person carry limit (SC-004)
- Ventilation allows airflow without compromising splash protection
- Component mounting prevents movement during transport via ratchet straps + zip ties
- Modifications: Power tools required (drill, jigsaw/rotary tool, step bits, hole saws)

---

### 4. Output Circuit

**Description**: User-facing power delivery interface for connecting loads

**Blue Sea 5026 Circuit Allocation** (12 circuits, 6 allocated in v1):

**Circuit 1 - Charge Input**:
- `circuitID`: **"CHARGE_IN"** (Blue Sea circuit 1)
- `connectorType`: **"Anderson_Powerpole_PP45"** (with adapter cable from VEVOR charger alligator clips)
- `voltageRating`: 14.6V (charge voltage)
- `currentRating`: **20-30A** (VEVOR charger 20A nominal)
- `fuseRating`: **30A** blade fuse
- `fuseType`: **"ST_blade_ATO"**
- `wireGauge`: **10 AWG** (Blue Sea to charge input connector)
- `polarity`: {`positive`: "red", `negative`: "black"}
- `labelText`: **"CHARGE IN 30A"**

**Circuit 2 - Diesel Heater Output**:
- `circuitID`: **"HEATER_OUT"** (Blue Sea circuit 2)
- `connectorType`: **"Anderson_Powerpole_PP45"**
- `voltageRating`: 12V nominal
- `currentRating`: **10A** continuous
- `fuseRating`: **10A** blade fuse
- `fuseType`: **"ST_blade_ATO"**
- `wireGauge`: **10 AWG** (Blue Sea to Powerpole) + **12 AWG pigtail** (Powerpole contact)
- `wireLength`: **~18-24 inches** (Blue Sea to side panel Powerpole)
- `polarity`: {`positive`: "red", `negative`: "black"}
- `labelText`: **"HEATER 10A"**

**Circuit 3 - Fridge/Cooler Output**:
- `circuitID`: **"FRIDGE_OUT"** (Blue Sea circuit 3)
- `connectorType`: **"Anderson_Powerpole_PP45"**
- `voltageRating`: 12V nominal
- `currentRating`: **15A** continuous
- `fuseRating`: **15A** blade fuse
- `fuseType`: **"ST_blade_ATO"**
- `wireGauge`: **10 AWG** + **12 AWG pigtail**
- `wireLength`: **~18-24 inches**
- `polarity`: {`positive`: "red", `negative`: "black"}
- `labelText`: **"FRIDGE 15A"**

**Circuit 4 - USB/12V Panel (Nilight 4-in-1)**:
- `circuitID`: **"USB_PANEL"** (Blue Sea circuit 4)
- `connectorType`: **"Hardwired to Nilight panel"** (female spade terminals)
- `voltageRating`: 12V nominal
- `currentRating`: **20A** (USB-C PD 100W + USB-A + 12V outlet combined)
- `fuseRating`: **20A** blade fuse
- `fuseType`: **"ST_blade_ATO"**
- `wireGauge`: **10 AWG** (Blue Sea to Nilight)
- `features`: ["USB-C PD (100W)", "USB-A QC 3.0 (2.1A)", "12V cigarette outlet", "integrated voltmeter", "ON/OFF switch"]
- `polarity`: {`positive`: "red", `negative`: "black"}
- `labelText`: **"USB PANEL 20A"** (internal, Nilight front panel)

**Circuit 5 - Spare Output 1**:
- `circuitID`: **"SPARE_OUT_1"** (Blue Sea circuit 5)
- `connectorType`: **"Anderson_Powerpole_PP45"**
- `voltageRating`: 12V nominal
- `currentRating`: **20A** continuous (future: inverter, solar, lights)
- `fuseRating`: **20A** blade fuse
- `fuseType`: **"ST_blade_ATO"**
- `wireGauge`: **10 AWG** + **12 AWG pigtail**
- `wireLength`: **~18-24 inches**
- `polarity`: {`positive`: "red", `negative`: "black"}
- `labelText`: **"SPARE 20A"**

**Circuit 6 - Spare Output 2**:
- `circuitID`: **"SPARE_OUT_2"** (Blue Sea circuit 6)
- `connectorType`: **"Anderson_Powerpole_PP45"**
- `voltageRating`: 12V nominal
- `currentRating`: **15A** continuous
- `fuseRating`: **15A** blade fuse
- `fuseType`: **"ST_blade_ATO"**
- `wireGauge`: **10 AWG** + **12 AWG pigtail**
- `wireLength`: **~18-24 inches**
- `polarity`: {`positive`: "red", `negative`: "black"}
- `labelText`: **"SPARE 15A"**

**Circuits 7-12: Future Expansion** (Blue Sea terminals available, not wired in v1)

**Relationships:**
- **Powered by** → Battery Module (via 100A ANL Main Fuse → Blue Sea 5026 busbar)
- **Protected by** → Circuit Fuses (blade fuses 10-30A per circuit)
- **Distributed by** → Blue Sea 5026 fuse block (central point, common ground bus)
- **Connects to** → External Loads (heater, fridge, spare devices) or Internal Load (Nilight panel)

**State Transitions:**
```
States: {idle, active, faulted}

Transitions:
  idle → active: Load connected and drawing current
  active → idle: Load disconnected
  active → faulted: Fuse opens due to overcurrent
  faulted → idle: Fuse replaced, load disconnected
```

---

### 5. Charging Circuit

**Description**: Interface for recharging battery from external AC charger

**Attributes:**
- `connectorType`: String - **"Anderson_Powerpole_PP45"** (battery box end)
- `chargerConnector`: String - **"Alligator clips"** (VEVOR charger end)
- `adapterCable`: Object
  - `required`: **true** (VEVOR alligator clips → Powerpole PP45)
  - `wireGauge`: **12 AWG**
  - `length`: **3-6 feet**
  - `label`: **"CHARGER ADAPTER - DO NOT USE FOR LOADS"**
- `chargerModel`: String - **"VEVOR 12V 20A LiFePO4 Charger"** (model 010889683485)
- `voltageInput`: Number - **14.6V** (LiFePO4 absorption voltage from charger)
- `chargeProfile`: Object
  - `bulk`: **14.4V** (constant current 20A)
  - `absorption`: **14.6V** (constant voltage, taper to 4A)
  - `float`: **13.6V** (maintenance, minimal current)
- `currentRating`: Number - **20A** (VEVOR charger output)
- `chargeTime`: String - **"7.5 hours"** (200Ah from 20% to 95% SOC: 150Ah / 20A)
- `fuseRating`: Number - **30A** blade fuse (Blue Sea circuit 1)
- `fuseType`: String - **"ST_blade_ATO"**
- `reversePolarityProtection`: String - **"mechanical_keyed"** (Powerpole connector prevents reverse)
- `wireGauge`: Number - **10 AWG** (Blue Sea circuit 1 to charge input Powerpole)
- `polarity`: Object
  - `positive`: String - "red"
  - `negative`: String - "black"
- `labelText`: String - **"CHARGE IN 30A"** (on enclosure at Powerpole connector)

**Relationships:**
- **Charges** → Battery Module (VEVOR 200Ah via Blue Sea circuit 1)
- **Protected by** → 30A blade fuse (Blue Sea circuit 1) + 100A ANL main fuse
- **Accepts** → VEVOR 20A LiFePO4 charger (via adapter cable)

**State Transitions:**
```
States: {idle, charging, fault}

Transitions:
  idle → charging: Charger connected, voltage >13.5V detected
  charging → idle: Charger disconnected or battery full (voltage plateaus at 14.4V)
  charging → fault: Reverse polarity detected, over-current, or fuse opens
  fault → idle: Fault cleared, charger disconnected, fuse replaced
```

---

### 6. Monitoring System

**Description**: Instrumentation for observing battery state and system health

#### 6.1 Battery Monitor - Victron BMV-712 Smart

**Attributes:**
- `type`: String - **"coulomb_counter_shunt_based"** (professional battery monitor)
- `manufacturer`: String - **"Victron Energy"**
- `model`: String - **"BMV-712 Smart"**
- `shunt`: Object
  - `rating`: **500A / 50mV** (measures current flow)
  - `placement`: **"negative trunk between battery- and system ground"**
  - `wiring`: **"Battery- → Shunt battery side | Shunt system side → Blue Sea negative bus"**
  - `note`: **"ALL negative wires connect to shunt system side, not battery directly"**
- `display`: Object
  - `type`: **"52mm × 52mm square panel mount"**
  - `location`: **"front panel cutout, right of Nilight panel"**
  - `connection`: **"RJ12 cable to shunt"**
  - `readings`: ["Voltage (±0.1V)", "SOC% (±1% after calibration)", "Current (A)", "Amp-hours consumed", "Time-to-go prediction", "Alarms"]
- `bluetooth`: Boolean - **true** (VictronConnect app for detailed monitoring, history, configuration)
- `accuracy`: Object
  - `voltage`: **±0.1V**
  - `SOC`: **±1%** (after full charge synchronization)
  - `current`: **±0.4%**
- `configuration`: Object
  - `batteryCapacity`: **200Ah**
  - `chargedVoltage`: **14.4V** (synchronize SOC to 100% when reached)
  - `tailCurrent`: **4A** (2% of capacity, end of charge detection)
  - `peukertExponent`: **1.05** (LiFePO4 typical)
  - `alarms`: ["30% SOC warning (low battery)", "20% SOC critical"]
- `temperatureSensor`: Object - **Optional** (BMV-712 kit includes sensor, can attach to battery for continuous temp monitoring via app)
- `price`: Number - **$200-250** (kit with shunt, display, RJ12 cable, temp sensor)

**Rationale:**
- LiFePO4 flat discharge curve: Voltage stays ~13.2V from 80% SOC to 30% SOC (voltage-only monitoring inadequate)
- Coulomb counting tracks every amp-hour in/out for accurate SOC%
- Runtime prediction critical for diesel heater winter camping safety
- Historical data enables capacity fade tracking over years

**Relationships:**
- **Monitors** → Battery Module (voltage, SOC, current, amp-hours)
- **Shunt intercepts** → All system negative current (measures total system draw)
- **Powered by** → Battery Module (~10-20mA quiescent)
- **Reports to** → User (display + Bluetooth app)

#### 6.2 Quick-Check Panel - Nilight 4-in-1

**Attributes:**
- `type`: String - **"integrated_multifunction_panel"**
- `manufacturer`: String - **"Nilight"**
- `model`: String - **"4-in-1 Panel"**
- `features`: Array
  - **"USB-C PD"** (Power Delivery, up to 100W fast charging)
  - **"USB-A QC 3.0"** (Quick Charge 3.0, 2.1A)
  - **"12V cigarette lighter outlet"** (standard 12V accessory socket)
  - **"Integrated LED voltmeter"** (blue illumination, ±0.1-0.2V typical)
  - **"ON/OFF rocker switch"** (prevents parasitic drain during storage)
- `cutoutDimensions`: String - **"4-6\" × 2-3\""** (verify when received, rectangular cutout)
- `mountingLocation`: String - **"front panel center, upper third"**
- `connection`: Object
  - `power`: **"Female spade terminals to 10 AWG from Blue Sea circuit 4"**
  - `fuse`: **"20A blade fuse (Blue Sea circuit 4)"**
- `voltmeterAccuracy`: Number - **±0.1-0.2V** (typical LED panel meter)
- `quiescentCurrent`: Number - **0mA** when OFF switch pressed, **<100mA** when ON (voltmeter + standby)
- `price`: Number - **$30-40**

**Rationale:**
- Instant voltage check without Bluetooth/phone
- Eliminates need for separate voltmeter (~$10-15 savings)
- ON/OFF switch prevents battery drain during storage
- USB-C PD enables fast phone/laptop charging

**Relationships:**
- **Powers** → USB devices (phones, tablets, laptops via USB-C PD)
- **Powers** → 12V devices (via cigarette outlet)
- **Displays** → Battery voltage (quick visual check, backup to Victron)
- **Powered by** → Blue Sea circuit 4 (20A fused)

#### 6.3 Temperature Monitoring (v1 Manual)

**Attributes:**
- `type`: String - **"infrared_thermometer"** (manual check, non-contact)
- `accuracy`: Number - **±0.5-1.0°C** (typical IR thermometer)
- `range`: Object - `min`: -20°C, `max`: 500°C (wide range covers battery + wire + fuse block)
- `targets`: Array - ["Battery case surface", "Blue Sea fuse block", "Wire connections", "100A ANL fuse holder"]
- `procedure`: String - **"Check before/after use, document in operating log if >40°C"**
- `upgrade`: String - **"Victron BMV-712 optional temperature sensor"** (attach to battery case, monitor via app)
- `futureEnhancement`: String - **"DS18B20 digital sensor with ESP32 datalogging"** (deferred to v2)
- `price`: Number - **$15-30** (infrared thermometer)

**Rationale:**
- VEVOR BMS has internal temperature protection (over-temp cutoff ~60-65°C)
- Manual checking validates no excessive resistance (poor connections, undersized wire)
- Incremental Evolution (Principle IV): Defer complexity until manual method proves inadequate

**Relationships:**
- **Monitors** → Battery Module, Wire connections, Blue Sea fuse block
- **Operated by** → User (manual check procedure)
- **Documents** → Temperature trends (operating log in FR-031)
- `forwardVoltage`: Number - volts, e.g., 2.0V (red), 3.0V (green)
- `forwardCurrent`: Number - milliamps (mA), e.g., 10-20mA
- `triggerVoltage`: Number - threshold voltage for LED activation
  - Power LED: >13.0V (on), <13.0V (off)
  - Low Battery LED: <13.0V (on), >13.0V (off)
  - Charging LED: >14.0V (on), <14.0V (off)
- `circuitType`: String - "voltage_comparator", "transistor_switch"

**Relationships:**
- **Indicates state of** → Battery Module
- **Powered by** → Battery Module (minimal quiescent current)
- **Visible to** → User (2 meters minimum per SC-005)

---

---

### 7. Protection Devices (Fuses)

**Multi-Layer Protection Architecture:**
1. **Primary**: VEVOR integrated 100A BMS (over-voltage, under-voltage, over-current, short-circuit, over-temp)
2. **Secondary**: 100A ANL main fuse (battery positive trunk, protects battery from downstream faults)
3. **Tertiary**: Blue Sea 5026 circuit fuses (10-30A blade fuses, load-specific protection)

#### 7.1 Main Battery Fuse (100A ANL)

**Attributes:**
- `type`: String - **"ANL"** (automotive nickel link, fast-acting)
- `rating`: Number - **100A** (matches VEVOR BMS continuous discharge rating)
- `voltage`: Number - **32V DC** rated (exceeds 12V system requirement)
- `timeCurrent`: String - **"ANL fuse I²t characteristics"** (typically opens in 0.5-10 seconds at 200% rating)
- `holderType`: String - **"inline ANL holder"** (4-6 AWG compatible)
- `location`: String - **"Within 18 inches of battery positive terminal"** (NEC recommendation, minimize unfused wire length)
- `wireGauge`: Number - **4 AWG** (Battery+ to ANL holder, ANL holder to Blue Sea busbar)
- `terminals`: String - **"M8 ring terminal"** (battery end) + **"ANL holder lugs"** (fuse end) + **"Blue Sea busbar post"**
- `price`: Number - **$15-25** (ANL fuse + inline holder + terminals)

**Rationale:**
- 100A matches VEVOR BMS limit (coordination: BMS trips at 100A, ANL fuse is backup for sustained overcurrent)
- Fast-acting to protect battery before BMS overheats
- Inline holder enables fuse replacement without disconnecting battery

**Relationships:**
- **Protects** → Battery Module (VEVOR 200Ah)
- **Isolates** → All downstream circuits on sustained overcurrent (>100A for >10 seconds)
- **Coordinates with** → VEVOR BMS (primary) and Blue Sea fuses (tertiary)

#### 7.2 Circuit Fuse Block (Blue Sea Systems 5026)

**Attributes:**
- `type`: String - **"12-circuit ST blade fuse block"** (centralized distribution)
- `manufacturer`: String - **"Blue Sea Systems"**
- `model`: String - **"5026"**
- `busbarRating`: Number - **100A** (main positive busbar capacity)
- `circuitCount`: Number - **12** (6 allocated in v1, 6 future expansion)
- `fuseType`: String - **"ST blade fuses"** (ATO/ATC standard automotive)
- `featureList`: Array
  - **"Common negative bus"** (star grounding point, all circuit negatives return here)
  - **"Individual fuse holders"** (each circuit independently fused)
  - **"Cover with fuse diagram"** (label circuit allocations)
  - **"Marine-grade"** (corrosion-resistant, tinned copper bus, IP-rated terminals)
  - **"Mounting flanges"** (screw-mount to enclosure wall)
- `groundingArchitecture`: String - **"Star ground: All circuit negatives → Blue Sea negative bus → 4 AWG to Victron shunt system side"**
- `circuitAllocations`: Array - **See Section 4 (Output Circuit)** for 6 allocated circuits
- `price`: Number - **$50-70**

**Circuit-Specific Fuses** (ST Blade ATO/ATC):
- Circuit 1 (Charge): **30A** fuse (VEVOR 20A charger + margin)
- Circuit 2 (Heater): **10A** fuse (diesel heater 8A + margin)
- Circuit 3 (Fridge): **15A** fuse (fridge/cooler 10A + margin)
- Circuit 4 (USB panel): **20A** fuse (Nilight panel USB-C PD 100W + USB-A + 12V)
- Circuit 5 (Spare 1): **20A** fuse (future: inverter, solar, etc.)
- Circuit 6 (Spare 2): **15A** fuse (future expansion)
- Circuits 7-12: **Unpopulated** in v1 (expansion capacity)

**Fuse Quantities** (with spares):
- 2× 10A (circuit 2 + 1 spare)
- 3× 15A (circuit 3, circuit 6, + 1 spare)
- 2× 20A (circuit 4, circuit 5 + spares in assortment)
- 2× 30A (circuit 1 + 1 spare)
- Assortment kit: **120pc Blade Fuse Assortment** (~$12-15, includes 5/7.5/10/15/20/25/30A)

**Relationships:**
- **Distributes power from** → 100A ANL main fuse (via 4 AWG positive trunk)
- **Protects** → Individual circuits (heater, fridge, USB panel, charge, spares)
- **Provides grounding for** → All circuit returns (common negative bus)
- **Feeds** → 6 allocated circuits (10 AWG wire to Powerpole/Nilight)

---

## Component Relationships Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ Greenmade 27gal Enclosure (30.4"×20.4"×14.7")                                   │
│                                                                                   │
│  ┌────────────────────────┐         ┌──────────────────────┐                   │
│  │  VEVOR Battery 200Ah   │◄────────│  Integrated BMS      │                   │
│  │  LiFePO4 12V (25kg)    │ protects│  (100A, OVP/UVP/OCP) │                   │
│  │  M8 posts              │         └──────────────────────┘                   │
│  └──┬────────────────┬────┘                                                     │
│     │ +              │ -                                                        │
│     │ 4AWG red       │ 4AWG black                                               │
│     │                │                                                          │
│     ▼                ▼                                                          │
│  ┌──────────────┐   ┌────────────────────┐                                     │
│  │ 100A ANL Fuse│   │ Victron BMV-712    │                                     │
│  │ (inline)     │   │ 500A Shunt         │                                     │
│  └──┬───────────┘   │ (in negative trunk)│                                     │
│     │               └──┬─────────────────┘                                     │
│     │ 4AWG red         │ 4AWG black (system side)                              │
│     │                  │                                                        │
│     ▼                  ▼                                                        │
│  ┌──────────────────────────────────────────────────┐                          │
│  │      Blue Sea 5026 Fuse Block (12 circuits)      │                          │
│  │  ┌─────────────────┐    ┌────────────────────┐  │                          │
│  │  │ Positive Busbar │    │ Negative Bus       │  │                          │
│  │  │ (100A)          │    │ (Star Ground)      │  │                          │
│  │  └─┬───┬───┬───┬───┘    └─┬──┬──┬──┬─────────┘  │                          │
│  │    │   │   │   │          │  │  │  │             │                          │
│  └────┼───┼───┼───┼──────────┼──┼──┼──┼─────────────┘                          │
│       │   │   │   │          │  │  │  │                                        │
│  10AWG│   │   │   │     10AWG│  │  │  │                                        │
│       ▼   ▼   ▼   ▼          ▼  ▼  ▼  ▼                                        │
│     ┌───────────────────────────────────────┐                                  │
│     │ Circuit 1: Charge Input (30A)        │◄─── VEVOR 20A Charger             │
│     │   Powerpole PP45 + adapter cable     │     (via adapter cable)           │
│     └───────────────────────────────────────┘                                  │
│     ┌───────────────────────────────────────┐                                  │
│     │ Circuit 2: Heater Output (10A)       │───► Diesel Heater                 │
│     │   Powerpole PP45                      │     (3-8A)                        │
│     └───────────────────────────────────────┘                                  │
│     ┌───────────────────────────────────────┐                                  │
│     │ Circuit 3: Fridge Output (15A)       │───► Fridge/Cooler                 │
│     │   Powerpole PP45                      │     (5-10A)                       │
│     └───────────────────────────────────────┘                                  │
│     ┌───────────────────────────────────────┐                                  │
│     │ Circuit 4: USB Panel (20A)           │                                   │
│     │   Hardwired to Nilight 4-in-1        │     ┌─────────────────────┐      │
│     │   (USB-C PD, USB-A, 12V, Voltmeter)  │────►│ Nilight Panel       │      │
│     └───────────────────────────────────────┘     │ (front panel)       │      │
│                                                    │ ON/OFF switch       │      │
│     ┌───────────────────────────────────────┐     └─────────────────────┘      │
│     │ Circuit 5: Spare 1 (20A)             │───► Future: Inverter/Solar       │
│     │   Powerpole PP45                      │                                   │
│     └───────────────────────────────────────┘                                  │
│     ┌───────────────────────────────────────┐                                  │
│     │ Circuit 6: Spare 2 (15A)             │───► Future Expansion              │
│     │   Powerpole PP45                      │                                   │
│     └───────────────────────────────────────┘                                  │
│                                                                                   │
│  ┌──────────────────────────────────────────────────────────────┐              │
│  │               Monitoring & Status                             │              │
│  │  ┌────────────────────────┐  ┌────────────────────────────┐  │              │
│  │  │ Victron BMV-712 Display│  │ Nilight Integrated Voltmeter│ │              │
│  │  │ (52mm square, front)   │  │ (LED, quick check)         │  │              │
│  │  │ - Voltage ±0.1V        │  │ - Backup display           │  │              │
│  │  │ - SOC% ±1%             │  │ - ON/OFF indicator LED     │  │              │
│  │  │ - Current, Ah consumed │  └────────────────────────────┘  │              │
│  │  │ - Time-to-go prediction│                                   │              │
│  │  │ - Bluetooth app        │  ┌────────────────────────────┐  │              │
│  │  │ - Alarms (30%, 20%)    │  │ Temperature Monitoring     │  │              │
│  │  └────────────────────────┘  │ (v1: Manual IR thermometer)│  │              │
│  │                               │ (Optional: Victron sensor) │  │              │
│  │                               └────────────────────────────┘  │              │
│  └──────────────────────────────────────────────────────────────┘              │
│                                                                                   │
│  Protection Architecture: 3 Layers                                              │
│  1. VEVOR BMS (primary): 100A OCP, OVP 14.6V, UVP 10.0V, over-temp, SCP       │
│  2. 100A ANL fuse (secondary): Sustained overcurrent backup                    │
│  3. Blue Sea blade fuses (tertiary): 10-30A circuit-specific protection        │
│                                                                                   │
│  Grounding: Star architecture - ALL negatives → Blue Sea bus → Victron shunt   │
└─────────────────────────────────────────────────────────────────────────────────┘

Key Wiring Paths:
  Positive: Battery+ → 100A ANL → Blue Sea+ bus → 6 circuits (10AWG) → Loads
  Negative: Loads → Blue Sea- bus → Victron shunt (system) → Battery-
  
Critical: ALL negative current flows through Victron shunt for accurate SOC tracking
```

---

## State Machine: Battery Box System

### Overall System States

```
┌────────┐       charger connected
│  IDLE  │◄──────────────────────────────────┐
│        │       no load, no charging         │
└────┬───┘                                     │
     │                                         │
     │ load connected                          │
     ▼                                         │
┌────────────┐   charger connected             │
│ DISCHARGING│───────────────────────────┐     │
│            │   (can charge + discharge)│     │
└────┬───────┘                           │     │
     │                                   ▼     │
     │ load disconnected            ┌─────────┴───┐
     └─────────────────────────────►│  CHARGING   │
                                     │             │
                                     └─────┬───────┘
                                           │
                                           │ charger disconnected
                                           │ or battery full
                                           └──────────────────────┐
                                                                  │
         ┌────────────────────────────────────────────────────────┘
         │
         │ fault condition (BMS trigger, fuse open, over-temp)
         ▼
    ┌────────┐
    │ FAULT  │
    │        │
    └────┬───┘
         │
         │ fault cleared, manual reset
         ▼
    ┌────────┐
    │  IDLE  │
    └────────┘
```

### Voltage-Based State Indicators

| Battery Voltage | Approximate SOC | Status LED State      | User Action |
|----------------|-----------------|------------------------|-------------|
| 14.4V - 14.6V  | 100% (charging) | Charging (Red) ON      | Wait for charge complete |
| 13.4V - 14.3V  | 80% - 99%       | Power (Green) ON       | System operational |
| 13.0V - 13.3V  | 20% - 80%       | Power (Green) ON       | System operational |
| 12.5V - 12.9V  | 10% - 20%       | Low Battery (Yellow) ON| Recharge soon |
| 11.0V - 12.4V  | 5% - 10%        | Low Battery (Yellow) ON| Recharge immediately |
| <11.0V         | <5%             | Low Battery (Yellow) ON, BMS approaching cutoff | Stop use, recharge |
| <10.0V         | 0% (BMS cutoff) | All LEDs OFF (no power)| BMS protection triggered, recharge required |

---

## Component Specifications Template

For each physical component procured, document the following in `specs/001-battery-box/docs/component-specs.md`:

### Battery Module
- Manufacturer:
- Model:
- Chemistry: LiFePO4
- Nominal Voltage: 12.8V
- Capacity: [XX] Ah
- Max Continuous Current: [XX] A
- BMS Integrated: Yes/No
- Purchase Date:
- Purchase Price:
- Datasheet Link:

### Enclosure
- Type: (Weatherproof case / Plywood box)
- Dimensions: L×W×H mm
- Weight (empty): [XX] kg
- Source:

### Output Connectors
- Connector Type: (Anderson PP45 / XT60 / etc.)
- Quantity:
- Current Rating: [XX] A
- Source:

### Fuses
- Main Fuse: [XX]A ANL, Manufacturer, Part Number
- Circuit Fuses: [XX]A Blade ATO, Quantity, Manufacturer
- Datasheet Links:

### Monitoring Components
- Voltmeter: Model, Range, Accuracy, Source
- Temperature Sensor: Model, Type, Accuracy, Source
- LEDs: Color, Size, Forward Voltage, Quantity

### Charger
- Manufacturer:
- Model:
- Output Voltage: [XX.X]V
- Output Current: [XX]A
- LiFePO4 Compatible: Yes
- Datasheet Link:

---

## Summary

This data model provides a complete structural definition of the Battery Box v1 physical system. All components, their attributes, relationships, and state transitions are documented to enable:

1. **Procurement**: Clear specifications for component sourcing
2. **Assembly**: Understanding of how components interconnect
3. **Testing**: Validation of state transitions and protection mechanisms
4. **Troubleshooting**: Fault diagnosis using state machine
5. **Future expansion**: Modular interfaces for adding capabilities

**Next Phase**: Generate component interface contracts and quickstart assembly guide.
