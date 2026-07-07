# test — food supply, surplus-yet-flat (Tilapi run, ~950 pop) — 2026-07-07

Curator screenshots (local, `Videos/Captures`): `Songs of Syx 07_07_2026 23_44_09`,
`23_45_50`, `23_45_53`, `23_45_56`.

## Food panel
| Field | Value |
|-------|-------|
| Production Rate | +595.90 |
| Consumption Rate | −412.80 |
| Net | +183.10 / day |
| Stored | 885 |
| Food Days | 2.000 |
| Population | ~954–967 |

Per-food, stored / production per day:

| Food | Stored | Prod/day |
|------|--------|----------|
| Meat | 734 | +507.11 |
| Egg | 2 | +49.33 |
| Fruit | 29 | +27.71 |
| Fish | 120 | +11.76 |
| Bread / Mushroom / Ration / Veg | 0 | 0 |

## Decay tooltips (all foods observed with 0 in warehouses)
| Food | Decay /yr | Decay stored | Net/day | Warehoused |
|------|-----------|--------------|---------|------------|
| Fish | −100% | −50% | −5.24 | 0/300 |
| Fruit | −50% | −25% | −10.29 | 0/540 |
| Egg | −10% | −5% | +3.33 | 0/380 |

Fish tooltip: "Must be eaten or processed quickly, else it will spoil." Egg tooltip:
"highly nutritious sustenance with a long shelf life."
Meat DEGRADE_RATE 0.75 (`init/resource/MEAT.txt`) — not screenshotted; implies ~−75%/yr.

## Follow-up (00:00–00:01, after removing some trades)
- A single **Auroch Pasture output storage held 1.81K meat** (`Songs of Syx 08_07_2026 00_01_54`) — food produced but not hauled to warehouses/stalls; confirms "trapped at source", not merely low production.
- Raiders panel (`00_00_23`): Defence 53, Attack Route "Surprise!", Potential Ransom **527K**. Raiders listed with wealth thresholds 180K→567K and Power 5→457; "At Large" from Ordu Mad Eye (270K/53) up to Henry the Outlaw (511K/384). Confirms [[population-thresholds]]: raider activity/strength scales with wealth (money + stored resources + slaves), so the hoarded food/materials inflate the raider threat while Defence is only 53.

## Finding
Production exceeds consumption by +183/day, yet Food Days is flat at 2.0. The surplus is
lost to **decay**: zero food is in warehouses (warehouses reduce spoilage), so everything
decays at the raw rate at its source. Meat (734 stored, fast-decay) decaying ≈25%/day ≈
183/day ≈ the whole net surplus. Not a bug. Observed relationship: the tooltip "stored"
decay ≈ 50 × the file DEGRADE_RATE for un-warehoused goods (fish 1.0→50%, fruit 0.5→25%,
egg 0.1→5%).
