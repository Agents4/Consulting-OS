# Worked Example: Project Northstar (Illustrative, Fictional)

**Purpose:** Shows what good looks like at each stage, using one fictional engagement. All names and numbers are invented. Skills point here for format examples.

---

## 1. The Setup

**Client:** Meridian Stays, a fictional 140-property regional hotel group (revenue $610M, EBITDA $92M, margin 15%).
**Sponsor:** CEO. **Counterpart:** VP Strategy. **Finance partner:** CFO.
**Trigger:** Direct bookings flat for four quarters while distribution cost rose 22%.

**SMART key question:**
How can Meridian recover $25M of annual EBITDA by FY2028 through distribution and revenue management without reducing guest satisfaction below 4.4 out of 5?

**Team (core strategy shape):** 1 Partner (about 1 day/week), 1 EM (full time), 2 Consultants, 1 Analyst, data science support on call. 10-week plan, waterfall phases.

---

## 2. Day-1 Answer (written in week 1)

> The gap is mostly distribution mix and rate leakage, not demand. We believe $14-19M comes from shifting booking mix to direct and corporate channels, and $6-9M from revenue-management and ancillary improvements. Cost cuts elsewhere are second order.

## 3. Issue Tree (excerpt)

```
Recover $25M EBITDA
├── Distribution mix
│   ├── Shift OTA bookings to direct (loyalty, app, rate parity)
│   ├── Grow corporate/TMC share (negotiated programs)
│   └── Reduce commission rates (renegotiate)
├── Revenue management
│   ├── Rate leakage (discounts, packages)
│   ├── Length-of-stay and displacement
│   └── Ancillary (parking, F&B, upgrades)
└── Cost
    ├── Procurement
    └── Labor scheduling
```

## 4. Hypothesis Log (excerpt)

| ID | Hypothesis | Status | Evidence | Confidence |
|---|---|---|---|---|
| H1 | OTA share can fall 8 points without volume loss | Supported | Direct-book test cities lost 0.6% volume | Medium |
| H2 | Rate leakage is 2-3% of room revenue | Testing | 14 properties analyzed; 2.4% average | Medium |
| H3 | Corporate programs under-priced vs peers | Weakened | Benchmarks within 3% of peers | Medium |
| H4 | Labor scheduling yields $5M+ | Killed | Union contracts limit; max $1.8M | High |

## 5. Workplan (excerpt, weeks 1-4)

| Workstream | Analysis | Source | Owner | Output | Due |
|---|---|---|---|---|---|
| Distribution | Channel mix and cost by property, 36 months | CRS export, finance ledger | Consultant 1 | Channel model v1 | Wk 2 Thu |
| Revenue mgmt | Rate leakage by property and segment | PMS rate-plan data | Analyst | Leakage model | Wk 3 Tue |
| Corporate | Negotiated rate benchmarks | Expert calls (6), TMC data | Consultant 2 | Benchmark pack | Wk 3 Fri |
| Cross | Baseline and bridge | CFO pack | EM | Baseline tab | Wk 2 Mon |

## 6. Ghost Deck (excerpt)

| # | Action title | Chart | Data needed | Source | Owner | Status |
|---|---|---|---|---|---|---|
| 4 | OTA bookings grew from 41% to 49% of room nights while direct fell 6 points | 100% stacked column, 2022-2026 | Room nights by channel | CRS | Consultant 1 | Data in |
| 5 | Distribution cost per occupied room rose 22%, driven by OTA commission | Waterfall | Cost by channel | Ledger | Analyst | Waiting for finance |
| 9 | Direct channel can recover 5-8 points of share within 24 months | Bar with range | Test-city results | Pilot data | Consultant 1 | Draft |

## 7. Model Spec (excerpt)

**Three questions the model answers:** (1) What is the baseline distribution cost by channel? (2) What EBITDA does each mix-shift scenario create? (3) Which assumption moves the answer most?
**Tabs:** Cover · Guide · Inputs · Data_CRS · Calc_Channel · Calc_RateLeak · Scenarios · Outputs · Checks · Log
**Checks:** Channel revenue sums to ledger revenue (tolerance $50K); room nights tie to PMS; scenario outputs finite.

## 8. SteerCo 2 Executive Summary (format example)

> **Recommendation:** Shift 6 points of room nights from OTA to direct and corporate over 24 months, and close rate leakage by 1.5 points. Together: $19-26M EBITDA at run rate (base $22M).
> - OTA share grew 8 points in four years; each point costs $1.3M in commission (Slide 5).
> - Test cities lost 0.6% volume when OTA promotion was reduced (Slide 9).
> - Rate leakage averages 2.4% of room revenue across 14 properties (Slide 11).
> **Investment:** $7M over 18 months. **Payback:** 9 months from first run-rate month.
> **Decisions needed today:** approve pilots in 6 cities; name an owner for loyalty relaunch.

## 9. Red-Team Questions the Partner Should Ask

1. What happens to occupancy if OTA reduces our ranking in response?
2. Who owns direct conversion today, and what do they get paid for?
3. Does the CFO accept the 2.4% leakage as a baseline or does Finance already net some?
4. Why is the corporate benchmark within 3% when the sponsor believes it is under-priced?
5. What is the downside case if only half the share shift happens?

## 10. Transition Snapshot

PMO of 3 people; weekly KPI tracker; model handed over with a 90-minute walkthrough; the CFO's analyst ran scenario 3 unaided before the team left.

---

**Note:** This example is for format only. Do not copy numbers into real work.
