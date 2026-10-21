---
name: meeting-notes
description: Turn a meeting transcript or rough notes into decisions, actions, owners, and hypothesis updates.
disable-model-invocation: false
user-invocable: true
---

# Meeting Notes

## Quick Start

```
/meeting-notes
```
Then provide:
1. **Transcript or notes**
2. **Meeting type** (client, SteerCo, team, partner)
3. **Attendees**

I will return decisions, actions with owners and dates, open questions, and signals about stakeholder stance within an hour of the meeting.

**Output:** Saved to `outputs/meeting-notes/meeting-notes-[topic]-[date].md`
**Time:** ~10 min

**When to use:** After every client or partner meeting

**Phase:** All  |  **Framework source:** `context-library/engagement-model/05-cadence-and-handoffs.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Meetings | `context-library/meetings/*.md` | action, decision | Earlier actions |
| Stakeholders | `outputs/stakeholder-maps/*.md` | stance | Signals |
| Hypotheses | `outputs/hypotheses/*.md` | test | Evidence mentioned |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If decision -> Link to `decision-doc`
- If stance -> Link to `stakeholder-map`
- If hypothesis -> Link to `hypothesis-draft`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/meetings/*.md`: Earlier actions
- `outputs/stakeholder-maps/*.md`: Signals
- `outputs/hypotheses/*.md`: Evidence mentioned

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Meetings:** [Open actions]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Missing owners

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Distribution
**"Who gets the notes and when?"**

Notes help only if they arrive fast.

---

## The Process

### Step 1: Summarize in three lines



### Step 2: List decisions



### Step 3: List actions

Owner and date.

### Step 4: Extract signals

Stance and hypothesis evidence.

### Step 5: Send

Same day.

---

## Structured Output Template

```markdown
# Meeting Notes: [Topic] - [Date]

**Attendees:** [ ]

## Summary
[3 lines]

## Decisions
- [ ]

## Actions
| Action | Owner | Due |
|---|---|---|

## Signals
[Stance, evidence]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/meeting-notes/meeting-notes-[topic]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/meetings/meeting-notes-[topic].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/decision-doc` - Decisions
- `/stakeholder-map` - Stance
- `/hypothesis-draft` - Evidence

**Pulls from:**
- `/steerco-prep` - Agenda

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Actions** have owners and dates
- [ ] **Decisions** are unambiguous
- [ ] **Sent same day**
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `decision-doc` - Log decisions
- `stakeholder-map` - Update map
- `status-update` - Status
