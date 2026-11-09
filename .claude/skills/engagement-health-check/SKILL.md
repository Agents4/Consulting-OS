---
name: engagement-health-check
description: "Check engagement health: scope, question, hypotheses, team load, client relationship, financials, quality, risks."
disable-model-invocation: false
user-invocable: true
---

# Engagement Health Check

## Quick Start

```
/engagement-health-check
```
Then provide:
1. **Engagement and week**
2. **Any concerns**
3. **Who is asking** (EM or partner)

I will score the engagement across eight dimensions with evidence, name the top two issues, and recommend actions.

**Output:** Saved to `outputs/status-updates/health-check-[date].md`
**Time:** ~20 min

**When to use:** Every two weeks, and when something feels off

**Phase:** All  |  **Framework source:** `context-library/engagement-model/03-engagement-lifecycle.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Status | `outputs/status-updates/*.md` | RAG | Trend |
| Hypotheses | `outputs/hypotheses/*.md` | status | Progress on answer |
| Risks | `context-library/decisions/risk-register*.md` | score | Risk |
| Decisions | `context-library/decisions/*.md` | scope change | Scope drift |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If risks -> Link to `risk-register`
- If scope -> Link to `decision-doc`
- If team load -> Link to `weekly-plan`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/status-updates/*.md`: Trend
- `outputs/hypotheses/*.md`: Progress on answer
- `context-library/decisions/risk-register*.md`: Risk
- `context-library/decisions/*.md`: Scope drift

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Status:** [Trend]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Client sentiment
- Team hours

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Pulse
**"How does the sponsor feel about progress today?"**

Relationship risk shows first in tone.

---

## The Process

### Step 1: Score eight dimensions

Question, scope, answer, evidence, team, client, quality, financials.

### Step 2: Cite evidence for each



### Step 3: Name the top two issues



### Step 4: Recommend actions



### Step 5: Share with the EM



---

## Structured Output Template

```markdown
# Health Check: [Engagement] - [Date]

| Dimension | RAG | Evidence | Action |
|---|---|---|---|
| Question and scope | | | |
| Answer and hypotheses | | | |
| Evidence and data | | | |
| Team load | | | |
| Client relationship | | | |
| Quality | | | |
| Financials | | | |
| Risks | | | |

## Top Two Issues
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/status-updates/health-check-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/engagements/health-check-[date].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/status-update` - Issues

**Pulls from:**
- `/status-update` - Trend

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Evidence** for each RAG
- [ ] **Two issues** named
- [ ] **Actions** proposed
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `risk-register` - Risks
- `decision-doc` - Scope
