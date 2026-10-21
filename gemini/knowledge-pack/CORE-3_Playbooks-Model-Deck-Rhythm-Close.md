# Consulting OS Core 3: Playbooks, Model, Recommend, Deck, Rhythm and Close

Each playbook is one task. In Gemini, trigger one by saying: Run the [name] playbook. Follow its questions, process and template. Deliver in chat.

# Section A: Model, recommend, storyline and deck


## Playbook: Initiative Sizing (name: initiative-sizing)

### Quick Start

Say: **Run the initiative-sizing playbook**
Then provide:
1. **The initiatives** (or point me to the driver tree)
2. **Baseline and benchmark data**
3. **Evidence for uplift** (pilots, peers, interviews)

I will size each initiative on a common basis (run-rate EBITDA, one-time cost, ramp, confidence), show Low/Base/High, and rank by value and ease.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~35 min

**When to use:** Develop phase, before the Solutions SteerCo

**Phase:** Develop

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Evidence
**"What evidence supports the uplift: pilot, peer, expert, or assumption?"**

Weight confidence by evidence type.

#### Question 2: The Cash
**"What one-time cost and which year does it hit?"**

Value without cost is not a business case.

---

### The Process

#### Step 1: Define each initiative

Scope, owner, mechanism, baseline.

#### Step 2: Size run-rate value

Baseline x uplift x flow-through; Low / Base / High.

#### Step 3: Add ramp and cost

Year-by-year ramp; one-time cost phasing.

#### Step 4: Apply a haircut

Confidence-weight; mark overlaps to avoid double counting.

#### Step 5: Rank

Value vs ease; sum with overlap removed.

---

### Common Mistakes

- **Double counting**: Two initiatives that move the same cost line must be netted.
- **Gross vs net**: Show EBITDA after flow-through, not revenue.

---

### Structured Output Template

```markdown
# Initiative Sizing: [Engagement]

## So-What
[Total run-rate EBITDA range and one-time cost]

| Initiative | Mechanism | Baseline | Uplift (L/B/H) | Flow-through | Run-rate EBITDA (L/B/H) | One-time cost | Ramp | Confidence | Evidence |
|---|---|---|---|---|---|---|---|---|---|

## Overlaps Removed
[ ]

## Ranking
| Initiative | Value | Ease | Priority |
|---|---|---|---|
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the model-spec playbook - Model inputs
- the options-evaluation playbook - Options to rank
- the roadmap-build playbook - Sequence

**Pulls from:**
- the value-driver-tree playbook - Levers
- the benchmark-analysis playbook - Gap
- the fact-base playbook - Baseline

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Run-rate and one-time** are separated
- [ ] **Low/Base/High** shown
- [ ] **Overlaps** removed
- [ ] **Evidence type** is stated
- [ ] **Baseline** ties to the fact base
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `model-spec` - Plan the model
- `options-evaluation` - Rank
- `scenario-sensitivity` - Stress test



## Playbook: Model Spec (name: model-spec)

### Quick Start

Say: **Run the model-spec playbook**
Then provide:
1. **The three questions** the model must answer
2. **Inputs and sources**
3. **Audience and decisions**

I will write a one-to-two page spec that a second person could build from, including tabs, input list, logic, outputs, checks, and the review plan.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~25 min

**When to use:** Before any model is built, and when scope of a model changes

**Phase:** Mobilize through Develop

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Questions
**"What three questions must this model answer?"**

A model with no stated question becomes a data dump.

#### Question 2: The Granularity
**"Monthly, quarterly, or annual? By segment or total?"**

Granularity drives size and error risk.

---

### The Process

#### Step 1: State the questions and audience

Who will use the outputs and for what decision.

#### Step 2: Sketch the structure

Tabs and flow: Cover, Guide, Inputs, Calc, Scenarios, Outputs, Checks, Log.

#### Step 3: List inputs

Each with unit, source, owner, scenario values.

#### Step 4: Describe calculations

In words and in formula pattern per block.

#### Step 5: Define outputs and checks

Outputs by slide; integrity and sense checks; owner; reviewer.

---

### Structured Output Template

```markdown
# Model Spec: [Model]

**Owner:** [ ]  |  **Reviewer:** [ ]  |  **Version:** [ ]

## Questions
1. [ ]

## Structure
| Tab | Purpose | Inputs from | Outputs to |
|---|---|---|---|

## Inputs
| Ref | Input | Unit | Low | Base | High | Source | Owner |
|---|---|---|---|---|---|---|---|

## Calculation Logic
[Blocks and formulas in words]

## Outputs
| Output | Used on slide | Definition |
|---|---|---|

## Checks
| Check | Test | Tolerance |
|---|---|---|

## Review Plan
[Independent review method and date]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the model-build playbook - Spec to build
- the model-audit playbook - Audit reference
- the scenario-sensitivity playbook - Scenario design

**Pulls from:**
- the fact-base playbook - Baselines
- the initiative-sizing playbook - Logic

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Three questions** are stated
- [ ] **Inputs** have unit and source
- [ ] **Checks** are defined before building
- [ ] **Owner and reviewer** named
- [ ] **Starter template** is used: the model starter template (inputs, calc, scenarios, outputs, checks, log tabs)
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `model-build` - Build it
- `model-audit` - Audit it
- `scenario-sensitivity` - Stress it



## Playbook: Model Build (name: model-build)

### Quick Start

Say: **Run the model-build playbook**
Then provide:
1. **The model spec**
2. **Input data** (clean and sourced)
3. **The starter file** (default: the model starter template (inputs, calc, scenarios, outputs, checks, log tabs))

I will build the workbook with openpyxl from the spec, recalculate with LibreOffice, confirm zero errors and green checks, and hand it over with a guide tab.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~45 to 90 min depending on size

**When to use:** After the spec is agreed

**Phase:** Develop

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Reviewer
**"Who reviews the model independently, and when?"**

Review is planned, not optional.

---

### The Process

#### Step 1: Copy the starter

Never build from a blank sheet; keep Cover, Guide, Inputs, Calc, Scenarios, Outputs, Checks, Log.

#### Step 2: Enter inputs

Blue font, one cell per assumption, unit, source, owner, date, confidence.

#### Step 3: Build calculations

One formula per row copied across; no hardcodes; no merged cells; no OFFSET or INDIRECT.

#### Step 4: Build outputs and checks

Outputs tab feeds slides; checks roll up to a master flag on the Cover.

#### Step 5: Recalculate and test

Run LibreOffice recalc; confirm zero errors; flex inputs and watch outputs move sensibly.

---

### Common Mistakes

- **Typing numbers into formulas**: Every number lives on the Inputs tab.
- **Silent circularity**: No circular references; use explicit iteration blocks if needed and document them.

---

### Structured Output Template

