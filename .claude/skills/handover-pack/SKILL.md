---
name: handover-pack
description: "Assemble the handover: model guide, data, deck masters, roadmap, owners, and a handover session plan."
disable-model-invocation: false
user-invocable: true
---

# Handover Pack

## Quick Start

```
/handover-pack
```
Then provide:
1. **The deliverables**
2. **Client owners**
3. **Handover date**

I will compile an index, model user guide, assumptions list, open items, and a handover session agenda so the client can run the work without us.

**Output:** Saved to `outputs/transition/handover-[engagement]-[date].md`
**Time:** ~30 min

**When to use:** Transition phase

**Phase:** Transition  |  **Framework source:** `context-library/engagement-model/03-engagement-lifecycle.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Models | `outputs/models/*.xlsx` | guide, log | Model and guide |
| Roadmap | `outputs/roadmaps/*.md` | owner | Owners |
| Compliance | `sub-agents/risk-compliance-advisor.md` | return, delete, confidential | Data return and deletion |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If retro -> Link to `retrospective`
- If knowledge -> Link to `knowledge-capture`
- If roadmap -> Link to `roadmap-build`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/models/*.xlsx`: Model and guide
- `outputs/roadmaps/*.md`: Owners
- `sub-agents/risk-compliance-advisor.md`: Data return and deletion

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Models:** [Files]

**From Roadmap:** [Owners]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Client system access
- Data deletion rules

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Owner
**"Who owns the model after we leave?"**

A model without an owner decays.

---

## The Process

### Step 1: Index deliverables



### Step 2: Write the model guide

Purpose, inputs, how to update, known limits.

### Step 3: List open items and owners



### Step 4: Plan the handover session

Walkthrough and Q&A.

### Step 5: Return or delete data

Per agreement.

---

## Structured Output Template

```markdown
# Handover Pack: [Engagement]

## Index
| Item | Location | Owner | Notes |
|---|---|---|---|

## Model Guide
[ ]

## Open Items
| Item | Owner | Date |
|---|---|---|

## Handover Session
[Agenda]

## Data Return and Deletion
[ ]
```

---

## Output Format Options

Check **Preferred output formats** in `context-library/engagement-info-template.md`. Default is Office files (xlsx, pptx). If it is blank, ask once and record the answer. Full guide: `advanced/google-workspace-option.md`.

For Google files: export .xlsx, .pptx, and PDF copies into the handover folder, move ownership or access to the client owner as agreed, remove team access, and record data return or deletion.

---

## Output Integration

### Where to Save

- Working draft: `outputs/transition/handover-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/engagements/handover-[engagement].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/retrospective` - Closeout

**Pulls from:**
- `/final-readout` - Final materials
- `/roadmap-build` - Owners

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Client owner** named for each item
- [ ] **Model guide** written
- [ ] **Data** return or deletion logged
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `retrospective` - Retro
- `knowledge-capture` - Capture assets
- `final-readout` - Readout
