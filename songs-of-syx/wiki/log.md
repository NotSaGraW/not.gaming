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

## [2026-07-06] resolve | test-training-ground-construction filed: capacity = dummy count (+1 per 2×2 dummy, reachability gap required, ~5 tiles/soldier). Curator self-corrected unit error; flag on training-grounds closed same session it was opened.

## [2026-07-06] schema+resolve | curator mounted v71 game files into source/ (gitignored). New origin `game-data` added to schema (top rank for parameters); `devlog` origin formalized. First game-data resolution: embassy tech EMBA0 found in tech/ADMIN.txt — embassy-emissaries card disputed → dev-stated. Extract filed as 2026-07-06-gamedata-embassy-tech.

## [2026-07-06] restructure | game files trimmed to source/gamedata-v71/ (init + base-data + base-txt + mods, 487 files, ~1 MB, verified byte-identical to raw copy). Raw base/data/mods folders flagged for curator deletion. Convention: one gamedata-<version> folder per game version, kept forever for cross-version diffs.

## [2026-07-06] correction | metadata fix in both discord source headers (immutability exception, curator-approved): "message content verbatim" was inaccurate — cataloguer trimmed UI artifacts and reconstructed message lines. Now reads "faithfully reconstructed, not byte-exact, original not re-fetchable". Content untouched.

## [2026-07-06] schema | confidence field split into evidence (game-data|measured|patch-note|dev-stated|community) + status (open|verified|disputed) — orthogonal axes were conflated. Staleness derived from version field, not stored. Inference-labeling rule added. lint.py added to repo root.

## [2026-07-06] INCIDENT+repair | schema migration script (sandbox python) wrote through a stale mount cache after curator's Windows-side mass deletions: cards got truncated tails or NUL padding, some lost History sections. Detected by lint.py broken-link errors + curator's NUL screenshot. All 18 cards rewritten clean from cataloguer context via the reliable write path; index/log/CLAUDE.md/sources unaffected. NEW RULE: no sandbox batch-rewrites of wiki files — bulk edits go through the harness file tools; after any batch operation, verify file tails, not just non-emptiness.

## [2026-07-06] ingest | card 19: brawls (game-data + community). Discovery: gamedata base-txt/Patchnotes.txt is a hotfix-level changelog absent from Steam announcements (v71 at 0.71.44) — check per version bump. Guards separate races (0.71.40); children excluded from brawls (0.71.41); per-pair race friction in OTHER_RACES (Human→Tilapi 0.2 vs 0.75 default). Extract filed as 2026-07-06-gamedata-brawls-hotfixes.

## [2026-07-06] ingest+verify | wiki.gg "Brawls" page captured (local-only: CC BY-SA incompatible with repo license; gitignore extended to *-wikigg-*). Its Dondorian/Human asymmetry example verified exactly against race files → page credible; distance constants (10/48/58, Chebyshev) and damage formula adopted as wiki-gg evidence, unverified. Full 8×8 OTHER_RACES matrix extracted (committable). brawls card updated via History.
