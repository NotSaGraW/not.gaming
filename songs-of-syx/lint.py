#!/usr/bin/env python3
"""Deterministic lint for the songs-of-syx wiki (schema of 2026-07-06).

Run from the songs-of-syx directory:  python3 lint.py
Exit code 1 on errors; warnings are informational.
Update CURRENT_VERSION when a new game version is ingested.
"""
import os, re, sys, glob

CURRENT_VERSION = "v71"

CATEGORIES = {"mechanic", "race", "building", "strategy", "event"}
EVIDENCE   = {"game-data", "measured", "patch-note", "dev-stated", "community"}
STATUS     = {"open", "verified", "disputed"}
AFFECTS    = {"food", "industry", "efficiency", "logistics", "loyalty",
              "fulfillment", "military", "trade", "admin", "population", "health"}
SPECIAL    = {"index.md", "log.md"}

errors, warnings = [], []

cards   = [f for f in sorted(glob.glob("wiki/*.md")) if os.path.basename(f) not in SPECIAL]
sources = sorted(glob.glob("source/*.md"))
ids     = {os.path.splitext(os.path.basename(f))[0] for f in cards}
src_ids = {os.path.splitext(os.path.basename(f))[0] for f in sources}

# empty files
for f in cards + sources + [f"wiki/{s}" for s in SPECIAL]:
    if os.path.exists(f) and os.path.getsize(f) == 0:
        errors.append(f"EMPTY FILE: {f}")

texts = {f: open(f, encoding="utf-8").read() for f in cards}
index_txt = open("wiki/index.md", encoding="utf-8").read()

# frontmatter + links per card
linked_from_cards = set()
for f, txt in texts.items():
    fid = os.path.splitext(os.path.basename(f))[0]
    fm = re.search(r"^---\n(.*?)\n---", txt, re.S)
    if not fm:
        errors.append(f"{fid}: no frontmatter"); continue
    d = dict(re.findall(r"^([\w-]+):\s*(.+)$", fm.group(1), re.M))
    if d.get("id") != fid:            errors.append(f"{fid}: id mismatch ({d.get('id')})")
    if d.get("category") not in CATEGORIES: errors.append(f"{fid}: bad category ({d.get('category')})")
    if d.get("evidence") not in EVIDENCE:   errors.append(f"{fid}: bad evidence ({d.get('evidence')})")
    if d.get("status") not in STATUS:       errors.append(f"{fid}: bad status ({d.get('status')})")
    if not d.get("version"):                errors.append(f"{fid}: missing version")
    elif d["version"] != CURRENT_VERSION:   warnings.append(f"{fid}: STALE (version {d['version']} < {CURRENT_VERSION})")
    bad = [a for a in re.findall(r"\w+", d.get("affects", "")) if a not in AFFECTS]
    if bad: errors.append(f"{fid}: affects outside vocab: {bad}")
    for m in re.findall(r"\[\[([^\]|]+)", txt):
        linked_from_cards.add(m)
        if m not in ids and m not in src_ids:
            errors.append(f"{fid}: broken link [[{m}]]")

# orphans: card not linked from any other card nor the index
for cid in ids:
    in_index = f"[[{cid}]]" in index_txt
    in_cards = any(f"[[{cid}]]" in t for f, t in texts.items()
                   if os.path.splitext(os.path.basename(f))[0] != cid)
    if not in_index and not in_cards:
        errors.append(f"ORPHAN: {cid} (not in index nor linked from any card)")

# phantom index entries + index link check
for m in re.findall(r"\[\[([^\]|]+)\]\]", index_txt):
    if m not in ids:
        errors.append(f"index: phantom card [[{m}]]")

# uncited sources (curated .md only)
for s in src_ids:
    if "README" in s: continue
    if s not in linked_from_cards:
        warnings.append(f"uncited source: {s}")

print(f"lint: {len(cards)} cards, {len(sources)} curated sources")
for e in errors:   print(f"  ERROR   {e}")
for w in warnings: print(f"  warning {w}")
if not errors and not warnings: print("  all clean")
sys.exit(1 if errors else 0)
