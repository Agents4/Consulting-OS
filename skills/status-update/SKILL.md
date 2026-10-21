---
name: status-update
description: "Write the weekly status for the sponsor: progress, findings, risks, decisions needed, next steps."
---

# Status Update

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/status-update
```
Then provide:
1. **This week's progress**
2. **Risks and blockers**
3. **Decisions needed**

I will write a one-page weekly status in answer-first form that a sponsor can read in 90 seconds.

**Output:** Saved to `outputs/status-updates/status-[date].md`
**Time:** ~15 min

**When to use:** Weekly, before the sponsor touchpoint

**Phase:** All  |  **Framework source:** `~/.gemini/extensions/consulting-os/templates/steerco-agenda-and-status-template.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Workplan | `outputs/workplans/*.md` | owner, due, done | Progress |
| Hypotheses | `outputs/hypotheses/*.md` | status, change | Findings |
| Risks | `outputs/*/risk-register*.md` | score, owner | Risks |
| Meetings | `outputs/meeting-notes/*.md` | decision, action | Decisions and actions |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If risk is high -> Link to `risk-register`
- If decision needed -> Link to `decision-doc`
- If SteerCo coming -> Link to `steerco-prep`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/workplans/*.md`: Progress
- `outputs/hypotheses/*.md`: Findings
- `outputs/*/risk-register*.md`: Risks
- `outputs/meeting-notes/*.md`: Decisions and actions

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Workplan:** [Progress]

**From Hypotheses:** [What changed]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Client-side blockers

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Headline
**"If the sponsor read one line, what should it say?"**

Lead with it.

---

## The Process

### Step 1: Headline

One line: on track, at risk, or off track and why.

### Step 2: Findings

Three bullets with numbers.

### Step 3: Progress vs plan

Done, in progress, slipped.

### Step 4: Risks and blockers

With owner and ask.

### Step 5: Decisions and next week

Who, what, by when.

---

## Structured Output Template

```markdown
# Weekly Status: [Engagement] - [Date]

**Headline:** [ ]  |  **RAG:** [G/A/R]

## Findings
- [ ]

## Progress vs Plan
| Item | Status | Note |
|---|---|---|

## Risks and Blockers
| Item | Owner | Ask |
|---|---|---|

## Decisions Needed
| Decision | By whom | By when |
|---|---|---|

## Next Week
- [ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/status-updates/status-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/meetings/status-[date].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/steerco-prep` - Progress
- `/weekly-review` - Input

**Pulls from:**
- `/workplan-build` - Progress
- `/risk-register` - Risks

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Headline** states RAG and why
- [ ] **Findings** have numbers
- [ ] **Asks** have owners and dates
- [ ] **Under one page**
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `risk-register` - Update risks
- `decision-doc` - Log decisions
- `steerco-prep` - Prep SteerCo
