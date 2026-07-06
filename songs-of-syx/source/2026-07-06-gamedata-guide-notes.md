# Source: game-data — dev manual reading notes (text/wiki/GUIDE.txt + ROOMS.txt, v71 install)

- **Origin:** game-data (dev-written in-game manual; full text at `source/gamedata-v71/text/wiki/`, local-only). These notes: paraphrase + short quotes, committable.
- **Read in full by cataloguer:** 2026-07-06 (33 guide chapters + 6 room notes)
- **VERSION WARNING:** the manual is dev-stated but per-chapter version-suspect. Confirmed stale: **Ch10 "Getting more Population"** still describes breeder-era nurseries ("rooms which produce babies", "reproduction capability" beds) — contradicts v71 natural propagation; **Ch21 "Law"** describes per-species punishment assignment — v71 patch notes say punishments are now per-crime. Claims from those chapters need patch-note cross-check before use.

---

## Hard numbers

- Divisions hold **up to 200 soldiers** (Ch27). Guide-terminology "conscripts" = region-sourced troops, auto-training, auto-replenish, **max 50% training**; militia/professional soldiers are capital divisions.
- Education: max 100% = **40% school (childhood-only) + 60% university** (Ch26).
- Epidemics **only occur if overall health < 1** (Ch23). Physicians raise the health stat only; hospitals treat the sick.
- Slave submission **< 80% risks slave revolts** (Ch19).
- Farms: min 64 tiles (8x8) ≈ 1 worker → max 2,025 (45x45) ≈ 31 workers. Pastures: min 49 (7x7) → max 2,025, ~30 workers (ROOMS).
- Hunter room: a map supports **~15 hunters** before per-worker decline (ROOMS).
- Water: 1 pump = 100 pressure = 100 canal tiles; canal freshwater aura radius 15; culverts connect within 8 tiles (Ch32).
- Maintenance: degradation floors production speed at 25% (Ch15).
- Damage ≈ Damage/(Defense+1); force and typed defenses apply **in sequence** (3 force def + 3 pierce def → 1/16, not 1/7); formation stat +1 = +1 defence AND block while cohesive (needs ranks ≥5 depth); blocked damage → damage/(1+block armor); attacks from behind bypass defence/block; projectiles undodgeable, dexterity irrelevant to them; charge damage scales with speed × charge stat (Ch30).

## Mechanics worth cards

- **Production math (Ch13):** base rate × all multipliers × (1 + sum of additives). Multiplicative = degradation, efficiency, species; additive = tools, tech, nobles, education, experience. "The multiplicative elements are much more important." Production speed also scales input consumption (speed, not efficiency). Workload semantics differ: farms cap work/day (over-staffing ok), workshops cap slots (workload <100% = supply/storage problem). Short-range fetching is free (hover consumption icon for radius).
- **Logistics (Ch11):** warehouses (crates per resource, upgrades raise crate capacity, slow decay) / haulers (single-resource, compact) / loading+unloading stations (bulk long-haul, destination not specifiable) / pull-push orders (ignore work radius) / fetch + prioritize toggles. Logistic workers have boosted carry capacity; oddjobbers and regular employees low, unboostable.
- **Priorities & housing (Ch14):** master priority > species priority > work groups (tie-breaker, non-restrictive). Species priority 0 = hard ban. **Subjects pick jobs first, then the home closest to their workplace.** Brawls: only housing proximity matters; different species working in the same building is safe (dev-stated).
- **Tech upkeep (Ch16):** research points decay (level-granted points don't); negative points weaken ALL techs and can make rooms unmaintainable; labs consume clay, libraries leather; big experience modifier on researchers; early specialization >> diversification (species multiplier compounds).
- **Trade detail (Ch17):** tolls = flat, distance-based, hit cheap goods, reduced by roads in regions; tariffs = tax on last production step's added value, reduced by better formal relations (vassal/overlord/ally best). AI empires simulate real production; diversify imports/exports to keep prices sane.
- **Raiders (Ch28):** attracted by wealth = money + stored resources + slaves; military equipment does NOT count. Buy-off possible; killed raiders never respawn and pay bounty. Deterrence stat lowers raider interest.
- **Diplomacy (Ch20):** opinion + relative power + wealth drive AI behavior; Rivalry grows with your wealth, hits smaller factions hardest. Emissaries: flatter/sabotage/assassinate (failed attempts lower future success chance). Opinion levers: chivalry, technology, kinship, kin treatment, gifts (gift value scales with receiver's wealth).
- **Health (Ch23):** health mainly decreased by population size; unburied corpses "very detrimental". Wells, physicians, lavatories most effective — effect based on actual usage, not count.
- **Slavery (Ch19):** slaves use submission, not happiness; can't commit crimes, no insanity, fewer services, no education, auto mass-grave/cannibal assignment, can't join divisions, deaths never 'wrongful', **do not cause brawls**, don't count for "others" fulfillment. Diplomacy penalty with rulers of enslaved species.
- **Equipment (Ch27):** additional equipment levels have diminishing returns per level, but doubling offense+defense together is superlinear in effectiveness; equipment decays only while stationed on the world map; secondary weapons/shield assignable.
- **Fulfillment (Ch12):** fulfillment→population capacity is non-linear ("small amounts can be worth a lot of population at higher values"); services pick 2 unmet needs per visit; basic needs fixed-rate, service needs relative; furniture fulfillment ignores item value ("just a bit is very economical"); drinking reduces health; decoration/aura satisfaction adjusts slowly toward tile aura level.
- **Regions (Ch31):** rebellion only if majority-species loyalty < 0 sustained; gov points global, produced by nobles, spent on city-hall chain which generates workforce for region building.
- **Roundness/Squareness (Ch22):** determined by structural walls only; 5+ straight wall = squareness; 5+ diagonal arrangement = roundness; roundness overwrites squareness.
- **Food sources (Ch9 + ROOMS):** early-game order: fisheries → pastures → farms → refiner chains. Pastures: fertility sets animal density (worker count), NOT per-worker yield → viable on poor land, love fresh water (+output). Orchards: higher per-worker output and density than farms, slow start, alluvium best. Fish: salt water richer; fish tiles > water tiles for capacity; per-fisher yield constant. Mushrooms: caves, soil-agnostic. Cannibalism: corpses of prisoners/slaves/deranged, yields significant, unboostable.
- **Tourists (Ch18), Havens (Ch33):** tourists = money at scale (rating = service satisfaction + employees in attracting industries; ban disliked species). Havens grant unique, powerful immigrants per-region requirements.
