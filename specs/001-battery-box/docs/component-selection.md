# Component Selection: Battery Box v1

**Purpose**: Document specific component choices with part numbers, suppliers, and procurement details  
**Created**: 2026-01-18  
**Status**: DRAFT - Components being selected  
**References**: [research.md](../research.md) | [component-interfaces.md](../contracts/component-interfaces.md)

---

## Selection Criteria

All components must meet the interface contracts defined in `contracts/component-interfaces.md` and align with research decisions in `research.md`. Priority considerations:

1. **Availability**: Preferably available from common suppliers (Amazon, local hardware/electronics stores)
2. **Cost**: Balance between budget and quality/safety
3. **Documentation**: Manufacturer datasheets available
4. **Reviews**: Established products with user validation where possible
5. **Constitution Compliance**: Safety ratings, proper specifications

---

## 1. Battery Module

### Requirements (from research.md)
- Chemistry: 12V LiFePO4 (4S configuration)
- Capacity: 50Ah minimum (100Ah recommended for 8+ hour runtime at 10A)
- Integrated BMS with OVP, UVP, OCP, SCP protection
- Continuous discharge: 30A minimum (50A+ preferred)
- Weight: Reasonable for portability (<15kg if possible)

### Options to Evaluate

#### Option A: Budget (50-100Ah range)
**Considerations**:
- Ampere Time, Renogy, Lossigy, ECO-WORTHY brands (common on Amazon)
- Price range: $200-400 for 100Ah
- Verify BMS specifications (some cheap batteries have inadequate BMS)
- Check reviews for longevity and customer service

#### Option B: Premium (100-200Ah range)
**Considerations**:
- Battle Born, RELiON, Victron brands
- Price range: $800-1200 for 100Ah
- Superior BMS, longer warranty, proven reliability
- Better for long-term investment

#### Option C: DIY Build (4S LiFePO4 cells + External BMS)
**Considerations**:
- Individual prismatic cells (e.g., 280Ah cells × 4)
- External BMS (Daly, JBD, Orion)
- Lower cost per Ah but requires assembly and balancing
- Higher complexity (Constitution Principle VII concern)

### Selected Component
**Status**: ✅ **PURCHASED**

**Product**: VEVOR 12V 200Ah Deep Cycle LiFePO4 Battery  
**Manufacturer**: VEVOR  
**Model/Part Number**: 010230251465  
**Capacity**: 200 Ah  
**Continuous Discharge**: 100A (per VEVOR specs - verify on datasheet when received)  
**BMS Features**: Integrated BMS with OVP, UVP, OCP, SCP, temperature protection  
**Dimensions**: 520mm × 238mm × 218mm (approx 20.5" × 9.4" × 8.6")  
**Weight**: ~25kg (55 lbs) - typical for 200Ah LiFePO4  
**Supplier**: VEVOR.com (manufacturer direct)  
**Price**: $282 
**Product Link**: https://www.vevor.com/deep-cycle-battery-c_12146/12v-200ah-deep-cycle-lifepo4-battery-bms-lithium-iron-phosphate-battery-for-rv-p_010230251465  
**Purchase Date**: 2026-01-12
**Serial Number**: 2026-01-15

**Decision Rationale**: 
- **Capacity for multi-day use**: 200Ah provides 40+ hours runtime for diesel heater (~5A average draw), enabling 2-3 nights of winter camping without recharge
- **Value**: Mid-tier brand with good price/capacity ratio (~$2.25-2.75/Ah)
- **Integrated BMS**: Simplifies build (Constitution Principle VII: Bounded Complexity)
- **Proven platform**: VEVOR RV/marine batteries have established user base and reviews

**Runtime Calculations**:
- Diesel heater low (3A): 200Ah / 3A = **66 hours** (2.75 days continuous)
- Diesel heater medium (5A): 200Ah / 5A = **40 hours** (1.67 days continuous)
- Diesel heater high (8A): 200Ah / 8A = **25 hours** (1 day continuous)
- Mixed use (heater + lights + phone charging): **2-3 nights comfortably** before recharge needed

**Portability Note**: At ~25kg (55 lbs) with enclosure (~3-5kg), total system weight will be 28-30kg (62-66 lbs). Still one-person portable with handles, but at upper limit. User prioritized capacity over minimum weight - appropriate for stated use case.

---

## 2. Enclosure

### Requirements (from research.md)
- Weatherproof plastic case OR plywood box
- Large enough for battery + components (internal dimensions ~400mm × 250mm × 250mm minimum)
- Drillable for cutouts (connectors, meter, LEDs, ventilation)
- Handles for portability
- Total weight with battery <18kg (one-person portable)

### Options to Evaluate

#### Option A: Plastic Weatherproof Case
**Examples**:
- Pelican Cases (expensive, bombproof)
- Harbor Freight Apache cases (Pelican-style, budget-friendly)
- Plano, MTM, Monoprice cases
- Price range: $50-200 depending on size/quality

**Pros**: Weather-resistant, durable, professional appearance, handles included  
**Cons**: Higher cost, requires drilling for customization

#### Option B: Plywood Box (DIY)
**Materials**:
- 1/2" or 3/4" plywood
- Wood screws, corner brackets
- Optional: Paint or polyurethane finish for moisture resistance
- Price range: $20-50 for materials

**Pros**: Low cost, fully customizable, easy to modify  
**Cons**: Heavier, not weatherproof, less durable for transport

#### Option C: Ammo Can (Metal)
**Examples**:
- .50 cal or .30 cal surplus ammo cans
- Price: $10-30 for surplus
- Very durable, weather-resistant

**Pros**: Extremely durable, weatherproof, low cost  
**Cons**: Metal (potential short circuit risk if battery contacts case), heavy, limited size options

### Selected Component
**Status**: ✅ **SELECTED & SIZE VERIFIED**

**Product**: Greenmade 27 Gallon Snap Lock Storage Box  
**Type**: Plastic storage tote (budget/incremental approach for v1)  
**Model**: Greenmade 27 gal Black/Yellow  
**External Dimensions**: 30.4"L × 20.4"W × 14.7"H (772mm × 518mm × 373mm)  
**Internal Dimensions**: ~28"L × 18"W × 13"H (estimate with 1-1.5" walls) (711mm × 457mm × 330mm)  
**Capacity**: 27 gallons / ~102 liters  
**Weight (empty)**: ~2-3 kg  
**Material**: Heavy-duty polyethylene plastic with snap lock latches  
**Color**: Black/Yellow  
**Supplier**: Ace Hardware or equivalent hardware store  
**Price**: ~$10-20 (27 gallon capacity)  

**✅ Size Verification - EXCELLENT FIT**:
| Dimension | Tote Internal | Battery Size | Clearance | Status |
|-----------|--------------|--------------|-----------|--------|
| Length | ~28" (711mm) | 20.5" (520mm) | **~7.5"** (190mm) | ✅ Excellent - front/back wiring space |
| Width | ~18" (457mm) | 9.4" (238mm) | **~8.5"** (220mm) | ✅ Excellent - side component mounting |
| Height | ~13" (330mm) | 8.6" (218mm) | **~4.5"** (110mm) | ✅ Excellent - top connectors + airflow |

