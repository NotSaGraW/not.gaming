---
id: overlays
name: Overlays (the in-game measurement layer)
category: mechanic
affects: [efficiency, logistics, health, fulfillment]
version: v71
evidence: measured
status: open
---

# Overlays (the in-game measurement layer)

The overlay menu (v71, curator screenshots 2026-07-06) is the game's instrumentation — the primary tool for verifying this wiki's claims against a live city. Available overlays: Foundation, Guard posts, Lighting, Moisture, Paint-Tool, Problem, Salt Water, Soil, Urbanisation, Fresh Water, Homeless, Maintenance, Noise, Path-Usage, Public Punishment, Shape, Space, Work-load.

Mapping to cards — which instrument tests what:

| Overlay | Verifies |
|---|---|
| Noise | [[training-grounds]] / refiner placement — emission auras are compact, visible, per-source |
| Path-Usage | [[logistics-system]] — actual traffic, not assumed traffic |
| Maintenance | [[production-math]] degradation multiplier — pending jobs visible before decay bites |
| Foundation | build-cost rule (expensive rooms on good foundations) |
| Moisture / Fresh Water / Salt Water / Soil | agriculture placement ([[food-harvest-cadence]]) |
| Guard posts | [[law-and-order]] detection coverage (crime location is what matters) |
| Homeless | [[housing-and-priorities]] — rooms whose workers found no nearby home |
| Space / Shape | environmental fulfillment auras (roundness/squareness from walls) |
| Work-load | staffing per room ([[production-math]] workload semantics) |
| Problem | general fault finder |

**Method rule (from a real correction):** layout and placement judgments are made from overlays, not from map screenshots. The cataloguer requests the relevant overlay before critiquing; the curator's overlay screenshot is a `test`-grade source.

- depends-on: —
- see-also: [[production-math]], [[logistics-system]], [[housing-and-priorities]]

**Source:** [[2026-07-06-test-overlays]]

## History

- **2026-07-06 (measured):** card created after curator's overlay set falsified two cataloguer layout critiques (noise adjacency, spine congestion) made from raw screenshots.
