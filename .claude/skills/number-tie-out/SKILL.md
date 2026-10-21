---
name: number-tie-out
description: Tie every number on a deck to its source or model cell, log it, and flag mismatches before review.
disable-model-invocation: false
user-invocable: true
---

# Number Tie-Out

## Quick Start

```
/number-tie-out
```
Then provide:
1. **The deck** (pptx or text)
2. **The model and fact base**
3. **Version**

I will extract each number on each slide, trace it to a model cell or source, flag mismatches and rounding issues, and give you a signed tie-out log.

**Output:** Saved to `outputs/reviews/tie-out-[deck]-[date].md`
**Time:** ~30 min for a 20-page deck

**When to use:** Before every SteerCo and the final readout; after any model change

**Phase:** Develop through Transition  |  **Framework source:** `context-library/engagement-model/06-deliverable-production-decks.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Decks | `outputs/decks/*.pptx`, `outputs/ghost-decks/*.md` | slide, number, chart | Numbers to tie |
| Models | `outputs/models/*.xlsx` | Outputs tab, bridge | Source of numbers |
| Fact Base | `outputs/analyses/fact-base-*.md` | baseline | Reference numbers |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If mismatch is a model error -> Link to `model-audit`
- If numbers change -> Link to `status-update`
- If QC next -> Link to `deck-qc`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/decks/*.pptx`, `outputs/ghost-decks/*.md`: Numbers to tie
- `outputs/models/*.xlsx`: Source of numbers
- `outputs/analyses/fact-base-*.md`: Reference numbers

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Decks:** [Slide and number counts]

**From Models:** [Outputs]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Slide numbers listed in model outputs
- Rounding policy

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Rounding Rule
**"One decimal for $M, whole % for shares, or something else?"**

Consistency prevents fake mismatches.

---

## The Process

### Step 1: Extract numbers

Per slide: value, unit, label, chart or text.

### Step 2: Trace each

To model cell or document and page.

### Step 3: Compare

Value, unit, rounding, period, definition.

### Step 4: Flag and fix

Mismatch, rounding, label, or unit; owner to fix.

### Step 5: Sign off

Reviewer initials and date; freeze version.

---

## Structured Output Template

```markdown
# Tie-Out Log: [Deck]

**Deck version:** [ ]  |  **Model version:** [ ]  |  **Date:** [ ]

| Slide | Number | Unit | Source (file / tab / cell) | Source value | Match? | Issue | Owner | Fixed |
|---|---|---|---|---|---|---|---|---|

## Summary
Numbers checked: [ ]  |  Mismatches: [ ]  |  Fixed: [ ]

## Sign-off
[Name, date]
```

---

## Output Format Options

Check **Preferred output formats** in `context-library/engagement-info-template.md`. Default is Office files (xlsx, pptx). If it is blank, ask once and record the answer. Full guide: `advanced/google-workspace-option.md`.

For Google Slides decks, charts embedded as linked Sheets charts tie by construction to the model `Outputs` tab; click Update before tying. Titles, callouts, and tables are typed text, so tie each to an `Outputs` cell (for example `Outputs!C9`). Read slide text with the Slides read tool where available. For Excel and PowerPoint, tie to the xlsx cell as before.

---

## Output Integration

### Where to Save

- Working draft: `outputs/reviews/tie-out-[deck]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decks/tie-out-[deck].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/deck-qc` - Clean numbers
- `/final-readout` - Signed log

**Pulls from:**
- `/model-build` - Outputs
- `/fact-base` - Baselines

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Every number** is traced
- [ ] **Units and periods** match
- [ ] **Rounding rule** is consistent
- [ ] **Sign-off** recorded
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `deck-qc` - Production QC
- `model-audit` - Audit the model
- `final-readout` - Prepare the readout