```markdown
# Model Build Note: [Model]

**File:** [name]  |  **Owner:** [ ]  |  **Version:** [ ]

## What was built
[Tabs and logic]

## Recalc Result
Errors: [0]  |  Integrity flags: [0]  |  Sense flags: [ ]

## Tests Run
| Test | Input change | Expected | Observed |
|---|---|---|---|

## Known Limits
[ ]

## Next Step
[Independent audit by [name]]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the model-audit playbook - File to audit
- the number-tie-out playbook - Outputs to tie
- the scenario-sensitivity playbook - Live model

**Pulls from:**
- the model-spec playbook - Spec
- the data-exploration playbook - Clean data

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Zero errors** after recalculation
- [ ] **No hardcodes** in formulas
- [ ] **Inputs** sourced and dated
- [ ] **Checks tab** rolls up to the Cover
- [ ] **Guide tab** explains the model
- [ ] **File name** follows `[Model]_[STATUS]_[vDATE]_[initials].xlsx`
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `model-audit` - Audit the model
- `number-tie-out` - Tie numbers
- `scenario-sensitivity` - Run scenarios



## Playbook: Model Audit (name: model-audit)

### Quick Start

Say: **Run the model-audit playbook**
Then provide:
1. **The model file**
2. **The spec and sources**
3. **Reasonableness anchors** (benchmarks, reported totals)

I will test the model five ways and return a findings list with severity, location, and fix, plus a sign-off recommendation.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~40 min

**When to use:** Before any model output goes to the client

**Phase:** Develop and Recommend

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Anchor
**"What reported figure or benchmark should the base case be near?"**

A model that lands far from anchors needs explaining.

---

### The Process

#### Step 1: Inputs vs sources

Sample every input back to its source.

#### Step 2: Formula review

Pattern consistency across rows, hardcodes, ranges, units, signs.

#### Step 3: Output vs benchmark

Compare to reported results and peer ranges.

#### Step 4: Back-of-envelope

Rebuild the answer in 10 lines; compare.

#### Step 5: Standards check

Colors, structure, checks, log; then sign-off recommendation.

---

### Structured Output Template

```markdown
# Model Audit: [Model]

**Auditor:** [ ]  |  **Date:** [ ]  |  **Version audited:** [ ]

## Verdict
[Ready / Ready after fixes / Not ready]

## Findings
| # | Severity (H/M/L) | Tab / cell | Issue | Impact | Fix | Status |
|---|---|---|---|---|---|---|

## Tests Run
| Method | Result |
|---|---|
| Inputs vs sources | |
| Formulas | |
| Outputs vs benchmark | |
| Back-of-envelope | |
| Standards | |
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the model-build playbook - Fixes
- the number-tie-out playbook - Cleared outputs

**Pulls from:**
- the model-spec playbook - Intent
- the fact-base playbook - Anchors

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Five methods** were run
- [ ] **Each finding** has location and fix
- [ ] **Severity** reasoning is stated
- [ ] **Sign-off** recommendation is explicit
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `model-build` - Apply fixes
- `number-tie-out` - Re-tie numbers
- `scenario-sensitivity` - Stress after fixes



## Playbook: Scenario and Sensitivity Analysis (name: scenario-sensitivity)

### Quick Start

Say: **Run the scenario-sensitivity playbook**
Then provide:
1. **The model** and its key outputs
2. **The uncertain assumptions**
3. **The decision threshold** (what NPV or margin changes the decision)

I will run Low/Base/High scenarios and one-at-a-time sensitivities, produce a tornado ranking, and identify the break-even conditions.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~25 min

**When to use:** Before a financial case goes to the SteerCo

**Phase:** Develop and Recommend

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Threshold
**"At what value does the decision flip?"**

Break-even is more useful than a fan of cases.

---

### The Process

#### Step 1: Define scenarios

Low, Base, High with a narrative each, not just numbers.

#### Step 2: Run the cases

Switch the selector; paste outputs as values into the Log tab with date.

#### Step 3: Run one-at-a-time sensitivities

Vary each key input by a fixed range; record effect on the output.

#### Step 4: Rank

Tornado of effects; top three assumptions named.

#### Step 5: Find break-evens

Input value at which the decision flips.

---

### Structured Output Template

```markdown
# Scenario and Sensitivity: [Model]

## So-What
[Answer holds in Low case / flips if X falls below Y]

## Scenarios
| Scenario | Narrative | Key inputs | Output (NPV / EBITDA) |
|---|---|---|---|

## Sensitivity (tornado)
| Input | Low | High | Output at low | Output at high | Swing |
|---|---|---|---|---|---|

## Break-evens
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the slide-draft playbook - Charts
- the recommendation playbook - Risk-adjusted case
- the risk-register playbook - Key assumptions

**Pulls from:**
- the model-build playbook - Model
- the initiative-sizing playbook - Ranges

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Scenario narratives** exist
- [ ] **Ranges** have a source
- [ ] **Break-even** is stated
- [ ] **Results** are pasted as values with date
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `recommendation` - Use in the recommendation
- `slide-draft` - Visualize
- `risk-register` - Log key risks



## Playbook: Number Tie-Out (name: number-tie-out)

### Quick Start

Say: **Run the number-tie-out playbook**
Then provide:
1. **The deck** (pptx or text)
2. **The model and fact base**
3. **Version**

I will extract each number on each slide, trace it to a model cell or source, flag mismatches and rounding issues, and give you a signed tie-out log.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~30 min for a 20-page deck

**When to use:** Before every SteerCo and the final readout; after any model change

**Phase:** Develop through Transition

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Rounding Rule
**"One decimal for $M, whole % for shares, or something else?"**

Consistency prevents fake mismatches.

---

### The Process

#### Step 1: Extract numbers

Per slide: value, unit, label, chart or text.

#### Step 2: Trace each

To model cell or document and page.

#### Step 3: Compare

Value, unit, rounding, period, definition.

#### Step 4: Flag and fix

Mismatch, rounding, label, or unit; owner to fix.

#### Step 5: Sign off

Reviewer initials and date; freeze version.

---

### Structured Output Template

```markdown
# Tie-Out Log: [Deck]

**Deck version:** [ ]  |  **Model version:** [ ]  |  **Date:** [ ]

| Slide | Number | Unit | Source (file / tab / cell) | Source value | Match? | Issue | Owner | Fixed |
|---|---|---|---|---|---|---|---|---|

## Summary
Numbers checked: [ ]  |  Mismatches: [ ]  |  Fixed: [ ]

## Sign-off
[Name, date]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the deck-qc playbook - Clean numbers
- the final-readout playbook - Signed log

**Pulls from:**
- the model-build playbook - Outputs
- the fact-base playbook - Baselines

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Every number** is traced
- [ ] **Units and periods** match
- [ ] **Rounding rule** is consistent
- [ ] **Sign-off** recorded
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `deck-qc` - Production QC
- `model-audit` - Audit the model
- `final-readout` - Prepare the readout



## Playbook: Options Evaluation (name: options-evaluation)

### Quick Start

Say: **Run the options-evaluation playbook**
Then provide:
1. **The decision** and the options considered
2. **Criteria** the client cares about (or I propose)
3. **Evidence** per option

I will structure options in the same format, weight and score against criteria with evidence, and show the sensitivity of the ranking to the weights.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** Develop phase when more than one path could answer the question

**Phase:** Develop

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Criteria
**"If you could pick three criteria, which would they be?"**

Agree criteria before scoring to avoid reverse-engineering.

#### Question 2: The Do-Nothing
**"What happens if we do nothing?"**

Always score the base case.

---

### The Process

#### Step 1: List options

