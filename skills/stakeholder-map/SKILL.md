---
name: stakeholder-map
description: "Map client stakeholders by influence, stance, and what they need, with a pre-wire and engagement plan."
---

# Stakeholder Map

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/stakeholder-map
```
Then provide:
1. **The org context** (org chart, who is in the room)
2. **What you have heard** about each person
3. **The decision** that needs their support

I will map each stakeholder's power, stance, and interests, then give a pre-wire sequence and the first ask per person.

**Output:** Saved to `outputs/stakeholder-maps/stakeholder-map-[engagement]-[date].md`
**Time:** ~20 min

**When to use:** Before kickoff and again before each SteerCo

**Phase:** Mobilize and ongoing  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/frameworks/change-and-implementation.md`; `context-library/client-stakeholder-template.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Stakeholders | `context-library/stakeholders/*.md` | role, stance, influence | Existing profiles |
| Meetings | `context-library/meetings/*.md` | concern, objection, supports, blocks | Signals from past meetings |
| Interviews | `context-library/interviews/*.md` | quote, resistance, support | What stakeholders said about the change |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If resistance is strong -> Link to `change-plan`
- If a decision needs pre-wiring -> Link to `steerco-prep`
- If a stakeholder is the CFO -> Link to `client-cfo (sub-agent)`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/stakeholders/*.md`: Existing profiles
- `context-library/meetings/*.md`: Signals from past meetings
- `context-library/interviews/*.md`: What stakeholders said about the change

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Stakeholders:** [Known profiles and stance]

**From Meetings:** [Signals of support and resistance]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Who actually holds the budget
- Informal influencers
- Prior failed initiatives

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Real Decider
**"Who can say no after the SteerCo says yes?"**

Often a finance or legal approver outside the room.

### Question 2: The Threat
**"Whose role or budget changes if our answer is accepted?"**

Those people need a different message and earlier contact.

---

## The Process

### Step 1: List every stakeholder

Name, role, reporting line, role in the decision.

### Step 2: Score influence and stance

Influence 1 to 5; stance from champion to opponent; evidence for each.

### Step 3: Capture interests and fears

What they win, what they lose, what they have said.

### Step 4: Sequence pre-wires

Order by influence and dependency. Assign a messenger per person.

### Step 5: Set the first ask

One concrete request per stakeholder with a date.

---

## Structured Output Template

```markdown
# Stakeholder Map: [Engagement]

| Name | Role | Influence (1-5) | Stance | Interests / fears | Evidence | Messenger | First ask |
|---|---|---|---|---|---|---|---|

## Pre-wire Sequence
1. [Person] - [what to align on] - [by when]

## Watch List
[People whose stance may shift and why]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/stakeholder-maps/stakeholder-map-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/stakeholders/stakeholder-map-[engagement].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/steerco-prep` - Pre-wire plan
- `/change-plan` - Change readiness input
- `/kickoff-plan` - Attendee strategy

**Pulls from:**
- `/interview-synthesis` - Stakeholder quotes
- `/meeting-notes` - Signals

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Every row** has evidence, not rumor
- [ ] **Opponents** have a specific ask and messenger
- [ ] **Pre-wire order** is explicit
- [ ] **Confidentiality**: no personal judgments that would embarrass if leaked
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `steerco-prep` - Prepare SteerCo with pre-wires
- `change-plan` - Plan adoption
- `interview-guide` - Interview stakeholders
