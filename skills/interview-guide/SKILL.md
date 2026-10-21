---
name: interview-guide
description: "Build an interview guide for client, customer, or expert interviews, tied to hypotheses."
---

# Interview Guide

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/interview-guide
```
Then provide:
1. **Who you are interviewing** (role, seniority, relationship)
2. **Hypotheses to test** with this person
3. **Time available** (30, 45, or 60 minutes)

I will write a hypothesis-linked guide with opening, open questions, probes, and a close, plus a note-taking grid.

**Output:** Saved to `outputs/interviews/interview-guide-[role]-[date].md`
**Time:** ~15 min

**When to use:** Before each interview round: executives, frontline, customers, experts

**Phase:** Diagnose  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/frameworks/interviewing-playbook.md`; `~/.gemini/extensions/consulting-os/templates/interview-guide-template.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Hypotheses | `outputs/hypotheses/*.md` | H1, test, evidence needed | What this interview must test |
| Stakeholders | `context-library/stakeholders/*.md` | role, stance, topics | Sensitivities and rapport |
| Prior Interviews | `context-library/interviews/*.md` | quote, theme | Avoid repeating questions |
| Frameworks | `~/.gemini/extensions/consulting-os/context-library/frameworks/interviewing-playbook.md` | open question, probe, MECE | Technique rules |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If interviews are done -> Link to `interview-synthesis`
- If customer survey is better -> Link to `survey-design`
- If sensitive stakeholder -> Link to `stakeholder-map`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/hypotheses/*.md`: What this interview must test
- `context-library/stakeholders/*.md`: Sensitivities and rapport
- `context-library/interviews/*.md`: Avoid repeating questions
- `~/.gemini/extensions/consulting-os/context-library/frameworks/interviewing-playbook.md`: Technique rules

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Hypotheses:** [What we need to hear]

**From Stakeholders:** [Topics to approach carefully]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Which hypothesis this person can speak to
- Confidentiality terms

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The One Thing
**"If you learn only one thing from this person, what is it?"**

Everything else is optional; this question is mandatory.

### Question 2: The Risk
**"Is there anything they should not be asked or told?"**

Protect the client and the interviewee.

---

## The Process

### Step 1: Pick the objective

One sentence: what we need to learn and which hypothesis it supports.

### Step 2: Write the opener

Purpose, confidentiality, how notes are used, time check.

### Step 3: Draft 6 to 8 open questions

Start broad, narrow with probes. No leading questions.

### Step 4: Add probes and quantification asks

'Can you give an example?' 'How many?' 'How often?'

### Step 5: Close and next steps

Ask who else to speak to, what data exists, and permission to follow up.

---

## Structured Output Template

```markdown
# Interview Guide: [Role / Person]

**Date:** [ ]  |  **Interviewer:** [ ]  |  **Note-taker:** [ ]  |  **Length:** [ ]

## Objective
[What we must learn] - tests H[ ]

## Opener
[Script]

## Questions
| # | Question | Probe | Hypothesis | Must ask? |
|---|---|---|---|---|

## Close
[Next steps, referrals, data asks]

## Note Grid
| Theme | Quote | Fact / opinion | Follow-up |
|---|---|---|---|
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/interviews/interview-guide-[role]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/interviews/guide-[role].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/interview-synthesis` - Notes structure
- `/hypothesis-draft` - Evidence
- `/stakeholder-map` - Stance signals

**Pulls from:**
- `/hypothesis-draft` - Tests
- `/stakeholder-map` - Sensitivities

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Questions** are open and non-leading
- [ ] **Every question** links to a hypothesis or is marked exploratory
- [ ] **Timing** fits the slot
- [ ] **Confidentiality** wording is included
- [ ] **Referral ask** is in the close
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `interview-synthesis` - Synthesize findings
- `survey-design` - Scale with a survey
- `hypothesis-draft` - Update hypotheses
