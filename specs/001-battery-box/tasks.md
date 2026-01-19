# Tasks: Battery Box v1

**Feature Branch**: `001-battery-box`  
**Generated**: 2026-01-19  
**Input**: Design documents from spec.md, plan.md, quickstart.md, data-model.md, contracts/

**Organization**: Tasks grouped by user story to enable independent implementation and testing.

## Format: `- [ ] [ID] [P?] [Story?] Description with file path`

- **[P]**: Can run in parallel (different files, no dependencies on incomplete tasks)
- **[Story]**: Which user story (US1, US2, US3) - omit for Setup/Foundational/Polish phases
- Include exact file paths for assembly steps

---

## Phase 1: Setup & Procurement

**Purpose**: Acquire components and prepare workspace

- [ ] T001 Verify VEVOR 200Ah battery received (model 010230251465), inspect for shipping damage, measure voltage 13.2-13.4V, document serial number and date code
- [ ] T002 Verify VEVOR 20A charger received (model 010889683485), inspect condition, test output voltage 14.4-14.6V unloaded with multimeter
- [ ] T003 Verify Greenmade 27gal tote received, check dimensions 30.4"×20.4"×14.7" external, verify latches and handles functional
- [ ] T004 Verify Nilight 4-in-1 panel received, check USB-C PD, USB-A, 12V outlet, integrated voltmeter all present
- [ ] T005 [P] Order Priority 1 core electrical components per shopping-list.md: 100A ANL fuse+holder, Blue Sea 5026, blade fuses, 2× KarlKers panel-mount units (B0F4L5FYQ2), 8× generic Powerpole PP45 pairs, Knoweasy crimper, wire (4/10/12/18 AWG), terminals, heat-shrink, zip ties (~$274-385)
- [ ] T006 [P] Order Priority 2 Victron BMV-712 Smart battery monitor kit per shopping-list.md (~$200-250)
- [ ] T007 [P] Order Priority 3 consumables per shopping-list.md: electrical tape, dielectric grease, ventilation mesh, labels, safety glasses (~$48-90)
- [ ] T008 Acquire tools: 1-1/8" hole saw (KarlKers 28.6mm holes), 52mm hole saw (Victron display), jigsaw or rotary tool (Nilight cutout), wire strippers, multimeter, heat gun, deburring tool
- [ ] T009 Create workspace with adequate lighting, work surface for component layout, power for tools, ventilation for heat-shrink work

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core assembly steps that MUST be complete before user story implementations

**⚠️ CRITICAL**: No circuit wiring can begin until enclosure prepared and battery/fuse block/Victron shunt mounted

