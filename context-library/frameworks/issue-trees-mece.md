# Issue Trees and MECE

**Purpose:** Reference for breaking a problem into pieces that are complete and non-overlapping. Used by `/issue-tree`, `/problem-statement`, `/workplan`.

**Source:** McKinsey problem-solving approach (Umbrex summary of Staff Paper 66); BCG course material.

---

## What an Issue Tree Is
A branching decomposition of the key question into sub-questions. Each level is **MECE** (mutually exclusive, collectively exhaustive). Branches are small enough to analyze.

## Issue Tree vs Hypothesis Tree
| | Issue tree | Hypothesis tree |
|---|---|---|
| Nodes are | Open questions ("How can Alpha increase revenue?") | Testable statements ("Alpha can add $8M EBITDA by winning new customers") |
| Use when | Team does not know enough to hypothesize | Team can form specific answers |
| Strength | Complete and safe | Focused and fast |
| Risk | Boils the ocean | Confirmation bias |

Move back and forth between them. Start with an issue tree, then turn the most promising branches into hypotheses.

## Writing Good Nodes
- Questions start with **what, how, or why**. "How can the client minimize its tax burden?" beats "Tax."
- Each branch gets one owner and one set of analyses.
- Use consistent logic at each level (do not mix a process split with a customer split at one level).

## Building Patterns
| Problem type | Natural first split |
|---|---|
| Profit problem | Revenue vs Cost → (Price × Volume × Mix) vs (Fixed + Variable) |
| Growth problem | Existing vs New → customers, products, geographies, channels (Ansoff) |
| Market entry | Market attractiveness, ability to win, entry mode, economics |
| M&A | Strategic fit, valuation and synergies, integration risk |
| Operations | Inputs → process → outputs; capacity, utilization, quality |
| Organization | Structure, roles, talent, governance, culture |
| Pricing | Customer value, cost, competition, strategy |

## MECE Checks
1. **Overlap check:** Could one fact fit in two boxes? If yes, redefine.
2. **Gap check:** Is there a possible answer that fits in none of the boxes? Add an "other" and question it.
3. **Level check:** Are siblings at the same altitude?
4. **Action check:** Can each leaf be analyzed with data you can get?
5. **So-what check:** If each leaf were true, would the parent be answered?

## Prioritizing Branches
Score each leaf on **impact** (size of prize, strategic importance) and **ease** (data availability, time, client control). Plot on a 2x2. Start with high-impact, easy ones. Drop low-impact, hard ones. Revisit as the analysis teaches you more. See `prioritization-matrices.md`.

## Worked Example
**Key question:** How can Alpha Manufacturing raise EBITDA by $13M (to $50M) by 2028?
```
Raise EBITDA by $13M
├── Grow revenue
│   ├── Win new customers (+$8M hypothesis)
│   ├── Raise price / mix on existing customers
│   └── Expand to new geographies
└── Cut cost (+$5M hypothesis)
    ├── Procurement
    ├── Conversion cost (plants)
    └── SG&A
```