Include do-nothing; same format for each.

#### Step 2: Agree criteria and weights

With the sponsor before scoring.

#### Step 3: Score with evidence

1 to 5 with a one-line reason per score.

#### Step 4: Test weights

Does the winner change under reasonable weights?

#### Step 5: State the trade-offs

What you give up by choosing the winner.

---

### Structured Output Template

```markdown
# Options Evaluation: [Decision]

## So-What
[Option B wins on X, trade-off Y]

## Options
| Option | Description | Value | Cost | Time | Risk |
|---|---|---|---|---|---|

## Scoring
| Criterion | Weight | Option A | Option B | Option C | Evidence |
|---|---|---|---|---|---|

## Weight Sensitivity
[ ]

## Trade-offs
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the recommendation playbook - Chosen option
- the slide-draft playbook - Options page
- the risk-register playbook - Option risks

**Pulls from:**
- the initiative-sizing playbook - Value
- the root-cause-analysis playbook - Causes

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Do-nothing** is included
- [ ] **Criteria agreed** before scoring
- [ ] **Scores** have reasons
- [ ] **Weight sensitivity** shown
- [ ] **Trade-offs** stated
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `recommendation` - Write the recommendation
- `scenario-sensitivity` - Stress it
- `decision-doc` - Log the choice



## Playbook: Recommendation (name: recommendation)

### Quick Start

Say: **Run the recommendation playbook**
Then provide:
1. **Findings and chosen option**
2. **Financial case outputs**
3. **Decision requested**

I will write the recommendation in answer-first form with the supporting argument, the conditions that must hold, and the explicit ask.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** Before the final SteerCo and when the storyline is converging

**Phase:** Recommend

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Ask
**"What exactly do you want the SteerCo to decide?"**

The recommendation must end in a decision.

---

### The Process

#### Step 1: State the recommendation

One sentence with size of prize and timeframe.

#### Step 2: Give three reasons

Each backed by a finding and a number.

#### Step 3: Show the financial case

Run-rate, one-time cost, payback, range.

#### Step 4: State conditions and risks

What must be true and how it is mitigated.

#### Step 5: Make the ask

Decisions, owners, dates.

---

### Structured Output Template

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

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the storyline playbook - Governing thought
- the final-readout playbook - Core content
- the roadmap-build playbook - Plan to deliver

**Pulls from:**
- the options-evaluation playbook - Choice
- the scenario-sensitivity playbook - Case

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Answer first**
- [ ] **Three reasons**, each with a number
- [ ] **Conditions** stated
- [ ] **Ask** is explicit
- [ ] **Numbers** tie to the model
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `storyline` - Build the story
- `final-readout` - Build the readout
- `roadmap-build` - Build the roadmap



## Playbook: Roadmap Build (name: roadmap-build)

### Quick Start

Say: **Run the roadmap-build playbook**
Then provide:
1. **The recommendation and initiatives**
2. **Dependencies and constraints**
3. **Client owners**

I will produce a sequenced 12-to-36-month roadmap with named client owners, KPIs, quick wins, and PMO governance.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~35 min

**When to use:** Recommend and Transition phases

**Phase:** Recommend and Transition

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Owner
**"Which named client leader owns each initiative?"**

Without an owner, it is a wish.

---

### The Process

#### Step 1: List initiatives and milestones



#### Step 2: Sequence by dependency and value

Quick wins first.

#### Step 3: Assign client owners and KPIs



#### Step 4: Reality check capacity

With the implementation reviewer.

#### Step 5: Set governance

PMO, cadence, escalation.

---

### Structured Output Template

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

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the final-readout playbook - Roadmap pages
- the handover-pack playbook - Plan to hand over

**Pulls from:**
- the recommendation playbook - Initiatives
- the initiative-sizing playbook - Value

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Client owner** per initiative
- [ ] **KPIs** defined
- [ ] **Quick wins** in 90 days
- [ ] **Capacity** checked
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `change-plan` - Adoption
- `handover-pack` - Handover
- `risk-register` - Risks



## Playbook: Change Plan (name: change-plan)

### Quick Start

Say: **Run the change-plan playbook**
Then provide:
1. **The change** and who is affected
2. **Stakeholder map**
3. **Timeline**

I will assess change readiness by group, craft the message and messenger for each, and set the first ask and a feedback loop.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** Develop and Recommend phases

**Phase:** Develop through Transition

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Loss
**"What do affected people lose, and what do they gain?"**

Address the loss directly.

---

### The Process

#### Step 1: Segment groups

Size, what changes, what they lose and gain.

#### Step 2: Rate readiness

1 to 5 with evidence.

#### Step 3: Write messages and pick messengers



#### Step 4: Plan the first ask and the feedback loop



#### Step 5: Add to the risk register

Resistance risks.

---

### Structured Output Template

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

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the roadmap-build playbook - Adoption steps
- the risk-register playbook - Resistance risks

**Pulls from:**
- the stakeholder-map playbook - Groups
- the interview-synthesis playbook - Voice

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Each group** has a message and messenger
- [ ] **Readiness** rated with evidence
- [ ] **Feedback loop** defined
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `roadmap-build` - Roadmap
- `stakeholder-map` - Stakeholders
- `risk-register` - Risks



## Playbook: Storyline (name: storyline)

### Quick Start

Say: **Run the storyline playbook**
Then provide:
1. **The answer or current best answer**
2. **Audience and decision**
3. **Evidence so far**

I will write the story as titles only (dot-dash), test that the titles read as a coherent argument, and map each page to the analysis behind it.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** Before building any deck; refresh at each gate

**Phase:** Develop and Recommend

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Audience
**"What does the SteerCo believe today, and what must they believe after?"**

The storyline moves belief from A to B.

#### Question 2: The Order
**"Does this argument go from answer to support, or from situation to answer?"**

Exec audiences get answer first.

---

### The Process

#### Step 1: Write the governing thought

One sentence; the answer.

#### Step 2: Write SCQA

Situation, complication, question, answer.

#### Step 3: Write the key lines

Three to five supports; each a full sentence.

#### Step 4: Write dot-dash

One action title per page under each key line.

#### Step 5: Read the titles aloud

They must tell the whole story without the pages; fix gaps and repeats.

---

### Structured Output Template

```markdown
# Storyline: [Engagement]

**Audience:** [ ]  |  **Decision:** [ ]  |  **Version:** [ ]

## Governing Thought
[ ]

## SCQA
S: [ ]  C: [ ]  Q: [ ]  A: [ ]

## Dot-Dash
**Key line 1:** [ ]
- Page: [Action title] | Evidence: [analysis] | Status: [Ghost / Draft / Tied]
- Page:

**Key line 2:** [ ]
- Page:

## Reading Test
[Notes on gaps or repeats]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the ghost-deck playbook - Page list
- the exec-summary playbook - Summary
- the final-readout playbook - Outline

**Pulls from:**
- the recommendation playbook - Answer
- the hypothesis-draft playbook - Evidence

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Titles alone** tell the story
- [ ] **One message** per page
- [ ] **Each key line** is a sentence
- [ ] **Evidence** is assigned to each page
- [ ] **Decision** is explicit at the end
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `ghost-deck` - Sketch the pages
- `exec-summary` - Write the summary
- `review-panel` - Review the story



