---
id: water-and-irrigation
name: Water & irrigation (pumps, canals, pressure)
category: mechanic
affects: [food, efficiency, health]
version: v71
evidence: game-data
status: open
---

# Water & irrigation (pumps, canals, pressure)

The system (dev manual, Ch32): **pumps → pressure → canals → freshwater aura.**

- **Pumps** must be placed on groundwater (found near natural fresh water; overlay highlights it). One pump = **100 pressure = 100 canal tiles**. Multiple pumps add pressure. Upgrading a pump reduces its workers, NOT its pressure.
- **Canals** consume 1 pressure per tile and radiate a freshwater aura **up to 15 tiles** — this is what raises moisture/fertility for farms, orchards (max +5%), woodcutters, and pastures (up to +10% output from full irrigation, per Ch9).
- **Culverts** bridge under obstructions (connect within 8 tiles) but cost more and consume more pressure. **Pools** consume pressure while operational. Canals slow subjects crossing them.

**The economic consequence (curator-sharpened):** irrigation cost scales with distance from groundwater — every 100 tiles of canal is another pump, and pumps can't start anywhere. So moisture is **cheap to fix near fresh water and effectively semi-frozen far from it**. Siting rule for moisture-hungry rooms: either the ground is already moist, or groundwater is near enough that a pump-and-canal run is short. "Fix it later with canals" is only true within pressure range of a water source ([[run-setup-priorities]] nuance: moisture is a *conditionally* flattened gradient).

Related: moisture can exceed 100% (v71) but per-room benefit caps low (pasture skill multiplier ≤1.075, measured — [[pastures]]).

- depends-on: —
- see-also: [[pastures]], [[food-harvest-cadence]], [[run-setup-priorities]], [[overlays]] (Moisture / Fresh Water / Salt Water overlays)

**Source:** [[2026-07-06-gamedata-guide-notes]], [[2026-07-06-test-pastures-production]]
