---
id: combat-mechanics
category: mechanic
affects: [military]
version: v71
evidence: game-data
status: open
---

# Combat mechanics (damage math)

Dev manual, Ch30 — the math behind the [[battle-equipment]] stats. Stats scale roughly
linearly: doubled defence ≈ half the incoming hits, doubled offence the opposite until
hits are guaranteed.

| Step | Rule |
|------|------|
| To hit | Offence vs defence skill, random on the ratio. |
| To block | Dexterity vs block, random on the ratio. At default values most attacks are blocked; even unequipped soldiers block somewhat. Blocked damage = damage / (1 + block armor). |
| Damage | ≈ Damage / (Defence + 1) — each +1 typed defence roughly halves incoming damage of that type. |
| Force | Multiplies all other damage types (a stronger soldier hits harder); deals damage alone and knocks back light targets; force absorption reduces all incoming damage. |
| Formation | +1 formation = +1 defence and +1 block while cohesive. Cohesion needs soldiers on their spots and ranks ≥5 deep. Flanking strips it — even for a soldier facing the flanker. |
| Charges | Damage × attacker speed × charge stat; hard to evade, still blockable; very exhausting (faster units lose more stamina). |
| Projectiles | Cannot be dodged; can be blocked (not from behind); dexterity is irrelevant against them. |

**Defences apply in sequence, not summed** — layered defence compounds:

```
damage        = incoming / (Defence + 1)
blocked       = incoming / (1 + block armor)
3 force-def + 3 pierce-def:  incoming × (1/4) × (1/4) = 1/16   (not 1/7)
```

Attacks from behind almost always bypass defence and block.

Equipment economics (Ch27): per-level gains diminish, but doubling offence *and* defence
together is superlinear — mid-level balanced equipment beats maxing one stat. Equipment
decays only while divisions are stationed on the world map.

Readings (cataloguer inference — labeled): the sequential-defence math is why
[[battle-equipment]]'s Plate (+50% force absorption, +50% force block, +8 slash)
outperforms its listed numbers, and why shields (+300% force block) pair multiplicatively
with any armor.

- depends-on: [[battle-equipment]]
- see-also: [[conscripts]], [[brawls]] (the wiki-gg brawl damage formula uses the same Force / Force-Absorption pair)

**Source:** [[2026-07-06-gamedata-guide-notes]]
