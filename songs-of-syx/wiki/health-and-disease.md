---
id: health-and-disease
name: Health & disease
category: mechanic
affects: [health, population]
version: v71
evidence: game-data
status: open
---

# Health & disease

Dev manual, Ch23:

- Health = resistance to disease; **mainly decreased by population size**. Small cities can mostly ignore it; big ones can't.
- **Epidemics only occur if overall health < 1** — they are entirely preventable with sufficient investment. Common diseases just happen; higher health lowers affliction chance. Some common diseases have epidemic variants.
- **Wells, physicians, and lavatories** are the most effective health raisers — but their effect is computed from **actual usage**, not building count. Poorly placed health buildings contribute nothing.
- **Physicians only raise the health stat; hospitals treat the sick** (shorter illness, much lower lethality; fabric + opiates behind tech significantly improve survival, per v71 patch notes). Different jobs.
- Unburied corpses are "very detrimental" — post-disaster corpse removal is a health priority (see [[corpse-management]]).
- Occupational health: some jobs (mining variants) massively reduce personal health — consider hospitals near mines (accident-prone, per ROOMS notes).
- Drinking (alcohol fulfillment) decreases health (Ch12) — a fulfillment/health trade.

Bigger cities need health *technology* to stay above the epidemic threshold.

- depends-on: —
- see-also: [[corpse-management]], [[accidents-and-nurseries]], [[population-thresholds]]

**Source:** [[2026-07-06-gamedata-guide-notes]]
