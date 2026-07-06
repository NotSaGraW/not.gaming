# Medieval Dynasty — Structured Guide Draft

This draft reorganizes `medieval-dynasty/README.md` into a single practical document. The goal is to keep the existing information, make the flow easier to follow, and separate early-game decisions from mid- and late-game reference material.

## Overview

- This document is a working draft.
- The structure follows the player progression from early setup to settlement scaling.
- Reference tables are grouped at the end for easier lookup.

## Contents

1. Early setup
2. Survival
3. Initial settlement
4. Scaling
5. Settlement management
6. External systems
7. Reference

---

# 1. Early setup

## Starting out

The game eases you in. You wake up in **Sedowin's infirmary** — 4 beds, a fireplace for cooking, and a chest outside with 50kg of storage. It works as a temporary base while you get started. Your first tasks are talking to **Mirogod** and **Derwan**, which unlocks building permissions in the area.

Once the intro quests are done, a **starting chest** near Sedowin contains a bow, copper arrows, and other items. The **infirmary attic** also has items you can take.

**Building cap:** 70 by default, expandable to 140 in Customise Game.

## First buildings

Building everything as fast as possible is a trap — most buildings only make sense once you have NPCs, blueprints, or specific materials. These are the ones that provide real value early:

| Building | Tech points | Why it matters |
|---|---|---|
| Simple Small Wattle House | 0 | First shelter. Includes Stone Campfire for cooking. Requires only sticks, logs, stone and straw — no planks |
| Food Storage I | 5 Farming | 500kg capacity. The Hunting Lodge I chest only holds 50kg — build this early if you plan to store significant amounts of food |
| Resource Storage I | 50 Building | Allows production buildings within 50m to draw materials directly from it. NPCs can access it from any distance on the map |
| Hunting Lodge I | 50 Survival | Workbench and Drying Rack for crafting and preserving meat. Critical before winter |
| Woodshed I | 100 Building | Only needed if you require planks — Tier 1 buildings use logs, sticks and straw only |

Tier 1 buildings only require logs, sticks and straw — no planks needed. Planks only appear in Tier 2 construction onward.

### Getting Farming tech points early

Craft a Wooden Hoe (1 log + 5 sticks, hand-craftable), place a small field from the Q menu, and use the hoe on one or two plots. 5 points takes only a few minutes and unlocks Food Storage I.

## Storage basics

| Building | Tech points | Capacity |
|---|---|---|
| Resource Storage I | 50 Building | 1,000 kg |
| Resource Storage II | 1,000 Building | 2,000 kg |
| Resource Storage III | 10,000 Building | 4,000 kg |
| Food Storage I | 5 Farming | 500 kg |
| Food Storage II | 1,000 Farming | 1,000 kg |
| Food Storage III | 6,500 Farming | 2,000 kg |

Both storage types share a single combined inventory regardless of how many buildings of that type you have or where they are on the map.

### How storage works

- Production buildings within range can draw materials directly from Resource Storage — the player does not need to carry them.
- NPCs can access both storages from **any distance** on the map once either storage exists.
- Building chests are separate and do not connect to Resource or Food Storage.
- Player Remote Storage range: 50m (Tier I), 75m (Tier II), 100m (Tier III).

## Before storage exists

- Food, water and firewood → NPC house chest.
- Work tools → production building chest.

---

# 2. Survival

## Core mechanics

Year 1 is the hardest part of the game. Without infrastructure — shelter, food sources, tools — every parameter is a threat. Once the basics are covered, the game becomes progressively easier as production takes over.

Five parameters to keep in balance:

| Parameter | HUD bar | Effect when neglected |
|---|---|---|
| Health | Red, inner left | At 0 → death |
| Stamina | Green, outer left | At 0 → can't run or attack |
| Hunger | Orange | At 0 → continuous health loss |
| Thirst | Blue | At 0 → continuous health loss |
| Temperature | White marker | Out of range → continuous health loss |

Two additional states: **poison** drains health continuously until corrected. **Dirt** increases the risk of being poisoned by food — it does not drain health directly.

