---
id: raiders
category: mechanic
affects: [military, trade, loyalty]
version: v71
evidence: game-data
status: open
---

# Raiders

Raiders are drawn by your capital's **wealth** (dev manual, Ch28):

- Wealth = **money + stored resources + slaves**. Military equipment does **not** count.
- Wealth, modified by your **defenses and deterrence**, determines which raiders consider
  raiding you. Investing in deterrence significantly lowers both the *number* and *strength*
  of raiders you face.
- When a raider decides to raid, you are offered a **buy-off** to avoid the fight; the more
  interested raiders there are, the more frequent the demands.
- Refuse → fight. Raiders spawn outside your territory (never in allied regions), target the
  **weakest point** in your defenses, and siege cities; fortifications and garrisons buy time
  for your armies. **Killing a raider is permanent** (no respawn) and pays a bounty.

## Raid menu (measured — [[2026-07-08-test-raider-panel]])

Header fields: Defence, Attack Route (e.g. "Surprise!"), Raid Security, Potential Ransom.
Per raider: name, status (In Hiding / At Large / Distant / R.I.P.), a wealth figure, Power;
selecting one shows Soldiers, Power, Ransom, Raids. A raider below the strength to attack
shows "does not have the strength to attack us currently and will leave us alone for now".

In the captured panel the list was ordered by the wealth figure ascending, with lower-wealth
raiders "In Hiding", a middle band "At Large!", and the highest "Distant".

## Not yet verified
Whether the per-raider "wealth" figure is the activation threshold, and how the raider
"Power" number compares to your "Defence" — not confirmed; measure before relying on it.

- depends-on: —
- see-also: [[population-thresholds]] (wealth/raider gate), [[conscripts]], [[law-and-order]]

**Source:** [[2026-07-08-test-raider-panel]], dev manual Ch28
