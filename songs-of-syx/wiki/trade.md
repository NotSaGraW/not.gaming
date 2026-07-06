---
id: trade
name: Trade & economy (v71 refactor)
category: mechanic
affects: [trade, logistics, industry]
version: v71
evidence: patch-note
status: open
---

# Trade & economy (v71 refactor)

Goal of the refactor: **every industry viable late game** (bread was the worst offender before). Mechanisms:

- Tariffs work both ways as a % of goods price; **tolls** favor cheap goods, tariff upgrades favor expensive goods.
- Every resource carries a **per-item logistics cost addition** (grain price raised to reflect transport). High-logistics goods (bread) trade dearer → exporting them earns more.
- Trade caps removed; AI factions hoard excess ("game theory" — they predict bad exports and under-invest), so local prices matter and each faction contributes to profit.
- Early trade is more expensive; late-game trade is situational and profitable.
- Import grain → export bread is now viable; own-grain → bread is the most profitable but needs the deepest tech (consumption nodes, see [[tech-tree]]).
- Emissary allocation "starts to matter a great deal" (see [[embassy-emissaries]]).
- UI: green/red arrows show work-value of exports vs imports; fewer-arrow imports against more-arrow exports = profit.
- Import depot capacity 250→600, export 200→500. Trade prices have more randomness to balance climate/race bonuses.

- depends-on: [[tech-tree]]
- see-also: [[embassy-emissaries]], [[free-fetch]]

**Source:** [[2026-06-15-patchnote-v71-reign-of-terror]], [[2026-06-15-devlog-v71-feature-breakdown]]