> Hunger, thirst, temperature and poison all kill the same way — continuous health drain until corrected. Stamina won't kill you directly but leaves you defenseless.

### Death and respawn

Dying on the Oxbow map respawns you in your house with **30 HP**, or in the nearest village if you don't have a house yet. You keep all items.

### Sleep

- Sleeping in a **bed** restores some health. Sleeping at a **campfire** does not.
- There is no penalty for not sleeping.
- Sleeping on the **last day of a season** fully restores health, hunger, thirst and dirt — regardless of current state.
- Heavy resources in your inventory at season change **teleport with you** to your house.

### Temperature and heat

- Heat effects begin at **30°C**.
- The first **3 years** have good weather only — dangerous conditions start from year 3.
- Heat sources in buildings and caves warm the character. Wading in a river cools them.
- Equipping a **torch** warms you — useful emergency fallback in winter without adequate clothing.
- Keep **two clothing sets** in your house chest (summer and winter) and swap at the start of each season.
- The starting clothes provide more protection than they appear to — removing them in summer may be worse than keeping them on.
- In your **first autumn**, craft a few torches in preparation for winter.

### Heating fuel order

The **Simple Small House includes a built-in fireplace** — once built, you have a permanent indoor heat source and cooking station.

Fuel order: **firewood → sticks → logs → planks**.
- Firewood cannot be hand-crafted — it requires a Woodshed.
- Sticks and logs work as direct fuel and are available from the start.

For NPCs, fuel is consumed automatically from Resource Storage. Without one, place fuel directly in the NPC's house chest.

### Dirt and poison

If the character is dirty, there is a chance of being poisoned by **any food** — not just raw meat. Washing in a river or lake removes dirt.

## Food

Three layers, ordered from least to most preparation required.

### Layer 1: Foraging

No tool, no building. Available immediately but with real risks.

**Berries**
- Ripe berries only grow in **summer** — dark blue colour, +0.2 food and +2 water each.
- In spring, only **unripe berries** (green) are available — +20% poison, minimal nutrition. Avoid except in extreme emergencies.
- Berries also hydrate — combined food and water source in the field.

**Mushrooms**
- Found mainly in **autumn**. Only Morels are available in spring and are safe.

| Mushroom | Poison | Safe |
|---|---|---|
| Bolete, Red Pine, Parasol | +0.5% | Yes |
| Morel | None | Yes |
| Fly Agaric | +100% | No |
| Wooly Milkcap, Bitter Bolete | +50% | No |

The game gives no visual warning about which mushrooms are dangerous.

**Antidote** — **St. John's Wort** reduces poison when consumed. Grows in spring, summer and autumn.

### Layer 2: Hunting

Raw meat gives **+13% poison** and low nutrition — it must be processed.

Minimum tools (hand-craftable, no scheme or building needed):
- **Wooden Spear** — 1 log
- **Stone Knife** — 5 sticks + 2 stones (needed to skin the animal after killing it)

**Weapon damage types**:
- **Slash** — best against small animals: knives, swords, axes
- **Pierce** — best against large animals: spears, picks, ranged weapons

**Animal behavior** (visible in Inspector Mode with the **Tracker** perk from the Hunting skill tree):

| Colour | Behaviour | Animals | Hunting difficulty |
|---|---|---|---|
| 🔴 Red | Aggressive — attack on sight | Wolf, Bear, Wisent, Boar | Avoid without preparation |
| 🟠 Orange | Defensive — attack if provoked | Fox, Lynx, Badger | Medium |
| 🟢 Green | Skittish — flee | Deer, Rabbit, Moose | Easy / Medium |

Boars charge in a straight line — sidestep to avoid. They yield 21 meat and 5 leather.

Hunting vendors can mark all spawn locations for a specific species on the map for a fee (bears: 5,000 coins).

### Layer 3: Processing

| Method | Requirement | Result |
|---|---|---|
| Campfire | Craftable from radial menu Q + torch to light | Removes poison, more nutritious |
| House fireplace | Built house | Same as campfire, indoors |
| Drying | Hunting Lodge I, drying rack | Alternative without salt |
| Salting | Hunting Lodge II + salt | Lasts much longer — ideal for winter |
| Kitchen | Building + production tech points | Complex recipes: soups, stews, bread |

