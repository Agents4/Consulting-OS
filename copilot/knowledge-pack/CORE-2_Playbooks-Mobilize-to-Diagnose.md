# Consulting OS Core 2: Playbooks, Mobilize to Diagnose

Each playbook is one task. In Copilot, trigger one by saying: Run the [name] playbook. Follow its questions, process and template. Deliver in chat.


## Playbook: Proposal Draft (name: proposal-draft)

### Quick Start

Say: **Run the proposal-draft playbook**
Then provide:
1. **The client and the trigger** (why now, who asked, what they said they want)
2. **Any RFP, brief, or call notes** (paste or point to the file)
3. **Constraints** (budget band, start date, team size, conflicts)

I will turn the opportunity into a proposal that frames the client's question sharply, shows a hypothesis-driven approach, and prices it against a staffing plan.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~30 min for a draft; ~60 min with a worked staffing and fee table

**When to use:** Responding to an RFP or turning a partner conversation into a written proposal

**Phase:** Pursuit

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Decision
**"What decision will the sponsor make with our answer, and by when?"**

This sets the key question and the end date. A proposal without a decision date is a brochure.

#### Question 2: The Hidden Constraint
**"What would make this a no-go internally for the client (budget, politics, data access)?"**

The strongest proposals address the constraint head on.

#### Question 3: The Competition
**"Who else is pitching, and what have they told the client?"**

Shapes the 'why us' section and how much to say about method.

---

### The Process

#### Step 1: Frame the situation and complication

Write 3 to 4 sentences in SCQA form using the client's own words. State the complication as a cost or a deadline.

#### Step 2: State the key question

One SMART question. Add the first hypothesis as a Day-1 answer so the client sees how we think. Link to the day-one-answer playbook.

#### Step 3: Design the approach

Three to four phases with the question each phase answers, the deliverable at the gate, and the client input needed.

#### Step 4: Staff and price

Build a team of partner, EM, 2 to 4 consultants/associates plus experts. Compute fees from weeks x team x blended rate in a small table, not from a guess.

#### Step 5: Add why us and what we need from you

Two or three proof points tied to this question. List client inputs (sponsor time, counterpart, data owners).

---

### Common Mistakes

- **Method before question**: Open with the client's problem, not our toolkit.
- **Fixed scope for an unknown problem**: Offer a diagnostic phase with a decision gate instead of fixing the end state.

---

### Structured Output Template

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

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the problem-statement playbook - Agreed key question after the win
- the workplan-build playbook - Phases become the workplan
- the kickoff-plan playbook - Team and governance carry into kickoff

**Pulls from:**
- the knowledge-capture playbook - Past case studies and credentials
- the day-one-answer playbook - Starting hypothesis

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

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

---

### Related Skills

- `problem-statement` - Write the agreed key question after the win
- `workplan-build` - Convert phases into a workplan
- `kickoff-plan` - Plan the first two weeks



## Playbook: Problem Statement (name: problem-statement)

### Quick Start

Say: **Run the problem-statement playbook**
Then provide:
1. **The client's own description** of the problem (email, SOW, call notes)
2. **The sponsor and decision** it supports
3. **Known constraints** (budget, timing, politics, data)

I will convert a loose brief into a one-page problem statement the sponsor can sign: a single key question, scope in and out, success criteria, and constraints.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~20 min

**When to use:** Week 1 of any engagement, or whenever scope drifts and the question needs resetting

**Phase:** Mobilize

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Decision
**"What will the sponsor do differently depending on our answer?"**

If nothing changes, the question is too broad or too soft.

#### Question 2: The Number
**"What would success look like in a number and a date?"**

A key question without a metric cannot be falsified.

#### Question 3: The Boundary
**"What is off the table (units, geographies, headcount, vendors)?"**

Out-of-scope items prevent late scope creep.

---

### The Process

#### Step 1: Draft three framings

Write the problem in three different ways. Reject two and note why.

#### Step 2: Make it SMART

Specific, Measurable, Action-oriented, Relevant, Time-bound, as a question.

#### Step 3: Set boundaries

List in-scope and out-of-scope items and the constraints.

#### Step 4: Define success

A table of criteria with metric, baseline, target, date, and who measures it.

#### Step 5: Get sign-off

Send with a handoff brief. Log agreement in the decision-doc playbook.

---

### Common Mistakes

- **A topic is not a question**: 'Digital strategy' is a topic. 'How can we reach 12% digital share of sales by 2028 within a $15M budget?' is a question.

---

### Structured Output Template

```markdown
# Problem Statement: [Engagement]

**Version:** [ ]  |  **Date:** [ ]  |  **Signed off by:** [Sponsor]

## Key Question
> [SMART question]

**Alternatives considered:** [A, B and why rejected]

## Scope
| In scope | Out of scope |
|---|---|

## Context and Trigger
[Why now]

## Success Criteria
| Criterion | Metric | Baseline | Target | By when | Measured by |
|---|---|---|---|---|---|

## Constraints and Assumptions
[Budget, time, data, politics]

## Decision Rights
[Who decides, who advises, who executes]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the day-one-answer playbook - The question to answer on Day 1
- the issue-tree playbook - Root of the tree
- the workplan-build playbook - Scope drives workplan

**Pulls from:**
- the proposal-draft playbook - Initial framing
- the stakeholder-map playbook - Sponsor view

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **One question**, not a list
- [ ] **Metric and date** inside the question or criteria
- [ ] **Out-of-scope** is explicit
- [ ] **Sponsor wording** is used where possible
- [ ] **Sign-off** captured in the decision log
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `day-one-answer` - State the first answer
- `issue-tree` - Break the question into parts
- `decision-doc` - Log the sign-off



## Playbook: Kickoff Plan (name: kickoff-plan)

### Quick Start

Say: **Run the kickoff-plan playbook**
Then provide:
1. **Engagement name and start date**
2. **Attendees** (sponsor, counterpart, SteerCo, team)
3. **What is already agreed** (scope, team, governance)

I will produce a kickoff agenda, a pre-day-1 checklist, a first-two-weeks plan, and a team charter so the cadence is running by day 10.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~20 min

**When to use:** The week before the engagement starts

**Phase:** Mobilize

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Sponsor
**"Who feels threatened by this work, and who wants it to succeed?"**

Determines pre-wire order and the tone of the kickoff.

#### Question 2: The Rhythm
**"Which SteerCo dates are already in calendars?"**

Hold dates 2 to 3 months ahead.

#### Question 3: The Logistics
**"What access, badges, and team space are still open?"**

Day-1 delays kill early momentum.

---

### The Process

#### Step 1: Draft the kickoff agenda

60 to 90 minutes: purpose, key question, scope, approach, roles, governance, data, first tasks.

#### Step 2: Build the pre-day-1 list

Read SOW twice, client research, stakeholder map, working style questions.

#### Step 3: Plan weeks 1 and 2

Data requests out by day 3, workplan by day 7, an early-win page by day 10.

#### Step 4: Settle logistics

Access, room, template, support staff, folders, calendar holds.

#### Step 5: Run the team charter conversation

Core hours, check-in/out times, review SLAs, feedback norms, leave and travel.

---

### Structured Output Template

```markdown
# Kickoff Plan: [Engagement]

## A. Kickoff Meeting
| Time | Item | Lead | Output |
|---|---|---|---|

## B. Before Day 1
- [ ] [Items]

## C. First Two Weeks
| Days | Focus | Done when |
|---|---|---|

## D. Logistics
- [ ] [Items]

