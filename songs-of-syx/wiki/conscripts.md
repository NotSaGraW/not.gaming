---
id: conscripts
category: mechanic
affects: [military]
version: v71
evidence: community
status: open
---

# Conscripts & army size (v70/v71)

Community claim (#chat-and-discussions, 2026-07-06): conscripts can be set to **70%
training**; conscript-spam is "less viable now that armies are smaller", but smaller armies
make **equipping much easier**. The army-size reduction is a v70/v71-era change — pre-v70
mass-conscript guides are stale.

Context: v70 remade the battle engine (cavalry, spears, formation defence, morale emphasis)
*(patch-note)*; v71 armies can only transfer divisions on the same tile *(patch-note)*.

**Flag:** "armies are smaller" needs a primary source — not found in v70/v71 patch notes as
written; likely a balance change or emergent from training/equipment costs. Verify before
relying on it.

- depends-on: —
- see-also: [[law-and-order]] (guards are drawn from trained troops)

**Source:** [[2026-07-06-discord-chat-conscripts-emissaries-crypts-food]], [[2025-12-04-patchnote-v70-riders-of-doom]], [[2026-06-15-patchnote-v71-reign-of-terror]], [[2026-07-06-test-conscripts-panel]]

## History

- **2026-07-06 (measured, v71, ~286 pop):** division size is 50; conscript cap = divisions × 50 (5 divisions → 18/250 pool). Training confirmed as a freely settable % slider, per-equipment sliders independent — mechanism behind the "70% training" tip verified. Pre-v70 division sizes unknown; "armies are smaller" flag stays open but curator-deprioritized (noise at current scale).
- **2026-07-06 correction (measured, tooltips):** the previous entry over-claimed. The division sliders set *targets*; the underlying pools are building-fed: melee training from Training Grounds (48/48 observed), archery from Archery Ranges, equipment from stockpiles. "Soldiers" = ready to deploy (18); "Recruits" (30) = currently training to join a division. Sent-out divisions must be supplied via army depots (8 days of health supplies mandatory from warehouses; no depot → rout risk). Stat values now on [[battle-equipment]].
- **2026-07-06 (measured):** Active Duty tooltip verbatim: division soldiers "become guards who actively protects your city against crime, and instills order and law" — confirms the guard mechanism described in [[law-and-order]].
- **2026-07-06 (game-data, dev manual Ch27):** divisions hold **up to 200 soldiers** — the measured "division size 50" was the curator's setting, not a cap. **Terminology flag:** the manual's "conscripts" are region-sourced troops (auto-train, auto-replenish, **max 50% training**, "fully equipping these is often wasteful"), distinct from capital divisions (militia/professional). The Discord "set them to 70% training" tip therefore refers to capital divisions or predates a change — reconcile in-game. Equipment: per-level diminishing returns, decays only while stationed on the world map. See [[combat-mechanics]] for the stat math.
