---
id: cretonian
name: Cretonian
category: race
version: v71
evidence: game-data
status: verified
source: gamedata-v71/data/assets/init/race/CRETONIAN.txt
# --- dataview summary fields ---
playable: true
climate: warm
terrain: flatland
archetype: pacifist-farmer
strong: [farming, orchards, rations, refining]
weak: [academia, workshops, combat]
refuses: [hunting, fightpit, arena]
costs: [short-lived, pacifist, cold-intolerant]
---

# Cretonian

The farm race, and the classic labour/slave stock: docile, fast-breeding, and averse
to violence. Best food producer in the game, poor at everything cerebral or martial.

## Two channels (read separately)

Preference (`PREFERRED.WORK`) vs production (`BOOST.ROOM_*>MUL`) — general mechanic on
[[species-aptitudes]]. Both key on species, not status ([[slavery]]).

## Production (capital rooms)

| Room | × |
|------|---|
| Farm / Orchard | 1.25 |
| Workshop-Ration | 1.2 |
| Refiner | 1.1 |
| Workshop (general) | 0.8 |
| School / University | 0.5 |

Best farm multiplier of any race (+25%, vs [[human]]'s +10%). Weak at crafts and half
as effective in education. Unlisted rooms ×1.0 [Likely].

## Preference (likes / dislikes)

Loves: Inn, Embassy (+3.0); Orchard, Canteen, Eatery, Workshop-Ration (+2.0); grain,
fruit, veg farming (+1.5). Refuses: **hunting (−4.0), fightpit (−3.0), arena (−2.0)** —
a pacifist by disposition. Mild dislikes: smithy, archery, police (−0.25).

## Traits & costs

- **Growth 0.10, Submission ×1.25** — breed fast and obey; the reason they are the
  default slave/labour race ([[slavery]]).
- **Death age ×0.75** — short-lived; high turnover offsets the fast breeding.
- **Combat ×0.9 skill, Morale ×0.75** — weak soldiers; keep them off the line.
- **Cold resistance −0.25, climate cold ×0.2** — a warm/temperate race; useless in
  the cold. Immigration ×0.4 (low draw — they grow by birth, not settlement).
- Lawfulness +0.5 — law-abiding; low crime.

## Preferences & affinities

Food: vegetable, bread, fruit. Build materials: Wood (1.0), Outdoors (1.0) — plain
builders. Warm to [[cantor]] (1.0), [[tilapi]], [[dondorian]] (0.75); cool to [[human]]
(0.2); hostile to [[amevia]] (0.05), [[garthimi]] (0.02), [[argonosh]] (0).

## Open

- Blank-cell defaults ([Likely] ×1.0 / 0) not spot-checked in game.
- `WORLD_BUILDING_*` world-map layer parked (agriculture ×1.5, mine ×0.75).
