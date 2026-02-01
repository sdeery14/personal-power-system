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
4. [Wiring Diagrams](#4-wiring-diagrams)
5. [Assembly Steps](#5-assembly-steps)
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
- **Wire strippers**: For AWG wire sizes in use (4 AWG, 10 AWG, 12 AWG)
- **Powerpole Crimper**: Knoweasy Powerpole crimper (PP15/30/45, ratcheting, contact positioner, $30-50)
- **Ring Terminal Crimper**: Ratcheting crimper for 4 AWG M8 ring terminals (NOT pliers - proper crimp essential)
- **Screwdrivers**: Phillips and flathead for Blue Sea 5026 mounting, self-tapping screws
- **Drill**: Variable speed with 52mm hole saw (Victron display), 32mm step bit/hole saw (Powerpole connectors 4-5×), 25-30mm bit (ventilation 4×)
- **Jigsaw or Rotary Tool**: For Nilight panel cutout 4-6"×2-3" rectangular (verify exact dimensions when panel received)
- **Deburring tool**: Remove sharp edges from drilled HDPE holes
- **Heat gun** (optional): For heat-shrink tubing on ring terminals
- **Torque wrench or socket set**: For battery M8 terminal bolts (8-10 Nm torque)

### Consumable Materials

- **Wire**: TXL or GXL automotive wire, 105°C rated
  - 4 AWG red (main positive trunk): 4 ft (Battery+ → ANL → Blue Sea+)
  - 4 AWG black (main negative trunk): 6-8 ft (Battery- → Victron shunt → Blue Sea-) **CRITICAL**
  - 10 AWG red (circuit wiring): 25 ft (Blue Sea+ terminals to Powerpole connectors, 6 circuits)
  - 10 AWG black (circuit wiring): 25 ft (same routing as red for star grounding)
  - 12 AWG red (Powerpole pigtails): 20 ft (Powerpole contact pigtails, 10 pairs)
  - 12 AWG black (Powerpole pigtails): 20 ft (same as red)
  - 18-22 AWG (Victron sensing): 10 ft (RJ12 cable included, optional temp sensor wire)
- **Ring terminals**: M8 for battery posts (4 AWG wire), insulated/heat-shrink covered
- **Powerpole contacts**: PP45-compatible contacts for 10 AWG/12 AWG wire (included with connector pairs)
- **Heat-shrink tubing**: Various sizes for ring terminals and wire splices
- **Zip ties**: Cable management inside Greenmade tote (various sizes, UV-resistant)
- **Electrical tape**: Temporary insulation, wire bundling
- **Labels**: Powerpole connector labels ("HEATER 10A", "FRIDGE 15A", "SPARE 20A", "SPARE 15A", "CHARGE IN 30A")

### Specialized Parts (from Component List)

See [Section 3: Component Checklist](#3-component-checklist)

---

## 3. Component Checklist

Verify all components before starting assembly:

### Core Components

- [ ] **Battery**: VEVOR 200Ah 12V LiFePO4 (model 010230251465), 520×238×218mm, 25kg, M8 posts, 100A BMS integrated, purchased 2026-01-18
- [ ] **Enclosure**: Greenmade 27-gallon storage tote, 30.4"L × 20.4"W × 14.7"H external, ~28"×18"×13" internal, HDPE, snap-lock latches, molded handles
- [ ] **Main Fuse**: 100A ANL fuse (32V DC rated, matches BMS rating)
- [ ] **Main Fuse Holder**: Inline ANL fuse holder (within 18" of battery+)
- [ ] **Fuse Block**: Blue Sea Systems 5026 (12 circuits, 100A busbar, ST blade fuses, common negative bus)
- [ ] **Circuit Fuses**: Blade fuse assortment - 10A (2×), 15A (3×), 20A (2×), 30A (2×) + spares

### Connectors

- [ ] **Panel-mount connectors** (2× KarlKers for Charge/Heater + generic Powerpole for remaining):
  - 2× KarlKers panel-mount Powerpole units (ASIN B0F4L5FYQ2, $14.99 each = ~$30)
    - Includes: housing, bonded red+black connector, 30A contacts, weather cover, threaded nut
    - For Circuit 1 Charge In (30A) and Circuit 2 Heater (10A)
  - 8× generic Anderson Powerpole PP45 bonded pairs (~$20-30)
    - 3× pairs for Fridge/Spare circuits (panel or external use - decide during assembly)
    - 5× pairs for cable ends to mate with KarlKers + other circuits
  - Purchase: Amazon - KarlKers B0F4L5FYQ2, generic Powerpole contact sets
- [ ] **Charging Adapter Cable**: VEVOR charger alligator clips → 12 AWG wire 3-6 ft → Powerpole PP45 (DIY assemble or pre-made)

### Monitoring Components

- [ ] **Battery Monitor**: Victron BMV-712 Smart kit (500A/50mV shunt, 52mm×52mm display, RJ12 cable, Bluetooth, optional temperature sensor)
- [ ] **Panel**: Nilight 4-in-1 (USB-C PD 100W, USB-A QC 3.0, 12V outlet, integrated LED voltmeter, ON/OFF switch, female spade terminals)
- [ ] **Temperature Sensor**: Manual IR thermometer (-20 to 80°C, ±0.5-1.0°C) + optional Victron temperature sensor (adhesive-backed, plugs into shunt)
- [ ] **Status Indicators**: Nilight panel ON/OFF LED + Victron BMV-712 display with alarms (defer custom 3-LED system to v2)

### Hardware

- [ ] **Battery Straps**: 2× ratchet straps for securing battery (bolted to tote bottom)
- [ ] **Mounting Hardware**: Self-tapping screws for Blue Sea 5026 side wall mounting, bolts for strap anchors
- [ ] **Cable Management**: Zip ties (various sizes), adhesive cable anchors for tote walls
- [ ] **Ventilation Mesh**: Stainless steel or aluminum mesh, 1/8" or 1/4" grid, 4× pieces for 25-30mm vent holes

### External Equipment (Not in Enclosure)

- [ ] **AC Charger**: VEVOR 20A LiFePO4 charger (model 010889683485), 14.6V absorption, alligator clips output, purchased
- [ ] **Test Loads**: 12V automotive bulb (5-10W), 12V fan (~5A), diesel heater (~8A), or electronic load (variable 0-30A)

---

## 4. Wiring Diagrams

**Purpose**: Complete electrical wiring reference for battery box v1

This section covers all wiring: main power distribution (battery to fuse block) and individual circuits (fuse block to loads). Use these diagrams during assembly and for future troubleshooting.

### 4.1 Main Trunk Wiring Overview

The main trunk wiring connects the battery to the Blue Sea 5026 fuse block through protective fusing (ANL) and monitoring (Victron shunt). All current flows through these components for safety and accurate state-of-charge tracking.

```
BATTERY 200Ah (M8 posts)
   |
   ├─[+]─────(4 AWG red)─────[M8 ring]───► ANL Holder INPUT
   │                                                  │
   │                                          [100A ANL Fuse]
   │                                                  │
   │                                     ANL Holder OUTPUT
   │                                                  │
   │                      (4 AWG red)────────────────┘
   │                                │
   │                                └───[ring]──► Blue Sea POSITIVE BUS
   │                                                  │
   │                                              [Circuits 1-6]
   │
   └─[-]─────(4 AWG black)────[M8 ring]──► Victron Shunt "BATTERY -"
                                                     │
                                           [500A Shunt measures ALL current]
                                                     │
                        (4 AWG black)────────────────┘
                                  │
                                  └────[ring]──► Blue Sea NEGATIVE BUS
                                                      │
                                                  [Circuits 1-6]
```

### 4.2 Wire Specifications

| Wire                 | From              | To                | Recommended Length  | Wire Gauge  | Terminal Type                       |
| -------------------- | ----------------- | ----------------- | ------------------- | ----------- | ----------------------------------- |
| **Positive Trunk 1** | Battery+ post     | ANL holder input  | Measure + 12" slack | 4 AWG red   | M8 ring (battery), match ANL stud   |
| **Positive Trunk 2** | ANL holder output | Blue Sea+ busbar  | Measure + 8" slack  | 4 AWG red   | Match ANL stud, match busbar stud   |
| **Negative Trunk 1** | Battery- post     | Shunt "BATTERY -" | Measure + 12" slack | 4 AWG black | M8 ring (battery), match shunt stud |
| **Negative Trunk 2** | Shunt "SYSTEM -"  | Blue Sea- bus     | Measure + 8" slack  | 4 AWG black | Match shunt stud, match busbar stud |

### 4.3 Measured Wire Lengths (Fill in during assembly)

**MEASURE BEFORE CUTTING!** Use string or tape measure along actual wire route path.

- [ ] Battery+ to ANL input: **\_\_\_\_** inches actual + 12" slack = **\_\_\_\_** total
- [ ] ANL output to Blue Sea+: **\_\_\_\_** inches actual + 8" slack = **\_\_\_\_** total
- [ ] Battery- to Shunt BATT: **\_\_\_\_** inches actual + 12" slack = **\_\_\_\_** total
- [ ] Shunt SYS to Blue Sea-: **\_\_\_\_** inches actual + 8" slack = **\_\_\_\_** total

**Note**: For components mounted on same panel (ANL → Blue Sea, Shunt → Blue Sea), actual distance may be only 4-12 inches. Add 6-8" slack for service access. Do NOT use excessive wire length.

### 4.4 Terminal Sizes (Verify before ordering/crimping)

Common terminal sizes (verify with calipers or component documentation):

| Component            | Stud Type  | Common Size   | Verify Your Parts  |
| -------------------- | ---------- | ------------- | ------------------ |
| VEVOR Battery posts  | M8 bolt    | 8mm (5/16")   | ☐ Measured: **\_** |
| ANL holder studs     | M8 or 1/4" | 8mm or 6.35mm | ☐ Measured: **\_** |
| Blue Sea 5026 busbar | 1/4" or M6 | 6.35mm or 6mm | ☐ Measured: **\_** |
| Victron shunt studs  | M8         | 8mm (5/16")   | ☐ Measured: **\_** |

**Tip**: M8 (8mm) and 5/16" (7.94mm) are interchangeable. M6 (6mm) and 1/4" (6.35mm) are interchangeable.

### 4.5 Crimping with Sanuke/Solsop Hydraulic Tool

**Die Selection**: Use **25mm² die** for 4 AWG wire (equivalent gauge)

**Steps**:

1. Strip wire 1/2" (12-15mm) of insulation
2. Insert stripped wire fully into ring terminal barrel until wire bottoms out
3. Rotate crimper head to 25mm² position (spring-loaded locking pin holds position)
4. Place terminal in crimper jaws at 25mm² die location
5. Squeeze handles - ratchet mechanism engages
6. Continue squeezing through 2-3 pumps until ratchet releases (full crimp)
7. Remove terminal, inspect crimp (should be hexagonal indent, wire cannot rotate in barrel)
8. **Tug test**: Pull hard on wire - should require 50+ lbs force to extract (will not come out with hand pull)
9. Optional: Slide heat-shrink tubing over crimp, apply heat gun until tubing shrinks tight

### 4.6 Connection Sequence (CRITICAL - Follow this order!)

**⚠️ SAFETY: Do NOT install 100A ANL fuse until ALL wiring complete and verified!**

**Phase 1: Crimp all terminals** (fuse still out, no power)

- [ ] Crimp all 4 wires with appropriate terminals
- [ ] Verify all crimps pass tug test
- [ ] Apply heat-shrink if desired

**Phase 2: Connect negative first** (establishes ground reference, safer)

- [ ] Battery- → Shunt "BATTERY -" side (M8 ring terminal, torque 8-10 Nm or hand-tight + 1/4 turn)
- [ ] Shunt "SYSTEM -" side → Blue Sea negative bus
- [ ] Verify no loose wires, all connections tight

**Phase 3: Connect positive second** (fuse still OUT = no power flow yet)

- [ ] Battery+ → ANL holder input (M8 ring terminal, torque 8-10 Nm)
- [ ] ANL holder output → Blue Sea positive busbar
- [ ] **VERIFY: 100A ANL fuse is REMOVED from holder** (open circuit, no current flow)

**Phase 4: Verify before power-up**

- [ ] All terminals tight (snug but not over-torqued - 8-10 Nm or hand-tight + 1/4 turn)
- [ ] No bare wire exposed (heat-shrink or electrical tape covers crimps)
- [ ] Positive and negative wires do NOT touch anywhere
- [ ] Panel secure, components not loose

**Phase 5: First power-up** (after all circuit wiring complete - see Step 12)

- [ ] Insert 100A ANL fuse into holder (may spark slightly - normal)
- [ ] Blue Sea busbar should now show ~13.3V (check with multimeter)
- [ ] Victron display should power on and show battery voltage
- [ ] Nilight panel ON switch should illuminate voltmeter

### 4.7 Voltage Drop Verification (Optional but recommended)

**Why**: Verify wire gauge and crimp quality are adequate for 100A capacity

**Procedure**:

1. Connect 30A test load (diesel heater = ~8A, multiple loads to reach 30A)
2. Measure voltage at battery terminals with multimeter: V_batt
3. Measure voltage at Blue Sea busbar with multimeter: V_bus
4. Calculate drop: V_drop = V_batt - V_bus
5. **Acceptable**: <0.3V drop at 30A load, <0.5V drop at 60A load
6. **If excessive drop**: Check crimp quality, verify wire gauge, check terminal tightness

### 4.8 Circuit Wiring Diagram (Blue Sea → Loads)

**Purpose**: Shows how each circuit connects from Blue Sea 5026 fuse block to individual loads

```
BLUE SEA 5026 FUSE BLOCK
├─ POSITIVE BUS (from ANL fuse)
│   │
│   ├─ Circuit 1 [30A fuse] ──(10 AWG red ~3-4 ft)──► KarlKers "CHARGE IN"
│   │                                                   (Powerpole contact)
│   │
│   ├─ Circuit 2 [10A fuse] ──(12 AWG red ~3-4 ft)──► KarlKers "HEATER"
│   │                                                   (Powerpole contact)
│   │
│   ├─ Circuit 3 [15A fuse] ──(12 AWG red)──────────► FRIDGE (deferred v1.1)
│   │                                                   (Powerpole contact)
│   │
│   ├─ Circuit 4 [20A fuse] ──(10 AWG red ~2-3 ft)──► Nilight Panel +
│   │                                                   (spade terminal)
│   │
│   ├─ Circuit 5 [20A fuse] ──(10 AWG red)──────────► SPARE (deferred v1.1)
│   │                                                   (Powerpole contact)
│   │
│   └─ Circuit 6 [15A fuse] ──(12 AWG red)──────────► SPARE (deferred v1.1)
│                                                       (Powerpole contact)
│
└─ NEGATIVE BUS (from Victron shunt "SYSTEM -")
    │
    ├─────────────────(10 AWG black ~3-4 ft)────────► KarlKers "CHARGE IN"
    │                                                   (Powerpole contact)
    │
    ├─────────────────(12 AWG black ~3-4 ft)────────► KarlKers "HEATER"
    │                                                   (Powerpole contact)
    │
    ├─────────────────(12 AWG black)────────────────► FRIDGE (deferred v1.1)
    │                                                   (Powerpole contact)
    │
    ├─────────────────(12 AWG black ~2-3 ft)────────► Powerpole PP45 ──► Nilight Panel -
    │                                                   (12 AWG bare wire)
    │
    ├─────────────────(10 AWG black)────────────────► SPARE (deferred v1.1)
    │                                                   (Powerpole contact)
    │
    └─────────────────(12 AWG black)────────────────► SPARE (deferred v1.1)
                                                        (Powerpole contact)
```

**CRITICAL**: All negative wires connect to Blue Sea negative bus (NOT directly to battery). This maintains star grounding through Victron shunt for accurate current measurement.

### 4.9 Circuit Wire Specifications

| Circuit # | Load            | Fuse Size | Wire Gauge | Positive From      | Negative From | Connector Type                      |
| --------- | --------------- | --------- | ---------- | ------------------ | ------------- | ----------------------------------- |
| **1**     | Charge Input    | 30A       | 10 AWG     | Circuit 1 terminal | Negative bus  | KarlKers Powerpole (PP45)           |
| **2**     | Heater Output   | 10A       | 12 AWG     | Circuit 2 terminal | Negative bus  | KarlKers Powerpole (PP45)           |
| **3**     | Fridge (future) | 15A       | 12 AWG     | Circuit 3 terminal | Negative bus  | Powerpole (deferred v1.1)           |
| **4**     | USB Panel       | 20A       | 12 AWG     | Circuit 4 terminal | Negative bus  | Powerpole PP45 (Nilight has 12 AWG) |
| **5**     | Spare (future)  | 20A       | 10 AWG     | Circuit 5 terminal | Negative bus  | Powerpole (deferred v1.1)           |
| **6**     | Spare (future)  | 15A       | 12 AWG     | Circuit 6 terminal | Negative bus  | Powerpole (deferred v1.1)           |

### 4.10 Terminal Types for Circuit Wiring

**At Blue Sea 5026 End (#10-32 studs):**

- Use TICONN heat-shrink ring terminals with #10 holes
- Red terminals: 10 AWG wire
- Blue or yellow terminals: 12 AWG wire
- Crimp with ratchet crimper, heat-shrink seal

**At Powerpole End (Circuits 1, 2, 4, and future circuits 3, 5, 6):**

- Use PP45 contacts from KarlKers (30A rated) or generic Powerpole kit
- Crimp with Knoweasy Powerpole crimper
- Insert into bonded red+black housing (keyed, prevents reverse polarity)
- Circuit 4 note: Nilight wire side uses same PP45 contacts crimped to its bare wires

**At Nilight Panel End (Circuit 4):**

- Nilight comes with 12 AWG wire and bare wire ends (red positive, black negative)
- Crimp PP45 contacts directly onto Nilight's bare wires using Knoweasy crimper
- Insert crimped contacts into PP45 housings (red housing for +, black for -)
- This creates serviceable Powerpole junction between Nilight and fuse box wiring
- Run 12 AWG from Blue Sea to Powerpole junction (Nilight's 12 AWG is limiting factor for circuit)

### 4.11 Circuit Wiring Checklist (Fill in during assembly)

**Phase 1 Circuits (v1 initial build):**

- [ ] Circuit 1 (Charge): Measured length **\_** + slack = **\_** cut
- [ ] Circuit 2 (Heater): Measured length **\_** + slack = **\_** cut
- [ ] Circuit 4 (USB Panel): Measured length **\_** + slack = **\_** cut

**Phase 2 Circuits (v1.1 after field validation):**

- [ ] Circuit 3 (Fridge): Measured length **\_** + slack = **\_** cut
- [ ] Circuit 5 (Spare 20A): Measured length **\_** + slack = **\_** cut
- [ ] Circuit 6 (Spare 15A): Measured length **\_** + slack = **\_** cut

**Wire Routing Notes:**

- Bundle positive and negative wires together with zip ties every 6-12"
- Avoid sharp bends (minimum 1" radius for 10/12 AWG)
- Keep wires away from sharp edges, moving parts
- Use grommets if passing through holes
- Label each Powerpole connector at both ends

---

## 5. Assembly Steps

### Step 1: Prepare Enclosure

**1.1 Plan component layout**

- Sketch layout on paper: battery position, connector locations, Victron + Nilight panel positions
- Battery at bottom center (low center of gravity, VEVOR 200Ah: 520×238×218mm fits with 7.5" front, 8.5" side, 4.5" top clearances)
- Connectors on side panel left vertical row (4-5× Powerpole cable access)
- Nilight panel on front panel center (visibility), Victron display front panel right of Nilight
- Blue Sea 5026 on side wall left near battery (accessible from top for fuse replacement)

**1.2 Mark and drill cutouts on Greenmade 27gal tote**

- [ ] **Nilight panel**: Mark 4-6"×2-3" rectangular cutout on front panel center upper third (verify exact dimensions when panel received)
- [ ] **Victron display**: Mark 52mm×52mm square cutout on front panel right of Nilight
- [ ] **Powerpole connectors** (incremental v1 approach):
  - **Phase 1 (2× KarlKers units)**: Mark 2× 1-1/8" (28.6mm) diameter holes on side panel left, top positions
    - Top: "CHARGE IN 30A" (Circuit 1)
    - Below: "HEATER 10A" (Circuit 2)
    - Use 1-1/8" hole saw or 28-30mm step bit
  - **Phase 2 (deferred to v1.1 after field validation)**: Mark 3× additional holes for Fridge/Spare circuits
    - Option A: 28.6mm holes if adopting 3 more KarlKers units
    - Option B: 32mm holes if using generic Powerpole with rubber grommets
    - Option C: Skip panel-mount, use external cable connections
- [ ] **Ventilation**: Mark 4× 25-30mm diameter holes on top corners (2 front, 2 rear for cross-flow)

**1.3 Drill holes in HDPE tote**

- [ ] **Nilight cutout**: Drill pilot holes at 4 corners, use jigsaw or rotary tool to cut rectangular opening
- [ ] **Victron cutout**: Use 52mm hole saw OR drill 4 corner pilot holes + jigsaw to cut square
- [ ] **Powerpole holes**: Use 32mm step bit or 32mm hole saw for 4-5 connector holes
- [ ] **Ventilation holes**: Use 25-30mm bit for 4 vent holes
- [ ] Deburr all holes (remove sharp HDPE edges with deburring tool or sandpaper)
- [ ] Test-fit Nilight panel, Victron display, Powerpole connectors before proceeding

**1.4 Install ventilation mesh**

- [ ] Cut stainless steel or aluminum mesh (1/8" or 1/4" grid) to cover 25-30mm vent holes with 10mm overlap
- [ ] Secure with epoxy, hot glue, or small screws/washers
- [ ] Net free area ~2000-2800mm² (exceeds 500mm² minimum for hydrogen off-gassing)

### Step 2: Mount Battery

**2.1 Position VEVOR 200Ah battery**

- [ ] Place battery in Greenmade tote (centered at bottom)
- [ ] Verify dimensions: 520×238×218mm (20.5"×9.4"×8.6") fits in ~28"×18"×13" internal tote
- [ ] Verify clearances: 7.5" front, 8.5" side, 4.5" top (sufficient for wiring and Blue Sea 5026 mounting)
- [ ] Battery terminals (M8 posts) accessible from top

**2.2 Secure battery (CRITICAL - prevents movement during transport)**

- [ ] Use 2× ratchet straps across top of battery
- [ ] Anchor straps via drilled holes + bolts through Greenmade tote bottom (4 anchor points)
- [ ] Alternative: If tote has molded ribs, route straps under ribs (may not be as secure)
- [ ] Verify battery cannot move when tote tilted or shaken (28-30kg total weight portable)

### Step 3: Install Main Fuse Holder

**3.1 Mount 100A ANL inline fuse holder**

- [ ] Position inline ANL fuse holder within 18" of battery positive terminal (NEC best practice)
- [ ] Secure with zip ties or mounting bracket to tote side wall
- [ ] **DO NOT install 100A ANL fuse yet** (fuse installed last after all wiring complete)

**3.2 Prepare 4 AWG main positive trunk wiring**

- [ ] Cut 4 AWG red wire: Battery+ → ANL fuse holder input (~4 ft total including routing)
- [ ] Strip wire ends 10-12mm
- [ ] Crimp M8 ring terminal on battery end (insulated/heat-shrink covered, torque 8-10 Nm when installed)
- [ ] Crimp ANL fuse holder lug on other end (or ring terminal if fuse holder has stud)
- [ ] Current capacity: 4 AWG = 105A at 40°C (exceeds 100A fuse rating, voltage drop <0.1V at 100A over 4 ft)

### Step 4: Mount Blue Sea 5026 Fuse Block

**4.1 Mount Blue Sea Systems 5026**

- [ ] Position on Greenmade tote side wall left near battery (accessible from top for fuse replacement)
- [ ] Secure with self-tapping screws through Blue Sea mounting flanges into HDPE tote wall
- [ ] Verify 100A positive busbar post and negative bus post accessible

**4.2 Wire main positive trunk to Blue Sea**

- [ ] Cut 4 AWG red wire: ANL fuse holder output → Blue Sea 5026 positive busbar post (~1-2 ft)
- [ ] Crimp ring terminal or lug for busbar stud connection
- [ ] Route wire cleanly along tote wall, secure with zip ties

**4.3 Prepare main negative trunk (CRITICAL for star grounding)**

- [ ] **DO NOT connect battery negative directly to Blue Sea negative bus**
- [ ] Main negative trunk will route: Battery- → Victron shunt battery side → Victron shunt system side → Blue Sea- negative bus
- [ ] This ensures ALL current (charge + loads) flows through Victron shunt for accurate SOC tracking
- [ ] See Step 5 for Victron shunt installation and negative trunk wiring

### Step 5: Install Victron BMV-712 Battery Monitor

**5.1 Mount 500A shunt on side wall**

- [ ] Position Victron 500A/50mV shunt on tote side wall near battery negative terminal (minimize 4 AWG wire length)
- [ ] Secure with screws or adhesive (shunt must be stationary for accurate measurement)
- [ ] Shunt has two sides: "Battery" side (connects to battery-) and "System" side (connects to Blue Sea- bus and all loads)

**5.2 Wire main negative trunk through shunt (CRITICAL)**

- [ ] Cut 4 AWG black wire segment 1: Battery- → Victron shunt battery side (~1-2 ft)
- [ ] Crimp M8 ring terminal on battery end, crimp shunt lug on other end
- [ ] Cut 4 AWG black wire segment 2: Victron shunt system side → Blue Sea negative bus (~4-6 ft total routing)
- [ ] Crimp shunt lug on shunt end, crimp ring terminal on Blue Sea bus end
- [ ] **Total 4 AWG black: 6-8 ft** (longer than positive side because of shunt routing)
- [ ] **VERIFY: ALL circuit negative wires will connect to Blue Sea negative bus, NOT directly to battery**
- [ ] This star grounding architecture ensures accurate coulomb counting (all current through shunt)

**5.3 Mount Victron display on front panel**

- [ ] Insert Victron BMV-712 display into 52mm×52mm square cutout (front panel right of Nilight)
- [ ] Secure with included bezel from front side
- [ ] Display mounts flush with panel surface

**5.4 Connect RJ12 cable from shunt to display**

- [ ] Plug RJ12 cable (included, ~3 meters) into Victron shunt RJ12 port
- [ ] Route cable cleanly from side wall shunt to front panel display
- [ ] Plug other end into Victron display RJ12 port
- [ ] Secure cable with zip ties along route

**5.5 Optional temperature sensor**

- [ ] If using Victron temperature sensor: Adhesive-backed sensor on battery case center
- [ ] Plug sensor into Victron shunt temperature port
- [ ] Enables continuous temperature monitoring via VictronConnect app
- [ ] Alternative: Use manual IR thermometer (procedure in testing section)

**For each output circuit:**

### Step 6: Wire Output Circuits (Heater with KarlKers, Fridge/Spare deferred)

**6.1 Circuit 2 (Heater - 10A) - KarlKers panel-mount**

- [ ] Install 10A ST blade fuse in Blue Sea circuit 2 position (**DO NOT install yet**, wait for Step 12)
- [ ] Cut 10 AWG red wire: Blue Sea circuit 2 terminal → KarlKers panel connector (~3-4 ft to side panel)
- [ ] Blue Sea end: Screw connection to circuit 2 positive terminal
- [ ] Crimp 12 AWG red pigtail (6-12") from 10 AWG to KarlKers included 30A Powerpole red contact
- [ ] Use Knoweasy Powerpole crimper, practice on scrap wire first, tug-test (should not pull out)
- [ ] Cut 10 AWG black wire: Blue Sea negative bus → KarlKers panel connector (~3-4 ft)
- [ ] Blue Sea end: Ring terminal to negative bus post
- [ ] Crimp 12 AWG black pigtail (6-12") from 10 AWG to KarlKers included 30A Powerpole black contact
- [ ] Insert crimped red+black contacts into KarlKers bonded housing (polarity keying prevents reversal)
- [ ] Mount KarlKers unit in 28.6mm panel hole, secure with threaded nut from rear (hand-tight + 1/4 turn)
- [ ] Install weatherproof rubber flip-up cover
- [ ] Label external panel: "HEATER 10A - 12V OUTPUT"

**6.2 Circuit 3 (Fridge - 15A) - DEFERRED to v1.1**

- [ ] **Decision point after field testing Charge/Heater circuits**:
  - Option A: Order 1 more KarlKers unit, drill 28.6mm hole, mount same as Circuit 2
  - Option B: Use generic Powerpole with 32mm hole + rubber grommet
  - Option C: External cable connection (Blue Sea terminal → 10 AWG → cable-end Powerpole, no panel hole)
- [ ] Wire when ready: Blue Sea circuit 3 (15A fuse) → 10 AWG red/black → Powerpole connector

**6.3 Circuits 5 & 6 (Spare 20A, Spare 15A) - DEFERRED to v1.1**

- [ ] Reserve for future loads after validating v1 field performance
- [ ] Can add panel-mount (KarlKers or generic) or external cables based on needs
- [ ] Wire when ready: Blue Sea circuits 5/6 → 10 AWG → Powerpole connectors

### Step 7: Wire Nilight 4-in-1 Panel (Blue Sea Circuit 4)

**7.1 Circuit 4 fuse installation**

- [ ] Circuit 4 (USB panel 20A): Install 20A ST blade fuse in Blue Sea position 4
- [ ] **DO NOT install fuse yet** (fuse installed last)

**7.2 Mount Nilight panel in front panel cutout**

- [ ] Insert Nilight 4-in-1 panel into 4-6"×2-3" rectangular cutout from front
- [ ] Secure with included mounting hardware (screws or snap-fit depending on panel design)
- [ ] Panel provides: USB-C PD (100W), USB-A QC 3.0 (2.1A), 12V cigarette outlet, integrated LED voltmeter, ON/OFF switch

**7.3 Positive wire run (10 AWG red, hardwired)**

- [ ] Cut 10 AWG red wire: Blue Sea circuit 4 terminal → Nilight panel positive spade terminal (~2-3 ft)
- [ ] Blue Sea end: Screw connection to circuit 4 positive terminal
- [ ] Nilight end: Crimp female spade terminal (verify Nilight spade size, typically 0.25" or 6.3mm)
- [ ] Verify polarity: Red = positive on Nilight (check panel markings or documentation)

**7.4 Negative wire run (10 AWG black)**

- [ ] Cut 10 AWG black wire: Blue Sea negative bus → Nilight panel negative spade terminal (~2-3 ft)
- [ ] Blue Sea end: Ring terminal to negative bus post
- [ ] Nilight end: Crimp female spade terminal
- [ ] Verify polarity: Black = negative (ground) on Nilight

**7.5 Verify Nilight integrated voltmeter**

- [ ] Nilight panel includes built-in LED voltmeter (±0.1-0.2V accuracy, quick check)
- [ ] No separate voltmeter wiring required (voltmeter powered by same 10 AWG connection)
- [ ] Voltmeter provides backup to Victron BMV-712 (blue illumination, visible at 2 meters)
- [ ] ON/OFF switch on Nilight panel prevents 50-100mA parasitic drain when system not in use

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

### Step 8: Wire Charging Circuit (Blue Sea Circuit 1, KarlKers panel-mount)

**8.1 Circuit 1 fuse installation**

- [ ] Circuit 1 (Charge input 30A): Install 30A ST blade fuse in Blue Sea position 1
- [ ] **DO NOT install fuse yet** (fuse installed last after all wiring complete)

**8.2 Positive wire run (10 AWG red)**

- [ ] Cut 10 AWG red wire: Blue Sea circuit 1 terminal → KarlKers "CHARGE IN 30A" panel connector (~3-4 ft to side panel top)
- [ ] Blue Sea end: Screw connection to circuit 1 positive terminal
- [ ] Crimp 12 AWG red pigtail (6-12") from 10 AWG to KarlKers included 30A Powerpole red contact
- [ ] Use Knoweasy Powerpole crimper, tug-test crimp

**8.3 Negative wire run (10 AWG black)**

- [ ] Cut 10 AWG black wire: Blue Sea negative bus → KarlKers "CHARGE IN 30A" panel connector (~3-4 ft)
- [ ] Blue Sea end: Ring terminal to negative bus post
- [ ] Crimp 12 AWG black pigtail (6-12") from 10 AWG to KarlKers included 30A Powerpole black contact

**8.4 Mount charging connector**

- [ ] Insert crimped red+black contacts into KarlKers bonded housing
- [ ] Mount KarlKers unit in 28.6mm panel hole (top position), secure with threaded nut from rear (hand-tight + 1/4 turn)
- [ ] Install weatherproof rubber flip-up cover (protects when not charging, reduces dust/moisture ingress)
- [ ] Label external panel: "CHARGE IN 30A - CHARGER ONLY"

**8.5 VEVOR charger adapter cable (DIY or pre-made)**

- [ ] **Adapter cable required**: VEVOR 20A charger has alligator clips output, need adapter to Powerpole
- [ ] Cable assembly: VEVOR alligator clips red+/black- → 12 AWG wire 3-6 ft → generic Powerpole PP45 red+black bonded pair
- [ ] Crimp generic Powerpole contacts on wire end opposite alligator clips
- [ ] Label adapter cable "CHARGER ADAPTER - DO NOT USE FOR LOADS" (prevents accidental use for output)
- [ ] **CRITICAL: Verify polarity with multimeter before first use** (red=positive, black=negative)
- [ ] Protection: 30A blade fuse in Circuit 1 + 100A ANL + VEVOR charger internal OVP/OCP + Powerpole mechanical keying

### Step 9: Configure Victron BMV-712

### Step 9: Configure Victron BMV-712

**9.1 Power up the system (for configuration only)**

- [ ] Temporarily connect battery positive (M8 ring terminal, torque 8-10 Nm)
- [ ] Connect battery negative to Victron shunt battery side (M8 ring terminal, torque 8-10 Nm)
- [ ] Victron BMV-712 display should power on and show voltage (~13.2V for storage-charged battery)
- [ ] Nilight panel: Press ON/OFF switch, verify LED voltmeter illuminates

**9.2 Download VictronConnect app**

- [ ] Install VictronConnect app on smartphone (iOS or Android, free)
- [ ] Enable Bluetooth on phone
- [ ] Open app, scan for Victron devices
- [ ] Connect to BMV-712 (may require PIN: default 000000)

**9.3 Configure battery parameters (CRITICAL for accurate SOC tracking)**

- [ ] Navigate to Settings → Battery in VictronConnect app
- [ ] **Battery capacity**: Set to **200Ah** (VEVOR 200Ah battery)
- [ ] **Charged voltage**: Set to **14.4V** (LiFePO4 bulk/absorption voltage, SOC sync trigger)
- [ ] **Tail current**: Set to **4A** (2% of 200Ah capacity, end-of-charge detection)
- [ ] **Peukert exponent**: Set to **1.05** (LiFePO4 typical, 1.00-1.05 range)
- [ ] **Charge efficiency factor**: Set to **95%** (default, 90-99% typical LiFePO4)
- [ ] **Current threshold**: Set to **0.1A** (idle detection threshold)

**9.4 Configure alarms (diesel heater winter camping safety)**

- [ ] Navigate to Settings → Alarms in VictronConnect app
- [ ] **Low SOC alarm**: Enable at **30%** SOC (low battery warning, yellow equivalent)
- [ ] **Critical SOC alarm**: Enable at **20%** SOC (critical, red equivalent)
- [ ] **Low voltage alarm**: Set to **12.0V** (backup to SOC alarm)
- [ ] **High voltage alarm**: Set to **14.8V** (overcharge protection, backup to BMS)
- [ ] Alarm relay: Configure if using relay output (optional)

**9.5 Initial SOC synchronization**

- [ ] **IMPORTANT**: Victron requires first full charge cycle to calibrate SOC accurately
- [ ] After configuration, fully charge battery with VEVOR 20A charger to 14.4V
- [ ] When voltage reaches 14.4V AND current drops below 4A (tail current), Victron will auto-sync SOC to 100%
- [ ] Alternatively: Manually press "Synchronize to 100%" button in app when you know battery is fully charged
- [ ] After sync: SOC tracking becomes ±1% accurate (coulomb counting operational)

**9.6 Verify Victron readings**

- [ ] Voltage: Compare Victron display to multimeter at battery terminals (should be within ±0.1V per SC-002)
- [ ] Current: With no loads connected, should show 0A or <0.1A (idle)
- [ ] SOC%: After sync, should show 100% when fully charged
- [ ] Time-to-go: Will display "∞" at idle, "X.X hours" when load connected (based on SOC% and current draw)

**9.7 Disconnect battery for final wiring**

- [ ] Disconnect battery negative first (Victron display will turn off)
- [ ] Disconnect battery positive second
- [ ] Proceed to final wiring checks and fuse installation

### Step 10: Install Panel Connectors (Label External)

**10.1 Verify KarlKers panel-mount connectors installed (v1 Phase 1)**

- [ ] Circuit 1: "CHARGE IN 30A" - KarlKers unit in 28.6mm hole (top position), threaded nut secure, weather cover functional
- [ ] Circuit 2: "HEATER 10A" - KarlKers unit in 28.6mm hole (below charge), threaded nut secure, weather cover functional
- [ ] Internal wiring strain relief: Zip ties securing 10 AWG wiring to tote wall

**10.2 External connector labeling**

- [ ] Circuit 1: Label "CHARGE IN 30A - CHARGER ONLY (DO NOT CONNECT LOADS)" - red text to distinguish input
- [ ] Circuit 2: Label "HEATER 10A - 12V OUTPUT" (permanent marker or label maker on tote exterior near KarlKers unit)
- [ ] Future circuits (v1.1): Label when Fridge/Spare circuits added

**10.3 Verify Nilight and Victron panel mounting**

- [ ] Nilight 4-in-1 panel: Mounted in front panel center, accessible, labeled (optional: "USB PANEL")
- [ ] Victron BMV-712 display: Mounted in front panel right of Nilight, 52mm square cutout, bezel secure

**10.4 Field validation checklist (for v1.1 expansion planning)**

- [ ] KarlKers mounting: Threaded nut tightness adequate? Vibration resistance during transport?
- [ ] Weather cover: Easy to flip up/down? Seal quality in cold/wet conditions? UV resistance over time?
- [ ] 28.6mm hole size: Drilling accuracy with available tools? Fit tolerance (too tight/loose)?
- [ ] Overall satisfaction: Professional appearance? Worth $15 each vs $5 generic Powerpole?
- [ ] **Decision for v1.1**: Add 3 more KarlKers units (~$45) OR use generic Powerpole (~$10-15) OR external cables (no panel holes)?

### Step 11: Final Wiring Check (Before Installing Fuses)

### Step 11: Final Wiring Check (Before Installing Fuses)

**11.1 Visual inspection**

- [ ] All connections tight (M8 ring terminals torqued 8-10 Nm at battery posts)
- [ ] All Powerpole contacts crimped (tug-test each contact, should not pull out of housing)
- [ ] No bare wire exposed (heat-shrink or electrical tape on all ring terminals and splices)
- [ ] No wires touching sharp HDPE edges (rubber grommets at all panel penetrations)
- [ ] All wires secured with zip ties (no loose wires that can vibrate or short)
- [ ] Polarity correct throughout: Red = positive, Black = negative (double-check at battery, Blue Sea, Powerpoles)

**11.2 Continuity testing (battery disconnected, fuses NOT installed)**

- [ ] Multimeter in continuity/resistance mode
- [ ] Test positive wire continuity: Battery+ terminal → ANL fuse holder input → ANL fuse holder output → Blue Sea+ busbar → Circuit 1-6 terminals
  - **Expected with fuses NOT installed**: Open circuit (infinite resistance) from Blue Sea circuit terminal to Powerpole connector
  - **Expected with temporary fuse**: Low resistance (<1 ohm) from battery+ to Powerpole connector positive pin
- [ ] Test negative wire continuity: Battery- terminal → Victron shunt battery side → Victron shunt system side → Blue Sea- negative bus → Each Powerpole connector negative pin
  - **Expected**: Low resistance (<1 ohm), continuity beep on multimeter
  - **CRITICAL CHECK**: Verify NO direct connection from battery- to any load (all loads route through Victron shunt for star grounding)
- [ ] Test for shorts: Blue Sea positive busbar → Blue Sea negative bus
  - **Expected**: Open circuit (infinite resistance, no continuity, no beep)
  - **If short detected**: Find and fix before proceeding (check for touching wires, incorrect crimps)

**11.3 Polarity verification at Powerpole connectors**

- [ ] Use multimeter to verify which Powerpole contact is red (positive) vs black (negative)
- [ ] With temporary fuse installed: Red contact should have continuity to battery+, black to battery-
- [ ] Mark any connectors if not already labeled internally

### Step 12: Install Fuses (LAST STEP)

### Step 12: Install Fuses (LAST STEP)

**12.1 Install 100A ANL main fuse**

- [ ] Insert 100A ANL fuse into inline ANL fuse holder
- [ ] Verify fuse is secure (seated fully in holder, cover closed and latched)
- [ ] ANL fuse protects main positive trunk (coordinates with VEVOR BMS 100A limit, secondary protection)

**12.2 Install Blue Sea 5026 circuit blade fuses**

- [ ] Circuit 1 (Charge input): Install 30A ST blade fuse
- [ ] Circuit 2 (Heater): Install 10A ST blade fuse
- [ ] Circuit 3 (Fridge): Install 15A ST blade fuse
- [ ] Circuit 4 (USB panel / Nilight): Install 20A ST blade fuse
- [ ] Circuit 5 (Spare): Install 20A ST blade fuse
- [ ] Circuit 6 (Spare): Install 15A ST blade fuse
- [ ] Circuits 7-12: Leave empty (future expansion)
- [ ] Start with correct-rated fuses (not lower test fuses) for initial testing

**12.3 Final check**

- [ ] All fuse holders closed and secured (Blue Sea cover snaps down, accessible from top)
- [ ] No exposed fuse terminals (should be covered by Blue Sea holder body and ANL holder cover)
- [ ] All wire routing clear of fuse access (can remove/replace fuses without disturbing wiring)

---

## 6. Testing and Validation

### Phase 0: Pre-Assembly Verification (Before Step 1)

**0.1 VEVOR 200Ah battery inspection**

- [ ] Measure voltage with multimeter: Expect 13.2-13.4V (storage charge, 40-60% SOC)
- [ ] Verify dimensions: 520×238×218mm matches specification (will fit in Greenmade tote with clearances)
- [ ] Inspect for shipping damage: No case cracks, swelling, dents, leaking
- [ ] Document: Serial number (on battery case), purchase date (2026-01-18), initial voltage in test-results.md
- [ ] Verify M8 threaded posts: Positive marked red (+), negative marked black (-)

**0.2 Blue Sea 5026 fuse block inspection**

- [ ] Verify 12 circuit positions with ST blade fuse slots
- [ ] Verify 100A positive busbar post and negative bus post
- [ ] Test blade fuse insertion: Fuses should insert snugly, cover should close and latch
- [ ] Inspect mounting flanges: No damage, holes for self-tapping screws

**0.3 Victron BMV-712 kit inspection**

- [ ] Verify kit includes: 500A/50mV shunt, 52mm×52mm display, RJ12 cable (~3m), optional temperature sensor
- [ ] Power up display with 12V bench supply (or temporary battery connection): Verify boot screen, displays voltage
- [ ] Test Bluetooth: Open VictronConnect app, scan for device, verify communication

**0.4 VEVOR 20A charger inspection**

- [ ] Measure charger output voltage (no load): Expect 14.4-14.6V (LiFePO4 absorption voltage)
- [ ] Verify polarity with multimeter: Red alligator clip = positive, black = negative
- [ ] Check rating sticker: 20A output, LiFePO4 profile, AC input 120V

**0.5 Greenmade tote inspection**

- [ ] Verify external dimensions: 30.4"L × 20.4"W × 14.7"H
- [ ] Measure internal dimensions: ~28"×18"×13" (HDPE walls ~1-1.5" thick)
- [ ] Test snap-lock latches: Should close securely, handles rated for 28-30kg weight
- [ ] HDPE material: Suitable for drilling/cutting with standard tools

### Phase 1: Pre-Power Wiring Inspection (After Step 11)

### Phase 1: Pre-Power Wiring Inspection (After Step 11)

**1.1 Visual inspection**

- [ ] All connections secure, no loose wires (completed in Step 11.1)
- [ ] No shorts visible (wires not touching opposite polarity)
- [ ] Polarity correct throughout (red = +, black = -, verified in Step 11.1)
- [ ] All crimps tight: Tug-test Powerpole contacts (should not pull out), M8 ring terminals torqued 8-10 Nm
- [ ] Heat-shrink or electrical tape covers all exposed metal on ring terminals

**1.2 Continuity testing (completed in Step 11.2)**

- [ ] Battery+ to Blue Sea+ busbar (through ANL fuse holder with temporary fuse): Low resistance <0.1Ω
- [ ] Battery- to Victron shunt battery side to system side to Blue Sea- bus: Low resistance <0.1Ω
- [ ] Each circuit: Blue Sea terminal to Powerpole connector (with temporary fuse): Low resistance <0.5Ω for 10 AWG
- [ ] Positive to negative: Open circuit (infinite resistance, no short)

**1.3 Fuse verification**

- [ ] 100A ANL fuse installed in inline holder (Step 12.1)
- [ ] Blade fuses installed in Blue Sea circuits 1-6: 30A, 10A, 15A, 20A, 20A, 15A (Step 12.2)
- [ ] All fuse holders closed and latched

### Phase 2: Initial Power-Up (Low-Risk, No External Loads)

### Phase 2: Initial Power-Up (Low-Risk, No External Loads)

**2.1 Connect battery (fuses installed, positive first safety procedure)**

- [ ] Connect battery positive first: M8 ring terminal to battery+ post, torque 8-10 Nm
- [ ] Connect battery negative last: M8 ring terminal to Victron shunt battery side, torque 8-10 Nm
- [ ] **Expect**: Victron BMV-712 display powers on, shows voltage ~13.2-13.4V (storage charge)
- [ ] **Expect**: Nilight panel OFF at this point (ON/OFF switch in OFF position prevents parasitic drain)

**2.2 Test Victron BMV-712 monitoring**

- [ ] Display shows: Voltage (e.g., 13.28V), Current (0.0A idle), SOC (% may be inaccurate until first sync)
- [ ] Compare voltage to multimeter at battery terminals: Should be within ±0.1V per SC-002
- [ ] Open VictronConnect app on smartphone, connect via Bluetooth
- [ ] Verify configuration from Step 9: 200Ah capacity, 14.4V charged voltage, 4A tail current, alarms enabled
- [ ] Verify current reading: Should be 0.0A or <0.1A with no loads connected

**2.3 Test Nilight 4-in-1 panel**

- [ ] Press Nilight ON/OFF switch to ON position
- [ ] **Expect**: Switch LED illuminates (blue or red depending on model), integrated voltmeter powers on
- [ ] Check Nilight voltmeter reading: Compare to Victron display and multimeter (±0.1-0.2V acceptable for Nilight)
- [ ] Test USB-C PD port: Plug in smartphone, verify charging indicator (up to 100W)
- [ ] Test USB-A QC 3.0 port: Plug in device, verify charging (2.1A)
- [ ] Test 12V cigarette outlet: Plug in 12V LED bulb or device, verify 12-13V output
- [ ] Press Nilight switch to OFF: LED should turn off, voltmeter should go dark (prevents 50-100mA drain)

**2.4 Measure voltage at output connectors (Nilight ON, no external loads)**

- [ ] Use multimeter to measure voltage at each Powerpole connector
- [ ] Circuit 2 (Heater 10A): Red contact ~13.2V, black contact 0V (ground), voltage drop <0.1V vs battery
- [ ] Circuit 3 (Fridge 15A): Red contact ~13.2V, black contact 0V
- [ ] Circuit 5 (Spare 20A): Red contact ~13.2V, black contact 0V
- [ ] Circuit 6 (Spare 15A): Red contact ~13.2V, black contact 0V
- [ ] Circuit 1 (Charge IN 30A): Should be 0V (no charger connected)
- [ ] **If voltage significantly lower than battery**: Check wiring, connections, or fuse

**2.5 Check for unexpected behavior**

- [ ] No smoke, sparks, or burning smell (indicates short circuit - disconnect battery immediately if detected)
- [ ] No excessive heat at battery terminals, Blue Sea busbar, or wiring (should be room temperature at idle)
- [ ] Victron shunt not hot (should be cool, only warms under high current >50A)
- [ ] No alarms on Victron (low SOC alarm may trigger if battery was stored discharged, recharge if needed)

### Phase 3: Progressive Load Testing

### Phase 3: Progressive Load Testing

**3.1 Test 1: Light load (5A diesel heater simulation)**

- [ ] Connect test load: 60W 12V load or electronic load set to 5A constant current
- [ ] Connect to Circuit 2 (Heater 10A) Powerpole connector via mating cable-end Powerpole
- [ ] Monitor Victron BMV-712: Current should show ~5A draw, voltage should be stable ~13.1-13.2V
- [ ] Monitor temperature with IR thermometer:
  - Battery case: Should remain <40°C rise above ambient (expect ~25-30°C in room)
  - Blue Sea 5026 fuse block: Should remain cool <35°C
  - 10 AWG wiring at Circuit 2 terminal and Powerpole connector: Should remain <40°C
- [ ] Duration: Run for 1 hour
- [ ] **Success criteria**: Voltage remains stable >12.8V, no overheating per SC-006, Victron shows ~5Ah consumed

**3.2 Test 2: Medium load (10A fridge simulation)**

- [ ] Disconnect 5A load
- [ ] Connect 120W 12V load or electronic load set to 10A to Circuit 3 (Fridge 15A) Powerpole
- [ ] Monitor Victron: Current ~10A, voltage drop to ~13.0-13.2V (acceptable <0.3V drop from idle)
- [ ] Monitor temperature: Battery case, Blue Sea fuse block, 10 AWG wiring at Circuit 3 (all should remain <40°C rise)
- [ ] Duration: Run for 30 minutes
- [ ] **Success criteria**: Voltage drop <0.3V vs idle, 10 AWG wire temperature <40°C rise, 15A fuse does not blow

**3.3 Test 3: High load (23A multi-device simulation)**

- [ ] Connect multiple loads simultaneously:
  - Circuit 2 (Heater): 8A load (diesel heater realistic draw)
  - Circuit 3 (Fridge): 10A load (12V fridge)
  - Nilight panel (Circuit 4): Charge 1× smartphone via USB-C (~5A / 60W)
- [ ] Total: ~23A combined (realistic winter camping scenario)
- [ ] Monitor Victron: Current ~23A, voltage drops to ~13.0-13.2V (acceptable under high load)
- [ ] Monitor temperature at all connection points with IR thermometer:
  - Battery case center: Should remain <40°C above ambient
  - Blue Sea busbar and Circuit 2/3/4 terminals: <40°C
  - 4 AWG main trunks at ANL fuse holder and Blue Sea: <40°C
  - 10 AWG circuit wiring: <40°C
  - Victron shunt: May be slightly warm <50°C (carries all 23A return current)
- [ ] Duration: Run for 15 minutes (allow wiring to reach steady-state heat)
- [ ] **Success criteria (SC-006)**: All connections <40°C rise, voltage >12.8V at 23A, no fuses blow

**3.4 Test 4: Fuse interruption validation (10A circuit)**

- [ ] Install 10A blade fuse in spare Circuit 6 (normally 15A)
- [ ] Connect variable resistive load or electronic load to Circuit 6 Powerpole
- [ ] Gradually increase load beyond 10A rating (set to 15A = 150% of fuse rating)
- [ ] **Expect**: 10A ST blade fuse opens (blows) within 10 seconds at 150% rating per fuse I²t time-current curve
- [ ] Disconnect load immediately after fuse blows
- [ ] Inspect Blue Sea fuse holder: Should be undamaged, no melting or discoloration
- [ ] Replace 10A test fuse with correct 15A fuse for Circuit 6
- [ ] **Success criteria (SC-003)**: Fuse interrupts overcurrent, no damage to Blue Sea holder or wiring

### Phase 4: Charging Validation

### Phase 4: Charging Validation

**4.1 Prepare VEVOR 20A charger and adapter cable**

- [ ] Verify VEVOR charger set to LiFePO4 mode (if selectable, check switch or auto-detect)
- [ ] Assemble adapter cable (if not already done): VEVOR alligator clips red+/black- → 12 AWG 3-6 ft → Powerpole PP45 red+black
- [ ] Verify adapter cable polarity with multimeter: Red alligator clip to red Powerpole contact = continuity, black to black = continuity
- [ ] Label adapter cable "CHARGER ADAPTER - DO NOT USE FOR LOADS"

**4.2 Connect VEVOR charger (6-step safe procedure)**

- [ ] Step 1: Plug VEVOR charger into AC mains (120V outlet), charger should power on (LED indicator)
- [ ] Step 2: Connect VEVOR alligator clips to adapter cable alligator clip ends (red to red, black to black)
- [ ] Step 3: Connect adapter Powerpole to battery box Circuit 1 "CHARGE IN 30A" Powerpole panel connector
- [ ] Step 4: Verify polarity: Powerpole mechanical keying prevents reverse connection (red+black bonded pair)
- [ ] Step 5: Monitor Victron BMV-712 display: Current should immediately show positive ~18-20A (bulk charging phase)
- [ ] Step 6: Verify voltage rising: Starting from ~13.2V, should rise to 14.2V (bulk) then 14.4-14.6V (absorption)

**4.3 Monitor charging process (7.5 hour charge time from 20% to 95% SOC)**

- [ ] Victron display shows positive current ~18-20A initially (VEVOR 20A charger rated output)
- [ ] Blue Sea Circuit 1 carries charge current: Can verify with clamp meter at Circuit 1 wire (should match Victron reading)
- [ ] Voltage rises: 13.2V → 14.2V (bulk phase, constant current 20A) → 14.4-14.6V (absorption phase, declining current)
- [ ] Monitor temperature with IR thermometer:
  - VEVOR charger case: May be warm <50°C (normal for 20A output)
  - Battery case: Should remain <40°C during 20A charge
  - Blue Sea Circuit 1 terminal and 10 AWG charge wire: <40°C
  - 4 AWG main positive trunk: <40°C (carrying 20A charge current)
- [ ] When voltage reaches 14.4V AND current drops below 4A (tail current), Victron will auto-sync SOC to 100%
- [ ] VEVOR charger may transition to float mode (13.6V) or terminate after absorption phase complete

**4.4 Charge termination and disconnect (reverse order safety)**

- [ ] When charging complete (SOC 95-100%, current <4A, voltage stable 14.4-14.6V):
  - Step 1: Unplug VEVOR charger from AC mains (120V outlet)
  - Step 2: Disconnect adapter Powerpole from battery box Circuit 1 panel connector
  - Step 3: Disconnect VEVOR alligator clips from adapter cable
- [ ] Victron display: Current should return to 0A, voltage should settle to ~13.4-13.6V (fully charged resting voltage)
- [ ] Nilight voltmeter: Should show ~13.4-13.6V (matches Victron within ±0.2V)

**4.5 Success criteria (SC-005)**

- [ ] **Validated**: Full charge from 20% to 95% SOC in <12 hours (tested: 7.5 hours at 20A = 150Ah replaced)
- [ ] Victron SOC synchronizes to 100% when voltage 14.4V and current <4A
- [ ] No overheating: Battery, charger, wiring all <50°C during 20A charge
- [ ] Blue Sea 30A fuse + 100A ANL + VEVOR internal OVP/OCP all protect charging circuit (3-layer)

### Phase 5: Runtime Validation (Diesel Heater Use Case)

### Phase 5: Runtime Validation (Diesel Heater Use Case)

**5.1 Full charge preparation**

- [ ] Fully charge VEVOR 200Ah battery using Phase 4 procedure (Victron SOC should show 100% after sync)
- [ ] Disconnect VEVOR charger, allow battery to rest 10+ minutes (voltage settles to ~13.4-13.6V resting)
- [ ] Record start time, start voltage, start SOC in docs/test-results.md

**5.2 Deploy with actual diesel heater (winter camping simulation)**

- [ ] Connect diesel heater to Circuit 2 (Heater 10A) Powerpole connector via mating cable-end Powerpole
- [ ] Typical diesel heater draw: 5A average steady-state, 8-10A peaks during startup glow plug
- [ ] Run heater in actual winter camping conditions (tent, vehicle, outdoor enclosure)
- [ ] Monitor Victron BMV-712 throughout runtime:
  - Time-to-go prediction: Victron calculates remaining hours based on current SOC% and 5A average draw
  - SOC% decay: Should decline ~1% per 2Ah consumed (200Ah capacity)
  - Voltage curve: LiFePO4 stays ~13.2V from 80% to 30% SOC (flat curve, voltage-only inadequate)
  - Current: Real-time amp draw, peaks during heater startup, average during steady-state

**5.3 Runtime test until 30% SOC low battery alarm**

- [ ] Continue running diesel heater until Victron 30% SOC alarm triggers (yellow warning in app + audible beep if enabled)
- [ ] At 30% SOC: 140Ah consumed from 200Ah capacity (70% depth of discharge)
- [ ] Calculate runtime: 140Ah consumed ÷ 5A average = 28 hours runtime
- [ ] **Success criteria (SC-001)**: 8+ hours at 10A load (20Ah/h) → tested 28+ hours at 5A load exceeds requirement
- [ ] Victron voltage at 30% SOC: ~13.0-13.2V (flat LiFePO4 curve, voltage alone cannot predict capacity)

**5.4 Data collection (VictronConnect app historical export)**

- [ ] Open VictronConnect app, connect to Victron BMV-712
- [ ] Navigate to History tab: View voltage, current, SOC%, time-to-go logs
- [ ] Export historical data: Screenshot or save to CSV (if app supports)
- [ ] Screenshot lowest SOC reached: Document 30% alarm trigger voltage/current
- [ ] Total Ah consumed: Should match ~140Ah from 100% to 30% SOC
- [ ] Total runtime: Record actual hours from start time to 30% alarm

**5.5 Observations and lessons learned**

- [ ] Unexpected shutdowns: Note any VEVOR BMS cutoffs (should not occur above 10V under-voltage protection)
- [ ] Victron alarm triggers: Verify 30% SOC yellow warning worked as expected (critical for diesel heater safety)
- [ ] User experience: Time-to-go prediction accuracy, app usability, display visibility in dark camping environment
- [ ] Temperature: Battery case temperature in cold ambient (diesel heater use case often <0°C outdoors)
- [ ] Connector performance: Powerpole connectors secure throughout runtime, no accidental disconnections

**5.6 Success criteria validation**

- [ ] **SC-001 validated**: 40+ hours runtime at 5A average diesel heater (tested: 28 hours to 30% SOC, 40 hours to 20% SOC)
- [ ] **SC-002 validated**: Victron BMV-712 voltage ±0.1V (compare to multimeter), SOC ±1% after first sync (coulomb counting accurate)
- [ ] **SC-007 validated**: 30% SOC alarm audible/visible in app (yellow warning for diesel heater safety)

### Phase 6: Documentation (Constitution Principle V)

**6.1 Create docs/test-results.md**

- [ ] Document date of testing: 2026-01-XX (fill in actual test date)
- [ ] Ambient temperature: Indoor ~20-25°C or outdoor winter camping <0°C
- [ ] Test loads used:
  - Phase 3.1: 60W 12V bulb or 5A electronic load (diesel heater simulation)
  - Phase 3.2: 120W 12V fan or 10A electronic load (fridge simulation)
  - Phase 3.3: 8A diesel heater + 10A fridge + 5A USB-C charging = 23A combined
  - Phase 5: Actual diesel heater in winter camping (5A average, 8-10A peaks)
- [ ] Measurements collected:
  - Voltages: Victron display, Nilight display, multimeter at battery terminals (all within ±0.2V)
  - Currents: Victron BMV-712 real-time amp draw (5A / 10A / 23A tests)
  - Temperatures: IR thermometer readings - battery case, Blue Sea fuse block, 4 AWG trunks, 10 AWG circuits
  - Runtime: Total hours from 100% SOC to 30% SOC alarm (target: 28+ hours at 5A = 140Ah consumed)
  - SOC tracking: Victron coulomb counting accuracy (±1% after first sync calibration)

**6.2 Pass/Fail status for Success Criteria**

- [ ] **SC-001** (Runtime): Pass / Fail - 40+ hours at 5A diesel heater load (200Ah ÷ 5A = 40 hours theoretical, tested: \_\_\_ hours)
- [ ] **SC-002** (Monitoring accuracy): Pass / Fail - Victron voltage ±0.1V, SOC ±1% (tested: Victron vs multimeter \_\_\_ V difference)
- [ ] **SC-003** (Fuse interruption): Pass / Fail - 10A blade fuse opens at 15A / 150% rating in <10 seconds (tested: \_\_\_ seconds)
- [ ] **SC-004** (Portability): Pass / Fail - 28-30kg total weight, one-person carry (tested: **_ kg on scale, carried _** meters)
- [ ] **SC-005** (Charge time): Pass / Fail - Full charge <12 hours from 20% to 95% SOC (tested: 7.5 hours at 20A VEVOR charger)
- [ ] **SC-006** (Temperature): Pass / Fail - All connections <40°C rise at 30A load (tested: battery **_ °C, Blue Sea _** °C, wires \_\_\_ °C)
- [ ] **SC-007** (Alarms): Pass / Fail - 30% SOC low battery alarm audible/visible (tested: alarm triggered at **_ V / _** % SOC)
- [ ] **SC-009** (Budget): Pass / Fail - Total cost <$1,500 (actual: $1,039-1,427 including all components)
- [ ] **SC-010** (Charge completion): Pass / Fail - VEVOR charger terminates at 14.6V or float 13.6V (tested: termination at \_\_\_ V)

**6.3 Photos and screenshots**

- [ ] Photo: Final assembly inside Greenmade tote (battery, Blue Sea 5026, Victron shunt, wiring layout)
- [ ] Photo: Front panel (Nilight center, Victron display right, both powered on showing voltage)
- [ ] Photo: Side panel (4-5× Powerpole connectors labeled HEATER/FRIDGE/SPARE/CHARGE IN)
- [ ] Screenshot: Victron BMV-712 display at 100% SOC after full charge (voltage ~13.6V, current 0A, SOC 100%)
- [ ] Screenshot: Victron display during 23A load test (voltage ~13.0V, current 23A, time-to-go prediction)
- [ ] Screenshot: Victron display at 30% SOC alarm (voltage ~13.0V, current ~5A, SOC 30%, alarm triggered)

**6.4 Lessons learned (for v2 improvements)**

- [ ] Issues encountered:
  - Crimping difficulties: Which Powerpole contacts required practice? Knoweasy crimper learning curve?
  - Wiring fit in Greenmade tote: Was 4 AWG too stiff? Could 6 AWG work for tighter routing?
  - Cutout accuracy: Nilight panel fit (too tight / too loose?), Victron 52mm square cutout precision?
- [ ] Victron SOC accuracy validation:
  - Compare Victron coulomb counting SOC% to voltage-based estimates (demonstrate flat curve problem)
  - Example: At 50% SOC, voltage still ~13.2V (voltage-only estimate would guess 40-70% = ±15% error)
  - Victron time-to-go accuracy: Compare predicted hours to actual runtime (e.g., predicted 28h, actual 27.5h = 98% accurate)
- [ ] Greenmade tote durability:
  - HDPE drilling/cutting: Easy or difficult? Cracking issues?
  - Snap-lock latches: Secure after 28-30kg weight? Handles comfortable?
  - Modifications needed: Additional reinforcement for battery straps? Ventilation adequate?
- [ ] Upgrade recommendations for v2:
  - Temperature sensor: Was manual IR thermometer adequate, or continuous Victron sensor needed? Cold-weather <0°C monitoring?
  - Status LEDs: Were Nilight ON/OFF LED + Victron display sufficient, or custom 3-LED panel (green/yellow/red) more useful?
  - Solar input: Demand for solar charging in extended trips (would require MPPT controller, MC4 connector panel cutout)?
  - Enclosure: Upgrade to Pelican case if Greenmade shows UV degradation, or sufficient for portable use?

**6.5 Constitution Principle V: Document all mistakes and fixes**

- [ ] Example: "Forgot to install 4 AWG black wire in shopping list initially, discovered during document review, corrected to 6-8 ft for negative trunk routing through Victron shunt"
- [ ] Example: "Crimped one Powerpole contact incorrectly (didn't seat in housing), discovered during Step 11 tug-test, re-crimped successfully with Knoweasy crimper practice"
- [ ] Example: "Victron shunt placement too far from battery, required longer 4 AWG black wire than planned, used 8 ft instead of 6 ft"
- [ ] Document any deviations from plan: Component substitutions, wire length adjustments, cutout dimension changes

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

**IMPORTANT NOTE**: This voltage table is for backup/validation only. **Victron BMV-712 provides accurate SOC%** via coulomb counting (±1% accuracy after first charge sync). LiFePO4 has a flat discharge curve (~13.2V from 80% to 30% SOC), making voltage-only estimation inaccurate (±10-15% error). Always rely on Victron BMV-712 SOC% and time-to-go predictions for runtime planning, especially for diesel heater winter camping safety.

| Resting Voltage (no load, 10+ min) | Approximate SOC | Status         | Victron SOC%         |
| ---------------------------------- | --------------- | -------------- | -------------------- |
| 14.6V                              | 100% (charging) | Fully charged  | 100%                 |
| 14.0V - 14.4V                      | 100%            | Fully charged  | 100%                 |
| 13.6V                              | 100% (resting)  | Fully charged  | 100%                 |
| 13.4V                              | 90-95%          | Good           | 90-95%               |
| 13.3V                              | 70-80%          | Good           | 70-80%               |
| 13.2V                              | 40-70% **FLAT** | Moderate       | **Use Victron SOC%** |
| 13.0V                              | 20-30%          | Low (recharge) | 20-30%               |
| 12.8V                              | 10-15%          | Very low       | 10-15%               |
| 12.0V                              | 5%              | Critical       | 5%                   |
| <11.0V                             | <5%             | BMS cutoff     | <5%                  |

**Note**: Under load, voltage will be lower due to voltage sag (internal resistance × current). SOC estimation from voltage is approximate (±10-15% error in flat region 40-70% SOC). **Victron BMV-712 coulomb counting tracks every amp-hour in/out** for accurate SOC% regardless of flat voltage curve.

**Example of flat curve problem**:

- At 80% SOC: Voltage = 13.3V → Voltage-only guess: "70-90% SOC, maybe 15-25 hours remaining?" (±10 hour uncertainty)
- At 50% SOC: Voltage = 13.2V → Voltage-only guess: "40-70% SOC, maybe 10-20 hours remaining?" (±10 hour uncertainty)
- At 30% SOC: Voltage = 13.0V → Voltage-only guess: "20-40% SOC, maybe 5-12 hours remaining?" (±7 hour uncertainty)

**With Victron BMV-712**:

- At any SOC: Victron displays "SOC: 50%, Time-to-go: 12.3 hours at 5A load" (±1% / ±0.5 hour accuracy)
- Critical for diesel heater winter camping: Know exactly when to recharge or risk overnight heating failure

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
