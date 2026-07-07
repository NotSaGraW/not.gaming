---
id: free-fetch
category: mechanic
affects: [logistics, efficiency]
version: v71
evidence: patch-note
status: open
---

# Free fetch & carry capacity (service logistics)

v71 relaxed the biggest layout constraint on services. Changes (v71 patch notes):

| Change | Detail |
|--------|--------|
| Free fetch on all services | Food stalls, markets, taverns, restaurants, hospitals, physician, janitor and bath houses no longer need warehouses directly adjacent — normal proximity is enough. |
| Carry capacity 4 → 7 | Max carry capacity raised for all jobs. |
| Restaurants | Cook slower, but higher carry capacity and free fetch. |
| Farmers auto-store | Farmers automatically store harvest and notify you if no storage is nearby. |
| Corpse burial | Every citizen can now bury corpses. |

Layout implication: pre-v71 guides that require warehouse-adjacent service blocks are
obsolete. Proximity still matters, but the adjacency requirement is gone — distance and
efficiency trade-offs should be re-measured in-game, not inherited.

- depends-on: —
- see-also: [[trade]], [[corpse-management]]

**Source:** [[2026-06-15-patchnote-v71-reign-of-terror]], [[2026-07-06-gamedata-guide-notes]]

## History

- **2026-07-06 (game-data, dev manual Ch13/Ch11):** the underlying rule generalizes — production rooms fetch inputs within a short radius at **zero production cost** (hover the consumption icon to see the radius); beyond it, hauling eats work time. Dev: "there is no need to shave off a tile from an already short route." Full storage/hauling picture on [[logistics-system]]; the math context on [[production-math]].
