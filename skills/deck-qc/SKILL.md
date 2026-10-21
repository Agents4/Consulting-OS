---
name: deck-qc
description: "Production QC: consistency, formatting, titles, sources, spelling, the horizontal flow test, and file hygiene."
---

# Deck QC

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/deck-qc
```
Then provide:
1. **The deck**
2. **Template rules**
3. **Version and audience**

I will check a deck for story flow, title quality, number tie, formatting consistency, language, sources, and file hygiene, and return a fix list.

**Output:** Saved to `outputs/reviews/deck-qc-[deck]-[date].md`
**Time:** ~30 min

**When to use:** Before any deck leaves the team

**Phase:** All  |  **Framework source:** `~/.gemini/extensions/consulting-os/sub-agents/production-qc-reviewer.md`; `~/.gemini/extensions/consulting-os/context-library/engagement-model/06-deliverable-production-decks.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Decks | `outputs/decks/*.pptx`, `outputs/ghost-decks/*.md` | slide, title | Deck to check |
| Tie-out | `outputs/reviews/tie-out-*.md` | mismatch | Numbers status |
| QC Persona | `~/.gemini/extensions/consulting-os/sub-agents/production-qc-reviewer.md` | format, consistency | QC checklist |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If numbers mismatch -> Link to `number-tie-out`
- If story weak -> Link to `storyline`
- If partner review next -> Link to `review-panel`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/decks/*.pptx`, `outputs/ghost-decks/*.md`: Deck to check
- `outputs/reviews/tie-out-*.md`: Numbers status
- `~/.gemini/extensions/consulting-os/sub-agents/production-qc-reviewer.md`: QC checklist

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Decks:** [Page count and status]

**From Tie-out:** [Open mismatches]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Template rules
- Audience

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Version
**"Which version is final, and who freezes it?"**

Version control is part of QC.

---

## The Process

### Step 1: Horizontal test

Read only the titles; story must hold.

### Step 2: Slide by slide

One message; chart matches title; units; source.

### Step 3: Format

Fonts, sizes, colors, alignment, spacing, page numbers, footers.

### Step 4: Language

Spelling, tense, numbers format, abbreviations defined, no banned phrases.

### Step 5: File hygiene

Remove comments, hidden slides, metadata, internal notes; save PDF and editable.

---

## Structured Output Template

```markdown
# Deck QC: [Deck]

**Version:** [ ]  |  **Reviewer:** [ ]  |  **Date:** [ ]

## Verdict
[Ready / Fix then ready / Not ready]

## Findings
| # | Slide | Category | Issue | Fix | Owner | Done |
|---|---|---|---|---|---|---|

## Checks
- [ ] Horizontal flow
- [ ] Titles
- [ ] Numbers tie
- [ ] Formatting
- [ ] Language
- [ ] File hygiene
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/reviews/deck-qc-[deck]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decks/qc-[deck].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/review-panel` - Clean deck
- `/final-readout` - Frozen version

**Pulls from:**
- `/number-tie-out` - Tie status
- `/slide-draft` - Slides

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Horizontal test** run
- [ ] **Every slide** checked
- [ ] **Comments and hidden slides** removed
- [ ] **PDF and editable** saved
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `number-tie-out` - Tie numbers
- `review-panel` - Panel review
- `final-readout` - Final readout
