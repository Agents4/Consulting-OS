---
name: decision-doc
description: "Log a decision: context, options, choice, owner, date, and what would reverse it."
---

# Decision Doc

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/decision-doc
```
Then provide:
1. **The decision** taken or needed
2. **Options and who decided**
3. **Date and forum**

I will write a one-page decision record and update the decision log so scope, definitions, and approvals have a paper trail.

**Output:** Saved to `outputs/decisions/decision-[topic]-[date].md`
**Time:** ~10 min

**When to use:** After any SteerCo, scope change, definition agreement, or model assumption sign-off

**Phase:** All  |  **Framework source:** `~/.gemini/extensions/consulting-os/templates/decision-log-template.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Decisions | `context-library/decisions/*.md` | decision, agreed, owner | Existing log |
| Meetings | `outputs/meeting-notes/*.md` | decided, agreed, approved | Where it was taken |
| Problem Statement | `outputs/problem-statements/*.md` | scope | Scope anchor |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If scope changed -> Link to `workplan-build`
- If definition agreed -> Link to `fact-base`
- If SteerCo outcome -> Link to `steerco-prep`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/decisions/*.md`: Existing log
- `outputs/meeting-notes/*.md`: Where it was taken
- `outputs/problem-statements/*.md`: Scope anchor

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Decisions:** [Open and closed decisions]

**From Meetings:** [Context]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Who owns the decision
- Reversal conditions

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Owner
**"Who has the authority to make this decision?"**

A decision by the wrong person will be reopened.

---

## The Process

### Step 1: State the decision

One sentence.

### Step 2: List options considered

Why rejected.

### Step 3: Record owner, date, forum



### Step 4: Record the reversal trigger

What would reopen it.

### Step 5: Update the log and notify

Send to affected people.

---

## Structured Output Template

```markdown
# Decision: [Topic]

**ID:** [D#]  |  **Date:** [ ]  |  **Forum:** [ ]  |  **Owner:** [ ]

## Decision
[ ]

## Context
[ ]

## Options Considered
| Option | Why not chosen |
|---|---|

## Impact
[Scope, timeline, model, deck]

## Reversal Trigger
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/decisions/decision-[topic]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decisions/decision-[topic].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/workplan-build` - Scope changes
- `/fact-base` - Definitions

**Pulls from:**
- `/steerco-prep` - Outcomes
- `/meeting-notes` - Context

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Owner** has authority
- [ ] **Reversal trigger** stated
- [ ] **Impact** listed
- [ ] **Log** updated
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `steerco-prep` - SteerCo outcomes
- `workplan-build` - Update plan
- `fact-base` - Update definitions
