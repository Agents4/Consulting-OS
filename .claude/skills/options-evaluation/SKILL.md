---
name: options-evaluation
description: Define options and criteria, score them consistently, and recommend a choice with trade-offs.
disable-model-invocation: false
user-invocable: true
---

# Options Evaluation

## Quick Start

```
/options-evaluation
```
Then provide:
1. **The decision** and the options considered
2. **Criteria** the client cares about (or I propose)
3. **Evidence** per option

I will structure options in the same format, weight and score against criteria with evidence, and show the sensitivity of the ranking to the weights.

**Output:** Saved to `outputs/analyses/options-evaluation-[decision]-[date].md`
**Time:** ~30 min

**When to use:** Develop phase when more than one path could answer the question

**Phase:** Develop  |  **Framework source:** `context-library/frameworks/prioritization-matrices.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Initiative Sizing | `outputs/analyses/initiative-sizing-*.md` | value, cost, ease | Value and cost per option |
| Stakeholders | `context-library/stakeholders/*.md` | criteria, priority | What the client values |
| Root Causes | `outputs/analyses/root-cause-*.md` | cause | Which options address which causes |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If choice made -> Link to `recommendation`
- If ranking sensitive -> Link to `scenario-sensitivity`
- If client disagrees on criteria -> Link to `decision-doc`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/analyses/initiative-sizing-*.md`: Value and cost per option
- `context-library/stakeholders/*.md`: What the client values
- `outputs/analyses/root-cause-*.md`: Which options address which causes

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Initiative Sizing:** [Value and cost]

**From Stakeholders:** [Criteria]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Weights
- Evidence for feasibility

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Criteria
**"If you could pick three criteria, which would they be?"**

Agree criteria before scoring to avoid reverse-engineering.

### Question 2: The Do-Nothing
**"What happens if we do nothing?"**

Always score the base case.

---

## The Process

### Step 1: List options

Include do-nothing; same format for each.

### Step 2: Agree criteria and weights

With the sponsor before scoring.

### Step 3: Score with evidence

1 to 5 with a one-line reason per score.

### Step 4: Test weights

Does the winner change under reasonable weights?

### Step 5: State the trade-offs

What you give up by choosing the winner.

---

## Structured Output Template

```markdown
# Options Evaluation: [Decision]

## So-What
[Option B wins on X, trade-off Y]

## Options
| Option | Description | Value | Cost | Time | Risk |
|---|---|---|---|---|---|

## Scoring
| Criterion | Weight | Option A | Option B | Option C | Evidence |
|---|---|---|---|---|---|

## Weight Sensitivity
[ ]

## Trade-offs
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/analyses/options-evaluation-[decision]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decisions/options-[decision].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/recommendation` - Chosen option
- `/slide-draft` - Options page
- `/risk-register` - Option risks

**Pulls from:**
- `/initiative-sizing` - Value
- `/root-cause-analysis` - Causes

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Do-nothing** is included
- [ ] **Criteria agreed** before scoring
- [ ] **Scores** have reasons
- [ ] **Weight sensitivity** shown
- [ ] **Trade-offs** stated
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `recommendation` - Write the recommendation
- `scenario-sensitivity` - Stress it
- `decision-doc` - Log the choice
