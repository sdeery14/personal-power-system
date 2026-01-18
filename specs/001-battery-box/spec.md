# Feature Specification: Battery Box v1

**Feature Branch**: `001-battery-box`  
**Created**: 2026-01-18  
**Status**: Draft  
**Input**: User description: "Battery Box v1 — the core portable DC power module — fully compliant with the project constitution"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Safe Manual Power Delivery (Priority: P1)

A user can connect a 12V DC load (such as a diesel heater, portable refrigerator, or phone charger) to the battery box and receive power safely with proper overcurrent protection and clear visual status indication.

**Why this priority**: This is the fundamental purpose of the battery box — to deliver stored DC power to loads. Without this capability, the system has no utility. Safety is paramount (Constitution Principle I: Safety First).

**Independent Test**: Can be fully tested by connecting a known 12V load (e.g., 5A test resistor or diesel heater) to the output terminals, verifying voltage is present, load operates correctly, and fuse protection responds to overcurrent conditions.

**Acceptance Scenarios**:

1. **Given** a fully charged battery box with no load connected, **When** a user connects a 10A diesel heater to the 12V output terminals, **Then** the heater receives 12V power, operates normally, and the battery voltage remains within safe limits (11.5V - 14.4V for LiFePO4).

2. **Given** a battery box with load connected, **When** the load draws excessive current exceeding the fuse rating, **Then** the fuse opens the circuit, load stops receiving power, and no damage occurs to the battery or wiring.

3. **Given** a battery box with proper voltage (>12V), **When** a user observes the status indicators, **Then** visual indicators clearly show battery is operational and capable of delivering power.

---

### User Story 2 - Basic State Monitoring (Priority: P2)

A user can observe the battery box's critical state (voltage, approximate state of charge, temperature) through built-in instrumentation without requiring external tools or software.

**Why this priority**: Transparency & Observability (Constitution Principle III) is non-negotiable. Users must be able to assess battery health and remaining capacity to avoid unexpected shutdowns or unsafe conditions.

**Independent Test**: Can be tested by reading the voltage display with battery under no load, light load (5A), and moderate load (15A), verifying values are accurate within ±0.1V of a reference multimeter, and temperature reading matches ambient conditions.

**Acceptance Scenarios**:

1. **Given** a battery box with built-in voltage meter, **When** a user reads the display with no load connected, **Then** the displayed voltage matches actual battery voltage within ±0.1V.

2. **Given** a battery box under load, **When** voltage drops below a defined warning threshold (e.g., 12.4V for LiFePO4 ~20% SOC), **Then** a warning indicator illuminates to alert the user.

3. **Given** a battery box in operation, **When** internal temperature is measured, **Then** temperature is displayed and remains within safe operating range (0°C to 45°C for typical LiFePO4).

---

### User Story 3 - External AC Charging Support (Priority: P3)

A user can recharge the battery box from a standard 120V AC outlet using a compatible external LiFePO4 AC charger with proper isolation and safety protection.

**Why this priority**: While loads are the primary function, the battery box must be rechargeable to be useful over time. AC charging is the most universally available charging method (home, campground, garage). This enables battery maintenance between use cycles.

**Independent Test**: Can be tested by connecting the battery box to 120V AC power with a depleted battery (e.g., 12.8V / 20% SOC), verifying charging current flows, voltage rises appropriately, and charger terminates at full charge (14.4V for LiFePO4) without user intervention.

**Acceptance Scenarios**:

1. **Given** a battery box at 50% state of charge, **When** a user connects the AC charger to a standard 120V outlet, **Then** the battery begins charging, charge current is within charger specifications, and voltage rises steadily toward full charge voltage.

2. **Given** a battery charging from AC, **When** the battery reaches full charge (14.4V for LiFePO4), **Then** the charger transitions to float/maintenance mode or terminates charging to prevent overcharge.

3. **Given** a battery box connected to AC charger, **When** a user observes status indicators, **Then** charging status is clearly indicated (charging vs. charged vs. fault).

---

### Edge Cases

- What happens when the battery is deeply discharged below the safe minimum voltage (e.g., <10V for 12V LiFePO4)?
- How does the system behave if multiple high-current loads are connected simultaneously, exceeding the total system capacity?
- What occurs if the battery temperature exceeds safe operating range (e.g., >45°C) during charging or discharging?
- How does the system respond to reverse polarity connection on load terminals (if mechanically possible)?
- What happens if AC charger is connected while loads are actively drawing power?
- How is the battery protected if left in a discharged state for extended periods (weeks/months)?

## Requirements *(mandatory)*

### Functional Requirements

**Battery & Energy Storage:**

- **FR-001**: Battery box MUST contain a 12V lithium battery with documented capacity (minimum 50Ah recommended for practical utility)
- **FR-002**: Battery chemistry MUST be clearly labeled on the enclosure (e.g., "12V LiFePO4 100Ah")
- **FR-003**: Battery safe minimum state-of-charge MUST be defined and documented per battery chemistry (e.g., 10% SOC / 12.8V for LiFePO4)
- **FR-004**: Battery MUST be protected from discharge below manufacturer's safe minimum voltage

**Safety & Protection:**

