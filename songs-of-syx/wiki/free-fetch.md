---
id: free-fetch
name: Free fetch & carry capacity (service logistics)
category: mechanic
affects: [logistics, efficiency]
version: v71
confidence: patch-note
---

# Free fetch & carry capacity (service logistics)

v71 relaxed the biggest layout constraint on services: **all services now have "free fetch"** — food stalls, markets, taverns, restaurants, hospitals, physicians, janitors, bath houses no longer need warehouses directly adjacent; normal proximity is enough.

Related throughput changes: max carry capacity per job raised **4 → 7**; restaurants cook slower but carry more; farmers auto-store harvest (and warn if no storage nearby); every citizen can bury corpses.

**Implication for layout planning:** pre-v71 guides that demand warehouse-adjacent service blocks are obsolete; proximity still matters but the adjacency dogma is dead. Distance/efficiency trade-offs should be re-measured in-game, not inherited.

- depends-on: —
- see-also: [[trade]], [[corpse-management]]

**Source:** [[2026-06-15-patchnote-v71-reign-of-terror]]
