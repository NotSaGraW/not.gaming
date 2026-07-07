---
id: battle-equipment
category: mechanic
affects: [military, industry]
version: v71
evidence: measured
status: open
---

# Battle equipment & training stats

Tooltip-measured values (v71, curator capture 2026-07-06). All bonuses per equipment
level/item as shown in the conscripts panel.

**Training (pool stats, from buildings):**

| Training | Building | Effects |
|----------|----------|---------|
| Melee | Training Grounds | Defence +100%, Offence +100%, Formation +1, Force +25%, Morale +4, Stamina +50% |
| Archery | Archery Range | Skill: Bow +1 |

**Armor & shield:**

| Item | Pro | Contra |
|------|-----|--------|
| Leather Armour | Force Absorption +25%, Slash Armour +3.5, Pierce Armour +1.25 | Speed −5% |
| Plate Armour | Force Absorption +50%, Force Block +50%, Slash Armour +8, Pierce Armour +2 | Offence −20%, Speed −25%, Weight +50% |
| Shield | Force Block +300% | — |

**Weapons & mounts:**

| Item | Pro | Contra |
|------|-----|--------|
| Warhammer | Force +50%, Pierce Damage +3 | — |
| Falcata | Offence +25%, Slash +1, Pierce +1 | — |
| Flanx | Offence +100%, Slash +6, Charge +1 | (two-handed) |
| Spear | Formation +5, Pierce +1 | unsuited for mounted combat |
| War-Beast | Charge +2, Offence +25%, Speed +2.5, Weight +500 | Formation −100%, Defence −50% |
| Bow | ranged (see below) | Speed −10%, wear −0.10/item/year |

**Bow projectile scaling** (From → To, inferred skill/training-dependent):

| Stat | From | To |
|------|------|----|
| Range | 119.4 | 197.4 tiles |
| Accuracy | 0.8 | 1.0 |
| Reload | 30 s | 3 s |
| Max angle | 50° | 75° |
| Force | 14 | 18 |
| Pierce damage | 4 | 12 |

Ammunition 40 per 24 h. *(The From→To axis is inferred to be skill-dependent — not stated
in the tooltip. Flag: confirm what drives it.)*

**Readings (cataloguer inference — NOT measured, do not inherit this card's evidence
tier):** melee training is the single largest multiplier in the panel (+100% offence AND
defence) — before optimizing equipment, fill Training Grounds. Spear (+5 formation) vs
War-Beast (−100% formation) are opposite archetypes: formation infantry vs shock cavalry,
matching v70's battle-engine design.

- depends-on: [[conscripts]]
- see-also: [[law-and-order]] (equipment/training also improve guard law enforcement, per patch notes)

**Source:** [[2026-07-06-test-conscripts-tooltips]]

## History

- **2026-07-06 (measured):** card created from tooltip capture.
- **2026-07-06 (game-data, dev manual Ch27/Ch30):** the formation stat's meaning defined — +1 formation = +1 defence AND block while cohesive (ranks ≥5); full damage math on [[combat-mechanics]]. Equipment: multiple items of one kind = quality levels with per-level diminishing returns, BUT doubling offense+defense together is superlinear; decay happens only while stationed on the world map; secondary weapon or shield assignable. Dev: training "extremely important... well-trained troops are significantly better and cost the same to equip and maintain" — corroborates this card's labeled inference about filling Training Grounds first.
