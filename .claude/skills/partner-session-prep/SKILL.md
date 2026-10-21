---
name: partner-session-prep
description: Prepare the problem-solving session with the partner: the question, options, evidence, and decision asked.
disable-model-invocation: false
user-invocable: true
---

# Partner Session Prep

## Quick Start

```
/partner-session-prep
```
Then provide:
1. **The issue** you need the partner's help with
2. **Evidence so far**
3. **Time available**

I will produce a one-page prep with the answer first, the evidence, the options you see, and the specific decision or steer you need.

**Output:** Saved to `outputs/team-messages/partner-session-prep-[date].md`
**Time:** ~15 min

**When to use:** Before each of the two or more weekly partner sessions

**Phase:** All  |  **Framework source:** `context-library/engagement-model/05-cadence-and-handoffs.md`; `sub-agents/partner-reviewer.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Hypotheses | `outputs/hypotheses/*.md` | status, change | Where the answer stands |
| Analyses | `outputs/analyses/*.md` | finding | Evidence |
| Partner Persona | `sub-agents/partner-reviewer.md` | what partners ask | Typical challenges |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If storyline help -> Link to `storyline`
- If decision to log -> Link to `decision-doc`
- If review -> Link to `review-panel`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/hypotheses/*.md`: Where the answer stands
- `outputs/analyses/*.md`: Evidence
- `sub-agents/partner-reviewer.md`: Typical challenges

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Hypotheses:** [Answer status]

**From Analyses:** [Key evidence]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Partner time
- Specific ask

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Ask
**"What exactly do you want from the partner: a decision, a steer, or an introduction?"**

Partners have 30 minutes.

---

## The Process

### Step 1: Lead with the answer

Current best view.

### Step 2: Show the evidence

Three pages at most.

### Step 3: State options

Each with a trade-off and your recommendation.

### Step 4: State the ask

Decision or steer needed.

### Step 5: Anticipate challenges

Top three questions.

---

## Structured Output Template

```markdown
# Partner Session Prep: [Date]

**Answer so far:** [ ]
**Evidence:** [3 bullets]
**Options:** [A / B and recommendation]
**The ask:** [ ]
**Likely challenges:** [ ]
**Time:** [ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/team-messages/partner-session-prep-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/meetings/partner-session-[date].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/decision-doc` - Decisions

**Pulls from:**
- `/hypothesis-draft` - Answer status

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Answer first**
- [ ] **Ask** is specific
- [ ] **Evidence** is three pages or fewer
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `steerco-prep` - SteerCo
- `decision-doc` - Log decisions
- `storyline` - Story
