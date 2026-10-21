---
name: risk-register
description: Maintain the engagement risk register and recommendation risks, with heatmap and escalation rules.
disable-model-invocation: false
user-invocable: true
---

# Risk Register

## Quick Start

```
/risk-register
```
Then provide:
1. **New risks or signals**
2. **Current register** (if any)
3. **Gate dates**

I will update the register with likelihood, impact, early signals, mitigation, and owner, and recommend what to escalate.

**Output:** Saved to `outputs/status-updates/risk-register-[date].md`
**Time:** ~15 min

**When to use:** Weekly, and whenever a new risk appears

**Phase:** All  |  **Framework source:** `templates/risk-register-template.md`; `sub-agents/risk-compliance-advisor.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Risks | `context-library/decisions/risk-register*.md` | risk, score, owner | Current register |
| Status | `outputs/status-updates/*.md` | blocker, slip | Signals |
| Compliance | `sub-agents/risk-compliance-advisor.md` | confidential, conflict | Compliance risks |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If escalation -> Link to `status-update`
- If recommendation risks -> Link to `recommendation`
- If change risks -> Link to `change-plan`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/decisions/risk-register*.md`: Current register
- `outputs/status-updates/*.md`: Signals
- `sub-agents/risk-compliance-advisor.md`: Compliance risks

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Risks:** [Open risks and scores]

**From Status:** [New signals]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Early signals
- Owners

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Signal
**"What would we see first if this risk is materializing?"**

Early signals make risks manageable.

---

## The Process

### Step 1: Add or update risks

Category, description, likelihood, impact.

### Step 2: Score

Likelihood x impact; escalate at 15 or more.

### Step 3: Set mitigation and owner



### Step 4: Update the heatmap



### Step 5: Escalate

To EM or partner with a recommended action.

---

## Structured Output Template

```markdown
# Risk Register: [Engagement] - [Date]

| ID | Risk | Category | L | I | Score | Early signal | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|

## Escalate Now
[ ]

## Heatmap
[ ]
```

---

## Output Format Options

Check **Preferred output formats** in `context-library/engagement-info-template.md`. Default is Office files (xlsx, pptx). If it is blank, ask once and record the answer. Full guide: `advanced/google-workspace-option.md`.

Build the register as a CSV and upload it to create a Google Sheet. Add conditional formatting on the Score column (15 and above red, 8 to 14 amber).

---

## Output Integration

### Where to Save

- Working draft: `outputs/status-updates/risk-register-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decisions/risk-register-[engagement].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/status-update` - Risks
- `/steerco-prep` - Escalations

**Pulls from:**
- `/status-update` - Signals

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Each risk** has owner and mitigation
- [ ] **Scores >= 15** escalated
- [ ] **Early signals** named
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `status-update` - Report
- `change-plan` - Change risks
- `recommendation` - Delivery risks
