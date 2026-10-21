---
name: retrospective
description: "Run an engagement retrospective: outcomes, estimates vs actuals, handoff quality, tooling, learnings."
---

# Retrospective

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/retrospective
```
Then provide:
1. **Engagement outcome**
2. **Plan vs actuals**
3. **Team views**

I will draft the retrospective with outcome snapshot, what worked, what to change, calibration table, and actions with owners.

**Output:** Saved to `outputs/retros/retro-[engagement]-[date].md`
**Time:** ~25 min

**When to use:** Within two weeks of the final SteerCo, and at a mid-engagement checkpoint on longer work

**Phase:** Close  |  **Framework source:** `~/.gemini/extensions/consulting-os/templates/retrospective-template.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Status | `outputs/status-updates/*.md` | slip, risk | What went wrong when |
| Decisions | `context-library/decisions/*.md` | change | Scope changes |
| Reviews | `outputs/reviews/*.md` | finding | Quality issues |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If assets -> Link to `knowledge-capture`
- If skill improvement -> Link to `weekly-review`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/status-updates/*.md`: What went wrong when
- `context-library/decisions/*.md`: Scope changes
- `outputs/reviews/*.md`: Quality issues

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Status:** [Timeline]

**From Reviews:** [Quality]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Actual hours
- Client satisfaction

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Counterfactual
**"If we ran this again, what is the first thing we would change?"**

Surfaces the real lesson.

---

## The Process

### Step 1: Snapshot outcome



### Step 2: List what worked and why



### Step 3: List what to change and root cause



### Step 4: Fill calibration table

Plan vs actual.

### Step 5: Agree actions

Owner, date.

---

## Structured Output Template

```markdown
# Retrospective: [Engagement]

## Outcome
[ ]
## What Worked
[ ]
## What to Change
[ ]
## Calibration
| Item | Plan | Actual | Reason |
|---|---|---|---|
## Actions
| Action | Owner | Date |
|---|---|---|
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/retros/retro-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/engagements/retro-[engagement].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/knowledge-capture` - Assets
- `/proposal-draft` - Better estimates

**Pulls from:**
- `/handover-pack` - Closeout

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Root causes**, not blame
- [ ] **Calibration** table filled
- [ ] **Actions** have owners
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `knowledge-capture` - Capture assets
- `weekly-review` - Weekly review
