---
name: meeting-agenda
description: "Write a meeting agenda with purpose, decisions, timing, pre-read, and roles."
---

# Meeting Agenda

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/meeting-agenda
```
Then provide:
1. **Purpose and attendees**
2. **Length**
3. **Decisions needed**

I will write a timed agenda with an owner and an output per item.

**Output:** Saved to `outputs/meeting-notes/agenda-[topic]-[date].md`
**Time:** ~5 min

**When to use:** Before any meeting with the client or partner

**Phase:** All  |  **Framework source:** `~/.gemini/extensions/consulting-os/templates/kickoff-agenda-template.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Meetings | `context-library/meetings/*.md` | open actions | Carry-overs |
| Decisions | `context-library/decisions/*.md` | pending | Decisions needed |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If SteerCo -> Link to `steerco-prep`
- If partner -> Link to `partner-session-prep`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/meetings/*.md`: Carry-overs
- `context-library/decisions/*.md`: Decisions needed

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Meetings:** [Open actions]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Pre-read

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Outcome
**"What is different after the meeting?"**

Defines the agenda.

---

## The Process

### Step 1: State purpose and outcome



### Step 2: List items with owner and output



### Step 3: Time-box



### Step 4: Attach pre-read



---

## Structured Output Template

```markdown
# Agenda: [Topic]

**Purpose / outcome:** [ ]

| Time | Item | Owner | Output |
|---|---|---|---|

**Pre-read:** [ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/meeting-notes/agenda-[topic]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/meetings/agenda-[topic].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/meeting-notes` - Notes

**Pulls from:**
- `/decision-doc` - Pending decisions

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Outcome** is stated
- [ ] **Timing** adds up
- [ ] **Pre-read** attached
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `meeting-notes` - Notes
- `steerco-prep` - SteerCo