**Internal Layout** (with generous clearances):
- Front panel: 7.5" space for voltmeter, status LEDs, output connectors
- Side panels: 8.5" space on each side for wiring routing, optional busbar
- Top clearance: 4.5" for connector mounting, cable management, ventilation
- Battery placement: Centered or rear-mounted, leaving front accessible

**Decision Rationale**: 
- **Incremental Evolution (Principle IV)**: Start with $9 functional enclosure, upgrade to $100+ hard case later if durability issues arise
- **Bounded Complexity (Principle VII)**: Avoid over-engineering v1 - focus on electrical functionality first
- **Budget efficiency**: $9 vs $100-200 = **$91-191 saved** for battery/electrical components
- **Learning platform**: Test assembly, connector placement, ventilation requirements before committing to expensive enclosure
- **Modular design**: Battery system is self-contained (BMS protects it), enclosure is just carrier/interface - can swap later without rebuild
- **Practical utility**: Integrated handles for portability, lightweight (total system ~27-30kg vs 30-33kg with heavy case)

**V1 Trade-offs** (Acceptable for incremental build):
- ❌ **Not weatherproof**: Indoor storage required, tarp cover during camping if needed
- ❌ **Not crush-resistant**: Don't stack heavy items on top during transport/storage
- ⚠️ **UV degradation**: Keep out of prolonged direct sunlight exposure
- ✅ **Easy to modify**: Drill, cut, mount components trivially with hand tools
- ✅ **Upgrade path**: Transfer entire assembly to Pelican/hard case later if needed

**Safety Mitigations for Plastic Tote**:
1. Add desiccant packs (2-3) to manage moisture/condensation
2. Apply warning labels: "CAUTION: HIGH CURRENT DC POWER - 12V 100A"
3. Use cable glands for all external connections (strain relief + weather seal)
4. Add ventilation mesh to prevent debris/insects entering
5. Secure battery with ratchet straps or foam padding to prevent internal movement

**Upgrade Criteria** (Future v2 considerations):
- If weatherproofing needed for outdoor storage → Pelican 1600 ($150-200)
- If frequent transport/abuse → Apache 4800 ($50-100)
- If UV exposure → Weatherproof hard case
- If v1 tote cracks/fails → Replace with same ($9) or upgrade based on lesson learned

**✅ SIZE VERIFIED**: 30.4" × 20.4" × 14.7" external dimensions provide **excellent fit** for 20.5" × 9.4" × 8.6" battery with 7.5" length, 8.5" width, 4.5" height clearances. Generous working space for wiring, components, and airflow.

