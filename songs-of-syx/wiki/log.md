# log

Append-only record of operations. Consistent prefix so it stays grep-parseable:
`grep "^## \[" log.md | tail -5`

## [YYYY-MM-DD] init | template instantiated

## [2026-07-06] init | schema filled and frozen after curator review (category 1:1, affects vocab, version + confidence fields, depends-on/see-also relations)

## [2026-07-06] ingest | 5 sources filed: v71 patch notes, v71 devlog transcript (origin `devlog` pending curator approval), v70 patch notes, 2 Discord captures (#chat-and-discussions, #gameplay-q-and-a)

## [2026-07-06] ingest | seed set: 16 cards (13 mechanic, 3 strategy). 1 disputed (embassy-emissaries), 2 test-in-game flags (crypt distance penalty, army size reduction). index.md rebuilt.

## [2026-07-06] schema | publication rule added after friction: repo is public → third-party verbatim captures local-only (gitignored), cards use role-level attribution. All nicknames stripped from cards; Discord sources untracked; history rewrite of ingest commit required.

## [2026-07-06] ingest | first measured source: test-conscripts-panel (division size 50, cap = divisions × 50, training slider confirmed). conscripts card gains History entry. "armies smaller" flag kept open, curator-deprioritized.

## [2026-07-06] ingest+correction | test-conscripts-tooltips filed (15 tooltip transcriptions). New card battle-equipment (measured). conscripts History corrected: prior entry partly inference (cataloguer over-claimed); pools are building-fed. Active Duty tooltip confirms guard mechanism on law-and-order. Lesson: icons are not data, tooltips are.

## [2026-07-06] ingest | test-training-grounds filed. New card training-grounds (first building card): 24 conscripts/room, emits noise. Open flag: tiles-per-soldier arithmetic (curator 10/soldier vs panel-implied 5.2/soldier) — determine capacity driver.