## E. Team Charter
[Core hours, check-ins, SLAs, norms]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the data-request playbook - Day 1 to 3 data asks
- the workplan-build playbook - Week 1 workplan
- the steerco-prep playbook - SteerCo calendar

**Pulls from:**
- the problem-statement playbook - Agreed question and scope
- the stakeholder-map playbook - Attendee map

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Agenda** has a named lead and an output per item
- [ ] **Data owners** are named
- [ ] **SteerCo dates** are scheduled
- [ ] **Early-win page** is planned for day 10
- [ ] **Team charter** covers hours, SLAs, feedback
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `stakeholder-map` - Map sponsors and sceptics
- `data-request` - Send the first requests
- `workplan-build` - Build the workplan



## Playbook: Stakeholder Map (name: stakeholder-map)

### Quick Start

Say: **Run the stakeholder-map playbook**
Then provide:
1. **The org context** (org chart, who is in the room)
2. **What you have heard** about each person
3. **The decision** that needs their support

I will map each stakeholder's power, stance, and interests, then give a pre-wire sequence and the first ask per person.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~20 min

**When to use:** Before kickoff and again before each SteerCo

**Phase:** Mobilize and ongoing

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Real Decider
**"Who can say no after the SteerCo says yes?"**

Often a finance or legal approver outside the room.

#### Question 2: The Threat
**"Whose role or budget changes if our answer is accepted?"**

Those people need a different message and earlier contact.

---

### The Process

#### Step 1: List every stakeholder

Name, role, reporting line, role in the decision.

#### Step 2: Score influence and stance

Influence 1 to 5; stance from champion to opponent; evidence for each.

#### Step 3: Capture interests and fears

What they win, what they lose, what they have said.

#### Step 4: Sequence pre-wires

Order by influence and dependency. Assign a messenger per person.

#### Step 5: Set the first ask

One concrete request per stakeholder with a date.

---

### Structured Output Template

```markdown
# Stakeholder Map: [Engagement]

| Name | Role | Influence (1-5) | Stance | Interests / fears | Evidence | Messenger | First ask |
|---|---|---|---|---|---|---|---|

## Pre-wire Sequence
1. [Person] - [what to align on] - [by when]

## Watch List
[People whose stance may shift and why]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the steerco-prep playbook - Pre-wire plan
- the change-plan playbook - Change readiness input
- the kickoff-plan playbook - Attendee strategy

**Pulls from:**
- the interview-synthesis playbook - Stakeholder quotes
- the meeting-notes playbook - Signals

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Every row** has evidence, not rumor
- [ ] **Opponents** have a specific ask and messenger
- [ ] **Pre-wire order** is explicit
- [ ] **Confidentiality**: no personal judgments that would embarrass if leaked
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `steerco-prep` - Prepare SteerCo with pre-wires
- `change-plan` - Plan adoption
- `interview-guide` - Interview stakeholders



## Playbook: Workplan Build (name: workplan-build)

### Quick Start

Say: **Run the workplan-build playbook**
Then provide:
1. **Key question and hypotheses**
2. **Team and availability**
3. **Gate dates** (Kickoff, Diagnostic, Solutions, Final)

I will convert hypotheses into modules, tasks, owners, and dates, with data dependencies and the end-product of each module named.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~25 min

**When to use:** Week 1, and any time scope or dates change

**Phase:** Mobilize

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Gates
**"What does the SteerCo need to see at each gate to say yes?"**

Work back from the gate, not forward from the data.

#### Question 2: The Critical Path
**"Which analysis, if late, delays the next SteerCo?"**

That one gets the strongest owner.

---

### The Process

#### Step 1: Define modules

One module per top-level issue-tree branch. Name the end-product (slide, model tab).

#### Step 2: List tasks

Per module: analysis, data need, owner, effort in days, dependency.

#### Step 3: Place on calendar

Back from each gate. Leave a review day before every SteerCo.

#### Step 4: Mark the critical path

Highlight tasks whose delay moves a gate.

#### Step 5: Agree with the EM

Walk through in 15 minutes; update weekly.

---

### Structured Output Template

```markdown
# Workplan: [Engagement]

## Gates
| Gate | Date | What the SteerCo decides |
|---|---|---|

## Modules and Tasks
| Module | Hypothesis | Task | Owner | Days | Depends on | End-product | Due |
|---|---|---|---|---|---|---|---|

## Critical Path
[Tasks]

## Risks to Dates
[Item, mitigation]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the daily-plan playbook - Daily priorities
- the weekly-plan playbook - Weekly goals
- the status-update playbook - Progress reporting

**Pulls from:**
- the hypothesis-draft playbook - Hypotheses to test
- the issue-tree playbook - Modules
- the data-request playbook - Data timing

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Every task** traces to a hypothesis
- [ ] **Every module** has a named end-product
- [ ] **Gate dates** have a review day before them
- [ ] **Owners** are not overloaded beyond 100%
- [ ] **Critical path** is marked
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `prioritize-analyses` - Rank competing analyses
- `data-request` - Send data asks
- `weekly-plan` - Plan the week



## Playbook: Data Request (name: data-request)

### Quick Start

Say: **Run the data-request playbook**
Then provide:
1. **The analyses** that need data
2. **Known client systems and data owners**
3. **Confidentiality constraints**

I will draft a precise data request list (field-level where possible), a tracker, and chase messages, and log the permission basis for each pull.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~15 min

**When to use:** Day 1 to 3, and whenever a new analysis needs data

**Phase:** Mobilize and Diagnose

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Minimum
**"What is the smallest dataset that tests the hypothesis?"**

Smaller asks arrive faster.

#### Question 2: The Fallback
**"If the data never arrives, what proxy do we use?"**

Decide now to avoid a blocked week.

---

### The Process

#### Step 1: List the asks

One row per dataset: fields, period, granularity, format, why we need it.

#### Step 2: Assign owners and dates

Counterpart owner and a due date with slack for cleaning.

#### Step 3: Record the permission basis

Who approved sharing, where it is stored, sensitivity level.

#### Step 4: Set a chase rhythm

Daily until in, with an escalation after 2 misses.

#### Step 5: Log receipts and quality

Date received, completeness, issues, who validated.

---

### Structured Output Template

