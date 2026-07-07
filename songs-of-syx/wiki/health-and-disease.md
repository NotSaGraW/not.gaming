---
id: health-and-disease
category: mechanic
affects: [health, population]
version: v71
evidence: game-data
status: open
---

# Health & disease

Dev manual, Ch23. Health is resistance to disease, **mainly decreased by population
size** — small cities can largely ignore it, big ones can't. Species and occupation also
affect it: some mining variants cut personal health massively (and mines are
accident-prone), so hospitals near mines help.

Diseases are **common** (regular, low lethality; higher health lowers affliction chance)
or **epidemics** (can destroy a city). **Epidemics only appear when overall health < 1** —
fully preventable with enough investment. Some common diseases also have epidemic variants.

Two different health jobs:

| Building | Role |
|----------|------|
| Physician | Raises the health *stat* only — does not cure the sick. |
| Hospital | Treats sick subjects: much shorter illness, far lower lethality. Fabric + opiates (behind tech) improve survival further (v71). |

**Wells, physicians and lavatories** are the strongest health raisers, but their effect is
computed from *actual usage*, not building count — poorly placed ones contribute nothing.
Bigger cities need health *technology* to stay above the epidemic threshold.

Unburied corpses are "very detrimental" — post-disaster corpse removal is a health
priority ([[corpse-management]]). Alcohol fulfillment slightly decreases health (Ch12) —
a fulfillment/health trade.

- depends-on: —
- see-also: [[corpse-management]], [[accidents-and-nurseries]], [[population-thresholds]]

**Source:** [[2026-07-06-gamedata-guide-notes]]
