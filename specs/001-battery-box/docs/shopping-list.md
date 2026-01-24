# Battery Box v1 - Consolidated Shopping List

**Date**: 2026-01-18 (Updated: 2026-01-24)  
**Feature**: 001-battery-box  
**Status**: Most items purchased, awaiting final hardware

---

## Already Purchased ✅

| Item | Quantity | Price | Source | Status |
|------|----------|-------|--------|--------|
| VEVOR 200Ah 12V LiFePO4 Battery | 1 | ~$450-550 | VEVOR.com | ✅ Purchased |
| VEVOR 20A LiFePO4 Charger (14.6V) | 1 | $57 | VEVOR.com | ✅ Purchased |
| Greenmade 27gal Storage Tote | 1 | ~$10-20 | Ace Hardware | ✅ Selected |
| Nilight 4-in-1 Panel (USB-C/USB-A/12V/Voltmeter) | 1 | ~$30-40 | Nilight/Amazon | ✅ Selected |

**Subtotal Already Purchased/Selected**: ~$547-667

---

## Priority 1: Core Electrical System (Buy First)

### Main Protection & Distribution

| Item | Quantity | Price | Status | Date |
|------|----------|-------|--------|------|
| **100A ANL Fuse** | 7-pack | ~$10 | ✅ Purchased | Jan 19 |
| **ANL Fuse Holder** (inline) | 1 | ~$15 | ✅ Purchased | Jan 19 |
| **Blue Sea Systems 5026 Fuse Block** | 1 | ~$60 | ✅ Purchased | Jan 20 |
| **ST Blade Fuse Assortment** | 1 kit | ~$12 | ✅ Purchased | Jan 19 |

**Priority 1 Subtotal**: ~$97

---

### Anderson Powerpole Connectors (Hybrid Approach: KarlKers + Generic)

| Item | Quantity | Price | Status | Date |
|------|----------|-------|--------|------|
| **KarlKers Panel-Mount Powerpole Units** | 2 | ~$30 | ✅ Purchased | Jan 24 |
| **Generic Powerpole PP45 Pairs** | 10 pairs | ~$25 | ✅ Purchased | Jan 20 |
| **Knoweasy Powerpole Crimper** | 1 | ~$40 | ✅ Purchased | Jan 20 |

**Configuration Notes - v1 Incremental Approach**:
- **Phase 1 (immediate)**: 2× KarlKers panel-mount for Circuit 1 Charge (30A) + Circuit 2 Heater (10A)
  - Each KarlKers includes: weatherproof housing, bonded red+black connector, 30A contacts, flip-up cover, threaded nut
  - Drill 2× 1-1/8" (28.6mm) holes in tote side panel
  - Secure from rear with threaded locking nut (hand-tight + 1/4 turn)
- **Phase 2 (deferred to v1.1 after field validation)**: Add Fridge/Spare circuits based on needs
  - Option A: Order 3 more KarlKers units (~$45) if satisfied with Phase 1 performance
  - Option B: Use 3× generic Powerpole with 32mm holes + rubber grommets (~$10-15)
  - Option C: External cable connections (no additional panel holes)
- **Generic Powerpole pairs** needed for: 
  - 1× VEVOR charger adapter cable (alligator clips → Powerpole)
  - 2× cable ends to mate with KarlKers panel-mount units (for heater device + future loads)
  - 3× future Fridge/Spare circuits (panel or external, decide post-validation)
  - 2× spares for testing/mistakes

**Alternative**: Powerwerx TRIcrimp ($80-120) for professional-grade tool if preferred

**Priority 1 Subtotal**: ~$95 (2× KarlKers $30 + generic Powerpole $25 + crimper $40)

---

### Wire (Automotive TXL/GXL, 105°C, Stranded Copper)

| Gauge | Color | Length | Est. Price | Purpose |
|-------|-------|--------|-----------|---------|
| **4 AWG** | Red | 4 ft | $8-12 | Battery + to ANL fuse to Blue Sea positive bus |
| **4 AWG** | **Black** | **6-8 ft** | **$12-18** | **Battery - to Victron shunt to Blue Sea negative bus** |
| **10 AWG** | Red | 25 ft | $20-30 | Circuit positive wiring (all outputs + charge) |
| **10 AWG** | Black | 25 ft | $20-30 | Individual circuit negative wiring |
| **12 AWG** | Red | 20 ft | $12-18 | Powerpole pigtails |
| **12 AWG** | Black | 20 ft | $12-18 | Powerpole pigtails |
| **18-22 AWG** | Assorted | 10 ft | $2-4 | Sensing wires, low-current |

