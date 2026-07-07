---
id: amevia
name: Amevia
category: race
version: v71
evidence: game-data
status: verified
source: gamedata-v71/data/assets/init/race/Q_AMEVIA.txt
# --- dataview summary fields ---
playable: true
climate: hot
terrain: coastal
archetype: fisher
strong: [fishing, clay, globdien-pasture]
weak: [farming, orchards, general-pastures]
refuses: []
costs: [cold-intolerant, no-work-preferences]
---

# Amevia

Coastal/aquatic fishers (file `Q_AMEVIA`). A specialist economy built on water — and a
data-light race: the file carries **no `WORK` preference block and no affinity block**.

## Two channels (read separately)

Production is fully defined; preference is **absent** — Amevia lists no `PREFERRED.WORK`,
so every job reads as neutral (0) by default. See [[species-aptitudes]]. Both channels
key on species, not status ([[slavery]]).

## Production (capital rooms)

| Room | × |
|------|---|
| Fishery | 1.25 |
| Mine-Clay / Pasture-Globdien | 1.2 |
| Farm / Orchard / Pasture (general) | 0.8 |

A fishing race first; clay and Globdien pasture are secondary. Weak at land farming.
Unlisted rooms ×1.0 [Likely].

## Preference (likes / dislikes)

None defined — the `WORK` block is empty, so there is no fulfillment steer or
auto-assignment favour by job. [Likely] a deliberate "neutral preference" design, but
flagged as a data gap rather than assumed.

## Traits & costs

- **Terrain wet ×1.5, ocean ×1.5** — an aquatic/coastal race; needs water.
- **Climate hot ×1.0, temperate ×0.5, cold ×0.25** — warm-water; cold resistance −0.4.
- **Death age ×1.5** — long-lived. Growth 0.05, pop cap ×0.8.
- **Mass ×1.25, blunt attack +20, offence ×1.1** — heavy melee brawlers.
- Sanity ×1.5, Lawfulness ×0.8, Submission ×0.5 — stable but wilful.

## Preferences & affinities

Food: fish, vegetable, egg. Build materials: none listed. Affinity block empty — how
Amevia regards other races isn't in the file; other races' feelings toward Amevia live
on their cards ([[human]] 0.75, [[dondorian]] 1.0, [[garthimi]] 1.0, [[cretonian]] 0.05).

## Open

- **No `WORK` preference block and no `OTHER_RACES` block** in the file — genuine data
  gaps, not omissions on this card. Worth an in-game check of whether the UI shows any
  job preference for Amevia.
- Blank-cell defaults ([Likely] ×1.0 / 0) not spot-checked in game.
- `WORLD_BUILDING_*` world-map layer parked (fishery ×1.5).
