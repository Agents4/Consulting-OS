---
name: steerco-prep
description: "Prepare a Steering Committee: agenda, pre-read, pre-wires, decisions needed, Q&A rehearsal."
disable-model-invocation: false
user-invocable: true
---

# SteerCo Prep

## Quick Start

```
/steerco-prep
```
Then provide:
1. **SteerCo date and attendees**
2. **Decisions to be made**
3. **Content ready** (decks, models)

I will produce the SteerCo agenda, pre-wire plan, pre-read checklist, expected objections with answers, and a decision log update.

**Output:** Saved to `outputs/steerco/steerco-[date].md`
**Time:** ~30 min

**When to use:** One week before each SteerCo and again 3 days before

**Phase:** All gates  |  **Framework source:** `templates/steerco-agenda-and-status-template.md`; `context-library/engagement-model/05-cadence-and-handoffs.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Stakeholders | `outputs/stakeholder-maps/*.md` | pre-wire, stance | Who to align first |
| Decisions | `context-library/decisions/*.md` | open, pending | Decisions to take |
| Status | `outputs/status-updates/*.md` | progress, risk | Progress and blockers |
| Review | `outputs/reviews/*.md` | verdict | Readiness |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If pre-wire needed -> Link to `stakeholder-map`
- If deck not ready -> Link to `deck-qc`
- If decisions logged -> Link to `decision-doc`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/stakeholder-maps/*.md`: Who to align first
- `context-library/decisions/*.md`: Decisions to take
- `outputs/status-updates/*.md`: Progress and blockers
- `outputs/reviews/*.md`: Readiness

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Stakeholders:** [Pre-wire plan]

**From Decisions:** [Open decisions]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Who can veto
- Pre-read send date

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Decision
**"What must the SteerCo decide, and what is the fallback if they do not?"**

A SteerCo without a decision is a status meeting.

---

## The Process

### Step 1: Define decisions and outcomes

Per agenda item.

### Step 2: Plan pre-wires

Sponsor first, then members; 2 to 3 days ahead.

### Step 3: Send the pre-read

With a one-page summary.

### Step 4: Rehearse objections

Top ten questions with answers; assign who answers.

### Step 5: Capture outcomes

Decisions, actions, owners in the log within 24 hours.

---

## Structured Output Template

```markdown
# SteerCo Prep: [Date]

## Agenda
| Time | Item | Lead | Decision / output |
|---|---|---|---|

## Pre-wire Plan
| Person | What to align on | By | Who |
|---|---|---|---|

## Pre-read Checklist
- [ ] Sent [date]
- [ ] Executive summary
- [ ] Decisions listed

## Likely Objections
| Question | Answer | Who answers |
|---|---|---|

## After the Meeting
[Decisions, actions, owners]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/steerco/steerco-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/meetings/steerco-[date].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/decision-doc` - Decisions
- `/status-update` - Next steps

**Pulls from:**
- `/stakeholder-map` - Pre-wires
- `/exec-summary` - Pre-read

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Decisions** explicit per item
- [ ] **Pre-wires** done for each member
- [ ] **Pre-read** sent 2 to 3 days ahead
- [ ] **Objection list** rehearsed
- [ ] **Outcomes** logged
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `stakeholder-map` - Plan pre-wires
- `exec-summary` - Write pre-read
- `decision-doc` - Log decisions
