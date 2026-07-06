# Source: game-data extract — embassy tech node (EMBA0)

- **Origin:** game-data (v71 install files, `source/data/assets/init/tech/ADMIN.txt`, lines ~278–290)
- **Date extracted:** 2026-07-06
- **Note:** short excerpt for reference; full game files are local-only (gitignored), see publication rule.

---

```
EMBA0: {
    LEVEL_MAX: 5,
    LEVEL_COST_INC: 5,
    COSTS: {
        CIVIC_KNOWLEDGE: 5,
    },
    REQUIRES_TECH_LEVEL: {
    },
    BOOST: {
        ROOM_EMBASSY>ADD: 0.2,
    },
},
```

Reading: embassy tech exists in the ADMIN tech tree. 5 levels, 5 Knowledge base cost with +5 increment per level, no tech prerequisites, each level adds +0.2 (+20%) to ROOM_EMBASSY output — +100% at max level.
