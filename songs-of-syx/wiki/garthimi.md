---
id: garthimi
name: Garthimi
category: race
version: v71
evidence: game-data
status: verified
source: gamedata-v71/data/assets/init/race/GARTHIMI.txt
# --- dataview summary fields ---
playable: true
climate: hot
terrain: mountain
archetype: beast-miner
strong: [mining, mason, hunting, balticrawler-pasture]
weak: [academia, farming, general-pastures]
refuses: [governing]
costs: [non-reproducing, short-lived, low-lawfulness]
---

# Garthimi

Bestial hot-climate miners and hunters. Strong backs, short lives, no natural births —
grown through the Breeder room — and constitutionally unfit to govern.

## Two channels (read separately)

Preference vs production — general mechanic on [[species-aptitudes]]. Both key on
species, not status ([[slavery]]).

## Production (capital rooms)

| Room | × |
|------|---|
| Pasture-Balticrawler | 3.0 |
| Workshop-Mason | 1.3 |
| Mine | 1.25 |
| Hunter | 1.2 |
| Breeder | 1.0 |
| Workshop / Farm / Orchard / Pasture (general) | 0.75 |
| Admin / Library | 0.6 |

**Not a general herder** — pastures are ×0.75 except Balticrawler at ×3.0 (specific
overrides wildcard; [[tilapi]] is the real herder). Mining/mason/hunting is the core.
Terrible in academia.

## Preference (likes / dislikes)

Loves: hunter, breeder, cannibal (+4.0), police (+3.0), Balticrawler pasture (+2.0),
coal/ore/stone mining (+2.0). **Cannot govern: court −100** (hard-barred). Dislikes all
farming (−0.5) and general pastures.

## Traits & costs

- **Reproduction age & speed ×0** — no natural births; population comes from the
  **Breeder** room ([[natural-propagation]]).
- **Death age ×0.5** — very short-lived; rapid turnover.
- **Speed ×1.4, Mass ×0.7** — small and fast. Lawfulness ×0.5 — crime-prone.
- **Climate hot ×1.0, cold ×0.2; terrain mountain ×1** — hot-mountain race.
- Religion Aminion; arena/doctor rates ×1.5.

## Preferences & affinities

Food: meat, fish. Build materials: Mountain (1.0), Stone (0.5). Warm only to
[[amevia]] and [[argonosh]] (1.0); cool to [[tilapi]] (0.3); hostile to everyone else —
[[human]], [[cretonian]], [[dondorian]], [[cantor]] all 0.02.

## Open

- Blank-cell defaults ([Likely] ×1.0 / 0) not spot-checked in game.
- `WORLD_BUILDING_*` world-map layer parked (mine ×1.5, Balticrawler ×3.0).
