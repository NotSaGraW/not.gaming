---
id: run-setup-priorities
name: Run setup — planning depth matches information
category: strategy
affects: [population, food, efficiency]
version: v71
evidence: game-data
status: open
---

# Run setup — planning depth matches information

Principle (curator + cataloguer synthesis, sources below): **planning depth should match information.** At t=0 you know the least the run will ever know; plan deeply only what is frozen, sketch what is structural, leave the rest to the run. Overplanning is spending hours optimizing gradients the game deliberately flattened.

**Worth regenerating / choosing carefully — the two frozen variables:**

- **Race** — the only multiplicative production bonus above 1 ([[production-math]]) and the entire preference matrix ([[brawls]]); everything downstream inherits it.
- **Region** — area × moisture caps maximum population ([[population-thresholds]], community); climate is the one fulfillment the dev manual calls impossible to fix later (Ch12).

**Not worth perfecting — gradients the game flattened (game-data):**

- Coastline shape: "an ocean tile on the world map always gets you the same amount of fish, no matter how the coast line looks" (ROOMS).
- Food choice: all foods equally nutritious; preference affects satisfaction only.
- Pasture land: per-worker yield fertility-independent.
- Foundations: farms don't need them; build expensive rooms on good ones, farms elsewhere.
- Moisture: irrigation raises it (can exceed 100%, v71).
- Tech: refundable. City itself: **resettle** keeps levels + resources (v70) — cities are drafts.

**Planning tool = skeleton, not city:** reserve wide main roads (decorations retrofit into them, Ch12), species-district boundaries with entrance separation ([[brawls]]), and noise zones ([[overlays]]). Buildings get discovered by the run.

- depends-on: —
- see-also: [[production-math]], [[population-thresholds]], [[brawls]], [[food-harvest-cadence]]

**Source:** [[2026-07-06-gamedata-guide-notes]], [[2026-07-06-gamedata-race-preferences]], [[2026-06-15-patchnote-v71-reign-of-terror]], [[2025-12-04-patchnote-v70-riders-of-doom]]
