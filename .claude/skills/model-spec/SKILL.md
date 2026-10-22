---
name: model-spec
description: "Write the model specification before building: questions, structure, inputs, calculations, outputs, checks, owner."
disable-model-invocation: false
user-invocable: true
---

# Model Spec

## Quick Start

```
/model-spec
```
Then provide:
1. **The three questions** the model must answer
2. **Inputs and sources**
3. **Audience and decisions**

I will write a one-to-two page spec that a second person could build from, including tabs, input list, logic, outputs, checks, and the review plan.

**Output:** Saved to `outputs/models/model-spec-[model]-[date].md`
**Time:** ~25 min

**When to use:** Before any model is built, and when scope of a model changes

**Phase:** Mobilize through Develop  |  **Framework source:** `templates/model-spec-template.md`; `context-library/engagement-model/07-excel-modeling-standards.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Models | `context-library/models/*.md` | model, tab, input | Existing models to reuse |
| Fact Base | `outputs/analyses/fact-base-*.md` | baseline, definition | Baseline inputs |
| Initiative Sizing | `outputs/analyses/initiative-sizing-*.md` | uplift, ramp, cost | Logic to implement |
| Standards | `context-library/engagement-model/07-excel-modeling-standards.md` | inputs, checks, color | Build rules |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If spec is agreed -> Link to `model-build`
- If review needed -> Link to `model-audit`
- If scenarios needed -> Link to `scenario-sensitivity`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/models/*.md`: Existing models to reuse
- `outputs/analyses/fact-base-*.md`: Baseline inputs
- `outputs/analyses/initiative-sizing-*.md`: Logic to implement
- `context-library/engagement-model/07-excel-modeling-standards.md`: Build rules

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Models:** [Reusable modules]

**From Fact Base:** [Baseline numbers]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- The three questions
- Time horizon and granularity
- Owner and reviewer

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Questions
**"What three questions must this model answer?"**

A model with no stated question becomes a data dump.

### Question 2: The Granularity
**"Monthly, quarterly, or annual? By segment or total?"**

Granularity drives size and error risk.

---

## The Process

### Step 1: State the questions and audience

Who will use the outputs and for what decision.

### Step 2: Sketch the structure

Tabs and flow: Cover, Guide, Inputs, Calc, Scenarios, Outputs, Checks, Log.

### Step 3: List inputs

Each with unit, source, owner, scenario values.

### Step 4: Describe calculations

In words and in formula pattern per block.

### Step 5: Define outputs and checks

Outputs by slide; integrity and sense checks; owner; reviewer.

---

## Structured Output Template

```markdown
# Model Spec: [Model]

**Owner:** [ ]  |  **Reviewer:** [ ]  |  **Version:** [ ]

## Questions
1. [ ]

## Structure
| Tab | Purpose | Inputs from | Outputs to |
|---|---|---|---|

## Inputs
| Ref | Input | Unit | Low | Base | High | Source | Owner |
|---|---|---|---|---|---|---|---|

## Calculation Logic
[Blocks and formulas in words]

## Outputs
| Output | Used on slide | Definition |
|---|---|---|

## Checks
| Check | Test | Tolerance |
|---|---|---|

## Review Plan
[Independent review method and date]
```

---

## Output Format Options

Check **Preferred output formats** in `context-library/engagement-info-template.md`. Default is Office files (xlsx, pptx). If it is blank, ask once and record the answer. Full guide: `advanced/google-workspace-option.md`.

| | Excel (default) | Google Sheets |
|---|---|---|
| Spec | Same spec | Same spec; record platform in the header |
| Starter | `templates/model-starter-template.xlsx` | Google copy of the starter (`templates/google-workspace-starters.md`) |
| Build later with | `/model-build` | `/google-workspace-output` |

Choose Excel for heavy models, very large data, or VBA. Choose Sheets for co-editing, light to medium models, and trackers.

---

## Output Integration

### Where to Save

- Working draft: `outputs/models/model-spec-[model]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/models/model-spec-[model].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/model-build` - Spec to build
- `/model-audit` - Audit reference
- `/scenario-sensitivity` - Scenario design

**Pulls from:**
- `/fact-base` - Baselines
- `/initiative-sizing` - Logic

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Three questions** are stated
- [ ] **Inputs** have unit and source
- [ ] **Checks** are defined before building
- [ ] **Owner and reviewer** named
- [ ] **Starter template** is used: `templates/model-starter-template.xlsx`
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `model-build` - Build it
- `model-audit` - Audit it
- `scenario-sensitivity` - Stress it