## Playbook: Ghost Deck (name: ghost-deck)

### Quick Start

Say: **Run the ghost-deck playbook**
Then provide:
1. **The storyline**
2. **Template and page budget**
3. **Data status**

I will produce a page-by-page ghost deck with an action title, chart type, axes, expected so-what, data source, and status tag per page.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~35 min

**When to use:** As soon as the storyline exists; before analyses are final

**Phase:** Develop and Recommend

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Page Budget
**"How many main pages and how many appendix pages?"**

Page limits force priorities.

---

### The Process

#### Step 1: List the pages

From dot-dash, in order.

#### Step 2: Write the action title

A full sentence with the so-what and a number if known.

#### Step 3: Choose the chart

Type, axes, units, highlight; see chart choices in the production guide.

#### Step 4: List data and owner

Model tab or source and who delivers it.

#### Step 5: Tag status

Ghost, Draft, Tied, Final.

---

### Structured Output Template

```markdown
# Ghost Deck: [Engagement]

| # | Section | Action title | Chart / visual | Axes and units | Source (model tab / file) | Owner | Status | Due |
|---|---|---|---|---|---|---|---|---|

## Data Needs
[ ]

## Production Notes
[Template, fonts, think-cell, page limit]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the slide-draft playbook - Pages to build
- the number-tie-out playbook - Numbers to tie
- the workplan-build playbook - Production tasks

**Pulls from:**
- the storyline playbook - Pages
- the model-build playbook - Data

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Every page** has an action title
- [ ] **Chart** type is chosen and justified
- [ ] **Source** per page
- [ ] **Status tag** per page
- [ ] **Page count** within budget
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `slide-draft` - Build pages
- `deck-qc` - QC the deck
- `number-tie-out` - Tie numbers



## Playbook: Slide Draft (name: slide-draft)

### Quick Start

Say: **Run the slide-draft playbook**
Then provide:
1. **The message** of the slide
2. **The data or analysis** behind it
3. **Audience**

I will draft the slide spec (and a pptx page when asked) with the title, chart, annotations, takeaway box, and source line, following one-message-per-slide.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~10 min per slide

**When to use:** Turning an analysis into a page

**Phase:** Develop and Recommend

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The So-What
**"What do you want the reader to conclude in 5 seconds?"**

That sentence is the title.

---

### The Process

#### Step 1: Write the action title

Full sentence; verb; so-what; number.

#### Step 2: Pick the chart

Comparison: bar; trend: line; composition: stacked or waterfall; relationship: scatter; process: flow.

#### Step 3: Design the layout

Chart left, takeaway right; or chart full width with callouts.

#### Step 4: Annotate

Highlight the one bar or point that proves the title; remove the rest of the noise.

#### Step 5: Add source, units, and notes

Source line, units, date; speaker notes if presented.

---

### Structured Output Template

```markdown
# Slide: [Title]

**Action title:** [ ]
**Chart:** [Type, axes, units, highlights]
**Layout:** [ ]
**Callouts:** [ ]
**Takeaway box:** [ ]
**Source:** [ ]
**Speaker notes:** [ ]
**Data location:** [model tab / cell]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the deck-qc playbook - Slide for QC
- the number-tie-out playbook - Numbers to tie

**Pulls from:**
- the ghost-deck playbook - Plan
- the scenario-sensitivity playbook - Charts

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Title** is a full sentence
- [ ] **One message** only
- [ ] **Chart** supports the title
- [ ] **Source and units** present
- [ ] **Passes** the horizontal read test
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `ghost-deck` - See the whole deck
- `deck-qc` - QC
- `number-tie-out` - Tie numbers



## Playbook: Executive Summary (name: exec-summary)

### Quick Start

Say: **Run the exec-summary playbook**
Then provide:
1. **The recommendation**
2. **Key numbers**
3. **Decision requested**

I will write a one-page executive summary that a busy sponsor can read in two minutes and act on.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~20 min

**When to use:** Each SteerCo pre-read and the final readout

**Phase:** Recommend

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Reader
**"Will the reader see only this page?"**

If yes, it must carry the whole case.

---

### The Process

#### Step 1: Lead with the answer

Recommendation and size of prize.

#### Step 2: Give three reasons

One sentence each with a number.

#### Step 3: State cost, timing, risks

Concise.

#### Step 4: End with the ask

Decision, owner, date.

#### Step 5: Cut 20%

Then check it still stands alone.

---

### Structured Output Template

```markdown
# Executive Summary

**Recommendation:** [ ]

**Why:**
1. [ ]
2. [ ]
3. [ ]

**Investment and timing:** [ ]
**Key risks and mitigations:** [ ]
**Decisions requested:** [ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the final-readout playbook - Opening page
- the steerco-prep playbook - Pre-read

**Pulls from:**
- the recommendation playbook - Answer
- the storyline playbook - Key lines

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Stands alone**
- [ ] **Numbers** tie
- [ ] **Ask** is explicit
- [ ] **Under one page**
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `storyline` - Align to story
- `final-readout` - Use in readout
- `number-tie-out` - Tie numbers



## Playbook: Deck QC (name: deck-qc)

### Quick Start

Say: **Run the deck-qc playbook**
Then provide:
1. **The deck**
2. **Template rules**
3. **Version and audience**

I will check a deck for story flow, title quality, number tie, formatting consistency, language, sources, and file hygiene, and return a fix list.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** Before any deck leaves the team

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Version
**"Which version is final, and who freezes it?"**

Version control is part of QC.

---

### The Process

#### Step 1: Horizontal test

Read only the titles; story must hold.

#### Step 2: Slide by slide

One message; chart matches title; units; source.

#### Step 3: Format

Fonts, sizes, colors, alignment, spacing, page numbers, footers.

#### Step 4: Language

Spelling, tense, numbers format, abbreviations defined, no banned phrases.

#### Step 5: File hygiene

Remove comments, hidden slides, metadata, internal notes; save PDF and editable.

---

### Structured Output Template

```markdown
# Deck QC: [Deck]

**Version:** [ ]  |  **Reviewer:** [ ]  |  **Date:** [ ]

## Verdict
[Ready / Fix then ready / Not ready]

## Findings
| # | Slide | Category | Issue | Fix | Owner | Done |
|---|---|---|---|---|---|---|

## Checks
- [ ] Horizontal flow
- [ ] Titles
- [ ] Numbers tie
- [ ] Formatting
- [ ] Language
- [ ] File hygiene
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the review-panel playbook - Clean deck
- the final-readout playbook - Frozen version

**Pulls from:**
- the number-tie-out playbook - Tie status
- the slide-draft playbook - Slides

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Horizontal test** run
- [ ] **Every slide** checked
- [ ] **Comments and hidden slides** removed
- [ ] **PDF and editable** saved
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `number-tie-out` - Tie numbers
- `review-panel` - Panel review
- `final-readout` - Final readout



## Playbook: Final Readout (name: final-readout)

### Quick Start

Say: **Run the final-readout playbook**
Then provide:
1. **Recommendation and storyline**
2. **Audience and date**
3. **Decks and models status**

