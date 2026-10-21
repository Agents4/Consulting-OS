---
name: hypothesis-draft
description: "Write and maintain a hypothesis log: statement, evidence for/against, test, confidence, status."
---

# Hypothesis Draft

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/hypothesis-draft
```
Then provide:
1. **The issue tree or the key question**
2. **What you already believe and why**
3. **Early evidence** (interviews, data, benchmarks)

I will turn the issue tree into falsifiable hypotheses, define the test that would kill each, and keep the log current as evidence arrives.

**Output:** Saved to `outputs/hypotheses/hypothesis-log-[engagement]-[date].md`
**Time:** ~20 min initial; ~10 min per update

**When to use:** After the issue tree, then after every new analysis or interview round

**Phase:** Mobilize through Recommend  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/frameworks/hypothesis-driven-approach.md`; `~/.gemini/extensions/consulting-os/templates/hypothesis-log-template.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Hypotheses | `context-library/hypotheses/*.md` | H1, status, confidence | Existing log |
| Issue Trees | `outputs/issue-trees/*.md` | leaf, branch | Where hypotheses attach |
| Analyses | `outputs/analyses/*.md` | finding, result, supports, contradicts | New evidence |
| Interviews | `outputs/interviews/*.md`, `context-library/interviews/*.md` | quote, theme | Qualitative evidence |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If a hypothesis is disproved -> Link to `day-one-answer`
- If tests need data -> Link to `data-request`
- If evidence is mixed -> Link to `skeptic (sub-agent)`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/hypotheses/*.md`: Existing log
- `outputs/issue-trees/*.md`: Where hypotheses attach
- `outputs/analyses/*.md`: New evidence
- `outputs/interviews/*.md`, `context-library/interviews/*.md`: Qualitative evidence

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Hypotheses:** [Open, confirmed, rejected counts]

**From Analyses:** [Latest evidence]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- The test that would prove it wrong
- Quantified thresholds

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Kill Test
**"What result would make you drop this hypothesis?"**

If nothing would, it is a belief, not a hypothesis.

### Question 2: The Threshold
**"What number turns this from 'probably' to 'proven'?"**

Set it before looking at the data.

---

## The Process

### Step 1: Write one hypothesis per leaf

Specific, falsifiable, with direction and size where possible.

### Step 2: Define the test

Analysis, data, threshold, owner, date.

### Step 3: Log evidence

For and against, with source and confidence.

### Step 4: Update status

Open, supported, partly supported, rejected; note what changed.

### Step 5: Reshape the answer

Update the Day-1 answer if a key hypothesis moves.

---

## Structured Output Template

```markdown
# Hypothesis Log: [Engagement]

| ID | Hypothesis | Branch | Test and threshold | Evidence for | Evidence against | Confidence | Status | Owner | Updated |
|---|---|---|---|---|---|---|---|---|---|

## Changes Since Last Update
[What moved and why]

## Impact on the Answer
[Does the Day-1 answer change?]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/hypotheses/hypothesis-log-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/hypotheses/hypothesis-log-[engagement].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/storyline` - Confirmed hypotheses become the storyline
- `/prioritize-analyses` - Tests to rank
- `/status-update` - Progress against hypotheses

**Pulls from:**
- `/issue-tree` - Leaf structure
- `/interview-synthesis` - Evidence
- `/ingest-materials` - New evidence and conflicts from client materials
- `/research-plan` - Sourced outside evidence, graded

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Each hypothesis** is falsifiable
- [ ] **Each test** has a threshold
- [ ] **Evidence** cites sources
- [ ] **Rejected hypotheses** are kept, with the reason
- [ ] **Day-1 answer** is checked against the log
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `day-one-answer` - Update the answer
- `storyline` - Build the storyline
- `skeptic` - Challenge the evidence
