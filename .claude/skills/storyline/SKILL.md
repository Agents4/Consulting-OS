---
name: storyline
description: "Build the storyline: governing thought, key lines, dot-dash page logic, using Pyramid Principle and SCQA."
disable-model-invocation: false
user-invocable: true
---

# Storyline

## Quick Start

```
/storyline
```
Then provide:
1. **The answer or current best answer**
2. **Audience and decision**
3. **Evidence so far**

I will write the story as titles only (dot-dash), test that the titles read as a coherent argument, and map each page to the analysis behind it.

**Output:** Saved to `outputs/storylines/storyline-[engagement]-[date].md`
**Time:** ~30 min

**When to use:** Before building any deck; refresh at each gate

**Phase:** Develop and Recommend  |  **Framework source:** `context-library/frameworks/pyramid-principle-scqa.md`; `context-library/frameworks/storyline-patterns.md`; `templates/storyline-dot-dash-template.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Day-One Answer | `outputs/hypotheses/day-one-answer-*.md` | governing thought | Answer to carry |
| Hypotheses | `outputs/hypotheses/*.md` | supported, rejected | What the evidence supports |
| Frameworks | `context-library/frameworks/storyline-patterns.md` | SCQA, pyramid, dot-dash | Story patterns |
| Writing Style | `context-library/writing-style-client-exec.md` | tone, length | Voice for the audience |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If storyline agreed -> Link to `ghost-deck`
- If evidence thin -> Link to `hypothesis-draft`
- If partner review -> Link to `review-panel`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/hypotheses/day-one-answer-*.md`: Answer to carry
- `outputs/hypotheses/*.md`: What the evidence supports
- `context-library/frameworks/storyline-patterns.md`: Story patterns
- `context-library/writing-style-client-exec.md`: Voice for the audience

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Hypotheses:** [What is proven]

**From Day-One Answer:** [Governing thought]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Decision at the end
- Audience's starting belief

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Audience
**"What does the SteerCo believe today, and what must they believe after?"**

The storyline moves belief from A to B.

### Question 2: The Order
**"Does this argument go from answer to support, or from situation to answer?"**

Exec audiences get answer first.

---

## The Process

### Step 1: Write the governing thought

One sentence; the answer.

### Step 2: Write SCQA

Situation, complication, question, answer.

### Step 3: Write the key lines

Three to five supports; each a full sentence.

### Step 4: Write dot-dash

One action title per page under each key line.

### Step 5: Read the titles aloud

They must tell the whole story without the pages; fix gaps and repeats.

---

## Structured Output Template

```markdown
# Storyline: [Engagement]

**Audience:** [ ]  |  **Decision:** [ ]  |  **Version:** [ ]

## Governing Thought
[ ]

## SCQA
S: [ ]  C: [ ]  Q: [ ]  A: [ ]

## Dot-Dash
**Key line 1:** [ ]
- Page: [Action title] | Evidence: [analysis] | Status: [Ghost / Draft / Tied]
- Page:

**Key line 2:** [ ]
- Page:

## Reading Test
[Notes on gaps or repeats]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/storylines/storyline-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decks/storyline-[engagement].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/ghost-deck` - Page list
- `/exec-summary` - Summary
- `/final-readout` - Outline

**Pulls from:**
- `/recommendation` - Answer
- `/hypothesis-draft` - Evidence

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Titles alone** tell the story
- [ ] **One message** per page
- [ ] **Each key line** is a sentence
- [ ] **Evidence** is assigned to each page
- [ ] **Decision** is explicit at the end
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `ghost-deck` - Sketch the pages
- `exec-summary` - Write the summary
- `review-panel` - Review the story
