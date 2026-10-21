---
name: data-request
description: "Create and track data requests to the client: what, why, format, owner, due date, with confidentiality basis."
---

# Data Request

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/data-request
```
Then provide:
1. **The analyses** that need data
2. **Known client systems and data owners**
3. **Confidentiality constraints**

I will draft a precise data request list (field-level where possible), a tracker, and chase messages, and log the permission basis for each pull.

**Output:** Saved to `outputs/data-requests/data-request-[engagement]-[date].md`
**Time:** ~15 min

**When to use:** Day 1 to 3, and whenever a new analysis needs data

**Phase:** Mobilize and Diagnose  |  **Framework source:** `~/.gemini/extensions/consulting-os/templates/data-request-tracker-template.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Workplan | `outputs/workplans/*.md` | task, depends on, data | What each analysis needs |
| Data | `context-library/data/*.md` | received, source, format | What already arrived |
| Stakeholders | `context-library/stakeholders/*.md` | data owner, IT, finance | Who owns each source |
| Compliance | `~/.gemini/extensions/consulting-os/sub-agents/risk-compliance-advisor.md` | confidential, PII, NDA | Handling rules |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If data is late -> Link to `status-update`
- If PII or sensitive data -> Link to `risk-compliance-advisor (sub-agent)`
- If data quality is poor -> Link to `data-exploration`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/workplans/*.md`: What each analysis needs
- `context-library/data/*.md`: What already arrived
- `context-library/stakeholders/*.md`: Who owns each source
- `~/.gemini/extensions/consulting-os/sub-agents/risk-compliance-advisor.md`: Handling rules

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Workplan:** [Analyses and their data needs]

**From Data folder:** [Received items]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Who owns each system
- Format and extract limits
- NDA and permitted storage

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Minimum
**"What is the smallest dataset that tests the hypothesis?"**

Smaller asks arrive faster.

### Question 2: The Fallback
**"If the data never arrives, what proxy do we use?"**

Decide now to avoid a blocked week.

---

## The Process

### Step 1: List the asks

One row per dataset: fields, period, granularity, format, why we need it.

### Step 2: Assign owners and dates

Counterpart owner and a due date with slack for cleaning.

### Step 3: Record the permission basis

Who approved sharing, where it is stored, sensitivity level.

### Step 4: Set a chase rhythm

Daily until in, with an escalation after 2 misses.

### Step 5: Log receipts and quality

Date received, completeness, issues, who validated.

---

## Structured Output Template

```markdown
# Data Request Tracker: [Engagement]

| # | Dataset | Fields / period | Why needed (hypothesis) | Client owner | Due | Format | Status | Quality notes | Permission basis |
|---|---|---|---|---|---|---|---|---|---|

## Chase Log
| Date | Item | Contact | Response | Next step |
|---|---|---|---|---|
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/data-requests/data-request-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/data/data-request-tracker.md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/data-exploration` - Received data to explore
- `/model-spec` - Data inputs
- `/status-update` - Data blockers

**Pulls from:**
- `/workplan-build` - Analyses needing data
- `/kickoff-plan` - Data owners

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Each ask** links to a hypothesis
- [ ] **Fields and periods** are specific
- [ ] **Owner and due date** are named
- [ ] **Permission basis** is recorded
- [ ] **Fallback** exists for critical items
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `data-exploration` - Profile the received data
- `model-spec` - Plan the model that uses it
- `risk-register` - Track data risk
