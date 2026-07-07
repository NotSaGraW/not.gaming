---
id: tech-tree
category: mechanic
affects: [admin, industry, trade]
version: v71
evidence: patch-note
status: open
---

# Tech tree (v71 remake)

Remade in v71: all techs **~50% cheaper**, common nodes removed, rooms with multiple
recipes cost more. New **consumption nodes** per recipe sit at the end of each branch —
upgrading them reduces input consumption (e.g. less grain per bread). Fully teched
consumption is what makes import-raw / export-refined the most profitable play ([[trade]]).

Education is the main tech engine now; tech limits have existed since v70.

- depends-on: [[admin-tech-points]]
- see-also: [[education]], [[trade]]

**Source:** [[2026-06-15-patchnote-v71-reign-of-terror]], [[2026-06-15-devlog-v71-feature-breakdown]], [[2025-12-04-patchnote-v70-riders-of-doom]], [[2026-07-06-gamedata-guide-notes]]

## History

- **2026-07-06 (game-data, dev manual Ch16):** research points **decay** (level-granted points don't); production eventually equals decay. Falling below required points weakens **all** techs and can make tech-dependent rooms unmaintainable. Labs consume clay (innovation), libraries leather (knowledge); both have large experience modifiers — researcher output compounds with headcount. Refunding freezes points temporarily. Tech production boosts are additive — see [[production-math]] for why that matters less than efficiency/degradation.
