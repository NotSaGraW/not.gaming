---
id: argonosh
name: Argonosh
category: race
version: v71
evidence: game-data
status: verified
source: gamedata-v71/data/assets/init/race/ARGONOSH.txt
# --- dataview summary fields ---
playable: false
climate: none
terrain: none
archetype: enforcer
strong: [policing, war]
weak: [everything-economic]
refuses: []
costs: [haven-gated, no-immigration, no-economy]
---

# Argonosh

A non-playable **haven-gated** war race: no economy at all, built purely for policing
and battle. The mirror of [[cantor]] — where Cantor is an industrial titan, Argonosh
is a pure enforcer.

## Two channels (read separately)

`ROOM*>MUL: 0.1` — a blanket ×0.1 to all general room work, with only Barracks and
Archery at ×1. `PREFERRED.WORK` is `*: 0` plus Police (+10), Guard (+1), Execution (+1).
Argonosh neither likes nor produces economic work. See [[species-aptitudes]]; both
channels key on species, not status ([[slavery]]).

## Production (capital rooms)

| Room | × |
|------|---|
| Barracks / Archery | 1.0 |
| Stockpile | 0.5 |
| School / University | 0 |
| everything else (`ROOM*`) | 0.1 |

No civilian economy. Use them as garrison and law, not labour.

## Preference (likes / dislikes)

Police (+10), Guard (+1), Execution (+1); everything else 0. A living enforcement caste.

## Traits & costs

- **Not playable; Immigration ×0** — acquired via havens, not grown. Reproduction speed ×0.
- **War build:** Health ×3, Mass +160, Speed ×2, Blunt attack +240 / defence +120,
  Morale ×3, Pierce defence +2 — fast, heavy shock troops. Weak bows (×0).
- **Lawfulness ×5, Sanity ×1000, Submission ×0.3** — fanatically orderly, hard to break.
- No climate/terrain profile in the file. Religion Shmalor.

## Preferences & affinities

Food: meat, fish, egg. Build materials: Mountain (1.0), Stone (0.6). Warm to
[[garthimi]], [[human]], [[cretonian]], [[amevia]] (1.0); hostile to [[cantor]],
[[tilapi]], [[dondorian]] (0.01).

## Open

- Haven-acquisition requirements not yet carded (see havens / world layer).
- Climate/economy absent by design; blank defaults [Likely], not verified in game.
