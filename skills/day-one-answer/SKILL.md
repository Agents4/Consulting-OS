---
name: day-one-answer
description: "State the best current answer to the key question on day 1, with the three to five things that must be true."
---

# Day-One Answer

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/day-one-answer
```
Then provide:
1. **The key question**
2. **What you know already** (industry, client, past work)
3. **Your gut view**, even if rough

I will draft the answer as if the SteerCo were tomorrow, name what must be true for it to hold, and turn those into the first analyses.

**Output:** Saved to `outputs/hypotheses/day-one-answer-[engagement]-[date].md`
**Time:** ~15 min

**When to use:** Day 1 and again at every gate

**Phase:** Mobilize; refreshed at gates  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/frameworks/hypothesis-driven-approach.md`; `~/.gemini/extensions/consulting-os/context-library/frameworks/pyramid-principle-scqa.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Problem Statement | `outputs/problem-statements/*.md` | key question | The question to answer |
| Hypotheses | `outputs/hypotheses/*.md` | H1, status | Current beliefs and evidence |
| Research | `context-library/research/*.md` | benchmark, market, comparable | Prior knowledge |
| Frameworks | `~/.gemini/extensions/consulting-os/context-library/frameworks/storyline-patterns.md` | answer first, governing thought | Answer shape |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If answer needs testing -> Link to `hypothesis-draft`
- If answer needs a storyline -> Link to `storyline`
- If answer feels weak -> Link to `skeptic (sub-agent)`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/problem-statements/*.md`: The question to answer
- `outputs/hypotheses/*.md`: Current beliefs and evidence
- `context-library/research/*.md`: Prior knowledge
- `~/.gemini/extensions/consulting-os/context-library/frameworks/storyline-patterns.md`: Answer shape

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Hypotheses:** [Latest evidence]

**From Research:** [Benchmarks and comparables]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Quantified claims
- Conditions under which the answer flips

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Gut Answer
**"If the SteerCo were tomorrow, what would you recommend?"**

Forces a position that analysis can then test.

### Question 2: The Flip
**"What fact would reverse the answer?"**

Those facts become the first analyses.

---

## The Process

### Step 1: State the answer in one sentence

Governing thought: recommendation plus size of prize plus main condition.

### Step 2: List what must be true

Three to five conditions, each testable.

### Step 3: Link to analyses

One analysis per condition, ranked by uncertainty and impact.

### Step 4: Name what would change your mind

Specific data points or findings.

### Step 5: Version it

Date and version; compare to the last version at each gate.

---

## Structured Output Template

```markdown
# Day-One Answer: [Engagement]

**Version:** [ ]  |  **Date:** [ ]

## Governing Thought
[One sentence: answer, prize, condition]

## What Must Be True
| # | Condition | Test | Confidence | Status |
|---|---|---|---|---|

## What Would Change Our Mind
- [ ]

## Change Since Last Version
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/hypotheses/day-one-answer-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/hypotheses/day-one-answer-[engagement].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/hypothesis-draft` - Conditions become hypotheses
- `/storyline` - Starting governing thought
- `/proposal-draft` - Opening hypothesis

**Pulls from:**
- `/problem-statement` - Question
- `/hypothesis-draft` - Evidence updates

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **One sentence** answer, not a topic
- [ ] **Conditions** are testable
- [ ] **Flip conditions** are named
- [ ] **Version** and date recorded
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `hypothesis-draft` - Build the log
- `storyline` - Build the storyline
- `skeptic` - Challenge the answer