I will build the readout outline, the page-by-page checklist, the red-team Q&A, and the pre-readout readiness list.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~40 min

**When to use:** Two weeks before the final SteerCo

**Phase:** Recommend

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Decision
**"What decision do we want at the end of the meeting?"**

The ask drives the structure.

---

### The Process

#### Step 1: Build the outline

Nine sections per the template.

#### Step 2: Assign pages and owners



#### Step 3: Run reviews

Partner, QC, tie-out, model audit.

#### Step 4: Rehearse Q&A

Top ten questions.

#### Step 5: Freeze and stage

PDF and editable master; handover pack.

---

### Structured Output Template

```markdown
# Final Readout: [Engagement]

## Outline
| Section | Pages | Content | Owner | Status |
|---|---|---|---|---|

## Q&A (Top 10)
| Question | Answer | Who |
|---|---|---|

## Readiness Checklist
- [ ] Sponsor pre-wired
- [ ] Pre-read sent
- [ ] Numbers tied
- [ ] Model audited
- [ ] Partner and QC review
- [ ] Version frozen
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the handover-pack playbook - Final materials
- the retrospective playbook - Outcome

**Pulls from:**
- the exec-summary playbook - Summary
- the roadmap-build playbook - Roadmap

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Decision** is explicit
- [ ] **Numbers tied**
- [ ] **Model audited**
- [ ] **Q&A rehearsed**
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `handover-pack` - Hand over
- `deck-qc` - QC
- `steerco-prep` - SteerCo



## Playbook: Google Workspace Output (name: google-workspace-output)

### Quick Start

Say: **Run the google-workspace-output playbook**
Then provide:
1. **What to deliver** (model, tracker, ghost deck, deck, or a conversion of an existing xlsx or pptx)
2. **Where it should live** (shared drive or folder)
3. **Who needs access** (team only, or a client counterpart)

I will check which Google connectors are available, choose the easiest route (CSV upload, copy of the Google starter, or in-place build), build it, verify the result, and set sharing the safe way.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~10 min for a tracker; ~30 to 60 min for a model or deck

**When to use:** The engagement uses Google Workspace, or a Google file is easier than building xlsx or pptx with Python

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Approval
**"Has the client approved Google Workspace for their data, in writing?"**

If not, stop. Use the Office path locally and ask the EM.

#### Question 2: The Tier
**"Which Google connectors are enabled here?"**

Drive only means create and convert. Sheets and Slides editors mean in-place builds. If an editor is missing and the file already exists, I ask you to enable it instead of making a copy.

#### Question 3: The Audience
**"Who opens the file, and do they need Excel or PowerPoint copies?"**

Decides whether to export .xlsx, .pptx, or PDF at the end.

---

### The Process

#### Step 1: Check the format rule

Read Preferred output formats in engagement info. If blank, ask once and record the answer.

#### Step 2: Check approval and tools

Confirm client approval for Google. List the connectors available. Pick Tier 1, 2, or 3.

#### Step 3: Pick the route

Tracker or log: build a CSV and upload it to create a Google Sheet (Tier 1). Model: copy the Google starter, or create a blank Sheet and write inputs, formulas, and formats with the Sheets editor (Tier 2). Deck: copy the Slides starter and build pages with the Slides editor (Tier 3); charts are built on the Sheet Outputs tab and embedded as linked charts. Without the editor, deliver the spec and ask you to enable the connector.

#### Step 4: Build in one pass per step

One write for the data and formulas, one batch for formatting and tabs, one for slides. Parsing follows the Sheets UI: numbers as numbers, years and IDs with a leading apostrophe.

#### Step 5: Verify

Read values back. For models: no error values, Checks master flag is 0, Base outputs match the starter. For decks: read text, export a PDF where possible, check overflow, fonts, charts. If layout could not be checked visually, say so.

#### Step 6: Share and log

Share with named people only; reader or commenter for the client; never anyone-with-link. Record file name, link, owner, version, access, and approval in `Client folder 01_Outputs/mcp-integration-logs/`.

---

### Common Mistakes

- **Making a second copy to avoid an edit**: Edits go into the same file. Ask to enable the editor connector instead.
- **Typed results**: Every derived number is a formula, not a pasted result.
- **Skipping the visual check**: Converted decks can change fonts and spacing. Check every page.

---

### Structured Output Template

```markdown
# Google Output Log: [Item]

**Date:** [ ]  |  **Owner:** [ ]  |  **Tier:** [1 / 2 / 3]  |  **Approval for client data:** [Y/N, where recorded]

| File | Type | Link | Route | Version | Shared with | Role |
|---|---|---|---|---|---|---|

## Verification
| Check | Result |
|---|---|
| Error values | |
| Master check | |
| Fonts and layout | |
| Charts linked | |

## Limits Noted
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the number-tie-out playbook - Linked Outputs tab and charts
- the deck-qc playbook - Deck to check
- the handover-pack playbook - Files to hand over

**Pulls from:**
- the model-spec playbook - What to build
- the ghost-deck playbook - Pages to build
- the connect-mcps playbook - Connectors

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Client approval** for Google confirmed and recorded
- [ ] **Edits** went into the existing file, not a copy
- [ ] **Every derived number** is a formula
- [ ] **Values read back** with no error cells
- [ ] **Sharing** is to named people only
- [ ] **Log** saved
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `model-build` - Excel route
- `ghost-deck` - Deck spec
- `connect-mcps` - Enable connectors


# Section B: Rhythm, governance and close


## Playbook: Daily Plan (name: daily-plan)

### Quick Start

Say: **Run the daily-plan playbook**
Then provide:
1. **Your role and today's calendar**
2. **Open assignments**
3. **Reviews due**

I will produce a daily plan with a top three, review windows, handoff asks, and a check-out note.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~5 min

**When to use:** Start of every day, and end of day for the check-out

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Top Three
**"What three outputs make today a success?"**

Anything else is a bonus.

---

### The Process

#### Step 1: Top three

With the deliverable and time block.

#### Step 2: Reviews and handoffs

Who needs what from you and by when.

#### Step 3: Check-in note

Priorities and risks for the team check-in.

#### Step 4: Check-out

What was done, what slipped, what is needed tomorrow.

---

### Structured Output Template

```markdown
# Daily Plan: [Date]

## Top Three
1. [Output] - [time block]

## Reviews and Handoffs
| With | What | By |
|---|---|---|

## Check-in Note
[ ]

## Check-out
Done: [ ]  Slipped: [ ]  Need: [ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the weekly-review playbook - Daily log

**Pulls from:**
- the workplan-build playbook - Tasks
- the handoff-brief playbook - Handoffs

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Three outputs**, not tasks
- [ ] **Review slots** protected
- [ ] **Check-out** written
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `weekly-plan` - Plan the week
- `handoff-brief` - Write handoffs
- `status-update` - Weekly status



## Playbook: Weekly Plan (name: weekly-plan)

### Quick Start

Say: **Run the weekly-plan playbook**
Then provide:
1. **Gate dates and SteerCo**
2. **Workplan**
3. **Team capacity**

I will produce a weekly plan with deliverables by day, review windows, and a partner session agenda.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~10 min

**When to use:** Monday morning or Friday afternoon

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Week's Outcome
**"What must be true by Friday?"**

Defines the weekly goal.

---

### The Process

#### Step 1: Set goals

Three outcomes tied to the next gate.

#### Step 2: Place deliverables by day

With review windows.

#### Step 3: Protect the review ladder

Draft to EM, then partner, with SLAs.

#### Step 4: Plan the partner session

Agenda and pre-read.

#### Step 5: Flag risks

Capacity, data, client.

---

### Structured Output Template

```markdown
# Weekly Plan: [Week of]