**Food freshness by storage location:**

| Location | Loss per season |
|---|---|
| On the ground | -100% |
| Inventory | -50% |
| Regular chest | -25% |
| Food Storage | -12.5% |

## Water

- Drink directly from **rivers or lakes** — approach the water, crouch if needed, hold E.
- Ripe berries give +2 water — combined food and water source.
- **Waterskin** — allows carrying water. Crafted at the Sewing Hut.

---

# 3. Initial settlement

## Crafting basics

### Hand-craftable items
- **Wooden Spear** — 1 log
- **Stone Knife** — 5 sticks + 2 stones
- **Stone Sickle**

Firewood cannot be hand-crafted — it requires a Woodshed.

### Manual vs NPC production

**You:**
- Immediate — uses materials directly from your inventory
- Grants Production XP to your character

**NPC:**
- Autonomous while you do other things
- Speed and quality depend on the NPC's Production skill level
- Requires materials in the building's **Resource Storage**
- Requires the **correct tools in the building's chest** — does not use tools from your inventory

If the building chest has no tool, the NPC produces nothing — even if you have that tool on you.

### Tech points

Tech points accumulate by doing activities (building, crafting, farming, hunting). There are four independent trees: **Building, Survival, Farming** and **Production**.

- Buildings unlock automatically when you reach the required tech threshold — no additional cost.
- Schemes must be purchased with coins from the **Technology tab** once the threshold is met. They are not sold by merchants.

### Resource and mining

#### Metals

**Smelting (Forge in Smithy):**

| Bar | Resources | Sale price |
|---|---|---|
| Copper Bar | 2 Copper Ore | 28 |
| Tin Bar | 2 Tin Ore | 35 |
| Bronze Bar | 1 Copper Bar + 1 Tin Bar | 140 |
| Iron Bar | 2 Iron Ore | 90 |

Smelting is always worth it — 2 Copper Ore (7×2 = 14) → Copper Bar (28). 2 Tin Ore (8×2 = 16) → Tin Bar (35). Bronze Bar (140) from bars worth 63 combined — more than double. Sell bars, not ore.

#### Mining

| Ore | Sale price | How to obtain | Requirement |
|---|---|---|---|
| Copper Ore | 7 | Mine in caves with a pickaxe, or Excavation Shed (also produces Stone, Straw, Limestone and Clay) | Basic pickaxe |
| Tin Ore | 8 | Mine in caves with a pickaxe | Basic pickaxe |
| Iron Ore | 17 | Skauki mine (day 1) or Mine building at a cave entrance | Pickaxe / High Building tech |
| Salt | 7 | Mine in caves | Basic pickaxe |

Mine resources respawn every season.

Iron is commonly available at the Skauki mine from day 1; plan early smelting if you want faster tool progression.

#### Trees

| Tree | Logs when felled |
|---|---|
| Birch | 2 |
| Spruce | 3 |
| Maple | 4 |

- Natural trees regrow in **2 years (8 seasons)** if the stump is left. Remove the stump with a shovel and they never regrow.
- Planted trees grow in **1 year (4 seasons)** and need space around them to develop.
- Each felled tree has a **25% chance** of dropping a seedling. Also available from vendors (Oxbow: Markuslaw in Piastovia or Zywia in Ostoya).
- Small saplings you collect for sticks **do not grow** — they are different from plantable seedlings.

Build nothing too close to a stump — it may vanish instead of regrowing.

---

# 4. Scaling

## Crops

### Setup

1. Provide tools to the Farm Shed: Simple Bags/Bags for fertilising, Hoes for ploughing, Sickles/Scythes for harvesting.
2. Provide resources: **1 Fertiliser per field plot** per sowing season + 1 seed per plot.
3. Define crops in each field for each season.
4. Assign Farmers to the Farm Shed.

### Getting fertiliser

- Drop berries or mushrooms on the ground → they become Rot next season → 10 Rot = 1 Fertiliser at the Barn table. No buildings required.
- 2 Manure = 1 Fertiliser at the Barn.
- The Pigsty produces Manure automatically.
- Also available from Resource and Farming vendors.

