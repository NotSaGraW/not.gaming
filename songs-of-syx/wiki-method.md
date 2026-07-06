# wiki-method — portable method for building a knowledge wiki with an LLM

Read this first in any new project. Domain-agnostic: the schema for the new
domain is designed fresh (see `CLAUDE.md`) — only the process and rules below
transfer.

## Provenance

This is **Andrej Karpathy's LLM Wiki framework** (idea file:
gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) plus two layers:
operational guardrails from the fitness pilot, and patches the gist's comment
thread surfaced. Karpathy frames his text as "intentionally abstract... optional
and modular" — a framework to adapt per domain, like Agile, not a fixed recipe.
Adapt it; just pre-empt the known failure modes below instead of rediscovering
them.

Karpathy's canonical layers: `raw/` (immutable sources), `wiki/` (LLM-owned
pages), schema file, `index.md` (catalog), `log.md` (append-only). This template
names sources `source/` instead of `raw/` — harmless; just be consistent.

## The pattern

Obsidian is the IDE, the LLM is the cataloguer, the wiki is the codebase.
Three operations: **ingest**, **query**, **lint**. The point vs RAG: knowledge is
compiled once into a persistent, compounding wiki and kept current, not
re-derived per query.

Roles:
- **Curator (human):** decides which sources enter, directs research, judges
  meaning. Does not write pages.
- **Cataloguer (LLM):** reads sources, creates/updates cards, maintains links and
  index, runs lint. **Never decides which sources are valid.**

## Hard rules (non-negotiable — each comes from a real failure)

1. **The cataloguer never invents a source.** If a card needs a source not in
   `source/`, STOP and ask the curator. Don't manufacture a source to make a link
   resolve. *(Pilot: fabricated sources, caught by the curator not the system —
   the gist thread calls this "hallucination becoming ground truth".)*
2. **git from commit zero.** Commit after every operation. Karpathy: "the wiki is
   just a git repo." Only real protection against a destructive edit. *(Pilot: a
   script emptied every card; survived only because content was regenerable.)*
3. **Never read-then-write the same file in one expression** (`open(path,'w')`
   truncates before the read evaluates). Build from explicit in-memory data, then
   write. After any batch write, verify no file is 0 bytes.
4. **Lint + verify after every ingest/edit before declaring done.**
5. **Sources are immutable and named by provenance** (search/topic), never by a
   taxonomy/category label. *(Pilot: a source named `arm-balances` collided with
   the `balance` category.)*
6. **Don't trust the log or memory as proof a file exists or existed.** Verify on
   disk.
7. **External edits don't show in Obsidian's graph until a full reindex**
   (Ctrl+P → "Reload app without saving"). Never conclude data is wrong from a
   stale graph.

## Scaling & integrity rules (validated by the gist's comment thread)

8. **Stable id, separate from display name.** Each card has a fixed id/slug that
   links point to; the readable name is a field. Never rename the id — rename only
   the display field. *(Pilot: a display rename forced rewriting every link.)*
9. **The index (and any search DB) is derived and rebuildable; the `source/` +
   `wiki/` files are the only truth.** Never treat `index.md` as authoritative.
10. **Re-touch by appending, not overwriting.** New info updating a card goes in a
    "History/Update" section, so nuance isn't compressed out and stale claims
    don't silently become ground truth.
11. **Lint by delta, deterministically.** Don't re-check the whole wiki (O(n²),
    blows the context). Deterministic checks (orphans, empty files, phantom cards,
    status flags) use grep/os.walk at near-zero cost. Reasoning checks
    (contradictions) run only on cards changed since last lint + their 1st/2nd
    degree link neighbors. Occasional full sweeps catch the rest.
12. **A contradiction is a node, not an edge** (when the domain has competing
    claims): its own page with status (open / held / resolved-with-proof) and
    provenance.

## Schema design principles (design fresh per domain)

- One concept per card (atomic). Its own name/identity → its own card.
- Orthogonal axes never share one field.
- Name the governing file for tool autoload: `CLAUDE.md` (Claude Code) or
  `AGENTS.md` (Codex). It is "the schema" in Karpathy's framework.
- Identifier = stable slug; display name in the reader's language, native name as
  a secondary field.
- Internal links use bare `[[stable-id]]`.
- Queryable fields use a controlled vocabulary (one form per term).
- For the graph to show relationships, cards need **directional links to each
  other**, not only links to shared category hubs.
- Categories as plain-text tags + a query (Dataview) unless you need browseable
  hubs; hand-kept category pages duplicate the index and drift.
- Rich detail added on demand at query time, not on ingest.

## Working style (carry the curator's preferences here)

- Concise prose, no filler. Critical by default; confidence tags
  [Certain]/[Likely]/[Guessing]; verify before asserting.
- Incremental, one operation at a time. Don't redesign the schema unilaterally —
  propose, the curator approves.
