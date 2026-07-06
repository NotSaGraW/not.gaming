# Source: game-data extract — full OTHER_RACES preference matrix (v71)

- **Origin:** game-data (v71 install files, `init/race/*.txt`, OTHER_RACES blocks; full files in `source/gamedata-v71/`, local-only)
- **Date extracted:** 2026-07-06
- **Reading:** row = how much this race likes the column race (1.0 = full preference). Not symmetric.

---

| likes → | HUMAN | DOND | TILAPI | GARTH | CRET | AMEVIA | CANTOR | ARGO |
|---|---|---|---|---|---|---|---|---|
| **HUMAN** | — | 0.75 | 0.2 | 0.75 | 0.75 | 0.75 | 0.75 | 0.75 |
| **DONDORIAN** | 1.0 | — | 0.75 | 0.02 | 1.0 | 1.0 | 1.0 | 0.01 |
| **TILAPI** | 0 | 0 | — | 0.3 | 0.4 | 0.4 | 0.4 | 0.4 |
| **GARTHIMI** | 0.02 | 0.02 | 0.3 | — | 0.02 | 1 | 0.02 | 1 |
| **CRETONIAN** | 0.2 | 0.75 | 0.75 | 0.02 | — | 0.05 | 1 | 0 |
| **Q_AMEVIA** | 0.10 | 0.10 | 0.10 | 0.25 | 0.10 | — | 0.10 | 0.10 |
| **CANTOR** | 0.05 | 1.0 | 1.0 | 0.01 | 1.0 | 1.0 | — | 0.01 |
| **ARGONOSH** | 1.0 | 0.01 | 0.01 | 1.0 | 1.0 | 1.0 | 0.01 | — |

All eight races also carry `OTHER_RACES_REVERSE: { *: 1 }` (consumer of the REVERSE table unidentified).
