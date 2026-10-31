# Diesel Heater Module (002) — Enclosed-Heater Decision and Order

**Status:** **ORDER PLACED (User-reported, 2026-10-31); NOT YET RECORDED AS RECEIVED, INSPECTED, INSTALLED, TESTED, OR COMMISSIONED.**
**Current direction:** Purchased enclosed heater; the custom aluminum-frame project is paused and retained as design history.
**Decision and order date:** 2026-10-31 (owner report)
**Companions:** [spec.md](spec.md), [design.md](design.md), [bom.md](bom.md) and [cad/](cad/README.md) document the **prior, now-paused VEVOR split-heater frame design**, not the purchased Hcalory product.
**Related electrical system:** [Battery Box V1 verification](../001-battery-box/verification-and-safety.md) — **not yet approved for connecting any heater load**.

## 1. Owner decision and procurement status

| Field | Record | Evidence |
|---|---|---|
| Selected product | **Hcalory TB2S+ Diesel Heater Toolbox 2S Plus, 6L Wireless Remote Upgraded** | **User-reported** model/version selection, reaffirmed 2026-10-31 |
| Product reference | [Hcalory TB2S+ official listing](https://hcalory.com/products/tb2s-diesel-heater-toolbox-2s-plus-6l-wireless-remote-upgraded) | Product identification; not an order receipt |
| Order status | **Ordered on 2026-10-31** | **User-reported**; receipt, invoice and seller transaction details not examined |
| Quantity | One heater ordered (working assumption from singular owner statement; order details not independently reviewed) | **User-reported/inferred; confirm against receipt if a procurement audit is needed** |
| Price paid, shipping, taxes, order number, seller | **Unknown / not recorded** | Do not substitute advertised prices for actual purchase cost or add private order numbers |
| Shipping, delivery and condition | **Unknown / not reported** | No claims of receipt or inspection |
| Intended primary use | Winter camping with the THUNDERBAY Ice Cube 6–8 insulated shelter | **User-reported** |
| Preferred control feature | Wireless remote sensing temperature **inside the shelter** and regulating heater operation outside | **Owner decision**; advertised behavior to be confirmed after receipt |
| Electrical supply concept | Direct use of the existing 12 V LiFePO4 battery system is desired; household AC-to-DC adapter is included per owner's understanding of the listing | **User-reported / Manufacturer-advertised (unverified kit contents)**; DC harness connector, current requirements and power interface have **not** been inspected or approved |

The selected purchase is an **enclosed all-in-one diesel heater**, rather than parts to enclose the previously owned heater. The brand/model is recorded as selected and ordered; manufacturer performance claims, included accessories and actual on-site functionality remain **unverified** until the owner's inventory and tests.

## 2. Why the direction changed

- **Owner decision (2026-10-31):** prioritize **remote in-shelter temperature regulation** over a case optimized for accessory storage.
- **Owner-reported comparison:** the proposed TNUTZ aluminum-frame structural materials alone were expected to cost about **$160–$180** before the remaining integration and build effort. This is a planning estimate, **not** a receipt or approved cart total.
- A complete enclosed heater with an integrated 6 L tank avoids building a custom portable frame to carry the separate 2 kW VEVOR heater and 10 L tank.
- Simpler transport and setup are important for winter camping. This purchase is a convenience and functionality decision, **not** a claim that the Hcalory is independently proven more reliable or safer.

## 3. Disposition of existing equipment and historical design

| Item / workstream | Current status |
|---|---|
| Existing VEVOR XMZ-D2 split-type 12 V 2 kW heater and separate 10 L tank | **Retain as owned equipment** for a possible later project; no sale, disposal or conversion is planned |
| Proposed 18-piece TNUTZ EXM-2020 frame, 28 CBK-020-A kits, 10 additional T-nuts and seven mounting screw/washer sets | **NOT ORDERED** as reported by owner; **purchase deferred indefinitely pending a new explicit decision** |
| `spec.md`, `design.md`, `bom.md`, CAD layouts, cut schedules, calculations and historical PRs | **Preserve without deletion as a paused design record**; not current Hcalory assembly instructions, procurement authority or commissioning criteria |
| Legacy G1-P, G2-D and G1–G5 frame release gates | **Remain closed** and apply only to the historical custom-frame route; they do not constitute an approved installation or operating procedure for the purchased heater |

No previous VEVOR-frame measurements, assumptions or manufacturer instructions are to be presented as tested specifications for the Hcalory TB2S+.

## 4. Next actions after delivery (not yet performed)

1. **Receipt/inventory:** record actual model label, package contents, remote, fuel tank, AC-to-DC adapter, DC harness, ducts/exhaust components and manuals; verify differences from the listing.
2. **Electrical interface review:** record the heater's DC input voltage range, mating connector and polarity, expected startup/steady power, appropriate protective device and cable specifications from the supplied documentation; separately verify and approve the corresponding Battery Box load circuit **before connection**. Do not assume the included AC adapter is required when using an approved 12 V DC supply.
3. **Thermostat behavior:** document where temperature is sensed, whether the unit modulates and/or completes controlled stop/restart cycles, temperature offset/hysteresis and remote signal-loss behavior from the manual and supervised observations.
4. **Camping integration:** select practical outside-heater placement, clean-air routing and warm-air duct entry to the shelter, exhaust separation and a separate working CO alarm inside the shelter; resolve manufacturer's ventilation and weather limits.
5. **Commissioning evidence:** later record approved setup and supervised functional tests, including startup/shutdown and electrical behavior. **Nothing in this decision/order record authorizes operation, unattended use, overnight use or connection to Battery Box V1.**

## 5. Evidence and change history

- **2026-10-31 — User-reported:** owner selected and ordered the **Hcalory TB2S+ 6 L Wireless Remote Upgraded** model (explicitly the Plus version). No amount, merchant confirmation, tracking information, delivery or testing evidence supplied.
- **2026-10-31 — Owner decision:** pause the TNUTZ structural purchase and custom-frame implementation; keep the VEVOR split heater for potential future use and preserve its documented design history.
- **Repository action:** documentation-only transition; does **not** order additional parts, change the battery box, adjust any safety gate, alter CAD, or authorize physical work.
