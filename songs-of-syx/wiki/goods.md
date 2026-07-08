---
id: goods
category: goods
status: verified
version: v71
source: gamedata
---

# Goods (resources)

All 42 stored/tradeable resources, grouped by the file `CATEGORY_DEFAULT` (0–4) and sorted by
decay ascending (ties alphabetical). Decay is the file `DEGRADE_RATE` — higher spoils faster; it
drives food buffering ([[food-supply-diagnosis]]) and storage planning ([[logistics-system]]).
Category **4 (military equipment) does not count toward raider wealth** ([[raiders]]). Category
labels describe each group's members; the game stores the numeric index. Which building makes each
good is on [[buildings]].

## Food & drink (0)

| Good | Decay |
|------|-------|
| Ration | 0.05 |
| Egg | 0.1 |
| Shedeh | 0.1 |
| Piva | 0.2 |
| Mushroom | 0.25 |
| Fruit | 0.5 |
| Vegetable | 0.5 |
| Meat | 0.75 |
| Bread | 1.0 |
| Fish | 1.0 |

## Raw materials (1)

| Good | Decay |
|------|-------|
| Gem | 0.001 |
| Coal | 0.01 |
| Ore | 0.01 |
| Stone | 0.01 |
| Sithilon Ore | 0.025 |
| Fibre | 0.05 |
| Clay | 0.1 |
| Grain | 0.1 |
| Leather | 0.1 |
| Wood | 0.1 |
| Herb | 0.2 |
| Opiate | 0.2 |
| Livestock | 0.5 |

## Refined materials (2)

| Good | Decay |
|------|-------|
| Furniture | 0.02 |
| Cut Stone | 0.05 |
| Fabric | 0.05 |
| Metal | 0.05 |
| Paper | 0.05 |
| Pottery | 0.05 |

## Manufactured (3)

| Good | Decay |
|------|-------|
| Jewelry | 0.01 |
| Machinery | 0.05 |
| Tool | 0.05 |
| Clothes | 0.1 |

## Military equipment (4)

| Good | Decay |
|------|-------|
| Bow | 0.05 |
| Falcata | 0.05 |
| Flanx | 0.05 |
| Shield | 0.05 |
| Spear | 0.05 |
| Warhammer | 0.05 |
| Leather Armour | 0.1 |
| Plate Armour | 0.1 |
| War-Beast | 0.2 |

- depends-on: —
- see-also: [[buildings]], [[food-supply-diagnosis]], [[trade]], [[production-math]]

**Source:** game-data — `init/resource/*.txt` (DEGRADE_RATE, CATEGORY_DEFAULT), `text/resource/*.txt` (names).
