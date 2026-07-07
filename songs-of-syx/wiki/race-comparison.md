---
id: race-comparison
name: Race comparison (generated view)
category: reference
version: v71
evidence: game-data
status: verified
source: rebuilt from the race cards
---

# Race comparison (generated view)

A live table rebuilt from the race cards — **not authoritative**, same status as
`index.md`. Renders **only in Obsidian with the Dataview plugin**; in GitHub or VS Code
the block below shows as code, not a table. The authoritative numbers live on each race
card ([[species-aptitudes]] explains the two channels).

```dataview
TABLE playable, climate, terrain, archetype, strong, weak, refuses, costs
FROM "wiki"
WHERE category = "race"
SORT playable DESC, archetype ASC
```

If Dataview is not installed, ask the cataloguer to regenerate the comparison from
source, or read the individual cards: [[human]], [[cretonian]], [[dondorian]],
[[garthimi]], [[tilapi]], [[amevia]], [[cantor]], [[argonosh]].
