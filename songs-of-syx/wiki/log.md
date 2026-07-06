# log

Append-only record of operations. Consistent prefix so it stays grep-parseable:
`grep "^## \[" log.md | tail -5`

## [YYYY-MM-DD] init | template instantiated

## [2026-07-06] init | schema filled and frozen after curator review (category 1:1, affects vocab, version + confidence fields, depends-on/see-also relations)

## [2026-07-06] ingest | 5 sources filed: v71 patch notes, v71 devlog transcript (origin `devlog` pending curator approval), v70 patch notes, 2 Discord captures (#chat-and-discussions, #gameplay-q-and-a)

## [2026-07-06] ingest | seed set: 16 cards (13 mechanic, 3 strategy). 1 disputed (embassy-emissaries), 2 test-in-game flags (crypt distance penalty, army size reduction). index.md rebuilt.

## [2026-07-06] schema | publication rule added after friction: repo is public → third-party verbatim captures local-only (gitignored), cards use role-level attribution. All nicknames stripped from cards; Discord sources untracked; history rewrite of ingest commit required.
