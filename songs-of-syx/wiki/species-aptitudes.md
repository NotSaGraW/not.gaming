---
id: species-aptitudes
name: Species aptitudes (the two-channel model)
category: mechanic
affects: [industry, fulfillment, population]
version: v71
evidence: game-data
status: verified
source: gamedata-v71/data/assets/init/race/*.txt
---

# Species aptitudes (the two-channel model)

Every race carries **two independent job signals** in its init file, and they can
disagree. Reading them as one number is the common mistake — a race can love a job it
is mediocre at, or excel at a job it resents.

## The two channels

- **Preference** — the `PREFERRED.WORK` block. Values run roughly −4…+5, centred on 0.
  This drives **fulfillment** (subjects are happier in jobs they like — dev manual:
  "fulfillment is increased by subjects having jobs they like") and **auto-assignment
  favour** (which species the workforce logic steers into a room). It does **not**
  change output. Read it by sign and rank, not as a multiplier.

- **Production** — the `BOOST.ROOM_*>MUL` block. Values centre on 1.0. This *is* the
  species multiplier in the [[production-math]] formula — the dominant, only-positive-
  capable term. Read it literally: `ROOM_LIBRARY_NORMAL>MUL: 1.25` = ×1.25 output.

Because the two are separate, [[human]] can produce +10% at farms (`ROOM_FARM* 1.1`)
while having no farm *preference* at all — productive but indifferent. [[cantor]] is
the extreme case: ×2.0 output across industry with near-zero preference for any of it
(mechanically superb, fulfillment-blind).

## Both key on species, never on status

Neither block has a citizen/pleb/slave dimension — status is not a variable in them.
So output is identical regardless of legal status; a [[human]] works a library at
×1.25 free or enslaved. What status changes lives in the separate `STATS` block
(fulfillment/behaviour), which is why slaves work the same but are unhappier
([[slavery]]). Curator-confirmed in play: no observed work difference between worker
types.

## Reading the raw values

- **Blank cells** default by block: an unlisted `ROOM_*>MUL` = ×1.0 (no boost); an
  unlisted `WORK` job = 0 (neutral preference). [Likely] — not yet spot-checked in
  game; one hover on an unlisted job settles it.
- **Wildcard vs specific**: a specific key overrides a wildcard. [[dondorian]] is
  `ROOM_FARM*: 0.75` but `ROOM_FARM_MUSHROOM: 1.0` — bad at farms generally, neutral
  at the one mountain crop.
- **Sentinels**: extreme values (WORK −10, −100; output ×2+) read as "hard barred /
  hard forced," not points on a continuous scale. Note `>ADD` operators mixed into
  BOOST are additive, not multiplicative (e.g. `ROOM_STOCKPILE>ADD`).
- **Two contexts**: `ROOM_*` governs capital rooms; a parallel `WORLD_BUILDING_*` set
  governs world-map camps (later-game expansion). Cards scope to `ROOM_*` unless noted.

## Per-race cards

Each race owns its own values: [[human]], [[cretonian]], [[dondorian]], [[garthimi]],
[[tilapi]], [[amevia]], [[cantor]], [[argonosh]]. A generated Dataview summary lives
in [[race-comparison]] (Obsidian-only view, rebuilt from the cards, not authoritative).

## Open

- Blank-cell defaults [Likely], pending one in-game hover.
- `WORLD_BUILDING_*` world-map production layer parked for a future card.
