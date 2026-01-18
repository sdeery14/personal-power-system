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
- `capacity`: Number - Amp-hours (Ah), e.g., 50, 100, 200
- `maxContinuousCurrent`: Number - Amps (A), per manufacturer spec
- `maxPulseCurrent`: Number - Amps (A), short duration per manufacturer spec
- `voltageRange`: Object
  - `max`: 14.6V (fully charged, per BMS cutoff)
  - `nominal`: 12.8V (resting voltage ~50% SOC)
  - `min`: 10.0V (BMS low-voltage cutoff)
  - `warningThreshold`: 13.0V (20% SOC, user warning)
- `temperatureRange`: Object
  - `dischargeMin`: 0°C
  - `dischargeMax`: 45°C
  - `chargeMin`: 0°C (some batteries require >0°C)
  - `chargeMax`: 45°C
  - `warningThreshold`: 40°C
- `cycleLife`: Number - e.g., 2000-5000 cycles to 80% capacity
- `weight`: Number - kilograms (kg)
- `dimensions`: Object - `length`, `width`, `height` in mm
- `manufacturer`: String
- `model`: String
- `bmsIntegrated`: Boolean - true if BMS included
- `serialNumber`: String (optional, for tracking)

**Relationships:**
- **Houses** → BMS (if `bmsIntegrated` = true)
- **Powers** → Output Circuits
- **Charged by** → Charging Circuit
- **Monitored by** → Monitoring System
- **Protected by** → Main Fuse

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
- `type`: String - "integrated" (within battery) or "external" (separate unit)
- `cellCount`: Number - 4 (for 12V system)
- `maxContinuousCurrent`: Number - Amps (A)
- `balancingCurrent`: Number - milliamps (mA), e.g., 50-200mA
- `protections`: Array of Strings
  - "over-voltage" (typically 3.65V/cell)
  - "under-voltage" (typically 2.5V/cell)
  - "over-current-discharge"
  - "over-current-charge"
  - "over-temperature" (if sensor present)
  - "short-circuit"
- `cutoffVoltages`: Object
  - `overVoltage`: 14.6V (disconnect charging)
  - `underVoltage`: 10.0V (disconnect loads)
- `temperatureSensor`: Boolean - true if BMS includes temp monitoring
- `manufacturer`: String
- `model`: String

**Relationships:**
- **Integrated with** → Battery Module (if `type` = "integrated")
- **Protects** → Battery Module
- **Controls** → Main Disconnect (opens circuit on fault)

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
- `material`: String - "plastic", "aluminum", "plywood"
- `dimensions`: Object - `length`, `width`, `height` in mm
- `weight`: Number - kilograms (kg), empty
- `weatherproof`: Boolean - true if rated for outdoor/wet conditions
- `ventilationHoles`: Number - count of ventilation openings
- `holeDiameter`: Number - mm, e.g., 25mm (1 inch)
- `meshCover`: Boolean - true if ventilation has debris screen
- `handles`: Boolean - true if carrying handles present
- `mountingPoints`: Array of Objects
  - `type`: "battery", "voltmeter", "fuse_holder", "connector_panel"
  - `location`: String - description (e.g., "front panel", "top lid")

**Relationships:**
- **Contains** → Battery Module, Protection Devices, Monitoring System
- **Provides access to** → Output Circuits, Charging Circuit

**Physical Constraints:**
- Total weight (enclosure + battery + components) should enable one-person portability
- Ventilation must allow airflow without compromising protection
- Component mounting must prevent movement during transport

---

### 4. Output Circuit

**Description**: User-facing power delivery interface for connecting loads

**Attributes:**
- `circuitID`: String - unique identifier, e.g., "OUT1", "OUT2"
- `connectorType`: String - "Anderson_PP45", "XT60", "cigarette_lighter", "screw_terminal"
- `voltageRating`: Number - 12V (nominal)
- `currentRating`: Number - Amps (A), maximum continuous current
- `fuseRating`: Number - Amps (A), protection fuse
- `fuseType`: String - "blade_ATO", "blade_mini", "ANL"
- `wireGauge`: Number - AWG, e.g., 10, 12, 14
- `wireLength`: Number - mm, from fuse to connector
- `polarity`: Object
  - `positive`: String - wire color, e.g., "red"
  - `negative`: String - wire color, e.g., "black"
- `labelText`: String - text on enclosure, e.g., "12V 30A OUTPUT"

**Relationships:**
- **Powered by** → Battery Module (via Main Fuse)
- **Protected by** → Circuit Fuse
- **Connects to** → External Load (user equipment)

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
- `connectorType`: String - "Anderson_PP30", "Anderson_PP45", "XT60", "barrel_jack"
- `voltageInput`: Number - Expected from charger, e.g., 14.4V (LiFePO4 bulk voltage)
- `currentRating`: Number - Amps (A), maximum charge current
- `fuseRating`: Number - Amps (A), e.g., 20A or 30A
- `fuseType`: String - "blade_ATO", "ANL"
- `reversePolarityProtection`: String - "schottky_diode", "MOSFET_circuit", "mechanical_keyed"
- `wireGauge`: Number - AWG, e.g., 10 or 12
- `polarity`: Object
  - `positive`: String - wire color, e.g., "red"
  - `negative`: String - wire color, e.g., "black"
