---
name: model-build
description: "Build the Excel model from the spec: separate inputs, calculations, outputs; formulas only; checks that pass."
---

# Model Build

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/model-build
```
Then provide:
1. **The model spec**
2. **Input data** (clean and sourced)
3. **The starter file** (default: `~/.gemini/extensions/consulting-os/templates/model-starter-template.xlsx`)

I will build the workbook with openpyxl from the spec, recalculate with LibreOffice, confirm zero errors and green checks, and hand it over with a guide tab.

**Output:** Saved to `outputs/models/[model]-DRAFT-v[date].xlsx`
**Time:** ~45 to 90 min depending on size

**When to use:** After the spec is agreed

**Phase:** Develop  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/engagement-model/07-excel-modeling-standards.md`; `~/.gemini/extensions/consulting-os/templates/model-starter-template.xlsx`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Model Spec | `outputs/models/model-spec-*.md` | tabs, inputs, checks | What to build |
| Standards | `~/.gemini/extensions/consulting-os/context-library/engagement-model/07-excel-modeling-standards.md` | blue, black, green, hardcode, check | Build rules |
| Data | `context-library/data/*.md`, `outputs/analyses/data-profile-*.md` | clean data, reconciled | Input data |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If model is built -> Link to `model-audit`
- If outputs needed on slides -> Link to `number-tie-out`
- If scenarios -> Link to `scenario-sensitivity`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/models/model-spec-*.md`: What to build
- `~/.gemini/extensions/consulting-os/context-library/engagement-model/07-excel-modeling-standards.md`: Build rules
- `context-library/data/*.md`, `outputs/analyses/data-profile-*.md`: Input data

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Model Spec:** [Tabs, inputs, checks]

**From Data:** [Clean inputs]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Missing inputs
- Unclear formulas in the spec

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Reviewer
**"Who reviews the model independently, and when?"**

Review is planned, not optional.

---

## The Process

### Step 1: Copy the starter

Never build from a blank sheet; keep Cover, Guide, Inputs, Calc, Scenarios, Outputs, Checks, Log.

### Step 2: Enter inputs

Blue font, one cell per assumption, unit, source, owner, date, confidence.

### Step 3: Build calculations

One formula per row copied across; no hardcodes; no merged cells; no OFFSET or INDIRECT.

### Step 4: Build outputs and checks

Outputs tab feeds slides; checks roll up to a master flag on the Cover.

### Step 5: Recalculate and test

Run LibreOffice recalc; confirm zero errors; flex inputs and watch outputs move sensibly.

---

## Common Mistakes

- **Typing numbers into formulas**: Every number lives on the Inputs tab.
- **Silent circularity**: No circular references; use explicit iteration blocks if needed and document them.

---

## Structured Output Template

```markdown
# Model Build Note: [Model]

**File:** [name]  |  **Owner:** [ ]  |  **Version:** [ ]

## What was built
[Tabs and logic]

## Recalc Result
Errors: [0]  |  Integrity flags: [0]  |  Sense flags: [ ]

## Tests Run
| Test | Input change | Expected | Observed |
|---|---|---|---|

## Known Limits
[ ]

## Next Step
[Independent audit by [name]]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/models/[model]-DRAFT-v[date].xlsx`
- When finalized and agreed with the EM or client: copy to `context-library/models/[model].xlsx`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/model-audit` - File to audit
- `/number-tie-out` - Outputs to tie
- `/scenario-sensitivity` - Live model

**Pulls from:**
- `/model-spec` - Spec
- `/data-exploration` - Clean data

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Zero errors** after recalculation
- [ ] **No hardcodes** in formulas
- [ ] **Inputs** sourced and dated
- [ ] **Checks tab** rolls up to the Cover
- [ ] **Guide tab** explains the model
- [ ] **File name** follows `[Model]_[STATUS]_[vDATE]_[initials].xlsx`
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `model-audit` - Audit the model
- `number-tie-out` - Tie numbers
- `scenario-sensitivity` - Run scenarios