### Field rules

- Maximum efficient size: **~50 plots**. Several 5×10 fields outperform a single 16×16 field.
- One farmer completes **25 plots** (harvest + fertilise + plough + sow) per day.
- Fields always align to **cardinal directions** — they cannot be rotated.
- Removing all scythes and sickles from the Resource Storage and Farm Shed chest prevents Farmers from harvesting — useful if you want to harvest manually for the Careful Farmer perk bonus.

### Recommended rotations

| Rotation | Cycle | Produces |
|---|---|---|
| Flax / Cabbage / Rye | Spring sow flax → summer harvest + sow cabbage → autumn harvest + sow rye → spring harvest | Linen for clothing, food, flour |
| Oat / Rye | Spring sow oat → autumn harvest + sow rye → spring harvest | Animal Feed ingredients |

### Crop calendar

| Crop | Spring | Summer | Autumn | Winter |
|---|---|---|---|---|
| Flax | Sow | Harvest | — | — |
| Onion | Sow | Harvest | — | — |
| Cabbage (Spring) | Sow | Harvest | — | — |
| Oat | Sow | Growing | Harvest | — |
| Beetroot | Sow | Growing | Harvest | — |
| Poppy | Sow | Growing | Harvest | — |
| Carrot (Spring) | Sow | Growing | Harvest | — |
| Wheat (Spring) | Sow | Growing | Harvest | — |
| Cabbage (Summer) | — | Sow | Harvest | — |
| Rye | Harvest | — | Sow | Growing |
| Wheat (Autumn) | Growing | Harvest | Sow | Growing |
| Carrot (Winter) | Growing | Harvest | — | Sow |

### Orchards

- Fruit trees take **5 seasons to grow**, first harvest the following summer, **full maturity at 12 seasons**.
- Hops mature in **1 season** — only useful for beer in the Tavern, not a priority early on.
- Orchards must be **planted manually** — Farmers only harvest them.

## Animals

| Building | Animal | Worker produces | Tool needed | Where to buy (Oxbow) |
|---|---|---|---|---|
| Pigsty | Pigs | Manure | — | Klonica |
| Henhouse | Chickens | Eggs + Feathers | — | Skauki |
| Goose House | Geese | Feathers + Eggs | — | Piastovia |
| Fold | Goats | Milk | Bucket | Ostoya |
| Fold | Sheep | Wool | Shearing Scissors | Ostoya |
| Cowshed | Cows | Milk | Bucket | Piastovia |
| Apiary | — | Honeycomb | — | Bees appear automatically |
| Donkey Shelter | Donkeys | Nothing | — | Skauki |
| Stable | Horses | Nothing | — | Piastovia |

Manure on the floor, eggs in nests and manual milking/shearing are **player-only bonus resources** — NPC workers cannot collect them.

### Feeding

- **Animal Feed** = Oat Grain + Rye Grain + Straw
- Feed is consumed **daily** — animals enter the unfed state as soon as the feeder runs empty, not at season change
- Unfed animals **do not starve**, but produce only **25%** and will not breed
- Breeding is evaluated **at season change** — each female has a 15% chance per adult male in the same building (20% for horses and donkeys)
- Feed is required for breeding, but whether having it only on the last day of the season is sufficient is unconfirmed.
- For breeding: one male + one female of the same species in the same building, fed, with a free space available

### Lifespan (average years)

| Chickens | Geese | Sheep | Goats | Pigs | Cows | Horses |
|---|---|---|---|---|---|---|
| 6.25 | 12.5 | 12.5 | 15 | 18.75 | 22.5 | 31.25 |

Animals can be injured by the building hammer — be careful when constructing nearby.

## Economy

### Pricing
- You sell at **50% of base value** and buy at **150% of base value**.
- Each level of the **Barter skill** shifts both prices 10% in your favour.
- All vendors pay the same — it does not matter who you sell to.
- Vendors **restock every season change** and their inventory **expands over time**.
- Item condition (durability) affects price.

### Making money early