- `labelText`: String - text on enclosure, e.g., "CHARGE INPUT 14.4V 20A MAX"

**Relationships:**
- **Charges** → Battery Module
- **Protected by** → Charge Input Fuse
- **Accepts** → External AC Charger (user-provided)

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

#### 6.1 Voltage Meter

**Attributes:**
- `type`: String - "digital_panel_meter", "analog_voltmeter"
- `displayType`: String - "LED", "LCD", "needle"
- `range`: Object - `min`: 5V, `max`: 30V
- `accuracy`: Number - ±0.1V
- `characterHeight`: Number - mm, e.g., 9mm (0.36") or 14mm (0.56")
- `color`: String - "red", "blue", "green"
- `quiescentCurrent`: Number - milliamps (mA), e.g., 10-20mA
- `mountingType`: String - "panel_mount_cutout", "bezel"
- `cutoutDimensions`: Object - `width`, `height` in mm

**Relationships:**
- **Measures** → Battery Module voltage
- **Powered by** → Battery Module (parasitic draw)
- **Visible from** → User (2 meters minimum per SC-005)

#### 6.2 Temperature Sensor

**Attributes:**
- `type`: String - "DS18B20", "NTC_thermistor_10K", "infrared_thermometer"
- `accuracy`: Number - ±0.5°C to ±1°C
- `range`: Object - `min`: -20°C, `max`: 85°C
- `mountingLocation`: String - "battery_case_surface", "enclosure_interior"
- `readoutMethod`: String - "digital_display", "data_logger", "manual_check"
- `cableLength`: Number - mm (if wired sensor)

**Relationships:**
- **Monitors** → Battery Module temperature
- **Reports to** → Monitoring Display or Data Logger (future feature)

#### 6.3 Status Indicators (LEDs)

**Attributes:**
- `indicatorID`: String - "power", "low_battery", "charging"
- `color`: String - "green", "yellow", "red"
- `diameter`: Number - mm, e.g., 10mm
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

### 7. Protection Devices (Fuses)

#### 7.1 Main Battery Fuse

**Attributes:**
- `type`: String - "ANL", "Mega", "Class_T"
- `rating`: Number - Amps (A), e.g., 50A, 80A, 100A
- `voltage`: Number - DC voltage rating, e.g., 32V
- `timeCurrent`: String - reference to manufacturer datasheet (for SC-003 validation)
- `holderType`: String - "inline_ANL_holder", "fuse_block"
- `location`: String - "between battery positive and main busbar"

**Relationships:**
- **Protects** → Battery Module
- **Isolates** → All downstream circuits on fault

#### 7.2 Circuit Fuses (Output/Charging)

**Attributes:**
- `fuseID`: String - unique identifier per circuit, e.g., "FUSE_OUT1", "FUSE_CHG"
- `type`: String - "blade_ATO", "blade_mini"
- `rating`: Number - Amps (A), e.g., 10A, 15A, 20A, 30A
- `holderType`: String - "inline_blade_holder", "panel_mount_holder"
- `circuitProtected`: String - reference to Output Circuit ID or "charging_circuit"

**Relationships:**
- **Protects** → Specific Output Circuit or Charging Circuit
- **Interrupts** → Circuit on overcurrent

---

## Component Relationships Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│ Enclosure                                                        │
│                                                                   │
│  ┌──────────────────┐         ┌──────────────────┐              │
│  │  Battery Module  │◄────────│       BMS        │              │
│  │  (LiFePO4 12V)   │ protects│   (integrated)   │              │
│  └────────┬─────────┘         └──────────────────┘              │
│           │                                                      │
│           │ powers                                               │
│           ▼                                                      │
│  ┌────────────────────┐                                         │
│  │  Main Fuse (ANL)   │                                         │
│  └────────┬───────────┘                                         │
│           │                                                      │
│           ├──────► ┌─────────────────┐                          │
│           │        │ Output Circuit 1│──┐                       │
│           │        │  (Fuse + Conn.) │  ├──► External Loads    │
│           │        └─────────────────┘  │                       │
│           │                              │                       │
│           ├──────► ┌─────────────────┐  │                       │
│           │        │ Output Circuit 2│──┘                       │
│           │        └─────────────────┘                          │
│           │                                                      │
│           └──────► ┌─────────────────────┐                      │
│                    │  Charging Circuit   │◄── External Charger │
│                    │   (Fuse + Conn.)    │                      │
│                    └─────────────────────┘                      │
│                                                                   │
│  ┌─────────────────────────────────────────────┐                │
│  │        Monitoring System                     │                │
│  │  ┌──────────────┐  ┌──────────────────────┐ │                │
│  │  │ Volt Meter   │  │  Temp Sensor         │ │                │
│  │  │ (LED Display)│  │  (DS18B20/Thermistor)│ │                │
│  │  └──────────────┘  └──────────────────────┘ │                │
│  │  ┌──────────────┐  ┌───────────┐ ┌────────┐│                │
│  │  │ Power LED    │  │ Low Batt  │ │Charging││                │
│  │  │  (Green)     │  │LED (Yellow)│ │LED (Red)││                │
│  │  └──────────────┘  └───────────┘ └────────┘│                │
│  └─────────────────────────────────────────────┘                │
└───────────────────────────────────────────────────────────────────┘
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
