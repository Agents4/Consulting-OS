---
name: review-panel
description: "Run a multi-persona review of any output with the sub-agent reviewers: partner, EM, skeptic, client sponsor, CFO, and QC."
---

# Review Panel

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/review-panel
```
Then provide:
1. **The output to review** (deck, model, memo)
2. **Audience and stakes**
3. **Which reviewers** (default: partner, EM, skeptic, client sponsor)

I will run each reviewer persona in turn, consolidate their feedback into one prioritized list, and flag contradictions between reviewers.

**Output:** Saved to `outputs/reviews/review-panel-[item]-[date].md`
**Time:** ~20 min

**When to use:** Before an EM or partner review, and before any client-facing output

**Phase:** All  |  **Framework source:** `~/.gemini/extensions/consulting-os/sub-agents/*.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Sub-agents | `~/.gemini/extensions/consulting-os/sub-agents/*.md` | persona, questions, red flags | Each reviewer's method and standards |
| Output | `outputs/**` | deck, model, memo | What is reviewed |
| Stakeholders | `context-library/stakeholders/*.md` | style, preference | Real reviewer preferences |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If model under review -> Link to `model-audit`
- If deck under review -> Link to `deck-qc`
- If story weak -> Link to `storyline`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `~/.gemini/extensions/consulting-os/sub-agents/*.md`: Each reviewer's method and standards
- `outputs/**`: What is reviewed
- `context-library/stakeholders/*.md`: Real reviewer preferences

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Sub-agents:** [Reviewers selected]

**From Output:** [Item and status]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Reviewer availability
- Stakes

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Stakes
**"Is this going to a client or staying internal?"**

Raises or lowers the bar and the number of reviewers.

---

## The Process

### Step 1: Choose reviewers

Partner for story; EM for plan; skeptic for logic; sponsor and CFO for client view; QC for production.

### Step 2: Run each persona

Each gives top three issues and one strength.

### Step 3: Consolidate

Merge duplicates; rank by severity.

### Step 4: Resolve conflicts

Where reviewers disagree, state the choice and why.

### Step 5: Create the fix list

Owner and due date.

---

## Structured Output Template

```markdown
# Review Panel: [Item]

## Verdict
[ ]

## Top Issues (ranked)
| # | Issue | Raised by | Severity | Fix | Owner |
|---|---|---|---|---|---|

## By Reviewer
**Partner:** [ ]
**EM:** [ ]
**Skeptic:** [ ]
**Client sponsor:** [ ]
**CFO:** [ ]
**QC:** [ ]

## Conflicts
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/reviews/review-panel-[item]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decks/review-[item].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/slide-draft` - Fixes
- `/model-build` - Fixes
- `/steerco-prep` - Readiness

**Pulls from:**
- `/deck-qc` - QC
- `/model-audit` - Audit

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Each persona** gives specific, actionable feedback
- [ ] **Conflicts** are resolved
- [ ] **Fix list** has owners
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `deck-qc` - QC the deck
- `model-audit` - Audit the model
- `steerco-prep` - Prepare the SteerCo
