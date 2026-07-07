---
id: tilapi
name: Tilapi
category: race
version: v71
evidence: game-data
status: verified
source: gamedata-v71/data/assets/init/race/TILAPI.txt
# --- dataview summary fields ---
playable: true
climate: temperate
terrain: forest
archetype: forager-archer
strong: [orchards, woodcutting, herding, hunting, bows]
weak: [mining]
refuses: [mining]
costs: [misanthropic]
---

# Tilapi

Forest foragers and archers: the game's default herder, strong on orchards and wood,
deadly with bows — and refuse to set foot in a mine.

## Two channels (read separately)

Preference vs production — general mechanic on [[species-aptitudes]]. Both key on
species, not status ([[slavery]]).

## Production (capital rooms)

| Room | × |
|------|---|
| Orchard / Woodcutter | 1.4 |
| Pasture (all) / Hunter / Workshop-Bowyer | 1.2 |
| Mine | 0.75 |

The broad herder — every pasture ×1.2 with positive preference across the board,
unlike [[garthimi]]'s single-animal spike. Orchards and woodcutting are the standouts.

## Preference (likes / dislikes)

Loves: cannibal (+4.0), police, hunter (+3.0); globdien/onx pastures (+1.5); most
pastures (+1.25); bowyer, archery (+1.0). **Refuses all mining (−10.0)** — hard-barred.
Farming only lukewarm (+0.25).

## Traits & costs

- **Bow ×1.5, Dexterity ×1.25, Speed ×1.4** — premier ranged skirmishers.
- **Death age ×1.4** — fairly long-lived. Growth 0.03, pop cap ×0.75 (small nation).
- **Terrain forest ×1.75; mountain/open/wet ~0** — a forest race, weak anywhere else.
  Climate temperate ×1.0.
- Bath/grooming/arena rates ×1.3 — service-hungry.

## Preferences & affinities

Food: meat, fruit, egg. Build materials: Wood (1.0), Outdoors (1.0). Misanthropic —
best affinity is only 0.4 ([[cantor]], [[argonosh]], [[cretonian]], [[amevia]]);
[[garthimi]] 0.3; **hostile to [[human]] and [[dondorian]] (0)**. Hard to mix into a
multi-race city.

## Open

- Blank-cell defaults ([Likely] ×1.0 / 0) not spot-checked in game.
- `WORLD_BUILDING_*` world-map layer parked (pasture ×1.25, orchard ×1.4).
