---
name: ghost-deck
description: "Create a ghost deck: empty slides with action titles, chart sketches, and data needs, before analysis finishes."
disable-model-invocation: false
user-invocable: true
---

# Ghost Deck

## Quick Start

```
/ghost-deck
```
Then provide:
1. **The storyline**
2. **Template and page budget**
3. **Data status**

I will produce a page-by-page ghost deck with an action title, chart type, axes, expected so-what, data source, and status tag per page.

**Output:** Saved to `outputs/ghost-decks/ghost-deck-[engagement]-[date].md`
**Time:** ~35 min

**When to use:** As soon as the storyline exists; before analyses are final

**Phase:** Develop and Recommend  |  **Framework source:** `templates/ghost-deck-template.md`; `templates/ghost-deck-starter.pptx`; `context-library/engagement-model/06-deliverable-production-decks.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Storyline | `outputs/storylines/*.md` | page, title, key line | Page list |
| Decks | `context-library/decks/*.md` | template, format, sample | Client or firm template rules |
| Frameworks | `context-library/engagement-model/06-deliverable-production-decks.md` | action title, chart choice | Slide rules |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If pages need building -> Link to `slide-draft`
- If tie out -> Link to `number-tie-out`
- If model needed -> Link to `model-spec`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/storylines/*.md`: Page list
- `context-library/decks/*.md`: Client or firm template rules
- `context-library/engagement-model/06-deliverable-production-decks.md`: Slide rules

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Storyline:** [Page list]

**From Decks:** [Template rules]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Template
- Page limits
- Chart preferences

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Page Budget
**"How many main pages and how many appendix pages?"**

Page limits force priorities.

---

## The Process

### Step 1: List the pages

From dot-dash, in order.

### Step 2: Write the action title

A full sentence with the so-what and a number if known.

### Step 3: Choose the chart

Type, axes, units, highlight; see chart choices in the production guide.

### Step 4: List data and owner

Model tab or source and who delivers it.

### Step 5: Tag status

Ghost, Draft, Tied, Final.

---

## Structured Output Template

```markdown
# Ghost Deck: [Engagement]

| # | Section | Action title | Chart / visual | Axes and units | Source (model tab / file) | Owner | Status | Due |
|---|---|---|---|---|---|---|---|---|

## Data Needs
[ ]

## Production Notes
[Template, fonts, think-cell, page limit]
```

---

## Output Format Options

Check **Preferred output formats** in `context-library/engagement-info-template.md`. Default is Office files (xlsx, pptx). If it is blank, ask once and record the answer. Full guide: `advanced/google-workspace-option.md`.

| | PowerPoint (default) | Google Slides |
|---|---|---|
| Start | `templates/ghost-deck-starter.pptx` | Google copy of the starter |
| Build | pptxgenjs or python-pptx | Slides editor builds the pages; or I hand you the page spec |
| Charts | Native pptx charts | Charts built on the Sheet `Outputs` tab, embedded as linked charts |
| Status tag | Text box on page | Text box on page |

Run `/google-workspace-output` for the Slides route.

---

## Output Integration

### Where to Save

- Working draft: `outputs/ghost-decks/ghost-deck-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decks/ghost-deck-[engagement].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/slide-draft` - Pages to build
- `/number-tie-out` - Numbers to tie
- `/workplan-build` - Production tasks

**Pulls from:**
- `/storyline` - Pages
- `/model-build` - Data

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Every page** has an action title
- [ ] **Chart** type is chosen and justified
- [ ] **Source** per page
- [ ] **Status tag** per page
- [ ] **Page count** within budget
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `slide-draft` - Build pages
- `deck-qc` - QC the deck
- `number-tie-out` - Tie numbers
