# Battery Box v1 - Consolidated Shopping List

**Date**: 2026-01-18  
**Feature**: 001-battery-box  
**Status**: Ready to purchase

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

| Item | Quantity | Est. Price | Product Search | Notes |
|------|----------|-----------|----------------|-------|
| **100A ANL Fuse** | 3-pack | $5-10 | "100A ANL fuse" Amazon | 1 installed + 2 spares |
| **ANL Fuse Holder** (inline) | 1 | $8-15 | "ANL fuse holder 100A" Amazon | 4-6 AWG wire compatibility |
| **Blue Sea Systems 5026 Fuse Block** | 1 | $50-70 | "Blue Sea 5026" Amazon/West Marine | 12 circuits, 100A busbar, marine-grade |
| **ST Blade Fuse Assortment** | 1 kit | $10-15 | "Automotive blade fuse assortment" Amazon | 10A, 15A, 20A, 30A (120pc kit) |

**Priority 1 Subtotal**: ~$73-110

---

### Anderson Powerpole Connectors

| Item | Quantity | Est. Price | Product Search | Notes |
|------|----------|-----------|----------------|-------|
| **Anderson Powerpole PP45 Pairs** | 10 pairs | $25-40 | "45A Quick Connect Battery Connector 10 Pair AWG10-12" Amazon | Pre-bonded red+black pairs + contacts |
| **Knoweasy Powerpole Crimper** | 1 | $30-50 | "Knoweasy Powerpole Crimper" Amazon | Budget alternative, PP15/30/45 compatible |

**Configuration Notes**:
- Each **bonded pair** = red housing + black housing clicked together (positive + negative)
- Need **10 pairs total** for 5 circuits (2 ends per circuit: panel mount + cable plug)
- Contacts included in 10-pair kit
- Compatible with genuine Anderson Powerpole system

**Alternative**: Powerwerx TRIcrimp ($80-120) for professional-grade tool if preferred

**Priority 1 Subtotal**: ~$55-90

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

| Item | Quantity | Est. Price | Product Search | Notes |
|------|----------|-----------|----------------|-------|
| **Ring Terminal Assortment** | 1 kit | $15-25 | "Marine ring terminal assortment" Amazon | M6/M8 battery, various for fuse holders |
| **Heat-Shrink Tubing Assortment** | 1 kit | $10-20 | "Heat shrink tubing assortment kit" Amazon | 1/4", 3/8", 1/2", 3/4", 1" sizes |
| **Zip Ties Assortment** | 100-pack | $5-10 | Hardware store/Amazon | 4", 6", 8" sizes |

**Priority 1 Hardware Subtotal**: ~$30-55

---

## Priority 2: Professional Battery Monitoring

| Item | Quantity | Est. Price | Product Search | Notes |
|------|----------|-----------|----------------|-------|
| **Victron BMV-712 Smart Battery Monitor** | 1 kit | $200-250 | "Victron BMV-712" Amazon/West Marine | Includes shunt, display, RJ12 cable, temp sensor |

**Why Critical**: 
- Accurate SOC% via coulomb counting (solves LiFePO4 flat discharge curve issue)
- Runtime predictions for diesel heater overnight winter camping
- Bluetooth monitoring from tent
- Historical data, alarms, battery health tracking

**Priority 2 Subtotal**: ~$200-250

---

## Priority 3: Consumables & Hardware

| Item | Quantity | Est. Price | Source | Notes |
|------|----------|-----------|--------|-------|
| Electrical tape (3M Super 33+) | 1 roll | $5 | Hardware store | |
| Dielectric grease | 1 tube | $5-10 | Auto parts store | Battery terminal corrosion prevention |
| Sandpaper/wire brush | 1 each | $3-5 | Hardware store | Terminal cleaning |
| Isopropyl alcohol 90%+ | 1 bottle | $5 | Pharmacy/hardware | Surface cleaning |
| Shop towels/rags | 1 pack | $5 | Hardware store | |
| Label maker or labels | 1 | $5-20 | Office supply/Amazon | Circuit labeling |
| Cable glands/grommets | 6-8 pc | $10-15 | Amazon | Strain relief for panel penetrations |
| Ventilation mesh | 1 ft² | $5-10 | Hardware store | Stainless or plastic, cover vent holes |
| Safety glasses | 1 | $5-10 | Hardware store | Drilling safety |

**Priority 3 Subtotal**: ~$48-90

---

## Tools to Verify/Purchase

### Already Owned (Verify Condition)
- [ ] Multimeter (DC voltage, continuity testing)
- [ ] Wire strippers (verify handles 10-14 AWG range)
- [ ] Screwdrivers (Phillips, flathead)
- [ ] Drill
- [ ] Heat gun or lighter (heat-shrink)
- [ ] Adjustable wrench or socket set (battery terminals)

### May Need to Purchase

