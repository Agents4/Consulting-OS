---
name: kickoff-plan
description: Plan the kickoff meeting, pre-day-1 reading, first two weeks, logistics, and team charter conversation.
disable-model-invocation: false
user-invocable: true
---

# Kickoff Plan

## Quick Start

```
/kickoff-plan
```
Then provide:
1. **Engagement name and start date**
2. **Attendees** (sponsor, counterpart, SteerCo, team)
3. **What is already agreed** (scope, team, governance)

I will produce a kickoff agenda, a pre-day-1 checklist, a first-two-weeks plan, and a team charter so the cadence is running by day 10.

**Output:** Saved to `outputs/kickoff/kickoff-plan-[engagement]-[date].md`
**Time:** ~20 min

**When to use:** The week before the engagement starts

**Phase:** Mobilize  |  **Framework source:** `templates/kickoff-agenda-template.md`; `context-library/engagement-model/05-cadence-and-handoffs.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Team Roster | `context-library/team-roster-template.md` | roles, hours, location | Team, working hours, on-site days |
| Stakeholders | `context-library/stakeholders/*.md` | sponsor, counterpart, SteerCo | Attendees and sensitivities |
| Problem Statement | `outputs/problem-statements/*.md` | key question, scope | What to present as agreed |
| Cadence | `context-library/engagement-model/05-cadence-and-handoffs.md` | check-in, SteerCo, pre-wire | Standard rhythm and handoff rules |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If data access is unclear -> Link to `data-request`
- If stakeholders are unmapped -> Link to `stakeholder-map`
- If workplan is missing -> Link to `workplan-build`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/team-roster-template.md`: Team, working hours, on-site days
- `context-library/stakeholders/*.md`: Attendees and sensitivities
- `outputs/problem-statements/*.md`: What to present as agreed
- `context-library/engagement-model/05-cadence-and-handoffs.md`: Standard rhythm and handoff rules

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Roster:** [Team and availability]

**From Stakeholders:** [Who needs pre-wiring]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Who the real sponsor is
- Data owners
- Client template and tool access

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Sponsor
**"Who feels threatened by this work, and who wants it to succeed?"**

Determines pre-wire order and the tone of the kickoff.

### Question 2: The Rhythm
**"Which SteerCo dates are already in calendars?"**

Hold dates 2 to 3 months ahead.

### Question 3: The Logistics
**"What access, badges, and team space are still open?"**

Day-1 delays kill early momentum.

---

## The Process

### Step 1: Draft the kickoff agenda

60 to 90 minutes: purpose, key question, scope, approach, roles, governance, data, first tasks.

### Step 2: Build the pre-day-1 list

Read SOW twice, client research, stakeholder map, working style questions.

### Step 3: Plan weeks 1 and 2

Data requests out by day 3, workplan by day 7, an early-win page by day 10.

### Step 4: Settle logistics

Access, room, template, support staff, folders, calendar holds.

### Step 5: Run the team charter conversation

Core hours, check-in/out times, review SLAs, feedback norms, leave and travel.

---

## Structured Output Template

```markdown
# Kickoff Plan: [Engagement]

## A. Kickoff Meeting
| Time | Item | Lead | Output |
|---|---|---|---|

## B. Before Day 1
- [ ] [Items]

## C. First Two Weeks
| Days | Focus | Done when |
|---|---|---|

## D. Logistics
- [ ] [Items]

## E. Team Charter
[Core hours, check-ins, SLAs, norms]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/kickoff/kickoff-plan-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/engagements/kickoff-[engagement].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/data-request` - Day 1 to 3 data asks
- `/workplan-build` - Week 1 workplan
- `/steerco-prep` - SteerCo calendar

**Pulls from:**
- `/problem-statement` - Agreed question and scope
- `/stakeholder-map` - Attendee map

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Agenda** has a named lead and an output per item
- [ ] **Data owners** are named
- [ ] **SteerCo dates** are scheduled
- [ ] **Early-win page** is planned for day 10
- [ ] **Team charter** covers hours, SLAs, feedback
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `stakeholder-map` - Map sponsors and sceptics
- `data-request` - Send the first requests
- `workplan-build` - Build the workplan