- **Pike arbitrage:** buy Pike from a food vendor → roast at campfire → sell roasted fish meat back for a profit.
- Random containers along **roads and riverbanks** respawn each season.
- Sell copper ore, tin ore and salt directly without a Smithy.
- Hunt, roast the meat, sell it.

### What to craft for profit

Simple or Fine Hoods · Bronze Shearing Scissors · Horseshoes · Poisoned bronze or iron arrows · Wines, mead, beer

### Market Stall

- Daily income is **the same regardless of which item is sold** — cheap items sell in larger quantities, expensive items sell slowly, but the daily total is identical.
- The **worker's Diplomacy skill** determines how much is sold per day.
- Coins earned go to the **Resource Storage**, not the player's inventory.
- Requires a Resource Storage (and Food Storage if selling food) to function.

### Vendors by village (Oxbow)

| Village | Vendors |
|---|---|
| Piastovia | Herbs, Tools, Resources, Food, Clothing, Exotic Goods, Innkeeper |
| Klonica | Hunter, Craftsman, Herbalist, Salty Treats |
| Ostoya | Seamstress, Fisherman, Farmer |
| Skauki | Stable, Blacksmith, Cook |

---

# 5. Settlement management

## People

### Recruiting
Travellers sit around campfires near villages and can be recruited if you have enough Dynasty Reputation. Reputation is gained by completing quests.

Useful trick: recruit and immediately remove a low-skill traveller to remove them from the pool — a new one with random stats will replace them.

### Basic needs
Each villager consumes **30 food value and 30 water value per day**. NPCs are immune to all food effects — poison, temperature, quality and variety are irrelevant. Food is purely a number. They do not need clothing and change outfits automatically with the seasons.

### Mood
If Mood reaches **-100%**, the villager permanently leaves the settlement and the map.

Mood essentials (Mood drops rapidly if any of these are missing):
- Housing
- Food
- Water
- Firewood

Mood bonuses (not required, but improve Mood):
- Higher quality house (stone > wood > wattle)
- Insulated house
- Job matching the villager's highest skill
- House decorations (up to 20)
- Spouse and children

Does not affect Mood: work intensity, food quality or variety, distance between house and workplace, weather.

### Work and production
- Non-farmer workers are **productive even while walking** — a miner 1km from the mine is mining in the background.
- **Farmers are not** — if they are walking, they are not producing. Keep their houses and Farm Shed close to the fields.
- Better tools **do not increase production rate** — they only last longer. NPCs always use the **lowest quality tool first**.
- Animals and bandits do not attack villagers. Villagers only die of old age, starting from age 60.

### Skills by building

| Skill | Buildings |
|---|---|
| Extraction | Excavation Shed, Mine, Well, Woodshed |
| Hunting | Hunting Lodge |
| Farming | Apiary, Barn, Cowshed, Farm Shed, Fold, Goose House, Henhouse, Pigsty, Stable, Windmill |
| Diplomacy | Market Stall |
| Survival | Fishing Hut, Herbalist's Hut |
| Production | Builder's Hut, Kitchen, Sewing Hut, Smithy, Tavern, Workshop |

### NPC families
- A man and a woman sharing a house with less than a 20-year age gap will eventually marry and have children.
- Only **one man and one woman** can share a house, regardless of bed count — the other beds are for children.
- Mothers stop working from the **2nd trimester** until the child turns 2 (9 seasons total).
- The husband receives a **+50% productivity boost** (reaching 150%) during that period — Busy Dad buff.

Baby boom warning: pairing many villagers at once can cause simultaneous pregnancies and collapse your production. Pair them **one couple at a time**, staggered across seasons.

### Taxes
- Paid every **spring** in coins to the Castellan in the main village.
- **Year 1 is exempt** — taxes start in year 2.
- Failing to pay reduces Dynasty Reputation by 100 points.
- Reaching **-10,000 Dynasty Reputation** is game over.
- Taxes apply to all built structures regardless of location on the map.
- The King's opinion **directly affects the tax amount** — good opinion reduces it, bad opinion increases it.

## Demand Control

The **People's Demand Control** tab in Management lets you control what NPCs consume from storage. It covers three categories: Food (64 items), Water (36 items) and Wood (4 items).

