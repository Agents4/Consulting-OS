---
name: daily-plan
description: "Plan the day: check-in priorities, review slots, handoffs, and check-out; keep the team's rhythm."
---

# Daily Plan

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/daily-plan
```
Then provide:
1. **Your role and today's calendar**
2. **Open assignments**
3. **Reviews due**

I will produce a daily plan with a top three, review windows, handoff asks, and a check-out note.

**Output:** Saved to `outputs/daily-plans/daily-plan-[date].md`
**Time:** ~5 min

**When to use:** Start of every day, and end of day for the check-out

**Phase:** All  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/engagement-model/05-cadence-and-handoffs.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Workplan | `outputs/workplans/*.md` | due, owner | Today's tasks |
| Status | `outputs/status-updates/*.md` | blocker, decision | Open items |
| Working Preferences | `context-library/personal-context-working-preferences.md` | hours, focus | How you work |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If weekly view -> Link to `weekly-plan`
- If review ready -> Link to `review-panel`
- If handoff -> Link to `handoff-brief`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/workplans/*.md`: Today's tasks
- `outputs/status-updates/*.md`: Open items
- `context-library/personal-context-working-preferences.md`: How you work

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Workplan:** [Tasks due]

**From Status:** [Blockers]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Who is waiting on you

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Top Three
**"What three outputs make today a success?"**

Anything else is a bonus.

---

## The Process

### Step 1: Top three

With the deliverable and time block.

### Step 2: Reviews and handoffs

Who needs what from you and by when.

### Step 3: Check-in note

Priorities and risks for the team check-in.

### Step 4: Check-out

What was done, what slipped, what is needed tomorrow.

---

## Structured Output Template

```markdown
# Daily Plan: [Date]

## Top Three
1. [Output] - [time block]

## Reviews and Handoffs
| With | What | By |
|---|---|---|

## Check-in Note
[ ]

## Check-out
Done: [ ]  Slipped: [ ]  Need: [ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/daily-plans/daily-plan-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/meetings/daily-plan-[date].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/weekly-review` - Daily log

**Pulls from:**
- `/workplan-build` - Tasks
- `/handoff-brief` - Handoffs

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Three outputs**, not tasks
- [ ] **Review slots** protected
- [ ] **Check-out** written
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `weekly-plan` - Plan the week
- `handoff-brief` - Write handoffs
- `status-update` - Weekly status
