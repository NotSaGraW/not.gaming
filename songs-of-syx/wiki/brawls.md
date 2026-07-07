---
id: brawls
category: mechanic
affects: [loyalty, health, fulfillment]
version: v71
evidence: game-data
status: open
---

# Brawls (causes & prevention)

**Who brawls with whom** (alpha-tester, Discord 2026-07-06): citizens never brawl with
slaves; citizens brawl with citizens of *other races*; slaves brawl with slaves of *other
races* — so single-race slave pools never brawl. *(community.)*

**Trigger** (wiki-gg "Brawls", edited 2026-06-26): housing brawls occur between species with
**<100% mutual preference** whose homes are close. An aggressor checks for other species
within **10 tiles** of its own front door; if the target is also within **48 tiles** of its
own home, a brawl may occur — so different-species housing entrances **>58 tiles apart**
(entrance-to-entrance) should produce zero brawls. Distances are Chebyshev (chess-king;
octagons, not circles). Courtyards can keep outsiders beyond the 10-tile zone. Housing
brawls ≠ the "Brawls!" riot event.

Claimed damage roll (wiki-gg, code-level, unverified — testable in-game):

```
brawl if:  rand(0,1) × 0.25 × Force(attacker) / ForceAbsorption(defender) > 0.4
```

**Preference values are game-data and asymmetric** — full matrix in
[[2026-07-06-gamedata-race-preferences]]. The wiki page's one falsifiable example
(Dondorian→Human 1.0 vs Human→Dondorian 0.75) **matches the race files exactly**. Standouts:
Tilapi like nobody (0 toward Human/Dondorian); Amevia dislike everyone (~0.10);
Dondorian↔Argonosh and Garthimi↔most are ~0.01–0.02 pairs; Human is the most tolerant
(0.75 default, 0.2 only toward Tilapi).

**Prevention (v71 hotfix-confirmed):** guards separate citizens and slaves (0.71.40);
children no longer brawl (0.71.41). Death by brawl has a default happiness impact of 0.5
(vs 2 for murder/starvation) — `LEAVE_CAUSE.txt`. *(game-data.)*

**Checklist:** single-race slave pools; check the preference matrix before mixing citizen
races (a 0.75/1.0 pair is near-safe, a 0/0.02 pair is a fight club); keep different-species
housing entrances >58 tiles apart or courtyard the approaches; station active-duty guards
where races mix; stay ≥0.71.41.

- depends-on: [[law-and-order]]
- see-also: [[slavery]], [[battle-equipment]] (Force / Force Absorption stats feed the claimed damage roll)

**Source:** [[2026-07-06-gamedata-brawls-hotfixes]], [[2026-07-06-gamedata-race-preferences]], [[2026-07-06-wikigg-brawls]], [[2026-07-06-discord-qanda-governing-slaves-health-growth]]

## History

- **2026-07-06:** card created from Discord rules + hotfix notes; OTHER_RACES consumer was inference-flagged.
- **2026-07-06 (wiki-gg + game-data):** curator captured wiki.gg "Brawls" page. Its falsifiable claim (Dondorian/Human asymmetry) verified exactly against race files → inference flag resolved: OTHER_RACES is the brawl-relevant preference. Distance constants (10/48/58) and damage formula adopted as wiki-gg evidence, unverified (code-level). Full 8×8 preference matrix extracted.
- **2026-07-06 (game-data, dev manual):** Ch14 confirms the qualitative mechanism — "having them live close together can cause deadly brawls. **Only housing matters** for this, they can work in the same building without any issues." Ch19: slaves "do not cause brawls." Housing-only trigger now dev-stated + wiki-gg + community concordant; job zoning is the placement tool ([[housing-and-priorities]]). Distance constants remain the only unverified piece.
- **2026-07-06 (measured, codex wide pass):** the OTHER_RACES matrix is UI-corroborated categorically — species codex "Others" portraits tint green/red matching the file values sign-for-sign across 6 checked races ([[2026-07-06-test-species-codex-wide]]). Exact percentages still pending a hover check.
