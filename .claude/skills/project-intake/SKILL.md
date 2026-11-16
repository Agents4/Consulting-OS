---
name: project-intake
description: "Register a new project under a program: key question, the program hypothesis it serves, owner, gate, overlaps and dependencies, plus the register row and a draft card."
disable-model-invocation: false
user-invocable: true
---

# Project Intake

## Quick Start

```
/project-intake
```
Then provide:
1. **The project** in a sentence, and who owns it
2. **Why now**: the decision it supports and when
3. **What exists**: any notes, data or earlier work

I will turn it into a register row and a draft project card, check it against the projects already in the register, and name what the SteerCo needs to know.

**Output:** Saved to `outputs/programs/[program]/intake-[ID]-[date].md`
**Time:** ~15 min

**When to use:** Each time a new project joins a program, before any analysis starts

**Phase:** Mobilize (per project)  |  **Framework source:** `templates/project-register-template.md`, `templates/project-card-template.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Program | `context-library/engagements/[program]/program.md` | key question, hypotheses, scope, SteerCo | Program key question, program hypotheses (PH IDs), scope limits |
| Register | `context-library/engagements/[program]/register.md` | owner, key question, depends on | Existing projects, owners, overlaps |
| Cards | `context-library/engagements/[program]/projects/*.md` | numbers, risks | Numbers and risks the new project may share |
| Decisions | `context-library/decisions/*.md` | scope, definition | Agreed definitions the project must use |
| Stakeholders | `context-library/stakeholders/*.md` | sponsor, SteerCo | Who must hear about the new project |

If the program files are Google Docs and Sheets and are not on disk, ask the user to paste the register and the program brief.

**Context Priority:**
1. Program context FIRST (program brief, register, cards, decisions)
2. Project materials SECOND (notes, data the user supplies)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If the key question is loose -> Link to `problem-statement`
- If the first hypothesis needs work -> Link to `hypothesis-draft`
- If data is needed -> Link to `data-request`
- If a new risk appears -> Link to `risk-register`

---

## Step 0: Understanding What Already Exists

Before drafting, read the program brief and the register. Show:

### Internal Intelligence Summary

**From the Program:** [Key question, the hypotheses the project could serve]

**From the Register:** [Projects with the same owner, the same question, the same data, or an upstream dependency]

### Gaps in Knowledge

List what is missing before drafting, for example:
- No program hypothesis this project serves
- No named owner or no gate date
- A metric the project needs that the fact base defines differently

If the gaps are material, ask first. If minor, draft with marked assumptions.

---

## Step 1: Diagnostic Questions

Ask only what the files cannot answer:

### Question 1: The Hypothesis
**"Which program hypothesis does this project test, or what would it change in the program answer?"**

If there is no answer, say so and ask why the project exists. Work that traces to no hypothesis does not enter the register.

### Question 2: The Decision
**"What decision will the SteerCo make with this, and by when?"**

---

## The Process

### Step 1: Write the key question
One sentence with a decision and a date. Test: could a colleague say on that date whether it was answered?

### Step 2: Link it to the program
Name the program hypothesis (PH ID) it serves. If it serves none, propose a new program hypothesis or stop.

### Step 3: Check overlaps and dependencies
Compare against every register row. Flag same owner, same question, shared data, or one project feeding another. Name the other project by ID. Do not merge or drop projects. Raise it.

### Step 4: Set phase, gate and owner
One gate with a date. Flag an owner who already holds several open projects.

### Step 5: Draft the first hypothesis and its test
One hypothesis with a test and a date.

### Step 6: Draft the register row and the card
Use `templates/project-register-template.md` and `templates/project-card-template.md`. Mark every assumption.

### Step 7: Say who should hear first
Name stakeholders to pre-wire and whether the SteerCo needs a decision on scope.

---

## Structured Output Template

```markdown
# Project Intake: [ID] [Name]

**Answer first:** [Add, merge with P#, or hold. One sentence why.]

## Register row
| ID | Project | Owner | Phase | Project key question | Serves program hypothesis | Status | Why | Next gate and date | Depends on | Card | Updated |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Overlaps and dependencies
| With | Type | What to do |
|---|---|---|

## Draft card
[Filled from templates/project-card-template.md]

## Open questions
[Question, who can answer, by when]

## Who should hear first
[Names]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/programs/[program]/intake-[ID]-[date].md`
- When agreed: the user adds the row to the register and moves the card to `context-library/engagements/[program]/projects/[ID].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/project-card` - Keeps the card current
- `/program-rollup` - The new row appears in the program view
- `/hypothesis-draft` - First hypothesis

**Pulls from:**
- `/problem-statement` - Key question wording
- `/stakeholder-map` - Who to pre-wire

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Hypothesis link** named, or the gap raised
- [ ] **Overlaps** checked against every register row
- [ ] **Owner and gate** have names and dates
- [ ] **Assumptions** marked with IDs
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `project-card` - Keep the card current
- `program-rollup` - See all projects together
- `problem-statement` - Sharpen the key question
- `hypothesis-draft` - Build the hypothesis log
