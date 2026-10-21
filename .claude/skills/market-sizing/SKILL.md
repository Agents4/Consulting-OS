---
name: market-sizing
description: Size a market top-down and bottom-up, reconcile the two, and state assumptions and ranges.
disable-model-invocation: false
user-invocable: true
---

# Market Sizing

## Quick Start

```
/market-sizing
```
Then provide:
1. **The market definition** (product, geography, segment, time)
2. **Data you have** (reports, client sales, benchmarks)
3. **The decision** the size supports

I will build a top-down and a bottom-up estimate, reconcile them, show a range, and list the assumptions that matter most.

**Output:** Saved to `outputs/analyses/market-sizing-[market]-[date].md`
**Time:** ~30 min

**When to use:** Sizing an opportunity, a new market, or a growth target

**Phase:** Diagnose and Develop  |  **Framework source:** `context-library/frameworks/market-sizing-methods.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Research | `context-library/research/*.md` | market size, CAGR, share, population | Published figures and their dates |
| Client Data | `context-library/data/*.md` | revenue, customers, price, units | Bottom-up inputs |
| Frameworks | `context-library/frameworks/market-sizing-methods.md` | TAM, SAM, SOM, top-down, bottom-up | Method rules |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If the question is still open and needs sourced web research -> Link to `research-plan`
- If numbers feed a model -> Link to `model-spec`
- If size feeds a prize -> Link to `initiative-sizing`
- If numbers go on a slide -> Link to `slide-draft`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/research/*.md`: Published figures and their dates
- `context-library/data/*.md`: Bottom-up inputs
- `context-library/frameworks/market-sizing-methods.md`: Method rules

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Research:** [Published market figures]

**From Client Data:** [Units, price, customers]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Market boundaries
- Price and volume sources
- Growth assumptions

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Boundary
**"Which products, geographies, and customer types are in or out?"**

Boundary choices change the answer more than math does.

### Question 2: The Decision
**"What size would change the decision?"**

A rough range is enough if it does not cross the threshold.

---

## The Process

### Step 1: Define the market

Product, geography, segment, year, currency.

### Step 2: Top-down

Start from a published total and narrow by segment, share, and relevance.

### Step 3: Bottom-up

Units x price x frequency x customers; use client data where possible.

### Step 4: Reconcile

Explain gaps over 20%; choose a base and a range.

### Step 5: Stress the drivers

Vary the top three assumptions; show their effect.

---

## Common Mistakes

- **Using one source**: Triangulate with at least two independent sources.
- **Mixing years or currencies**: State year and currency on every number.

---

## Structured Output Template

```markdown
# Market Sizing: [Market]

**Boundary:** [Product / geography / segment / year / currency]

## Answer
[Base size and range in one sentence]

## Top-Down
| Step | Value | Source |
|---|---|---|

## Bottom-Up
| Driver | Value | Source |
|---|---|---|

## Reconciliation
[Gap and explanation]

## Sensitivity
| Assumption | Low | Base | High | Effect on size |
|---|---|---|---|---|
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/analyses/market-sizing-[market]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/research/market-sizing-[market].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/initiative-sizing` - Addressable base
- `/model-spec` - Inputs
- `/slide-draft` - Chart

**Pulls from:**
- `/benchmark-analysis` - Comparables
- `/data-request` - Client data

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Boundary** is explicit
- [ ] **Two methods** are reconciled
- [ ] **Range** is shown
- [ ] **Sources and years** are cited
- [ ] **Units and currency** are consistent
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `initiative-sizing` - Size the prize
- `benchmark-analysis` - Compare to peers
- `model-spec` - Plan the model
