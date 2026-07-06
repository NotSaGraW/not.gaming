---
id: production-math
name: Production math (multipliers vs additives)
category: mechanic
affects: [industry, efficiency, logistics]
version: v71
evidence: game-data
status: verified
---

# Production math (multipliers vs additives)

The formula behind every industry (dev manual, Ch13): **base rate × all multipliers × (1 + sum of all additives)** = rate per worker; × employees × workload = daily production.

- **Multiplicative** (dominant): degradation, efficiency, species aptitude. Dev: "the multiplicative elements are much more important than the additive ones — take care to maintain and build your industries well." Species is usually the only multiplier that can exceed 1.
- **Additive** (diminishing relative value as they stack): tools, technology, nobles, education, experience. Two +100% additives = ×3; one additive +100% and one multiplicative ×2 = ×4.
- Increasing production speed **also scales input consumption** — it's speed, not efficiency. Input savings come from consumption-node techs ([[tech-tree]]).

**Workload semantics differ by room type:** farms cap total work per day — over-staffing is fine and buffers travel time; low workload = you can remove farmers. Workshops have fixed slots — workload under 100% means missing workers, storage overflow, or supply failure, never "too many staff."

**Proximity:** workers fetch inputs within a short radius at zero production cost (hover the consumption icon to see the radius per workbench count); beyond it, hauling eats work time. Combined with [[free-fetch]], this kills most warehouse-adjacency dogma — see [[logistics-system]].

Strategy implication (dev-stated, Ch16): early game, **specialize** — the species multiplier compounds with tech additives, so concentrating research and workers on industries your species excels at beats diversification until the capital is large.

- depends-on: —
- see-also: [[tech-tree]], [[free-fetch]], [[logistics-system]], [[training-grounds]] (maintenance/degradation applies to all rooms)

**Source:** [[2026-07-06-gamedata-guide-notes]], [[2026-07-06-test-pastures-production]]

## History

- **2026-07-06 (measured → status verified):** curator's 4-pasture tooltip dataset confirms the formula numerically — per-room total is a pure product of factors, and the Skill stat itself displays `product(multipliers) × (1 + sum(additives))` (observed: 1.61 × 2.21 = 3.28). Dev manual and live game agree; first formula-level verification in the wiki.
