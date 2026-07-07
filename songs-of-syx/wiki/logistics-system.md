---
id: logistics-system
category: mechanic
affects: [logistics, efficiency]
version: v71
evidence: game-data
status: open
---

# Logistics system (storage, hauling, orders)

The moving parts (dev manual, Ch11). Only goods stored in logistics buildings/rooms
appear on the goods panel.

| Element | Behaviour |
|---------|-----------|
| Warehouse | Collects crated resources in its work radius; each crate adds capacity, upgrades raise per-crate capacity; stored goods decay slower. Can use pull orders. |
| Hauler | Single-resource mini-warehouse, no walls needed; place where the good is consumed. Can use pull orders. |
| Loading / unloading station | Bulk transport over long distance; more workers = faster prep, cart capacity is fixed. Destination not specifiable (distance barely affects throughput). Economical only at scale — "not economical" to replace a few warehouse workers. |
| Pull / push orders | Redistribute between storages; **ignore work radius entirely**; a pull limit leaves a set amount in the source. |
| Fetch / prioritize toggles | Fetch = take from the ground and room outputs; prioritize = also take from other logistics rooms that don't have prioritize set. |

Worker classes:

| Class | Carrying capacity |
|-------|-------------------|
| Logistics worker (employed by the room) | High, boostable; works only for its room |
| Oddjobber (unemployed) | Low, not boostable; hauls opportunistically anywhere |
| Other employee | Low, not boostable; hauls only for its own job |

Species differ in natural carrying capacity, which matters only for logistics workers —
so put high-carry species (Dondorian > Cretonian > Human) in warehouse jobs.

With [[free-fetch]] (services need proximity, not adjacency) and the zero-cost fetch
radius on production rooms ([[production-math]]), the layout takeaway is to plan by radius
and pull-order topology rather than adjacency — a synthesis of the above, not a single
dev quote.

- depends-on: —
- see-also: [[free-fetch]], [[production-math]], [[trade]] (import/export depots are logistics rooms with a market attached)

**Source:** [[2026-07-06-gamedata-guide-notes]]
