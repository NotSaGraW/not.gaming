# Source: in-game test — hunter cabin full production tooltip (v71)

- **Origin:** test (curator screenshot `Songs of Syx 07_07_2026 23_54_11`; conditions:
  Hunter #001, ~954 pop, Tilapi, 11/11 employees at 100% fill, tech additive +1.00)
- **Date:** 2026-07-07
- **Immutable. Do not edit.**

---

Meat production tooltip, Hunter #001 (all values as displayed):

```
Base:
  Rate        2.200
  Employees   11
  Work-load   1.00
  Commute     1.04
              = 25.168
Multipliers   (value)  (min ↔ max):
  Degrade     ×1.00    (0.250 ↔ 1.000)
  Employees   ×0.70    (0.000 ↔ 1.000)
  Luck        ×0.79    (0.600 ↔ 1.400)
  Efficiency  ×0.95    (0.500 ↔ 1.000)
  Overtime    ×1.00    (1.000 ↔ 1.250)
  Species     ×1.20    (0.100 ↔ 1.200)
  Climate     ×1.00    (0.100 ↔ 1.200)
  Event       ×1.00    (0.100 ↔ 2.000)
  Other (*)   ×1.00    (1.000 ↔ 1.050)
              = 0.63
Additive:
  Technology  +1.00    (0.000 ↔ 4.000)
Total: 25.17 × 0.63 × (1 + 1.00) = +31.80
```

Produced today 30, yesterday 31, this year 426, last year 852, estimated this year 494.
Room panel header showed Efficiency 100% while the formula multiplier read ×0.95.

## Resolves (measured, no inference)
- **Employees ×0.70 at 11/11 (100% fill):** the Employees multiplier is 0.70 at full
  staffing, range 0.000↔1.000 → it is NOT a fill-rate factor (fill-rate would read 1.00 at
  100%). Driver still unlabeled.
- **Commute 1.04 sits in the Base line as a >1 bonus** — confirmed.
- **Efficiency ×0.95 vs panel header 100%** — the header stat is not the formula input.
- Every factor's min↔max envelope is now recorded for a hunter room.
