---
name: workplan-build
description: "Build a hypothesis-driven workplan: modules, tasks, owners, dates, dependencies, gates."
---

# Workplan Build

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/workplan-build
```
Then provide:
1. **Key question and hypotheses**
2. **Team and availability**
3. **Gate dates** (Kickoff, Diagnostic, Solutions, Final)

I will convert hypotheses into modules, tasks, owners, and dates, with data dependencies and the end-product of each module named.

**Output:** Saved to `outputs/workplans/workplan-[engagement]-[date].md`
**Time:** ~25 min

**When to use:** Week 1, and any time scope or dates change

**Phase:** Mobilize  |  **Framework source:** `~/.gemini/extensions/consulting-os/templates/workplan-template.md`; `~/.gemini/extensions/consulting-os/context-library/frameworks/hypothesis-driven-approach.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Hypotheses | `context-library/hypotheses/*.md`, `outputs/hypotheses/*.md` | H1, hypothesis, test | What must be tested and how |
| Issue Trees | `outputs/issue-trees/*.md` | branch, leaf, analysis | Modules and analyses |
| Team Roster | `context-library/team-roster-template.md` | owner, availability | Capacity by person |
| Data Requests | `outputs/data-requests/*.md` | owner, date, status | Data dependencies |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If analyses compete for time -> Link to `prioritize-analyses`
- If data blocks a module -> Link to `data-request`
- If risk to dates -> Link to `risk-register`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/hypotheses/*.md`, `outputs/hypotheses/*.md`: What must be tested and how
- `outputs/issue-trees/*.md`: Modules and analyses
- `context-library/team-roster-template.md`: Capacity by person
- `outputs/data-requests/*.md`: Data dependencies

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Hypotheses:** [List with tests]

**From Roster:** [Capacity]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Data arrival dates
- Client counterpart availability
- Gate dates

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Gates
**"What does the SteerCo need to see at each gate to say yes?"**

Work back from the gate, not forward from the data.

### Question 2: The Critical Path
**"Which analysis, if late, delays the next SteerCo?"**

That one gets the strongest owner.

---

## The Process

### Step 1: Define modules

One module per top-level issue-tree branch. Name the end-product (slide, model tab).

### Step 2: List tasks

Per module: analysis, data need, owner, effort in days, dependency.

### Step 3: Place on calendar

Back from each gate. Leave a review day before every SteerCo.

### Step 4: Mark the critical path

Highlight tasks whose delay moves a gate.

### Step 5: Agree with the EM

Walk through in 15 minutes; update weekly.

---

## Structured Output Template

```markdown
# Workplan: [Engagement]

## Gates
| Gate | Date | What the SteerCo decides |
|---|---|---|

## Modules and Tasks
| Module | Hypothesis | Task | Owner | Days | Depends on | End-product | Due |
|---|---|---|---|---|---|---|---|

## Critical Path
[Tasks]

## Risks to Dates
[Item, mitigation]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/workplans/workplan-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/engagements/workplan-[engagement].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/daily-plan` - Daily priorities
- `/weekly-plan` - Weekly goals
- `/status-update` - Progress reporting

**Pulls from:**
- `/hypothesis-draft` - Hypotheses to test
- `/issue-tree` - Modules
- `/data-request` - Data timing

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Every task** traces to a hypothesis
- [ ] **Every module** has a named end-product
- [ ] **Gate dates** have a review day before them
- [ ] **Owners** are not overloaded beyond 100%
- [ ] **Critical path** is marked
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `prioritize-analyses` - Rank competing analyses
- `data-request` - Send data asks
- `weekly-plan` - Plan the week