**Modifications Required**:
- [ ] Drill cutout for voltmeter: 45mm × 26mm (1.77" × 1.02")
- [ ] Drill holes for LEDs: 3× 10mm (0.39") diameter
- [ ] Drill holes for output connectors: 2-4× 30-40mm diameter (depends on connector choice)
- [ ] Drill hole for charge connector: 1× 30-40mm diameter
- [ ] Drill ventilation holes: 4× 25-30mm diameter (2 front top corners, 2 rear top corners)
- [ ] Install mesh screen over ventilation holes
- [ ] Install cable glands for all external wire exits (strain relief)
- [ ] Add warning labels on all sides

---

## 3. Main Fuse and Holder

### Requirements
- Type: ANL, Mega, or Class-T fuse
- Rating: Based on battery BMS rating (typically 50A-100A)
- Voltage: 32V DC minimum
- Holder: Inline or panel-mount

### Options to Evaluate
- **ANL Fuse + Inline Holder**: Common, readily available, easy to replace
- **Mega Fuse + Holder**: Similar to ANL, automotive-grade
- **Blue Sea Systems fuse blocks**: High quality, panel-mount options

### Selected Component

**Main Fuse**  
**Status**: ✅ **SELECTED**

**Type**: ANL fuse  
**Rating**: 100A (matches VEVOR 200Ah battery BMS continuous discharge rating)  
**Voltage**: 32V DC minimum (adequate for 12V system)  
**Manufacturer**: Generic (Bussmann, Littelfuse, or compatible)  
**Quantity**: 1× installed + 2-3× spares  
**Supplier**: Amazon, auto parts store (AutoZone, O'Reilly)  
**Price**: $5-10 for 3-pack  
**Product Search**: "100A ANL fuse" on Amazon

**Fuse Holder**  
**Status**: ✅ **SELECTED**

**Type**: Inline ANL fuse holder  
**Wire Gauge Compatibility**: 4 AWG or 6 AWG (main battery positive wire)  
**Material**: Nickel-plated brass terminals, weatherproof cover  
**Mounting**: Inline (between battery positive terminal and distribution busbar)  
**Manufacturer**: Generic (Blue Sea Systems for premium, generic for budget)  
**Supplier**: Amazon, marine supply store  
**Price**: $8-15 (Blue Sea), $5-8 (generic)  
**Product Search**: "ANL fuse holder 100A" or "inline ANL fuse block" on Amazon

**Sizing Rationale**:
- **Battery BMS rating**: 100A continuous discharge (per VEVOR specs)
- **Maximum system load**: Heater 8A + Fridge 10A + USB panel 20A + Spare outputs 40A = ~78A theoretical max (very unlikely scenario)
- **Fuse selection**: 100A matches BMS rating - protects wiring without nuisance trips
- **Wire protection**: 100A fuse requires minimum 6 AWG wire (but using 4 AWG for safety margin, see Wire section)
- **Safety margin**: BMS provides backup protection at 100A if fuse fails to blow

**Installation Location**: 
- Within 18 inches of battery positive terminal (NEC/ABYC best practice)
- Before any branch circuits or distribution points
- Accessible for fuse replacement without disassembling entire system  

---

## 4. Circuit Fuses and Holders

### Requirements
- Type: Blade fuses (ATO/ATC standard automotive)
- Ratings: Assortment (10A, 15A, 20A, 30A) based on output circuits
- Holders: Inline blade fuse holders (quantity depends on number of outputs)

### Selected Components

**Blade Fuses**  
**Status**: ✅ **SELECTED**

**Type**: ATO or ATC standard automotive blade fuse  
**Ratings Needed** (based on circuit design):
- 2× 10A fuses - Diesel heater circuit (3-8A typical load)
- 3× 15A fuses - Fridge circuit + spare outputs (5-10A typical loads)
- 2× 20A fuses - Combo panel circuit + spare high-power output
- 2× 30A fuses - Charge input circuit (20A charger with margin)
- **Total**: ~10-15 fuses (includes spares for each rating)

**Supplier**: Auto parts store (AutoZone, O'Reilly), Amazon assorted pack, hardware store  
**Price**: $10-15 for 120-piece assorted pack with storage case  
**Product Example**: "Automotive Blade Fuse Assortment Kit" (Amazon search)

**Inline Fuse Holders**  
**Status**: ✅ **UPGRADED** - Using Blue Sea Systems Fuse Block Instead (See Section 4A)

**⚠️ Original plan was individual inline fuse holders, but user selected superior centralized fuse block approach.**

**Benefits of fuse block over inline holders**:
- Centralized fuse location (easier troubleshooting)
- Cleaner, more organized wiring
- Integrated ground bus (simplifies negative wiring)
- Future expansion capacity (12 circuits vs 6 needed)
- Marine-grade reliability
- Professional appearance

**See Section 4A below** for Blue Sea Systems fuse block details.

---

## 4A. Blue Sea Systems Fuse Block (Replaces Inline Holders)

### Selected Component
**Status**: ✅ **SELECTED**

**Product**: Blue Sea Systems 5026 ST Blade Fuse Block  
**Model**: 5026  
**Manufacturer**: Blue Sea Systems  
**Type**: 12-circuit ST blade (ATO/ATC) fuse block with negative bus and cover  
**Circuit Capacity**: 12 independent fused circuits  
**Busbar Rating**: 100A maximum (matches main 100A ANL fuse and battery BMS)  
**Fuse Type**: ST blade (standard automotive ATO/ATC)  
**Dimensions**: Approximately 6.9" × 3.8" × 1.5" (175mm × 97mm × 38mm)  
**Mounting**: Panel mount with screws (4 mounting holes)  
**Features**:
- Cover included (protects fuses from accidental contact/shorts)
- Common negative bus bar (all circuit grounds terminate here)
- Marine-grade construction (tinned copper, corrosion-resistant)
- Individual circuit labeling (write-on labels or use label maker)
- Easy fuse replacement (lift cover, swap fuse)

**Circuit Allocation** (6 used, 6 future expansion):

| Circuit # | Purpose | Fuse Rating | Wire Gauge | Notes |
|-----------|---------|-------------|------------|-------|
| 1 | Charge Input | 30A | 10 AWG | VEVOR charger input |
| 2 | Diesel Heater | 10A | 10 AWG | Powerpole output |
| 3 | Fridge/Cooler | 15A | 10 AWG | Powerpole output |
| 4 | Nilight USB Panel | 20A | 10 AWG | Feeds combo panel |
| 5 | Spare Powerpole #1 | 20A | 10 AWG | Future inverter/high-power |
| 6 | Spare Powerpole #2 | 15A | 10 AWG | Future device |
| 7 | **Future** | - | - | Solar input, lights, etc. |
| 8 | **Future** | - | - |  |
| 9 | **Future** | - | - |  |
| 10 | **Future** | - | - |  |
| 11 | **Future** | - | - |  |
| 12 | **Future** | - | - |  |

**Wiring Architecture**:
- **Input**: 4 AWG from 100A ANL fuse → Fuse block main positive busbar (single connection)
- **Outputs**: Each circuit → 10 AWG wire → Powerpole connector or device
- **Grounds**: All negative wires → Fuse block negative bus → Single 4 AWG to battery negative
- **Result**: Star grounding topology (best practice for DC systems)

**Mounting Location**:
- Inside tote, mounted to side wall or rear wall
- Position for easy fuse access when cover is lifted
- Keep wires organized with zip ties routing to front panel connectors

**Supplier**: Amazon, West Marine, Fisheries Supply, Blue Sea direct  
**Price**: $50-70  
**Product Search**: "Blue Sea 5026" or "Blue Sea ST Blade Fuse Block 12 Circuit"  

**Decision Rationale**:
- **Professional upgrade**: Centralized fuse management vs scattered inline holders
- **Safety (Principle I)**: Marine-grade quality, proper strain relief, organized troubleshooting
- **Modularity (Principle II)**: Each circuit independently fused, easy to add/remove loads
- **Transparency (Principle III)**: Cover opens to reveal all fuses at once, labeled circuits
- **Incremental Evolution (Principle IV)**: 6 spare circuits ready for future expansion (solar, inverter, lighting)
- **Practical utility (Principle VI)**: Easier to maintain than hunting for inline holders in wiring mess
- **Bounded complexity (Principle VII)**: Simplifies wiring topology with common ground bus

**Cost-Benefit**: $50-70 vs $12-18 inline holders = **$32-52 premium** for significantly better system  

---

## 5. Output Connectors

### Requirements
- Type: Anderson Powerpole PP45 OR XT60 (Constitution: standardized connectors)
- Quantity: [X] outputs (to be determined based on use case)
- Current rating: 30A-60A per connector

### Options to Evaluate

#### Option A: Anderson Powerpole
- **PP15**: 15A (red housing) - for low power
- **PP30**: 30A (red housing) - general purpose
- **PP45**: 45A (red housing) - high power
- Genderless, polarity-keyed, widely used in ham radio/RV
- Requires proper crimp tool (SB50 or compatible)
- Price: $3-5 per mated pair

#### Option B: XT60 or XT90
- **XT60**: 60A continuous (yellow housing)
- **XT90**: 90A continuous (yellow housing)
- Compact, anti-spark design, very common in RC/drone
- Solder connection (no special crimp tool)
- Price: $1-3 per mated pair

### Selected Component
**Status**: ✅ **SELECTED** - Hybrid Strategy

**Primary Connector Type**: Anderson Powerpole PP45  
**Model**: PowerPole 45A (red housing)  
**Current Rating**: 45A continuous per connector  

**Quantity Needed** (High-Power Modular Circuits):
1. **Charge Input** - 1× PP45 pair - Connects to VEVOR 20A charger (20A circuit)
2. **Diesel Heater Output** - 1× PP45 pair - 10A fused circuit (3-8A typical load)
3. **Fridge/Cooler Output** - 1× PP45 pair - 15A fused circuit (5-10A typical load)
4. **Spare Output #1** - 1× PP45 pair - 20A fused circuit (future inverter/high-power device)
5. **Spare Output #2** (optional) - 1× PP45 pair - 15A fused circuit (flex capacity)

**Total**: 4-5× PP45 mated pairs (8-10 housings + 8-10 contacts)

**Supplier**: Amazon (PowerWerx official or compatible), PowerWerx direct  
**Price**: $3-5 per mated pair × 4-5 = **$12-25**  
**Crimping Tool Required**: Yes - SB50 or compatible Powerpole crimp tool ($30-100, see Tools section)

**Panel Mounting**:
- [ ] Drill 4-5× 32mm holes in front/side panel for Powerpole housings
- [ ] Use Powerpole panel mount adapters OR cable glands for strain relief
- [ ] Label each output: "CHARGE", "HEATER", "FRIDGE", "AUX1", "AUX2"
- [ ] Color code wiring: Red=positive, Black=negative

**Decision Rationale**:
- **Standardization**: Powerpole is industry standard for portable power (ham radio, emergency, RV)
- **Modularity (Principle II)**: Each high-power device gets individual fused circuit with quick-disconnect
- **Safety (Principle I)**: Genderless + polarity-keyed = impossible to reverse polarity
- **Durability**: 45A rating handles all loads (diesel heater 8A, fridge 10A, charger 20A) with safety margin
- **Future expansion**: Easy to build mating cables for new devices (inverter, compressor, etc.)

---

## 6. Charging Input Connector

### Requirements
- Same type as output connectors (for consistency) OR barrel jack for lower current
- Must match external charger connector
- Reverse polarity protection via mechanical keying or diode

### Selected Component
**Status**: ✅ **SELECTED** - Anderson Powerpole PP45

**Connector Type**: Anderson Powerpole PP45 (same as high-power outputs for consistency)  
**Model**: PowerPole 45A (red housing)  
**Current Rating**: 45A (sufficient for 20A VEVOR charger with margin)  
**Supplier**: Amazon / PowerWerx (included in output connector order above)  
**Price**: Included in 4-5× pair order above  

**Compatibility with VEVOR Charger**:
- VEVOR charger outputs: Alligator clips + ring terminal connectors
- **Adapter cable required**: Create cable with alligator clips on charger end, Powerpole PP45 on battery box end
- Cable specs: 12 AWG wire, ~3-6 feet length, labeled "CHARGER ADAPTER - DO NOT USE FOR LOADS"
- Alternative: Replace charger output cables with permanent Powerpole connectors (may void warranty, not recommended for v1)

**Circuit Design**:
- Fuse: 30A blade fuse in inline holder (protects against charger malfunction)
- Wire gauge: 10 AWG from charge input to battery positive busbar
- Reverse polarity protection: Mechanical (Powerpole keying prevents reverse connection)
- Panel location: Side or rear panel (separate from load outputs to avoid confusion)

---

## 6A. USB/12V Combo Panel (Convenience Devices)

### Requirements
- USB-A ports: 2-4 ports with 2.4A per port capability
- USB-C PD port: 1-2 ports with 30-100W output (3-9A at 12V input)
- Cigarette/12V outlet: 1 port with 10-15A capability
- Panel mount design (rectangular cutout)
- Integrated circuit protection (fuses or resettable breakers)
- LED indicators for power status

### Options to Evaluate

#### Option A: Multi-Function Panel with USB-C PD
**Examples**:
- "12V Panel Mount USB-C PD Cigarette Lighter" (Amazon search)
- Typical specs: 2× USB-A (2.4A each), 1× USB-C PD (65W), 1× cigarette outlet (15A)
- Price range: $25-50

**Pros**: Single integrated unit, clean installation, built-in protection  
**Cons**: Higher cost, limited customization

#### Option B: Separate Modules Mounted Together
**Components**:
- Dual USB panel mount module ($10-15)
- USB-C PD panel mount module ($15-25)
- Cigarette outlet panel mount ($5-10)

**Pros**: Lower cost, flexible layout, easy to replace individual modules  
**Cons**: Multiple cutouts required, more complex wiring

### Selected Component
**Status**: ✅ **SELECTED**

**Product**: Nilight 4-in-1 ON/OFF Charger Socket Panel  
**Manufacturer**: Nilight  
**Model**: 4-in-1 Blue Panel (PD Type C + QC 3.0 USB + Voltmeter + Cigarette)

**Features**:
- USB-C: 1× port with PD (Power Delivery) and QC 3.0 fast charging
- USB-A: 1× port with QC 3.0 @ 5V/2.1A output
- Cigarette/12V outlet: 1× standard 12V socket @ 10-15A max
- **Built-in LED voltmeter**: Real-time voltage display (eliminates need for separate voltmeter!)
- **ON/OFF toggle switch**: Disconnect all USB/12V loads when not in use (prevents parasitic drain)
- LED indicator lights: Blue illumination for night use
- **Total maximum current**: ~15-20A (USB 4.2A + cigarette 15A if all used simultaneously)

**Electrical Specs**:
- Input voltage range: 12-24V DC (compatible with 10-14.6V LiFePO4 range)
- USB output: Dual 5V/2.1A ports (4.2A total)
- Voltmeter accuracy: Not specified (likely ±0.1-0.2V, adequate for monitoring)
- Pre-wired: Female spade terminals for easy connection

**Mounting**:
- Panel cutout: [Verify dimensions when received - likely ~4-6" wide × 2-3" tall]
- Orientation: Horizontal or vertical mounting
- Hardware: Stainless steel mounting screws included
- Location: Front panel (center or right side for easy access)

**Wire Gauge to Panel**: 10 AWG (feeds 20A fused circuit from battery positive busbar)  
**Circuit Protection**: 20A blade fuse in inline holder + panel internal protection  

**Supplier**: Nilight.com (manufacturer direct) or Amazon  
**Price**: ~$30-40 (estimate)  
**Product Link**: https://www.nilight.com/products/4-in-1-on-off-blue-charger-socket-panel-pd-type-c-qc-30-usb-voltmeter-cigarette  

**Package Includes**:
- Pre-wired charger socket panel
- Mounting screws (stainless steel)
- Female spade terminals

**Circuit Design**:
- Dedicated 20A fused circuit from battery positive busbar
- 10 AWG wire to panel positive spade terminal
- Ground wire to battery negative or chassis ground via panel negative spade terminal
- ON/OFF switch allows disconnecting all USB/12V loads (prevents 50-100mA parasitic drain during storage)
- Wire routing: Inside tote along side wall, cable management with zip ties
- Panel located on front for easy access (won't interfere with Powerpole outputs)

**Decision Rationale**:
- **Integrated solution**: 4-in-1 design eliminates need for separate voltmeter (saves ~$10-15 + installation time)
- **ON/OFF switch (Bonus)**: Critical for preventing parasitic drain during storage - extends battery life
- **Fast charging**: PD + QC 3.0 support for modern devices (laptops, tablets, phones)
- **Reputable brand**: Nilight specializes in automotive/marine panels - better quality than generic
- **Pre-wired**: Female spade terminals simplify installation vs soldering
- **Single cutout**: Cleaner installation than separate USB + voltmeter + cigarette modules
- **Practical utility (Principle VI)**: Fits exact use case - phone/laptop charging + 12V accessories
- **Bounded complexity (Principle VII)**: All-in-one reduces component count and wiring complexity

**⚠️ Installation Note**: Verify panel cutout dimensions when received before cutting tote. Measure twice, cut once!

---

## 7. Digital Voltmeter

### Requirements
- Voltage range: 5-30V DC (covers 10V-14.6V battery range)
- Accuracy: ±0.1V or ±1%
- Display: LED (red or blue), 0.36" or 0.56" character height
- Panel mount cutout
- Low quiescent current (<20mA)

### Options to Evaluate
- Generic Chinese panel meters (Amazon, eBay): $5-15, adequate accuracy
- "0.36 inch LED voltmeter" or "0.56 inch LED voltmeter" search terms
- Common models: 2-wire or 3-wire (reverse polarity protection)

### Selected Component
**Status**: ✅ **COVERED BY NILIGHT PANEL** (Section 6A) + **VICTRON BMV-712** (Section 7A)

**⚠️ No separate voltmeter needed!** The Nilight 4-in-1 combo panel (Section 6A) includes a built-in LED voltmeter with real-time voltage display.

**✅ UPGRADED: Victron BMV-712 Smart Battery Monitor added for professional-grade monitoring** (See Section 7A below)

**Benefits of integrated voltmeter**:
- Saves ~$10-15 on separate voltmeter purchase
- Eliminates extra panel cutout (one less hole to drill)
- Reduces wiring complexity (powered by same circuit as USB/12V)
- Cleaner front panel appearance (single integrated unit)
- Same visibility and accuracy as standalone units (±0.1-0.2V typical)

**Specifications** (from Nilight panel):
- Voltage range: 12-24V DC (covers 10-14.6V LiFePO4 range)
- Display: LED (blue illumination for night visibility)
- Accuracy: Not specified by manufacturer (likely ±0.1-0.2V, adequate for monitoring)
- Power consumption: Negligible (<20mA, shared with panel LEDs)

**✅ Constitution Requirements Satisfied**:
- **Principle III (Transparency & Observability)** - Basic voltage monitoring: Nilight panel voltmeter
- **Enhanced monitoring for critical use case**: Victron BMV-712 provides accurate SOC, runtime estimates, historical data (essential for multi-day winter camping with diesel heater)

---

## 7A. Victron BMV-712 Smart Battery Monitor (Professional Upgrade)

### Selected Component
**Status**: ✅ **SELECTED**

**Product**: Victron Energy BMV-712 Smart Battery Monitor with Shunt  
**Manufacturer**: Victron Energy  
**Model**: BMV-712 Smart (Grey)  
**Voltage Range**: 6.5-70 VDC (covers 12V LiFePO4 system)  

**What It Does**:
- **Coulomb counting**: Tracks every amp-hour in (charging) and out (loads) via shunt
- **Accurate State of Charge (SOC)**: Calculates actual % remaining based on current flow, not voltage estimation
- **Runtime prediction**: "23.4 hours remaining at current 8.2A load"
- **Historical data**: Charge cycles, deepest discharge, voltage trends, amp-hour statistics
- **Alarms**: Configurable low SOC, low voltage, high/low temperature alerts
- **Bluetooth**: Monitor from smartphone/tablet via VictronConnect app (no need to open battery box)
- **Display**: Integrated panel display showing voltage, current, SOC%, amp-hours, time remaining

**Why Critical for Winter Camping Use Case**:
- **LiFePO4 flat discharge curve problem**: Voltage stays ~13.2V from 80% SOC down to 30% SOC - can't estimate remaining capacity from voltage alone
- **Diesel heater overnight**: Know exact runtime remaining (e.g., "18.7 hours at current 5.3A draw") vs guessing from voltage
- **Multi-day trips**: Track total consumption per day, plan recharge timing accurately
- **Battery health**: Monitor charge/discharge cycles, detect capacity degradation over time
- **Safety**: Set alarm at 30% SOC to prevent deep discharge in cold weather (critical when heater is life-safety device)
- **Remote monitoring**: Check battery status from inside tent without going outside in cold

**Components Included**:
- BMV-712 display unit (panel mount)
- 500A/50mV shunt (measures current flow on negative side)
- 10m (33 ft) RJ12 cable (display to shunt)
- Battery temperature sensor (optional connection)
- Mounting hardware
- VictronConnect app (iOS/Android, free)

**Specifications**:
- **Voltage range**: 6.5-70 VDC (12V system)
- **Shunt rating**: 500A continuous, 50mV drop at rated current
- **Current measurement accuracy**: ±0.4% of full scale
- **SOC accuracy**: ±1% after calibration (coulomb counting method)
- **Display**: 4-digit LCD (voltage, current, SOC, Ah, time-to-go)
- **Bluetooth**: Built-in (VictronConnect app)
- **Power consumption**: <4mA @ 12V (negligible)
- **Panel cutout**: 52mm × 52mm (2.05" × 2.05") square

**Installation Architecture** (Critical Wiring Change):

```
Battery + → 100A ANL fuse → Blue Sea 5026 positive busbar → All loads

Battery - → BMV-712 Shunt (battery side)
                  ↓
            BMV-712 Shunt (system side) → Blue Sea 5026 negative bus → All load grounds
                  ↓                            ↓
            RJ12 cable                    Charger ground
                  ↓
            BMV-712 Display (front panel)
```

**⚠️ CRITICAL WIRING RULE**: 
- **ALL negative wires** (loads, charger, everything) must connect to **system side** of shunt, NOT directly to battery negative
- **ONLY** the shunt itself connects to battery negative terminal
- This ensures shunt measures all current flow in/out of battery
- Incorrect wiring = inaccurate readings or "synchronization error" alerts

**Mounting Locations**:
- **Display**: Front panel (52mm square cutout, near Nilight panel for visibility)
- **Shunt**: Inside tote, between battery negative terminal and Blue Sea ground bus
- **Temperature sensor** (optional): Attach to battery case with adhesive or Velcro

**Configuration** (via VictronConnect app):
- Set battery capacity: 200Ah (VEVOR battery)
- Set charged voltage: 14.4V (LiFePO4)
- Set tail current: 4A (when to consider battery "full")
- Set Peukert exponent: 1.05 (LiFePO4 default)
- Enable low SOC alarm: 30% warning, 20% critical
- Calibrate SOC to 100% after first full charge

**Supplier**: Amazon, West Marine, Victron distributors  
**Price**: $200-250  
**Product Search**: "Victron BMV-712" or "Victron BMV-712 Smart"  

**Decision Rationale**:
- **Safety (Principle I)**: Accurate SOC monitoring prevents dangerous deep discharge during winter camping (heater is life-safety device)
- **Transparency (Principle III)**: Professional-grade observability - SOC%, runtime, historical data, Bluetooth remote monitoring
- **Practical Utility (Principle VI)**: Critical for multi-day winter camping use case - know exact remaining runtime for diesel heater
- **Battery longevity**: Avoid deep discharges that reduce LiFePO4 cycle life - BMV-712 prevents guessing games
- **Data-driven decisions**: Plan future trips based on actual consumption data (e.g., "heater uses 40Ah per night at medium setting")
- **Victron quality**: Industry-leading battery monitors, proven reliability, excellent app support
- **Future integration**: Can add Victron solar charge controller, inverter, etc. (all integrate via VE.Smart network)

**Cost-Benefit**: $200-250 is significant, but essential for safe, reliable multi-day winter camping where battery depletion could be life-threatening.

**Nilight Panel Voltmeter Still Useful**: Provides quick visual check without phone, backup if Bluetooth unavailable, validates BMV-712 voltage reading.

---

## 8. Temperature Sensor

### Requirements
- Type: DS18B20 digital (1-Wire) OR 10K NTC thermistor
- Accuracy: ±0.5°C to ±1.0°C
- Mounting: Adhesive-backed or probe style
- Readout: Digital display / data logger / manual IR thermometer check

### Options to Evaluate

#### Option A: DS18B20 Digital Sensor
- 1-Wire protocol, easy to interface with Arduino/Raspberry Pi (future)
- Waterproof probe versions available
- Price: $5-10
- Requires microcontroller for readout (deferred to future feature?)

#### Option B: NTC Thermistor
- Analog, requires voltage divider and meter/ADC
- Very simple, low cost ($2-5)
- Can use analog panel meter for continuous display

#### Option C: Manual Check (IR Thermometer)
- No integrated sensor, user measures manually before/after use
- IR thermometer: $15-30
- Simplest for v1, satisfies FR-015 (measurable once per session)

### Selected Component
**Status**: 🔍 NEEDS DECISION

**Approach**: [DS18B20 / Thermistor / Manual IR check]  
**Product**: [TO BE FILLED]  
**Temperature Range**: [XX]°C to [XX]°C  
**Accuracy**: ±[X]°C  
**Supplier**: [Source]  
**Price**: $[X]  

**Readout Method**: [Display / Logger / Manual measurement]  
**Decision Rationale**: [Why this approach for v1]

---

## 9. Status LEDs

### Requirements
- Quantity: 3 (Power/Green, Low Battery/Yellow, Charging/Red)
- Size: 10mm diameter (for visibility at 2m)
- Panel-mount bezels
- Forward voltage: 2.0-3.5V depending on color
- Current-limiting resistors

### Selected Components

**LEDs**  
**Status**: 🔍 NEEDS DECISION

**Size**: [5mm / 10mm]  
**Quantity**: 1× Green, 1× Yellow/Amber, 1× Red  
**Forward Voltage**: 
- Green: ~3.0-3.5V
- Yellow: ~2.0-2.5V
- Red: ~2.0-2.2V
**Forward Current**: [10-20mA]  
**Viewing Angle**: [Wide / Standard]  
**Supplier**: [Electronics store / Amazon]  
**Price**: $[X] for set of 3  

**LED Bezels (Panel Mount)**  
**Size**: [5mm / 10mm] to match LED  
**Type**: [Snap-in / Threaded]  
**Quantity**: 3  
**Supplier**: [Source]  
**Price**: $[X] each  

**Trigger Circuit Approach**  
**Option Selected**: [Voltage comparator IC / Transistor switches / Pre-built LED module / Manual interpretation]  
**Components Needed**: [LM339 IC + resistors / Transistors + Zeners / Other]  
**Complexity Assessment**: [Simple enough for v1 / Defer to future]  

---

## 10. Wire and Terminals

### Requirements
- Wire: TXL or GXL automotive wire, 105°C rated, stranded copper
- Gauges needed: 10 AWG (main), 12 AWG (circuits), 14 AWG (aux), 18-22 AWG (sensing)
- Colors: Red (positive), Black (negative)
- Ring terminals: Insulated, heat-shrink style, proper crimp
- Heat-shrink tubing: Various sizes

### Selected Components

**Wire**  
**Status**: ✅ **SELECTED**

Based on circuit design with 100A main fuse, Anderson Powerpole outputs, and Nilight panel:

**4 AWG** (Main Battery Positive):
- **Quantity**: 3-4 feet Red
- **Purpose**: Battery positive terminal → 100A ANL fuse → Distribution point
- **Current Capacity**: 150A continuous (safety margin above 100A fuse)
- **Voltage Drop**: <0.3V at 100A over 4 feet

**10 AWG** (High-Power Circuits):
- **Quantity**: 20-25 feet Red, 20-25 feet Black
- **Purpose**: 
  - Charge input circuit (30A fused) - 4-6 ft per polarity
  - Diesel heater output (10A fused) - 3-4 ft per polarity  
  - Fridge output (15A fused) - 3-4 ft per polarity
  - Spare outputs (15-20A fused) - 3-4 ft each per polarity
  - Nilight panel feed (20A fused) - 3-4 ft per polarity
- **Current Capacity**: 40A continuous (adequate for all circuits with margin)
- **Voltage Drop**: <0.5V at 20A over 5 feet

**12 AWG** (Anderson Powerpole Crimp Contacts):
- **Quantity**: 15-20 feet Red, 15-20 feet Black
- **Purpose**: Pigtails from inline fuses to Powerpole housings (short runs, 1-2 ft each)
- **Current Capacity**: 25A continuous (matches PP45 rating with margin)
- **Note**: PP45 contacts accept 10-12 AWG wire

**14 AWG** (Optional/Aux):
- **Quantity**: 10 feet Red, 10 feet Black (optional, spare capacity)
- **Purpose**: Future low-current circuits, LED wiring, extensions
- **Current Capacity**: 15A continuous

**18-22 AWG** (Sensing/Control):
- **Quantity**: 10 feet assorted (Red, Black, Yellow, Green optional)
- **Purpose**: Voltmeter sense wires, LED circuits, low-current control
- **Current Capacity**: 3-7A depending on gauge

**Type**: TXL or GXL automotive wire, stranded copper  
**Insulation Rating**: 105°C minimum (withstands engine bay temps, overkill for battery box but standard)  
**Supplier**: Amazon ("Marine tinned copper wire" or "automotive primary wire"), auto parts store  
**Price Estimate**: 
- 4 AWG: $2-3/foot × 4 ft = $8-12
- 10 AWG: $0.80-1.20/foot × 45 ft = $36-54
- 12 AWG: $0.60-0.90/foot × 35 ft = $21-32
- 14 AWG: $0.40-0.60/foot × 20 ft = $8-12
- 18-22 AWG: $0.20-0.40/foot × 10 ft = $2-4
- **Total wire**: ~$75-115

**Ring Terminals**  
**Status**: ✅ **SELECTED**

**M8 or M6** (Battery Terminal Connections):
- **Size**: M8 recommended (5/16") - verify VEVOR battery terminal post size when received
- **Wire Gauge**: 4 AWG (main positive) + 10 AWG (main negative or ground)
- **Quantity**: 4-6 terminals (main positive, main negative, spare connections)
- **Type**: Insulated heat-shrink ring terminals (red for positive, black for negative)

**Fuse Holder / Distribution Terminals**:
- **Size**: 1/4" or 5/16" ring terminals for inline fuse holders
- **Wire Gauge**: 4 AWG (ANL fuse holder), 10-12 AWG (blade fuse holders)
- **Quantity**: 12-15 terminals (6 inline fuse holders × 2 ends each)
- **Type**: Insulated heat-shrink style

**Anderson Powerpole Terminals**:
- **Type**: PP45 crimp contacts (purchased with Powerpole housings, see Section 5)
- **Wire Gauge Compatibility**: 10-12 AWG
- **Quantity**: 8-10 contacts (included in Powerpole pair purchase)

**Supplier**: Amazon ("Marine ring terminal assortment"), auto parts store  
**Price**: $15-25 for assorted pack (various sizes)  

**Heat-Shrink Tubing**  
**Status**: ✅ **SELECTED**

**Sizes Needed**:
- 1/4" (6mm) - for 18-22 AWG connections
- 3/8" (10mm) - for 12-14 AWG connections  
- 1/2" (12mm) - for 10 AWG connections
- 3/4" (19mm) - for 4 AWG connections
- 1" (25mm) - for bundling multiple wires

**Quantity**: Assorted pack with 3-6 feet per size  
**Type**: 2:1 or 3:1 shrink ratio, adhesive-lined preferred (waterproof seal)  
**Color**: Black primary, Red for positive wire identification  
**Supplier**: Amazon ("Heat shrink tubing assortment kit")  
**Price**: $10-20 for comprehensive assortment kit

**Cable Management**  
**Zip Ties**: 100-pack assorted sizes (4", 6", 8") - $5-10  
**Wire Loom** (optional): Split corrugated tubing for wire protection/bundling - $10-15  
**Cable Clips**: Adhesive-backed or screw-mount for routing inside tote - $5-10

**Total Wire & Terminals Budget**: ~$120-180  

**Heat-Shrink Tubing**  
- Various sizes: 3mm, 6mm, 10mm, 15mm
- Color: Black or assorted
**Supplier**: [Source]  
**Price**: $[X] for kit  

---

## 11. External AC Charger

### Requirements
- Chemistry: LiFePO4-specific (14.4V bulk, 14.6V absorption, 13.6V float)
- Charge current: 10A minimum (for reasonable charge time)
- Input: 120V AC (North America)
- Output connector: Must match battery box charge input
- Protections: OVP, OCP, reverse polarity, short circuit
- UL/CE listed preferred

### Options to Evaluate

#### Option A: Victron Blue Smart IP65 (12V 10A or 15A)
- Excellent reputation, Bluetooth monitoring
- LiFePO4 mode, adaptive charging
- Price: $150-200 (premium)

#### Option B: Renogy 12V 20A DC-DC Charger (with AC adapter)
- Good quality, solar compatible (future expansion)
- Price: $100-150

#### Option C: NOCO Genius Series (verify LiFePO4 mode)
- Consumer-grade, widely available
- Price: $50-100
- Verify model supports LiFePO4 (some are lead-acid only)

#### Option D: Generic LiFePO4 Charger (Amazon)
- Budget option ($30-60)
- Verify specifications carefully, read reviews
- Risk: Quality/longevity concerns

### Selected Component
**Status**: ✅ **PURCHASED**

**Product**: VEVOR 12V 20A Lithium Battery Charger (14.6V LiFePO4)  
**Manufacturer**: VEVOR  
**Model**: 010889683485  
**Output Voltage**: 14.6V (LiFePO4 absorption voltage)  
**Output Current**: 20A  
**Chemistry Modes**: LiFePO4 dedicated (may have selectable modes - verify)  
**Input**: 100-120V AC, 50/60Hz  
**Output Connector**: Alligator clips + ring terminal connectors (verify exact type when received)  
**Protections**: Over-voltage, over-current, short circuit, reverse polarity, over-temperature  
**Certifications**: CE certified (verify if UL listed)  
**Supplier**: VEVOR.com (manufacturer direct)  
**Price**: $57 
**Product Link**: https://www.vevor.com/battery-chargers-c_14017/vevor-12v-20a-lithium-battery-charger-14-6v-ac-dc-lifepo4-smart-charger-for-rv-p_010889683485  

**Charge Time Calculation**:
- 200Ah battery from 20% to 95% SOC: 75% × 200Ah = 150Ah to replace
- At 20A charge rate: 150Ah / 20A = **7.5 hours**
- Full charge from empty (not recommended, but theoretical): 200Ah / 20A = **10 hours**
- Charge rate: 0.1C (gentle, extends battery life per Constitution Principle IV: Incremental Evolution)

**Charge Input Connector Compatibility**: 
- Charger output: Alligator clips (temporary connection style)
- Battery box charge input: Will design Anderson Powerpole or XT60 connector
- **Adapter needed**: Yes - will create cable with charger clips on one end, Powerpole/XT60 on other end
- Alternative: Replace charger output cables with permanent connectors (may void warranty)

**Decision Rationale**: 
- **Brand match**: Same manufacturer as battery (likely tested together, warranty compatibility)
- **Appropriate charge rate**: 20A = 0.1C rate (gentle, recommended for longevity)
- **Correct voltage**: 14.6V is proper LiFePO4 absorption voltage (not lead-acid 14.7V)
- **Smart charging**: Multi-stage charging (bulk, absorption, float) extends battery life
- **Safety**: Multiple protection features align with Constitution Principle I (Safety First)
- **Value**: Good price for 20A LiFePO4 charger (~$4-6 per amp)

---

## 12. Hardware and Fasteners

### Components Needed
- **Battery mounting**: Ratchet straps OR foam padding OR mounting brackets
- **Component mounting**: Screws, standoffs, brackets for fuse holders, busbar, meter
- **Cable glands/grommets**: Strain relief for panel penetrations (quantity based on connector count)
- **Ventilation mesh**: Stainless steel or plastic mesh to cover vent holes
- **Zip ties**: Cable management (various sizes, pack of 50-100)
- **Adhesive foam**: Anti-vibration padding for battery (optional)

### Selected Components
**Status**: 🔍 NEEDS DECISION - List to be compiled after enclosure/connector choices finalized

---

## 13. Tools and Consumables

### Tools Required (not consumed, may already own)

**✅ Already Owned by User**:
- [ ] Qibaok Qi-28BMA Crimper (AWG26-20) - **NOT compatible with this project** (see below)
- [ ] Multimeter (digital, DC voltage and continuity)
- [ ] Wire strippers (verify AWG range covers 10-14 AWG)
- [ ] Screwdrivers (Phillips, flathead)
- [ ] Drill (for enclosure cutouts)
- [ ] Step drill bits or hole saw
- [ ] Heat gun or lighter (for heat-shrink)
- [ ] Adjustable wrench or socket set (for battery terminals)

**🔴 Tools to Purchase**:

### Anderson Powerpole Crimp Tool
**Status**: ✅ **SELECTED** - Powerwerx TRIcrimp

**⚠️ User's existing Qibaok Qi-28BMA crimper is NOT compatible**:
- Existing tool: AWG26-20 (0.1-0.5mm²) - designed for small electronics wiring
- Required wire gauge: AWG10-12 (3.3-5.3mm²) - 6-8× larger diameter
- Powerpole PP45 contacts require larger crimper with SB50-compatible dies

**SELECTED: Powerwerx TRIcrimp** ✅ (Premium/Professional Option)
- **Product**: Powerwerx TRIcrimp - Official Anderson Powerpole crimping tool
- **Compatible Contacts**: PP15, PP30, PP45 (all Anderson Powerpole sizes)
- **Features**: 
  - Three-in-one design: Strips wire, crimps wire barrel, crimps insulation barrel in sequence
  - Color-coded dies for different contact sizes
  - Ratcheting action ensures complete crimp cycle
  - Professional-quality crimps every time (minimal learning curve)
  - Lifetime durability - tool will outlast user
- **Wire Gauge**: AWG10-12 (perfect for this project)
- **Supplier**: PowerWerx.com (manufacturer direct), Amazon
- **Price**: $80-120 (premium investment)
- **Product Search**: "Powerwerx TRIcrimp" or "TRIcrimp Anderson Powerpole"

**Decision Rationale**:
- **Professional quality**: Best crimp consistency for safety-critical 20-30A connections
- **Future-proof**: User likely to build more cables (inverter, solar, extensions, load cables)
- **Buy-once-cry-once**: Premium tool vs buying pre-made cables at $15-30 each
- **Safety (Principle I)**: Good crimps critical at high current - bad crimps cause heat/fire
- **Long-term value**: Tool pays for itself after 4-6 pre-made cable equivalents

**Alternative Option (Budget)**: IWISS SN-28B Ratcheting Crimper ($35-50)
- Good for occasional/DIY use, adequate quality
- Works for Powerpole + ring terminals
- Consider if budget-constrained and only building ~5 cables ever

### Other Tools to Verify/Purchase

**Wire Strippers**:
- **Verify compatibility**: Must handle AWG10-14 range (your Qibaok may only strip small wires)
- **If needed**: Klein Tools 11063W or similar ($15-30) - handles AWG10-20

**Ring Terminal Crimper** (if not using ratcheting crimper above):
- **Budget**: Harbor Freight ratcheting crimper ($10-20)
- **Quality**: Klein Tools or Channellock ($30-50)
- **Note**: IWISS SN-28B (Option A above) handles ring terminals too - no separate tool needed

**Hole Saw Set or Step Drill Bits** (for enclosure):
- **For Nilight panel**: Rectangular cutout (likely 4-6" × 2-3") - use jigsaw or rotary tool
- **For Powerpole outputs**: 1-1/4" (32mm) holes - step drill bit or hole saw
- **For ventilation**: 1" (25mm) holes - spade bit or hole saw
- **Supplier**: Harbor Freight, Amazon, hardware store
- **Price**: Step drill bit set $15-30, hole saw set $20-40

**Heat Gun** (if not already owned):
- **Purpose**: Shrink heat-shrink tubing (lighter works but heat gun is safer/faster)
- **Price**: $15-30 for basic heat gun
- **Alternative**: Hair dryer on high heat (slower but works)

### Consumables
**Status**: ✅ **LISTED**

- [ ] Electrical tape (3M Super 33+ or equivalent) - $5
- [ ] Dielectric grease (for battery terminals, prevents corrosion) - $5-10
- [ ] Sandpaper or wire brush (for cleaning terminals before assembly) - $3-5
- [ ] Isopropyl alcohol (for cleaning surfaces, 90%+ preferred) - $5
- [ ] Shop towels or rags - $5
- [ ] Safety glasses (for drilling) - $5-10
- [ ] Work gloves - $5-10
- [ ] Marker or label maker (for labeling circuits) - $5-20

**Total Tools Budget**: $35-50 (crimper only) to $150-200 (if purchasing many tools)  
**Total Consumables**: ~$40-70

---

## Budget Estimate

**Status**: 🔍 TO BE CALCULATED (after component selection)

| Component Category | Estimated Cost | Notes |
|--------------------|----------------|-------|
| Battery (100Ah LiFePO4) | $250-900 | Wide range depending on brand |
| Enclosure | $20-150 | Plywood cheap, quality case expensive |
| Main Fuse + Holder | $15-30 | ANL fuse system |
| Circuit Fuses + Holders | $20-40 | Blade fuses and inline holders |
| Connectors (output + charging) | $15-40 | Powerpole or XT60 sets |
| Voltmeter | $10-20 | Panel-mount digital LED |
| Temperature Sensor | $5-30 | Digital sensor or IR thermometer |
| LEDs + Bezels | $10-20 | 3 LEDs with panel-mount bezels |
| Wire + Terminals | $30-60 | Various gauges and ring terminals |
| AC Charger | $50-200 | Budget to premium LiFePO4 charger |
| Hardware/Fasteners | $20-40 | Mounting hardware, zip ties, mesh |
| **Total (Estimated)** | **$445-1530** | Budget to premium build |

**Target Budget**: $[XXX] (to be determined based on priorities)

---

## Decision Process

### Phase 1: Core Component Selection (Battery + Enclosure)
**Priority**: HIGH - These determine all other choices

**Tasks**:
1. Research available LiFePO4 batteries in budget range (check Amazon, local suppliers)
2. Read reviews, verify BMS specifications
3. Select battery based on capacity needs, budget, availability
4. Measure battery dimensions to inform enclosure selection
5. Select enclosure based on battery fit, portability, budget

**Timeline**: [Date to complete by]

### Phase 2: Electrical Components
**Priority**: HIGH - Needed for wiring design

**Tasks**:
1. Select connector type (Powerpole vs XT60) - affects tooling and panel design
2. Select fuse ratings based on battery BMS specs
3. Select voltmeter and LED components
4. Determine wire gauges and quantities needed

**Timeline**: [Date to complete by]

### Phase 3: Charger Selection
**Priority**: MEDIUM - Can be deferred slightly, but needed before charging circuit finalized

**Tasks**:
1. Research LiFePO4-compatible chargers
2. Verify output connector compatibility with battery box charge input
3. Select based on budget and features

**Timeline**: [Date to complete by]

### Phase 4: Hardware and Consumables
**Priority**: LOW - Can be selected as build progresses

**Tasks**:
1. Compile hardware list based on enclosure and component choices
2. Purchase fasteners, zip ties, heat-shrink, etc.

**Timeline**: [Date to complete by]

---

## Component Selection Log

### Decision Log Format
```
Date: [YYYY-MM-DD]
Component: [Component name]
Decision: [Product selected with part number]
Rationale: [Why this choice]
Alternatives Considered: [Other options and why rejected]
Procurement: [Ordered from X, tracking #, expected delivery]
```

### Decisions Made
[To be filled as components are selected]

---

## Next Steps

1. **Review component-selection.md** and research options for each category
2. **Make core decisions**: Battery and enclosure first (longest lead time, most dependent)
3. **Document selections**: Fill in product names, part numbers, suppliers, prices
4. **Update quickstart.md**: Revise with specific part numbers and procedures once components known
5. **Generate tasks**: Use specific components to create concrete assembly tasks in `/speckit.tasks`

**Once all components selected and documented**, we'll have:
- Exact BOM (Bill of Materials) with part numbers
- Total project cost calculated
- Specific assembly procedures (no more "install voltmeter", instead "install Bayite DC 6-30V Red LED voltmeter with 45mm×26mm cutout")
- Realistic timeline based on component availability

**Status**: Ready for component research and selection phase.
