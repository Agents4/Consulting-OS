---
name: prioritize-analyses
description: "Rank candidate analyses by impact on the answer, effort, and data readiness; decide what to run, park, or kill."
---

# Prioritize Analyses

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/prioritize-analyses
```
Then provide:
1. **The candidate analyses** (or point me to the issue tree)
2. **Team capacity** until the next gate
3. **Data status**

I will score each analysis, plot it on an impact-effort matrix, and recommend the next-two-weeks plan with explicit parked items.

**Output:** Saved to `outputs/analyses/prioritization-[engagement]-[date].md`
**Time:** ~20 min

**When to use:** Start of each phase and whenever the list of possible analyses outgrows capacity

**Phase:** Mobilize and Diagnose  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/frameworks/prioritization-matrices.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Issue Trees | `outputs/issue-trees/*.md` | leaf, analysis | Candidate analyses |
| Hypotheses | `outputs/hypotheses/*.md` | confidence, test | Uncertainty that analysis would reduce |
| Workplan | `outputs/workplans/*.md` | owner, days, gate | Capacity and dates |
| Data Requests | `outputs/data-requests/*.md` | status | Data readiness |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If list is agreed -> Link to `workplan-build`
- If data is blocking -> Link to `data-request`
- If scope pressure -> Link to `decision-doc`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/issue-trees/*.md`: Candidate analyses
- `outputs/hypotheses/*.md`: Uncertainty that analysis would reduce
- `outputs/workplans/*.md`: Capacity and dates
- `outputs/data-requests/*.md`: Data readiness

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Issue Tree:** [Candidate analyses]

**From Workplan:** [Capacity]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Effort estimates
- How much each analysis changes the answer

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Gate
**"Which gate is the binding constraint?"**

Prioritize for the next decision, not for completeness.

### Question 2: The Swing
**"Which analysis could change the recommendation the most?"**

Those get run first even if hard.

---

## The Process

### Step 1: List candidates

One line each with the hypothesis it tests.

### Step 2: Score impact and effort

Impact on the answer 1 to 5; effort in days; data readiness; confidence in the result.

### Step 3: Plot the matrix

Do now, schedule, quick check, park.

### Step 4: Apply the 80/20 rule

Cut analyses that cannot change the answer.

### Step 5: Agree with the EM

Record parked items and why.

---

## Structured Output Template

```markdown
# Analysis Prioritization: [Engagement]

| Analysis | Hypothesis | Impact (1-5) | Effort (days) | Data ready? | Quadrant | Decision | Owner |
|---|---|---|---|---|---|---|---|

## Matrix
```
High impact | Schedule | Do now
Low impact  | Park     | Quick check
            Hard       Easy
```

## Parked and Why
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/analyses/prioritization-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/hypotheses/prioritization-[engagement].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/workplan-build` - Updated plan
- `/daily-plan` - Daily focus

**Pulls from:**
- `/issue-tree` - Candidates
- `/hypothesis-draft` - Uncertainty

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Every analysis** links to a hypothesis
- [ ] **Scores** have a one-line reason
- [ ] **Parked items** are recorded
- [ ] **Capacity** fits the next gate
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `workplan-build` - Update the plan
- `hypothesis-draft` - Update hypotheses
- `decision-doc` - Log scope trade-offs
