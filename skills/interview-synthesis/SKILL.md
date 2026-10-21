---
name: interview-synthesis
description: "Synthesize interview notes into themes, quotes, and hypothesis updates with strength of evidence."
---

# Interview Synthesis

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/interview-synthesis
```
Then provide:
1. **Interview notes** (paste or files in `context-library/interviews/`)
2. **Hypotheses** being tested
3. **Number and mix of interviewees**

I will cluster themes, count support, pull verbatim quotes, flag contradictions, and say what changes in the hypothesis log.

**Output:** Saved to `outputs/research-synthesis/interview-synthesis-[round]-[date].md`
**Time:** ~25 min for 8 to 12 interviews

**When to use:** After each interview round, before the next SteerCo

**Phase:** Diagnose  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/frameworks/interviewing-playbook.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Interviews | `context-library/interviews/*.md`, `outputs/interviews/*.md` | quote, theme, pain, driver | Raw notes |
| Hypotheses | `outputs/hypotheses/*.md` | H1, test | What to update |
| Stakeholders | `context-library/stakeholders/*.md` | role, stance | Weight by role |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If themes conflict with data -> Link to `root-cause-analysis`
- If quote needs a slide -> Link to `slide-draft`
- If stance shifts -> Link to `stakeholder-map`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/interviews/*.md`, `outputs/interviews/*.md`: Raw notes
- `outputs/hypotheses/*.md`: What to update
- `context-library/stakeholders/*.md`: Weight by role

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Interviews:** [Count, mix, themes]

**From Hypotheses:** [Open tests]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Missing segments
- Single-source claims

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Weight
**"Which interviews should count more, and why?"**

Frontline vs executive views may diverge on purpose.

### Question 2: The Surprise
**"What did you hear that you did not expect?"**

Surprises often become the insight.

---

## The Process

### Step 1: Code the notes

Tag each statement with a theme, interviewee type, and fact vs opinion.

### Step 2: Count and cluster

Number of interviewees per theme and per segment.

### Step 3: Pick verbatim quotes

Two per major theme, anonymized unless agreed.

### Step 4: Flag contradictions

Between groups, and between interviews and data.

### Step 5: Update hypotheses

Supported, weakened, or new; list the follow-ups.

---

## Structured Output Template

```markdown
# Interview Synthesis: [Round]

**Interviews:** [n]  |  **Mix:** [ ]  |  **Dates:** [ ]

## Headline
[Three-sentence so-what]

## Themes
| Theme | Interviewees (n of N) | Segments | Strength | Representative quote |
|---|---|---|---|---|

## Contradictions
[ ]

## Hypothesis Impact
| Hypothesis | Change | Evidence |
|---|---|---|

## Follow-ups
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/research-synthesis/interview-synthesis-[round]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/research/interview-synthesis-[round].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/hypothesis-draft` - Evidence
- `/slide-draft` - Quotes for slides
- `/change-plan` - Voice of employees

**Pulls from:**
- `/interview-guide` - Guide used
- `/stakeholder-map` - Roles

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **n of N** shown for each theme
- [ ] **Quotes** are verbatim and anonymized
- [ ] **Opinions** are not presented as facts
- [ ] **Contradictions** are listed
- [ ] **Hypothesis log** is updated
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `hypothesis-draft` - Update the log
- `root-cause-analysis` - Test causes
- `storyline` - Use in the story
