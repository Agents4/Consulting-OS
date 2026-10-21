---
name: client-update-email
description: "Draft a client email: status, request, escalation, or thank-you, in the right tone and length."
---

# Client Update Email

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/client-update-email
```
Then provide:
1. **Purpose and recipient**
2. **Key message**
3. **Ask and date**

I will draft a short, answer-first email in the client-exec voice with a clear ask.

**Output:** Saved to `outputs/team-messages/client-email-[topic]-[date].md`
**Time:** ~5 min

**When to use:** Whenever writing to the client

**Phase:** All  |  **Framework source:** `context-library/writing-style-client-exec.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Writing Style | `context-library/writing-style-client-exec.md` | tone, length | Voice |
| Stakeholders | `outputs/stakeholder-maps/*.md` | preference, stance | Recipient notes |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If status -> Link to `status-update`
- If escalation -> Link to `risk-register`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/writing-style-client-exec.md`: Voice
- `outputs/stakeholder-maps/*.md`: Recipient notes

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Writing Style:** [Voice rules]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Sensitivities

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Ask
**"What do you want the recipient to do, and by when?"**

One ask per email.

---

## The Process

### Step 1: Lead with the message



### Step 2: State the ask and date



### Step 3: Add only needed context



### Step 4: Check tone

Match the recipient.

---

## Structured Output Template

```markdown
Subject: [Message in one line]

[Recipient],

[Message in two sentences.]

[Ask and date.]

[Name]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/team-messages/client-email-[topic]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/meetings/client-email-[topic].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/status-update` - Updates

**Pulls from:**
- `/status-update` - Content

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **One ask**
- [ ] **Under 150 words**
- [ ] **Tone** fits
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `status-update` - Status
- `risk-register` - Escalations
