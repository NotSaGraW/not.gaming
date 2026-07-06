---
id: slavery
name: Slavery (v71 rework)
category: mechanic
affects: [population, loyalty, trade]
version: v71
evidence: patch-note
status: open
---

# Slavery (v71 rework)

Reworked from the ground up in v71. Slaves are a special subject type whose fulfilment and happiness work almost identically to citizens' — but their base fulfillment is very low (enslavement removes freedom), which makes **law far more potent on slaves**. Dev (devlog): "you basically have to be a tyrant to own slaves."

Slaves are a fully tradable good — but what you import/export are **captives**; you must enslave captives to make them slaves. Captives are a separate pool; treatment affects chivalry/cruelty (small fulfillment effect; dev plans to tie it to diplomacy later).

Behavior rules (alpha-tester, Discord 2026-07-06): citizens never brawl with slaves; citizens brawl with citizens of other races; slaves brawl with slaves of other races → single-race slave pools never brawl. *(evidence: community, alpha-tester)*

Slave uprisings replace runaways (v71 announcement summary): unhappy slaves rebel rather than flee. Community observation: Amevians may be the most economical slaves — 150-year lifespan *(lifespan UI-verified 2026-07-06: species screen shows death age 150; see [[2026-07-06-test-species-screens]])*.

- depends-on: [[law-and-order]]
- see-also: —

**Source:** [[2026-06-15-patchnote-v71-reign-of-terror]], [[2026-06-15-devlog-v71-feature-breakdown]], [[2026-07-06-discord-qanda-governing-slaves-health-growth]], [[2026-07-06-discord-chat-conscripts-emissaries-crypts-food]], [[2026-07-06-gamedata-guide-notes]]

## History

- **2026-07-06 (game-data, dev manual Ch19):** slave differences enumerated — submission instead of happiness; can't commit crimes, no insanity, far fewer services, less furniture, no education/indoctrination, auto-assigned to mass graves/cannibals on death, can't join divisions, deaths never "wrongful", don't affect "others" fulfillment, **do not cause brawls** (confirms the community rule). **Submission < 80% risks revolts**; submission drops as slave share of population grows; raised by religion, nobles, decorations, soldier presence. Owning slaves worsens relations with rulers of the enslaved species.
