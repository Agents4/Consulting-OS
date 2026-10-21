---
name: exec-summary
description: Write the executive summary page: answer, prize, three reasons, risks, ask. Must stand alone.
disable-model-invocation: false
user-invocable: true
---

# Executive Summary

## Quick Start

```
/exec-summary
```
Then provide:
1. **The recommendation**
2. **Key numbers**
3. **Decision requested**

I will write a one-page executive summary that a busy sponsor can read in two minutes and act on.

**Output:** Saved to `outputs/decks/exec-summary-[engagement]-[date].md`
**Time:** ~20 min

**When to use:** Each SteerCo pre-read and the final readout

**Phase:** Recommend  |  **Framework source:** `context-library/frameworks/pyramid-principle-scqa.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Recommendation | `outputs/recommendations/*.md` | recommend, ask | The answer |
| Storyline | `outputs/storylines/*.md` | governing thought, key lines | Structure |
| Writing Style | `context-library/writing-style-client-exec.md` | tone, length | Voice |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If numbers need tie -> Link to `number-tie-out`
- If review -> Link to `review-panel`
- If slides -> Link to `slide-draft`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/recommendations/*.md`: The answer
- `outputs/storylines/*.md`: Structure
- `context-library/writing-style-client-exec.md`: Voice

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Recommendation:** [Answer]

**From Storyline:** [Key lines]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Decision date
- Owner of the ask

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Reader
**"Will the reader see only this page?"**

If yes, it must carry the whole case.

---

## The Process

### Step 1: Lead with the answer

Recommendation and size of prize.

### Step 2: Give three reasons

One sentence each with a number.

### Step 3: State cost, timing, risks

Concise.

### Step 4: End with the ask

Decision, owner, date.

### Step 5: Cut 20%

Then check it still stands alone.

---

## Structured Output Template

```markdown
# Executive Summary

**Recommendation:** [ ]

**Why:**
1. [ ]
2. [ ]
3. [ ]

**Investment and timing:** [ ]
**Key risks and mitigations:** [ ]
**Decisions requested:** [ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/decks/exec-summary-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decks/exec-summary-[engagement].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/final-readout` - Opening page
- `/steerco-prep` - Pre-read

**Pulls from:**
- `/recommendation` - Answer
- `/storyline` - Key lines

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Stands alone**
- [ ] **Numbers** tie
- [ ] **Ask** is explicit
- [ ] **Under one page**
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `storyline` - Align to story
- `final-readout` - Use in readout
- `number-tie-out` - Tie numbers
