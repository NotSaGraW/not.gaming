---
id: education
name: Education (v71 overhaul)
category: mechanic
affects: [admin, population, loyalty]
version: v71
evidence: patch-note
status: open
---

# Education (v71 overhaul)

Two separate, non-interchangeable tracks:

- **Child education (schools):** unique to childhood. When enabled, children stay in "child" status until they finish the configured days of school. **Cannot be recouped later** — an adult can't retroactively get child education.
- **University education:** counted separately. Max education requires both.

Education limit is measured in days with diminishing returns. The highest limit is tech-gated. Education **multiplies innovation, knowledge, and admin output** based on education level and room quality — it's now mainly a technology engine. Indoctrination increases loyalty. Speed/limit upgrades cost admin.

- depends-on: [[natural-propagation]], [[admin-tech-points]]
- see-also: —

**Source:** [[2026-06-15-patchnote-v71-reign-of-terror]], [[2026-06-15-devlog-v71-feature-breakdown]], [[2026-07-06-gamedata-guide-notes]]

## History

- **2026-07-06 (game-data, dev manual Ch26):** the split quantified — max 100% education = **40% school (childhood-only) + 60% university**, confirming the two-track non-recoupable structure. Species have per-day learning rates (can be 0; schools use their own rate, not the species one). Effects are capital-wide per statistic. Education boosts research (including level-granted innovation) and diplomacy; indoctrination boosts happiness/loyalty.
