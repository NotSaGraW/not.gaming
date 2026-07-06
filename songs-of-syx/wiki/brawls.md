---
id: brawls
name: Brawls (causes & prevention)
category: mechanic
affects: [loyalty, health, fulfillment]
version: v71
evidence: game-data
status: open
---

# Brawls (causes & prevention)

**Who brawls with whom** (alpha-tester, Discord 2026-07-06): citizens never brawl with slaves; citizens brawl with citizens of *other races*; slaves brawl with slaves of *other races*. → Single-race slave pools never brawl. *(evidence: community)*

**Trigger condition** (wiki-gg "Brawls", edited 2026-06-26): housing brawls occur between species with **<100% mutual preference** whose homes are close. Mechanism: an aggressor checks for other species within **10 tiles of their own front door**; if the target is also within **48 tiles of its own home**, a brawl may occur → different-species housing entrances **>58 tiles apart** (entrance-to-entrance) should produce zero brawls. Distances are tile distance (chess-king/Chebyshev — octagons, not circles). Courtyards can keep outsiders beyond the R=10 zone (courtyard = enclosed entrance yard: house doors open onto a walled interior space with one opening, not onto a public street, so other species have no path within 10 tiles of the doors; removes routine traffic, not every possible visit). Damage roll claimed: `rand(0,1) × 0.25 × Force(attacker) / ForceAbsorption(defender) > 0.4`. Housing brawls ≠ the "Brawls!" riot event. *(evidence: wiki-gg — distance/formula constants are code-level, not in data files; testable in-game but unverified)*

**Preference values are game-data and asymmetric** — full matrix in [[2026-07-06-gamedata-race-preferences]]. The wiki page's one falsifiable example (Dondorian→Human 1.0 vs Human→Dondorian 0.75) **matches the race files exactly**, which corroborates the page's credibility. Standouts: Tilapi like nobody (0 toward Human/Dondorian); Amevia dislike everyone (~0.10); Dondorian↔Argonosh and Garthimi↔most are ~0.01–0.02 pairs; Human is the most tolerant race (0.75 default, 0.2 only toward Tilapi).

**Prevention levers, v71 hotfix-confirmed:** guards separate citizens and slaves (0.71.40); children no longer brawl (0.71.41). *(game-data: hotfix notes)*

Death by brawl has a default happiness impact of 0.5 (vs 2 for murder/starvation) — `LEAVE_CAUSE.txt`. *(game-data)*

**Practical checklist:** single-race slave pools; check the preference matrix before mixing citizen races (a 0.75/1.0 pair is near-safe, a 0/0.02 pair is a fight club); keep different-species housing entrances >58 tiles apart or courtyard the approaches; station active-duty guards where races mix; stay ≥0.71.41.

- depends-on: [[law-and-order]]
- see-also: [[slavery]], [[battle-equipment]] (Force / Force Absorption stats feed the claimed damage roll)

**Source:** [[2026-07-06-gamedata-brawls-hotfixes]], [[2026-07-06-gamedata-race-preferences]], [[2026-07-06-wikigg-brawls]], [[2026-07-06-discord-qanda-governing-slaves-health-growth]]

## History

- **2026-07-06:** card created from Discord rules + hotfix notes; OTHER_RACES consumer was inference-flagged.
- **2026-07-06 (wiki-gg + game-data):** curator captured wiki.gg "Brawls" page. Its falsifiable claim (Dondorian/Human asymmetry) verified exactly against race files → inference flag resolved: OTHER_RACES is the brawl-relevant preference. Distance constants (10/48/58) and damage formula adopted as wiki-gg evidence, unverified (code-level). Full 8×8 preference matrix extracted.
