---
name: scenario-sensitivity
description: Design scenarios and sensitivities, run them, and show which assumptions move the answer most.
disable-model-invocation: false
user-invocable: true
---

# Scenario and Sensitivity Analysis

## Quick Start

```
/scenario-sensitivity
```
Then provide:
1. **The model** and its key outputs
2. **The uncertain assumptions**
3. **The decision threshold** (what NPV or margin changes the decision)

I will run Low/Base/High scenarios and one-at-a-time sensitivities, produce a tornado ranking, and identify the break-even conditions.

**Output:** Saved to `outputs/analyses/scenario-sensitivity-[model]-[date].md`
**Time:** ~25 min

**When to use:** Before a financial case goes to the SteerCo

**Phase:** Develop and Recommend  |  **Framework source:** `templates/model-starter-template.xlsx` (Scenarios tab)

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Models | `outputs/models/*.xlsx`, `context-library/models/*.md` | scenario, input | Live model |
| Initiative Sizing | `outputs/analyses/initiative-sizing-*.md` | Low/Base/High | Ranges |
| Decisions | `context-library/decisions/*.md` | threshold, hurdle | Decision thresholds |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If finance challenges -> Link to `client-cfo (sub-agent)`
- If results go on slides -> Link to `slide-draft`
- If model errors found -> Link to `model-audit`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/models/*.xlsx`, `context-library/models/*.md`: Live model
- `outputs/analyses/initiative-sizing-*.md`: Ranges
- `context-library/decisions/*.md`: Decision thresholds

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Models:** [Scenario structure]

**From Initiative Sizing:** [Ranges]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Hurdle rate
- Which assumptions are most uncertain

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Threshold
**"At what value does the decision flip?"**

Break-even is more useful than a fan of cases.

---

## The Process

### Step 1: Define scenarios

Low, Base, High with a narrative each, not just numbers.

### Step 2: Run the cases

Switch the selector; paste outputs as values into the Log tab with date.

### Step 3: Run one-at-a-time sensitivities

Vary each key input by a fixed range; record effect on the output.

### Step 4: Rank

Tornado of effects; top three assumptions named.

### Step 5: Find break-evens

Input value at which the decision flips.

---

## Structured Output Template

```markdown
# Scenario and Sensitivity: [Model]

## So-What
[Answer holds in Low case / flips if X falls below Y]

## Scenarios
| Scenario | Narrative | Key inputs | Output (NPV / EBITDA) |
|---|---|---|---|

## Sensitivity (tornado)
| Input | Low | High | Output at low | Output at high | Swing |
|---|---|---|---|---|---|

## Break-evens
[ ]
```

---

## Output Format Options

Check **Preferred output formats** in `context-library/engagement-info-template.md`. Default is Office files (xlsx, pptx). If it is blank, ask once and record the answer. Full guide: `advanced/google-workspace-option.md`.

In Google Sheets the scenario selector is a dropdown on `Scenarios`. Sensitivity grids are formulas (odd size, base case in the center), not Excel Data Tables. Paste scenario results as values with a date into `Log`.

---

## Output Integration

### Where to Save

- Working draft: `outputs/analyses/scenario-sensitivity-[model]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/models/scenarios-[model].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/slide-draft` - Charts
- `/recommendation` - Risk-adjusted case
- `/risk-register` - Key assumptions

**Pulls from:**
- `/model-build` - Model
- `/initiative-sizing` - Ranges

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Scenario narratives** exist
- [ ] **Ranges** have a source
- [ ] **Break-even** is stated
- [ ] **Results** are pasted as values with date
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `recommendation` - Use in the recommendation
- `slide-draft` - Visualize
- `risk-register` - Log key risks
