---
name: survey-design
description: Design a customer or employee survey: sample, questions, scales, analysis plan, and bias checks.
disable-model-invocation: false
user-invocable: true
---

# Survey Design

## Quick Start

```
/survey-design
```
Then provide:
1. **The hypothesis** the survey tests
2. **Population and sample size**
3. **Channel and timing**

I will write the questionnaire, the sampling plan, and the analysis plan before any responses arrive, and flag bias risks.

**Output:** Saved to `outputs/research-synthesis/survey-design-[topic]-[date].md`
**Time:** ~30 min

**When to use:** Interviews suggest a pattern that needs quantifying

**Phase:** Diagnose  |  **Framework source:** `context-library/frameworks/interviewing-playbook.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Hypotheses | `outputs/hypotheses/*.md` | test, evidence needed | What the survey must show |
| Interviews | `outputs/research-synthesis/*.md` | theme, language | Customer wording for questions |
| Compliance | `sub-agents/risk-compliance-advisor.md` | consent, PII | Privacy and consent rules |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If responses arrive -> Link to `data-exploration`
- If privacy questions -> Link to `risk-compliance-advisor (sub-agent)`
- If need qualitative depth -> Link to `interview-guide`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/hypotheses/*.md`: What the survey must show
- `outputs/research-synthesis/*.md`: Customer wording for questions
- `sub-agents/risk-compliance-advisor.md`: Privacy and consent rules

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Hypotheses:** [What to quantify]

**From Interviews:** [Language to reuse]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Sample frame
- Response rate
- Incentives

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Decision
**"What result would change the recommendation?"**

Writes the analysis plan before launch.

---

## The Process

### Step 1: Define the objective and the decision rule

What result changes what.

### Step 2: Design the sample

Segments, size, quotas, response rate assumption.

### Step 3: Write questions

Neutral, one idea per question, consistent scales.

### Step 4: Plan the analysis

Cuts, significance, how results map to hypotheses.

### Step 5: Pilot

Five respondents; fix wording; then launch.

---

## Structured Output Template

```markdown
# Survey Design: [Topic]

## Objective and Decision Rule
[ ]

## Sample
| Segment | Target n | Method | Expected response rate |
|---|---|---|---|

## Questionnaire
| # | Question | Type | Scale | Hypothesis |
|---|---|---|---|---|

## Analysis Plan
[Cuts, tests, mapping to hypotheses]

## Bias and Privacy Check
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/research-synthesis/survey-design-[topic]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/research/survey-design-[topic].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/data-exploration` - Results
- `/hypothesis-draft` - Evidence

**Pulls from:**
- `/interview-synthesis` - Wording

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Questions** are neutral
- [ ] **Sample** supports the cuts planned
- [ ] **Decision rule** set before launch
- [ ] **Consent and privacy** addressed
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `interview-guide` - Add depth
- `data-exploration` - Profile results
- `root-cause-analysis` - Test causes