```markdown
# Data Request Tracker: [Engagement]

| # | Dataset | Fields / period | Why needed (hypothesis) | Client owner | Due | Format | Status | Quality notes | Permission basis |
|---|---|---|---|---|---|---|---|---|---|

## Chase Log
| Date | Item | Contact | Response | Next step |
|---|---|---|---|---|
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the data-exploration playbook - Received data to explore
- the model-spec playbook - Data inputs
- the status-update playbook - Data blockers

**Pulls from:**
- the workplan-build playbook - Analyses needing data
- the kickoff-plan playbook - Data owners

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Each ask** links to a hypothesis
- [ ] **Fields and periods** are specific
- [ ] **Owner and due date** are named
- [ ] **Permission basis** is recorded
- [ ] **Fallback** exists for critical items
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `data-exploration` - Profile the received data
- `model-spec` - Plan the model that uses it
- `risk-register` - Track data risk



## Playbook: Ingest Materials (name: ingest-materials)

### Quick Start

Say: **Run the ingest-materials playbook**
Then provide (all optional):
1. **Folders to scan** (default: `context docs/client-materials/` and `context docs/data/`)
2. **Files to prioritize or skip**
3. **Depth**: quick scan (digests only) or deep read (digests plus reconciliation)

I will find new and changed files, read each one in any format, write a one-page digest per file, check what it means for what we already know, and propose exact updates to the fact base, hypotheses, stakeholders, decisions, risks, and data requests. Nothing in `context docs/` changes until you approve each file.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~5 min per document, plus ~15 min for the cross-check and proposal

**When to use:** After you drop files into `client-materials/` or `data/`, after every client data delivery, and before the fact-base playbook, the hypothesis-draft playbook, or a SteerCo

**Phase:** Mobilize through Recommend, and weekly

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: Clearance
**"Is every file in the list cleared to be read here, under the platforms approved in engagement info?"**

Skip anything marked restricted, or that holds personal data (HR, customer names, health), until you confirm. When in doubt, skip and log it.

#### Question 2: Priority
**"Which two or three files matter most this week, and which hypothesis or slide do they feed?"**

Read those first and in depth. The rest get a quick scan.

#### Question 3: Depth
**"Quick scan (digests only) or deep read (digests plus reconciliation to the fact base)?"**

Default to quick scan above 10 files.

---

### The Process

#### Step 1: Inventory and classify

Build one table: file, type (SOW, annual report, board deck, KPI pack, org chart, contract, policy, prior consultant report, data extract, email thread), size, file date, hash, status (new, changed, unchanged, skipped), sensitivity (public, client confidential, restricted), and cleared (yes, no, ask). Show it and confirm before reading.

#### Step 2: Read each file in its own format

- **.md, .txt, .csv:** Read directly. For a CSV, read headers and a sample, never print the whole file.
- **.docx, .pptx:** Convert with `markitdown` or `pandoc`. Keep slide numbers and speaker notes.
- **.pdf:** `pdftotext -layout` for text. For scanned pages, render and read them, and mark the figures as lower confidence.
- **.xlsx:** Use `openpyxl` to list sheets, used ranges, headers, and which cells are formulas. Record sheet and cell references. Do not paste tables. Large datasets go to the data-exploration playbook.
- **Images and charts:** View them. Read values only where they are printed on the chart.
- **Email exports (.eml, .msg):** Headers, thread order, and the ask.
- **Audio and video:** Ask for a transcript. Do not guess.
- **Google Docs, Sheets, Slides:** Read through the Drive connector only with your approval.
- **Cannot read it:** Log it as unreadable and say why. Never infer contents from the file name.

#### Step 3: Write one digest per file

Use the digest template below. Rules: every number carries its unit, period, and location (page, slide, sheet and cell). Quotes are exact and carry a location. Mark what the document **claims** versus what the data **shows**. Record the author and the date.

#### Step 4: Cross-check against what we know

For each digest, compare with:
- **Fact base:** agrees, conflicts, or new for each metric.
- **Hypotheses:** supports, weakens, or no effect, with strength (strong: client data, validated; medium: partial data or benchmark; weak: opinion or analogy).
- **Stakeholders:** new names, role changes, stance signals, reporting lines.
- **Decisions:** definitions or approvals the file implies.
- **Risks:** data quality, scope, confidentiality, political.
- **Data requests:** items satisfied, partly satisfied, or newly needed.
- **Other files:** the same metric with different values. Never pick silently. Show both and ask which the sponsor treats as the source of truth.

#### Step 5: Write the update proposal

One numbered list, grouped by target file. Each update has an ID (U1, U2), the target file and section, the action (add, change, close), the exact text to paste, the evidence (file and location), a confidence, and a decision box (Approve, Edit, Skip). Lead with a "So what" of the three findings that change the answer or the plan.

#### Step 6: Get approval, then apply

Show the proposal and ask which updates to apply. For each approved target:
1. Write the updated copy of the file to `Client folder 01_Outputs/research-synthesis/ingest-[date]/updates/`, mirroring its path in `context docs/`.
2. Only after you say "apply" for that specific file, save a copy of the original to `Client folder 01_Outputs/research-synthesis/ingest-[date]/backup/`, then write the update into `context docs/`.

Never apply an update you have not approved, and never delete or overwrite a client file in `client-materials/` or `data/`. If you say "apply all", I still list every file I changed.

#### Step 7: Update the index

Append one row per file to `Client folder 01_Outputs/research-synthesis/ingest-index.md`: path, hash, date ingested, digest path, updates applied. Files you skipped or left unapproved stay marked **pending** so the next run raises them again.

#### Step 8: Hand off

Name the next skills the findings call for, for example the fact-base playbook for a number conflict, the hypothesis-draft playbook for a moved hypothesis, the stakeholder-map playbook for new people, the risk-register playbook for a new risk, the decision-doc playbook for a definition, the data-request playbook for a gap.

---

### Common Mistakes

- **Ingesting everything at once**: Set a priority and a depth first. Ten files read well beat fifty skimmed.
- **A digest with no locations**: A fact without a page or cell cannot be tied out later.
- **Picking between conflicting numbers silently**: Show both, ask, and log the decision.
- **Treating a client claim as data**: Label claims. A slide saying "churn is 5%" is a claim until the data shows it.
- **Updating the knowledge base without approval**: Proposals first. Edits only on your explicit approval, file by file.
- **Digesting a big dataset**: Profile it with the data-exploration playbook. Digest what it is and where it lives.
- **Reading restricted or personal data**: Ask first. Skip and log when unsure.

---

### Structured Output Template

```markdown
# Digest: [File name]

**Path:** [ ]  |  **Type:** [ ]  |  **Author / source:** [ ]  |  **Date:** [ ]  |  **Sensitivity:** [ ]
**Read in full:** [Y / partial / N]  |  **Hash:** [first 12 characters]

## What it is and why it matters
[2 to 3 sentences. Which question or hypothesis it feeds.]

## Key facts
| ID | Fact | Value | Unit | Period | Location (page / slide / cell) | Claim or data | Confidence |
|---|---|---|---|---|---|---|---|
| F1 | | | | | | | |

## Definitions and terms the client uses
- [Term]: [definition] ([location])

## Quotes worth keeping
- "[Exact quote]" ([location], [who])

## People and organization
- [Name, role, what the document says about them or their stance]

