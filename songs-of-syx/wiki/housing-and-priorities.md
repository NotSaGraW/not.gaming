---
id: housing-and-priorities
category: mechanic
affects: [population, efficiency, fulfillment]
version: v71
evidence: game-data
status: open
---

# Housing choice & job priorities

The control system for who works and lives where (dev manual, Ch14). Subjects look for a
job first, then take the closest available house to their workplace (skipping forbidden
ones; too-far housing is never chosen — the housing overlay shows rooms with homeless
workers). You place jobs, not people; housing follows.

The workforce menu (hammer icon) has three priority sets in a fixed hierarchy —
**master > species > work groups**:

| Priority | Effect |
|----------|--------|
| Master | Which jobs get workers first; low-priority rooms lose workers first when labour is short. Keep food production and hospitals high. |
| Species | Which species works a job. 0 = hard ban, even if no one else is available. Routes each job to the species with the best aptitude. |
| Work groups | Tie-breaker between rooms of equal species priority, for zoning. Non-restrictive (won't ban others when no fitting species is available), slow to apply, and defeated by any lower species priority. |

Dev's worked example: warehouses are needed in both a mountain zone and an outside zone;
Dondorians have the highest carrying capacity, so their higher species priority pulls
them outside. Lower the Dondorian warehouse priority to tie the Cretonians' — then work
groups fill each zone's warehouses locally.

Because homes chase workplaces, **job zoning is housing zoning**: cluster a species' jobs
in one district and their houses cluster there too. That is the brawl control — only
housing proximity triggers brawls between species that dislike each other; they can share
a workplace safely ([[brawls]]).

- depends-on: —
- see-also: [[brawls]], [[logistics-system]] (high-carry species belong in warehouse jobs)

**Source:** [[2026-07-06-gamedata-guide-notes]]
