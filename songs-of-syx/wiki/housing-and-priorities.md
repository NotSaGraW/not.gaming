---
id: housing-and-priorities
name: Housing choice & job priorities
category: mechanic
affects: [population, efficiency, fulfillment]
version: v71
evidence: game-data
status: open
---

# Housing choice & job priorities

The control system for who works and lives where (dev manual, Ch14):

**Jobs come first, homes second.** Subjects pick a job, then take **the closest available house to their workplace** (skipping forbidden ones; too-far housing is never chosen — the housing overlay shows rooms with homeless workers). You do not place people; you place jobs, and housing follows.

**Priority hierarchy: master > species > work groups.**

- *Master priority* — which rooms keep workers when labor is short; keep food production and hospitals high.
- *Species priority* — which species gets a job type; **0 is a hard ban** even if no one else is available; used to route species to their aptitudes.
- *Work groups* — tie-breakers between same-species-priority rooms, for zoning (cave district vs surface district); non-restrictive, slow to apply, and defeated by any species-priority mismatch.

Dev's worked example: to zone two districts sharing a species-priority job (warehouses), lower the dominant species' priority to tie the other's — then work groups decide per-room.

**Why this is the brawl tool:** since homes chase workplaces, *job zoning is housing zoning* — put species A's jobs in one district and their houses cluster there, which is what keeps different-species entrances apart ([[brawls]]: only housing proximity triggers brawls; shared workplaces are safe, dev-stated).

- depends-on: —
- see-also: [[brawls]], [[logistics-system]] (high-carry species belong in warehouse jobs)

**Source:** [[2026-07-06-gamedata-guide-notes]]