## Goals
1. [ ]

## By Day
| Day | Deliverable | Owner | Review | Client touchpoint |
|---|---|---|---|---|

## Partner Session
[Agenda]

## Risks
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the daily-plan playbook - Daily detail
- the status-update playbook - Plan vs actual

**Pulls from:**
- the workplan-build playbook - Tasks

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Goals** link to a gate
- [ ] **Review windows** exist
- [ ] **Capacity** is realistic
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `daily-plan` - Daily
- `partner-session-prep` - Partner session
- `weekly-review` - Review the week



## Playbook: Weekly Review (name: weekly-review)

### Quick Start

Say: **Run the weekly-review playbook**
Then provide:
1. **This week's outputs**
2. **Feedback received**
3. **Next week's gate**

I will review the week against plan, update the learning log, and propose improvements to skills and templates.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~15 min

**When to use:** Friday afternoon

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Lesson
**"What is the one thing to change next week?"**

Keep it to one.

---

### The Process

#### Step 1: Compare plan to actual



#### Step 2: Collect feedback



#### Step 3: Update the learning log



#### Step 4: Propose skill or template fixes



#### Step 5: Set next week's goals



---

### Structured Output Template

```markdown
# Weekly Review: [Week]

## Plan vs Actual
[ ]
## Feedback
[ ]
## Learning Log
- [ ]
## Skill and Template Fixes
[ ]
## Next Week
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the weekly-plan playbook - Goals

**Pulls from:**
- the daily-plan playbook - Log
- the status-update playbook - Status

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **One lesson** captured
- [ ] **Fixes** proposed
- [ ] **Next week** goals set
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `weekly-plan` - Plan next week
- `retrospective` - Retro



## Playbook: Status Update (name: status-update)

### Quick Start

Say: **Run the status-update playbook**
Then provide:
1. **This week's progress**
2. **Risks and blockers**
3. **Decisions needed**

I will write a one-page weekly status in answer-first form that a sponsor can read in 90 seconds.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~15 min

**When to use:** Weekly, before the sponsor touchpoint

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Headline
**"If the sponsor read one line, what should it say?"**

Lead with it.

---

### The Process

#### Step 1: Headline

One line: on track, at risk, or off track and why.

#### Step 2: Findings

Three bullets with numbers.

#### Step 3: Progress vs plan

Done, in progress, slipped.

#### Step 4: Risks and blockers

With owner and ask.

#### Step 5: Decisions and next week

Who, what, by when.

---

### Structured Output Template

```markdown
# Weekly Status: [Engagement] - [Date]

**Headline:** [ ]  |  **RAG:** [G/A/R]

## Findings
- [ ]

## Progress vs Plan
| Item | Status | Note |
|---|---|---|

## Risks and Blockers
| Item | Owner | Ask |
|---|---|---|

## Decisions Needed
| Decision | By whom | By when |
|---|---|---|

