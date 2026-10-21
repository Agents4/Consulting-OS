---
name: root-cause-analysis
description: "Find root causes of a performance gap using drivers, 5 whys, and data splits; separate cause from symptom."
---

# Root Cause Analysis

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/root-cause-analysis
```
Then provide:
1. **The gap or problem** with numbers
2. **Data available** for splits
3. **Hypotheses on cause**

I will split the problem by dimension, test each cause hypothesis, and give a ranked list of root causes with evidence and confidence.

**Output:** Saved to `outputs/analyses/root-cause-[topic]-[date].md`
**Time:** ~30 min

**When to use:** A KPI is off, a gap is found, or interviews and data disagree

**Phase:** Diagnose  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/frameworks/seven-step-problem-solving.md`; 5 Whys; driver splits

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Analyses | `outputs/analyses/*.md` | gap, variance, driver | What the gap looks like |
| Interviews | `outputs/research-synthesis/*.md` | cause, reason, blocker | Qualitative explanations |
| Data | `context-library/data/*.md` | segment, region, time | Splits possible |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If data needs cleaning -> Link to `data-exploration`
- If driver tree helps -> Link to `value-driver-tree`
- If fix options next -> Link to `options-evaluation`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/analyses/*.md`: What the gap looks like
- `outputs/research-synthesis/*.md`: Qualitative explanations
- `context-library/data/*.md`: Splits possible

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Analyses:** [Gap size and shape]

**From Interviews:** [Stated causes]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Which splits are available
- Time trend

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Split
**"Where is the gap concentrated (segment, site, time, product)?"**

Concentration points to cause.

---

## The Process

### Step 1: Quantify the gap

Size, trend, and where it is largest.

### Step 2: Split by dimension

Pareto the gap by segment, time, product, region.

### Step 3: List cause hypotheses

Structured by driver tree.

### Step 4: Test each

With data or field evidence; record result.

### Step 5: Rank root causes

Evidence strength x share of gap explained.

---

## Structured Output Template

```markdown
# Root Cause Analysis: [Topic]

## So-What
[Primary cause and share of gap explained]

## Gap Quantified
[ ]

## Splits
| Dimension | Finding | Share of gap |
|---|---|---|

## Cause Hypotheses
| Cause | Test | Result | Evidence strength | Share explained |
|---|---|---|---|---|

## Root Causes Ranked
1. [ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/analyses/root-cause-[topic]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/research/root-cause-[topic].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/options-evaluation` - Causes to address
- `/storyline` - Diagnostic pages
- `/hypothesis-draft` - Updates

**Pulls from:**
- `/data-exploration` - Clean data
- `/interview-synthesis` - Field evidence

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Cause vs symptom** is distinguished
- [ ] **Shares** sum to the gap or explain the rest
- [ ] **Evidence** cited for each cause
- [ ] **Alternatives** considered
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `options-evaluation` - Choose fixes
- `value-driver-tree` - Link to value
- `skeptic` - Challenge
