# index

Catalog of all cards. Read this first to locate entries. Rebuildable from the
cards — not authoritative.

## Entries

### mechanic
- [[natural-propagation]] — population, food, fulfillment — v71 children/family system; pregnant subjects stop working; Garthimi breeder exception
- [[law-and-order]] — loyalty, fulfillment — v71 rework: trade happiness for loyalty; effects multiplied by guard/coverage infrastructure, exponential returns
- [[slavery]] — population, loyalty, trade — v71 rework: slaves ≈ citizens with low base fulfillment; captives tradable; single-race slave pools never brawl
- [[education]] — admin, population, loyalty — v71: child education (schools) and university are separate, non-recoupable tracks; multiplies tech output
- [[admin-tech-points]] — admin, industry — admin repurposed as tech point producer; three point types: administration, innovation, knowledge
- [[tech-tree]] — admin, industry, trade — v71 remake: ~50% cheaper, no common nodes, per-recipe consumption nodes
- [[trade]] — trade, logistics, industry — v71 refactor: two-way tariffs, tolls, per-item logistics cost, no trade caps; every industry viable late
- [[free-fetch]] — logistics, efficiency — all services free-fetch; carry capacity 4→7; warehouse-adjacency requirement gone
- [[accidents-and-nurseries]] — health, population, fulfillment — accidents off <150 employees, exponential later; global nursery; community says skip early
- [[corpse-management]] — health, fulfillment, logistics — corpse removal equal for health; graves add cheap fulfillment; crypt distance penalty UNVERIFIED (test)
- [[governing-points]] — admin, population — start 5, +20/governor, +40/promotion; regions can't build without them; Squeeze replaces tax rate
- [[embassy-emissaries]] — trade, admin — RESOLVED: embassy tech EMBA0 exists (ADMIN tree, 5 lvls, Knowledge, +20%/lvl from game data)
- [[conscripts]] — military — 70% training setting; division size 50 (measured); army-depot supply chain; "armies are smaller" needs primary source
- [[raiders]] — military, trade — attracted by wealth (money + stored resources + slaves); deterrence lowers count/strength; killing permanent; raid-menu fields (measured)
- [[brawls]] — loyalty, health, fulfillment — who brawls with whom; guards separate races (0.71.40 hotfix); per-pair race friction values in race files
- [[production-math]] — industry, efficiency, logistics — the formula: multipliers (dominant: degradation/efficiency/species) vs additives (tools/tech/education); specialize early
- [[logistics-system]] — logistics, efficiency — warehouses/haulers/stations/pull-push orders; plan by radius and orders, not adjacency
- [[combat-mechanics]] — military — damage math: sequential defenses compound (1/16 not 1/7); formation +1 = +1 def/block at ranks ≥5; flanking strips it
- [[housing-and-priorities]] — population, efficiency, fulfillment — jobs first, closest home second; master > species > work-group priorities; job zoning IS housing zoning
- [[health-and-disease]] — health, population — epidemics only below health 1; wells/physicians/lavatories by actual usage; hospitals treat, physicians don't
- [[overlays]] — efficiency, logistics, health, fulfillment — the in-game overlay instruments; placement claims are judged by overlay, never by screenshot
- [[water-and-irrigation]] — food, efficiency, health — pumps on groundwater only, 100 pressure = 100 canal tiles; irrigation cost scales with distance → moisture only conditionally fixable
- [[battle-equipment]] — military, industry — measured tooltip stats: training multipliers, armor/weapon/mount trade-offs, bow scaling table
- [[species-aptitudes]] — industry, fulfillment, population — the two-channel model: PREFERRED.WORK (preference/fulfillment) vs BOOST.ROOM_*>MUL (production multiplier); both key on species not status

### strategy
- [[population-thresholds]] — population, military, health, admin — the gates: 150 (accidents), 200 (raiders), ~300 (hunting cap), 1500 (promotions)
- [[food-harvest-cadence]] — food, population — harvest cadence over food type: daily harvests self-buffer, annual harvests starve you
- [[food-supply-diagnosis]] — food, logistics, population — days-of-food flat despite a surplus = decay of un-warehoused fast-decay food; fix with rations + warehouse reserve (measured)
- [[dondorian-settlement]] — food, population — mountain-on-ocean fishmax; cold pastures pointless; tyrant Dondorians dev-flagged non-viable
- [[run-setup-priorities]] — population, food, efficiency — plan deeply only race + region (frozen); the game flattened most other setup gradients; planning tool reserves skeletons

### species
- [[human]] — playable; education ×1.5, knowledge ×1.25; temperate/open; immigration ×1.5
- [[cretonian]] — playable; farm/orchard ×1.25; warm/open; growth 0.10, submission ×1.25
- [[dondorian]] — playable; workshop ×1.2, jewelry/smithy ×1.25; cold mountains; immigration ×25, reproduction ×0
- [[garthimi]] — playable; mine ×1.25, mason ×1.3, Pasture-Balti ×3.0; hot mountains; bred via Breeder room
- [[tilapi]] — playable; orchard/woodcutter ×1.4, bow ×1.5; forest; mining −10 (barred)
- [[amevia]] — playable; fishery ×1.25; wet/ocean; no WORK or OTHER_RACES block in file
- [[cantor]] — non-playable (haven); mine/refiner/workshop/woodcutter ×2.0; no climate; immigration ×0
- [[argonosh]] — non-playable (haven); barracks/archery ×1, other rooms ×0.1; immigration ×0

### building
- [[training-grounds]] — military, efficiency — capacity = training dummies (+1 each, 2×2, need access gap; ~5 tiles/soldier, measured); emits noise
- [[pastures]] — food, industry, efficiency — output formula measured; adult-fraction multiplier dominates young herds (~0.10 floor); 2-missed-days kills livestock; headroom map: faction/tech/nobles
- [[carpenter]] — producing-building card: 5 recipes (furniture/spear/warhammer/shield), room factors, per-species output×preference slice
- [[buildings]] — all 112 rooms, one alphabetical table: output (good/need/points/population) + the game's own descriptions; recipes and build/upkeep costs deferred to their own card

### goods
- [[goods]] — all 42 resources grouped by category (food/raw/refined/manufactured/military) with decay rates; military doesn't count toward raider wealth

### animal
- [[animals]] — all 9 animals: 6 pasture livestock + 3 wild fauna; yields, climate/terrain suitability, danger/mass, game descriptions

### event
*(none yet)*
