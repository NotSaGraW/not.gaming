---
id: crafting
category: building
status: verified
version: v71
source: gamedata
---

# Crafting & Refining

The secondary-production buildings: **workshops** turn materials into finished goods, **refiners**
turn raw into intermediate. Recipes are the base `IN`/`OUT` per unit of work — actual throughput
runs through the production formula ([[production-math]]), scaled by skill, tools, tech and the
species multiplier. Inputs and outputs link to [[goods]]. Build and upkeep costs are deferred to
the cost card. Descriptions are the game's own (`text/room/`).

Output skill is a per-species **wildcard** — one value covers every building in the group
(`ROOM_WORKSHOP*` / `ROOM_REFINER*`), with a few building-specific overrides. Work *preference*
(the fulfillment a species gets from a job) is separate, keyed per building in each race's
`PREFERRED.WORK`; it lives on the species cards and [[species-aptitudes]], not here.

## Workshops

### Recipes

| Building | Inputs | Output |
|----------|--------|--------|
| Bowyer | 4.0 Wood + 1.0 Leather | 0.4 Bow |
| Carpenter | 2.0 Wood | 0.5 Furniture |
| Carpenter | 2.0 Wood + 2.5 Stone | 0.5 Spear |
| Carpenter | 1.0 Wood + 0.4 Metal | 1.0 Spear |
| Carpenter | 2.0 Wood + 2.5 Stone | 0.25 Warhammer |
| Carpenter | 6.0 Wood + 2.0 Leather | 1.0 Shield |
| Jeweller | 0.04 Metal + 0.1 Gem | 0.1 Jewelry |
| Masonry | 2 Stone | 0.5 Cut Stone |
| Mechanic | 1.0 Furniture + 0.4 Metal | 0.25 Machinery |
| Papermaker | 2.0 Wood | 0.75 Paper |
| Pottery | 1.0 Clay | 1 Pottery |
| Rationmaker | 6 Bread | 2 Ration |
| Rationmaker | 3 Bread + 0.025 Herb | 2.5 Ration |
| Rationmaker | 3 Meat + 0.125 Herb | 3 Ration |
| Rationmaker | 3 Fish + 0.125 Herb | 3 Ration |
| Rationmaker | 3 Fruit + 1 Shedeh | 3 Ration |
| Rationmaker | 3 Vegetable + 1 Shedeh | 3 Ration |
| Smithy | 2.0 Coal + 0.4 Metal | 2.0 Tool |
| Smithy | 2.0 Coal + 0.4 Metal | 0.15 Plate Armour |
| Smithy | 2.0 Coal + 0.4 Metal | 0.5 Falcata |
| Smithy | 2.0 Coal + 0.4 Metal | 0.25 Flanx |
| Smithy | 1.0 Coal + 0.4 Metal + 2 Wood | 0.5 Warhammer |
| Tailor | 4 Leather | 3.0 Clothes |
| Tailor | 4.0 Fabric | 3.0 Clothes |
| Tailor | 2.0 Leather | 0.25 Leather Armour |

### Room factors

| Building | Base fulfillment | Accidents/yr | Storage |
|----------|------------------|--------------|---------|
| Bowyer | 0.5 | 0.025 | 25 |
| Carpenter | 0.5 | 0.025 | 50 |
| Jeweller | 0.5 | 0.025 | 25 |
| Masonry | 0 | 0.025 | 25 |
| Mechanic | 0.5 | 0.025 | 25 |
| Papermaker | 0.5 | 0.025 | 40 |
| Pottery | 0.5 | 0.025 | 50 |
| Rationmaker | 0.5 | 0.025 | 150 |
| Smithy | 0 | 0.025 | 25 |
| Tailor | 0.5 | 0.025 | 150 |

### Output ×, by species (`ROOM_WORKSHOP*` wildcard)

| Species | × |
|---------|---|
| [[cantor]] | 2.0 |
| [[dondorian]] | 1.20 |
| [[human]] | 1.0 |
| [[tilapi]] | 1.0 |
| [[amevia]] | 1.0 |
| [[argonosh]] | 1.0 |
| [[cretonian]] | 0.8 |
| [[garthimi]] | 0.75 |

Building-specific overrides (replace the wildcard for that building):

| Species | Building | × |
|---------|----------|---|
| [[dondorian]] | Jeweller | 1.25 |
| [[dondorian]] | Smithy | 1.25 |
| [[dondorian]] | Bowyer | 0.8 |
| [[garthimi]] | Masonry | 1.3 |
| [[garthimi]] | Rationmaker | 0.9 |
| [[cretonian]] | Rationmaker | 1.2 |
| [[tilapi]] | Bowyer | 1.2 |

## Refiners

### Recipes

| Building | Inputs | Output |
|----------|--------|--------|
| Bakery | 6 Grain + 1.0 Wood | 6 Bread |
| Bakery | 7 Grain + 0.5 Coal | 7 Bread |
| Brewery | 2.0 Grain + 0.25 Pottery + 0.5 Coal | 2.5 Piva |
| Brewery | 2.0 Fruit + 0.25 Pottery + 0.5 Coal | 2.25 Shedeh |
| Charcoaler | 2 Wood | 6 Coal |
| Metal Smelter | 1.25 Coal + 1.25 Ore | 0.5 Metal |
| Weaver | 2 Fibre | 2 Fabric |

### Room factors

| Building | Base fulfillment | Accidents/yr | Storage |
|----------|------------------|--------------|---------|
| Bakery | 0 | 0.05 | 350 |
| Brewery | 0.5 | 0.05 | 125 |
| Charcoaler | — | 0.05 | 300 |
| Metal Smelter | — | 0.05 | 25 |
| Weaver | 0.5 | 0.05 | 100 |

### Output ×, by species (`ROOM_REFINER*` wildcard)

No building-specific overrides — every refiner uses the wildcard.

| Species | × |
|---------|---|
| [[cantor]] | 2.0 |
| [[cretonian]] | 1.1 |
| [[human]] | 1.0 |
| [[dondorian]] | 1.0 |
| [[tilapi]] | 1.0 |
| [[amevia]] | 1.0 |
| [[argonosh]] | 1.0 |
| [[garthimi]] | 0.9 |

- depends-on: —
- see-also: [[buildings]], [[goods]], [[production-math]], [[species-aptitudes]]

**Source:** game-data — `init/room/WORKSHOP_*.txt`, `init/room/REFINER_*.txt` (INDUSTRIES recipes, WORK.FULFILLMENT/ACCIDENTS, STORAGE), `init/race/*.txt` (`BOOST.ROOM_WORKSHOP*`/`ROOM_REFINER*` and building overrides), `text/room/*` (names), `text/resource/*` (good names).
