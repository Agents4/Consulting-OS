---
name: problem-statement
description: Write the SMART key question, scope, success criteria, and constraints for sponsor sign-off in week 1.
disable-model-invocation: false
user-invocable: true
---

# Problem Statement

## Quick Start

```
/problem-statement
```
Then provide:
1. **The client's own description** of the problem (email, SOW, call notes)
2. **The sponsor and decision** it supports
3. **Known constraints** (budget, timing, politics, data)

I will convert a loose brief into a one-page problem statement the sponsor can sign: a single key question, scope in and out, success criteria, and constraints.

**Output:** Saved to `outputs/problem-statements/problem-statement-[engagement]-[date].md`
**Time:** ~20 min

**When to use:** Week 1 of any engagement, or whenever scope drifts and the question needs resetting

**Phase:** Mobilize  |  **Framework source:** Seven-step problem solving, step 1; `templates/problem-statement-template.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Client Materials | `context-library/client-materials/*.md` | SOW, brief, objective, KPI | Stated goals and success measures |
| Stakeholders | `context-library/stakeholders/*.md`, `context-library/client-stakeholder-template.md` | sponsor, decision, success | Who decides and what they care about |
| Decisions | `context-library/decisions/*.md` | scope, out of scope, change | Prior scope decisions |
| Frameworks | `context-library/frameworks/seven-step-problem-solving.md` | SMART, key question | Question format rules |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If the question is agreed -> Link to `day-one-answer`
- If scope is contested -> Link to `decision-doc`
- If success criteria need a model -> Link to `model-spec`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/client-materials/*.md`: Stated goals and success measures
- `context-library/stakeholders/*.md`, `context-library/client-stakeholder-template.md`: Who decides and what they care about
- `context-library/decisions/*.md`: Prior scope decisions
- `context-library/frameworks/seven-step-problem-solving.md`: Question format rules

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Client Materials:** [Stated goal, timeframe, KPI]

**From Stakeholders:** [Sponsor and the decision they own]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- The decision the answer feeds
- A quantified target
- What is explicitly out of scope

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Decision
**"What will the sponsor do differently depending on our answer?"**

If nothing changes, the question is too broad or too soft.

### Question 2: The Number
**"What would success look like in a number and a date?"**

A key question without a metric cannot be falsified.

### Question 3: The Boundary
**"What is off the table (units, geographies, headcount, vendors)?"**

Out-of-scope items prevent late scope creep.

---

## The Process

### Step 1: Draft three framings

Write the problem in three different ways. Reject two and note why.

### Step 2: Make it SMART

Specific, Measurable, Action-oriented, Relevant, Time-bound, as a question.

### Step 3: Set boundaries

List in-scope and out-of-scope items and the constraints.

### Step 4: Define success

A table of criteria with metric, baseline, target, date, and who measures it.

### Step 5: Get sign-off

Send with a handoff brief. Log agreement in `/decision-doc`.

---

## Common Mistakes

- **A topic is not a question**: 'Digital strategy' is a topic. 'How can we reach 12% digital share of sales by 2028 within a $15M budget?' is a question.

---

## Structured Output Template

```markdown
# Problem Statement: [Engagement]

**Version:** [ ]  |  **Date:** [ ]  |  **Signed off by:** [Sponsor]

## Key Question
> [SMART question]

**Alternatives considered:** [A, B and why rejected]

## Scope
| In scope | Out of scope |
|---|---|

## Context and Trigger
[Why now]

## Success Criteria
| Criterion | Metric | Baseline | Target | By when | Measured by |
|---|---|---|---|---|---|

## Constraints and Assumptions
[Budget, time, data, politics]

## Decision Rights
[Who decides, who advises, who executes]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/problem-statements/problem-statement-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/engagements/problem-statement-[engagement].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/day-one-answer` - The question to answer on Day 1
- `/issue-tree` - Root of the tree
- `/workplan-build` - Scope drives workplan

**Pulls from:**
- `/proposal-draft` - Initial framing
- `/stakeholder-map` - Sponsor view

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **One question**, not a list
- [ ] **Metric and date** inside the question or criteria
- [ ] **Out-of-scope** is explicit
- [ ] **Sponsor wording** is used where possible
- [ ] **Sign-off** captured in the decision log
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `day-one-answer` - State the first answer
- `issue-tree` - Break the question into parts
- `decision-doc` - Log the sign-off