## Checks against what we know
- Fact base: [agrees / conflicts / new, with IDs]
- Hypotheses: [H#: supports / weakens / no effect, strength]
- Other files: [conflicts]

## Open questions
- [ ]
```

```markdown
# Ingest Proposal: [Engagement], [date]

**Files read:** [N]  |  **Skipped:** [N, why]  |  **Pending approval:** [N]

## So what
1. [Finding that changes the answer or the plan]
2. [ ]
3. [ ]

## Conflicts to resolve
| Metric | Source A | Source B | Which does the sponsor treat as correct? |
|---|---|---|---|

## Proposed updates
| ID | Target file and section | Action | Exact text | Evidence (file, location) | Confidence | Decision |
|---|---|---|---|---|---|---|
| U1 | | add / change / close | | | | Approve / Edit / Skip |

## Next skills
- [ ]
```

```markdown
# Ingest Index

| Path | Hash (12) | Ingested | Digest | Updates applied | Status |
|---|---|---|---|---|---|
| | | | | | ingested / pending / skipped / unreadable |
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the fact-base playbook - New and conflicting numbers
- the hypothesis-draft playbook - Evidence for and against
- the stakeholder-map playbook - People and stance signals
- the risk-register playbook - New risks
- the decision-doc playbook - Definitions to agree
- the data-request playbook - Requests closed and opened

**Pulls from:**
- the data-request playbook - What was asked for
- the hypothesis-draft playbook - What the evidence has to test
- the fact-base playbook - Numbers already agreed

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Every file** is accounted for: read, skipped with a reason, or unreadable
- [ ] **Clearance** checked before reading each file
- [ ] **Every number** has a unit, a period, and a location
- [ ] **Quotes** are exact and located
- [ ] **Claims and data** are labeled apart
- [ ] **Conflicts** are shown with both values, not resolved silently
- [ ] **Each proposed update** has exact text, evidence, and a decision box
- [ ] **No file in `context docs/`** changed without your approval for that file, and a backup exists for each
- [ ] **Index** updated, with pending files marked
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `fact-base` - Agree one number per metric
- `data-exploration` - Profile large datasets
- `hypothesis-draft` - Update the hypothesis log
- `stakeholder-map` - Update people and stance
- `risk-register` - Log new risks
- `decision-doc` - Log definitions
- `data-request` - Close and open requests
- `interview-synthesis` - Same method for interview notes


## How this playbook works in Copilot

Add each new file to the Notebook as a reference, then say: Run the ingest-materials playbook on [file names]. There is no file hashing here. Treat a file as new when its name and modified date are not in the ingest index doc. Read each file as provided, write one digest per file, and end with the update proposal (U1, U2 and so on). I cannot write to your files, so each approved update comes back as a CONTEXT UPDATES block: the target context doc, the section, and the exact text to paste. Paste approved updates yourself, then add the ingested files to the ingest index doc.

---




## Playbook: Research Plan (name: research-plan)

### Quick Start

Say: **Run the research-plan playbook**
Then provide:
1. **The question or hypothesis** the research must help answer (or let me pull it from the hypothesis log)
2. **The decision or slide it feeds**
3. **Time box and depth**: quick (about 10 searches), standard (about 25), or deep (50 or more)

I will turn the question into a short list of research questions, map the best sources for each, and show you the plan before I search. After you approve it, I run the searches, log every source with a grade, and write a synthesis that says what moved and what is still open.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~10 min to plan, plus ~30 min to run a standard pass

**When to use:** Before the competitive-landscape playbook, the market-sizing playbook, or the benchmark-analysis playbook when the question is open; whenever a hypothesis needs outside evidence; when the sponsor asks "what do we know about X?"

**Phase:** Diagnose

### Step 1: Diagnostic Questions

#### Question 1: The decision
**"What decision or slide does this research feed, and what would change your mind?"**

Research with no decision behind it becomes a reading list. Name the hypothesis and the result that would weaken it.

#### Question 2: The confidentiality line
**"Is there anything I must keep out of search queries?"**

Default: no client name, no project code name, no internal figures, no names of people we interviewed. Search on the market, the competitor set, or the metric, never on the client's situation.

#### Question 3: Depth and stop rule
**"Quick, standard, or deep? And when do we stop?"**

Default stop rule: stop a research question when two independent sources of grade A or B agree, or when the time box ends. Report what is still open.

---

### The Process

#### Phase A: Plan (show it, get approval, then search)

**1. Turn the question into research questions.** Five to seven at most. Each one is specific and answerable: "What share of [segment] bookings went through [channel] in the last two full years?" beats "Understand the channel landscape." For each, write the hypothesis it tests and the result that would weaken it.

**2. Map the sources.** For each research question, list the best source types in order, and why:
- **Grade A, primary:** regulator filings, annual reports and 10-Ks, statistical agencies, company investor decks, court records, standards bodies, official price lists
- **Grade B, reputable secondary:** industry associations, major business press, peer-reviewed research, analyst summaries with stated method
- **Grade C, weak:** vendor blogs, press releases without data, unsourced listicles, opinion, forums. Use only to find a lead, never as the proof of a number.

**3. Draft the search plan.** For each question: three to five queries, the sites or publishers to favor, and the date window. Prefer primary sources and add the year to queries about current facts.

**4. Set the budget.** Searches and page fetches allowed, time box, and the stop rule.

**5. Run the confidentiality check.** Read every draft query. Remove client identifiers. If web tools are not approved for this engagement, stop and say so.

**6. Show the plan** as the table below and ask for approval or edits before running anything.

#### Phase B: Run

**7. Search in batches by research question.** Send independent searches together. Read the result list, then fetch the pages that look primary. Read the page itself, not just the snippet.

**8. Log every source you use** in the source log: ID (S1, S2), URL, publisher, author or body, publication date, date accessed, source type, and grade (A, B, C).

**9. Record each finding as a claim.** One line each: the claim, the number with unit and period, the source ID and location (section, table, page), and a status:
- **Sourced:** stated in a grade A or B source
- **Corroborated:** two independent sources agree
- **Inferred:** our calculation from sourced inputs (show the inputs)
- **Unverified:** single weak source, or conflicting sources

Any number that drives the answer needs two independent sources, or it is flagged single-source.

**10. Check recency.** For any "current" fact (a price, a rank, a share, a rule in force), find the date. If the newest source is more than 12 months old, say so on the claim.

**11. Handle conflicts and walls.** When sources disagree, show both values and the reason they may differ (definition, period, scope). Do not pick silently. When a page is paywalled, blocked, or will not load, log it as unreachable and ask you to supply the file. Do not try to get around it.

**12. Stop** by the stop rule. List what is still open.

#### Phase C: Synthesize

**13. Write the answer first.** Three sentences: what we learned, what it means for the hypothesis, and what we still do not know.

**14. Findings by research question,** each with its claims, grades, and the effect on the hypothesis (supports, weakens, no effect) with strength: strong (grade A, corroborated), medium (grade B or one A), weak (grade C or inferred).

**15. Close the gaps.** For each open item name the next move: an expert interview (the interview-guide playbook), a client data request (the data-request playbook), a model run, or park it.

**16. Hand off.** Propose the updates to the hypothesis log, fact base, and risk register as a list. Apply nothing to `context docs/` yourself.

---

### Common Mistakes

- **Searching before planning**: Twenty random searches produce a pile, not an answer. Write the research questions first.
- **Putting client details in a query**: Search the market, never the client. Check every query.
- **Trusting the snippet**: Open the page. Snippets drop the period, the unit, and the caveat.
- **Treating a vendor claim as a fact**: A press release saying "40% savings" is a claim from an interested party. Grade it C.
- **One source for a number that drives the answer**: Find a second independent source or flag it.
- **Mixing definitions**: Two "market size" figures often differ in scope or year. Compare the definitions before the numbers.
- **Stale facts stated as current**: Date every current-state claim.
- **Researching what the client already told us**: Read the ingest digests first.
- **Never stopping**: Use the stop rule. Report the open items instead of searching forever.

---

### Structured Output Template

```markdown
# Research Plan: [Topic], [date]

## So what
[Question, decision it feeds, depth, time box, and what would change our mind]

## Research questions
| ID | Research question | Hypothesis tested | Result that would weaken it | Source types (grade) | Queries | Date window |
|---|---|---|---|---|---|---|
| R1 | | H1 | | A: ; B: | | |

## Budget and stop rule
[Searches, fetches, time box, stop rule]

## Confidentiality check
[Terms kept out of queries; web tools approved: yes/no]

## Decision needed
[Approve / edit / cut]
```

```markdown
# Research: [Topic], [date]

## So what
[Three sentences: what we learned, effect on the hypothesis, what is still open]

## Findings
### R1: [Research question]
**Effect on H1:** [supports / weakens / no effect], [strong / medium / weak]
| Claim | Number, unit, period | Source ID and location | Status |
|---|---|---|---|
| | | S1, p. | sourced |

## Conflicts
[Both values, likely reason, who should rule]

## Still open
| Item | Next move | Owner |
|---|---|---|

## Proposed updates
[Hypothesis log, fact base, risk register: exact text, evidence, confidence]

## Source log
| ID | URL | Publisher | Date published | Date accessed | Type | Grade |
|---|---|---|---|---|---|---|
| S1 | | | | | | A |

## Unreachable
[Pages that were blocked or paywalled, and what we needed from them]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the competitive-landscape playbook, the market-sizing playbook, the benchmark-analysis playbook - Sourced inputs
- the hypothesis-draft playbook - Evidence for and against
- the fact-base playbook - External numbers with grades
- the interview-guide playbook - Questions the web could not answer
- the data-request playbook - Client data the research showed we need
- the risk-register playbook - Risks the research surfaced

**Pulls from:**
- the hypothesis-draft playbook - What needs outside evidence
- the ingest-materials playbook - What the client already told us
- the fact-base playbook - Numbers already agreed

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Plan approved** before any search ran
- [ ] **Every research question** ties to a hypothesis and a decision
- [ ] **No client identifiers** appear in any query
- [ ] **Every source** is in the log with URL, date published, date accessed, and a grade
- [ ] **Every number** has a unit, a period, and a source location
- [ ] **Numbers that drive the answer** have two independent sources, or are flagged single-source
- [ ] **Current-state claims** carry a date
- [ ] **Conflicts** are shown with both values
- [ ] **Blocked pages** are logged as unreachable, not worked around
- [ ] **Open items** each have a next move
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every claim has a source or is marked inferred or unverified
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `competitive-landscape` - Map competitors once the facts are in
- `market-sizing` - Size the market from sourced inputs
- `benchmark-analysis` - Compare to peers
- `hypothesis-draft` - Update the hypothesis log
- `ingest-materials` - Digest what the client gave us
- `interview-guide` - Cover what the web cannot
- `data-request` - Ask the client for what only they hold
- `fact-base` - Agree one number per metric


## How this playbook works in Copilot

Use the web search this chat provides. If web search is off or not approved for this client, deliver the research plan only and stop before searching. Keep client names and internal figures out of every query. Give the source log with full URLs so the team can check each one. Save the plan and findings in the client Outputs folder.

---




## Playbook: Day-One Answer (name: day-one-answer)

### Quick Start

Say: **Run the day-one-answer playbook**
Then provide:
1. **The key question**
2. **What you know already** (industry, client, past work)
3. **Your gut view**, even if rough

I will draft the answer as if the SteerCo were tomorrow, name what must be true for it to hold, and turn those into the first analyses.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~15 min

**When to use:** Day 1 and again at every gate

**Phase:** Mobilize; refreshed at gates

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Gut Answer
**"If the SteerCo were tomorrow, what would you recommend?"**

Forces a position that analysis can then test.

#### Question 2: The Flip
**"What fact would reverse the answer?"**

Those facts become the first analyses.

---

### The Process

#### Step 1: State the answer in one sentence

Governing thought: recommendation plus size of prize plus main condition.

#### Step 2: List what must be true

Three to five conditions, each testable.

#### Step 3: Link to analyses

One analysis per condition, ranked by uncertainty and impact.

#### Step 4: Name what would change your mind

Specific data points or findings.

#### Step 5: Version it

Date and version; compare to the last version at each gate.

---

### Structured Output Template

```markdown
# Day-One Answer: [Engagement]

**Version:** [ ]  |  **Date:** [ ]

## Governing Thought
[One sentence: answer, prize, condition]

## What Must Be True
| # | Condition | Test | Confidence | Status |
|---|---|---|---|---|

## What Would Change Our Mind
- [ ]

## Change Since Last Version
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the hypothesis-draft playbook - Conditions become hypotheses
- the storyline playbook - Starting governing thought
- the proposal-draft playbook - Opening hypothesis

**Pulls from:**
- the problem-statement playbook - Question
- the hypothesis-draft playbook - Evidence updates

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **One sentence** answer, not a topic
- [ ] **Conditions** are testable
- [ ] **Flip conditions** are named
- [ ] **Version** and date recorded
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `hypothesis-draft` - Build the log
- `storyline` - Build the storyline
- `skeptic` - Challenge the answer



## Playbook: Issue Tree (name: issue-tree)

### Quick Start

Say: **Run the issue-tree playbook**
Then provide:
1. **The key question**
2. **Any existing structure or framework** you want to test
3. **Depth needed** (default 3 levels)

I will build a MECE tree, test it for gaps and overlaps, tag each leaf with a hypothesis and analysis, and flag where the answer is most uncertain.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~25 min

**When to use:** Right after the problem statement, and when a new branch emerges

**Phase:** Mobilize

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Tree Type
**"Is this a why tree, a how tree, or a driver tree?"**

Mixing types is the commonest MECE failure.

#### Question 2: The Cut
**"What is the cleanest first split (customers, products, channels, time, cost vs revenue)?"**

The first split sets all later branches.

---

### The Process

#### Step 1: Choose tree type

Diagnostic (why), solution (how), or value-driver.

#### Step 2: Draft level 1

Two to five branches. Test: mutually exclusive, collectively exhaustive.

#### Step 3: Draft levels 2 and 3

Stop at leaves that can be tested with a specific analysis.

#### Step 4: Run the MECE test

Look for overlaps (same item in two branches) and gaps (what is missing).

#### Step 5: Tag leaves

For each leaf: hypothesis, analysis, data, owner, confidence.

---

### Structured Output Template

```markdown
# Issue Tree: [Engagement]

**Key question:** [ ]  |  **Tree type:** [Diagnostic / Solution / Driver]

```
Key question
|- 1. [Branch]
|   |- 1.1 [Leaf] - H[ ] - [analysis]
|   |- 1.2 [Leaf]
|- 2. [Branch]
```

## MECE Test
| Check | Result | Fix |
|---|---|---|

## Leaf Tags
| Leaf | Hypothesis | Analysis | Data | Owner | Confidence |
|---|---|---|---|---|---|
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the hypothesis-draft playbook - Branches to hypothesize on
- the workplan-build playbook - Modules
- the prioritize-analyses playbook - Leaves to rank

**Pulls from:**
- the problem-statement playbook - Root question
- the interview-synthesis playbook - Field evidence

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Siblings** are mutually exclusive
- [ ] **Branches** together cover the question
- [ ] **No leaf** is untestable
- [ ] **Depth** is consistent across branches
- [ ] **Tree type** is not mixed
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `hypothesis-draft` - Write hypotheses per branch
- `prioritize-analyses` - Rank leaves
- `value-driver-tree` - Quantify drivers



## Playbook: Hypothesis Draft (name: hypothesis-draft)

### Quick Start

Say: **Run the hypothesis-draft playbook**
Then provide:
1. **The issue tree or the key question**
2. **What you already believe and why**
3. **Early evidence** (interviews, data, benchmarks)

I will turn the issue tree into falsifiable hypotheses, define the test that would kill each, and keep the log current as evidence arrives.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~20 min initial; ~10 min per update

**When to use:** After the issue tree, then after every new analysis or interview round

**Phase:** Mobilize through Recommend

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Kill Test
**"What result would make you drop this hypothesis?"**

If nothing would, it is a belief, not a hypothesis.

#### Question 2: The Threshold
**"What number turns this from 'probably' to 'proven'?"**

Set it before looking at the data.

---

### The Process

#### Step 1: Write one hypothesis per leaf

Specific, falsifiable, with direction and size where possible.

#### Step 2: Define the test

Analysis, data, threshold, owner, date.

#### Step 3: Log evidence

For and against, with source and confidence.

#### Step 4: Update status

Open, supported, partly supported, rejected; note what changed.

#### Step 5: Reshape the answer

Update the Day-1 answer if a key hypothesis moves.

---

### Structured Output Template

```markdown
# Hypothesis Log: [Engagement]

| ID | Hypothesis | Branch | Test and threshold | Evidence for | Evidence against | Confidence | Status | Owner | Updated |
|---|---|---|---|---|---|---|---|---|---|

## Changes Since Last Update
[What moved and why]

## Impact on the Answer
[Does the Day-1 answer change?]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the storyline playbook - Confirmed hypotheses become the storyline
- the prioritize-analyses playbook - Tests to rank
- the status-update playbook - Progress against hypotheses

**Pulls from:**
- the issue-tree playbook - Leaf structure
- the interview-synthesis playbook - Evidence
- the ingest-materials playbook - New evidence and conflicts from client materials
- the research-plan playbook - Sourced outside evidence, graded

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Each hypothesis** is falsifiable
- [ ] **Each test** has a threshold
- [ ] **Evidence** cites sources
- [ ] **Rejected hypotheses** are kept, with the reason
- [ ] **Day-1 answer** is checked against the log
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `day-one-answer` - Update the answer
- `storyline` - Build the storyline
- `skeptic` - Challenge the evidence



## Playbook: Prioritize Analyses (name: prioritize-analyses)

### Quick Start

Say: **Run the prioritize-analyses playbook**
Then provide:
1. **The candidate analyses** (or point me to the issue tree)
2. **Team capacity** until the next gate
3. **Data status**

I will score each analysis, plot it on an impact-effort matrix, and recommend the next-two-weeks plan with explicit parked items.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~20 min

**When to use:** Start of each phase and whenever the list of possible analyses outgrows capacity

**Phase:** Mobilize and Diagnose

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Gate
**"Which gate is the binding constraint?"**

Prioritize for the next decision, not for completeness.

#### Question 2: The Swing
**"Which analysis could change the recommendation the most?"**

Those get run first even if hard.

---

### The Process

#### Step 1: List candidates

One line each with the hypothesis it tests.

#### Step 2: Score impact and effort

Impact on the answer 1 to 5; effort in days; data readiness; confidence in the result.

#### Step 3: Plot the matrix

Do now, schedule, quick check, park.

#### Step 4: Apply the 80/20 rule

Cut analyses that cannot change the answer.

#### Step 5: Agree with the EM

Record parked items and why.

---

### Structured Output Template

```markdown
# Analysis Prioritization: [Engagement]

| Analysis | Hypothesis | Impact (1-5) | Effort (days) | Data ready? | Quadrant | Decision | Owner |
|---|---|---|---|---|---|---|---|

## Matrix
```
High impact | Schedule | Do now
Low impact  | Park     | Quick check
            Hard       Easy
```

## Parked and Why
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the workplan-build playbook - Updated plan
- the daily-plan playbook - Daily focus

**Pulls from:**
- the issue-tree playbook - Candidates
- the hypothesis-draft playbook - Uncertainty

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Every analysis** links to a hypothesis
- [ ] **Scores** have a one-line reason
- [ ] **Parked items** are recorded
- [ ] **Capacity** fits the next gate
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `workplan-build` - Update the plan
- `hypothesis-draft` - Update hypotheses
- `decision-doc` - Log scope trade-offs



## Playbook: Interview Guide (name: interview-guide)

### Quick Start

Say: **Run the interview-guide playbook**
Then provide:
1. **Who you are interviewing** (role, seniority, relationship)
2. **Hypotheses to test** with this person
3. **Time available** (30, 45, or 60 minutes)

I will write a hypothesis-linked guide with opening, open questions, probes, and a close, plus a note-taking grid.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~15 min

**When to use:** Before each interview round: executives, frontline, customers, experts

**Phase:** Diagnose

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The One Thing
**"If you learn only one thing from this person, what is it?"**

Everything else is optional; this question is mandatory.

#### Question 2: The Risk
**"Is there anything they should not be asked or told?"**

Protect the client and the interviewee.

---

### The Process

#### Step 1: Pick the objective

One sentence: what we need to learn and which hypothesis it supports.

#### Step 2: Write the opener

Purpose, confidentiality, how notes are used, time check.

#### Step 3: Draft 6 to 8 open questions

Start broad, narrow with probes. No leading questions.

#### Step 4: Add probes and quantification asks

'Can you give an example?' 'How many?' 'How often?'

#### Step 5: Close and next steps

Ask who else to speak to, what data exists, and permission to follow up.

---

### Structured Output Template

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

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the interview-synthesis playbook - Notes structure
- the hypothesis-draft playbook - Evidence
- the stakeholder-map playbook - Stance signals

**Pulls from:**
- the hypothesis-draft playbook - Tests
- the stakeholder-map playbook - Sensitivities

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Questions** are open and non-leading
- [ ] **Every question** links to a hypothesis or is marked exploratory
- [ ] **Timing** fits the slot
- [ ] **Confidentiality** wording is included
- [ ] **Referral ask** is in the close
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `interview-synthesis` - Synthesize findings
- `survey-design` - Scale with a survey
- `hypothesis-draft` - Update hypotheses



## Playbook: Interview Synthesis (name: interview-synthesis)

### Quick Start

Say: **Run the interview-synthesis playbook**
Then provide:
1. **Interview notes** (paste or files in `context docs/interviews/`)
2. **Hypotheses** being tested
3. **Number and mix of interviewees**

I will cluster themes, count support, pull verbatim quotes, flag contradictions, and say what changes in the hypothesis log.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~25 min for 8 to 12 interviews

**When to use:** After each interview round, before the next SteerCo

**Phase:** Diagnose

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Weight
**"Which interviews should count more, and why?"**

Frontline vs executive views may diverge on purpose.

#### Question 2: The Surprise
**"What did you hear that you did not expect?"**

Surprises often become the insight.

---

### The Process

#### Step 1: Code the notes

Tag each statement with a theme, interviewee type, and fact vs opinion.

#### Step 2: Count and cluster

Number of interviewees per theme and per segment.

#### Step 3: Pick verbatim quotes

Two per major theme, anonymized unless agreed.

#### Step 4: Flag contradictions

Between groups, and between interviews and data.

#### Step 5: Update hypotheses

Supported, weakened, or new; list the follow-ups.

---

### Structured Output Template

```markdown
# Interview Synthesis: [Round]

**Interviews:** [n]  |  **Mix:** [ ]  |  **Dates:** [ ]

## Headline
[Three-sentence so-what]

## Themes
| Theme | Interviewees (n of N) | Segments | Strength | Representative quote |
|---|---|---|---|---|

## Contradictions
[ ]

## Hypothesis Impact
| Hypothesis | Change | Evidence |
|---|---|---|

## Follow-ups
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the hypothesis-draft playbook - Evidence
- the slide-draft playbook - Quotes for slides
- the change-plan playbook - Voice of employees

**Pulls from:**
- the interview-guide playbook - Guide used
- the stakeholder-map playbook - Roles

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **n of N** shown for each theme
- [ ] **Quotes** are verbatim and anonymized
- [ ] **Opinions** are not presented as facts
- [ ] **Contradictions** are listed
- [ ] **Hypothesis log** is updated
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `hypothesis-draft` - Update the log
- `root-cause-analysis` - Test causes
- `storyline` - Use in the story



## Playbook: Survey Design (name: survey-design)

### Quick Start

Say: **Run the survey-design playbook**
Then provide:
1. **The hypothesis** the survey tests
2. **Population and sample size**
3. **Channel and timing**

I will write the questionnaire, the sampling plan, and the analysis plan before any responses arrive, and flag bias risks.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** Interviews suggest a pattern that needs quantifying

**Phase:** Diagnose

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Decision
**"What result would change the recommendation?"**

Writes the analysis plan before launch.

---

### The Process

#### Step 1: Define the objective and the decision rule

What result changes what.

#### Step 2: Design the sample

Segments, size, quotas, response rate assumption.

#### Step 3: Write questions

Neutral, one idea per question, consistent scales.

#### Step 4: Plan the analysis

Cuts, significance, how results map to hypotheses.

#### Step 5: Pilot

Five respondents; fix wording; then launch.

---

### Structured Output Template

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

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the data-exploration playbook - Results
- the hypothesis-draft playbook - Evidence

**Pulls from:**
- the interview-synthesis playbook - Wording

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Questions** are neutral
- [ ] **Sample** supports the cuts planned
- [ ] **Decision rule** set before launch
- [ ] **Consent and privacy** addressed
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `interview-guide` - Add depth
- `data-exploration` - Profile results
- `root-cause-analysis` - Test causes



## Playbook: Fact Base (name: fact-base)

### Quick Start

Say: **Run the fact-base playbook**
Then provide:
1. **The baseline period** and metrics
2. **Client sources** for each metric
3. **Known disagreements** between sources

I will produce a single agreed set of baseline numbers with sources, definitions, and reconciliations, so every page uses the same facts.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** Weeks 1 to 3, and whenever a core number is disputed

**Phase:** Diagnose

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Source of Truth
**"Which system or report does the CFO treat as correct?"**

The fact base must match their number.

---

### The Process

#### Step 1: List the metrics

Only those used on slides or in the model.

#### Step 2: Assign a source per metric

With owner, date, and definition.

#### Step 3: Reconcile conflicts

Explain gaps and pick one number; log the decision.

#### Step 4: Get client sign-off

CFO or counterpart confirms.

#### Step 5: Publish

One-page fact sheet linked from the model Inputs tab.

---

### Structured Output Template

```markdown
# Fact Base: [Engagement]

**Baseline period:** [ ]  |  **Signed off by:** [ ]  |  **Date:** [ ]

| Metric | Value | Unit | Definition | Source | Owner | Date | Conflicts resolved |
|---|---|---|---|---|---|---|---|

## Conflicts and Decisions
| Metric | Source A | Source B | Chosen | Why |
|---|---|---|---|---|
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the model-spec playbook - Baseline inputs
- the number-tie-out playbook - Reference numbers
- the slide-draft playbook - Facts on slides

**Pulls from:**
- the data-exploration playbook - Reconciled data
- the ingest-materials playbook - Digested client materials and conflicts

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **One number per metric**
- [ ] **Definition and source** recorded
- [ ] **Conflicts** resolved and logged
- [ ] **Client sign-off** obtained
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `number-tie-out` - Tie every page
- `model-spec` - Plan the model
- `decision-doc` - Log definitions



## Playbook: Data Exploration (name: data-exploration)

### Quick Start

Say: **Run the data-exploration playbook**
Then provide:
1. **The data file(s)**
2. **What the data should show** (and a reported figure to reconcile to)
3. **The analysis it feeds**

I will profile each field, flag quality issues, reconcile to a reported total, document cleaning steps, and produce a clean, versioned dataset.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** Every time new client data arrives, before any analysis uses it

**Phase:** Diagnose

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Control Total
**"Which reported number should the data reconcile to?"**

Without a control total, errors are invisible.

---

### The Process

#### Step 1: Inventory

Rows, columns, period, keys, date received.

#### Step 2: Profile

Missing, duplicates, ranges, outliers per field.

#### Step 3: Reconcile

Sum to the reported figure; explain gaps.

#### Step 4: Clean

Rules logged one by one; never overwrite raw data.

#### Step 5: Document

Data dictionary and a list of open questions for the client.

---

### Structured Output Template

```markdown
# Data Profile: [Dataset]

**Source / owner / date:** [ ]  |  **Rows:** [ ]  |  **Period:** [ ]

## Reconciliation
| Check | Data | Reported | Gap | Explanation |
|---|---|---|---|---|

## Field Profile
| Field | Type | Missing % | Distinct | Min / Max | Issue |
|---|---|---|---|---|---|

## Cleaning Log
| # | Rule | Rows affected | Rationale |
|---|---|---|---|

## Open Questions to Client
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the model-spec playbook - Clean inputs
- the root-cause-analysis playbook - Reliable data
- the benchmark-analysis playbook - Client values

**Pulls from:**
- the data-request playbook - Source and owner

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Reconciled** to a reported total
- [ ] **Cleaning steps** are logged
- [ ] **Raw file** is untouched
- [ ] **Open questions** go back to the client
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `data-request` - Ask for corrections
- `model-spec` - Plan the model
- `root-cause-analysis` - Find causes



## Playbook: Market Sizing (name: market-sizing)

### Quick Start

Say: **Run the market-sizing playbook**
Then provide:
1. **The market definition** (product, geography, segment, time)
2. **Data you have** (reports, client sales, benchmarks)
3. **The decision** the size supports

I will build a top-down and a bottom-up estimate, reconcile them, show a range, and list the assumptions that matter most.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** Sizing an opportunity, a new market, or a growth target

**Phase:** Diagnose and Develop

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Boundary
**"Which products, geographies, and customer types are in or out?"**

Boundary choices change the answer more than math does.

#### Question 2: The Decision
**"What size would change the decision?"**

A rough range is enough if it does not cross the threshold.

---

### The Process

#### Step 1: Define the market

Product, geography, segment, year, currency.

#### Step 2: Top-down

Start from a published total and narrow by segment, share, and relevance.

#### Step 3: Bottom-up

Units x price x frequency x customers; use client data where possible.

#### Step 4: Reconcile

Explain gaps over 20%; choose a base and a range.

#### Step 5: Stress the drivers

Vary the top three assumptions; show their effect.

---

### Common Mistakes

- **Using one source**: Triangulate with at least two independent sources.
- **Mixing years or currencies**: State year and currency on every number.

---

### Structured Output Template

```markdown
# Market Sizing: [Market]

**Boundary:** [Product / geography / segment / year / currency]

## Answer
[Base size and range in one sentence]

## Top-Down
| Step | Value | Source |
|---|---|---|

## Bottom-Up
| Driver | Value | Source |
|---|---|---|

## Reconciliation
[Gap and explanation]

## Sensitivity
| Assumption | Low | Base | High | Effect on size |
|---|---|---|---|---|
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the initiative-sizing playbook - Addressable base
- the model-spec playbook - Inputs
- the slide-draft playbook - Chart

**Pulls from:**
- the benchmark-analysis playbook - Comparables
- the data-request playbook - Client data

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Boundary** is explicit
- [ ] **Two methods** are reconciled
- [ ] **Range** is shown
- [ ] **Sources and years** are cited
- [ ] **Units and currency** are consistent
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `initiative-sizing` - Size the prize
- `benchmark-analysis` - Compare to peers
- `model-spec` - Plan the model



## Playbook: Benchmark Analysis (name: benchmark-analysis)

### Quick Start

Say: **Run the benchmark-analysis playbook**
Then provide:
1. **The metrics** to benchmark
2. **Peer set** and why they are comparable
3. **Client data** for the same metrics and period

I will normalize definitions, build the peer comparison, size the gap to median and top quartile, and caveat comparability.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** Diagnose phase; sizing improvement potential; supporting a target

**Phase:** Diagnose

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Peer Set
**"Which peers would the sponsor accept as fair comparison?"**

A benchmark the sponsor rejects will not drive action.

#### Question 2: The Definition
**"How does each source define the metric?"**

Mismatched definitions are the main benchmarking error.

---

### The Process

#### Step 1: Choose metrics and peers

Limit to metrics that connect to the key question.

#### Step 2: Normalize

Align period, currency, scope, and definition; log adjustments.

#### Step 3: Compare

Median, quartiles, best-in-class; show client position.

#### Step 4: Size the gap

Gap x client base = value if closed; show a haircut.

#### Step 5: Caveat

What the benchmark cannot tell us; what would a skeptic say.

---

### Structured Output Template

```markdown
# Benchmark: [Topic]

## So-What
[Client is X vs median; closing half the gap is worth $Y]

## Peer Set and Rationale
| Peer | Why included | Source | Year |
|---|---|---|---|

## Normalization Log
| Adjustment | Reason | Effect |
|---|---|---|

## Comparison
| Metric | Client | Median | Top quartile | Gap | Value of gap |
|---|---|---|---|---|---|

## Caveats
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the initiative-sizing playbook - Gap to size
- the slide-draft playbook - Chart
- the hypothesis-draft playbook - Evidence

**Pulls from:**
- the competitive-landscape playbook - Peer set
- the data-request playbook - Client data

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Definitions** are aligned
- [ ] **Adjustments** are logged
- [ ] **Sources and years** are cited
- [ ] **Gap value** has a haircut
- [ ] **Caveats** are stated
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `initiative-sizing` - Convert gap to value
- `root-cause-analysis` - Explain the gap
- `slide-draft` - Make the chart



## Playbook: Competitive Landscape (name: competitive-landscape)

### Quick Start

Say: **Run the competitive-landscape playbook**
Then provide:
1. **The client and market**
2. **Competitors to include** (or let me suggest)
3. **What decision** the landscape informs

I will build a competitor profile set and a positioning map focused on the decision, with evidence and gaps flagged.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~35 min with web research

**When to use:** Diagnose phase; market entry; positioning; pricing

**Phase:** Diagnose

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Decision
**"What would we do differently if a competitor moved?"**

Scope the landscape to what drives a decision.

#### Question 2: The Axes
**"Which two dimensions matter most to customers?"**

They define the positioning map.

---

### The Process

#### Step 1: Define the field

Direct, indirect, new entrants, substitutes.

#### Step 2: Profile each

Offer, price, scale, strengths, moves, evidence.

#### Step 3: Map positioning

Two axes chosen from customer evidence.

#### Step 4: Draw implications

Where the client wins, loses, and what moves are likely.

#### Step 5: List gaps

What we could not verify and who could.

---

### Structured Output Template

```markdown
# Competitive Landscape: [Market]

## So-What
[Implication for the client]

## Competitor Profiles
| Competitor | Offer | Scale | Price | Strengths | Weaknesses | Recent moves | Source |
|---|---|---|---|---|---|---|---|

## Positioning Map
[Axes and placement]

## Implications
[ ]

## Gaps
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the benchmark-analysis playbook - Peer set
- the storyline playbook - Context pages
- the slide-draft playbook - Visual

**Pulls from:**
- the interview-synthesis playbook - Customer view
- the market-sizing playbook - Size

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Every claim** has a source and date
- [ ] **Axes** come from customer evidence
- [ ] **Implications** link to the decision
- [ ] **Gaps** are listed
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `benchmark-analysis` - Quantify the gap
- `market-sizing` - Size the market
- `slide-draft` - Visualize



## Playbook: Value Driver Tree (name: value-driver-tree)

### Quick Start

Say: **Run the value-driver-tree playbook**
Then provide:
1. **The financial outcome** (EBITDA, margin, NPV, cash)
2. **Baseline data**
3. **Candidate levers**

I will build the driver tree to measurable leaves, attach baseline values, and mark which drivers are controllable and which carry the most value.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** Sizing improvement, linking operations to the P&L, setting targets

**Phase:** Diagnose and Develop

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Outcome
**"Which single financial number must move?"**

All drivers must roll up to it.

---

### The Process

#### Step 1: State the outcome

Pick one metric and its baseline.

#### Step 2: Decompose

Revenue = volume x price x mix; cost by fixed/variable and by activity.

#### Step 3: Attach values

Baseline per leaf; mark source and quality.

#### Step 4: Rate each driver

Controllable? Sensitivity? Evidence for a lever?

#### Step 5: Rank

Sensitivity x controllability gives the shortlist of levers.

---

### Structured Output Template

```markdown
# Value Driver Tree: [Outcome]

```
[Outcome]
|- Revenue
|   |- Volume x Price x Mix
|- Cost
|   |- Variable / Fixed
```

## Driver Table
| Driver | Baseline | Unit | Source | Controllable? | Sensitivity | Lever idea |
|---|---|---|---|---|---|---|

## Shortlist of Levers
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the initiative-sizing playbook - Levers to size
- the model-spec playbook - Model structure
- the slide-draft playbook - Tree graphic

**Pulls from:**
- the issue-tree playbook - Structure
- the data-exploration playbook - Baseline

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Tree rolls up** exactly to the outcome
- [ ] **Baseline** ties to a source
- [ ] **Controllable** vs not is marked
- [ ] **Leaves** are measurable
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `initiative-sizing` - Size levers
- `model-spec` - Plan the model
- `benchmark-analysis` - Target values



## Playbook: Root Cause Analysis (name: root-cause-analysis)

### Quick Start

Say: **Run the root-cause-analysis playbook**
Then provide:
1. **The gap or problem** with numbers
2. **Data available** for splits
3. **Hypotheses on cause**

I will split the problem by dimension, test each cause hypothesis, and give a ranked list of root causes with evidence and confidence.

**Output:** Delivered in chat. Copy into Word or Excel and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** A KPI is off, a gap is found, or interviews and data disagree

**Phase:** Diagnose

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Split
**"Where is the gap concentrated (segment, site, time, product)?"**

Concentration points to cause.

---

### The Process

#### Step 1: Quantify the gap

Size, trend, and where it is largest.

#### Step 2: Split by dimension

Pareto the gap by segment, time, product, region.

#### Step 3: List cause hypotheses

Structured by driver tree.

#### Step 4: Test each

With data or field evidence; record result.

#### Step 5: Rank root causes

Evidence strength x share of gap explained.

---

### Structured Output Template

```markdown
# Root Cause Analysis: [Topic]

## So-What
[Primary cause and share of gap explained]

## Gap Quantified
[ ]

## Splits
| Dimension | Finding | Share of gap |
|---|---|---|

## Cause Hypotheses
| Cause | Test | Result | Evidence strength | Share explained |
|---|---|---|---|---|

## Root Causes Ranked
1. [ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the options-evaluation playbook - Causes to address
- the storyline playbook - Diagnostic pages
- the hypothesis-draft playbook - Updates

**Pulls from:**
- the data-exploration playbook - Clean data
- the interview-synthesis playbook - Field evidence

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Cause vs symptom** is distinguished
- [ ] **Shares** sum to the gap or explain the rest
- [ ] **Evidence** cited for each cause
- [ ] **Alternatives** considered
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `options-evaluation` - Choose fixes
- `value-driver-tree` - Link to value
- `skeptic` - Challenge

