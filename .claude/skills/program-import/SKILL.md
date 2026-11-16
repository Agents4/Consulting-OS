---
name: program-import
description: "Bring existing projects into a program from the documents they already have: charters, plans, status reports, decks, trackers and notes. Drafts a card and register row per project, with every field sourced and every gap marked."
disable-model-invocation: false
user-invocable: true
---

# Program Import

## Quick Start

```
/program-import
```
Then provide (all optional):
1. **The program** and, if it exists, its key question and hypotheses
2. **Where the project materials are**: a folder, a list of files, or pasted text. One project or many
3. **Projects to include or skip**, and any owner names you already know

I will inventory what exists, group it by project, draft a card and a register row for each project from the documents alone, and list what is unknown and who could answer it. Nothing is invented to fill a field.

**Output:** Saved to `outputs/programs/[program]/import-[date]/` (plan, one card draft per project, a consolidated register draft, a source log, and open questions by owner)
**Time:** ~10 min per project, plus ~20 min for the cross-project pass

**When to use:** When projects already exist and you want them in the program without retyping them. Use `/project-intake` for a project that does not exist yet.

**Phase:** Mobilize (program set-up)  |  **Framework source:** `templates/project-register-template.md`, `templates/project-card-template.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Program | `context-library/engagements/[program]/program.md` | key question, hypotheses, scope, fact base | Program question and PH IDs, if they exist |
| Register | `context-library/engagements/[program]/register.md` | project IDs, owners | Projects already registered, so nothing is duplicated |
| Project materials | the folder the user names; default `context-library/client-materials/` | charter, plan, status, milestone, owner, risk, budget | What each project says about itself |
| Data | `context-library/data/` | the project name | Numbers the projects cite |
| Fact base | `outputs/analyses/fact-base*.md`, `context-library/data/` | metric names | The agreed numbers to compare against |
| Stakeholders | `context-library/stakeholders/*.md` | owner, sponsor | Who owns what |

If the materials are in Drive, a project tool, or another connector, ask before using it on client data and confirm it is approved for this. If a Google file is not readable, ask the user to paste it.

**Context Priority:**
1. The project's own documents FIRST. They are the only source for what the project says
2. Program context SECOND (program brief, register, fact base)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If files conflict on a number -> Link to `ingest-materials` and `fact-base`
- If a card needs polish -> Link to `project-card`
- If a program hypothesis is missing -> Link to `hypothesis-draft`
- If an owner or sponsor is unknown -> Link to `stakeholder-map`
- If cross-project risks appear -> Link to `risk-register`
- When the register is ready -> Link to `program-rollup`

---

## Step 0: Understanding What Already Exists

Before reading in depth, list what is in the materials and what is already in the program. Show:

### Internal Intelligence Summary

**From the Materials:** [Files found, grouped by the project each appears to belong to, and files that fit no project]

**From the Program:** [Projects already registered, program hypotheses, or "none yet"]

### Gaps in Knowledge

List what is missing before drafting, for example:
- Files with no clear project
- A project with only one document
- No program question or hypotheses to map projects to
- A project mentioned in several files under different names

If the gaps are material, ask first. If minor, draft and mark them.

---

## Step 1: Diagnostic Questions

Ask only what the files cannot answer:

### Question 1: The Scope
**"Which projects count as part of this program, and which are adjacent?"**

Do not guess the boundary. A project outside the program does not get a row.

### Question 2: The Source of Truth
**"When two documents disagree, which one is the system of record for status, dates and owners?"**

---

## The Process

### Step 1: Inventory
List every file with its type, date and the project it belongs to. Group files by project. Put anything that fits none in an "unassigned" list for the user. Confirm the project list with the user before drafting cards. For a large set, work in batches the user approves.

### Step 2: Resolve the project list
Merge names that refer to one project, and say how you matched them. Flag any pair you are unsure about instead of merging it. Assign provisional IDs (P1, P2) unless the program already has a scheme.

### Step 3: Extract for each project
For each project, fill the card from its documents only. Record the source file and location for every field.

- **Key question:** use the document's own wording if it states one. If it does not, propose one from the project's goal and mark it Proposed.
- **Owner, phase, gate and dates:** copy what the documents say, with the document date. If sources disagree, show both.
- **Status:** copy the status and date the source states. Do not assign green, amber or red yourself. If none is stated, write Unknown.
- **Hypotheses:** list those the documents state. If the project has none, you may list implied ones from its goals and mark each Implied, Low confidence, and ask the owner to confirm.
- **Numbers:** table each figure with its source, date and whether it matches the program fact base.
- **Decisions, risks and dependencies:** extract those the documents state, with owner and date where given.

### Step 4: Map to the program
If the program has hypotheses, propose which one each project serves and say why. The user approves each link. If the program has no hypotheses, group the projects by the questions they ask and propose draft program hypotheses, marked Proposed. A project that fits none stays unmapped and goes to the owner with the question: why are we doing it?

### Step 5: Cross-project pass
Across all imported projects, find:
- Overlaps: same goal, owner, data or deliverable
- Dependencies named in one document and missing from the other
- The same metric with different values, shown with both sources and not resolved
- Owners on many projects at once
- Projects with no activity or update since a date the user sets, or the oldest source for each

### Step 6: Grade each project
Give each project a completeness note: which fields are sourced, which are Unknown, and how old the newest source is. Rank the projects by how much work is needed before the card is usable. This is a reading of the documents, not a judgment on the project.

### Step 7: List open questions by owner
Every Unknown becomes a question with a name, so the owner can answer it. Do not ask the user to guess.

### Step 8: Propose, do not promote
Nothing goes into `context-library/` until the user approves it, one project at a time. The user moves agreed files there by hand.

---

## Structured Output Template

```markdown
# Program Import: [Program], [date]

**Answer first:** [N projects found from M files. X have enough to be usable now, Y need owner input, Z files fit no project.]

## Import plan
| ID | Project (and other names) | Files used | Newest source | Completeness | Needs |
|---|---|---|---|---|---|

## Register draft
[Rows from templates/project-register-template.md. Every unsourced cell reads Unknown.]

## Program mapping
| Project | Proposed program hypothesis | Why | Approve? |
|---|---|---|---|

## Cross-project findings
| Type | Projects | Detail | Who decides |
|---|---|---|---|

## Open questions by owner
| Owner | Project | Question | Needed for |
|---|---|---|---|

## Unassigned files
[File, why it did not fit]

## Source log
| Project | Field | Value | Source file and location | Date |
|---|---|---|---|---|

## Assumptions
[A# list]
```

Each project card draft is saved as its own file, using `templates/project-card-template.md`, with Proposed, Implied and Unknown marked in place.

---

## Output Integration

### Where to Save

- Working drafts: `outputs/programs/[program]/import-[date]/` (`import-plan.md`, `register-draft.md`, `cards/[ID]-[slug].md`, `source-log.md`, `open-questions.md`)
- When approved: the user moves each card to `context-library/engagements/[program]/projects/[ID].md` and merges the register rows into `register.md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/project-card` - Keeps each imported card current
- `/program-rollup` - Reads the new register and cards
- `/hypothesis-draft` - Program hypotheses
- `/risk-register` - Cross-project risks

**Pulls from:**
- `/ingest-materials` - Digests of the same files, if already run
- `/fact-base` - The agreed numbers
- `/stakeholder-map` - Owners and sponsors

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Every field** has a source file and location, or reads Unknown
- [ ] **Nothing is invented**: key questions, hypotheses and statuses not in the documents are marked Proposed, Implied or Unknown
- [ ] **Merged project names** show how they were matched; unsure pairs are flagged, not merged
- [ ] **Status** is copied from a source, with its date, never assigned
- [ ] **Conflicting numbers** are shown with both sources and not resolved
- [ ] **Program links** are proposals the user approves
- [ ] **Every Unknown** has a named owner and a question
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `project-intake` - Register a project that is new
- `project-card` - Keep each card current
- `program-rollup` - See all projects together
- `ingest-materials` - Digest files and reconcile the fact base
- `hypothesis-draft` - Build the program hypotheses
