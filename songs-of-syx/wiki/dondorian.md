---
id: dondorian
name: Dondorian
category: race
version: v71
evidence: game-data
status: verified
source: gamedata-v71/data/assets/init/race/DONDORIAN.txt
# --- dataview summary fields ---
playable: true
climate: cold
terrain: mountain
archetype: craftsman-miner
strong: [workshops, jewelry, smithy, mining]
weak: [farming, orchards, academia]
refuses: []
costs: [non-reproducing, heat-intolerant]
---

# Dondorian

Mountain-dwelling craftsmen: the best workshop race, long-lived, and demand-driven —
they barely reproduce, so you grow them by immigration, not birth.

## Two channels (read separately)

Preference vs production — general mechanic on [[species-aptitudes]]. Both key on
species, not status ([[slavery]]).

## Production (capital rooms)

| Room | × |
|------|---|
| Workshop-Smithy / Jewelry | 1.25 |
| Workshop (general) | 1.20 |
| Mine | 1.15 |
| Refiner | 1.0 |
| Farm | 0.75 |
| Orchard | 0.65 |
| School / University | 0 / 0.4 |

Craft-and-mine specialists; poor farmers and near-useless in schools. Note the
mountain build affinity below makes them the natural carve-into-the-rock race.

## Preference (likes / dislikes)

Loves: **Tavern (+5.0)**, Jewelry (+2.5), Smithy (+2.0); carpenter, paper, brewery,
hunter (+1.0). Mild dislikes: gem mining (−0.5), coaler (−0.25). Nothing hard-barred.

## Traits & costs

- **Reproduction speed ×0 + Immigration ×25** — Dondorians do **not** breed; the whole
  population arrives by settlement. Plan growth around immigration, not nurseries.
- **Death age ×1.8** — long-lived, so slow turnover once settled.
- **Sanity ×5.0, Lawfulness ×1.0** — stable and orderly; low crime.
- **Cold resistance +0.25, climate cold ×1.0 / hot ×0.1; terrain mountain ×5.5** — a
  cold-mountain race, crippled on flatland or in heat.
- Combat: Block ×1.25, formation +0.5 — solid defensive infantry; weak bows (×0.75).

## Preferences & affinities

Food: meat, fish, mushroom. Build materials: **Mountain (1.0)** — carved rooms — then
Grand (0.6), Stone (0.3). Warm to [[human]], [[amevia]], [[cretonian]], [[cantor]]
(1.0), [[tilapi]] (0.75); hostile to [[garthimi]] (0.02), [[argonosh]] (0.01). Pairs
notably well with [[human]] (shared food/road/structure tastes).

## Open

- Blank-cell defaults ([Likely] ×1.0 / 0) not spot-checked in game.
- `WORLD_BUILDING_*` world-map layer parked (mine ×1.5, agriculture ×0.5).
