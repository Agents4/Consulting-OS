---
name: fact-base
description: "Assemble the baseline fact base: current performance, definitions, and the one set of numbers the team uses."
---

# Fact Base

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/fact-base
```
Then provide:
1. **The baseline period** and metrics
2. **Client sources** for each metric
3. **Known disagreements** between sources

I will produce a single agreed set of baseline numbers with sources, definitions, and reconciliations, so every page uses the same facts.

**Output:** Saved to `outputs/analyses/fact-base-[engagement]-[date].md`
**Time:** ~30 min

**When to use:** Weeks 1 to 3, and whenever a core number is disputed

**Phase:** Diagnose  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/engagement-model/06-deliverable-production-decks.md` (tie-out discipline)

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Data | `context-library/data/*.md` | baseline, actual, reported | Candidate numbers |
| Client Materials | `context-library/client-materials/*.md` | annual report, budget, KPI | Official figures |
| Decisions | `context-library/decisions/*.md` | definition, agreed number | Definitions already agreed |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If numbers conflict -> Link to `data-exploration`
- If definition needs sign-off -> Link to `decision-doc`
- If model uses these -> Link to `model-spec`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/data/*.md`: Candidate numbers
- `context-library/client-materials/*.md`: Official figures
- `context-library/decisions/*.md`: Definitions already agreed

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Data:** [Candidate baselines]

**From Client Materials:** [Official numbers]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Which source wins when they conflict
- Fiscal vs calendar year

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Source of Truth
**"Which system or report does the CFO treat as correct?"**

The fact base must match their number.

---

## The Process

### Step 1: List the metrics

Only those used on slides or in the model.

### Step 2: Assign a source per metric

With owner, date, and definition.

### Step 3: Reconcile conflicts

Explain gaps and pick one number; log the decision.

### Step 4: Get client sign-off

CFO or counterpart confirms.

### Step 5: Publish

One-page fact sheet linked from the model Inputs tab.

---

## Structured Output Template

```markdown
# Fact Base: [Engagement]

**Baseline period:** [ ]  |  **Signed off by:** [ ]  |  **Date:** [ ]

| Metric | Value | Unit | Definition | Source | Owner | Date | Conflicts resolved |
|---|---|---|---|---|---|---|---|

## Conflicts and Decisions
| Metric | Source A | Source B | Chosen | Why |
|---|---|---|---|---|
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/analyses/fact-base-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/data/fact-base-[engagement].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/model-spec` - Baseline inputs
- `/number-tie-out` - Reference numbers
- `/slide-draft` - Facts on slides

**Pulls from:**
- `/data-exploration` - Reconciled data
- `/ingest-materials` - Digested client materials and conflicts

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **One number per metric**
- [ ] **Definition and source** recorded
- [ ] **Conflicts** resolved and logged
- [ ] **Client sign-off** obtained
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `number-tie-out` - Tie every page
- `model-spec` - Plan the model
- `decision-doc` - Log definitions