**Wood consumption order (priority 1→4):** Firewood → Stick → Log → Plank

Disable everything by default, then enable only what you want NPCs to consume. Without explicit configuration, NPCs may burn construction logs and planks as fuel.

## Buildings and rules

- Buildings unlock automatically at the required tech threshold — no additional cost.
- Placed but unbuilt blueprints **already generate taxes**.
- Buildings without a completed foundation **do not pay taxes**.
- Buildings and furniture can be **moved** with the hammer in Move Mode at no additional resource cost.
- All Customise Game settings can be changed **at any time**, including in long-running saves.

### The 70m rule
- Farm workers lose efficiency if the Farm Shed is more than 70m from the field.
- Do not build within 70m of an animal spawn point. This includes roads, platforms and fences. Furniture and decorations do not block spawns.

---

# 6. External systems

## Combat and bandits

Bandits **do not attack your settlement** — they stay near their camps. Camps are random each 1–2 seasons, except for one **permanent camp in the northeast of the Oxbow** — bandits there respawn but loot does not.

Shields are equipped from the **torch slot** by holding **F** — not a secondary weapon slot. The most basic option is the Wooden Round Shield.

### Loot

There are three types of loot containers on the map, each behaving differently:

**Fixed containers** — chests inside specific abandoned buildings (such as those southeast of Piastovia). Contain valuable items including spears, poisoned arrows, coins and occasionally high-durability weapons. Many items are hidden — search thoroughly. Once looted, they never refill.

**Random containers** — barrels, broken carts, sacks and chests that appear along roads and riverbanks. These respawn at season change at randomised locations across the map, with new contents each time. The same spot may not respawn for 2–6 seasons.

**Lost Places and ruins** — abandoned structures scattered across the map, not marked on the map. May contain bandits or wolves. Bandits sometimes partially restock chests with lower-value items between visits.

**Village house chests** — contain valuable items and sometimes coins. Taking them without permission is theft and reduces Dynasty Reputation proportionally to the item's value.

## The King and the Herald

The King's opinion affects both your **taxes** and your **villagers' mood**. There are three King types — Good, Neutral and Bad — identifiable by his title. A Bad King with a good opinion of you **lowers** villager mood.

Ignoring Herald quests drops opinion to Neutral at most. **Failing** them can drop it further. You have **5 seasons** to complete a Challenge — speak to the Herald as early in the season as possible. The Herald can appear in any Tavern on the map, including ones you build. The probability of his appearance increases by **25% each season** he does not visit.

Reputation-locked progression:
- Village name: **Very Good** opinion + 10,000 coins
- Crest: **Excellent** opinion + 10,000 coins

---

# 7. Reference

## Quick reference

- Diagonal sprinting while overencumbered is faster than going straight.
- Tree stumps regrow in 8 seasons unless removed with a shovel.
- Inspector Mode (Alt) shows NPC names, ages and skill levels.
- Searching the **Knowledge tab** finds recipes and information in-game.
- Lost Places and ruins contain loot and bandits — not marked on the map.

## Gameplay settings

All settings are adjustable at any time, including in long-running saves. Season length changes apply from the next season onward.

| Setting | Normal | Hard |
|---|---|---|
| Length of Season (Days) | 3 | 3 |
| Taxes | 100% | 200% |
| Buildings Limit | 100% | 100% |
| Events | ✅ | ✅ |
| Remote Storage Access | ✅ | ☐ |
| Unlimited HP | ☐ | ☐ |
| Unlimited Stamina | ☐ | ☐ |
| Lack of Hunger | ☐ | ☐ |
| Lack of Thirst | ☐ | ☐ |
| Unlimited Carry Weight | ☐ | ☐ |
| Inhabitants – Food Needs | 100% | 200% |
| Inhabitants – Water Needs | 100% | 200% |
| Inhabitants – Wood Needs | 100% | 200% |
| Bandits – HP | 100% | 200% |
| Bandits – Damage | 100% | 200% |
| Animals – HP | 100% | 200% |
| Animals – Damage | 100% | 200% |
| Poisoning | ✅ | ✅ |
| Temperature | ✅ | ✅ |
| Fast Crafting | ☐ | ☐ |
| Fast Building | ☐ | ☐ |
| XP Gain Multiplier | 100% | 100% |
| Technology Gain Multiplier | 100% | 100% |
| Clothes and Armour Durability Loss | 100% | 100% |
| Tools and Weapons Durability Loss | 100% | 100% |
| Dynasty Reputation Gain Multiplier | 100% | 100% |
| Stop Dropped Items from Spoiling | ☐ | ☐ |
| Storage Interior | ✅ | ✅ |

