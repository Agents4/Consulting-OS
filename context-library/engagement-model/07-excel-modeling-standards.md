# How an Excel Model Gets Made

The model is the evidence. A top-tier engagement lives or dies on whether the client's finance partner trusts the numbers. Consultants rarely write formal "financial models" the way bankers do. They build purpose-built models that answer a few specific questions, then stress-test them hard.

## The Lifecycle (9 steps)

| # | Step | Owner | Output | Skill |
|---|---|---|---|---|
| 1 | **Define the three questions the model must answer** and the hypothesis it tests. Write them on the first tab | Consultant | Model purpose | `/model-spec` |
| 2 | **Spec on paper first.** Drivers, structure (driver tree), tabs, inputs and sources, outputs, time axis, units, scenarios. Get the EM to approve the spec | Consultant | Model spec | `/model-spec` |
| 3 | **Prototype with dummy data** to confirm the mechanics work. Start rough; add detail where it matters | Analyst | Skeleton | `/model-build` |
| 4 | **Load real data** and document every source. Do not wait for every data point; get the key ones first | Analyst | Populated model | `/model-build` |
| 5 | **Build calculation logic** in a clean flow: inputs → calculations → outputs | Analyst | Working model | `/model-build` |
| 6 | **Add checks and sense checks.** Sum checks, reconciliations, error flags rolled up to a master check on the cover | Analyst | Check tab | `/model-build` |
| 7 | **Stress test.** Push inputs to extremes and confirm outputs move in the expected direction; test the biggest drivers; build scenarios and sensitivities | Consultant | Scenarios, tornado | `/scenario-sensitivity` |
| 8 | **Independent review.** Someone other than the builder reviews inputs, formulas, outputs, and adherence to standards; reconciles key outputs to independent sources | Reviewer | Review log | `/model-review` |
| 9 | **Lock, version, and hand over.** User guide, instructions tab, assumptions log, version log; client user runs it once | Model owner | Handover pack | `/transition-plan` |

**Working rules that experienced consultants repeat:**
- Share the model with the manager early and often. Do not build in private.
- Get to ~80% complete before adding nuance. Defer nice-to-have factors.
- Start with one scenario, finish it, then copy its rows so scenarios have parallel structure.
- In an A/B comparison, include only the variables that differ.
- Be able to say which variables have the largest effect on the outcome.
- Check that someone unfamiliar with the situation could follow the model.

---

## Sheet Architecture (default)

| Tab | Purpose |
|---|---|
| **Cover** | Title, purpose, owner, version, status, date, table of contents with hyperlinks, color key, master check |
| **Guide** | How to use the model; model structure diagram; top 4-5 components explained |
| **Inputs** | Every assumption and driver in one place; unit, source, owner, date, comment |
| **Data** | Raw client or external data, untouched. Cleaned data goes in a separate tab |
| **Calc_** | Calculation tabs by module, flowing top to bottom and left to right. One periodicity per sheet |
| **Scenarios** | Scenario selector and scenario-specific inputs |
| **Outputs** | Summary tables and chart sources that feed the slides. Tab names match slide references |
| **Checks** | All error checks and sense checks, summarized to one master flag |
| **Log** | Version log, change log, open issues, review sign-off |

Keep model content in one workbook where possible. Avoid external links unless necessary. Avoid hidden sheets. Any sheet reachable in two clicks from the contents list.

---

## Formatting and Color Conventions

**Pick one convention, show it on the Cover, and keep it the same on every tab.** Conventions differ by firm and client (the table shows the common default and two alternatives seen in published guidance).

| Element | Common default | Alternative seen |
|---|---|---|
| Hard-coded inputs and assumptions | **Blue font** (light yellow fill optional) | Black (inputs) with calculations in blue |
| Formulas / calculations | **Black font** | Blue, orange, or purple |
| Links from other sheets | **Green font** | Treated as calculations |
| Links to external files | Red or orange | |
| Check cells | Conditional format: green when OK, red when flagged | |
| Estimates not yet confirmed | Yellow highlight or "(Est.)" label | |
| Outputs | Bold, border, subtle fill | Green or red font for results |

If a client or firm template exists, use it. Otherwise use the default and document it. Keep to roughly 6-8 colors; use muted tones; check contrast.

**Number formatting:** negatives in brackets, zeros as dashes, consistent decimals, a units column on every line, display millions with number formats (do not divide the underlying value), label real vs nominal.

**Layout:** freeze panes with headers, labels, and checks visible; no merged cells (use Center Across Selection); consistent first-period column across sheets; one blank column after the time series; group and collapse rather than hide; hide gridlines on finished sheets; print setup (headers, margins, page numbers).

---

## Formula Rules

