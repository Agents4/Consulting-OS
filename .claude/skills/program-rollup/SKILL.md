---
name: program-rollup
description: "Roll up the project register and cards into one program view: status, dependencies, cross-project risks, conflicting numbers, hypothesis tally, stale cards, and what the SteerCo must decide."
disable-model-invocation: false
user-invocable: true
---

# Program Rollup

## Quick Start

```
/program-rollup
```
Then provide:
1. **The program**
2. **The next SteerCo date**, if there is one
3. **Anything the cards do not show**, such as a decision taken in a hallway

I will read the register and every card, and give you the program view in one page with the answer first.

**Output:** Saved to `outputs/programs/[program]/rollup-[date].md`
**Time:** ~20 min

**When to use:** Weekly, before a SteerCo, and whenever a sponsor asks "where are we on the program"

**Phase:** All  |  **Framework source:** `templates/project-register-template.md`, `templates/project-card-template.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Program | `context-library/engagements/[program]/program.md` | key question, hypotheses, fact base, SteerCo | Program question, program hypotheses, agreed numbers |
| Register | `context-library/engagements/[program]/register.md` | status, depends on, owner, gate | One row per project |
| Cards | `context-library/engagements/[program]/projects/*.md` | hypotheses, numbers, risks, decisions | The detail behind each row |
| Decisions | `context-library/decisions/*.md` | open, owner | Decisions waiting on the SteerCo |
| Risks | `outputs/reviews/risk-register*.md`, `context-library/decisions/*.md` | risk | The existing risk register |

If the register is a Google Sheet and the cards are Docs and are not on disk, ask the user to paste them.

**Context Priority:**
1. Program context FIRST (program brief, register, cards)
2. Decisions and risks SECOND
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If numbers conflict -> Link to `number-tie-out`
- If a new cross-project risk appears -> Link to `risk-register`
- If a card is stale -> Link to `project-card`
- If the SteerCo is near -> Link to `steerco-prep`
- If the sponsor needs a note -> Link to `status-update`

---

## Step 0: Understanding What Already Exists

Read the register, then every card. Show:

### Internal Intelligence Summary

**From the Register:** [Count of projects by phase and status]

**From the Cards:** [Cards read, cards missing, cards older than the last SteerCo]

### Gaps in Knowledge

List what is missing before drafting, for example:
- A register row with no card, or a card with no register row
- A project that serves no program hypothesis
- An owner on several projects at once

---

## Step 1: Diagnostic Questions

Ask only what the files cannot answer:

### Question 1: The Audience
**"Who reads this, and what do they decide with it?"**

The sponsor needs decisions. The team needs dependencies.

---

## The Process

### Step 1: State the answer
Is the program on track to answer its key question? Say yes, partly or no, in one sentence, with the single biggest reason.

### Step 2: Tally status
Projects by phase and by status. List every amber and red project with its reason from its own card.

### Step 3: Map dependencies
List the dependency chains across projects. Name the one that sets the program's critical path. Flag a project waiting on another that is itself red.

### Step 4: Find cross-project risks
Risks that appear on two or more cards, or that sit on a dependency link. Give each an owner and a date, or flag the gap.

### Step 5: Find conflicting numbers
Compare the numbers tables across cards and the program fact base. Where one metric has two values, show both with sources. Do not pick one. Name who decides.

### Step 6: Tally the program hypotheses
For each program hypothesis, list the projects that test it and where each stands. Use only what the cards say. Mark a hypothesis with no project, or only Low confidence evidence, as untested.

### Step 7: List what the SteerCo must decide
Decisions from the cards, with owner and date, ranked by what they unblock.

### Step 8: Flag stale cards and missing information
Cards not updated since the last SteerCo and any gap in the register.

---

## Structured Output Template

```markdown
# Program View: [Program], [date]

**Answer first:** [On track, partly or off track, and why, in one or two sentences]

## SteerCo must decide
| Decision | Project | Owner | Needed by | What it unblocks |
|---|---|---|---|---|

## Status
| ID | Project | Owner | Phase | Status | Why | Next gate |
|---|---|---|---|---|---|---|

## Dependencies and critical path
[Chains, and the one that sets the pace]

## Cross-project risks
| Risk | Projects | Owner | Action and date |
|---|---|---|---|

## Conflicting numbers
| Metric | Value A (source, project) | Value B (source, project) | Who decides |
|---|---|---|---|

## Program hypotheses
| PH | Hypothesis | Projects testing it | Where it stands | Confidence |
|---|---|---|---|---|

## Stale cards and gaps
[Card, last update, what is missing]

## Assumptions
[A# list]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/programs/[program]/rollup-[date].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/steerco-prep` - Decisions and the pre-read
- `/status-update` - The sponsor note
- `/risk-register` - Cross-project risks

**Pulls from:**
- `/project-card` - Current cards
- `/project-intake` - New rows
- `/decision-doc` - Open decisions

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Answer** leads and names the single biggest reason
- [ ] **Every status** carries the reason from its own card
- [ ] **Conflicting numbers** are shown, not resolved
- [ ] **Hypothesis tally** uses only what the cards say
- [ ] **Stale cards** and missing rows are listed
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `project-card` - Keep each card current
- `project-intake` - Add a project
- `steerco-prep` - Prepare the SteerCo
- `status-update` - Write the sponsor note
- `risk-register` - Maintain the risk register
