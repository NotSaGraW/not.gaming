# wiki-template — local knowledge-base starter (Karpathy LLM Wiki framework)

Copy this **whole directory** to start a new local-memory project (gaming,
career, learning…). It gives you the structure, the rules and an empty schema to
fill — so a fresh LLM conversation knows what to do and avoids the mistakes
already documented.

## What's inside

```
wiki-template/
  README.md        ← this file
  wiki-method.md   ← the method + hard rules. Read this FIRST in any new project.
  CLAUDE.md        ← governing schema. Fill the <placeholders> for your domain.
  source/          ← immutable raw sources. Curator drops files here; never edited.
  wiki/
    index.md       ← catalog of all cards (rebuildable, not authoritative)
    log.md         ← append-only operation log
```

## Bootstrap a new project (first session)

1. Copy this directory, rename it for the project, open it as an Obsidian vault.
2. `git init` and a first commit. (This is the rule we most lacked — do it now.)
3. Read `wiki-method.md`.
4. Fill `CLAUDE.md` with the curator: fields, axes, what counts as a source,
   relation semantics, the stable-id convention. Freeze it before bulk ingest.
5. Curator drops the first source(s) into `source/`.
6. Ingest a seed set (~10–15 cards), built from data. Lint. Commit.
7. Expand. Lint. Commit. Repeat.

## Telling the LLM what to do

In Claude Code, `CLAUDE.md` auto-loads as project instructions. Otherwise start
the conversation with: "Read `wiki-method.md` and `CLAUDE.md` before doing
anything." That loads the framework, the guardrails and the domain schema in one
shot.
