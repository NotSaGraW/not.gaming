# Source: in-game test — hunter's cabin production tooltips (v71)

- **Origin:** test (curator's tooltip screenshots; conditions: 5 hunter's cabins, ~478 pop, temperate coastal map, all rooms fully staffed at 100% fill, species multiplier ×1.20 on all rooms, technology additive +1.00, no tools/faction/nobility/religion bonuses shown)
- **Date:** 2026-07-07
- **Immutable. Do not edit.**

---

## Formula verification (production tooltip, per room)

Hunter tooltips expose a different base decomposition than pastures: **Base = rate × employees × work-load × commute**, then × product(multipliers) × (1 + sum(additives)). Verified numerically on 5 rooms, e.g. 2.200 × 11 × 1.00 × 1.05 = 25.410; 25.41 × 0.84 × (1 + 1.00) = +42.50 (matches display).

Displayed multiplier products are rounded to 2 decimals: back-solving from displayed totals gives ~0.876 where the tooltip prints 0.88 (~0.5% residual). The formula is exact; the display is not.

## Base rate (hunter, meat)

- Meat 2.200 per employee-day (before multipliers)

## Multiplier envelopes (min ↔ max shown in tooltip)

Multipliers: Degrade 0.250↔1.000 | Employees 0.000↔1.000 | Luck 0.600↔1.400 | Efficiency 0.500↔1.000 | Overtime 1.000↔1.250 | Species 0.100↔1.200 | Climate 1.000↔1.200 | Event 0.100↔2.000 | Other Effects 1.000↔1.050
Additives: Technology 0.000↔4.000 (only additive listed for this room)

## Observations (5 rooms, same species/map, same moment)

| Room | Size | Employees | Work-load | Commute | Base | Empl. | Luck | Effic. | Species | Mult (shown) | Tech | Total/day | Today | Yesterday | This yr | Last yr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| #001 | 87 | 11/11 | 1.00 | 1.05 | 25.410 | 0.70 | 1.05 | 0.95 | 1.20 | 0.84 | +1.00 | 42.50 | 40 | 41 | 513 | 1.13K |
| #002 | 75 | 9/9 | 1.00 | 1.06 | 20.988 | 0.70 | 1.05 | 1.00 | 1.20 | 0.88 | +1.00 | 36.77 | 30 | 39 | 432 | 282 |
| #003 | 75 | 9/9 | 1.00 | 1.06 | 20.988 | 0.70 | 1.05 | 1.00 | 1.20 | 0.88 | +1.00 | 36.77 | 34 | 27 | 425 | 80 |
| #004 | 75 | 9/9 | 1.00 | 1.05 | 20.790 | 0.70 | 1.05 | 1.00 | 1.20 | 0.88 | +1.00 | 36.43 | 38 | 27 | 426 | 79 |
| #005 | 30 | 3/3 | 1.00 | 1.05 | 6.930 | 0.70 | 1.05 | 1.00 | 1.20 | 0.88 | +1.00 | 12.14 | 10 | 10 | 115 | 0 |

## Facts and anomalies

- **Employees multiplier ≠ fill rate.** All 5 rooms are fully staffed (11/11, 9/9, 3/3) yet show Employees ×0.70 with range 0.000↔1.000. Uniform value across rooms of different sizes suggests a population-level driver (skill? effective presence?), not a room property. Driver unidentified — hover check pending.
- **Commute enters the base as a >1 multiplier.** Rooms showing commute stat 105–106% get base × 1.05–1.06 — above 100% is a bonus, not a penalty.
- **Header/tooltip mismatch (#001):** room header shows efficiency 100%; tooltip applies Efficiency ×0.95. UI stat and formula input are not the same figure.
- **Luck ×1.05 on all 5 rooms simultaneously** in one snapshot — consistent with a shared (global/daily) roll rather than per-room, single snapshot cannot distinguish.
- **Capacity is not a clean function of room size:** 87→11, 75→9, 30→3 slots (7.9–10.0 tiles/slot). Consistent with slots coming from placed furniture, as measured on training grounds.
- **Unidentified second figure** under the meat estimate: 4.056–4.331 per room, scales with neither employees nor total. Meaning unknown.
- Climate multiplier range for this room reads 1.000↔1.200 (pastures showed 0.750↔1.250) — envelope appears room-type-specific.
