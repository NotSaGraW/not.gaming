---
id: animals
category: animal
status: verified
version: v71
source: gamedata
---

# Animals

The 9 animals in the game data. Six are **pasture livestock** — each is the animal behind one
[[pastures|pasture]] room and produces its listed goods when raised; the other three are **wild
fauna** taken by hunting, never pastured (no room references them). Yields link to [[goods]];
`Livestock` is the seed stock a pasture needs to populate. Descriptions are the game's own `DESC`
(`text/animal/`), unedited. Yields are per the animal's `RESOURCE_AMOUNT`.

| Animal | Pasture | Yields | Danger | Mass |
|--------|---------|--------|--------|------|
| Auroch | Yes | Meat 0.8, Leather 0.5 | 0.5 | 110 |
| Balticrawler | Yes | Meat 1.15 | 0.0 | 200 |
| Entelodont | Yes | Meat 1, Leather 0.25 | 0.25 | 55 |
| Globdien | Yes | Meat 0.5, Egg 0.25 | 0 | 45 |
| Onx | Yes | Meat 0.8, Fibre 0.5 | 0.1 | 45 |
| War-Beast | Yes | Meat 0.5, Leather 0.75 | 0.2 | 300 |
| Dinoris | wild | Meat 0.5, Egg 0.5 | 0.25 | 35 |
| Smilodon | wild | Meat 0.5, Leather 0.5 | 1.0 | 75 |
| Stagbeast | wild | Meat 0.5, Leather 0.75 | 0.2 | 75 |

## Climate multipliers

Suitability multiplier from the animal's CLIMATE block — higher = thrives, 0 = absent. (Exact in-game application not separately verified.)

| Animal | Cold | Temperate | Hot |
|--------|------|-----------|-----|
| Auroch | 0.8 | 1 | 0 |
| Balticrawler | 1.0 | 1.0 | 0.75 |
| Entelodont | 0.5 | 1 | 0.5 |
| Globdien | 0.1 | 0.4 | 1 |
| Onx | 1.0 | 1 | 0 |
| War-Beast | 1.0 | 0.75 | 0.25 |
| Dinoris | 0.0 | 1 | 0.5 |
| Smilodon | 0.5 | 0.5 | 0.1 |
| Stagbeast | 1.0 | 0.0 | 0 |

## Terrain multipliers

Suitability multiplier from the TERRAIN block; `None` is open/plains. Blank = not listed. Balticrawler's Mountain 1.0 vs 0.1 elsewhere matches its cave-dwelling description.

| Animal | Forest | Wet | Mountain | Ocean | Open (None) |
|--------|--------|-----|----------|-------|-------------|
| Auroch | 0.5 | 0.5 |  |  | 1.0 |
| Balticrawler | 0.1 | 0.1 | 1.0 |  | 0.1 |
| Entelodont | 1.0 | 1.0 |  |  | 0.2 |
| Globdien | 0.1 | 1 |  | 1 | 0.1 |
| Onx | 0.5 |  |  |  | 1.0 |
| War-Beast | 1.0 |  |  |  | 1.0 |
| Dinoris | 1.0 | 0.7 |  |  | 0.2 |
| Smilodon | 0.2 |  | 0.5 |  | 0.05 |
| Stagbeast | 1.0 |  |  |  | 0.2 |

## Descriptions

**Auroch** — Aurochs are giant beasts, found in the north, with a ferocious temperament.

**Balticrawler** — Balticrawlers are huge larvae, that prefer dark caves as their dwelling. They feed on fungus, which they sweep up from the stone floor.

**Entelodont** — A ferocious four-legged mammal, an Entelodont can both feed a family for several days, as well as inspire fear in the hearts of hunters. Their thick hides can blunt the impact of any hunting weapon if not used with enough strength. Its ferocity and fearlessness often lead the hunters of these creatures to lose their pride, and sometimes, their lives.

**Globdien** — The docile Globdiens have long since been domesticated by Amevias and Amevian settlers regularly take over a dozen eggs of these reptiles with them. As herbivores they are generally harmless to the average hunter in the wild, albeit their jaws can snap bone with ease. Their eggs are harvested and collected for purposes of animal husbandry and the occasional omelette.

**Onx** — An onx is a stubborn beast, best left to its grazing. Though generally peaceful, it can wreak havoc with its sharp horns and compact frame if provoked. It thrives in mountainous areas. Its favourite food is the Grieving Lilly, only found on southern ridges in dry and northern climates.

**War-Beast** — The war beast. Can be tamed enough to ride upon and give our troops much leverage in battle.

**Dinoris** — This majestic bird, though flightless, has often inspired works of art and the odd song or two. Occasionally hunted for its prized meat, this herbivore is also valued for its decorative feathers, used to adorn tiaras, crowns, helmets and various head wear. Some Dinorises are also rumoured to lay eggs of solid gold, but this has never been proven.

**Smilodon** — A deadly, fast, killing machine, this huge omnivore can run down any other known grounded animal. It often stays away from humanoids, but does not shy away from a fight. Few live to tell such a tale.

**Stagbeast** — A mighty antlered beast, this animal thrives on luscious plains. Their antlers make for impressive hunting trophies, as securing one of them means having to face off against a herd of these mighty animals, which can run down whole groups of hunters with their sharp antlers, capable of piercing all known armour.


- depends-on: —
- see-also: [[pastures]], [[goods]], [[food-harvest-cadence]]

**Source:** game-data — `init/animal/*.txt` (RESOURCES/RESOURCE_AMOUNT, CLIMATE, TERRAIN, DANGER, MASS), `text/animal/*.txt` (NAME, DESC), pasture linkage via `ANIMAL:` field in `init/room/PASTURE_*`.
