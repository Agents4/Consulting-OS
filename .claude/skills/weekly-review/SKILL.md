---
name: weekly-review
description: Review the week: progress, what worked, what slipped, learning log, and next week's priorities.
disable-model-invocation: false
user-invocable: true
---

# Weekly Review

## Quick Start

```
/weekly-review
```
Then provide:
1. **This week's outputs**
2. **Feedback received**
3. **Next week's gate**

I will review the week against plan, update the learning log, and propose improvements to skills and templates.

**Output:** Saved to `outputs/weekly-reviews/weekly-review-[week].md`
**Time:** ~15 min

**When to use:** Friday afternoon

**Phase:** All  |  **Framework source:** CLAUDE.md self-improving loop

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Daily Plans | `outputs/daily-plans/*.md` | done, slipped | Week log |
| Status | `outputs/status-updates/*.md` | progress | Status |
| Reviews | `outputs/reviews/*.md` | finding | Feedback |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If next week -> Link to `weekly-plan`
- If retro at the end -> Link to `retrospective`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/daily-plans/*.md`: Week log
- `outputs/status-updates/*.md`: Status
- `outputs/reviews/*.md`: Feedback

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Daily Plans:** [Done and slipped]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Feedback not yet given

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Lesson
**"What is the one thing to change next week?"**

Keep it to one.

---

## The Process

### Step 1: Compare plan to actual



### Step 2: Collect feedback



### Step 3: Update the learning log



### Step 4: Propose skill or template fixes



### Step 5: Set next week's goals



---

## Structured Output Template

```markdown
# Weekly Review: [Week]

## Plan vs Actual
[ ]
## Feedback
[ ]
## Learning Log
- [ ]
## Skill and Template Fixes
[ ]
## Next Week
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/weekly-reviews/weekly-review-[week].md`
- When finalized and agreed with the EM or client: copy to `context-library/meetings/weekly-review-[week].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/weekly-plan` - Goals

**Pulls from:**
- `/daily-plan` - Log
- `/status-update` - Status

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **One lesson** captured
- [ ] **Fixes** proposed
- [ ] **Next week** goals set
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `weekly-plan` - Plan next week
- `retrospective` - Retro
