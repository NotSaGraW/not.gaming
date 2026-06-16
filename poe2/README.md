# Path of Exile 2 — Personal SSF Reference

> League: **Runes of Aldur** · Patch: **0.5.2** · Character: **[Lossehelim (Disciple of Varashta)](https://poe.ninja/poe2/profile/SaGraW-0758/runesofaldur/character/Lossehelim)** · Last updated: June 2026

[![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc-sa/4.0/) [![Patch](https://img.shields.io/badge/patch-0.5.2-blue)](https://www.pathofexile.com/forum) [![Status](https://img.shields.io/badge/status-active-green)]()

---

## Contents

**Part I — Crafting**

- [Basics](#basics)
- [Item Level](#item-level)
- [Essences](#essences)
- [Omens](#omens)
- [Desecration](#desecration)
- [Fracturing Orbs](#fracturing-orbs)
- [Runeforging](#runeforging)
- [Crafting Workflow](#crafting-workflow)

**Part II — League Mechanics**

- [What Drops, Build Value and How to Use It](#what-drops-build-value-and-how-to-use-it)
- [Atlas Node Priority](#atlas-node-priority)

**Part III — Gear Priorities**

- [Current State](#current-state)
- [Priorities](#priorities)
- [Crafting by Slot](#crafting-by-slot)

> Items marked ⚠️ have limited live validation or come from a single source.

---

# Part I — Crafting

## Basics

A rare item has 6 mods maximum: 3 prefixes and 3 suffixes. Prefixes and suffixes are independent — a currency that targets prefixes never touches suffixes.

Each item can hold **1 crafted mod + 1 desecrated mod** maximum. Essences, Perfect Essences and Imbued Alloys all share the same crafted slot. Chaining is not possible.

At T15-16, use **Perfect** Exalted/Regal/Chaos when available — they floor at mod level 50, cutting the lowest garbage tiers from the pool.

Before any expensive craft: open **PoE2DB** (poe2db.tw), look up the base, check which tags the mods you need carry and at what ilvl T1 unlocks.

---

## Item Level

T15 maps with monster level 79-80 drop bases of the right ilvl directly. Key T1 gates:

| Mod | Slot | Min ilvl for T1 |
|---|---|---|
| % Movement Speed | Boots | 82 |
| Elemental Resistance | All | 82 (+41–45%) |
| Chaos Resistance | Body Armour | 81 |
| +# Minion Skill Levels | Amulet/Sceptre | 81 |
| +# Max Life / ES | Body/Belt/Jewellery | Varies — check PoE2DB |

An item at ilvl 75-80 has less mod competition than one at ilvl 82 — better odds of hitting what you want at the cost of locking out the absolute T1s.

---

## Essences

Guarantee a specific mod on craft. Limit: 1 Greater + 1 Perfect per item. Use on the hardest mod to get for each piece.

| Essence | Type | Guarantees | Use case |
|---|---|---|---|
| Essence of Enhancement | Prefix | % increased Global Armour/Evasion/ES | Body armour, boots |
| Essence of the Body | Prefix | +# Maximum Life | Belt, jewellery |
| Essence of Command | Prefix | % increased Damage to Allies | Main sceptre |

---

## Omens

Activate automatically with the next currency used.

**Rule:** Sinistral = Prefix · Dextral = Suffix

| Omen | Effect | When |
|---|---|---|
| Omen of Sinistral Exaltation | Exalt adds a Prefix only | Suffixes full, prefix slot open |
| Omen of Dextral Exaltation | Exalt adds a Suffix only | Prefixes full, suffix slot open |
| Omen of Sinistral Annulment | Annulment removes a Prefix | Good suffixes, bad prefix to remove |
| Omen of Dextral Annulment | Annulment removes a Suffix | Good prefixes, bad suffix to remove |
| Omen of Light | Annulment removes only the Desecrated mod | Retry Desecration without touching the rest |
| Omen of Abyssal Echoes | Rerolls all 3 Desecration options | None of the 3 options are useful |
| Omen of Sinistral Necromancy | Desecration reveal targets Prefixes only | Force desecrated mod onto a prefix |
| Omen of Dextral Necromancy | Desecration reveal targets Suffixes only | Force desecrated mod onto a suffix |

**Core combo:** Omen of Light + Annulment = remove the Desecrated mod without touching the rest of the item.

---

## Desecration

Abyssal Bones add a hidden mod revealed at an Abyssal Well inside Abyss encounters in maps. Maximum 1 Desecrated mod per item.

| Bone | Mod level floor | Use |
|---|---|---|
| Preserved Bone | None | Any slot, any ilvl |
| Ancient Bone | ≥ 40 | Mid to high quality mods |
| Gnawed Bone | Cap at 64 | Cannot reach T1 on mods gated above 64 |

**Retry loop:** Omen of Light + Annulment removes only the Desecrated mod, leaving the rest intact.

---

## Fracturing Orbs

Lock a mod permanently — nothing can remove it afterwards. Use when you have T1 on the hardest mod to get and want to build the rest on top without risking it. In SSF there is no recovery if a hard-won T1 gets wiped.

**Priority targets:** +Minion Skill Levels (suffix) on sceptre · T1 ES (prefix) on body armour.

---

## Runeforging

Runes socket into items without occupying the crafted slot. Materials — Runic Alloys and Verisium — come from Expedition. Apply after crafting is complete.

---

## Crafting Workflow

```
1. Base at the right ilvl (PoE2DB → highest T1 gate among the mods you need)
2. Essence → lock the hardest mod to get (one shot only per item)
3. Fill remaining slots with targeted Exalts
   → Sinistral/Dextral Exaltation to control which side gets the mod
   → If one side is full: Annulment Omen to open a slot first
4. Desecration
   → Necromancy Omen to target prefix or suffix side
   → Abyssal Echoes if none of the 3 options are useful
   → Omen of Light + Annulment to remove and retry
5. Divine → only when all mods are correct but values are low
6. Fracture → lock the highest-value mod before corrupting
7. Runes → after everything else; no interaction with the craft
8. Corruption → final layer, pure RNG
```

---

# Part II — League Mechanics

## What Drops, Build Value and How to Use It

In SSF, Atlas investment decisions are driven by what you need to craft, not by trade value.

| League | What it drops | Build value | How to use it |
|---|---|---|---|
| **Abyss** | Abyssal Bones, Exalted Orbs (~5 per clear), raw currency, Abyss Strongboxes | Bones are the primary Desecration material. Exalts are crafting consumables | Run Abyss tablets with the extra Abyss mod. Invest Atlas nodes starting from "From Below" → "Dark Depths" ⚠️ node names unverified for 0.5 reworked Atlas |
| **Ritual** | Fracturing Orbs, Omens, uniques | Fracturing Orbs lock T1 ES or +Minion Skill Levels. Omens of Annulment and Exaltation enable directed crafting. Post-0.5.2 Queen's Ritual Favours include 10 extra Omens | Farm 3 altars per map before advancing. Node "Bring Forth the Unseen" enables Summoning Circles — summoned bosses in the Ritual chain can drop multiple Fracturing Orbs per map |
| **Breach** | Hiveblood, rings with additional minion projectiles, Catalysts | Rings with the additional minion projectile mod are the single largest ranged upgrade available — Snipers, Arsonists and Frost Mages all benefit. ⚠️ ~1,458 Hiveblood = guaranteed ilvl 84 base via Wombgift in Genesis Tree | Complete Origins of the Fortress to unlock the Genesis Tree. Catalysts are only available through the Genesis Tree in 0.5 |
| **Delirium** | Divine Orbs, Perfect Exalted Orbs, Liquid Emotions, Megalomaniac Jewels | Divines reroll values on completed gear. Liquid Emotions are endgame jewel crafting material. Megalomaniac Jewels with minion damage notable combinations can be significant | Engage once the build sustains full fog coverage at T15 comfortably |
| **Expedition** | Runic Alloys, Verisium | Runeforging materials — add mods to items without consuming the crafted slot | Apply Runeforging after all other crafting is done |
| **Trial of Chaos** | Soul Core (Xipocado), raw currency | Soul Core of Dominion: 40% increased Damage with Command Skills on sceptre/wand/staff — applies directly to Deception and Brutality. Limited to 1 per character | Requires Inscribed Ultimatum ≥ level 65. Socket into the main sceptre immediately |

---

## Atlas Node Priority

```
ABYSS:    "From Below" → "Dark Depths" → left side → "Lord of the Pit"  ⚠️
          Produces: Abyssal Bones, Exalted Orbs, raw currency

RITUAL:   "Bring Forth the Unseen" (Summoning Circles)
          Produces: Fracturing Orbs, Omens, uniques

BREACH:   Genesis Tree first
          Produces: Catalysts, rings with additional minion projectiles

DELIRIUM: Once ready to sustain full fog coverage at T15
          Produces: Divines, Liquid Emotions, Megalomaniac Jewels
```

---

# Part III — Gear Priorities

## Current State

> [Lossehelim on poe.ninja](https://poe.ninja/poe2/profile/SaGraW-0758/runesofaldur/character/Lossehelim)

| Stat | Value | Status |
|---|---|---|
| ES | 6,609 | Sufficient for CI transition |
| Life | 1,736 | Emergency buffer — gone with CI |
| Chaos res | 39% | Solved by CI |
| Chaos max hit | 8.7k | Solved by CI |
| Elemental max hit | 31k | No issue |
| Block | 30% | From shield |
| Deception DPS | 38k | Rotation working |

---

## Priorities

**1. CI — transition now**

CI solves chaos resistance; it is not something you do after solving it. With CI, maximum life becomes 1 and the character becomes immune to chaos damage and bleeding. With 6,609 ES you already handle T15-16 — the defensive pool against physical and elemental hits does not change. Sacred Rituals references ES, not life, so it stays active and physical damage reduction remains the same.

What changes post-CI: chaos immune, bleeding immune, stun covered by the tree's "28% of maximum ES as additional Stun Threshold" (~1,850 at current ES). Ground DoT still stops ES recharge but without the 1,736 life buffer — move out faster. Two passive nodes lose almost all value: "5% of Maximum Life Converted to ES" gives 0.05 ES with life at 1, and "Immune to Bleeding while Archon Buff is active" is made redundant by CI itself.

**2. Breach rings with additional minion projectiles**

Scales all ranged minions simultaneously — Skeletal Snipers, Arsonists and Frost Mages all fire more projectiles, multiplying AoE and single-target output at once. Requires Breach Atlas investment and completing Origins of the Fortress to access the Genesis Tree.

**3. Main sceptre (WS1): % Increased Damage to Allies (prefix) + +Minion Skill Levels (suffix)**

Bases: Rattling Sceptre or Omen Sceptre. Target mod is +# to Level of all Minion Skills — it is a **suffix**. Use Omen of Dextral Exaltation to force Exalts into the suffix slot when hunting it. Use Essence of Command to lock % Increased Damage to Allies as the main prefix. % increased Spirit is the second most valuable prefix.

**4. Pending gem upgrades**

Skeletal Reaver: Minion Splash I → II · Skeletal Frost Mage: Multishot I → II

---

## Crafting by Slot

| Slot | Prefix target | Suffix target | Strategy |
|---|---|---|---|
| Body Armour | T1 ES (ilvl varies — check PoE2DB) | Post-CI: elemental res or minion mod | Fracture T1 ES. Essence of Enhancement to lock it. Chaos res has no value post-CI |
| Sceptre WS1 | % Increased Damage to Allies + % Spirit | +Minion Skill Levels | Fracture +Minion Skill Levels. Essence of Command for % ally damage prefix. Omen of Dextral Exaltation to push Exalts into the suffix slot |
| Rings | ES | Elemental res | Chaos res irrelevant post-CI. Breach rings with minion projectile mod override everything else here |
| Amulet | Spirit + Life | +Minion Skill Levels | +Minion Skill Levels is a suffix. Divine if values are low; do not replace if mods are correct |
| Boots | ES | Movement Speed T1 (ilvl 82) | Essence of Enhancement to lock ES. Regal hunting movespeed |

---

*Patch 0.5.2 — Runes of Aldur. Update on 0.6.*
