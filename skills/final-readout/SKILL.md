---
name: final-readout
description: "Prepare the final SteerCo readout: outline, pages, Q&A rehearsal, pre-readout checklist, decisions."
---

# Final Readout

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/final-readout
```
Then provide:
1. **Recommendation and storyline**
2. **Audience and date**
3. **Decks and models status**

I will build the readout outline, the page-by-page checklist, the red-team Q&A, and the pre-readout readiness list.

**Output:** Saved to `outputs/decks/final-readout-[engagement]-[date].md`
**Time:** ~40 min

**When to use:** Two weeks before the final SteerCo

**Phase:** Recommend  |  **Framework source:** `~/.gemini/extensions/consulting-os/templates/final-readout-outline-template.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Storyline | `outputs/storylines/*.md` | governing thought | Structure |
| Recommendation | `outputs/recommendations/*.md` | ask | Content |
| Reviews | `outputs/reviews/*.md` | verdict | Readiness |
| Tie-out | `outputs/reviews/tie-out-*.md` | mismatch | Number status |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If numbers -> Link to `number-tie-out`
- If QC -> Link to `deck-qc`
- If handover -> Link to `handover-pack`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/storylines/*.md`: Structure
- `outputs/recommendations/*.md`: Content
- `outputs/reviews/*.md`: Readiness
- `outputs/reviews/tie-out-*.md`: Number status

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Storyline:** [Structure]

**From Reviews:** [Open issues]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Audience Q&A
- Client lead speaking role

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Decision
**"What decision do we want at the end of the meeting?"**

The ask drives the structure.

---

## The Process

### Step 1: Build the outline

Nine sections per the template.

### Step 2: Assign pages and owners



### Step 3: Run reviews

Partner, QC, tie-out, model audit.

### Step 4: Rehearse Q&A

Top ten questions.

### Step 5: Freeze and stage

PDF and editable master; handover pack.

---

## Structured Output Template

```markdown
# Final Readout: [Engagement]

## Outline
| Section | Pages | Content | Owner | Status |
|---|---|---|---|---|

## Q&A (Top 10)
| Question | Answer | Who |
|---|---|---|

## Readiness Checklist
- [ ] Sponsor pre-wired
- [ ] Pre-read sent
- [ ] Numbers tied
- [ ] Model audited
- [ ] Partner and QC review
- [ ] Version frozen
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/decks/final-readout-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decks/final-readout-[engagement].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/handover-pack` - Final materials
- `/retrospective` - Outcome

**Pulls from:**
- `/exec-summary` - Summary
- `/roadmap-build` - Roadmap

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Decision** is explicit
- [ ] **Numbers tied**
- [ ] **Model audited**
- [ ] **Q&A rehearsed**
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `handover-pack` - Hand over
- `deck-qc` - QC
- `steerco-prep` - SteerCo
