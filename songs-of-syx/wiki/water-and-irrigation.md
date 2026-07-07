---
id: water-and-irrigation
category: mechanic
affects: [food, efficiency, health]
version: v71
evidence: game-data
status: open
---

# Water & irrigation (pumps, canals, pressure)

The system (dev manual, Ch32): **pumps → pressure → canals → freshwater aura.**

| Element | Behaviour |
|---------|-----------|
| Pump | Placed on groundwater (near natural freshwater; overlay highlights it). Outputs 100 pressure = 100 canal tiles; multiple pumps add pressure. Upgrading lowers workers needed, not pressure. |
| Canal | Consumes 1 pressure per tile; radiates a freshwater aura up to 15 tiles that raises fertility (farms, orchards, pastures) and boosts woodcutters. Slows subjects crossing it. |
| Culvert | Like a canal but connects to other culverts within 8 tiles, flowing water under walls and roads. Costs more, uses more pressure. |
| Pool / moat / pond | Swimming (small satisfaction boost). Operational pools consume pressure. |

Aura effect on output (Ch9): orchards up to +5%, pastures up to +10% from full irrigation.

Economic consequence (curator synthesis): irrigation cost scales with distance from
groundwater — every 100 tiles of canal is another pump, and pumps can only start on
groundwater. So moisture is cheap to fix near fresh water and effectively semi-frozen far
from it. "Fix it later with canals" holds only within pressure range of a water source
([[run-setup-priorities]]: moisture is a *conditionally* flattened gradient).

Moisture can exceed 100% (v71), but per-room benefit caps low — pasture skill multiplier
≤1.075, measured ([[pastures]]).

- depends-on: —
- see-also: [[pastures]], [[food-harvest-cadence]], [[run-setup-priorities]], [[overlays]] (Moisture / Fresh Water / Salt Water overlays)

**Source:** [[2026-07-06-gamedata-guide-notes]], [[2026-07-06-test-pastures-production]]