- **FR-005**: All power output circuits MUST be protected by appropriately rated fuses (minimum 125% of expected continuous load current)
- **FR-006**: Battery terminals MUST be protected from accidental short circuit (covered terminals, insulated connections, or internal battery BMS protection)
- **FR-007**: System MUST fail safely: any protection device failure MUST result in open circuit, not continued operation
- **FR-008**: Enclosure MUST provide basic protection from physical damage to battery and connections (minimum: closed box with secured lid)
- **FR-009**: All user-accessible terminals MUST be clearly labeled with voltage, polarity, and maximum current rating

**Electrical Interfaces (Constitution Principle II: Modularity):**

- **FR-010**: Power output SHOULD use standardized connectors (Anderson Powerpole 30A/45A, XT60, or cigarette lighter socket)
- **FR-011**: Any non-standard connector MUST be documented with rationale and replacement strategy
- **FR-012**: AC charging input MUST use a standard connector compatible with common chargers (e.g., Anderson Powerpole, XT60, or barrel jack)
- **FR-013**: Charging interface MUST include reverse polarity protection

**Monitoring & Observability (Constitution Principle III):**

- **FR-014**: Battery voltage MUST be measurable without disassembly (built-in voltmeter or accessible test points)
- **FR-015**: Battery temperature MUST be measurable at least once per operational session (built-in sensor or documented procedure with thermometer)
- **FR-016**: State of charge estimation method MUST be documented (voltage-based lookup table or SOC indicator); voltage-based SOC estimation MUST account for load conditions and be treated as approximate
- **FR-017**: Visual status indicators MUST clearly communicate at minimum: power available, low battery warning, charging status

**Charging:**

- **FR-018**: Battery box MUST support charging from 120V AC mains via a compatible external LiFePO4 charger
- **FR-019**: Charger MUST match battery chemistry and voltage (e.g., LiFePO4-compatible charger for LiFePO4 battery)
- **FR-020**: Charger MUST terminate or reduce current when battery reaches full charge voltage
- **FR-021**: Charging MUST NOT create hazardous conditions (overheating, overcharge, fire risk)
- **FR-022**: Supported AC charger model(s) MUST be documented, including output voltage, current rating, and battery chemistry compatibility

**Physical & Mechanical:**

- **FR-023**: Battery box MUST be portable (weight manageable for one person, handles or carrying method provided)
- **FR-024**: Enclosure MUST allow thermal management (ventilation holes or passive cooling for heat dissipation)
- **FR-025**: Battery MUST be securely mounted within enclosure to prevent movement during transport

**Documentation (Constitution Principle V):**

- **FR-026**: Battery specifications MUST be documented (chemistry, nominal voltage, capacity, manufacturer, model)
- **FR-027**: Maximum continuous discharge current MUST be documented and clearly labeled
- **FR-028**: Charger specifications MUST be documented (voltage, charge current, charge termination method)
- **FR-029**: All fuse ratings and locations MUST be documented
- **FR-030**: Wiring diagram showing all connections MUST be created and stored with the battery box
- **FR-031**: Operating instructions MUST be created covering: safe connection of loads, charging procedure, storage guidelines, emergency shutdown

### Key Entities

- **Battery Module**: The core energy storage component (e.g., 12V 100Ah LiFePO4 battery pack with integrated or external BMS)
  - Attributes: chemistry type, nominal voltage, capacity (Ah), safe voltage range, safe temperature range, cycle life, manufacturer/model
  
- **Enclosure**: Physical housing containing battery and electrical components
  - Attributes: material (e.g., plastic, metal), dimensions, weight capacity, ventilation design, mounting points, handle/carrying method
  
- **Output Circuit**: User-facing power delivery interface
  - Attributes: connector type, voltage rating, current rating, fuse rating, wire gauge (AWG), polarity marking
  
- **Charging Circuit**: Interface for recharging the battery
  - Attributes: connector type, compatible charger specifications, reverse polarity protection method, charge termination method
  
- **Monitoring System**: Instrumentation for observing battery state
  - Attributes: voltage measurement method (analog meter, digital display, test points), temperature sensor type/location, SOC indication method, status LED configuration

- **Protection Devices**: Safety components preventing unsafe conditions
  - Attributes: fuse types and ratings, fuse locations, BMS protection features (if integrated), physical safeguards

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A user can connect a typical 12V DC load (5A - 15A) and receive power for the expected duration based on battery capacity (e.g., 100Ah battery delivers 10A for 8+ hours before reaching low-voltage warning)

- **SC-002**: Battery voltage measurement is accurate within ±0.1V when compared to a calibrated multimeter

- **SC-003**: Fuse protection successfully interrupts circuit when test load exceeds fuse rating, consistent with fuse manufacturer's time-current characteristics, with no damage to battery or wiring

- **SC-004**: Battery can be recharged from 20% SOC to 95% SOC using AC charger within documented time frame (e.g., 100Ah battery at 10A charge rate completes in ~8 hours)

- **SC-005**: User can identify battery state (operational / low battery / charging / fault) from visual indicators at a distance of 2 meters in typical lighting conditions

- **SC-006**: Battery temperature remains below 40°C during continuous 10A discharge in ambient temperature of 25°C

- **SC-007**: All required documentation (specifications, wiring diagram, operating instructions) is present and can be understood by a technically-inclined user without prior power systems experience

- **SC-008**: Battery box MUST be portable by one person with reasonable effort, without tools or disassembly

- **SC-009**: System operates safely for 100 charge/discharge cycles without component failure or degradation requiring repair

- **SC-010**: No safety incidents (smoke, sparks, thermal damage, injury) occur during normal operation or documented fault conditions (overcurrent, reverse polarity test)
