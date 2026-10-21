---
name: knowledge-capture
description: "Capture reusable assets after an engagement: frameworks, model modules, benchmarks, case study draft, expert contacts."
---

# Knowledge Capture

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/knowledge-capture
```
Then provide:
1. **The engagement**
2. **Assets worth keeping**
3. **Confidentiality limits**

I will classify what is reusable, strip confidential detail, and write a short case summary and an asset index.

**Output:** Saved to `outputs/retros/knowledge-capture-[engagement]-[date].md`
**Time:** ~25 min

**When to use:** After the retro

**Phase:** Close  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/engagement-model/08-support-functions-and-tools.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Models | `outputs/models/*.xlsx` | module | Reusable modules |
| Decks | `outputs/decks/*.md` | slide | Reusable pages |
| Compliance | `~/.gemini/extensions/consulting-os/sub-agents/risk-compliance-advisor.md` | confidential, anonymize | What can be kept |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If proposal -> Link to `proposal-draft`
- If retro -> Link to `retrospective`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/models/*.xlsx`: Reusable modules
- `outputs/decks/*.md`: Reusable pages
- `~/.gemini/extensions/consulting-os/sub-agents/risk-compliance-advisor.md`: What can be kept

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Models:** [Modules]

**From Decks:** [Pages]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Client permissions
- Anonymization rules

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Limit
**"What client information must never leave the engagement folder?"**

Strip it first.

---

## The Process

### Step 1: List assets



### Step 2: Anonymize



### Step 3: Write a short case

Situation, approach, result.

### Step 4: Index with tags



### Step 5: Store in the firm knowledge base

Via the user.

---

## Structured Output Template

```markdown
# Knowledge Capture: [Engagement]

## Case Summary
[Situation / approach / result, anonymized]

## Asset Index
| Asset | Type | Location | Reusable? | Confidentiality | Owner |
|---|---|---|---|---|---|
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/retros/knowledge-capture-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `~/.gemini/extensions/consulting-os/context-library/example-engagements/[engagement]-case.md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/proposal-draft` - Credentials

**Pulls from:**
- `/retrospective` - Learnings

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Client identifiers** removed
- [ ] **Assets tagged**
- [ ] **Owner** named
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `retrospective` - Retro
- `proposal-draft` - Reuse
