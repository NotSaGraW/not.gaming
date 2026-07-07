---
id: human
name: Human
category: race
version: v71
evidence: game-data
status: verified
source: gamedata-v71/data/assets/init/race/HUMAN.txt
# --- dataview summary fields ---
playable: true
climate: temperate
terrain: flatland
archetype: scholar-generalist
strong: [education, knowledge, admin, farming]
weak: [mining]
refuses: [gem-mining]
costs: [low-sanity, low-lawfulness, short-lived]
---

# Human

The default playable race: temperate-climate flatlanders with no terrain lock and no
sharp specialisation. Their one real economic edge is **knowledge work** — schools,
universities, libraries, laboratories, admin — paid for with the worst sanity and
lawfulness of any species. The forgiving starter, but a crime-prone one.

## Two channels (read separately)

A race carries two independent job signals that can disagree — the general mechanic is
on [[species-aptitudes]]:

- **Preference** (`PREFERRED.WORK`) — how much subjects *like* a job: fulfillment and
  auto-assignment favour, **not** output.
- **Production** (`BOOST.ROOM_*>MUL`) — the species multiplier in the [[production-math]]
  formula, applied to output. Read literally (×).

Both key on species, never on status: a Human works identically free, pleb, or slave —
only fulfillment differs ([[slavery]]).

## Production (capital rooms)

| Room | × |
|------|---|
| School / University | 1.5 |
| Admin / Library / Laboratory | 1.25 |
| Farm / Orchard | 1.1 |

Only species with an Innovation/Administration/Knowledge bonus. Farm boost (+10%) is
real but half of [[cretonian]]'s (+25%). Unlisted rooms default to ×1.0 [Likely].
World-map camps (`WORLD_BUILDING_*`) parked for a future world-layer card.

## Preference (likes / dislikes)

Strong: Library, Laboratory (+2.0); University, Stage, Embassy (+1.0). Mild (+0.75):
most workshops, admin, tavern, tomb, school. Dislikes: gem mining (−1.0), coal/ore
refining (−0.75). Nothing hard-barred.

## Traits & costs

- **Sanity ×0.8, Lawfulness ×0.75** — lowest of any race; more Deranged and crime.
  Weigh against [[law-and-order]] and asylum/[[health-and-disease]].
- **Death age ×0.8** — shorter-lived, faster population turnover.
- **Cold/Hot resistance −0.15 each** — the reason they lock to temperate (climate ×1.0
  temperate, ×0.8 otherwise); on open terrain ×1.5, mountain/forest ×0.2.
- **Immigration ×1.5** — strong upside: Humans draw settlers faster than any race,
  reinforcing them as the populous default.
- Minor: blunt attack +10; otherwise combat-average.

## Preferences & affinities

Food: bread, meat, mushroom, egg; drinks anything. Build materials: Grand (1.0) >
Stone (0.7) > Wood (0.5); mountain-carved (0.2) least liked. Neutral (+0.75) to all
races except cooler toward [[tilapi]] (+0.2); [[dondorian]] pairs well (shared food,
road, structure tastes). Others tolerate Humans at a flat 1.0 — universally easy
neighbours.

## Open

- Blank-cell defaults ([Likely] ×1.0 production / 0 preference) not yet spot-checked in game.
- `WORLD_BUILDING_*` world-map layer parked.
