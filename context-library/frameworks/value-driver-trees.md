# Value Driver Trees and Bridges

**Purpose:** Connect an action to a financial outcome using drivers the client can measure. Used by `/value-sizing`, `/business-case`, `/model-spec`.

---

## Core Trees

### Profit (EBITDA)
```
EBITDA
├── Revenue
│   ├── Volume (customers × frequency × units)
│   ├── Price (list × realization)
│   └── Mix
└── Cost
    ├── Variable (COGS, distribution, commissions)
    └── Fixed (people, facilities, IT, overhead)
```

### Customer Revenue
```
Revenue = Customers acquired × ARPU × Retention curve
Customers acquired = Traffic × Conversion
ARPU = Base price + Upsell + Cross-sell
```

### Unit Economics
`Contribution per unit = Price - Variable cost per unit`  ·  `LTV/CAC` ·  `Payback = CAC / (monthly contribution)`

### Cost Take-Out
Spend cube: category × supplier × business unit × owner. Levers: demand (need less), specification (buy different), supplier (buy better), process (do differently).

## Rules for a Good Driver Tree
1. Each node is measurable with data the client has or can get.
2. The math works: parent equals a function of children.
3. Drivers are independent where possible (avoid double counting).
4. Stop where the lever becomes an action ("change commission plan").
5. Every lever has an owner on the client side.

## The Bridge (Waterfall)
Baseline → initiative 1 → initiative 2 → ... → target. Rules:
- Baseline agreed with the client finance partner.
- Initiatives are additive after removing overlaps (list the overlaps and how they were netted).
- Ranges, not points, in early versions. Show low / base / high.
- Separate run-rate from in-year impact; separate one-time costs from recurring.
- Label confidence: High (data-backed), Medium (benchmark-backed), Low (hypothesis).

## Sizing Template
| Initiative | Driver | Baseline | Target | Δ | Calculation | Low / Base / High | Confidence | One-time cost | Owner |
|---|---|---|---|---|---|---|---|---|---|

## Confidence Calibration
| Evidence | Haircut guidance (adjust to your firm's norms) |
|---|---|
| Client data, validated by owner | 0-10% |
| Benchmark from comparable peers | 20-30% |
| Analog from another industry | 30-50% |
| Pure hypothesis | 50%+ or exclude |

## Double-Counting Checklist
- Do two initiatives claim the same cost line?
- Do revenue initiatives share the same customer base?
- Are enabling costs (IT, change) netted?
- Do savings assume headcount that another initiative also removes?
