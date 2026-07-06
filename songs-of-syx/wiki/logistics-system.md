---
id: logistics-system
name: Logistics system (storage, hauling, orders)
category: mechanic
affects: [logistics, efficiency]
version: v71
evidence: game-data
status: open
---

# Logistics system (storage, hauling, orders)

The moving parts (dev manual, Ch11):

- **Warehouses** — collect crated resources in work radius; each crate adds capacity, upgrades raise per-crate capacity; stored goods decay slower. Only goods in logistics rooms appear on the goods panel.
- **Haulers** — single-resource mini-warehouses, no walls needed; place where the good is consumed.
- **Loading/unloading stations** — bulk transport over long distances; more workers = faster prep, cart capacity fixed; destinations not specifiable (distance barely matters to throughput). Economical only at scale — "replacing a few warehouse workers with one of these is not economical."
- **Pull/push orders** — the glue between storages; **ignore work radius entirely**; pull limits prevent draining the source. This is how you feed districts without global hauling chaos.
- **Fetch / prioritize toggles** — fetch = may take from ground and room outputs; prioritize = may also take from other logistics buildings that don't have prioritize set.

**Worker classes:** logistics workers (employed by the room) have boosted, boostable carry capacity; oddjobbers (unemployed) haul opportunistically, low capacity, unboostable; regular employees haul only for their job, same low cap. Species differ in natural carry capacity — matters only for logistics workers ([[battle-equipment]]-style aptitude choice: put high-carry species in warehouses).

Together with [[free-fetch]] (services need proximity, not adjacency) and the zero-cost fetch radius on production rooms ([[production-math]]), the dev-stated layout doctrine is: **plan by radius and pull-order topology, not by adjacency.**

- depends-on: —
- see-also: [[free-fetch]], [[production-math]], [[trade]] (import/export depots are logistics rooms with a market attached)

**Source:** [[2026-07-06-gamedata-guide-notes]]
