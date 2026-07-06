---
id: pastures
name: Pastures (production mechanics)
category: building
affects: [food, industry, efficiency]
version: v71
evidence: measured
status: open
---

# Pastures (production mechanics)

Per-room output/day = **Base Rate × Efficiency × Capacity × Skill × Animals × Adult Animals × Tending × Drought** (all multiplicative; measured, matches [[production-math]]). Auroch base rates: meat 0.560, leather 0.560, livestock 0.088.

**Adult Animals is the dominant early swing:** the multiplier ≈ the adult fraction of the herd, with an apparent floor of 0.10 — a freshly stocked pasture full of juveniles produces ~10% of its potential *even fully staffed and tended*. Let herds mature before judging or slaughtering. *(measured, 4 rooms; floor is a 1-point inference)*

**Capacity scales with area, modulated by ground:** ~70–78 tiles per capacity point observed, but one same-map room needed 111 — consistent with soil setting animal density (ROOMS, dev-stated). Check the Soil overlay before siting ([[overlays]]). Max animals ≈ 1.36 × capacity multiplier *(inference)*.

**Tending is binary-survival:** one missed day lowers produce; **two consecutive missed days kill livestock** (tooltip verbatim). Production of the current day is based on the previous day's work.

**Skill modifier envelopes** (where headroom lives, from tooltip ranges): multiplicative — Species ≤1.20, Climate ≤1.25, Moisture 0.5–1.075 (excess-over-100% moisture works but is capped), Realm ≤2.0, Event 0.4–2.0, Overtime ≤1.25; additive — **Faction ≤+6.0**, **Technology ≤+5.2**, Nobilities ≤+2.5, Experience ≤+1.0, Tools ≤+1.0, Religion ≤+0.05, Titles ≤+0.15. Species and climate are chosen at setup ([[run-setup-priorities]]); the big lifetime levers are faction, technology, and nobles.

Flag (unresolved): very large pastures may lose workload to travel time — one 2,035-tile room ran 34% workload with tending unmet while smaller rooms sat ≥90%. Test whether splitting oversized pastures fixes tending.

- depends-on: —
- see-also: [[production-math]], [[food-harvest-cadence]], [[overlays]]

**Source:** [[2026-07-06-test-pastures-production]], [[2026-07-06-gamedata-guide-notes]]

## History

- **2026-07-06 (measured):** card created from curator's 4-pasture tooltip dataset; formula verified numerically.
- **2026-07-06 (measured, Soil overlay):** the capacity-per-tile spread is NOT explained by soil on the observed map — soil was uniformly high where all 4 pastures stand. Remaining suspects for the 111-vs-~75 outlier: unusable tiles inside an irregular coastal footprint, or a non-soil density input. Flag stays open, hypothesis narrowed.
