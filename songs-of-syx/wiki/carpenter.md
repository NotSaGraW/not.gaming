---
id: carpenter
category: building
status: verified
version: v71
source: gamedata
---

# Carpenter

> Workshop that carves Furniture out of Wood.

Bonus (tech): Wood Carving — increases effectiveness of Carpenters. Emits noise.

## Recipes

Selectable per workshop. Values are the base `IN`/`OUT` per unit of work — actual throughput is
this ratio run through the production formula ([[production-math]]), scaled by worker skill, tools,
tech and species multiplier.

| Recipe | Inputs | Output |
|--------|--------|--------|
| Furniture | 2 Wood | 0.5 Furniture |
| Spear (wood/stone) | 2 Wood + 2.5 Stone | 0.5 Spear |
| Spear (wood/metal) | 1 Wood + 0.4 Metal | 1.0 Spear |
| Warhammer | 2 Wood + 2.5 Stone | 0.25 Warhammer |
| Shield | 6 Wood + 2 Leather | 1.0 Shield |

Inputs/outputs link to [[goods]].

## Room factors

| Factor | Value |
|--------|-------|
| Base fulfillment (the job itself) | 0.5 |
| Accidents per year | 0.025 |
| Internal storage | 50 |
| Upgrade tiers | 2 (boost 0 → 1) |
| Build materials (palette) | Stone, Wood, Metal |

Floor is free (`AREA_COSTS` all 0); the material *amounts* — placeable items, upgrade tiers,
upkeep — are deferred to the build-cost card, not stated here.

## By species

Two independent channels ([[species-aptitudes]]): **output** is a production multiplier (no race
has a carpenter-specific one, so all use the `ROOM_WORKSHOP*` wildcard); **work preference** feeds
fulfillment, not output — a species can be efficient at a job it dislikes, or content at one it's
mediocre at. Sorted by output.

| Species | Output ×(workshop) | Work preference |
|---------|--------------------|-----------------|
| [[cantor]] | 2.0 | 0 (via `*` default) |
| [[dondorian]] | 1.20 | 1.0 |
| [[human]] | 1.0 | 0.75 |
| [[tilapi]] | 1.0 | unlisted |
| [[amevia]] | 1.0 | unlisted |
| [[argonosh]] | 1.0 | 0 (via `*` default) |
| [[cretonian]] | 0.8 | unlisted |
| [[garthimi]] | 0.75 | unlisted |

"unlisted" = the race file gives no explicit `PREFERRED.WORK` entry for Carpenter and no `*`
default, so the engine default applies (not shown in the files — do not read as 0). Cantor and
Argonosh set an explicit `*: 0`.

- depends-on: —
- see-also: [[buildings]], [[goods]], [[production-math]], [[species-aptitudes]]

**Source:** game-data — `init/room/WORKSHOP_CARPENTER.txt` (INDUSTRIES recipes, WORK.FULFILLMENT/ACCIDENTS, STORAGE, UPGRADES, RESOURCES), `init/race/*.txt` (`BOOST.ROOM_WORKSHOP*>MUL` output, `PREFERRED.WORK.WORKSHOP_CARPENTER` preference), `text/room/WORKSHOP_CARPENTER.txt` (name, description).
