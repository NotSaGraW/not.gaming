---
id: free-fetch
name: Free fetch & carry capacity (service logistics)
category: mechanic
affects: [logistics, efficiency]
version: v71
evidence: patch-note
status: open
---

# Free fetch & carry capacity (service logistics)

v71 relaxed the biggest layout constraint on services: **all services now have "free fetch"** — food stalls, markets, taverns, restaurants, hospitals, physicians, janitors, bath houses no longer need warehouses directly adjacent; normal proximity is enough.

Related throughput changes: max carry capacity per job raised **4 → 7**; restaurants cook slower but carry more; farmers auto-store harvest (and warn if no storage nearby); every citizen can bury corpses.

**Implication for layout planning:** pre-v71 guides that demand warehouse-adjacent service blocks are obsolete; proximity still matters but the adjacency dogma is dead. Distance/efficiency trade-offs should be re-measured in-game, not inherited.

- depends-on: —
- see-also: [[trade]], [[corpse-management]]

**Source:** [[2026-06-15-patchnote-v71-reign-of-terror]], [[2026-07-06-gamedata-guide-notes]]

## History

- **2026-07-06 (game-data, dev manual Ch13/Ch11):** the underlying rule generalizes — production rooms fetch inputs within a short radius at **zero production cost** (hover the consumption icon to see the radius); beyond it, hauling eats work time. Dev: "there is no need to shave off a tile from an already short route." Full storage/hauling picture on [[logistics-system]]; the math context on [[production-math]].
