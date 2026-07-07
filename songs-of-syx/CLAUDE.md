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

1. `game-data` — the game's own files, trimmed + versioned copies in
   `source/gamedata-<version>/`, **replicating the install's structure
   exactly** (`data/assets/init/`, `data/assets/text/`, `base/data/`,
   `base/txt/`, `mods/`; art/audio excluded; local-only/gitignored, ~2 MB per
   version). Never invent a layout — identical structure is what makes
   cross-version diffs mechanical. Keep old versions forever. Authoritative
   for *parameters*; says nothing about emergent runtime behavior.
2. `test` — curator's own in-game measurements (game version, map conditions,
   and observed numbers recorded). Authoritative for *behavior*.
3. `patchnote` — official release notes.
4. `devlog` — the developer's video/blog walkthroughs (transcripts). Ranks with
   patchnote for intent, below it for exact values.
5. `discord` — captures from the official Discord, author names and dates kept.
   Alpha-testers and the dev rank above general community.
6. `wiki-gg` / `wiki-old` — community wiki pages, dated; assume stale until the
   claim is version-checked.

Small dated extracts from game files (a node, a stat block) may be committed
with file-path attribution; wholesale game-file copies stay local-only.

Reject hype and uncredentialed content. Every claim on a card must be traceable
to a file in `source/`. The cataloguer never creates sources — for web content
the curator decides, the cataloguer may fetch and file after approval.

## Publication rule (added 2026-07-06 after real friction)

This repo is **public**. Third-party verbatim content (Discord captures, forum
posts) is other people's expression: it stays **local-only** — gitignored,
never committed. Community-wiki captures are additionally license-blocked:
CC BY-SA text cannot be redistributed under this repo's BY-NC-SA (ShareAlike
forbids adding restrictions). Facts and extracted values always flow freely. Cards built from it use paraphrase and **role-level
attribution only** ("alpha-tester", "moderator", "community"), never nicknames
or verbatim quotes. Official developer announcements (patch notes) may be
committed with attribution. Facts and game knowledge are freely usable;
people's words are not ours to republish.

## Card schema

Each card carries:

- **id** — stable slug, never renamed. All links point to this.
- **name** — human-readable display name.
- **category** — exactly one of: `mechanic` | `species` | `building` | `strategy`
  | `event` | `reference`. If a card wants two, split the card. `reference` is
  for generated, non-authoritative views (e.g. a Dataview table rebuilt from
  other cards) — same status as `index.md`; owns no facts of its own.
- **affects** — one or more from the controlled vocabulary: `food`, `industry`,
  `efficiency`, `logistics`, `loyalty`, `fulfillment`, `military`, `trade`,
  `admin`, `population`, `health`. One form per term; extend only via curator
  approval, recorded here.
- **version** — game version the claim was last verified against (e.g. `v71`).
  Staleness is *derived* (version < current game version → lint warns), never
  stored as a field.
- **evidence** — provenance tier, one of: `game-data` | `measured` |
  `patch-note` | `dev-stated` | `community`. Never changes unless a better
  source arrives. game-data/measured are authoritative (parameters/behavior
  respectively).
- **status** — verification state, one of: `open` (single-source, unchecked) |
  `verified` (independently cross-confirmed) | `disputed` (conflicting claims;
  card names both and carries a resolution path). Evidence says how much to
  trust the source; status says whether anyone has checked.
- Cataloguer interpretation on a card (e.g. a "Readings" section) must be
  explicitly labeled as inference and never inherits the card's evidence tier.
- **Run-independence:** cards state facts about the game, valid independent of
  any playthrough. Curator run context appears only as measurement conditions
  in `test` sources — never as claims, never in cards or the log as fact.
- **source** — `[[link]]` to file(s) in `source/`.
- **relations** — `depends-on` (directional: prerequisite mechanic/tech) and
  `see-also` (undirected, use sparingly).

Rich detail (procedure, caveats, edge cases) is added on demand when a card is
queried, not on ingest. Updates append to a `## History` section on the card —
never overwrite prior claims (method rule 10).

## Card authoring

How a card body is written. Earned from repeated mistakes; each rule keeps the
example that motivated it so the mistake stays recognizable.

- **Names: the in-game display name, never the file token.** Tokens mislead —
  `TOMB_NORMAL` is "Crypt", `ALCO_WINE` is "Shedeh", `COTTON` is "Fibre",
  `PLEASURE_NORMAL` is "Massage Parlour", `PASTURE_BALTI` is "Balticrawler Breeder".
  Map every token through the `NAME:` field in `text/room/`, `text/resource/`,
  `text/animal/` before it reaches a card.

- **Words: the game's text, not the cataloguer's.** A species card's prose is the
  in-game `DESC`/`DESC_LONG` plus the game's own `PROS`/`CONS` (`text/race/`); a
  mechanic card's prose is the matching `GUIDE.txt` chapter. The cataloguer adds no
  description, no framing, no "what this card is" preamble.

- **No editorializing; no superlative without proof.** "Premier archers", "best
  workshop race", "the forgiving starter" are opinion stated as fact — banned. A
  comparative claim requires checking every candidate first: "Humans draw settlers
  faster than any race" was false — Dondorians immigrate ×25 to Humans' ×1.5.

- **Data in tables; prose only for genuine explanation.** Entity cards (species,
  buildings, goods) are almost all tables. Mechanic cards carry explanatory prose but
  still tabulate any actual numbers. Group and sort tables by value.

- **A distribution is a table, never a collapsed label.** Anything shaped as a
  wildcard baseline plus named overrides is a set of values, not one category.
  "Religion: Crator" was wrong — the file is `RELIGION*>ADD: -0.9` with `CRATOR: 0`,
  i.e. every god at a value. Terrain is a per-tile thriving multiplier, not a habitat.
  Where the file stores a modifier, compute the value the game shows: religion belief
  = base `1.0` + modifier (Crator 1.0, others 0.1).

- **Never invent meaning.** If a block's effect isn't understood (a raw `STATS`
  weight, the `RESOURCE` yield) flag it or omit it — do not guess a purpose.

- **Formulae: a code block for the equation, a table for the factor values.** Never
  bury a formula or a list of factor ranges in prose. `output = Base × Skill × …` goes
  in a ``` block; the Species/Faction/Tech envelopes go in a sorted table (see
  [[pastures]]). LaTeX `$$` is optional for typeset math but renders only in Obsidian
  and on GitHub, not plain VS Code — the code block renders everywhere.

Frontmatter working set: `category` · `status` · `version` · `source` (source as
provenance *type*: `gamedata`/`patch`/`ingame`/`community`). `category` mirrors the
game's domains (`species`, not "race"); `type` is a sub-bucket only where a domain is
large and self-grouping (e.g. buildings). `evidence` is now optional (source-as-type
carries provenance; lint only checks it when present); `name`/`affects` are still an
open question. The species layer omits all three.

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
- Contradictions get their own card (`status: disputed`) naming both claims,
  their sources, and a resolution path.
