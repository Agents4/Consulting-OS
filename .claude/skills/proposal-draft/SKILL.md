---
name: proposal-draft
description: "Draft an engagement proposal: situation, objectives, approach, team, timeline, fees, and why us. Pursuit phase."
disable-model-invocation: false
user-invocable: true
---

# Proposal Draft

## Quick Start

```
/proposal-draft
```
Then provide:
1. **The client and the trigger** (why now, who asked, what they said they want)
2. **Any RFP, brief, or call notes** (paste or point to the file)
3. **Constraints** (budget band, start date, team size, conflicts)

I will turn the opportunity into a proposal that frames the client's question sharply, shows a hypothesis-driven approach, and prices it against a staffing plan.

**Output:** Saved to `outputs/proposals/proposal-[client]-[date].md`
**Time:** ~30 min for a draft; ~60 min with a worked staffing and fee table

**When to use:** Responding to an RFP or turning a partner conversation into a written proposal

**Phase:** Pursuit  |  **Framework source:** `templates/proposal-template.md`; `context-library/engagement-model/03-engagement-lifecycle.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Client Materials | `context-library/client-materials/*.md` | RFP, brief, annual report, strategy, press | Client context, stated objectives, language the client uses |
| Frameworks | `context-library/frameworks/storyline-patterns.md` | SCQA, pyramid, proposal | How to open with a sharp situation and complication |
| Writing Style | `context-library/writing-style-proposal.md` | tone, length, structure | House proposal voice |
| Team Roster | `context-library/team-roster-template.md` | staffing, roles, availability | Who can be offered and at what time commitment |
| Example Engagement | `context-library/example-engagements/*.md` | approach, phases, fees | Format reference only, never copied content |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If the key question is unclear -> Link to `problem-statement`
- If scope needs a phase plan -> Link to `workplan-build`
- If a similar past engagement exists -> Link to `knowledge-capture`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/client-materials/*.md`: Client context, stated objectives, language the client uses
- `context-library/frameworks/storyline-patterns.md`: How to open with a sharp situation and complication
- `context-library/writing-style-proposal.md`: House proposal voice
- `context-library/team-roster-template.md`: Who can be offered and at what time commitment
- `context-library/example-engagements/*.md`: Format reference only, never copied content

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Client Materials:** [Client context, trigger, stated goals]

**From Roster:** [Available people and seniority mix]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- The sponsor's real decision and deadline
- Budget band and who approves fees
- Conflicts or exclusivity issues

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Decision
**"What decision will the sponsor make with our answer, and by when?"**

This sets the key question and the end date. A proposal without a decision date is a brochure.

### Question 2: The Hidden Constraint
**"What would make this a no-go internally for the client (budget, politics, data access)?"**

The strongest proposals address the constraint head on.

### Question 3: The Competition
**"Who else is pitching, and what have they told the client?"**

Shapes the 'why us' section and how much to say about method.

---

## The Process

### Step 1: Frame the situation and complication

Write 3 to 4 sentences in SCQA form using the client's own words. State the complication as a cost or a deadline.

### Step 2: State the key question

One SMART question. Add the first hypothesis as a Day-1 answer so the client sees how we think. Link to `/day-one-answer`.

### Step 3: Design the approach

Three to four phases with the question each phase answers, the deliverable at the gate, and the client input needed.

### Step 4: Staff and price

Build a team of partner, EM, 2 to 4 consultants/associates plus experts. Compute fees from weeks x team x blended rate in a small table, not from a guess.

### Step 5: Add why us and what we need from you

Two or three proof points tied to this question. List client inputs (sponsor time, counterpart, data owners).

---

## Common Mistakes

- **Method before question**: Open with the client's problem, not our toolkit.
- **Fixed scope for an unknown problem**: Offer a diagnostic phase with a decision gate instead of fixing the end state.

---

## Structured Output Template

```markdown
# Proposal: [Engagement Name]

**Client:** [ ]  |  **Date:** [ ]  |  **Version:** [ ]

## 1. Where you are and what is at stake
[SCQA in 4 sentences]

## 2. The question we will answer
> [Key question]
**Our starting hypothesis:** [Day-1 answer]

## 3. Our approach
| Phase | Question it answers | Weeks | Deliverable at gate |
|---|---|---|---|

## 4. Team
| Role | Name | Time commitment |
|---|---|---|

## 5. Timeline and governance
[Gates, SteerCo cadence, check-ins]

## 6. Investment
| Item | Weeks | Team | Fee |
|---|---|---|---|

## 7. What we need from you
[Sponsor time, counterpart, data owners, access]

## 8. Why us
[Three proof points tied to this question]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/proposals/proposal-[client]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/client-materials/proposal-[client].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/problem-statement` - Agreed key question after the win
- `/workplan-build` - Phases become the workplan
- `/kickoff-plan` - Team and governance carry into kickoff

**Pulls from:**
- `/knowledge-capture` - Past case studies and credentials
- `/day-one-answer` - Starting hypothesis

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Key question** is a single SMART question the sponsor would recognize
- [ ] **Day-1 answer** is stated as a falsifiable hypothesis
- [ ] **Every phase** ends in a decision gate with a named deliverable
- [ ] **Fees** reconcile to weeks x team x rate
- [ ] **Client inputs** are listed with owners
- [ ] **No jargon** the client does not use
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `problem-statement` - Write the agreed key question after the win
- `workplan-build` - Convert phases into a workplan
- `kickoff-plan` - Plan the first two weeks
