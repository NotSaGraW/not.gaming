---
id: embassy-emissaries
name: Emissaries & embassy points
category: mechanic
affects: [trade, admin]
version: v71
evidence: game-data
status: verified
---

# Emissaries & embassy points

**RESOLVED 2026-07-06 via game data — the tech exists.**

`EMBA0` in the ADMIN tech tree (v71 files): in-game name **"Embassy"** — "Unlocks a place that lets us improve relations with other factions and manipulate their courts" (`text/tech/ADMIN.txt`). 5 levels, costs Civic Knowledge (5 base, +5 per level), no prerequisites, each level `ROOM_EMBASSY>ADD: 0.2` → +20% embassy output per level, +100% at max. See [[2026-07-06-gamedata-embassy-tech]].

Original dispute, kept for the record:

- Claim A (community): there is an "embassy tech" (using Knowledge) that improves emissaries — author self-hedged: "or maybe I'm hallucinating v70."
- Claim B (community, different author): "Can't find anything" in v71.
- Adjacent facts: gifting cloth/jewelry/sithilon gives embassy points *(evidence: community)*; v71 patch notes add an **Emissary office for nobles** and state emissary allocation "starts to matter a great deal" *(patch-note)* — possibly what Claim A half-remembers, possibly a real tech node neither found.

- depends-on: [[trade]]
- see-also: [[tech-tree]]

**Source:** [[2026-07-06-discord-chat-conscripts-emissaries-crypts-food]], [[2026-06-15-patchnote-v71-reign-of-terror]], [[2026-07-06-gamedata-embassy-tech]]

## History

- **2026-07-06 (game-data):** dispute resolved by reading `tech/ADMIN.txt` from the v71 install. Claim A confirmed (tech exists, costs Knowledge); Claim B's "can't find anything" explained — it sits in the ADMIN tree. Status disputed → verified; evidence → game-data. Races with embassy references in init files: Cretonian, Garthimi, Human, Amevia, Tilapi — unexplored, possible race-specific embassy interactions.
- **2026-07-06 (game-data, dev manual Ch20):** emissary actions are flatter / sabotage / assassinate — flattery and sabotage move opinion; assassination is a per-day attempt chance, and failures lower future success odds. Opinion levers beyond emissaries: chivalry, technology, kinship, kin treatment, gifts (gift value scales with the receiver's wealth). Original Discord question ("get more out of my emissaries") thus has three answers: the Embassy tech, gifts (cloth/jewelry/sithilon), and targeting rulers where kinship multiplies.
