---
id: training-grounds
name: Training Grounds (building)
category: building
affects: [military, efficiency]
version: v71
confidence: measured
---

# Training Grounds (building)

Feeds the melee-training pool that gives divisions their biggest multipliers (see [[battle-equipment]]: +100% offence, +100% defence at full training).

Measured (2026-07-06, ~286 pop): capacity 24 conscripts per room; 2 rooms → 48/48 pool. Room #001: 125 tiles for 24 capacity. Recruits-limit slider per room and global; Training Speed 110% observed (upgrades 0/2 available). Insulation tracked per room (100% observed); **emits noise** — keep away from housing/fulfillment rooms. Degrade 0%.

**Layout (measured, resolved):** capacity = **number of Training Dummies, +1 each**. Dummies are 2×2 and must be reachable ("Item must be reachable") — no edge-to-edge tiling; leave a 1×2 access gap. Efficient packing: 5×2 = 2 dummies = 2 soldiers → **~5 tiles per soldier** (matches the 125-tile / 24-capacity room ≈ 5.2). Foundation flooring adds +3.00%. Floor area itself does NOT drive capacity — a bigger empty room trains nobody.

- depends-on: —
- see-also: [[battle-equipment]], [[conscripts]], [[law-and-order]] (trained guards enforce law better)

**Source:** [[2026-07-06-test-training-grounds]], [[2026-07-06-test-conscripts-tooltips]]

## History

- **2026-07-06 (measured):** card created from curator's room readings.
