# Source: in-game test — auroch pasture production tooltips (v71)

- **Origin:** test (curator's tooltip screenshots; conditions: 4 auroch pastures, ~471 pop, temperate coastal map, skill ~348–354%, technology additive +1.20, no tools/faction/nobility/religion bonuses)
- **Date:** 2026-07-06
- **Immutable. Do not edit.**

---

## Formula verification (production tooltip, per room)

Total/day = Base Rate × Efficiency × Capacity × Skill × Animals × Adult Animals × Tending × Drought — all multiplicative. Verified numerically on 4 rooms, e.g. 0.560 × 14.57 × 3.54 × 1.00 × 0.64 = 18.46 (matches display).

Skill tooltip displays its own formula: product(multipliers) × (1 + sum(additives)) — observed: 1.61 × (1 + 1.21) = 3.28. Matches the dev-manual production model exactly.

## Base rates (auroch)

- Meat 0.560 | Leather 0.560 | Livestock 0.088 (per capacity·skill unit/day)

## Skill modifier envelopes (min ↔ max shown in tooltip)

Multipliers: Moisture 0.500↔1.075 | Realm 0↔2.000 | Overtime 1.000↔1.250 | Species 0.100↔1.200 | Climate 0.750↔1.250 | Event 0.400↔2.000 | Other 0.450↔1.103
Additives: Experience 0↔1.000 | Tools 0↔1.000 | Faction 0↔6.000 | Religion 0↔0.050 | Nobilities 0↔2.500 | Technology 0↔5.200 | Titles 0↔0.150

## Observations (4 rooms, same species/map)

| Room | Tiles | Capacity | Animals (adult) | AdultAnim. mult | Workload | Meat/day |
|---|---|---|---|---|---|---|
| #001 | 858 | 7.70 | 11 (11) | 1.00 | 91% | 15.0 |
| #002 | 2035 | 28.98 | 35/39 (23) | 0.69 | 34% | 35.6 |
| #003 | 1129 | 14.57 | 20 (12) | 0.64 | 93% | 18.5 |
| #004 | 1199 | 15.40 | 21 (0) | 0.10 | 90% | 3.0 |

- Adult Animals multiplier ≈ adult fraction (0.657→0.69; 0.60→0.64; 0 adults→0.10 — apparent floor 0.10). Cataloguer inference from 4 points.
- Tiles per capacity point varies on one map: ~70–78 (3 rooms) vs 111 (#001) — consistent with soil-density claim (ROOMS), unchecked against Soil overlay.
- Animal max ≈ 1.36 × capacity multiplier across all 4 rooms (inference).
- Tending tooltip verbatim: failing to tend one day lowers produce; "failing two days in a row results in livestock dying."
- Moisture tooltip: room needs average 100% for full boost; observed map average 212% → "212% target value"; skill moisture multiplier nonetheless capped at 1.075 (showed 1.08).
- Anomaly, unresolved: #002 (2035 tiles) showed 34% workload with tending unmet while 3 smaller rooms sat ≥90% — possible travel-time loss at large pasture size.