## Next Week
- [ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the steerco-prep playbook - Progress
- the weekly-review playbook - Input

**Pulls from:**
- the workplan-build playbook - Progress
- the risk-register playbook - Risks

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Headline** states RAG and why
- [ ] **Findings** have numbers
- [ ] **Asks** have owners and dates
- [ ] **Under one page**
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `risk-register` - Update risks
- `decision-doc` - Log decisions
- `steerco-prep` - Prep SteerCo



## Playbook: SteerCo Prep (name: steerco-prep)

### Quick Start

Say: **Run the steerco-prep playbook**
Then provide:
1. **SteerCo date and attendees**
2. **Decisions to be made**
3. **Content ready** (decks, models)

I will produce the SteerCo agenda, pre-wire plan, pre-read checklist, expected objections with answers, and a decision log update.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** One week before each SteerCo and again 3 days before

**Phase:** All gates

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Decision
**"What must the SteerCo decide, and what is the fallback if they do not?"**

A SteerCo without a decision is a status meeting.

---

### The Process

#### Step 1: Define decisions and outcomes

Per agenda item.

#### Step 2: Plan pre-wires

Sponsor first, then members; 2 to 3 days ahead.

#### Step 3: Send the pre-read

With a one-page summary.

#### Step 4: Rehearse objections

Top ten questions with answers; assign who answers.

#### Step 5: Capture outcomes

Decisions, actions, owners in the log within 24 hours.

---

### Structured Output Template

```markdown
# SteerCo Prep: [Date]

## Agenda
| Time | Item | Lead | Decision / output |
|---|---|---|---|

## Pre-wire Plan
| Person | What to align on | By | Who |
|---|---|---|---|

## Pre-read Checklist
- [ ] Sent [date]
- [ ] Executive summary
- [ ] Decisions listed

## Likely Objections
| Question | Answer | Who answers |
|---|---|---|

## After the Meeting
[Decisions, actions, owners]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the decision-doc playbook - Decisions
- the status-update playbook - Next steps

**Pulls from:**
- the stakeholder-map playbook - Pre-wires
- the exec-summary playbook - Pre-read

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Decisions** explicit per item
- [ ] **Pre-wires** done for each member
- [ ] **Pre-read** sent 2 to 3 days ahead
- [ ] **Objection list** rehearsed
- [ ] **Outcomes** logged
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `stakeholder-map` - Plan pre-wires
- `exec-summary` - Write pre-read
- `decision-doc` - Log decisions



## Playbook: Partner Session Prep (name: partner-session-prep)

### Quick Start

Say: **Run the partner-session-prep playbook**
Then provide:
1. **The issue** you need the partner's help with
2. **Evidence so far**
3. **Time available**

I will produce a one-page prep with the answer first, the evidence, the options you see, and the specific decision or steer you need.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~15 min

**When to use:** Before each of the two or more weekly partner sessions

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Ask
**"What exactly do you want from the partner: a decision, a steer, or an introduction?"**

Partners have 30 minutes.

---

### The Process

#### Step 1: Lead with the answer

Current best view.

#### Step 2: Show the evidence

Three pages at most.

#### Step 3: State options

Each with a trade-off and your recommendation.

#### Step 4: State the ask

Decision or steer needed.

#### Step 5: Anticipate challenges

Top three questions.

---

### Structured Output Template

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

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the decision-doc playbook - Decisions

**Pulls from:**
- the hypothesis-draft playbook - Answer status

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Answer first**
- [ ] **Ask** is specific
- [ ] **Evidence** is three pages or fewer
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `steerco-prep` - SteerCo
- `decision-doc` - Log decisions
- `storyline` - Story



## Playbook: Handoff Brief (name: handoff-brief)

### Quick Start

Say: **Run the handoff-brief playbook**
Then provide:
1. **The assignment or submission**
2. **To whom**
3. **By when**

I will write a four-part handoff that lets the recipient start immediately and lets the reviewer check the work fast.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~5 min

**When to use:** Every time work changes hands

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Output
**"What exact output do you want back?"**

Format and level of polish.

---

### The Process

#### Step 1: Brief

Question, hypothesis, format, data, constraints.

#### Step 2: Backup

Where the work and sources are.

#### Step 3: So-what

Expected or current finding and why it matters.

#### Step 4: Ask

What you need and by when; flag early if.

---

### Structured Output Template

```markdown
# Handoff: [Topic]

**From / To / Needed by:** [ ]

## Brief
[ ]
## Backup
[ ]
## So-What
[ ]
## Ask
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the daily-plan playbook - Asks

**Pulls from:**
- the workplan-build playbook - Tasks

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **All four parts** present
- [ ] **Needed-by** time stated
- [ ] **Backup** link works
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `review-panel` - Request review
- `daily-plan` - Plan the day



## Playbook: Meeting Agenda (name: meeting-agenda)

### Quick Start

Say: **Run the meeting-agenda playbook**
Then provide:
1. **Purpose and attendees**
2. **Length**
3. **Decisions needed**

I will write a timed agenda with an owner and an output per item.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~5 min

**When to use:** Before any meeting with the client or partner

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Outcome
**"What is different after the meeting?"**

Defines the agenda.

---

### The Process

#### Step 1: State purpose and outcome



#### Step 2: List items with owner and output



#### Step 3: Time-box



#### Step 4: Attach pre-read



---

### Structured Output Template

```markdown
# Agenda: [Topic]

**Purpose / outcome:** [ ]

| Time | Item | Owner | Output |
|---|---|---|---|

**Pre-read:** [ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the meeting-notes playbook - Notes

**Pulls from:**
- the decision-doc playbook - Pending decisions

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Outcome** is stated
- [ ] **Timing** adds up
- [ ] **Pre-read** attached
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `meeting-notes` - Notes
- `steerco-prep` - SteerCo



## Playbook: Meeting Notes (name: meeting-notes)

### Quick Start

Say: **Run the meeting-notes playbook**
Then provide:
1. **Transcript or notes**
2. **Meeting type** (client, SteerCo, team, partner)
3. **Attendees**

I will return decisions, actions with owners and dates, open questions, and signals about stakeholder stance within an hour of the meeting.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~10 min

**When to use:** After every client or partner meeting

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Distribution
**"Who gets the notes and when?"**

Notes help only if they arrive fast.

---

### The Process

#### Step 1: Summarize in three lines



#### Step 2: List decisions



#### Step 3: List actions

Owner and date.

#### Step 4: Extract signals

Stance and hypothesis evidence.

#### Step 5: Send

Same day.

---

### Structured Output Template

```markdown
# Meeting Notes: [Topic] - [Date]

**Attendees:** [ ]

## Summary
[3 lines]

## Decisions
- [ ]

## Actions
| Action | Owner | Due |
|---|---|---|

## Signals
[Stance, evidence]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the decision-doc playbook - Decisions
- the stakeholder-map playbook - Stance
- the hypothesis-draft playbook - Evidence

**Pulls from:**
- the steerco-prep playbook - Agenda

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Actions** have owners and dates
- [ ] **Decisions** are unambiguous
- [ ] **Sent same day**
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `decision-doc` - Log decisions
- `stakeholder-map` - Update map
- `status-update` - Status



## Playbook: Decision Doc (name: decision-doc)

### Quick Start

Say: **Run the decision-doc playbook**
Then provide:
1. **The decision** taken or needed
2. **Options and who decided**
3. **Date and forum**

I will write a one-page decision record and update the decision log so scope, definitions, and approvals have a paper trail.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~10 min

**When to use:** After any SteerCo, scope change, definition agreement, or model assumption sign-off

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Owner
**"Who has the authority to make this decision?"**

A decision by the wrong person will be reopened.

---

### The Process

#### Step 1: State the decision

One sentence.

#### Step 2: List options considered

Why rejected.

#### Step 3: Record owner, date, forum



#### Step 4: Record the reversal trigger

What would reopen it.

#### Step 5: Update the log and notify

Send to affected people.

---

### Structured Output Template

```markdown
# Decision: [Topic]

**ID:** [D#]  |  **Date:** [ ]  |  **Forum:** [ ]  |  **Owner:** [ ]

## Decision
[ ]

## Context
[ ]

## Options Considered
| Option | Why not chosen |
|---|---|

## Impact
[Scope, timeline, model, deck]

## Reversal Trigger
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the workplan-build playbook - Scope changes
- the fact-base playbook - Definitions

**Pulls from:**
- the steerco-prep playbook - Outcomes
- the meeting-notes playbook - Context

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Owner** has authority
- [ ] **Reversal trigger** stated
- [ ] **Impact** listed
- [ ] **Log** updated
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `steerco-prep` - SteerCo outcomes
- `workplan-build` - Update plan
- `fact-base` - Update definitions



## Playbook: Risk Register (name: risk-register)

### Quick Start

Say: **Run the risk-register playbook**
Then provide:
1. **New risks or signals**
2. **Current register** (if any)
3. **Gate dates**

I will update the register with likelihood, impact, early signals, mitigation, and owner, and recommend what to escalate.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~15 min

**When to use:** Weekly, and whenever a new risk appears

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Signal
**"What would we see first if this risk is materializing?"**

Early signals make risks manageable.

---

### The Process

#### Step 1: Add or update risks

Category, description, likelihood, impact.

#### Step 2: Score

Likelihood x impact; escalate at 15 or more.

#### Step 3: Set mitigation and owner



#### Step 4: Update the heatmap



#### Step 5: Escalate

To EM or partner with a recommended action.

---

### Structured Output Template

```markdown
# Risk Register: [Engagement] - [Date]

| ID | Risk | Category | L | I | Score | Early signal | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|

## Escalate Now
[ ]

## Heatmap
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the status-update playbook - Risks
- the steerco-prep playbook - Escalations

**Pulls from:**
- the status-update playbook - Signals

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Each risk** has owner and mitigation
- [ ] **Scores >= 15** escalated
- [ ] **Early signals** named
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `status-update` - Report
- `change-plan` - Change risks
- `recommendation` - Delivery risks



## Playbook: Client Update Email (name: client-update-email)

### Quick Start

Say: **Run the client-update-email playbook**
Then provide:
1. **Purpose and recipient**
2. **Key message**
3. **Ask and date**

I will draft a short, answer-first email in the client-exec voice with a clear ask.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~5 min

**When to use:** Whenever writing to the client

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Ask
**"What do you want the recipient to do, and by when?"**

One ask per email.

---

### The Process

#### Step 1: Lead with the message



#### Step 2: State the ask and date



#### Step 3: Add only needed context



#### Step 4: Check tone

Match the recipient.

---

### Structured Output Template

```markdown
Subject: [Message in one line]

[Recipient],

[Message in two sentences.]

[Ask and date.]

[Name]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the status-update playbook - Updates

**Pulls from:**
- the status-update playbook - Content

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **One ask**
- [ ] **Under 150 words**
- [ ] **Tone** fits
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `status-update` - Status
- `risk-register` - Escalations



## Playbook: Engagement Health Check (name: engagement-health-check)

### Quick Start

Say: **Run the engagement-health-check playbook**
Then provide:
1. **Engagement and week**
2. **Any concerns**
3. **Who is asking** (EM or partner)

I will score the engagement across eight dimensions with evidence, name the top two issues, and recommend actions.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~20 min

**When to use:** Every two weeks, and when something feels off

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Pulse
**"How does the sponsor feel about progress today?"**

Relationship risk shows first in tone.

---

### The Process

#### Step 1: Score eight dimensions

Question, scope, answer, evidence, team, client, quality, financials.

#### Step 2: Cite evidence for each



#### Step 3: Name the top two issues



#### Step 4: Recommend actions



#### Step 5: Share with the EM



---

### Structured Output Template

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

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the status-update playbook - Issues

**Pulls from:**
- the status-update playbook - Trend

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Evidence** for each RAG
- [ ] **Two issues** named
- [ ] **Actions** proposed
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `risk-register` - Risks
- `decision-doc` - Scope



## Playbook: Review Panel (name: review-panel)

### Quick Start

Say: **Run the review-panel playbook**
Then provide:
1. **The output to review** (deck, model, memo)
2. **Audience and stakes**
3. **Which reviewers** (default: partner, EM, skeptic, client sponsor)

I will run each reviewer persona in turn, consolidate their feedback into one prioritized list, and flag contradictions between reviewers.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~20 min

**When to use:** Before an EM or partner review, and before any client-facing output

**Phase:** All

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Stakes
**"Is this going to a client or staying internal?"**

Raises or lowers the bar and the number of reviewers.

---

### The Process

#### Step 1: Choose reviewers

Partner for story; EM for plan; skeptic for logic; sponsor and CFO for client view; QC for production.

#### Step 2: Run each persona

Each gives top three issues and one strength.

#### Step 3: Consolidate

Merge duplicates; rank by severity.

#### Step 4: Resolve conflicts

Where reviewers disagree, state the choice and why.

#### Step 5: Create the fix list

Owner and due date.

---

### Structured Output Template

```markdown
# Review Panel: [Item]

## Verdict
[ ]

## Top Issues (ranked)
| # | Issue | Raised by | Severity | Fix | Owner |
|---|---|---|---|---|---|

## By Reviewer
**Partner:** [ ]
**EM:** [ ]
**Skeptic:** [ ]
**Client sponsor:** [ ]
**CFO:** [ ]
**QC:** [ ]

## Conflicts
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the slide-draft playbook - Fixes
- the model-build playbook - Fixes
- the steerco-prep playbook - Readiness

**Pulls from:**
- the deck-qc playbook - QC
- the model-audit playbook - Audit

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Each persona** gives specific, actionable feedback
- [ ] **Conflicts** are resolved
- [ ] **Fix list** has owners
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `deck-qc` - QC the deck
- `model-audit` - Audit the model
- `steerco-prep` - Prepare the SteerCo



## Playbook: Handover Pack (name: handover-pack)

### Quick Start

Say: **Run the handover-pack playbook**
Then provide:
1. **The deliverables**
2. **Client owners**
3. **Handover date**

I will compile an index, model user guide, assumptions list, open items, and a handover session agenda so the client can run the work without us.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~30 min

**When to use:** Transition phase

**Phase:** Transition

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Owner
**"Who owns the model after we leave?"**

A model without an owner decays.

---

### The Process

#### Step 1: Index deliverables



#### Step 2: Write the model guide

Purpose, inputs, how to update, known limits.

#### Step 3: List open items and owners



#### Step 4: Plan the handover session

Walkthrough and Q&A.

#### Step 5: Return or delete data

Per agreement.

---

### Structured Output Template

```markdown
# Handover Pack: [Engagement]

## Index
| Item | Location | Owner | Notes |
|---|---|---|---|

## Model Guide
[ ]

## Open Items
| Item | Owner | Date |
|---|---|---|

## Handover Session
[Agenda]

## Data Return and Deletion
[ ]
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the retrospective playbook - Closeout

**Pulls from:**
- the final-readout playbook - Final materials
- the roadmap-build playbook - Owners

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Client owner** named for each item
- [ ] **Model guide** written
- [ ] **Data** return or deletion logged
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `retrospective` - Retro
- `knowledge-capture` - Capture assets
- `final-readout` - Readout



## Playbook: Retrospective (name: retrospective)

### Quick Start

Say: **Run the retrospective playbook**
Then provide:
1. **Engagement outcome**
2. **Plan vs actuals**
3. **Team views**

I will draft the retrospective with outcome snapshot, what worked, what to change, calibration table, and actions with owners.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~25 min

**When to use:** Within two weeks of the final SteerCo, and at a mid-engagement checkpoint on longer work

**Phase:** Close

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Counterfactual
**"If we ran this again, what is the first thing we would change?"**

Surfaces the real lesson.

---

### The Process

#### Step 1: Snapshot outcome



#### Step 2: List what worked and why



#### Step 3: List what to change and root cause



#### Step 4: Fill calibration table

Plan vs actual.

#### Step 5: Agree actions

Owner, date.

---

### Structured Output Template

```markdown
# Retrospective: [Engagement]

## Outcome
[ ]
## What Worked
[ ]
## What to Change
[ ]
## Calibration
| Item | Plan | Actual | Reason |
|---|---|---|---|
## Actions
| Action | Owner | Date |
|---|---|---|
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the knowledge-capture playbook - Assets
- the proposal-draft playbook - Better estimates

**Pulls from:**
- the handover-pack playbook - Closeout

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Root causes**, not blame
- [ ] **Calibration** table filled
- [ ] **Actions** have owners
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `knowledge-capture` - Capture assets
- `weekly-review` - Weekly review



## Playbook: Knowledge Capture (name: knowledge-capture)

### Quick Start

Say: **Run the knowledge-capture playbook**
Then provide:
1. **The engagement**
2. **Assets worth keeping**
3. **Confidentiality limits**

I will classify what is reusable, strip confidential detail, and write a short case summary and an asset index.

**Output:** Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.
**Time:** ~25 min

**When to use:** After the retro

**Phase:** Close

### Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

#### Question 1: The Limit
**"What client information must never leave the engagement folder?"**

Strip it first.

---

### The Process

#### Step 1: List assets



#### Step 2: Anonymize



#### Step 3: Write a short case

Situation, approach, result.

#### Step 4: Index with tags



#### Step 5: Store in the firm knowledge base

Via the user.

---

### Structured Output Template

```markdown
# Knowledge Capture: [Engagement]

## Case Summary
[Situation / approach / result, anonymized]

## Asset Index
| Asset | Type | Location | Reusable? | Confidentiality | Owner |
|---|---|---|---|---|---|
```

---

### Output Integration

#### Cross-Skill Integration

**Feeds into:**
- the proposal-draft playbook - Credentials

**Pulls from:**
- the retrospective playbook - Learnings

When this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.

---

### Output Quality Self-Check

Before delivering, verify:

- [ ] **Client identifiers** removed
- [ ] **Assets tagged**
- [ ] **Owner** named
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge

---

### Related Skills

- `retrospective` - Retro
- `proposal-draft` - Reuse