**Critical**: Main negative wire (4 AWG black) carries ALL return current through Victron shunt - must match positive side capacity (100A+)

**Wire Search Terms**: "Marine tinned copper wire [gauge]" or "automotive primary wire TXL"  
**Supplier**: Amazon, auto parts store  
**Priority 1 Wire Subtotal**: ~$86-130

---

### Terminals & Hardware

| Item | Quantity | Price | Status | Date |
|------|----------|-------|--------|------|
| **Ring Terminal Assortment** | 1 kit | ~$18 | ✅ Purchased | Jan 19 |
| **Heat-Shrink Tubing Assortment** | 1 kit | ~$12 | ✅ Purchased | Jan 19 |
| **Zip Ties Assortment** | 100-pack | ~$8 | ✅ Purchased | Jan 19 |

**Priority 1 Hardware Subtotal**: ~$38

---

## Priority 2: Professional Battery Monitoring

| Item | Quantity | Price | Status | Date |
|------|----------|-------|--------|------|
| **Victron BMV-712 Smart Battery Monitor** | 1 kit | ~$220 | ✅ Purchased | Jan 20 |

**Why Critical**: 
- Accurate SOC% via coulomb counting (solves LiFePO4 flat discharge curve issue)
- Runtime predictions for diesel heater overnight winter camping
- Bluetooth monitoring from tent
- Historical data, alarms, battery health tracking

**Priority 2 Subtotal**: ~$220

---

## Priority 3: Consumables & Hardware

