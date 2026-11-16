---
name: project-card
description: "Create or refresh a one-page project card: key question, answer so far, hypotheses with confidence, numbers, decisions, risks, next gate, and the register row update."
---

# Project Card

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/project-card
```
Then provide:
1. **The project** (ID or name)
2. **What changed**: new notes, a decision, a result, a meeting
3. **Or say "refresh"** and I will read what exists and tell you what looks stale

I will update the card with only the changes you give me, keep it to one page, and write the matching register row.

**Output:** Saved to `outputs/programs/[program]/cards/[ID]-[slug]-[date].md`
**Time:** ~10 min

**When to use:** After a meeting, a decision, a new result, or at the weekly review. The card is the unit of knowledge for each project.

**Phase:** All  |  **Framework source:** `~/.gemini/extensions/consulting-os/templates/project-card-template.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Existing card | `context-library/engagements/[program]/projects/[ID].md`, `outputs/programs/[program]/cards/[ID]-*.md` | the project ID | The current card. Re-read it before any change |
| Register | `context-library/engagements/[program]/register.md` | the project ID | Owner, phase, status, depends on |
| Program | `context-library/engagements/[program]/program.md` | hypotheses, fact base | Program hypothesis IDs and the agreed numbers |
| Decisions | `context-library/decisions/*.md` | the project ID | Decisions already logged |
| Meetings | `outputs/meeting-notes/*.md` | the project ID | What was said since the last update |

If the card lives in Google Docs and is not on disk, ask the user to paste it.

**Context Priority:**
1. The existing card FIRST. Re-read it and apply only the requested change. Never regenerate it from scratch
2. Program context SECOND (register, program brief, decisions)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`)

**Cross-Skill Links:**
- If a decision was taken -> Link to `decision-doc`
- If a hypothesis changed -> Link to `hypothesis-draft`
- If a number changed -> Link to `number-tie-out`
- If a new risk appeared -> Link to `risk-register`

---

## Step 0: Understanding What Already Exists

Read the current card and the register row. Show:

### Internal Intelligence Summary

**From the Card:** [What it says now, and its last update date]

**From the Register:** [Status, phase, gate]

### Gaps in Knowledge

List what is missing, for example:
- A hypothesis with no confidence rating or no test date
- A number with no source, or one that differs from the program fact base
- A gate date that has passed with no outcome recorded

---

## Step 1: Diagnostic Questions

Ask only what the files cannot answer:

### Question 1: The Change
**"What changed since the last update, and how do you know?"**

### Question 2: The Status
**"Is the status still right, and what is the one reason?"**

---

## The Process

### Step 1: Apply only the change
Update the sections the change touches. Leave the rest as written.

### Step 2: Update the hypotheses
Set confidence (H, M or L) from the evidence and cite it. One remark is Low confidence. Move a settled hypothesis to supported or rejected and say what settled it.

### Step 3: Check the numbers
Compare each number with the program fact base. Where they differ, mark it. Do not pick one. Say who decides.

### Step 4: Set the status
Green, amber or red, with one reason. No reason, no status.

### Step 5: Keep it to one page
Move detail into an evidence doc and link it.

### Step 6: Write the register row
Produce the updated row so the user can paste it into the register.

---

## Structured Output Template

```markdown
# Project Card: [ID] [Name]

**What changed:** [One or two lines]

[Card body from ~/.gemini/extensions/consulting-os/templates/project-card-template.md]

## Register row update
| ID | Project | Owner | Phase | Status | Why | Next gate and date | Depends on | Updated |
|---|---|---|---|---|---|---|---|---|

## Stale or unsourced
[Fields not updated since the last SteerCo, numbers with no source]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/programs/[program]/cards/[ID]-[slug]-[date].md`
- When agreed: the user replaces the card in `context-library/engagements/[program]/projects/[ID].md` and updates the register row
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/program-rollup` - Reads every card
- `/status-update` - Project progress
- `/steerco-prep` - Decisions needed

**Pulls from:**
- `/meeting-notes` - What changed
- `/decision-doc` - Decisions
- `/hypothesis-draft` - Hypothesis updates

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Only the requested change** was applied
- [ ] **One page** or detail moved to a linked doc
- [ ] **Each hypothesis** has a confidence and a test date
- [ ] **Each number** has a source and a check against the fact base
- [ ] **Status** has a reason
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `project-intake` - Register a new project
- `program-rollup` - See all projects together
- `hypothesis-draft` - Maintain the hypothesis log
- `decision-doc` - Log a decision
