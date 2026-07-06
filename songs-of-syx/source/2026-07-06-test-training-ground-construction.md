# Source: in-game test — Training Ground construction UI

- **Origin:** test (curator's own experiment, construction mode screenshots, v71)
- **Date:** 2026-07-06
- **Conditions:** curator's city, ~286 pop; placing a new Training Ground
- **Immutable. Do not edit.**

---

Construction UI readings:

- Item: **Training Dummies**, footprint 2×2. Placement tooltip: "2x2 — 1 (item), 1.250 — **Capacity +1.00**".
- Room capacity is driven by dummy count: each dummy adds +1 conscript capacity.
- Dummies require reachability: placing without adjacent access space errors with **"Item must be reachable."** → dummies cannot be tiled edge-to-edge; a 1×2 access gap between dummies is needed.
- Consequence (curator's corrected rule): 5×2 fits 2 dummies (2×2 + 1×2 gap + 2×2) = 2 soldiers → ~5 tiles per soldier in efficient packing.
- This resolves the arithmetic tension in [[2026-07-06-test-training-grounds]]: 125-tile room / 24 capacity ≈ 5.2 tiles/soldier — matches dummy+gap packing, not the earlier 10-tiles/soldier reading (that figure was per-dummy-with-margin, wrong unit).
- Panel also shows: **Foundation +3.00%** (capacity bonus from foundation flooring), insulation options, shape tools; resource cost shown in wood.
