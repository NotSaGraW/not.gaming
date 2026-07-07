---
id: cantor
name: Cantor
category: race
version: v71
evidence: game-data
status: verified
source: gamedata-v71/data/assets/init/race/CANTOR.txt
# --- dataview summary fields ---
playable: false
climate: none
terrain: none
archetype: industrial-titan
strong: [mining, refining, workshops, woodcutting]
weak: [farming, academia]
refuses: []
costs: [haven-gated, no-immigration, no-preference]
---

# Cantor

A non-playable **haven-gated** giant: mechanically the best industrial worker in the
game, with zero preference for any of it. Acquired through havens, not started as, and
not a natural immigrant ([[run-setup-priorities]]).

## Two channels (read separately)

The extreme divergence case for [[species-aptitudes]]: superb production, near-null
preference. `PREFERRED.WORK` is a flat `*: 0` with only Court (+10) and Guard (+0.5)
above it — Cantor *likes* nothing economic but *produces* at ×2 anyway. Both channels
key on species, not status ([[slavery]]).

## Production (capital rooms)

| Room | × |
|------|---|
| Mine / Refiner / Workshop / Woodcutter | 2.0 |
| Pasture / Fishery | 0.8 |
| Farm / Orchard | 0.6 |
| School / University | 0 |

Double output across the whole industrial chain, plus Stockpile +10 storage. Useless
at food and education. This is why Cantor labour (often enslaved) is prized.

## Preference (likes / dislikes)

Effectively none: default `*: 0`. Court (+10), Guard (+0.5). No fulfillment steer.

## Traits & costs

- **Not playable; Immigration ×0** — you don't grow Cantor; you acquire them via havens
  or capture. Reproduction speed ×0.
- **Physical titan:** Health ×10, Mass ×5, Death age ×10, Blunt attack +300, defence
  +250, Morale ×3, Lawfulness ×10, Sanity ×10000 — near-unbreakable heavy infantry.
- No climate/terrain profile in the file (doesn't settle by climate like the playable
  races). Religion Athuri.

## Preferences & affinities

Food: egg, meat, fish. Build materials: Grand (1.0), Stone (0.5). Warm to most
([[tilapi]], [[cretonian]], [[amevia]], [[dondorian]] 1.0); hostile to [[human]]
(0.05), [[garthimi]], [[argonosh]] (0.01).

## Open

- Haven-acquisition requirements not yet carded (see havens / world layer).
- `WORLD_BUILDING_*` / climate absent by design; blank defaults [Likely], not verified in game.
