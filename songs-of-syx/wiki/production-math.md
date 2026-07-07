---
id: production-math
category: mechanic
affects: [industry, efficiency, logistics]
version: v71
evidence: game-data
status: verified
---

# Production math (multipliers vs additives)

The formula behind every industry (dev manual, Ch13):

```
rate per worker  = base rate × all multipliers × (1 + sum of all additives)
daily production = rate per worker × employees × workload
```

| Multiplicative (dominant) | Additive (diminishing as they stack) |
|---------------------------|--------------------------------------|
| degradation, efficiency, species aptitude | tools, technology, nobles, education, experience |

Dev: "the multiplicative elements are much more important than the additive ones." The
species multiplier is usually the only one that can become positive. Stacking: two +100%
additives sum to 300% speed; two ×2 multipliers give ×4 — the same as combining one +100%
additive with one ×2 multiplier.

Increasing production also increases input consumption — it is strictly the *speed* of
production, not its efficiency. Input savings come from consumption-node techs ([[tech-tree]]).

Workload differs by room type. Farms cap total work per day, so over-staffing is fine and
buffers travel distance — a low workload means you can remove farmers without losing
output. Workshops have a fixed number of working spots, so a workload below 100% means
missing workers, storage overflow, or a supply issue — never over-staffing.

Proximity: workers fetch resources within a short radius at zero production cost (hover
the consumption icon to see how many workbenches benefit at each range); beyond it,
hauling eats work time. With [[free-fetch]], this removes most warehouse-adjacency
assumptions — see [[logistics-system]].

Strategy (dev-stated, Ch16): early game, specialize — the multiplicative species boost
means tech and workers concentrated on the industries your species excels at beat
diversification until the capital is large.

- depends-on: —
- see-also: [[tech-tree]], [[free-fetch]], [[logistics-system]], [[training-grounds]] (maintenance/degradation applies to all rooms)

**Source:** [[2026-07-06-gamedata-guide-notes]], [[2026-07-06-test-pastures-production]], [[2026-07-07-test-hunters-production]]

## History

- **2026-07-06 (measured → status verified):** curator's 4-pasture tooltip dataset confirms the formula numerically — per-room total is a pure product of factors, and the Skill stat itself displays `product(multipliers) × (1 + sum(additives))` (observed: 1.61 × 2.21 = 3.28). Dev manual and live game agree; first formula-level verification in the wiki.
- **2026-07-07 (measured, hunters ×5):** formula verified on a second room type — base = rate × employees × work-load × commute, then multiplicative block, then ×(1+tech). Displayed multipliers are rounded to 2 decimals; back-solved actuals differ ~0.5% from display. New finds: commute >100% is a base *bonus*; Employees multiplier is ×0.70 at full staffing on every room (not fill-rate — driver unknown); multiplier envelopes are room-type-specific (hunter Climate 1.000↔1.200 vs pasture 0.750↔1.250) ([[2026-07-07-test-hunters-production]]).
- **2026-07-07 (measured, full factor tooltip — [[2026-07-07-test-hunter-formula]]):** whole formula seen at once on Hunter #001 (base 2.200 × 11 × 1.00 × commute 1.04 = 25.168; multipliers Degrade 1.00 · Employees 0.70 · Luck 0.79 · Efficiency 0.95 · Species 1.20 = 0.63; +tech 1.00; total 31.80 — arithmetic checks). Resolves: **Employees ×0.70 at 11/11 fill confirms it is NOT fill-rate** (driver still unlabeled); Commute 1.04 confirmed a base bonus; panel-header Efficiency 100% ≠ formula multiplier ×0.95. Full per-factor min↔max envelope recorded.