On Hard, Remote Storage Access is disabled — the player must be within physical range of a storage building to access it. NPCs are unaffected.

## Technology

Tech points accumulate by doing activities. There are four independent trees — Building, Survival, Farming and Production — each unlocking buildings and schemes independently.

### Building tech

| Building | Tech points |
|---|---|
| Resource Storage I | 50 |
| Woodshed I | 100 |
| Simple House | 250 |
| Excavation Shed | 500 |
| Resource Storage II | 1,000 |
| House | 1,500 |
| Woodshed II | 2,500 |
| Mine | 5,000 |
| Builder's Hut | 7,500 |
| Resource Storage III | 10,000 |

### Survival tech

| Building | Tech points |
|---|---|
| Hunting Lodge I | 50 |
| Herbalist's Hut I | 250 |
| Fishing Hut I | 500 |
| Hunting Lodge II | 1,000 |
| Herbalist's Hut II | 1,500 |

### Production tech

| Tier | Tech points | Scheme costs |
|---|---|---|
| Copper (Smithy I) | 50 | Copper Knife (150), Copper Hammer (100), Copper Shovel (100). Others not listed |
| Bronze | 500 | Bronze Hammer (200), Bronze Shovel (200), Bronze Sickle (250), Bronze Shearing Scissors (200). Others not listed |
| Iron | 5,000 | All schemes not listed |

## Smithy

All Smithy recipes require purchasing a scheme from the Technology tab.

Best early profit: the Bronze Knife (1 stick + 1 bronze bar) provides an excellent material-to-value ratio and is a reliable early sell item.

### Forge — Smelting

| Bar | Resources | Sale price |
|---|---|---|
| Copper Bar | 2 Copper Ore | 28 |
| Tin Bar | 2 Tin Ore | 35 |
| Bronze Bar | 1 Copper Bar + 1 Tin Bar | 140 |
| Iron Bar | 2 Iron Ore | 90 |

### Anvil — Copper tools (50 Production tech)

| Item | Scheme | Resources | Sale price |
|---|---|---|---|
| Copper Axe | not listed | 1 log + 4 copper bars | 220 |
| Copper Knife | 150 | 1 stick + 2 copper bars | 110 |
| Copper Sickle | not listed | 1 log + 2 copper bars | 120 |
| Copper Hoe | not listed | 1 log + 2 copper bars | 110 |
| Copper Hammer | 100 | 2 copper bars + 1 log | 110 |
| Copper Shovel | 100 | 2 logs + 4 copper bars | 220 |

### Anvil — Bronze tools (500 Production tech)

| Item | Scheme | Resources | Sale price |
|---|---|---|---|
| Bronze Axe | not listed | 1 log + 2 bronze bars | 590 |
| Bronze Pickaxe | not listed | 1 log + 2 bronze bars | 590 |
| Bronze Knife | not listed | 1 stick + 1 bronze bar | 300 |
| Bronze Scythe | not listed | 1 stick + 1 log + 2 bronze bars | 590 |
| Bronze Hoe | not listed | 1 log + 2 bronze bars | 290 |
| Bronze Hammer | 200 | 1 bronze bar + 1 stick | 290 |
| Bronze Shovel | 200 | 1 log + 2 bronze bars | 590 |
| Bronze Sickle | 250 | 1 log + 1 bronze bar | 200 |
| Bronze Shearing Scissors (x2) | 200 | 1 bronze bar | 150 |

### Anvil — Iron tools (5,000 Production tech)

