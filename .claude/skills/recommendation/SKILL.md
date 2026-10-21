---
name: recommendation
description: Synthesize the final recommendation: what, why, financial case, conditions, risks, and the ask.
disable-model-invocation: false
user-invocable: true
---

# Recommendation

## Quick Start

```
/recommendation
```
Then provide:
1. **Findings and chosen option**
2. **Financial case outputs**
3. **Decision requested**

I will write the recommendation in answer-first form with the supporting argument, the conditions that must hold, and the explicit ask.

**Output:** Saved to `outputs/recommendations/recommendation-[engagement]-[date].md`
**Time:** ~30 min

**When to use:** Before the final SteerCo and when the storyline is converging

**Phase:** Recommend  |  **Framework source:** `context-library/frameworks/pyramid-principle-scqa.md`; `context-library/frameworks/storyline-patterns.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Options | `outputs/analyses/options-evaluation-*.md` | winner, trade-off | Chosen option |
| Models | `outputs/models/*.xlsx`, `outputs/analyses/scenario-sensitivity-*.md` | NPV, payback, range | Financial case |
| Hypotheses | `outputs/hypotheses/*.md` | supported, rejected | What is proven |
| Risks | `outputs/*/risk-register*.md` | risk, mitigation | Conditions and risks |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If storyline needed -> Link to `storyline`
- If readout next -> Link to `final-readout`
- If pressure test -> Link to `partner-reviewer (sub-agent)`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/analyses/options-evaluation-*.md`: Chosen option
- `outputs/models/*.xlsx`, `outputs/analyses/scenario-sensitivity-*.md`: Financial case
- `outputs/hypotheses/*.md`: What is proven
- `outputs/*/risk-register*.md`: Conditions and risks

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Options:** [Chosen option]

**From Models:** [Financial case]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- The decision requested
- Conditions the client must meet

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Ask
**"What exactly do you want the SteerCo to decide?"**

The recommendation must end in a decision.

---

## The Process

### Step 1: State the recommendation

One sentence with size of prize and timeframe.

### Step 2: Give three reasons

Each backed by a finding and a number.

### Step 3: Show the financial case

Run-rate, one-time cost, payback, range.

### Step 4: State conditions and risks

What must be true and how it is mitigated.

### Step 5: Make the ask

Decisions, owners, dates.

---

## Structured Output Template

```markdown
# Recommendation: [Engagement]

## We recommend
[One sentence]

## Why
1. [Reason + proof number]
2.
3.

## Financial Case
| Metric | Low | Base | High |
|---|---|---|---|

## Conditions
[ ]

## Risks and Mitigation
[ ]

## The Ask
| Decision | Owner | By when |
|---|---|---|
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/recommendations/recommendation-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decisions/recommendation-[engagement].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/storyline` - Governing thought
- `/final-readout` - Core content
- `/roadmap-build` - Plan to deliver

**Pulls from:**
- `/options-evaluation` - Choice
- `/scenario-sensitivity` - Case

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Answer first**
- [ ] **Three reasons**, each with a number
- [ ] **Conditions** stated
- [ ] **Ask** is explicit
- [ ] **Numbers** tie to the model
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `storyline` - Build the story
- `final-readout` - Build the readout
- `roadmap-build` - Build the roadmap
