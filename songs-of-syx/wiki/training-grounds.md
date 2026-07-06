---
id: training-grounds
name: Training Grounds (building)
category: building
affects: [military, efficiency]
version: v71
evidence: measured
status: verified
---

# Training Grounds (building)

Feeds the melee-training pool that gives divisions their biggest multipliers (see [[battle-equipment]]: +100% offence, +100% defence at full training).

Room properties (measured): recruits-limit slider exists per room and globally; training speed is a room stat with upgrades (0/2 tier observed); insulation tracked per room; **emits noise** (compact per-room aura, see [[overlays]]); subject to degradation like any room. Capacity is NOT fixed per room — it equals the dummy count (below); observed instance and conditions in [[2026-07-06-test-training-grounds]].

**Layout (measured, resolved):** capacity = **number of Training Dummies, +1 each**. Dummies are 2×2 and must be reachable ("Item must be reachable") — no edge-to-edge tiling; leave a 1×2 access gap. Efficient packing: 5×2 = 2 dummies = 2 soldiers → **~5 tiles per soldier** (matches the 125-tile / 24-capacity room ≈ 5.2). Foundation flooring adds +3.00%. Floor area itself does NOT drive capacity — a bigger empty room trains nobody.

- depends-on: —
- see-also: [[battle-equipment]], [[conscripts]], [[law-and-order]] (trained guards enforce law better)

**Source:** [[2026-07-06-test-training-grounds]], [[2026-07-06-test-conscripts-tooltips]], [[2026-07-06-test-training-ground-construction]]

## History

- **2026-07-06 (measured):** card created from curator's room readings.
- **2026-07-06 correction (measured):** capacity driver resolved by construction-mode test — it's dummy count (+1 each, 2×2, reachability-gapped), not floor area. Curator's earlier "5×2 per soldier" corrected to 5×2 per **2** soldiers (~5 tiles/soldier); reconciles with 125/24 panel arithmetic. Flag closed. Also measured: Foundation +3.00%.
