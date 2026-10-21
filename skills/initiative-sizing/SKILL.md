---
name: initiative-sizing
description: "Size the value of each initiative: baseline, uplift, flow-through, ramp-up, one-time cost, with ranges and a haircut."
---

# Initiative Sizing

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/initiative-sizing
```
Then provide:
1. **The initiatives** (or point me to the driver tree)
2. **Baseline and benchmark data**
3. **Evidence for uplift** (pilots, peers, interviews)

I will size each initiative on a common basis (run-rate EBITDA, one-time cost, ramp, confidence), show Low/Base/High, and rank by value and ease.

**Output:** Saved to `outputs/analyses/initiative-sizing-[engagement]-[date].md`
**Time:** ~35 min

**When to use:** Develop phase, before the Solutions SteerCo

**Phase:** Develop  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/frameworks/value-driver-trees.md`; `~/.gemini/extensions/consulting-os/context-library/frameworks/prioritization-matrices.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Value Drivers | `outputs/analyses/value-driver-tree-*.md` | lever, driver, baseline | Levers and baselines |
| Benchmarks | `outputs/analyses/benchmark-*.md` | gap, quartile | Evidence for achievable uplift |
| Models | `context-library/models/*.md` | initiative, flow-through, ramp | Existing model logic |
| Fact Base | `outputs/analyses/fact-base-*.md` | baseline | Agreed baseline numbers |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If model needed -> Link to `model-spec`
- If initiatives need ranking -> Link to `options-evaluation`
- If finance will challenge -> Link to `client-cfo (sub-agent)`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/analyses/value-driver-tree-*.md`: Levers and baselines
- `outputs/analyses/benchmark-*.md`: Evidence for achievable uplift
- `context-library/models/*.md`: Existing model logic
- `outputs/analyses/fact-base-*.md`: Agreed baseline numbers

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Value Drivers:** [Levers with baselines]

**From Benchmarks:** [Gaps]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Evidence for uplift per initiative
- One-time cost estimate
- Ramp-up timing

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Evidence
**"What evidence supports the uplift: pilot, peer, expert, or assumption?"**

Weight confidence by evidence type.

### Question 2: The Cash
**"What one-time cost and which year does it hit?"**

Value without cost is not a business case.

---

## The Process

### Step 1: Define each initiative

Scope, owner, mechanism, baseline.

### Step 2: Size run-rate value

Baseline x uplift x flow-through; Low / Base / High.

### Step 3: Add ramp and cost

Year-by-year ramp; one-time cost phasing.

### Step 4: Apply a haircut

Confidence-weight; mark overlaps to avoid double counting.

### Step 5: Rank

Value vs ease; sum with overlap removed.

---

## Common Mistakes

- **Double counting**: Two initiatives that move the same cost line must be netted.
- **Gross vs net**: Show EBITDA after flow-through, not revenue.

---

## Structured Output Template

```markdown
# Initiative Sizing: [Engagement]

## So-What
[Total run-rate EBITDA range and one-time cost]

| Initiative | Mechanism | Baseline | Uplift (L/B/H) | Flow-through | Run-rate EBITDA (L/B/H) | One-time cost | Ramp | Confidence | Evidence |
|---|---|---|---|---|---|---|---|---|---|

## Overlaps Removed
[ ]

## Ranking
| Initiative | Value | Ease | Priority |
|---|---|---|---|
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/analyses/initiative-sizing-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/models/initiative-sizing-[engagement].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/model-spec` - Model inputs
- `/options-evaluation` - Options to rank
- `/roadmap-build` - Sequence

**Pulls from:**
- `/value-driver-tree` - Levers
- `/benchmark-analysis` - Gap
- `/fact-base` - Baseline

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Run-rate and one-time** are separated
- [ ] **Low/Base/High** shown
- [ ] **Overlaps** removed
- [ ] **Evidence type** is stated
- [ ] **Baseline** ties to the fact base
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `model-spec` - Plan the model
- `options-evaluation` - Rank
- `scenario-sensitivity` - Stress test
