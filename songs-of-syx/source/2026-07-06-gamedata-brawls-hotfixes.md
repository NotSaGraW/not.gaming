# Source: game-data extract — brawl-related values and hotfix notes (v71)

- **Origin:** game-data (v71 install files, extracts; full files in `source/gamedata-v71/`, local-only)
- **Date extracted:** 2026-07-06
- **Note:** `base-txt/Patchnotes.txt` is a hotfix-level changelog (0.71.YY point releases) that does not appear in Steam announcements — check it per version bump.

---

From `base-txt/Patchnotes.txt`:

```
2026-06-24 0.71.41
Possibly nurfed brawls by disabling children from brawling.

2026-06-24 0.71.40
Guards separate citizens and slaves
```

From `init/config/LEAVE_CAUSE.txt` (death causes → default happiness impact):

```
MURDER: 2,
STARVED: 2,
BRAWL: 0.5,
ACCIDENT: 0.1,
```

From `init/race/HUMAN.txt` (race liking toward other races):

```
OTHER_RACES: {
    GARTHIMI: 0.75,
    CRETONIAN: 0.75,
    CANTOR: 0.75,
    Q_AMEVIA: 0.75,
    DONDORIAN: 0.75,
    ARGONOSH: 0.75,
    TILAPI: 0.2,
},
OTHER_RACES_REVERSE: { *: 1 },
```