| Tool | Est. Price | Product Search | Notes |
|------|-----------|----------------|-------|
| Step drill bit set or hole saw | $15-40 | Hardware store/Amazon | For enclosure cutouts (Nilight panel ~4-6", Powerpole 1.25", BMV-712 52mm, ventilation 1") |
| Wire strippers (if existing won't handle 10 AWG) | $15-30 | "Klein Tools 11063W" Amazon | Handles AWG10-20 |

**Tools Subtotal**: ~$0-70 (depending on what you already have)

---

## Budget Summary

| Category | Estimated Cost |
|----------|---------------|44-350 |
| **Priority 2: Victron BMV-712** | $200-250 |
| **Priority 3: Consumables** | $48-90 |
| **Tools (if needed)** | $0-70 |
| **GRAND TOTAL** | **$1,039-1,427** |

**Remaining to Purchase**: ~$492-760

**Note**: Budget adjusted for:
- Added 4 AWG black wire (main negative trunk): +$12-18
- Switched to budget Knoweasy crimper vs TRIcrimp: -$50
- Switched to generic Powerpole-compatible connectors: -$5-10 |

**Remaining to Purchase**: ~$520-832 (Priority 1-3 + tools)

---

## Shopping Strategy

### Phase 1: Core Build (Order Immediately)
**Budget**: ~$272-422
- 100A ANL fuse + holder
- Blue Sea 5026 fuse block
- Blade fuse assortment
- Anderson Powerpole PP45 connectors (5 pairs)
- Powerwerx TRIcrimp tool
- Wire (all gauges)
- Ring terminals, heat-shrink, zip ties

**Why First**: Cannot proceed with assembly without these components.

### Phase 2: Professional Monitoring (Order with Phase 1 or Shortly After)
**Budget**: ~$200-250
- Victron BMV-712 Smart battery monitor

**Why Important**: Critical for winter camping safety (diesel heater runtime monitoring). Can technically test basic system without it, but should install before first camping trip.

### Phase 3: Consumables & Hardware (Order with Phase 1 or Pick Up Locally)
**Budget**: ~$48-90
- Electrical tape, dielectric grease, cleaning supplies
- Cable glands, ventilation mesh, labels
- Safety equipment

**Why**: Needed during assembly, but many items available at local hardware store same-day if forgotten.

---

## Suggested Procurement Timeline

**Week 1** (Now):
1. Order Priority 1 (core electrical) from Amazon/PowerWerx
2. Order Priority 2 (Victron BMV-712) from Amazon/West Marine
3. Purchase Priority 3 consumables from local hardware store

**Week 2** (When parts arrive):
1. Verify all components received
2. Begin assembly per quickstart.md
3. Purchase any forgotten consumables locally as needed

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

## Assembly Prerequisites Checklist

Before starting assembly, verify you have:
-compatible pairs (10×) with contacts
- [ ] Knoweasy Powerpole crimper (or Powerwerx TRIcrimp if preferred)
- [ ] Wire: **4 AWG red (4ft), 4 AWG black (6-8ft)**holder
- [ ] Blue Sea 5026 fuse block
- [ ] ST blade fuses (10A, 15A, 20A, 30A)
- [ ] Anderson Powerpole PP45 pairs (5×)
- [ ] Powerwerx TRIcrimp tool
- [ ] Wire: 4 AWG red (4ft), 10 AWG red/black (25ft each), 12 AWG red/black (20ft each)
- [ ] Ring terminals (M8 battery, assorted for fuses)
- [ ] Heat-shrink tubing (assorted)

**Monitoring**:
- [ ] Victron BMV-712 kit (shunt, display, cables)

**Enclosure & Components** (already purchased):
- [ ] Greenmade 27gal tote
- [ ] Nilight 4-in-1 panel
- [ ] VEVOR 200Ah battery (verify delivered)
- [ ] VEVOR 20A charger (verify delivered)

**Consumables**:
- [ ] Electrical tape, dielectric grease
- [ ] Zip ties, cable glands, ventilation mesh
- [ ] Cleaning supplies (sandpaper, alcohol, rags)
- [ ] Labels for circuit identification

**Tools**:
- [ ] Multimeter
- [ ] Wire strippers (10-14 AWG capable)
- [ ] Powerwerx TRIcrimp
- [ ] Screwdrivers
- [ ] Drill + step bits/hole saws
- [ ] Heat gun
- [ ] Wrenches for battery terminals
- [ ] Safety glasses

---

## Notes

- **Prices are estimates** as of 2026-01-18. Verify current pricing before purchase.
- **Wire lengths** include 20% margin for routing, mistakes, future repairs.
- **Anderson Powerpole contacts** are included with housing pairs (verify when ordering).
- **Victron BMV-712** includes all necessary cables and shunt - no additional parts needed.
- **Blue Sea 5026** uses standard ATO/ATC blade fuses (same as inline holders would use).
- **Temperature sensor deferred to v2** (manual IR thermometer sufficient for v1).
- **Status LEDs deferred to v2** (Nilight panel ON indicator + Victron BMV-712 display cover basic status needs).

---

## Deferred to v2 (Not Purchasing Now)

- Temperature sensor (DS18B20 or NTC thermistor with display)
- Status LED system (3-LED voltage comparator circuit)
- Battery heating pad (for sub-freezing charging)
- Solar charge controller integration
- Inverter (AC output capability)
- Additional output circuits beyond 6 currently planned

These can be added later without major rework due to modular design (spare circuits on Blue Sea 5026, Anderson Powerpole standardization).

---

**Document Status**: Ready for procurement  
**Next Step**: Begin Phase 1 ordering (core electrical components)  
**Reference**: See [component-selection.md](component-selection.md) for detailed specifications and rationale
