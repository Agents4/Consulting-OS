---
name: slide-draft
description: "Draft a single slide: action title, chart choice, layout, callouts, source line, and speaker notes."
disable-model-invocation: false
user-invocable: true
---

# Slide Draft

## Quick Start

```
/slide-draft
```
Then provide:
1. **The message** of the slide
2. **The data or analysis** behind it
3. **Audience**

I will draft the slide spec (and a pptx page when asked) with the title, chart, annotations, takeaway box, and source line, following one-message-per-slide.

**Output:** Saved to `outputs/decks/slide-[topic]-[date].md`
**Time:** ~10 min per slide

**When to use:** Turning an analysis into a page

**Phase:** Develop and Recommend  |  **Framework source:** `context-library/engagement-model/06-deliverable-production-decks.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Ghost Deck | `outputs/ghost-decks/*.md` | page, title, chart | What was planned |
| Analyses | `outputs/analyses/*.md` | finding, so-what | Evidence |
| Decks | `context-library/decks/*.md` | template, style | House style |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If numbers must tie -> Link to `number-tie-out`
- If chart data from model -> Link to `model-build`
- If QC -> Link to `deck-qc`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/ghost-decks/*.md`: What was planned
- `outputs/analyses/*.md`: Evidence
- `context-library/decks/*.md`: House style

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Ghost Deck:** [Planned page]

**From Analyses:** [Findings]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Final numbers
- Template

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The So-What
**"What do you want the reader to conclude in 5 seconds?"**

That sentence is the title.

---

## The Process

### Step 1: Write the action title

Full sentence; verb; so-what; number.

### Step 2: Pick the chart

Comparison: bar; trend: line; composition: stacked or waterfall; relationship: scatter; process: flow.

### Step 3: Design the layout

Chart left, takeaway right; or chart full width with callouts.

### Step 4: Annotate

Highlight the one bar or point that proves the title; remove the rest of the noise.

### Step 5: Add source, units, and notes

Source line, units, date; speaker notes if presented.

---

## Structured Output Template

```markdown
# Slide: [Title]

**Action title:** [ ]
**Chart:** [Type, axes, units, highlights]
**Layout:** [ ]
**Callouts:** [ ]
**Takeaway box:** [ ]
**Source:** [ ]
**Speaker notes:** [ ]
**Data location:** [model tab / cell]
```

---

## Output Format Options

Check **Preferred output formats** in `context-library/engagement-info-template.md`. Default is Office files (xlsx, pptx). If it is blank, ask once and record the answer. Full guide: `advanced/google-workspace-option.md`.

In Google Slides: slides never shrink text, so size boxes and cut words before placing. Titles hold about two lines. Put the chart label in a text box above a linked chart. Callouts and growth arrows are text boxes and shapes drawn over the chart. Logos and images cannot be inserted from a chat file; copy them from the template.

---

## Output Integration

### Where to Save

- Working draft: `outputs/decks/slide-[topic]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decks/slide-[topic].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/deck-qc` - Slide for QC
- `/number-tie-out` - Numbers to tie

**Pulls from:**
- `/ghost-deck` - Plan
- `/scenario-sensitivity` - Charts

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Title** is a full sentence
- [ ] **One message** only
- [ ] **Chart** supports the title
- [ ] **Source and units** present
- [ ] **Passes** the horizontal read test
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `ghost-deck` - See the whole deck
- `deck-qc` - QC
- `number-tie-out` - Tie numbers
