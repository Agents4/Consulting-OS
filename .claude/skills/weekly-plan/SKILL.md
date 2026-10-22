---
name: weekly-plan
description: "Plan the week: goals, deliverables by day, review ladder, partner session, SteerCo prep."
disable-model-invocation: false
user-invocable: true
---

# Weekly Plan

## Quick Start

```
/weekly-plan
```
Then provide:
1. **Gate dates and SteerCo**
2. **Workplan**
3. **Team capacity**

I will produce a weekly plan with deliverables by day, review windows, and a partner session agenda.

**Output:** Saved to `outputs/weekly-plans/weekly-plan-[week].md`
**Time:** ~10 min

**When to use:** Monday morning or Friday afternoon

**Phase:** All  |  **Framework source:** `context-library/engagement-model/05-cadence-and-handoffs.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Workplan | `outputs/workplans/*.md` | due, owner | Tasks this week |
| Status | `outputs/status-updates/*.md` | risk, slip | Carry-over |
| Calendar | `context-library/meetings/*.md` | SteerCo, partner session | Fixed points |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If daily detail -> Link to `daily-plan`
- If partner session -> Link to `partner-session-prep`
- If SteerCo -> Link to `steerco-prep`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/workplans/*.md`: Tasks this week
- `outputs/status-updates/*.md`: Carry-over
- `context-library/meetings/*.md`: Fixed points

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Workplan:** [Due this week]

**From Status:** [Slipped items]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Client availability

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Week's Outcome
**"What must be true by Friday?"**

Defines the weekly goal.

---

## The Process

### Step 1: Set goals

Three outcomes tied to the next gate.

### Step 2: Place deliverables by day

With review windows.

### Step 3: Protect the review ladder

Draft to EM, then partner, with SLAs.

### Step 4: Plan the partner session

Agenda and pre-read.

### Step 5: Flag risks

Capacity, data, client.

---

## Structured Output Template

```markdown
# Weekly Plan: [Week of]

## Goals
1. [ ]

## By Day
| Day | Deliverable | Owner | Review | Client touchpoint |
|---|---|---|---|---|

## Partner Session
[Agenda]

## Risks
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/weekly-plans/weekly-plan-[week].md`
- When finalized and agreed with the EM or client: copy to `context-library/meetings/weekly-plan-[week].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/daily-plan` - Daily detail
- `/status-update` - Plan vs actual

**Pulls from:**
- `/workplan-build` - Tasks

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Goals** link to a gate
- [ ] **Review windows** exist
- [ ] **Capacity** is realistic
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `daily-plan` - Daily
- `partner-session-prep` - Partner session
- `weekly-review` - Review the week