| Item | Scheme | Resources | Sale price |
|---|---|---|---|
| Iron Axe | not listed | 1 log + 4 iron bars | 880 |
| Iron Pickaxe | not listed | 1 log + 4 iron bars | 880 |
| Iron Knife | not listed | 1 stick + 2 iron bars | 440 |
| Iron Sickle | not listed | 1 log + 2 iron bars | 440 |
| Iron Hoe | not listed | 1 log + 2 iron bars | 440 |
| Iron Scythe | not listed | 1 stick + 1 log + 4 iron bars | 880 |
| Iron Hammer | not listed | 2 iron bars + 1 stick | 400 |
| Iron Shovel | not listed | 1 log + 2 iron bars | 800 |
| Iron Shearing Scissors | not listed | 1 iron bar | 210 |
| Iron Horseshoes | not listed | 2 iron bars | 440 |

The sale prices reflect base value only — material gathering time not included.

## Working clothes

A complete set reduces crafting time by **80%** at the corresponding workstations. A single piece provides no bonus — the full set is required.

| Set | Workstations |
|---|---|
| Blacksmith (Apron, Boots, Coif, Gloves, Trousers) | Anvil, Forge, Workbench (Smithy only) |
| Cook (Apron, Hat, Shoes, Trousers) | Oven, Cauldron, Stone Grate, Fireplace, Campfire |
| Seamster (Doublet, Hat, Hose, Shoes) | Spinning Wheel, Tailoring Table, Loom |

Unlocked in the Production tech tree. Crafted at the Sewing Hut or purchased from clothing vendors.

## Building sizes

Measurements in field plots. Mine and Fishing Hut have no fixed size — Mine can only be placed at cave mouths with ore deposits, Fishing Hut in water.

### Housing — construction materials

| House | Material | Sticks | Logs | Planks | Stone | Straw |
|---|---|---|---|---|---|---|
| Simple Small | Wattle | 66 | 25 | — | 10 | 32 |
| Simple Small | Wooden | — | 50 | 24 | 10 | — |
| Simple Small | Stone | — | 27 | 48 | 76 | — |
| Simple | Wattle | 80 | 32 | — | 12 | 48 |
| Simple | Wooden | — | 63 | 36 | 12 | — |
| Simple | Stone | — | 35 | 72 | 92 | — |
| House | Wattle | 106 | 34 | — | 14 | 60 |
| House | Wooden | — | 71 | 48 | 14 | — |
| House | Stone | — | 38 | 80 | 108 | — |

All houses include a Stone Campfire for cooking. Wattle variants require no planks — Wooden and Stone require a Woodshed.

### Housing — footprint

| Building | Size |
|---|---|
| Simple Small House | 5×5 |
| Simple House | 5×7 |
| House | 7×7 |

### Production and services

| Building | Size | Building | Size |
|---|---|---|---|
| Apiary | 3×4 | Market Stall | 3×3 |
| Barn | 5×6 | Pigsty | 4×4 |
| Builder's Hut | 3×4 | Resource Storage | 7×7 |
| Cowshed | 5×5 | Sewing Hut | 3×5 |
| Donkey Shelter | 5×5 | Smithy | 4×4 |
| Excavation Shed | 3×4 | Stable | 6×6 |
| Farm Shed | 3×3 | Tavern | 7×8 |
| Fold | 4×4 | Well | 3×3 |
| Food Storage | 5×5 | Windmill | 4×5 |
| Goose House | 3×4 | Woodshed | 4×4 |
| Henhouse | 3×4 | Workshop | 5×5 |
| Herbalist's Hut | 4×4 | Kitchen | 3×5 |
| Hunting Lodge | 4×5 | | |

## King titles

| Good Kings | Neutral Kings | Bad Kings |
|---|---|---|
| The Beloved | The Ambitious | The Aggressor |
| The Benevolent | The Bearded | The Bad |
| The Brave | The Coward | The Bloody |
| The Builder | The Great | The Cruel |
| The Caring | The Lazy | The Dangerous |
| The Fair | The Lion | The Greedy |
| The Generous | The Powerful | The Mad |
| The Merciful | The Strong | The Warlike |
| The Wise | | |

---

## Notes

This is a structural draft for review before any final migration to `README.md`.