| Item | Quantity | Price | Status | Date |
|------|----------|-------|--------|------|
| Electrical tape (3M Super 33+) | 1 roll | ~$5 | ✅ Have | Already owned |
| Dielectric grease | 1 tube | ~$7 | ✅ Have | Already owned |
| Sandpaper/wire brush | 1 each | ~$4 | ✅ Have | Already owned |
| Isopropyl alcohol 90%+ | 1 bottle | ~$5 | ✅ Have | Already owned |
| Shop towels/rags | 1 pack | ~$5 | ✅ Have | Already owned |
| Label maker or labels | 1 | ~$10 | ✅ Purchased | Jan 19 |
| Cable glands/grommets | 8 pc | ~$12 | ✅ Purchased | Jan 20 |
| Ventilation mesh | 1 ft² | ~$8 | ✅ Purchased | Jan 20 |
| Safety glasses | 1 | ~$8 | ✅ Have | Already owned |
| Cam buckle straps (1" webbing) | 2 | ~$12 | ✅ Have | Already owned |
| Steel strap loops with screws | 4 | ~$8 | ✅ Purchased | Jan 19 |

**Priority 3 Subtotal**: ~$89

---

## Tools to Verify/Purchase

### Already Owned ✅
- [x] Multimeter (DC voltage, continuity testing)
- [x] Wire strippers (handles 10-14 AWG range)
- [x] Screwdrivers (Phillips, flathead)
- [x] Drill
- [x] Heat gun (heat-shrink)
- [x] Adjustable wrench (battery terminals)
- [x] Jigsaw (for Nilight rectangular cutout)
- [x] Dremel/rotary tool (detail work)
- [x] Circular saw (plywood cutting)

### Purchased Tools

| Tool | Price | Status | Date |
|------|-------|--------|------|
| Step drill bit (1/4"-1-3/8") | ~$20 | ✅ Purchased | Jan 20 |
| 52mm hole saw | ~$15 | ⏳ Ordered | Arriving Jan 30 |
| #8×3/4" truss head screws (125 pc) | ~$12 | ⏳ Ordered | Shipping |
| L brackets with screws | ~$10 | ⏳ Ordered | Arriving today Jan 24 |
| 3/4" plywood (battery base + panel) | ~$20 | ✅ Purchased | Jan 24 |

**Tools Subtotal**: ~$77

---

## Budget Summary

| Category | Actual Cost |
|----------|-------------|
| **Already Purchased (Battery/Charger/Tote/Nilight)** | ~$550 |
| **Priority 1: Core Electrical** (ANL, Blue Sea, Powerpole, wire, hardware) | ~$322 |
| **Priority 2: Victron BMV-712** | ~$220 |
| **Priority 3: Consumables** | ~$30 (purchased items) |
| **Priority 3: Consumables** | ~$59 (already owned) |
| **Tools & Materials** | ~$77 |
| **GRAND TOTAL SPENT** | **~$1,199** |
| **Already Owned Items** | ~$59 |
| **Total Project Value** | **~$1,258** |

**Remaining to Purchase**: L brackets ($10, arriving today), 52mm saw ($15, Jan 30), truss screws ($12, shipping) = ~$37

**Note - v1 Incremental Connector Approach**: 
- Start with 2× KarlKers panel-mount ($30) for Charge + Heater circuits
- Field validate: mounting ease, weather seal, vibration resistance, drilling accuracy
- v1.1 expansion: Add 3 more KarlKers (~$45) OR use generic Powerpole (~$10-15) OR external cables
- Budget accommodates either path, total still under $1,500 SC-009 success criteria

**Budget adjusted for**:
- 2× KarlKers panel-mount units vs 5× generic panel Powerpole: +$5 immediate (2×$15 vs 5×$5)
- Added 4 AWG black wire (main negative trunk): +$12-18
- Switched to budget Knoweasy crimper vs TRIcrimp: -$50
- Switched to generic Powerpole-compatible connectors: -$5-10

---

## Shopping Strategy - COMPLETED ✅

### Phase 1: Core Build ✅
**Actual Spent**: ~$322
- ✅ 100A ANL fuse + holder (Jan 19)
- ✅ Blue Sea 5026 fuse block (Jan 20)
- ✅ Blade fuse assortment (Jan 19)
- ✅ 2× KarlKers panel-mount Powerpole units (Jan 24)
- ✅ 10× generic Powerpole PP45 pairs (Jan 20)
- ✅ Knoweasy Powerpole crimper (Jan 20)
- ✅ Wire all gauges: 4/10/12 AWG (Jan 19-20)
- ✅ Ring terminals, heat-shrink, zip ties (Jan 19)
- ✅ Strap loops, cam buckles (Jan 19/owned)

**Status**: All core electrical components received and verified

### Phase 2: Professional Monitoring ✅
**Actual Spent**: ~$220
- ✅ Victron BMV-712 Smart battery monitor (Jan 20)

**Status**: Received, ready for installation

### Phase 3: Consumables & Hardware ✅
**Actual Spent**: ~$30 (purchased) + ~$59 (owned)
- ✅ Grommets, mesh, labels (Jan 19-20)
- ✅ Electrical tape, dielectric grease, cleaning supplies (already owned)
- ✅ Safety equipment (already owned)

**Status**: All consumables available

### Phase 4 (v1.1): Expand Circuits After Field Validation
**Budget**: ~$0-60 (deferred, depends on Phase 1 validation)
- **Option A**: 3× KarlKers panel-mount units (~$45) if impressed with Phase 1 performance
- **Option B**: 3× generic Powerpole with rubber grommets (~$10-15) if KarlKers unnecessary
- **Option C**: External cable connections ($0, no panel holes, use existing generic Powerpole pairs)
- Drill 28.6mm or 32mm holes as needed
- Wire and crimp Fridge (Circuit 3, 15A), Spare (Circuit 5, 20A), Spare (Circuit 6, 15A)

---

## Actual Procurement Timeline ✅

**Week 1** (Jan 19-24) - COMPLETE:
1. ✅ Ordered Priority 1 (core electrical) - Jan 19
2. ✅ Ordered Priority 2 (Victron BMV-712) - Jan 19
3. ✅ Ordered fabrication materials (plywood, hardware) - Jan 19-24
4. ✅ All major parts received by Jan 24
5. ✅ Fabrication begun (base + tapered panel cut)

**Week 2** (Current - Assembly in progress):
1. ✅ All components verified functional
2. 🔄 Awaiting final hardware (L brackets, 52mm saw, truss screws)
3. 🔄 Begin component mounting per quickstart.md
4. 🔄 Execute drilling and wiring tasks

**Week 3** (Assembly & testing):
1. Complete assembly
2. Execute 6-phase testing protocol (quickstart.md)
3. Document test results
4. First field test (non-critical use)

**Week 4+** (Deployment):
1. Winter camping field test with diesel heater
2. Monitor BMV-712 data, optimize settings
3. Document lessons learned for future improvements

---

## Specific Product Links (Examples)

### Amazon Quick Links (verify current prices)

**Anderson Powerpole**:
- Search: "PowerWerx PP45 5-pair kit" or "Anderson Powerpole 45 amp red"
- Alternative: Individual pairs ~$3-5 each

**Powerwerx TRIcrimp**:
- Direct: https://powerwerx.com/tricrimp-powerpole-crimping-tool
- Amazon: Search "Powerwerx TRIcrimp"
- Price: $80-120

**Blue Sea 5026**:
- Amazon: Search "Blue Sea 5026" or ASIN B001P6FTTG (verify)
- West Marine: In-stock at marine stores
- Price: $50-70

**Victron BMV-712**:
- Amazon: Search "Victron BMV-712 Smart"
- West Marine, Fisheries Supply, Victron dealers
- Price: $200-250

**Wire**:
- Amazon: "12 AWG marine tinned copper wire" (select length, color)
- Auto parts store: Ask for "automotive primary wire TXL" in bulk

**100A ANL Fuse**:
- Amazon: "100A ANL fuse 3 pack"
- Auto parts store: May need to order (not always stocked)

---

## Assembly Prerequisites Checklist ✅

**Electrical Components**:
- [x] 100A ANL fuse (7× total) + inline holder
- [x] Blue Sea 5026 fuse block
- [x] ST blade fuses (10A, 15A, 20A, 30A assortment)
- [x] 2× KarlKers panel-mount Powerpole units (Charge + Heater)
- [x] 10× generic Powerpole PP45 pairs
- [x] Knoweasy Powerpole crimper
- [x] Wire: 4 AWG red/black (6ft each), 10 AWG red/black (20ft each), 12 AWG red/black (15ft each)
- [x] Ring terminals (M8 battery, assorted)
- [x] Heat-shrink tubing (assorted)

**Monitoring**:
- [x] Victron BMV-712 kit (shunt, display, RJ12 cable, temp sensor)

**Enclosure & Components**:
- [x] Greenmade 27gal tote
- [x] Nilight 4-in-1 panel
- [x] VEVOR 200Ah battery (verified 13.34V)
- [x] VEVOR 20A charger (verified 14.64V)

**Fabrication**:
- [x] 3/4" plywood battery base (15"×25" rounded corners)
- [x] 3/4" plywood left panel (12" tall, 8"→5" tapered)
- [x] 4× steel strap loops with screws
- [x] 2× cam buckle straps (1" webbing)
- [ ] L brackets with screws (arriving today Jan 24)
- [ ] #8×3/4" truss head screws (125 pc, shipping)

**Consumables**:
- [x] Electrical tape, dielectric grease
- [x] Zip ties, grommets (8 pc), ventilation mesh
- [x] Cleaning supplies (sandpaper, alcohol, rags)
- [x] Labels for circuit identification

**Tools**:
- [x] Multimeter
- [x] Wire strippers (10-14 AWG capable)
- [x] Knoweasy Powerpole crimper
- [x] Screwdrivers
- [x] Drill + step drill bit (1/4"-1-3/8")
- [ ] 52mm hole saw (arriving Jan 30)
- [x] Jigsaw/Dremel (for Nilight cutout)
- [x] Heat gun
- [x] Wrenches for battery terminals
- [x] Safety glasses
- [x] Circular saw (plywood cutting)

---

## Notes

- **Actual prices** as of 2026-01-24 procurement: ~$1,199 spent + ~$59 already owned = ~$1,258 total project value
- **Wire lengths** included 20% margin for routing, mistakes, future repairs - proved adequate
- **Anderson Powerpole**: Generic PP45 pairs worked well, KarlKers panel-mount units arrived intact
- **Victron BMV-712** includes all necessary cables and shunt - no additional parts needed ✅
- **Blue Sea 5026** uses standard ATO/ATC blade fuses ✅
- **Temperature sensor deferred to v2** (manual IR thermometer sufficient for v1)
- **Status LEDs deferred to v2** (Nilight panel ON indicator + Victron BMV-712 display cover basic status needs)
- **Fabrication improvements**: Tapered panel (8"→5") and rounded base corners (15"×25") fit tote geometry better than original plan

---

## Deferred to v2 (Not Purchasing Now)

- Temperature sensor (DS18B20 or NTC thermistor with display)
- Status LED system (3-LED voltage comparator circuit)
- Battery heating pad (for sub-freezing charging)
- Solar charge controller integration
- Inverter (AC output capability)
- Additional output circuits beyond 6 currently planned (evaluate after field testing v1)

These can be added later without major rework due to modular design (spare circuits on Blue Sea 5026, Anderson Powerpole standardization).

---

**Document Status**: ✅ Procurement complete (99%), awaiting L brackets + 52mm saw + truss screws  
**Current Phase**: Assembly & fabrication (Phase 2)  
**Next Step**: Complete drilling and component mounting per tasks.md  
**Reference**: See [component-selection.md](component-selection.md) for specifications and [tasks.md](../tasks.md) for execution progress
