---
name: model-audit
description: "Independently audit a model: inputs vs sources, formulas, outputs vs benchmark, back-of-envelope, standards."
---

# Model Audit

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/model-audit
```
Then provide:
1. **The model file**
2. **The spec and sources**
3. **Reasonableness anchors** (benchmarks, reported totals)

I will test the model five ways and return a findings list with severity, location, and fix, plus a sign-off recommendation.

**Output:** Saved to `outputs/reviews/model-audit-[model]-[date].md`
**Time:** ~40 min

**When to use:** Before any model output goes to the client

**Phase:** Develop and Recommend  |  **Framework source:** `~/.gemini/extensions/consulting-os/sub-agents/model-auditor.md`; `~/.gemini/extensions/consulting-os/context-library/engagement-model/07-excel-modeling-standards.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Model Spec | `outputs/models/model-spec-*.md` | intent, checks | What the model should do |
| Fact Base | `outputs/analyses/fact-base-*.md` | baseline | Reference numbers |
| Auditor Persona | `~/.gemini/extensions/consulting-os/sub-agents/model-auditor.md` | review, finding | Audit stance and method |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If findings fixed -> Link to `number-tie-out`
- If logic unclear -> Link to `model-spec`
- If finance will review -> Link to `client-cfo (sub-agent)`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/models/model-spec-*.md`: What the model should do
- `outputs/analyses/fact-base-*.md`: Reference numbers
- `~/.gemini/extensions/consulting-os/sub-agents/model-auditor.md`: Audit stance and method

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Spec:** [Intended logic]

**From Fact Base:** [Anchors]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Reviewer independence
- Sources for each input

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Anchor
**"What reported figure or benchmark should the base case be near?"**

A model that lands far from anchors needs explaining.

---

## The Process

### Step 1: Inputs vs sources

Sample every input back to its source.

### Step 2: Formula review

Pattern consistency across rows, hardcodes, ranges, units, signs.

### Step 3: Output vs benchmark

Compare to reported results and peer ranges.

### Step 4: Back-of-envelope

Rebuild the answer in 10 lines; compare.

### Step 5: Standards check

Colors, structure, checks, log; then sign-off recommendation.

---

## Structured Output Template

```markdown
# Model Audit: [Model]

**Auditor:** [ ]  |  **Date:** [ ]  |  **Version audited:** [ ]

## Verdict
[Ready / Ready after fixes / Not ready]

## Findings
| # | Severity (H/M/L) | Tab / cell | Issue | Impact | Fix | Status |
|---|---|---|---|---|---|---|

## Tests Run
| Method | Result |
|---|---|
| Inputs vs sources | |
| Formulas | |
| Outputs vs benchmark | |
| Back-of-envelope | |
| Standards | |
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/reviews/model-audit-[model]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/models/audit-[model].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/model-build` - Fixes
- `/number-tie-out` - Cleared outputs

**Pulls from:**
- `/model-spec` - Intent
- `/fact-base` - Anchors

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Five methods** were run
- [ ] **Each finding** has location and fix
- [ ] **Severity** reasoning is stated
- [ ] **Sign-off** recommendation is explicit
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `model-build` - Apply fixes
- `number-tie-out` - Re-tie numbers
- `scenario-sensitivity` - Stress after fixes