- [ ] T010 Plan component layout on paper: battery bottom center (520×238×218mm = 20.5"×9.4"×8.6" lengthwise), left long side plywood panel 8"×12" (Blue Sea + Victron shunt + ANL holder vertical stack), right long side HDPE direct mount (Nilight + Victron display), front/back short side HDPE (2× KarlKers vertical), top corners (4× ventilation)
- [ ] T011 Cut left side plywood panel from 3/4" stock: 8" wide × 12" tall (measure tote internal dimensions to verify fit), this panel mounts Blue Sea 5026, Victron shunt, and ANL holder in vertical stack
- [ ] T012 Mark all cutouts: Nilight 4-6"×2-3" rectangular on tote right side HDPE, Victron 52mm square on tote right side HDPE below Nilight, 2× KarlKers 28.6mm holes on tote front or back short side HDPE vertical 3-4" spacing, 4× ventilation 25-30mm on tote top corners
- [ ] T013 [P] Drill Nilight rectangular cutout directly in tote right side HDPE (pilot holes + jigsaw/Dremel), verify exact dimensions when Nilight received, deburr edges
- [ ] T014 [P] Drill Victron 52mm square cutout directly in tote right side HDPE (4 pilot holes at corners + jigsaw straight cuts), deburr edges
- [ ] T015 [P] Drill 2× KarlKers 28.6mm holes directly in tote short side HDPE with step bit (top for Charge, below for Heater), deburr HDPE edges
- [ ] T016 [P] Drill 4× ventilation 25-30mm holes in tote HDPE top corners with step bit, deburr edges
- [ ] T017 Cut and install ventilation mesh over 4× vent holes in tote (1/8" or 1/4" grid, 10mm overlap), secure with epoxy/hot glue, verify net free area ~2000-2800mm²
- [ ] T018 Prepare plywood battery base: cut 3/4" plywood to 14.5"×24.5" (fits 15"×25" tote internal dimensions with clearance), pre-drill pilot holes, screw 4 steel strap loops to plywood using included screws at corners or mid-points for cam buckle strap anchoring, place plywood in tote bottom
- [ ] T019 Secure VEVOR battery: position battery in foam (520mm×238mm×218mm = 20.5"×9.4"×8.6") on plywood base lengthwise orientation, cut channels in top foam for M8 terminal access and wire routing clearance, secure with 2× cam buckle straps (6 ft recommended, route across 9.4" width) over battery attached to plywood strap loops (foam distributes pressure across battery top), verify battery cannot move when tote tilted/shaken
- [ ] T020 Mount 100A ANL inline fuse holder to left side plywood panel near top (within 18" wire run from battery+) with screws or zip ties, DO NOT install fuse yet
- [ ] T021 Cut 4 AWG red wire ~4 ft, crimp M8 ring terminal (battery+ end) and ANL lug (holder end), route Battery+ → ANL holder input, verify 105A capacity > 100A fuse
- [ ] T022 Mount Blue Sea 5026 to left side plywood panel with screws through mounting flanges (pre-drill pilot holes), position for accessible busbar/negative bus posts, verify clearances
- [ ] T023 Cut 4 AWG red wire ~1-2 ft, crimp ring terminals, wire ANL holder output → Blue Sea positive busbar on panel, secure with zip ties
- [ ] T024 Mount Victron 500A shunt to left side plywood panel below Blue Sea with screws, shunt stationary for accurate measurement, two sides: "Battery" (battery-) and "System" (loads)
- [ ] T025 Cut 4 AWG black wire segment 1 (~1-2 ft): crimp M8 ring terminal (battery- end) and shunt lug, wire Battery- → Victron shunt battery side
- [ ] T026 Cut 4 AWG black wire segment 2 (~4-6 ft): crimp shunt lugs, wire Victron shunt system side → Blue Sea negative bus (total 4 AWG black 6-8 ft for star grounding)
- [ ] T027 Secure left side plywood panel to tote left wall: drill through tote HDPE + panel edges at 4-6 points, use screws/bolts with washers, verify panel rigid and components accessible
- [ ] T028 Install Victron BMV-712 display into 52mm square cutout in tote right side HDPE, secure with bezel from front, display flush mount
- [ ] T029 Mount Nilight 4-in-1 panel into rectangular cutout in tote right side HDPE (verify fit when arrives), secure per manufacturer instructions (likely snap-in or screws from rear), verify USB-C/USB-A/12V outlet/voltmeter/ON-OFF accessible
- [ ] T030 Route RJ12 cable (~3m) from Victron shunt (left panel) to display (right side) across battery top or around side, plug both ends, secure cable with zip ties along route
- [ ] T031 Optional: Install Victron temperature sensor (adhesive to battery center, plug into shunt temp port) for continuous monitoring

**Checkpoint**: Foundation complete - left plywood panel installed with Blue Sea/Victron shunt, battery secured, displays mounted to right side HDPE, main positive/negative trunks wired, monitoring infrastructure ready. User story circuits can now be wired.

---

## Phase 3: User Story 1 - Safe Manual Power Delivery (Priority: P1) 🎯 MVP

**Goal**: Deliver 12V DC power to heater load with fuse protection and visual status

**Independent Test**: Connect diesel heater (5-10A) to Circuit 2 HEATER output via KarlKers panel connector, verify heater operates, Victron shows voltage 12.8-13.4V and current 5-10A, Nilight voltmeter displays ~13V, weatherproof cover functional

### Implementation for User Story 1

- [ ] T032 [P] [US1] Cut 10 AWG red wire ~3-4 ft: Blue Sea circuit 2 terminal → KarlKers Heater panel connector short side, screw connection at Blue Sea end
- [ ] T033 [P] [US1] Crimp 12 AWG red pigtail 6-12" from 10 AWG to KarlKers included 30A Powerpole red contact using Knoweasy crimper (practice on scrap wire, tug-test)
- [ ] T032 [P] [US1] Cut 10 AWG black wire ~3-4 ft: Blue Sea negative bus → KarlKers Heater panel connector, crimp ring terminal at bus end
- [ ] T033 [P] [US1] Crimp 12 AWG black pigtail 6-12" from 10 AWG to KarlKers included 30A Powerpole black contact
- [ ] T034 [US1] Insert crimped red+black contacts into KarlKers bonded housing (polarity keying prevents reversal), verify contacts seated
- [ ] T035 [US1] Mount KarlKers Heater unit in 28.6mm panel hole (below Charge position), secure with threaded nut from rear (hand-tight + 1/4 turn)
- [ ] T036 [US1] Install KarlKers weatherproof rubber flip-up cover, test flip mechanism, verify seal when closed
- [ ] T037 [US1] Label external panel near connector: "HEATER 10A - 12V OUTPUT" with permanent marker or label maker
- [ ] T038 [US1] Crimp external mating cable: diesel heater wire → 12 AWG → generic Powerpole PP45 red+black bonded pair (mates with KarlKers), label cable "HEATER LOAD"
- [ ] T039 [US1] Prepare 10A ST blade fuse for Blue Sea circuit 2, DO NOT install yet (wait for Step 12 final fuse installation)

**FR-005 Fuse Protection Test** (SC-003):
- [ ] T040 [US1] Wire 10A fuse test circuit: Blue Sea circuit 2 → 10A fuse → variable resistive load (or adjustable power supply in current-limiting mode)
- [ ] T041 [US1] Gradually increase load from 5A → 10A → 12A → 15A (150% rating), observe fuse opens within manufacturer's time-current curve (<10 seconds at 150%)
- [ ] T042 [US1] Verify after fuse opens: no damage to Blue Sea holder, no overheating of 10 AWG wire, no arcing marks, replace fuse and reset

**FR-009 Terminal Labeling Validation**:
- [ ] T043 [US1] Verify all labels clearly state: voltage (12V), polarity (red+ black-), current rating (10A), purpose (HEATER OUTPUT)
- [ ] T044 [US1] Test label visibility from 2 meters distance in normal lighting per SC-005

**Checkpoint**: User Story 1 complete - Heater circuit functional, fuse protection validated, terminals labeled, independent test passed

---

## Phase 4: User Story 2 - Basic State Monitoring (Priority: P2)

**Goal**: Observe battery voltage, SOC%, current, and temperature through Victron BMV-712 and Nilight panel

**Independent Test**: With no load, Victron displays ~13.2V / 100% SOC / 0A / ambient temp, Nilight voltmeter shows ~13.2V. Under 10A load (heater), Victron shows ~13.0V / current 10A / SOC decreasing / temp <40°C, readings accurate within SC-002 ±0.1V

### Implementation for User Story 2

- [ ] T045 [P] [US2] Mount Nilight 4-in-1 panel in front panel 4-6"×2-3" rectangular cutout, secure with included mounting hardware (screws or snap-fit)
- [ ] T046 [P] [US2] Cut 10 AWG red wire ~2-3 ft: Blue Sea circuit 4 terminal → Nilight positive spade terminal, screw connection at Blue Sea end
- [ ] T047 [P] [US2] Crimp female spade terminal on Nilight end (verify spade size 0.25" or 6.3mm per panel specs), verify polarity red=positive
- [ ] T048 [P] [US2] Cut 10 AWG black wire ~2-3 ft: Blue Sea negative bus → Nilight negative spade terminal, crimp ring terminal at bus, spade at panel
- [ ] T049 [US2] Prepare 20A ST blade fuse for Blue Sea circuit 4, DO NOT install yet
- [ ] T050 [US2] Download VictronConnect app on smartphone (iOS/Android), verify Bluetooth pairing with BMV-712 display
- [ ] T051 [US2] Configure Victron via app per quickstart.md Step 9: Battery capacity 200Ah, Charged voltage 14.4V, Tail current 4A, Peukert exponent 1.05, Charge efficiency 95%
- [ ] T052 [US2] Enable Victron alarms: Low voltage 12.4V, Low SOC 30% (diesel heater warning), Critical SOC 20%, High temperature 45°C (if sensor installed)
- [ ] T053 [US2] Perform first Victron SOC sync: Fully charge battery with VEVOR 20A charger to 14.4V, wait for current <4A tail, press "Synchronize to 100%" in app or auto-sync

**FR-014 Voltage Accuracy Validation** (SC-002):
- [ ] T054 [US2] With battery disconnected: measure voltage at battery terminals with calibrated multimeter, record value
- [ ] T055 [US2] Reconnect battery, measure Victron BMV-712 display voltage and Nilight voltmeter voltage
- [ ] T056 [US2] Verify Victron within ±0.1V of multimeter (e.g., multimeter 13.25V → Victron 13.20-13.30V acceptable)
- [ ] T057 [US2] Verify Nilight voltmeter within ±0.2V of multimeter (backup/quick check, less accurate than Victron)

**FR-015 Temperature Measurement**:
- [ ] T058 [US2] If Victron temp sensor installed: verify app displays ambient temperature (e.g., 20-25°C indoor)
- [ ] T059 [US2] If using manual IR thermometer: document procedure in operating instructions - point at battery center, read surface temp, record in log

**FR-016 SOC Estimation Validation**:
- [ ] T060 [US2] Verify Victron app displays SOC% (e.g., 100% after full charge, 98% after 4Ah consumed = 10A for 24 minutes)
- [ ] T061 [US2] Verify Victron time-to-go prediction appears when load connected (e.g., "20.0 hours remaining" at 10A load with 200Ah capacity)
- [ ] T062 [US2] Document in operating instructions: Victron SOC% is accurate (±1% after sync), voltage-only SOC estimates inaccurate (±10-15% due to LiFePO4 flat curve 13.2V from 80%-30%)

**FR-017 Visual Status Indicators** (SC-005):
- [ ] T063 [US2] Verify Nilight ON/OFF LED illuminates when switch pressed (blue LED visible at 2 meters)
- [ ] T064 [US2] Verify Victron display readable from 2 meters: voltage large font, SOC% visible, alarms indicated by blinking or color change
- [ ] T065 [US2] Test low battery warning: Discharge battery to 30% SOC (or adjust alarm threshold in app for testing), verify Victron alarm triggers (audible beep or visual indicator)

**Checkpoint**: User Story 2 complete - Monitoring functional, voltage accuracy ±0.1V validated, SOC% coulomb counting operational, visual indicators readable at 2m, independent test passed

---

## Phase 5: User Story 3 - External AC Charging Support (Priority: P3)

**Goal**: Recharge battery from 120V AC via VEVOR 20A charger through Circuit 1 Charge input

**Independent Test**: Deplete battery to ~50% SOC (13.2V, 100Ah consumed), connect VEVOR charger via adapter cable to Circuit 1 KarlKers Charge panel connector, verify charging current 18-20A bulk phase shown in Victron, voltage rises 13.2V → 14.2V → 14.4V absorption, charger terminates at <4A tail current, Victron auto-syncs to 100% SOC, total charge time ~5-6 hours for 100Ah

### Implementation for User Story 3

- [ ] T066 [P] [US3] Cut 10 AWG red wire ~3-4 ft: Blue Sea circuit 1 terminal → KarlKers Charge panel connector side left top position, screw connection at Blue Sea end
- [ ] T067 [P] [US3] Crimp 12 AWG red pigtail 6-12" from 10 AWG to KarlKers included 30A Powerpole red contact using Knoweasy crimper, tug-test
- [ ] T068 [P] [US3] Cut 10 AWG black wire ~3-4 ft: Blue Sea negative bus → KarlKers Charge panel connector, crimp ring terminal at bus end
- [ ] T069 [P] [US3] Crimp 12 AWG black pigtail 6-12" from 10 AWG to KarlKers included 30A Powerpole black contact
- [ ] T070 [US3] Insert crimped red+black contacts into KarlKers bonded housing, verify contacts seated and polarity correct
- [ ] T071 [US3] Mount KarlKers Charge unit in 28.6mm panel hole (top position above Heater), secure with threaded nut from rear (hand-tight + 1/4 turn)
- [ ] T072 [US3] Install KarlKers weatherproof rubber flip-up cover, test flip mechanism
- [ ] T073 [US3] Label external panel near connector: "CHARGE IN 30A - CHARGER ONLY (DO NOT CONNECT LOADS)" in red text to distinguish input from outputs
- [ ] T074 [US3] Assemble VEVOR charger adapter cable: VEVOR alligator clips red+/black- → 12 AWG wire 3-6 ft → generic Powerpole PP45 red+black bonded pair (mates with KarlKers Charge)
- [ ] T075 [US3] Crimp generic Powerpole contacts to 12 AWG wire opposite alligator clips, tug-test crimps
- [ ] T076 [US3] Label adapter cable: "CHARGER ADAPTER - DO NOT USE FOR LOADS" with heat-shrink label or tape
- [ ] T077 [US3] Verify adapter cable polarity with multimeter: alligator red clip = Powerpole red pin positive (touch multimeter red probe to alligator red, black to alligator black, then verify Powerpole pins match)
- [ ] T078 [US3] Prepare 30A ST blade fuse for Blue Sea circuit 1, DO NOT install yet

**FR-018 to FR-022 AC Charging Validation** (SC-004):
- [ ] T079 [US3] Discharge battery to ~50% SOC (13.2V, 100Ah consumed) using heater load or test resistor at 10A for 10 hours
- [ ] T080 [US3] Document starting conditions: Victron SOC%, voltage, time, ambient temperature
- [ ] T081 [US3] Execute 6-step safe charging procedure per quickstart.md Step 8.5: (1) Plug VEVOR charger into 120V AC outlet, (2) Verify charger output voltage 14.4-14.6V with multimeter before connection, (3) Connect alligator clips to adapter cable (charger side), (4) Connect Powerpole to KarlKers Charge panel connector (battery side), (5) Monitor Victron: expect 18-20A bulk current, voltage rising 13.2V → 14.2V → 14.4-14.6V absorption, (6) When current drops <4A tail current, Victron auto-syncs to 100% SOC
- [ ] T082 [US3] Monitor charging phases with Victron app: Bulk phase (18-20A constant current, voltage rising), Absorption phase (14.4-14.6V constant voltage, current tapering), Float/termination (current <4A, VEVOR charger LED indicates full charge)
- [ ] T083 [US3] Record charge time from 50% to 95% SOC (expected ~5-6 hours for 100Ah at 18-20A average, validate SC-004 charge time documented)
- [ ] T084 [US3] Verify Victron auto-sync to 100% SOC when voltage 14.4V AND current <4A (or manually sync if auto-sync fails)
- [ ] T085 [US3] Monitor temperatures during charging with IR thermometer: VEVOR charger <50°C, Battery surface <40°C (SC-006 thermal validation), Blue Sea terminals <40°C, 10 AWG wiring <40°C
- [ ] T086 [US3] Disconnect in reverse order: (1) Unplug Powerpole from KarlKers panel, (2) Disconnect alligator clips from adapter, (3) Unplug VEVOR from 120V AC
- [ ] T087 [US3] Verify Victron displays 100% SOC, voltage 13.4-13.6V (resting voltage after charge), time-to-go shows "∞" at idle

**FR-013 Reverse Polarity Protection Test**:
- [ ] T088 [US3] With battery DISCONNECTED (for safety): attempt to connect adapter cable with reversed polarity (red to black, black to red)
- [ ] T089 [US3] Verify Powerpole mechanical keying prevents insertion (contacts physically blocked by housing geometry)
- [ ] T090 [US3] Document in operating instructions: "Powerpole connectors are polarized - reversed connection not possible due to contact keying"

**Checkpoint**: User Story 3 complete - Charging circuit functional, adapter cable assembled, charge time validated ~5-6 hours per SC-004, reverse polarity protection confirmed, independent test passed

---

## Phase 6: Integration & Final Assembly

**Purpose**: Complete wiring checks, install all fuses, validate combined system operation

- [ ] T091 Perform Step 11 final wiring check per quickstart.md: Visual inspection (M8 ring terminals torqued 8-10 Nm, Powerpole contacts tug-tested, no bare wire, no sharp edges, zip ties secure, polarity correct red+/black-)
- [ ] T092 Continuity testing with multimeter (battery DISCONNECTED): Battery+ terminal through ANL holder to Blue Sea+ busbar <0.1Ω, Battery- terminal through Victron shunt (both sides) to Blue Sea- bus <0.1Ω
- [ ] T093 [P] Continuity testing each circuit: Blue Sea circuit terminal to panel Powerpole connector <0.5Ω for 10 AWG runs (Circuit 1 Charge, Circuit 2 Heater, Circuit 4 USB panel)
- [ ] T094 CRITICAL CHECK: Verify NO direct connection battery- to loads, all negatives route through Victron shunt system side for star grounding (measure resistance battery- to Blue Sea- bus should show through shunt path only)
- [ ] T095 Short circuit check with multimeter: verify no shorts positive to negative (infinite resistance) at battery terminals, Blue Sea busbar, all Powerpole panel connectors
- [ ] T096 Polarity verification at Powerpole panel connectors: touch multimeter red probe to Powerpole red pin, black to black pin, measure ~13V when battery connected (confirms polarity)
- [ ] T097 Install 100A ANL fuse in inline holder (Battery+ trunk), verify fuse seated and holder closed/latched
- [ ] T098 Install Blue Sea blade fuses in circuit positions: Circuit 1 Charge 30A, Circuit 2 Heater 10A, Circuit 4 USB panel 20A, all fuse holders closed/latched
- [ ] T099 Reconnect battery: positive first (M8 ring terminal to battery+ post, torque 8-10 Nm), negative last (to Victron shunt battery side, torque 8-10 Nm)
- [ ] T100 Initial power-up verification per quickstart.md Phase 2: Victron displays ~13.2V, Nilight ON/OFF test (voltmeter powers on), measure voltages at Powerpole panel connectors (~13.2V at Charge and Heater), check for smoke/heat/alarms (none expected)

**Checkpoint**: Integration complete - all circuits wired, fuses installed, battery connected, initial power-up successful, ready for progressive load testing

---

## Phase 7: Progressive Load Testing & Validation

**Purpose**: Validate system performance under real loads per success criteria SC-001, SC-003, SC-006

**Test 1 - Diesel Heater 5A Simulation** (SC-001 Runtime):
- [ ] T101 Connect diesel heater (or 5A test load) to Circuit 2 Heater Powerpole panel connector via mating cable
- [ ] T102 Record starting conditions: Victron SOC% (e.g., 100%), voltage (e.g., 13.2V), time (e.g., 10:00 AM)
- [ ] T103 Run heater continuously for 1 hour, monitor Victron: current steady ~5A, voltage stable >12.8V, temperature <40°C (battery/Blue Sea/wires with IR thermometer)
- [ ] T104 After 1 hour: Record Victron Ah consumed (expected ~5Ah), SOC% (expected ~97.5% = 200Ah - 5Ah), voltage drop <0.3V (13.2V → ~12.9V under load acceptable)
- [ ] T105 Extrapolate runtime: 5A continuous → 200Ah capacity / 5A = 40 hours to 0% SOC, practical runtime to 30% SOC alarm = 140Ah / 5A = 28 hours (validates SC-001 runtime goal 40+ hours)

**Test 2 - Fridge 10A Simulation** (if Circuit 3 wired in v1.1, otherwise defer):
- [ ] T106 Connect 10A test load (fridge or resistive load) to Circuit 3 (or use Circuit 2 Heater for testing if Fridge not wired yet)
- [ ] T107 Run load for 30 minutes, monitor: voltage drop <0.3V (acceptable under 10A), 10 AWG wire temp <40°C, 15A fuse does NOT blow (10A = 67% rating, safe continuous)
- [ ] T108 Verify Blue Sea terminal connections remain tight, no heat buildup at connections

**Test 3 - Multi-Device 23A Combined Load** (SC-006 Thermal):
- [ ] T109 Connect multiple loads simultaneously to test peak capacity: Heater 8A + Fridge 10A + USB-C 5A = 23A combined (if circuits available, otherwise use test resistors to simulate)
- [ ] T110 Run combined load for 15 minutes steady-state, monitor Victron: current ~23A, voltage >12.8V
- [ ] T111 Thermal check with IR thermometer every 5 minutes: Battery surface <40°C, Blue Sea terminals <40°C, 10 AWG wiring <40°C, 4 AWG main trunks <40°C (validates SC-006 thermal management)
- [ ] T112 Calculate voltage drop: Measure at battery terminals vs. Powerpole panel connectors under 23A load, acceptable <0.5V drop (e.g., 13.0V battery → 12.5V panel acceptable for 10 AWG wire lengths)

**Test 4 - Fuse Interruption Validation** (SC-003):
- [ ] T113 Setup fuse test: Use Circuit 2 Heater (10A fuse) with variable load (adjustable resistor or power supply in current-limiting mode)
- [ ] T114 Gradually increase load: 5A (safe) → 10A (rated) → 12A (120%) → 15A (150% overload)
- [ ] T115 Observe and record: Fuse opens at 150% rating (~15A) within time-current curve (expected <10 seconds for ST blade fuse per manufacturer specs)
- [ ] T116 Verify post-interruption: No damage to Blue Sea fuse holder, no arcing marks, no overheating of 10 AWG wire, no damage to battery (Victron shows no voltage sag)
- [ ] T117 Replace blown fuse, reset circuit, verify operation returns to normal

**Checkpoint**: Load testing complete - runtime validated 40+ hours diesel heater per SC-001, fuse protection per SC-003, thermal management <40°C per SC-006

---

## Phase 8: Field Runtime Validation & Documentation

**Purpose**: Real-world deployment with diesel heater, validate success criteria SC-001, SC-005, SC-007, SC-009, SC-010

**Phase 5 Runtime Test** (SC-001 Full Validation):
- [ ] T118 Deploy battery box to winter camping scenario (or simulate with actual diesel heater in garage for extended test)
- [ ] T119 Connect diesel heater to Circuit 2 Heater output, record starting conditions: Victron 100% SOC, 13.2V, time, ambient temperature
- [ ] T120 Run diesel heater continuously at 5A average (with 8-10A peak cycles during ignition), monitor Victron app: time-to-go prediction, SOC% decay (~1% per 2Ah consumed), current real-time, voltage curve (expect flat ~13.2V from 80% to 30% SOC per LiFePO4 characteristics)
- [ ] T121 Continue operation until 30% SOC alarm triggers (Victron beeps/blinks), record: total runtime hours (expected 28 hours = 140Ah consumed / 5A average), total Ah consumed (expected 140Ah = 70% of 200Ah capacity), lowest voltage reached (expected ~13.0V even at 30% SOC due to flat curve)
- [ ] T122 Export Victron historical data via VictronConnect app: voltage log, current log, SOC log, time log, screenshot at various states (100% SOC start, 50% mid-test, 30% alarm)
- [ ] T123 Validate SC-001: Runtime ≥40 hours at 5A to 0% SOC theoretical (practical 28 hours to 30% alarm = pass, provides safety margin for diesel heater overnight operation)

**Documentation Creation** (SC-007):
- [ ] T124 Create docs/test-results.md per quickstart.md Phase 6: date of tests, ambient temperature, test loads used (heater 5A, combined 23A), measurements (voltage/current/SOC/runtime from Victron), pass/fail status for SC-001 through SC-010
- [ ] T125 Capture photos: internal assembly layout (battery/Blue Sea/Victron/wiring), Victron display at 100% SOC, Victron display during 23A load test, Victron display at 30% SOC alarm, KarlKers panel connectors with labels
- [ ] T126 Capture Victron app screenshots: configuration settings (200Ah/14.4V/4A/alarms), SOC% graph over discharge cycle, voltage graph (showing flat LiFePO4 curve), current graph (showing heater 5A steady with peaks), time-to-go prediction example
- [ ] T127 Document lessons learned: crimping difficulties (which contacts required re-crimp?), wiring routing fit (any wire lengths too short/long?), cutout accuracy (28.6mm KarlKers holes drilling challenges?), Victron SOC validation (did coulomb counting match expected Ah consumed?), Greenmade durability (any cracks/deformation during assembly or transport?)
- [ ] T128 Document v2 upgrade recommendations based on field experience: temperature sensor continuous monitoring (was manual IR sufficient?), status LEDs useful beyond Victron+Nilight (need instant indicators without displays?), solar input demand (how often needed recharging?), Pelican case upgrade needed (Greenmade durability issues?)
- [ ] T129 Document Constitution Principle V mistakes and fixes: "Forgot to order Knoweasy crimper initially, delayed assembly 3 days", "Crimped Powerpole contact incorrectly (wire not fully inserted), re-crimped after tug-test failure", "Victron shunt mounted 5 ft from battery, needed extra 4 AWG black wire", "Drilled 32mm holes before confirming KarlKers 28.6mm size, had to enlarge holes"

**Portability & Safety Validation** (SC-008, SC-010):
- [ ] T130 Test portability: One person lifts and carries battery box by tote handles for 50 feet, verify weight manageable (~28-30kg total), no tools/disassembly required (SC-008 pass)
- [ ] T131 Test transport durability: Secure battery box in vehicle, drive over rough road for 10 miles, inspect: battery straps still tight, Blue Sea 5026 mounting screws secure, KarlKers threaded nuts tight, Victron shunt stationary, no loose wiring
- [ ] T132 Review safety log: Document any incidents during assembly/testing (smoke/sparks/thermal damage/injury), expected SC-010 = zero incidents
- [ ] T133 Validate SC-009: System has completed at least 10 charge/discharge cycles during testing (each camping trip counts), inspect for component degradation (loose connections, cracked solder, fuse holder damage), expected = no failures requiring repair

**Checkpoint**: Field validation complete - runtime 28+ hours to 30% alarm per SC-001, documentation created per SC-007, portability validated per SC-008, safety incidents zero per SC-010, 100 cycles durability path established per SC-009

---

## Phase 9: Polish & Future Planning

**Purpose**: Final refinements and v1.1 expansion planning

- [ ] T134 Create operating instructions document: safe connection of loads (match load current to circuit fuse rating, verify polarity), charging procedure (6-step safe sequence from quickstart.md), storage guidelines (store at 50-80% SOC, recharge every 3 months if unused, disconnect loads during storage), emergency shutdown (pull 100A ANL fuse to isolate battery)
- [ ] T135 Create quick reference card laminated and stored in tote: Circuit labels (Charge 30A input only, Heater 10A output), Victron SOC interpretation (30% alarm = recharge soon, 20% critical = stop loads immediately, voltage unreliable for SOC), emergency contacts (battery manufacturer VEVOR support, local electrician if troubleshooting needed)
- [ ] T136 Label all fuses: Tape labels on Blue Sea 5026 fuse holder positions: "1-CHARGE 30A", "2-HEATER 10A", "4-USB 20A", "3/5/6-SPARE", 100A ANL labeled "MAIN 100A"
- [ ] T137 Create v1.1 expansion task list based on field validation: (1) Evaluate KarlKers performance (mounting ease, weather seal, vibration resistance, drilling accuracy with 1-1/8" hole saw), (2) Decision: order 3 more KarlKers units (~$45) OR use generic Powerpole with 32mm holes (~$10-15) OR external cables ($0), (3) Wire Circuit 3 Fridge 15A, Circuit 5 Spare 20A, Circuit 6 Spare 15A when needed
- [ ] T138 Plan v2 upgrades based on lessons learned: Pelican case if Greenmade shows UV degradation/needs better protection ($100-200), solar input Circuit 7 if frequent recharging needed (solar controller + panel $150-300), inverter Circuit 8 if AC loads needed (300W pure sine inverter $100-150), automated heating control if diesel heater PID loop desired (Arduino + relay + temp sensor $50-100), 3-LED status panel if instant indicators more useful than displays ($20-40)
- [ ] T139 Commit all documentation to git repository: specs/001-battery-box/docs/test-results.md, wiring-diagram.png (photo or sketch), operating-instructions.md, lessons-learned.md, v1.1-expansion-plan.md, v2-upgrade-ideas.md
- [ ] T140 Update constitution with lessons learned: any new principles discovered during Battery Box v1? (e.g., "Always prototype connector holes before drilling production enclosure", "Budget 20% contingency for wire length miscalculations", "Test crimps on scrap wire before production connectors")

**Checkpoint**: Polish complete - operating instructions created, quick reference card laminated, v1.1 expansion path defined, v2 upgrade ideas documented, constitution updated with lessons learned

---

## Dependencies & Execution Strategy

### Critical Path (Sequential - Cannot Parallelize)
1. **T001-T009** (Procurement) → **T010-T029** (Foundation) → **All User Story Tasks** → **T091-T100** (Integration) → **T101-T140** (Testing & Docs)

### User Story Independence
- **User Story 1 (Heater Circuit)**: T030-T044 can execute independently after Foundation complete
- **User Story 2 (Monitoring)**: T045-T065 can execute in parallel with US1 (different components: Nilight panel vs Heater circuit)
- **User Story 3 (Charging)**: T066-T090 can execute in parallel with US1/US2 (different component: Charge circuit independent of Heater/Monitoring)

### Parallel Opportunities (Tasks marked [P])
- **Procurement**: T005 (core electrical), T006 (Victron), T007 (consumables) can all order simultaneously
- **Drilling**: T013 (Victron), T014 (KarlKers), T015 (ventilation) can drill simultaneously if multiple people or careful fixture planning
- **User Story Implementations**: After Foundation (T029), US1/US2/US3 tasks can proceed in parallel on different circuits

### Suggested Execution Plan
1. **Week 1**: Procurement (T001-T009) - order all parts, receive existing components, prepare workspace
2. **Week 2**: Foundation (T010-T029) - enclosure prep, battery mounting, main trunks wiring, monitoring infrastructure (MUST complete before user stories)
3. **Week 3**: User Stories in parallel - one person per story OR sequence P1 → P2 → P3 (US1 Heater circuit, US2 Monitoring config, US3 Charging circuit)
4. **Week 4**: Integration (T091-T100) - final wiring checks, fuse installation, initial power-up, progressive load testing (T101-T117)
5. **Week 5**: Field validation (T118-T133) - deploy to winter camping, 28-hour runtime test, documentation creation
6. **Week 6**: Polish (T134-T140) - operating instructions, labels, v1.1 planning, git commit all docs

### MVP Scope (Minimum Viable Product)
- **Phase 1 + 2 + User Story 1 only** = functional battery box with heater circuit, fuse protection, manual monitoring (Nilight voltmeter), no Victron/no charging circuit
- **Recommendation**: Include User Story 2 (Victron BMV-712) in MVP - critical for diesel heater winter camping safety (SOC% accuracy prevents overnight shutdown)

---

## Summary

**Total Tasks**: 140 tasks organized into 9 phases  
**User Stories**: 3 stories (P1 Heater power delivery, P2 Monitoring, P3 AC charging)  
**Estimated Effort**: 40-60 hours over 4-6 weeks (includes procurement delays, assembly time, testing duration, documentation)  
**Parallel Opportunities**: 15 tasks marked [P] can execute simultaneously  
**MVP Path**: Phases 1-2-3-4-6 (Foundation + US1 Heater + US2 Monitoring + Integration) delivers functional winter camping power box

**Success Criteria Validation Mapped**:
- SC-001 Runtime: T105, T118-T123 (40+ hours diesel heater)
- SC-002 Voltage Accuracy: T054-T057 (±0.1V)
- SC-003 Fuse Protection: T040-T042, T113-T117
- SC-004 Charge Time: T079-T087 (7.5 hours full charge)
- SC-005 Visual Indicators: T044, T063-T065 (2m visibility)
- SC-006 Temperature: T103, T111, T085 (<40°C under load)
- SC-007 Documentation: T124-T129
- SC-008 Portability: T130-T131 (one person)
- SC-009 Durability: T133 (100 cycles)
- SC-010 Safety: T132 (zero incidents)

**Next Action**: Begin T001 - verify VEVOR battery received and inspect for shipping damage