1. **No hard-codes inside formulas.** Only 1, 0, -1 (and occasionally 12 or 4) may appear in a formula. Everything else is an input cell.
2. **One formula per row**, copied across the whole time series. Same logic for actuals and forecasts.
3. **Enter each input once**, link to it everywhere else.
4. **Do not mix a link and a calculation in the same cell.**
5. **Avoid daisy-chaining.** Link to the original source cell.
6. **Avoid volatile and fragile functions:** OFFSET and INDIRECT are high risk. Use INDEX-MATCH or XLOOKUP over VLOOKUP/HLOOKUP. Use nested IF and array formulas only with a reason.
7. **No circular references.** Set calculation to automatic; iterative calculation off.
8. **Break complex formulas into steps.** If you cannot explain a formula in about 30 seconds, split it.
9. **Test errors specifically.** Do not wrap everything in IFERROR to hide problems.
10. **Avoid macros** unless unavoidable; never rely on recorder output.
11. **Replace references to blank cells with explicit zeros.**
12. **Use data validation drop-downs** (not form controls) for selectors.

---

## Checks

| Type | Examples |
|---|---|
| **Integrity checks** (must be zero) | Sub-totals equal totals; annual equals sum of monthly; assets equal liabilities plus equity (if applicable); allocated equals source; data row counts match |
| **Reconciliation** | Model baseline to the client's reported financials; external-link values to source |
| **Sense checks** (rule-of-thumb, do not necessarily mean error) | Growth rates within plausible bands; margin within benchmark; unit economics positive; price × volume ties to revenue |
| **Error flags** | No #REF!, #DIV/0!, #NUM! in outputs under any scenario |
| **Master check** | One cell on the cover, linked to all check totals, using a named tolerance (use ABS and 1/0 flags) |

---

## Documentation

- Cover: purpose, intended users, assumed knowledge, unusual sections.
- Every sheet and section described.
- Every input has Source, Owner, Date, and Comment.
- Instructions tab or cell comments for the top components.
- Plain-language explanation column beside key calculations.
- Version log: what changed, who, when.
- File naming: `[Model]_[STATUS]_[vYYYYMMDD]_[initials].xlsx` (internal edits tracked separately from external releases).

---

## Common Model Types on a Strategy Engagement

| Model | Core logic | Key checks |
|---|---|---|
| Market sizing | Top-down (market → segment → share) and bottom-up (units × price), triangulated | Two methods within an agreed band |
| Baseline / driver tree | Revenue or cost decomposed into drivers (price × volume × mix) | Ties to reported actuals |
| Opportunity sizing / EBITDA bridge | Baseline → initiatives with ranges → target | Sum of initiatives equals bridge; no double counting |
| Business case / NPV | Costs, benefits, timing, discount rate | Cash flows sum; sensitivity to ramp-up and one-time costs |
| Benchmarking database | Peer metrics normalized | Definitions consistent; source per row |
| Pricing / revenue model | Elasticity or price-volume scenarios | Revenue reconciles to current baseline |
| Capacity / operations model | Demand, throughput, utilization, headcount | Capacity ≥ demand in base case |
| Org / FTE model | Spans and layers, cost per FTE, transitions | Headcount ties to HR data |
| Cost take-out | Spend cube by category × supplier × owner; savings levers | Spend ties to ledger |

## Data Handling Tools
Excel (Power Query for repeatable cleaning, PivotTables, Power Pivot), SQL, Python or R for large files, Alteryx or similar for repeatable pipelines, Tableau or Power BI for exploration, Solver and what-if tools (Goal Seek, Scenario Manager, Data Tables) for optimization and scenarios. Keep raw data untouched; every transformation logged.

## Review Methods (mix at least three)
1. **Input review:** every input against its source.
2. **Formula review:** consistency across rows, no hard-codes, no broken ranges (trace precedents/dependents; Go To Special).
3. **Output review:** reasonableness vs rule of thumb and benchmark.
4. **Back-of-envelope triangulation:** can a 5-line mental model reproduce the answer within ±20%?
5. **Standards review:** adherence to this file.
6. **Independent rebuild** of the key calculation by a second person for high-stakes outputs.

## Model Owner Rule
One person holds the master workbook. Everyone else sends changes to that person or works on a branch copy that is merged at a fixed time. The owner publishes a new version number daily.

## Variant: Google Sheets
The architecture (Cover, Guide, Inputs, Calc, Scenarios, Outputs, Checks, Log), color convention, formula rules, and review methods carry over unchanged. What changes: calculation is live, so verification is reading values and scanning for error cells; versions are named in Version history and frozen by copying to FINAL; Calc, Outputs, and Checks are protected; avoid QUERY, ARRAYFORMULA, IMPORTRANGE, and GOOGLEFINANCE if the file may be exported to Excel; sensitivity tables are formula grids, not Data Tables. Heavy models and very large data stay in Excel. Details: `advanced/google-workspace-option.md`.
