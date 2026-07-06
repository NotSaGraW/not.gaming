# songs-of-syx — schema

Governing file: how this wiki is built and maintained. Configuration, not
content. It co-evolves with use: when a rule causes friction, adjust it here.
Frozen 2026-07-06 after curator review. Read `wiki-method.md` first.

This file is "the schema" in Karpathy's framework. It is named `CLAUDE.md` so
Claude Code auto-loads it as project instructions (Codex's equivalent is
`AGENTS.md`).

## Purpose

Reference for Songs of Syx mechanics and strategy, v71 onward. Claims are
version-tagged and confidence-tagged; the curator's own in-game measurements
outrank community claims.

## Roles

- **Curator (human, SaGraW):** decides which sources enter, directs research,
  judges meaning. Does not write pages.
- **Cataloguer (model):** reads sources, creates/updates cards, maintains links
  and index, runs lint. Does not decide which sources are valid.

## Architecture

- `source/` — immutable sources. Never edited. Source of truth.
- `wiki/` — one card per game concept (mechanic, race, building, strategy,
  event). Owned by the model.
- `wiki/index.md` — catalog of the whole wiki (rebuildable, not authoritative).
- `wiki/log.md` — chronological, append-only record of operations.

## Source quality (curator's filter)

Accepted origins, in trust order:

1. `test` — curator's own in-game measurements (game version, map conditions,
   and observed numbers recorded).
2. `patchnote` — official release notes.
3. `discord` — captures from the official Discord, author names and dates kept.
   Alpha-testers and the dev rank above general community.
4. `wiki-gg` / `wiki-old` — community wiki pages, dated; assume stale until the
   claim is version-checked.

Reject hype and uncredentialed content. Every claim on a card must be traceable
to a file in `source/`. The cataloguer never creates sources — for web content
the curator decides, the cataloguer may fetch and file after approval.

## Publication rule (added 2026-07-06 after real friction)

This repo is **public**. Third-party verbatim content (Discord captures, forum
posts) is other people's expression: it stays **local-only** — gitignored,
never committed. Cards built from it use paraphrase and **role-level
attribution only** ("alpha-tester", "moderator", "community"), never nicknames
or verbatim quotes. Official developer announcements (patch notes) may be
committed with attribution. Facts and game knowledge are freely usable;
people's words are not ours to republish.

## Card schema

Each card carries:

- **id** — stable slug, never renamed. All links point to this.
- **name** — human-readable display name.
- **category** — exactly one of: `mechanic` | `race` | `building` | `strategy`
  | `event`. If a card wants two, split the card.
- **affects** — one or more from the controlled vocabulary: `food`, `industry`,
  `efficiency`, `logistics`, `loyalty`, `fulfillment`, `military`, `trade`,
  `admin`, `population`, `health`. One form per term; extend only via curator
  approval, recorded here.
- **version** — game version the claim was last verified against (e.g. `v71`).
  A card whose version lags the current game version is stale-by-default.
- **confidence** — `measured` | `patch-note` | `dev-stated` | `community-claim`
  | `disputed`. Only `measured` and `patch-note` justify building strategy on.
  `disputed` cards carry a "test in-game" flag and name both claims.
- **source** — `[[link]]` to file(s) in `source/`.
- **relations** — `depends-on` (directional: prerequisite mechanic/tech) and
  `see-also` (undirected, use sparingly).

Rich detail (procedure, caveats, edge cases) is added on demand when a card is
queried, not on ingest. Updates append to a `## History` section on the card —
never overwrite prior claims (method rule 10).

## Operations

- **Ingest:** curator drops a source into `source/` and flags it. Cataloguer
  reads it, discusses relevance, creates/updates cards, updates affected
  relations and `index.md`, appends a `log.md` entry. Commit after every
  operation (curator commits via VS Code).
- **Query:** curator asks. Cataloguer reads `index.md`, locates cards, answers
  with citations. A good answer can be filed back as a new page.
- **Lint:** on request and after every ingest. Deterministic checks first
  (orphans, phantom cards, empty files, broken links, schema conformity);
  reasoning checks (contradictions) on changed cards + neighbors. Judgement
  conflicts go to the curator, not auto-resolved.
- **Version bump:** when a new game version releases, ingest its patch notes
  first; every card whose `affects` overlaps the patch scope is flagged for
  re-verification rather than silently trusted.

## Conventions

- Internal links use `[[stable-id]]`.
- Source files: `YYYY-MM-DD-<origin>-<topic>.md`, origin from the list above.
  Named by provenance, never by category label (method rule 5).
- Log entries: `## [YYYY-MM-DD] operation | detail`.
- Contradictions get their own card (`confidence: disputed`) with status
  open / held / resolved-with-proof.
