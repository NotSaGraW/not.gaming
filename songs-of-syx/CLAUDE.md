# <project> — schema

Governing file: how this wiki is built and maintained. Configuration, not
content. It co-evolves with use: when a rule causes friction, adjust it here.
Fill every <placeholder> with the curator before bulk ingest, then freeze.

This file is "the schema" in Karpathy's framework. It is named `CLAUDE.md` so
Claude Code auto-loads it as project instructions (Codex's equivalent is
`AGENTS.md`).

## Purpose

<one line: what this wiki is a reference for>

## Roles

- **Curator (human):** decides which sources enter, directs research, judges
  meaning. Does not write pages.
- **Cataloguer (model):** reads sources, creates/updates cards, maintains links
  and index, runs lint. Does not decide which sources are valid.

## Architecture

- `source/` — immutable sources. Never edited. Source of truth.
- `wiki/` — one card per <entity / concept>. Owned by the model.
- `wiki/index.md` — catalog of the whole wiki (rebuildable, not authoritative).
- `wiki/log.md` — chronological, append-only record of operations.

## Source quality (curator's filter)

Only sources with a basis enter (manuals, papers, credentialed authors). Reject
hype / uncredentialed content. Every claim on a card must be traceable to a
source in `source/`. The cataloguer never creates sources.

## Card schema  (DEFINE PER DOMAIN — example fields below)

Each card carries:

- **id** — stable slug, never renamed. All links point to this.
- **name** — human-readable display name (+ canonical/native name as secondary).
- **<classifying field>** — e.g. tags/categories. Plain text unless you need
  browseable hubs. Keep orthogonal axes in separate fields.
- **<"what it affects" field>** — controlled vocabulary (one form per term).
- **source** — `[[link]]` to a file in `source/`.
- **<relations>** — directional links to related cards (`leads to` / depends-on /
  prerequisite). This is what makes the graph show relationships.

Rich detail (procedure, caveats, edge cases) is added on demand when a card is
queried, not on ingest.

## Operations

- **Ingest:** curator drops a source into `source/` and flags it. Cataloguer
  reads it, discusses relevance, creates/updates cards, updates affected
  relations and `index.md`, appends a `log.md` entry.
- **Query:** curator asks. Cataloguer reads `index.md`, locates cards, answers
  with citations. A good answer can be filed back as a new page.
- **Lint:** on request. Deterministic checks first (orphans, phantom cards, empty
  files, broken links); reasoning checks (contradictions) on changed cards +
  neighbors. Judgement conflicts go to the curator, not auto-resolved.

## Conventions

- Internal links use `[[stable-id]]`.
- Log entries: `## [YYYY-MM-DD] operation | detail`.
