---
name: roadmap-build
description: Build the implementation roadmap: initiatives, sequencing, owners, milestones, KPIs, quick wins, governance.
disable-model-invocation: false
user-invocable: true
---

# Roadmap Build

## Quick Start

```
/roadmap-build
```
Then provide:
1. **The recommendation and initiatives**
2. **Dependencies and constraints**
3. **Client owners**

I will produce a sequenced 12-to-36-month roadmap with named client owners, KPIs, quick wins, and PMO governance.

**Output:** Saved to `outputs/roadmaps/roadmap-[engagement]-[date].md`
**Time:** ~35 min

**When to use:** Recommend and Transition phases

**Phase:** Recommend and Transition  |  **Framework source:** `context-library/frameworks/change-and-implementation.md`; `sub-agents/implementation-lead.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Recommendation | `outputs/recommendations/*.md` | initiative, owner | What to implement |
| Initiative Sizing | `outputs/analyses/initiative-sizing-*.md` | ramp, cost | Value timing |
| Implementation Persona | `sub-agents/implementation-lead.md` | feasibility, capacity | Reality checks |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If change readiness -> Link to `change-plan`
- If risks -> Link to `risk-register`
- If handover -> Link to `handover-pack`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/recommendations/*.md`: What to implement
- `outputs/analyses/initiative-sizing-*.md`: Value timing
- `sub-agents/implementation-lead.md`: Reality checks

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Recommendation:** [Initiatives]

**From Sizing:** [Ramp]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Owners
- Capacity
- Dependencies

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Owner
**"Which named client leader owns each initiative?"**

Without an owner, it is a wish.

---

## The Process

### Step 1: List initiatives and milestones



### Step 2: Sequence by dependency and value

Quick wins first.

### Step 3: Assign client owners and KPIs



### Step 4: Reality check capacity

With the implementation reviewer.

### Step 5: Set governance

PMO, cadence, escalation.

---

## Structured Output Template

```markdown
# Roadmap: [Engagement]

| Initiative | Owner | Q1 | Q2 | Q3 | Q4 | KPI | Run-rate value | Dependencies |
|---|---|---|---|---|---|---|---|---|

## Quick Wins (first 90 days)
[ ]

## Governance
[PMO, cadence, escalation]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/roadmaps/roadmap-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/decisions/roadmap-[engagement].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/final-readout` - Roadmap pages
- `/handover-pack` - Plan to hand over

**Pulls from:**
- `/recommendation` - Initiatives
- `/initiative-sizing` - Value

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Client owner** per initiative
- [ ] **KPIs** defined
- [ ] **Quick wins** in 90 days
- [ ] **Capacity** checked
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `change-plan` - Adoption
- `handover-pack` - Handover
- `risk-register` - Risks
