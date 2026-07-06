---
id: combat-mechanics
name: Combat mechanics (damage math)
category: mechanic
affects: [military]
version: v71
evidence: game-data
status: open
---

# Combat mechanics (damage math)

Dev manual, Ch30 — the math behind the [[battle-equipment]] stats:

- **To hit:** offence vs defence skill, random roll on the ratio. Stats scale linearly — double defence ≈ half incoming hits.
- **To block:** dexterity vs block, random on the ratio. At default values most attacks are blocked; even unequipped soldiers block somewhat. Blocked hits: damage / (1 + block armor).
- **Damage:** ≈ Damage / (Defense + 1) — each +1 typed defense halves-ish incoming damage of that type.
- **Force is a multiplier on everything:** a stronger soldier's weapon hits harder; force alone damages and can knock back light targets; force absorption reduces ALL incoming damage. Crucially, **defenses apply in sequence, not summed**: 3 force-def + 3 pierce-def → incoming pierce ×(1/4)×(1/4) = **1/16**, not 1/7. Layered defense compounds.
- **Formation stat:** +1 formation = +1 defence AND +1 block while cohesive. Cohesion requires soldiers on their spots and **ranks at least 5 deep**. Flanking strips formation bonuses even for soldiers facing the flanker; attacks from behind bypass defence and block almost entirely.
- **Charges:** damage scales with attacker speed × charge stat; nearly unevadable but blockable; exhausting (faster units lose more stamina).
- **Projectiles:** cannot be dodged, can be blocked (not from behind); dexterity is irrelevant against them.

Equipment economics (Ch27): per-level equipment gains diminish, but doubling offense *and* defense together is superlinear in effectiveness — mid-level balanced equipment beats maxing one stat. Equipment decays only while divisions are stationed on the world map.

Readings (cataloguer inference — labeled): the sequential-defense math is why [[battle-equipment]]'s Plate (+50% force absorption AND +50% force block AND +8 slash) is so much better than its listed numbers suggest, and why shields (+300% force block) pair multiplicatively with any armor.

- depends-on: [[battle-equipment]]
- see-also: [[conscripts]], [[brawls]] (the wiki-gg brawl damage formula uses the same Force / Force-Absorption pair)

**Source:** [[2026-07-06-gamedata-guide-notes]]
