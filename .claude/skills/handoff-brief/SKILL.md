---
name: handoff-brief
description: "Write a handoff: Brief, Backup, So-what, Ask. For assignments and review submissions."
disable-model-invocation: false
user-invocable: true
---

# Handoff Brief

## Quick Start

```
/handoff-brief
```
Then provide:
1. **The assignment or submission**
2. **To whom**
3. **By when**

I will write a four-part handoff that lets the recipient start immediately and lets the reviewer check the work fast.

**Output:** Saved to `outputs/team-messages/handoff-[topic]-[date].md`
**Time:** ~5 min

**When to use:** Every time work changes hands

**Phase:** All  |  **Framework source:** `templates/handoff-brief-template.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Workplan | `outputs/workplans/*.md` | owner, due | Context of the task |
| Hypotheses | `outputs/hypotheses/*.md` | test | Which hypothesis |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If asking for review -> Link to `review-panel`
- If model handoff -> Link to `model-spec`
- If slide handoff -> Link to `ghost-deck`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/workplans/*.md`: Context of the task
- `outputs/hypotheses/*.md`: Which hypothesis

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Workplan:** [Task context]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- What the recipient already knows

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Output
**"What exact output do you want back?"**

Format and level of polish.

---

## The Process

### Step 1: Brief

Question, hypothesis, format, data, constraints.

### Step 2: Backup

Where the work and sources are.

### Step 3: So-what

Expected or current finding and why it matters.

### Step 4: Ask

What you need and by when; flag early if.

---

## Structured Output Template

```markdown
# Handoff: [Topic]

**From / To / Needed by:** [ ]

## Brief
[ ]
## Backup
[ ]
## So-What
[ ]
## Ask
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/team-messages/handoff-[topic]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/meetings/handoff-[topic].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/daily-plan` - Asks

**Pulls from:**
- `/workplan-build` - Tasks

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **All four parts** present
- [ ] **Needed-by** time stated
- [ ] **Backup** link works
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `review-panel` - Request review
- `daily-plan` - Plan the day
