---
id: food-supply-diagnosis
category: strategy
affects: [food, logistics, population]
version: v71
evidence: measured
status: open
---

# Food supply — why "days of food" stays low with a surplus

Measured symptom: production exceeds consumption, yet the Food panel shows only 2 days and
never climbs, with **every food 0 in warehouses**. The surplus is not accumulating in
reachable/preserved storage. The exact split between decay and distribution is **not yet
quantified** — flagged below.

## The measured case (~950 pop, Tilapi)

| Food panel | Value |
|------------|-------|
| Production Rate | +595.90 |
| Consumption Rate | −412.80 |
| Net | **+183 / day** |
| Stored | 885 |
| Food Days | **2.0** (flat) |

Two candidate causes — **not yet separated, both unquantified:**

- **Distribution.** Every food read **0 in warehouses**, and a large meat pile was observed
  in production storage rather than in warehouses/stalls (exact quantity/location — one
  pasture vs city total — not confirmed). Food that never reaches the warehouse/stall
  pipeline may not count toward reachable food.
- **Decay.** Un-warehoused food decays at the raw rate (table below). How much of the
  +183/day surplus is lost to decay versus simply sitting uncounted was **not measured** —
  do not assume decay accounts for all of it.

Open, to measure in-game: whether the food-days meter counts production-storage food, and
what the tooltip "% Stored" means numerically (per day / snapshot / per year).

## Food decay (game-data `DEGRADE_RATE`, and in-game tooltip "stored" rate un-warehoused)

| Food | DEGRADE_RATE | Tooltip "stored" | Keeps? |
|------|--------------|------------------|--------|
| Ration | 0.05 | — | best |
| Egg | 0.1 | −5% | good |
| Fruit | 0.5 | −25% | poor |
| Meat | 0.75 | (not observed) | poor |
| Bread | 1.0 | — | worst |
| Fish | 1.0 | −50% | worst |

Observed on 3 tooltips only: the "stored" decay ≈ 50 × DEGRADE_RATE for un-warehoused goods
(fish 1.0→50%, fruit 0.5→25%, egg 0.1→5%) — a 3-point pattern, not confirmed as the formula.
Manual (Ch8/Ch11): warehouses slow spoilage; whether a food service does is untested.

## What to try (safe regardless of the exact cause)

1. **Convert meat to Rations** *(game-data, solid).* DEGRADE_RATE 0.05 vs meat 0.75 — 15×
   slower; rations keep wherever they sit. Eggs (0.1) also keep.
2. **Get food into warehouses** *(addresses the measured 0-warehoused).* Assign food crates,
   pull orders / prioritize, and enough haulers so food reaches preserved storage instead of
   sitting in production output.
3. Don't rely on **Fish/Fruit** for a buffer — both were running per-food deficits (fish
   −5.24, fruit −10.29) *and* decaying fast (measured).
4. *(Untested)* if food stalls turn out to hoard food, lowering food servings would reduce
   how much they pull — verify before relying on it.

- depends-on: [[free-fetch]], [[logistics-system]]
- see-also: [[food-harvest-cadence]], [[pastures]], [[trade]]

**Source:** [[2026-07-07-test-food-supply]]
