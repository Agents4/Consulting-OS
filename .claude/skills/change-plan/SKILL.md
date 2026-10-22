---
name: change-plan
description: "Plan adoption: stakeholder groups, what changes, resistance, messages, messengers, and early asks."
disable-model-invocation: false
user-invocable: true
---

# Change Plan

## Quick Start

```
/change-plan
```
Then provide:
1. **The change** and who is affected
2. **Stakeholder map**
3. **Timeline**

I will assess change readiness by group, craft the message and messenger for each, and set the first ask and a feedback loop.

**Output:** Saved to `outputs/roadmaps/change-plan-[engagement]-[date].md`
**Time:** ~30 min

**When to use:** Develop and Recommend phases

**Phase:** Develop through Transition  |  **Framework source:** `context-library/frameworks/change-and-implementation.md`; `templates/risk-register-template.md` (change readiness)

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Stakeholders | `outputs/stakeholder-maps/*.md` | stance, influence | Groups and stance |
| Interviews | `outputs/research-synthesis/*.md` | fear, resist, support | Voice of employees |
| Roadmap | `outputs/roadmaps/*.md` | timing | Change timing |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If roadmap -> Link to `roadmap-build`
- If risks -> Link to `risk-register`
- If stakeholders -> Link to `stakeholder-map`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/stakeholder-maps/*.md`: Groups and stance
- `outputs/research-synthesis/*.md`: Voice of employees
- `outputs/roadmaps/*.md`: Change timing

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Stakeholders:** [Groups]

**From Interviews:** [Concerns]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Who loses what
- Capacity for change

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Loss
**"What do affected people lose, and what do they gain?"**

Address the loss directly.

---

## The Process

### Step 1: Segment groups

Size, what changes, what they lose and gain.

### Step 2: Rate readiness

1 to 5 with evidence.

### Step 3: Write messages and pick messengers



### Step 4: Plan the first ask and the feedback loop



### Step 5: Add to the risk register

Resistance risks.

---

## Structured Output Template

```markdown
# Change Plan: [Engagement]

| Group | Size | What changes | Lose | Gain | Stance | Readiness | Message | Messenger | First ask |
|---|---|---|---|---|---|---|---|---|---|

## Communication Calendar
[ ]

## Feedback Loop
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/roadmaps/change-plan-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decisions/change-plan-[engagement].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/roadmap-build` - Adoption steps
- `/risk-register` - Resistance risks

**Pulls from:**
- `/stakeholder-map` - Groups
- `/interview-synthesis` - Voice

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Each group** has a message and messenger
- [ ] **Readiness** rated with evidence
- [ ] **Feedback loop** defined
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `roadmap-build` - Roadmap
- `stakeholder-map` - Stakeholders
- `risk-register` - Risks
