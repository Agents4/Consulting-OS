# Consulting OS Core 1: Engagement Model, Frameworks and Standards

Roles, lifecycle, tasks, cadence and handoffs, frameworks, deck and model standards, voice by audience. Shared across all clients. Reference only. Client facts live in the client context docs.

# Part 1: How an engagement runs

## The Strategy Engagement Model: Overview

**Purpose:** Reference model of how a McKinsey, BCG, or Bain style strategy engagement actually runs. Every skill, sub-agent, and template in Consulting-OS is built on this model. Claude reads these files before it plans, drafts, or reviews anything.

**Compiled:** October 2026, from public firm material, practitioner guides, and press coverage (see `sources.md`). Firms do not publish their internal playbooks. Where sources agree, this file states the practice as typical. Where they conflict or the claim is anecdotal, the file says so. Replace any default here with your firm's or client's real standard in `context docs/engagement-info-template.md`.

---

### The Engagement on a Page

```
PURSUIT        MOBILIZE       DIAGNOSE        DEVELOP + SYNTHESIZE     RECOMMEND        TRANSITION + CLOSE
(1-4 wks,      (wk 1-2)       (wk 2-5)        (wk 4-9)                 (final 2-3 wks)  (last wk + after)
partner-led)

Proposal  -->  Kickoff   -->  Interviews  --> Solutions, sizing,   --> Final SteerCo -->  Handover to client
SOW            Data request   Data analysis    business case,            Readout           PMO, models,
Team staffed   Workplan       Benchmarks       roadmap, workshops        Implementation    playbooks, retro,
               Hypotheses     Model v1         Model v2, Day-N answer    plan              case study
               Day-1 answer   Week-1 answer
```

Four things run the whole way through:

1. **A governing hypothesis.** The team always has a current best answer (Day-1, Week-1, Week-N) and spends its time proving or killing it.
2. **A rhythm.** Daily check-in and check-out, 2+ partner problem-solving sessions a week, one client progress review or SteerCo a week or two. The week is organized around the next client touchpoint, not around tasks.
3. **Layered review.** Nothing reaches the client before someone more senior has reviewed it. Analyst to consultant to engagement manager to partner.
4. **Two artifacts carry the work:** a storyline in PowerPoint (the argument) and an Excel model (the evidence). Every number on a slide traces back to a cell in a model.

---

### Title Map (the three firms side by side)

| Generic seat | McKinsey | BCG | Bain |
|---|---|---|---|
| Entry (undergrad) | Business Analyst | Associate | Associate Consultant (AC) |
| Post-MBA / advanced degree | Associate | Consultant | Consultant |
| Day-to-day team leader | Engagement Manager (EM) | Project Leader (PL) | Manager, then Senior Manager |
| Pre-partner | Associate Partner (AP) | Principal | Associate Partner (AP) |
| Partner | Partner | Managing Director and Partner (MD&P) | Partner |
| Senior | Senior Partner | Senior MD&P | Senior Partner |

Consulting-OS uses the McKinsey-style generic names (Partner, Associate Partner, Engagement Manager, Associate, Business Analyst) unless your `team-roster-template.md` says otherwise. The seat matters more than the title.

---

### How This Folder Is Organized

| File | What it answers |
|---|---|
| `01-roles-and-team-structure.md` | Who is on the team, how it is shaped, what each seat owns |
| `02-skills-by-role.md` | What each seat must be good at, and what changes at each level |
| `03-engagement-lifecycle.md` | Phases, gates, durations, and commercial model |
| `04-tasks-by-phase.md` | The work, task by task, with owner and reviewer |
| `05-cadence-and-handoffs.md` | Meeting rhythm, review ladder, handoff contracts |
| `06-deliverable-production-decks.md` | How a slide deck gets made, from storyline to final QC |
| `07-excel-modeling-standards.md` | How a model gets specified, built, checked, reviewed |
| `08-support-functions-and-tools.md` | Research, graphics, analytics hubs, expert networks, tool stack |
| `09-ai-in-consulting-2026.md` | What the firms say about AI on engagements, and what it means for the OS |
| `10-glossary.md` | The vocabulary |
| `sources.md` | Where every claim came from, with reliability notes |

---

### What Consulting-OS Does With This Model

Consulting-OS gives Claude a seat on the team. You tell it which seat you hold (or which seat you want it to play), and it:

- Works the **analyst seat**: pulls data, builds exhibits, drafts model tabs, formats slides, cleans notes.
- Works the **consultant seat**: structures a workstream, drafts the analysis plan, synthesizes interviews, writes the first storyline.
- Plays the **reviewer seats** through sub-agents: engagement manager, partner, client sponsor, CFO, skeptic, model auditor.
- Keeps the **rhythm**: daily plans, check-ins, weekly SteerCo prep, status updates.

You stay accountable for the answer. See `09-ai-in-consulting-2026.md` for the verification rules.


## Roles and Team Structure

### Team Shapes

| Engagement type | Typical team | Duration | Notes |
|---|---|---|---|
| Diagnostic / rapid assessment | 2-3 consultants + EM, part-time partner | 2-6 weeks | Often the "foot in the door" for a bigger piece |
| Core strategy engagement | 1 part-time partner, 1 EM (full time), 2-4 Associates/Analysts | 4-12 weeks (some sources say 3-6 months) | The default shape. Core case teams run 3-6 people |
| Due diligence (commercial) | Partner + EM + 3-4 consultants | 2-4 weeks | Compressed. Hours run well above normal |
| Transformation / implementation | Several teams under one partner, plus a client-side PMO | 6-24 months | Team mix shifts from analysis to change management |
| Expanded team | Core team + specialists (data scientist, expert, designer, practice expert) | Varies | Teams of 6-12 when specialists join |

**Staffing ratios reported by practitioner sources:**
- A partner oversees about 2-7 active projects at once and spends roughly half a day to a day per week on each.
- An Associate Partner / Principal handles up to three or four parallel projects.
- An Engagement Manager / Project Leader runs one team full time (some firms split a manager across two clients).
- Associates, consultants, and analysts are usually full time on one client.

**Commercial note:** MBB-style firms typically bill by project or by team, not by hour. One practitioner source gives an illustrative invoice of "1 month, team of 5: $500,000 + 20% travel." Hourly billing is the Big 4 / implementation-firm model. So team size and mix are part of the scope and price.

---

### The Seats

#### Partner (Senior Partner / Managing Director and Partner)
- **Owns:** The client relationship, the quality bar, the final answer, and selling the next piece of work.
- **Does on the engagement:** Frames the senior client question, shapes the hypothesis, joins problem-solving sessions (at least twice a week on a typical BCG-style case), pre-wires the CEO or sponsor, runs the SteerCo, challenges the storyline.
- **Does not do:** Build slides or models. Reads and reshapes them.
- **Time:** Part time. See ratios above.
- **Typical asks of the team:** "What's the one-line answer? What would have to be true? Where is the client going to push back?"

#### Associate Partner / Principal
- **Owns:** Senior review and client problem solving across two to four engagements. Bridges the working team and the partners.
- **Does:** Reviews storylines and key analyses, steps in on difficult stakeholders, builds a "spike" (topic expertise), supports business development.
- **Time:** Part time on each engagement.

#### Engagement Manager / Project Leader / Manager
- **Owns:** The workplan, the team's rhythm, the quality of every page, and the day-to-day client relationship. The hardest seat on the team: first time managing people, first time owning the whole answer.
- **Does:** Turns the partner's framing into a workplan with workstreams and deadlines. Assigns work, reviews every output, gives daily feedback, leads client working sessions, owns the storyline and the final deck, manages scope and change control.
- **Time:** Full time on one engagement.
- **Handoff role:** The middle layer. Translates up ("here is the so-what") and down ("here is the analysis I need and why").

#### Associate (McKinsey) / Consultant (BCG, Bain)
- **Owns:** One or more workstreams end to end. Typically post-MBA or advanced degree, or an experienced hire.
- **Does:** Defines the analysis, requests data, runs interviews, builds or directs the model, drafts the pages, supervises an Analyst, presents to mid-level client stakeholders.
- **Time:** Full time.

#### Business Analyst / Associate / Associate Consultant
- **Owns:** Analyses, exhibits, and research inside a workstream.
- **Does:** Cleans data, builds model tabs, creates exhibits, checks numbers, takes notes in client meetings, drafts first-pass pages. Early in an engagement, data work can consume 60-70% of a junior's hours. Slide creation runs about 30% of working time in the middle of the engagement (one practitioner source citing a survey).
- **Judged on:** Accuracy and speed. Moves from "doing the analysis" to "directing it" over about two years.

#### Specialists and Experts
- **Data scientist / analytics team:** Builds heavier models, pulls and cleans large datasets, builds custom tools. Access usually requires senior approval because of the budget.
- **Industry or functional expert (internal):** Pressure-tests assumptions, supplies benchmarks, sits in problem-solving sessions.
- **External experts:** Former executives and operators booked through expert networks for interviews (see `08-support-functions-and-tools.md`).

#### Support Functions (not on the core team, but on the critical path)
- **Research / knowledge team:** Pulls financial data, reports, and benchmarks the team cannot get itself.
- **Graphics / production team:** Builds or beautifies slides, does deck-wide formatting. Needs lead time (often an overnight or multi-day turnaround). Use selectively for SteerCo and final pages.
- **IT / helpdesk:** Unblocks tools and files. Practitioner advice: call after about five minutes stuck on a tech or Excel problem.
- **Engagement support / administrative:** Travel, rooms, badges, expense, calendar.

#### Client-Side Roles
| Role | What they do on the engagement | What the team needs from them |
|---|---|---|
| Executive sponsor (CEO, BU head) | Owns the outcome, decides, unblocks | Access, decisions, air cover. Pre-wire before every SteerCo |
| Day-to-day counterpart (project lead) | Daily contact, data, logistics | Data requests answered, introductions, early reaction to findings |
| SteerCo members | Review progress, decide direction | Pre-reads 2-3 days ahead, clear asks |
| Finance partner (CFO or FP&A) | Validates baselines and savings | Agreed baseline numbers, sign-off on financial impact |
| Subject-matter experts / data owners | Provide data and context | A named person per data request, with a due date |
| Skeptics / "people who feel threatened" | Can slow or block | Early identification (see `/stakeholder-map`) |
| Implementation owners / client PMO | Carry the plan after the team leaves | Involvement in solution design, not just the final readout |

---

### Two Operating Principles Worth Writing On the Wall

1. **The most senior person on the team makes the call when the team debates the recommendation or the client materials, because they are accountable for the deliverable.** Junior people are encouraged to speak up first because they are closest to the data.
2. **Single-point ownership.** Every analysis, every page, every model has exactly one named owner. Shared ownership means no ownership.

---

### Team Composition Checklist (use in `/team-structure`)

- [ ] One partner named, with a stated weekly time commitment
- [ ] One EM full time (or a named exception)
- [ ] Each workstream has one owner at consultant level or above
- [ ] An analyst is paired to each workstream, or one analyst is shared with explicit priorities
- [ ] A named model owner (one person holds the master workbook)
- [ ] A named deck owner (one person holds the master deck)
- [ ] Specialist access confirmed with lead times (data science, graphics, research, experts)
- [ ] Client counterpart per workstream named
- [ ] Backups named for travel, illness, and leave


## Skills by Role

What each seat has to be good at, how the bar rises, and where Consulting-OS helps.

**Proficiency scale:** 1 = Foundational (can do with guidance) · 2 = Working (does it alone, gets reviewed) · 3 = Expert (sets the standard, reviews others) · 4 = Mastery (teaches and sells it)

---

### Skill Matrix

| Skill | Analyst | Associate / Consultant | EM / PL | AP / Principal | Partner | Consulting-OS skills |
|---|---|---|---|---|---|---|
| Structured problem solving (issue trees, MECE, hypotheses) | 1 | 2 | 3 | 3 | 4 | `/problem-statement` `/issue-tree` `/hypothesis-log` |
| Quantitative analysis and sense-checking | 2 | 3 | 3 | 2 | 2 | `/data-analysis` `/market-sizing` `/value-sizing` |
| Excel modeling | 3 | 3 | 2 | 1 | 1 | `/model-spec` `/model-build` `/model-review` |
| Synthesis (finding the "so what") | 1 | 2 | 3 | 4 | 4 | `/day-one-answer` `/storyline` |
| Slide craft (action titles, exhibits, layout) | 3 | 3 | 3 | 2 | 2 | `/ghost-deck` `/slide-build` `/deck-review` |
| Storytelling and narrative | 1 | 2 | 3 | 4 | 4 | `/storyline` `/exec-summary` |
| Research and secondary sources | 3 | 2 | 1 | 1 | 1 | `/industry-primer` `/competitor-analysis` |
| Interviewing (client, expert, customer) | 1 | 3 | 3 | 3 | 4 | `/interview-guide` `/interview-synthesis` |
| Data wrangling (Power Query, SQL, Python, Alteryx) | 3 | 2 | 1 | 1 | 1 | `/data-request` `/data-analysis` |
| Project and workplan management | 1 | 2 | 4 | 3 | 2 | `/workplan` `/daily-plan` `/weekly-plan` |
| Team leadership and feedback | 1 | 2 | 4 | 4 | 4 | `/team-structure` `/weekly-review` |
| Client management and stakeholder influence | 1 | 2 | 3 | 4 | 4 | `/stakeholder-map` `/steerco-prep` |
| Facilitation (workshops, working sessions) | 1 | 2 | 3 | 3 | 3 | `/workshop-design` |
| Executive presence and presenting | 1 | 2 | 3 | 4 | 4 | `/steerco-prep` `/final-readout` |
| Commercial / business development | 0 | 1 | 2 | 3 | 4 | `/proposal-draft` |
| Domain and industry depth | 1 | 2 | 3 | 4 | 4 | `/industry-primer` |
| Change management and implementation design | 1 | 2 | 3 | 3 | 3 | `/change-readiness` `/transition-plan` |
| AI fluency (prompting, verifying, delegating to agents) | 3 | 3 | 3 | 2 | 2 | All skills |

---

### What Changes at Each Level

| Move | From | To | The hard part |
|---|---|---|---|
| Analyst to Associate/Consultant | Doing the analysis | Defining and directing it | Choosing which analysis matters (80/20), not just doing it well |
| Associate/Consultant to EM | Owning a workstream | Owning the whole answer and the team | Managing people for the first time, on an ambiguous problem, with a client watching |
| EM to AP/Principal | One engagement | Several engagements | Reviewing at speed, building a "spike" of expertise, supporting selling |
| AP/Principal to Partner | Advising | Owning the client relationship and revenue | Selling, firm leadership, thought leadership |

Typical time at level (reported, varies by firm and performance): about two years at each early level; two to three years as day-to-day manager; one to four years pre-partner. Many people leave before the pre-partner stage.

---

### Seat Profiles (what "good" looks like)

#### Business Analyst
- **Good:** Numbers are right on first pass. Every exhibit has a source and a so-what draft. Asks "what question is this answering?" before building. Flags data problems within hours, not days.
- **Weak:** Builds beautiful pages for the wrong question. Hardcodes numbers in formulas. Cannot explain how a figure was derived.

#### Associate / Consultant
- **Good:** Arrives at the check-in with a point of view, not a data dump. States the answer first, then the support. Manages the analyst's time. Runs interviews that produce quotes and numbers.
- **Weak:** Waits for direction. Presents findings without implications.

#### Engagement Manager
- **Good:** Keeps a current Day-N answer on the wall. Reviews everything within hours. Knows what the partner will ask. Protects the team's time and scope. Pre-wires the client so nothing surprises anyone.
- **Weak:** Becomes the best analyst on the team and stops managing. Lets scope drift without a change-control conversation.

#### Partner
- **Good:** Asks the three questions that change the storyline. Spends time where the answer is most uncertain. Owns the room with the CEO.
- **Weak:** Arrives late to the problem and reframes it in week 6.

---

### Skills the Client-Side Lead Needs (if you are the client running an MBB-style engagement)

If the Consulting-OS user sits on the client side (for example, an internal strategy lead running a consulting-style engagement with an in-house team, or managing an outside firm), the skills that matter most are: `/problem-statement`, `/stakeholder-map`, `/workplan`, `/data-request`, `/deck-review`, `/model-review`, `/steerco-prep`, `/transition-plan`. Use `/review-panel` with the Partner and Skeptic sub-agents to test outside work.


## Engagement Lifecycle

### Phases and Gates

| # | Phase | Typical timing (core strategy engagement, ~10-12 wks) | Led by | Ends at gate |
|---|---|---|---|---|
| 0 | Pursuit and Contracting | 1-4 weeks before start | Partner | Signed SOW, team named |
| 1 | Mobilize and Frame | Weeks 1-2 | EM | **Kickoff SteerCo:** problem statement, workplan, and hypotheses agreed |
| 2 | Diagnose | Weeks 2-5 | EM + Consultants | **Diagnostic SteerCo:** baseline and Week-1 answer validated |
| 3 | Develop and Synthesize | Weeks 4-9 | Consultants, with client workshops | **Solutions SteerCo:** options, sizing, prioritization |
| 4 | Recommend and Validate | Final 2-3 weeks | Partner + EM | **Final SteerCo / Readout:** decision and mandate |
| 5 | Transition | Last week and after | EM + client PMO | Handover accepted |
| 6 | Close and Learn | Week after | EM | Retro done, case study and follow-on logged |

A BCG-authored example of a waterfall plan (1-2 weeks scoping, 1-2 diagnostics, 3-4 solution development, 3-4 validation) totals 8-12 weeks. The same source offers an agile alternative: 2-3 week sprints, each producing a more refined version of the output (an MVP), four sprints in the example. Consulting-OS supports both; `/workplan` asks which one you are running.

### Duration Benchmarks (as reported; sources differ)

| Engagement type | Typical duration |
|---|---|
| Commercial due diligence | 2-4 weeks |
| Strategy | 4-12 weeks (one source says 3-6 months) |
| Implementation / transformation | 6-24 months |

---

### Phase 0: Pursuit and Contracting

**Goal:** Agree the problem, the approach, the team, and the price before day 1.

**What happens:**
- Partner (with AP/EM support) meets the sponsor, clarifies the real question, and tests an early hypothesis.
- Proposal drafted: situation, objectives, approach by phase, deliverables, team, timeline, fees, assumptions, change-control clause.
- Pricing: fixed or project fee for a well-diagnosed problem with clear deliverables, time-and-materials when scope is genuinely uncertain, and increasingly outcome-linked arrangements.
- Statement of Work (SOW) signed. A named change-control clause lets scope changes be priced and approved rather than absorbed.
- Staffing: partner picks the EM; EM picks or is given the team.

**Outputs:** Proposal, SOW, staffing plan, conflicts and confidentiality clearance.
**Skills:** `/proposal-draft` `/problem-statement` `/team-structure`

---

### Phase 1: Mobilize and Frame (Weeks 1-2)

**Goal:** Everyone agrees on the question, the plan, and the rhythm. The first useful thing reaches the client by day 7-10.

**What happens:**
- Prep before day 1: read the SOW twice (second time hunting for vague parts); research the client and sector; learn the partner's and EM's working styles; ask who the sponsor is, who feels threatened, and who wants it to succeed.
- Kickoff meeting. Agenda: objectives (the single question), scope (in and out), roles and decision rights, governance and cadence, data and access, first 3-5 tasks with owners.
- Data requests sent in the first three days. Data access is a common cause of stalled projects.
- Problem statement worksheet: SMART key question, context, success criteria, scope and constraints, stakeholders, key sources of insight.
- Issue tree or hypothesis tree, prioritized (impact vs ease), turned into a workplan with analyses, owners, sources, and dates.
- Day-1 answer written down, strawman deck started in week 1.
- Team charter: core hours, on-site days, check-in/check-out times, tools.
- Logistics: badges, network access, team room, client template, and early booking of support staff (designers, analysts, research), who are often booked weeks ahead.
- Stakeholder map built in week 1.

**Outputs:** Kickoff deck, problem statement, workplan, data request tracker, hypothesis tree, ghost deck v0, team charter.
**Skills:** `/kickoff-plan` `/problem-statement` `/stakeholder-map` `/issue-tree` `/hypothesis-log` `/workplan` `/data-request` `/day-one-answer` `/team-structure`

---

### Phase 2: Diagnose (Weeks 2-5)

**Goal:** Establish the facts. Where are we today, how do we compare, what is the size of the prize, and which hypotheses survive?

**What happens:**
- Interviews: client executives, middle managers, frontline, customers, external experts. Heavy early investment in one-on-ones and walk-throughs of existing work.
- Data analysis on the client's own data: baseline financials, cost and revenue drivers, operational metrics, customer data.
- Outside-in work: market sizing, competitor and benchmark analysis, industry primer.
- First version of the core model (driver tree, baseline, or market model).
- Hypotheses updated each time data lands. Day-1 answer becomes Week-1, then Week-3 answer.
- Early-win pages shared with the client counterpart to test reactions.

**Outputs:** Diagnostic findings, baseline model v1, interview synthesis, benchmark pack, prioritized list of opportunities, Diagnostic SteerCo deck.
**Skills:** `/interview-guide` `/interview-synthesis` `/data-analysis` `/market-sizing` `/competitor-analysis` `/industry-primer` `/survey-design` `/value-sizing` `/model-spec` `/model-build` `/hypothesis-log` `/steerco-prep`

---

### Phase 3: Develop and Synthesize (Weeks 4-9)

**Goal:** Move from "what is true" to "what should we do." Generate options, size them, test them with the client, and pick.

**What happens:**
- Solution development, often in client workshops (this is where buy-in is built).
- Opportunity sizing with ranges and confidence; scenarios and sensitivities.
- Business case: costs, benefits, timing, NPV or payback.
- Risks and change-readiness assessed.
- Model v2: scenario selector, sensitivities, audit checks.
- Storyline rewritten around the answer, not the analysis.

**Outputs:** Option set, sized initiatives, business case model, workshop outputs, draft storyline and ghost deck, Solutions SteerCo deck.
**Skills:** `/workshop-design` `/value-sizing` `/scenario-sensitivity` `/business-case` `/model-review` `/change-readiness` `/storyline` `/ghost-deck` `/slide-build` `/deck-review` `/review-panel` `/red-team`

---

### Phase 4: Recommend and Validate (Final 2-3 Weeks)

**Goal:** A recommendation the client will act on. The BCG example reserves one to two weeks at the end to iterate and anchor the output with stakeholders.

**What happens:**
- Pre-wire the sponsor and key SteerCo members one-on-one. No surprises.
- Final deck: executive summary, recommendation, roadmap, financials, risks, next steps, appendix.
- Deep numbers tie-out: every number on a slide traced to the model; model audited.
- Red-team the readout: list the 5-10 hardest questions, rehearse answers.
- Final SteerCo / readout presented, ideally with the client project lead presenting to their own boss.

**Outputs:** Final deck, backup/appendix, final model, implementation roadmap, Q&A prep.
**Skills:** `/recommendation-roadmap` `/exec-summary` `/final-readout` `/steerco-prep` `/deck-review` `/model-review` `/red-team` `/review-panel`

---

### Phase 5: Transition (Last Week and After)

**Goal:** The client can run the plan without the team in the room.

**What happens:**
- Handover of models (with a user guide and instructions tab), data, playbooks, templates, and the deck of record.
- Implementation roadmap with named owners, milestones, and KPIs; PMO or transformation office set up on the client side.
- Optional: team stays on for implementation support under a follow-on SOW.

**Outputs:** Handover pack, PMO charter, KPI tracker, follow-on proposal if relevant.
**Skills:** `/transition-plan` `/change-readiness` `/recommendation-roadmap`

---

### Phase 6: Close and Learn

**Goal:** Capture what the next team needs to know.

**What happens:**
- Team retrospective: what worked, what to change, process and tooling lessons.
- Knowledge capture: reusable slides, model modules, benchmarks, expert contacts, anonymized case study.
- Client follow-up: referral or case-study request (one practitioner source says make it within a week of the final readout), follow-on opportunity logged.
- Feedback for individuals.

**Outputs:** Retro notes, knowledge asset list, case study draft, calibration data for estimates.
**Skills:** `/engagement-retro` `/weekly-review`

---

### Gate Criteria (use in `/steerco-prep`)

| Gate | Must be true to pass |
|---|---|
| Kickoff | Question is SMART and agreed in writing; scope in/out listed; sponsor named; cadence set; data owners named |
| Diagnostic | Baseline numbers agreed with the client finance partner; top hypotheses confirmed or killed with evidence; prize sized within a range |
| Solutions | Options sized and ranked with a stated method; owners identified; risks named; the client has reacted to the leading option in a working session |
| Final | Recommendation unambiguous; every number traces to the model; decision requested is explicit; implementation owner exists |
| Transition | Client team has run the model once without us; PMO in place; KPI baseline recorded |


## Tasks by Phase

Every task on a strategy engagement, with who does it (R = does the work, A = accountable, C = consulted), who reviews, what comes out, and which Consulting-OS skill helps.

**Seat codes:** P = Partner · AP = Associate Partner/Principal · EM = Engagement Manager/PL · C = Associate/Consultant · A = Analyst · CL = Client counterpart · SP = Specialist/support

---

### Phase 0: Pursuit and Contracting

| Task | R | A | Reviewer | Output | Skill |
|---|---|---|---|---|---|
| Clarify the real question with the sponsor | P | P | AP | Problem hypothesis, scope notes | `/problem-statement` |
| Draft proposal and approach | EM | P | AP | Proposal deck or document | `/proposal-draft` |
| Build the team plan and fee | EM | P | AP | Staffing plan, fee model | `/team-structure` |
| Negotiate SOW, add change-control clause | P | P | Firm legal/risk | Signed SOW | `/proposal-draft` |
| Conflicts, confidentiality, independence checks | EM | P | Risk/Legal | Clearance record | `sub-agents/risk-compliance-advisor.md` |

### Phase 1: Mobilize and Frame

| Task | R | A | Reviewer | Output | Skill |
|---|---|---|---|---|---|
| Read SOW twice; list vague areas | EM, C | EM | P | Questions list | `/kickoff-plan` |
| Research client, sector, competitors (week 0-1) | A | C | EM | Industry primer | `/industry-primer` |
| Build stakeholder map; rank influence and interest | EM | EM | P | Stakeholder map and pre-wire plan | `/stakeholder-map` |
| Hold kickoff meeting | EM | P | P | Kickoff deck and notes | `/kickoff-plan` |
| Write SMART key question and problem statement worksheet | EM | P | P, CL | Signed-off problem statement | `/problem-statement` |
| Send data requests (within first 3 days) | C, A | EM | EM | Data request tracker | `/data-request` |
| Build issue/hypothesis tree and prioritize | EM, C | EM | P | Tree + 2x2 | `/issue-tree` `/prioritize` |
| Write workplan (what, how, who, when) | EM | EM | P | Workplan | `/workplan` |
| Write the Day-1 answer | EM | P | P | One-paragraph hypothesis | `/day-one-answer` |
| Sketch ghost deck v0 | EM, C | EM | P | Ghost deck | `/ghost-deck` |
| Hold team charter conversation | EM | EM | None | Core hours, tools, norms | `/team-structure` |
| Arrange logistics and book support early | A | EM | None | Room, access, template, support bookings | `/kickoff-plan` |
| Deliver an early win (one useful page by day 7-10) | C | EM | P | One page to client | `/slide-build` |

### Phase 2: Diagnose

| Task | R | A | Reviewer | Output | Skill |
|---|---|---|---|---|---|
| Write interview guides (execs, frontline, customers, experts) | C | EM | EM | Guides | `/interview-guide` |
| Book and run interviews; take notes | C, A | C | EM | Notes within 24 hours | `/meeting-notes` |
| Synthesize interviews into themes | C | EM | EM | Interview synthesis | `/interview-synthesis` |
| Clean and structure client data | A | C | C | Clean dataset, data log | `/data-analysis` |
| Baseline analysis: revenue, cost, operations, customers | A, C | C | EM | Baseline model, exhibits | `/data-analysis` `/model-build` |
| Market sizing (top-down and bottom-up, triangulated) | A, C | C | EM | Sizing model | `/market-sizing` |
| Competitor and benchmark analysis | A | C | EM | Benchmark pack | `/competitor-analysis` |
| Survey design and analysis (if needed) | C, SP | C | EM | Survey results | `/survey-design` |
| Size the prize (driver trees, ranges) | C | EM | P | Opportunity sizing | `/value-sizing` |
| Update hypotheses; log what evidence moved them | C | EM | P | Hypothesis log | `/hypothesis-log` |
| Daily check-in / check-out | EM | EM | None | Priorities, blockers | `/team-checkin` |
| Prepare Diagnostic SteerCo | EM | P | P | Deck, pre-read, pre-wire plan | `/steerco-prep` |

### Phase 3: Develop and Synthesize

| Task | R | A | Reviewer | Output | Skill |
|---|---|---|---|---|---|
| Design and run solution workshops with the client | EM, C | EM | P | Workshop outputs | `/workshop-design` |
| Generate and screen options | C | EM | P | Option long-list and short-list | `/prioritize` |
| Size each initiative; document method | C, A | C | EM | Sized initiatives | `/value-sizing` |
| Build business case (costs, benefits, timing, NPV/payback) | C | C | EM, CL finance | Business case model | `/business-case` |
| Scenarios and sensitivities | A | C | EM | Scenario tab, tornado | `/scenario-sensitivity` |
| Assess risks and change readiness | C | EM | P | Risk register, readiness view | `/change-readiness` |
| Independent model review | A (not the builder) | EM | SP | Review log | `/model-review` |
| Rewrite storyline around the answer | EM | P | P | Storyline v2 | `/storyline` |
| Populate ghost deck with analysis | C, A | C | EM | Draft deck | `/slide-build` |
| Review deck page by page | EM | P | P | Marked-up deck | `/deck-review` |
| Red-team recommendation | Sub-agents | EM | P | Red-team memo | `/red-team` `/review-panel` |
| Weekly status to sponsor | EM | EM | P | Status page | `/status-update` |

### Phase 4: Recommend and Validate

| Task | R | A | Reviewer | Output | Skill |
|---|---|---|---|---|---|
| Pre-wire sponsor and SteerCo members | P, EM | P | None | Pre-wire notes | `/steerco-prep` |
| Executive summary | EM | P | P | One-page summary | `/exec-summary` |
| Recommendation and implementation roadmap | EM, C | EM | P | Roadmap with owners | `/recommendation-roadmap` |
| Final deck assembly and polish (request graphics early) | C, A, SP | EM | P | Final deck | `/final-readout` |
| Number tie-out: every slide figure to model | A | EM | C | Tie-out log | `/deck-review` |
| Q&A preparation | EM, C | EM | P | Top 10 hard questions | `/red-team` |
| Present final SteerCo | P, EM, CL | P | None | Decision | `/final-readout` |
| Log decisions | EM | EM | None | Decision log | `/decision-log` |

### Phase 5 and 6: Transition and Close

| Task | R | A | Reviewer | Output | Skill |
|---|---|---|---|---|---|
| Handover pack: models, data, deck of record, user guide | C, A | EM | CL | Handover pack | `/transition-plan` |
| Stand up client PMO or tracker | EM, CL | EM | P | KPI tracker | `/transition-plan` |
| Train client users on the model | C | EM | None | Trained users | `/transition-plan` |
| Team retrospective | EM | EM | P | Retro notes | `/engagement-retro` |
| Knowledge capture | C, A | EM | P | Reusable assets | `/engagement-retro` |
| Case study and follow-on | P | P | None | Case study, follow-on proposal | `/engagement-retro` |

---

### Standing Tasks (every week of the engagement)

| Task | Owner | When |
|---|---|---|
| Update workplan and hypothesis log | EM | Monday and Friday |
| Chase outstanding data requests | A | Daily |
| Team check-in and check-out | EM | Daily |
| Partner problem-solving session | EM + P | 2+ times a week |
| Pre-read and pre-wire | EM | 2-3 days before each SteerCo |
| Weekly sponsor status | EM | Weekly |
| Decision log update | EM | After each decision |
| Model version save and change log | Model owner | Daily |
| Weekly review and learning log | EM | Friday |

### Time Allocation (rough shape, junior seats)

| Stage | Where the hours go |
|---|---|
| Early weeks | 60-70% data gathering, cleaning, and modeling |
| Middle weeks | About 30% slide creation; the rest in analysis, interviews, and synthesis |
| Pre-SteerCo days | Heavy slide, tie-out, and rehearsal load |

These percentages come from practitioner sources and one survey cited by one source. Treat them as planning heuristics, not norms.


## Cadence and Handoffs

### The Rhythm

**Principle:** The week is organized around the next client touchpoint (SteerCo, progress review, working session), not around individual tasks. Work backwards from it.

#### Daily

| Time (typical) | Event | Who | Purpose |
|---|---|---|---|
| Morning, ~30 min | Team check-in / huddle | Whole team | Priorities, split of work, what client meetings are coming, blockers |
| Mid-morning to early afternoon | Deep work blocks | Analysts, Consultants | Models, data cuts, research, interview notes |
| Early afternoon | Client working sessions and meetings | EM, Consultants | Share progress, confirm assumptions, collect data |
| Afternoon | Slide building and synthesis | Consultants, Analysts | Turn analysis into pages, answer review comments |
| Late afternoon | Manager or partner check-in / case team meeting | EM + Partner/AP | Feedback, direction, decisions |
| End of day | Check-out (round-robin) | Whole team | What got done, what is next, who needs help |
| Evening | Synthesis of the day's findings into the next update | Whole team | "What do we now believe?" |

A McKinsey day-in-the-life post shows the pattern from the EM seat: car-pool with the team to the client, client's own daily check-in, weekly priorities with client team leaders, analysis for a later session with a partner, 5pm team check-out, 6pm problem-solving session with the partner, and evening refining of materials.

#### Weekly

| Day | Event | Notes |
|---|---|---|
| Monday | Set the week's definition of success; refresh workplan | Define what has to be true by the next SteerCo |
| Mid-week | Partner problem-solving sessions (2+ per week on a typical BCG-style case) | Partner gives input on storyline, challenges hypotheses |
| Weekly (some cases bi-weekly) | Client progress review / SteerCo | Core anchor. Most of the week's work is packaged into its storyline |
| Weekly | Sponsor status page | One page, same format each time |
| Thursday/Friday | Team learning and feedback; admin, expenses, training, recruiting | Traditional model: team on client site Monday-Thursday, home-office Friday. Post-COVID many projects are hybrid |
| Friday | Weekly review and plan | `/weekly-review` then `/weekly-plan` |

**Hours (anecdotal, from practitioner write-ups):** normal weeks run roughly 55-65 hours; weeks right after a deliverable are lighter (~45); weeks before a major board-level presentation run heavier (~75). Treat as indicative.

#### Periodic

| Cadence | Event |
|---|---|
| Weekly or bi-weekly | SteerCo (the sponsor group) |
| Monthly | Executive sponsor check-in with partner (if SteerCo is less frequent) |
| At each gate | Gate review (see `03-engagement-lifecycle.md`) |
| Mid-engagement | Team health check and feedback conversation |
| End of engagement | Retro and individual feedback |

**Sponsor communication rhythm:** the project lead sees the team daily; the sponsor may see it every week or every few weeks. Calendar sponsor meetings 2-3 months ahead so cancellations are less likely. Hold the SteerCo weekly, with no exceptions, even if there is little to report, if that is what was agreed.

---

### Meeting Types

| Meeting | Length | Owner | Output | Skill |
|---|---|---|---|---|
| Team check-in / check-out | 15-30 min | EM | Priorities and blockers | `/team-checkin` |
| Problem-solving session (team + partner) | 45-90 min | EM | Decisions on storyline, hypotheses, next analyses | `/meeting-agenda` `/meeting-notes` |
| Client working session | 60-90 min | Consultant or EM | Assumptions confirmed, data agreed | `/meeting-agenda` |
| Workshop | Half day to 2 days | EM | Options, buy-in | `/workshop-design` |
| Interview | 30-60 min | Consultant | Notes with quotes and numbers | `/interview-guide` |
| SteerCo | 60-90 min | Partner | Decisions and next-step mandate | `/steerco-prep` |
| Retro | 60 min | EM | Lessons | `/engagement-retro` |

#### Pre-Read and Pre-Wire Rules
- Share the executive summary with the client counterpart **2-3 days before** the SteerCo. Never surprise them.
- Preview the final recommendation with the sponsor early to build buy-in.
- Red-team the meeting: list the five to ten most likely questions and test answers.
- Give the client project lead a prominent role, ideally presenting to their own boss.
- Plan 15-20 minutes of content for a sponsor update and expect to get about half the time. Open with the executive summary, then spend the meeting on decisions, not recap.
- One-page status standard: overall health in one sentence; progress against last period's three commitments; three commitments for next period; decisions needed with dates; risks named before they surface.

---

### The Review Ladder

Nothing reaches the client without a more senior reviewer.

```
Analyst  --draft exhibit + backup-->  Consultant  --workstream page + so-what-->  EM
   ^                                                                                |
   |                                                                          page turn
   |                                                                                v
Production / graphics  <--polish request--  EM  --storyline + deck-->  Partner / AP
                                                                                |
                                                                          pre-wire
                                                                                v
                                                                         Client sponsor
```

**Review SLAs (write these into your team charter):**
| Reviewer | Turnaround |
|---|---|
| EM on an analyst/consultant page | Same day for urgent pages; otherwise within a few hours of the next check-out |
| Partner on a storyline | Within 24 hours of a problem-solving session |
| Graphics team | Overnight to several days; book early |

---

### Handoff Contracts

A handoff is a promise. Each one has the same four parts: **Brief, Backup, So-what, Ask.**

| Handoff | From to To | Brief (what was asked) | Backup (what travels with it) | So-what (the take) | Ask |
|---|---|---|---|---|---|
| Question framing | Partner to EM | Key question, hypothesis, client politics | Proposal, sponsor notes | "Here's what I think is true" | "Build a plan to prove or kill it" |
| Workstream brief | EM to Consultant | Workstream question, deadline, output format | Workplan row, hypothesis, data list | "This analysis matters because..." | "Come back with a point of view by X" |
| Analysis spec | Consultant to Analyst | Exact analysis, data source, chart type | Mock exhibit, formulas to use | "The finding we expect is..." | "Backup ready by X; flag data issues early" |
| Draft exhibit | Analyst to Consultant | Draft chart or table | Model tab, source file, assumptions, checks | "What I see in the data is..." | "Confirm or redirect" |
| Page for review | Consultant to EM | Page(s) with action titles | Model, sources, open questions | "The so-what is..." | "Reaction, then approval" |
| Deck for review | EM to Partner | Full storyline and deck | Executive summary, open issues, risk list | "The answer is..." | "Challenge the logic, tell me the three weakest pages" |
| Polish request | EM to Graphics | Pages, deadline, template | Marked-up draft, data files | Intended message per page | "Format and fix, return by X" |
| Pre-read | EM to Client counterpart | Exec summary, key pages | Backup on request | Decisions required | "Tell us what will surprise your boss" |
| Model handover | Model owner to Reviewer | Model purpose, tabs, checks | Spec, assumptions log, version log | Key outputs and ranges | "Break it" |
| Engagement handover | EM to Client PMO | Plan, owners, KPIs | Models, data, user guide | What to watch | "Run the model once without us" |

#### Handoff Failure Modes
- **Backup missing:** The page lands without a source. Reviewer cannot check. Rework follows.
- **No so-what:** Data dump. The reviewer has to do the thinking.
- **Silent redirection:** The EM changes the question but not the brief. The analyst builds the wrong thing.
- **Late flag:** Data problem found at the review stage, not at the cleaning stage.
- **Version drift:** Two people edit different copies of the model or deck. Fix: one deck owner and one model owner.

---

### Escalation Paths

| Situation | First stop | Then |
|---|---|---|
| Data not delivered | Client counterpart | Sponsor via EM |
| Scope creep | EM | Partner and sponsor, using change-control clause |
| Team disagreement on recommendation | EM | Most senior person decides |
| Quality concern on a page | Reviewer | EM |
| Client conflict or political issue | EM | Partner, immediately |
| Confidentiality incident (wrong file sent, client data in wrong tool) | EM | Partner and firm risk, same day |


## Support Functions and Tool Stack

### Support Functions Around the Team

| Function | What it does | How teams use it | Lead time / cost note |
|---|---|---|---|
| **Research / knowledge team** | Pulls financial statements, industry reports, and data only the central research desk can access; finds internal prior work and experts | Request in week 0-1 for the industry primer and baseline financials | Quick for simple pulls; ask for scope and deadline in writing |
| **Graphics / production team** | Builds slides from a sketch, beautifies drafts, does deck-wide find-and-replace and alignment | At McKinsey the team often designs the content and format and graphics builds the slide; at BCG and Bain it is mainly polish. Use selectively for SteerCo and final pages | Turnaround takes time (overnight to days). Book early. Polishing needs planning and approval |
| **Data analytics / digital hubs** | Heavier analytics, custom tools, data engineering. Examples of firm units: McKinsey's QuantumBlack, BCG X, Bain's Advanced Analytics Group | Pull in for large datasets, machine-learning work, or tools the client will keep | Usually requires senior approval and a dedicated budget |
| **Expert networks** | Book calls with former executives, operators, and customers | Expert interviews for benchmarks, market views, and pressure-testing | Compliance rules apply: no inside information, no restricted companies; calls often logged |
| **IT helpdesk** | Fixes tools, laptops, file access | Call after about 5 minutes stuck on a tech or Excel problem | Fast |
| **Practice and expertise leaders** | Provide frameworks, prior cases, benchmarks, and sometimes a partner "expert" for hard problems | Ask in week 1 for the closest prior work | Via partner or EM |
| **Recruiting / staffing** | Place people on the team | EM works through partner | Weeks |
| **Engagement support / admin** | Travel, rooms, expenses, scheduling | Early request | Days |

**Practitioner caveat:** Junior consultants still build most of their own slides and do much of their own research. Support teams work when briefed well. The consultant owns quality and must give a clear sketch, data, deadline, and intended message.

**Access norm:** Analysts and associates typically need their EM's approval to use paid support because costs are charged to a cost center.

### Tool Stack (typical)

| Job | Common tools |
|---|---|
| Decks | PowerPoint with firm or client master; think-cell; Mekko Graphics; slide libraries |
| Models | Excel (Power Query, PivotTables, Solver); Python/R and SQL for scale; Alteryx for repeatable pipelines |
| Visual analytics | Tableau, Power BI |
| Project plan / tracker | Excel or PowerPoint Gantt, Smartsheet, Asana, Microsoft Planner |
| Collaboration | Microsoft Teams or Slack; SharePoint, Box, or the client's data room |
| Survey | Qualtrics, SurveyMonkey; conjoint platforms |
| Transcription and notes | Otter, Grain, Teams or Zoom transcripts |
| Research | Company filings, industry databases, firm knowledge base, expert networks |
| AI | Firm-approved generative AI (for example Lilli at McKinsey, ChatGPT Enterprise and Deckster at BCG, Sage at Bain, as reported) |

### Data Environment Rules (non-negotiable)
- Client confidential data stays in approved environments (client data room, firm-approved tenant, or approved AI). It does not go into public or unapproved tools.
- Keep a data log: what was received, from whom, when, with what permission, where stored.
- Personal data follows privacy law (GDPR, CCPA, sector rules) and the SOW.
- Expert network calls follow the network's and the firm's compliance rules.
- Work product is shared on the firm's or client's tenant, never on personal accounts.

### Where Claude Fits
In Consulting-OS, Claude covers much of the research, first-draft analysis, notes, formatting, and review work that used to go to analysts and production support. Use it for speed and breadth. Keep humans accountable for the answer, the numbers, and anything client-confidential. See `09-ai-in-consulting-2026.md`.

### Google Workspace Option
Where the client or firm works in Google Workspace, Claude can create and convert files through the Drive connector and edit them in place through the Sheets and Slides editor connectors. It is a platform choice like any other: it needs the client's written approval for client data, named-person sharing, and files owned in a firm shared drive. See `advanced/google-workspace-option.md`.


## AI in Consulting (as of October 2026)

**Reliability note:** Figures below come from press coverage in 2025-2026 quoting firm leaders. They conflict in places and change fast. Use them for direction, not for quotation. Re-check before you cite.

### What the Firms Report

| Firm | Reported tooling and use |
|---|---|
| **McKinsey** | Lilli, an in-house generative AI platform on the firm's knowledge base (launched 2023). Reported monthly use above 70-75% of staff. Used for research, summarization, analysis, brainstorming, drafting proposals, and building slides from prompts through agents. A "Tone of Voice" tool checks report tone. Client data may go only into Lilli (not into outside chatbots). Leadership has described a workforce of humans and AI agents; reported agent counts range from about 20,000 to 25,000. Headcount reported falling from above 45,000 to about 40,000. QuantumBlack reported at about 1,700 people and about 40% of the firm's work. Shift reported from fee-for-service toward outcome-linked business cases |
| **BCG** | ChatGPT Enterprise to all staff (reported 33,000); 18,000+ custom GPTs; Deckster, a slide editor reported as trained on 800-900 templates with a "review this" button that grades slides against best practice (about 40% of associates reported using it weekly); GENE, a conversational assistant; an agent-building platform in beta. AI advisory work reported at about a fifth of revenue |
| **Bain** | Sage, an internal assistant built on OpenAI models |
| **Others** | Deloitte (Sidekick, Zora AI agents, Ascend), PwC/Strategy& (Microsoft Copilot) |

### What Is Changing on the Engagement

| Work | Before | Now |
|---|---|---|
| First-draft slides | Analyst builds from sketch | Agent drafts from prompt and template; human edits |
| Research and prior-work search | Research desk and knowledge team | Knowledge-base assistant with internal expert pointers |
| Interview notes and synthesis | Manual | Transcript → structured notes → theme clustering |
| Data cleaning and first-pass analysis | Analyst in Excel/Alteryx | Assisted code and formulas, still reviewed by a person |
| Slide QC | Manager and graphics review | Automated checks against best-practice rules, then human review |
| Proposals | Weeks of EM and AP time | Drafted from knowledge base in hours |
| Tone and house style | Partner edits | Style agents |

Reported implication: routine drafting and slide production shifts to AI; people focus on client-facing, judgment-heavy work. Leaders say this does not necessarily mean fewer analysts. Critics on anonymous forums call current tools "functional enough" for low-stakes tasks.

### What Does Not Change
- **Accountability.** The partner and EM own the answer. The client pays for judgment.
- **Layered review.** AI output enters the review ladder at analyst level, no higher.
- **Burden of proof.** A claim that will be used to commit money needs sources and a second check.
- **Confidentiality.** Client data goes only into approved environments.
- **Relationships.** Pre-wiring, trust, and facilitation stay human.

### Operating Rules for Consulting-OS

1. **Claude takes the analyst and junior-consultant seats; the human holds EM, AP, and Partner.** You can ask Claude to play a reviewer seat through sub-agents, but you make the call.
2. **Every number gets a source and a tie-out.** If Claude cannot cite where a figure came from, it marks it `[UNSOURCED]` and does not put it on a slide.
3. **Facts vs assumptions are labeled.** Claude tags each statement as Sourced Fact, Client-Provided, Estimate, or Hypothesis.
4. **No client data in unapproved tools.** Confirm your environment (see `setup/environment-keys.md`). If you are not sure the environment is approved, use anonymized or synthetic data.
5. **Do not invent quotes, benchmarks, or citations.** Placeholders are labeled `[PLACEHOLDER: need source]`.
6. **Check arithmetic by running it.** Claude recomputes totals and sensitivities in code or in the model, not in prose.
7. **Review AI drafts like an analyst's.** Run `/deck-review` or `/model-review` before anything goes upstream.
8. **Disclose AI use where the client or firm requires it.** Check the SOW and firm policy.

### Pricing Direction
Reported movement toward outcome-linked and shared-risk arrangements raises the importance of baselines, measurement, and the transition plan. `/value-sizing`, `/business-case`, and `/transition-plan` include a "measurement and baseline" section for that reason.

### Skills the Team Now Needs More Of
Verification habits, prompt and context design, ability to define a good analysis precisely enough to delegate it, and the judgment to know when the output is plausible but wrong.


## Glossary

| Term | Meaning |
|---|---|
| **Action title** | A slide title written as a full-sentence conclusion ("Partner channel CAC is 40% below paid"), not a topic ("CAC by channel") |
| **Appendix / backup** | Supporting pages not presented live but available when questions arise |
| **Answer first** | Start with the recommendation, then support it (Bain's phrasing; the same idea as Day-1 answer and Pyramid Principle) |
| **Back-of-envelope** | A fast rough calculation to sense-check a result or size a problem |
| **Baseline** | The current-state numbers against which impact is measured. Must be agreed with the client finance partner |
| **Benchmark** | A comparison to peers or best practice |
| **Bridge / waterfall** | A chart that walks from one number to another through its drivers (for example, an EBITDA bridge) |
| **Burden of proof** | The level of evidence a claim needs before the audience will accept it. Ranges from expert opinion to statistical models |
| **Case team** | The firm-side team on an engagement (Bain/BCG usage; "engagement team" at McKinsey) |
| **Change control** | The SOW process for pricing and approving scope changes |
| **Check-in / check-out** | Short daily team meetings at start and end of the day |
| **Day-1 / Week-1 answer** | The team's current best answer to the key question, written before the analysis is complete and revised constantly |
| **Deck of record** | The master version of the deck; all others are derived |
| **Diagnostic** | The phase (or a small engagement) that establishes facts and the size of the prize |
| **Dot-dash** | Text outline of a storyline: dots are top-level messages, dashes are supporting facts |
| **80/20** | Focus on the 20% of analyses that drive 80% of the answer |
| **EM / PL** | Engagement Manager (McKinsey) / Project Leader (BCG) |
| **Exec summary** | The one page (or slide) that carries the whole answer |
| **Ghost deck** | A deck of blank slides with action titles, chart sketches, and data needs written in, built before the analysis |
| **Governing thought** | The single top message of a pyramid |
| **Hypothesis** | A testable statement about the answer ("We can add $8M EBITDA by winning new customers"). Must be falsifiable, material, and actionable |
| **Hypothesis tree** | An issue tree built from hypotheses instead of questions |
| **Issue tree** | A MECE breakdown of the key question into sub-questions |
| **Key question** | The SMART question the engagement exists to answer |
| **Leave-behind** | A deck that stands alone without a presenter |
| **MECE** | Mutually exclusive, collectively exhaustive: no overlap, no gaps |
| **Mekko / Marimekko** | A variable-width stacked chart used for market share and segment analysis |
| **MVP (output)** | An early, rough version of the final output, refined each iteration |
| **Model owner / deck owner** | The one person who holds the master workbook or deck |
| **Page turn** | A page-by-page review of the deck with the page owner in the room |
| **Pre-read** | Material sent to attendees before a meeting |
| **Pre-wire** | Previewing content one-on-one with key stakeholders before the group meeting, so nothing surprises anyone |
| **Prize** | The total value at stake (the sized opportunity) |
| **Problem statement worksheet** | One-page capture of the question, context, success criteria, scope and constraints, stakeholders, and key sources of insight |
| **Pyramid Principle** | Barbara Minto's method: one governing thought supported by grouped arguments, top-down |
| **Quick win** | A low-effort, high-visibility step the client can start immediately |
| **Readout** | The final presentation of findings and recommendations |
| **Red team** | A group that attacks the recommendation to find weaknesses before the client does |
| **SCQA** | Situation, Complication, Question, Answer: the opening frame |
| **SOW** | Statement of Work: the contract for scope, deliverables, team, timeline, and fees |
| **SteerCo / SteerCom** | Steering committee: the client group that oversees the engagement and makes decisions |
| **Sticker / tracker** | A tag on a slide marking section, status, or "Preliminary" |
| **Strawman** | An early draft intended to be attacked and improved |
| **Synthesis** | Turning findings into a "so what" |
| **Tie-out** | Verifying that each number on a slide matches the model and the source |
| **Transformation office / PMO** | The client-side team that runs implementation |
| **Workstream / module** | A defined slice of the work with one owner |
| **Workplan / analysis plan** | The what, how, who, and when for each analysis, aligned to meeting milestones |
| **Wild shot / trap / quick win / big win** | BCG's labels on an effort-vs-importance grid of analyses |


# Part 2: Frameworks

## Change Management and Implementation

**Purpose:** Make sure a recommendation can be carried out. Used by `/change-readiness`, `/transition-plan`, `/recommendation-roadmap`.

---

### Why Strategy Engagements Fail After the Readout
- No named owner on the client side
- Plan lives in a deck, not in a tracker with dates and KPIs
- Baseline never agreed, so savings cannot be proven
- Middle management never involved in design
- Incentives still reward the old behavior
- The team that built the model leaves; nobody can run it

### Readiness Questions (from the problem-solving method)
1. Does each person who must change, from CEO to frontline, understand what changes and why, and are they committed?
2. Are key leaders and role models personally committed to behaving differently?
3. Are formal mechanisms (KPIs, incentives, governance, systems) in place to reinforce the change?
4. Do people have the skills and confidence to act in the new way?

### Two Reference Models (use one)
| Model | Steps |
|---|---|
| **Kotter 8 steps** | Urgency · coalition · vision · communicate · remove barriers · short-term wins · build on gains · anchor in culture |
| **ADKAR** | Awareness · Desire · Knowledge · Ability · Reinforcement |

### Stakeholder Change Curve
For each stakeholder group: current stance (champion / supporter / neutral / skeptic / blocker), what they lose, what they gain, the message, the messenger, the first ask.

### Implementation Plan Components
| Component | Contents |
|---|---|
| **Initiatives** | Sequenced, with timing and dependencies |
| **Owners** | One named client owner per initiative |
| **KPIs** | Metric, baseline, target, source, frequency, owner |
| **Governance** | Transformation office or PMO; weekly cadence; escalation |
| **Quick wins** | 30/60/90-day items that prove momentum |
| **Risks** | Likelihood, impact, mitigation, owner |
| **Resources** | People, budget, tools, external support |
| **Communications** | Audience, message, channel, timing |
| **Capability building** | Training, playbooks, hiring |

### Transition Pack Checklist
- [ ] Deck of record and backup
- [ ] Final model, user guide, instructions tab, version log
- [ ] Data folder and data log
- [ ] Initiative charters
- [ ] KPI tracker with baselines
- [ ] Governance calendar
- [ ] Training done; client user ran the model once unaided
- [ ] Follow-on support agreement (or explicit end of support)

### Measurement and Baseline (important for outcome-linked fees)
Agree in writing: baseline definition and period, measurement method, who signs off, treatment of one-time items, attribution rules when other initiatives overlap.


## Hypothesis-Driven Approach

**Purpose:** Reference for working from an early answer instead of from all the data. Used by `/hypothesis-log`, `/day-one-answer`, `/workplan`, `/data-analysis`.

**Source:** McKinsey and BCG problem-solving material; BCG partner deck at Aalto University (March 2022).

---

### The Idea
Form a testable answer on day 1. Direct every analysis at proving or killing it. Revise as evidence arrives. The alternative (collect everything, then think) boils the ocean.

A hypothesis is not an answer. Explain this to clients, who may be nervous about a solution reached early. The hypothesis structures the work; the evidence decides.

### What Makes a Good Hypothesis
| Test | Question |
|---|---|
| **Falsifiable** | Can it be proven or disproven with data? |
| **Debatable** | Could a smart person disagree? A statement that cannot be wrong teaches nothing |
| **Material** | If reversed, would the overall logic change? |
| **Non-obvious** | Would it sound naive if you said it to the CEO? |
| **Actionable** | Does it point to something the client could do? |

### Burden of Proof
Decide how strong the evidence must be before the audience will accept it. The ladder, weakest to strongest:
1. Expert opinion or anecdote
2. Case studies and analogs
3. Benchmarks
4. Client data analysis
5. Statistical test or correlation
6. Analytic model or pilot

Raise the bar when the finding is controversial, the decision is large, or the audience is skeptical.

### Day-1, Week-1, Week-N Answers
- Write the answer on day 1, even with little data.
- Rewrite after every analytical step. Keep a version history (this is what `/hypothesis-log` does).
- Always have an answer and communicate frequently.
- When a hypothesis dies, log why. A killed hypothesis is a finding.

### Analysis Prioritization (BCG grid)
| | Low effort | High effort |
|---|---|---|
| **High importance** | **Quick win:** do first and use to shape the rest | **Big win:** invest time, plan carefully, iterate |
| **Low importance** | **Wild shot:** try without spending much | **Trap:** ask whether it is really needed or whether an analog exists |

### Hypothesis Log Structure
| ID | Hypothesis | Parent branch | Evidence needed | Burden of proof | Status | Evidence so far | Confidence | Last updated |
|---|---|---|---|---|---|---|---|---|
| H1 | Partner channel CAC is 40% below paid | Grow revenue | Channel-level CAC, 24 months | Client data | Testing | CAC 38% lower in 2 of 3 regions | Medium | Oct 12 |

Status values: Open · Testing · Supported · Weakened · Killed · Replaced.

### Common Failure Modes
- **Anchoring:** Falling in love with H1 and reading ambiguous data as support.
- **Unfalsifiable hypothesis:** "We can improve performance."
- **No update trail:** Nobody can tell why the answer changed.
- **Too many hypotheses:** More than five at the top level means the tree is not prioritized.
- **Hiding the hypothesis from the client:** Share it as a working view, not a conclusion.

### Helpful Habit: Ask "What Would Have to Be True?"
For a proposed recommendation, list the conditions that must hold. Test each. If any cannot hold, the recommendation fails or must change.


## Interviewing Playbook (Client, Customer, Expert)

**Purpose:** How to run interviews that produce quotes, numbers, and surprises. Used by `/interview-guide`, `/interview-synthesis`.

---

### Interview Types
| Type | Who | Purpose | Length | Output |
|---|---|---|---|---|
| **Executive** | CEO, BU heads, CFO | Hypotheses, priorities, politics, success criteria | 30-60 min | Direction, constraints, sensitivities |
| **Middle management** | Function and regional leads | How work actually gets done; data sources | 45-60 min | Process, pain points, data leads |
| **Frontline** | Operators, sales reps, agents | Reality check | 30-45 min | Specific examples, workarounds |
| **Customer / user** | Buyers and end users | Needs, switching, willingness to pay | 30-45 min | Quotes, segments |
| **External expert** | Former execs, operators | Benchmarks, market view | 30-60 min | Numbers, pressure test |
| **Supplier / partner** | Channel partners | Economics, relationships | 30 min | Terms, friction |

### Structure of a 45-Minute Interview
1. **Open (3 min):** Purpose, confidentiality, how notes are used.
2. **Context (7 min):** Role, scope, how they spend time.
3. **Core questions (25 min):** 5-7 open questions that test your hypotheses without leading.
4. **Numbers (5 min):** Ask for sizes, rates, frequencies, with ranges.
5. **Close (5 min):** "What should I have asked?" "Who else should I speak to?" "What data would you point me to?"

### Question Craft
- Open: "Walk me through the last time..." beats "Do you like...?"
- Ask for stories and specifics, then numbers.
- Test hypotheses by asking what would have to be true.
- Ask what they would do with a magic wand and no constraints.
- Silence is a tool. Do not fill it.
- Separate fact (what happened), opinion (what they think), and rumor (what they heard).

### Roles in the Room
- **Lead:** asks. **Scribe:** takes verbatim notes with timestamps. One person only listens.
- Notes written up within 24 hours. Tag each note: quote · number · hypothesis supported/weakened · follow-up.

### Expert Network Rules
- No material non-public information. No current employees of restricted clients or competitors in sensitive contexts.
- Follow the network's and firm's compliance script.
- Record who, when, topic, and approval.
- Ask for ranges and reasoning, not only point numbers.

### Synthesis Method
1. List every claim with the interview ID.
2. Cluster by theme (bottom-up).
3. Count frequency (how many of N raised it) and intensity (how strongly).
4. Separate by segment (exec vs frontline can diverge, and the divergence is a finding).
5. Tie each theme to a hypothesis: supports, weakens, new.
6. Pull 1-2 representative quotes per theme (anonymized unless agreed).
7. Write the "so what" for each theme.

### Confidentiality
Interview notes are confidential. Attribute by role or ID, not by name, unless the interviewee agreed. Store in the approved location.


## Issue Trees and MECE

**Purpose:** Reference for breaking a problem into pieces that are complete and non-overlapping. Used by `/issue-tree`, `/problem-statement`, `/workplan`.

**Source:** McKinsey problem-solving approach (Umbrex summary of Staff Paper 66); BCG course material.

---

### What an Issue Tree Is
A branching decomposition of the key question into sub-questions. Each level is **MECE** (mutually exclusive, collectively exhaustive). Branches are small enough to analyze.

### Issue Tree vs Hypothesis Tree
| | Issue tree | Hypothesis tree |
|---|---|---|
| Nodes are | Open questions ("How can Alpha increase revenue?") | Testable statements ("Alpha can add $8M EBITDA by winning new customers") |
| Use when | Team does not know enough to hypothesize | Team can form specific answers |
| Strength | Complete and safe | Focused and fast |
| Risk | Boils the ocean | Confirmation bias |

Move back and forth between them. Start with an issue tree, then turn the most promising branches into hypotheses.

### Writing Good Nodes
- Questions start with **what, how, or why**. "How can the client minimize its tax burden?" beats "Tax."
- Each branch gets one owner and one set of analyses.
- Use consistent logic at each level (do not mix a process split with a customer split at one level).

### Building Patterns
| Problem type | Natural first split |
|---|---|
| Profit problem | Revenue vs Cost → (Price × Volume × Mix) vs (Fixed + Variable) |
| Growth problem | Existing vs New → customers, products, geographies, channels (Ansoff) |
| Market entry | Market attractiveness, ability to win, entry mode, economics |
| M&A | Strategic fit, valuation and synergies, integration risk |
| Operations | Inputs → process → outputs; capacity, utilization, quality |
| Organization | Structure, roles, talent, governance, culture |
| Pricing | Customer value, cost, competition, strategy |

### MECE Checks
1. **Overlap check:** Could one fact fit in two boxes? If yes, redefine.
2. **Gap check:** Is there a possible answer that fits in none of the boxes? Add an "other" and question it.
3. **Level check:** Are siblings at the same altitude?
4. **Action check:** Can each leaf be analyzed with data you can get?
5. **So-what check:** If each leaf were true, would the parent be answered?

### Prioritizing Branches
Score each leaf on **impact** (size of prize, strategic importance) and **ease** (data availability, time, client control). Plot on a 2x2. Start with high-impact, easy ones. Drop low-impact, hard ones. Revisit as the analysis teaches you more. See `prioritization-matrices.md`.

### Worked Example
**Key question:** How can Alpha Manufacturing raise EBITDA by $13M (to $50M) by 2028?
```
Raise EBITDA by $13M
├── Grow revenue
│   ├── Win new customers (+$8M hypothesis)
│   ├── Raise price / mix on existing customers
│   └── Expand to new geographies
└── Cut cost (+$5M hypothesis)
    ├── Procurement
    ├── Conversion cost (plants)
    └── SG&A
```


## Market Sizing Methods

**Purpose:** Estimate market size credibly and fast. Used by `/market-sizing`, `/value-sizing`.

---

### Three Methods
| Method | How | Strength | Weakness |
|---|---|---|---|
| **Top-down** | Start from a total (population, industry revenue) and filter by segment, penetration, and share | Fast, uses published data | Can hide weak assumptions behind big numbers |
| **Bottom-up** | Units × price: number of customers × usage × price | Grounded in the unit economics | Needs customer and price data; risk of missing segments |
| **Analog / triangulation** | Compare to a similar market, region, or period | Fast sanity check | Analog may not hold |

**Rule:** Use at least two methods and reconcile. A gap above ±20-30% means an assumption is wrong. Find it.

### TAM / SAM / SOM
- **TAM:** Total demand for the product category.
- **SAM:** The part you can serve with your product and geography.
- **SOM:** The part you can realistically capture in the plan period.

### Process (6 steps)
1. **Define the market precisely:** product, customer, geography, time, price basis, what is excluded.
2. **Pick the unit:** revenue, units, transactions, users.
3. **Build top-down:** each filter written with source and rationale.
4. **Build bottom-up:** segment customers, size each, apply usage and price.
5. **Triangulate:** compare, explain the gap, adjust.
6. **Sensitivity:** vary the three biggest assumptions; report a range.

### Example Skeleton (travel distribution)
- Top-down: global hotel bookings × share booked through intermediaries × share in target region × average commission.
- Bottom-up: number of corporate travel programs in region × average spend × managed-travel penetration × take rate.
- Analog: more mature region's penetration curve applied with a lag.

### Back-of-Envelope Discipline
- Round aggressively; keep powers of ten honest.
- Write every assumption on the page.
- Check units on both sides.
- Ask: does the per-customer figure make sense?

### Source Hierarchy
1. Client internal data
2. Company filings and regulator data
3. Industry associations and government statistics
4. Analyst reports and databases
5. Expert interviews
6. Press and web (lowest; verify)

Cite the source and year for every input. Mark estimates as estimates.


## Prioritization Matrices

**Purpose:** Choose which issues to analyze, which initiatives to recommend, and which tasks to do first. Used by `/prioritize`, `/issue-tree`, `/workplan`, `/recommendation-roadmap`.

---

### 1. Impact vs Ease (issues and initiatives)
| | Easy | Hard |
|---|---|---|
| **High impact** | Do now (quick wins) | Plan and invest (big bets) |
| **Low impact** | Do if free (fillers) | Drop |

**Scoring:** 1-5 on each axis with a written rationale. Impact: EBITDA or strategic value. Ease: time, cost, data, client control, dependencies.

### 2. Effort vs Importance (analyses) - BCG grid
Big win · Quick win · Wild shot · Trap (see `hypothesis-driven-approach.md`).

### 3. Value vs Risk (initiatives)
| | Low risk | High risk |
|---|---|---|
| **High value** | Commit | Pilot first |
| **Low value** | Backlog | Reject |

### 4. Weighted Scoring (when a committee must choose)
| Criterion | Weight | Option A | Option B | Option C |
|---|---|---|---|---|
| Financial value (NPV) | 30% | | | |
| Strategic fit | 20% | | | |
| Feasibility | 20% | | | |
| Risk | 15% | | | |
| Time to impact | 15% | | | |
| **Weighted score** | 100% | | | |

Agree the weights with the SteerCo before scoring, not after. Run a sensitivity on the weights.

### 5. Critical Path Triage (team tasks) - LNO adapted
| Class | Meaning | Rule |
|---|---|---|
| **Critical** | On the path to the next SteerCo or gate | Do first, protect time |
| **Multiplier** | Reusable asset that speeds later work (a model module, a template) | Do when it saves more than it costs |
| **Neutral** | Needed, low visibility | Do efficiently |
| **Overhead** | Admin | Batch it, delegate it |

### 6. Horizon View (roadmap)
- **0-90 days:** quick wins, mobilization
- **3-12 months:** core initiatives
- **12+ months:** structural bets

### Rules of Thumb
- Score in a group, then discuss the outliers.
- Show the ranges, not point estimates, when sizing.
- If the top three are close, the criteria are not discriminating. Add one.
- Re-run the matrix when new data lands.


## Pyramid Principle and SCQA

**Purpose:** Reference for structuring any answer, memo, or deck so the conclusion comes first and the support is grouped logically. Used by `/storyline`, `/exec-summary`, `/day-one-answer`, and `/deck-review`.

**Source:** Barbara Minto, *The Pyramid Principle*; McKinsey problem-solving material (Staff Paper 66 via Umbrex); BCG partner course material.

---

### The Core Idea
Think bottom-up (gather and group facts to find the message). Communicate top-down (lead with the message, then the support).

```
                 Governing thought (the answer)
                /            |             \
          Key line 1     Key line 2      Key line 3
          /    |   \      /   |   \       /   |   \
        facts  facts ...                        (data, analysis, evidence)
```

### Rules
1. **One governing thought** per pyramid.
2. **Ideas at any level summarize the ideas below them.**
3. **Ideas in a group are the same kind** (all reasons, all steps, all options) and logically ordered.
4. **Write each box as a declarative sentence.** Topic labels hide missing thinking.
5. **Exclude what is interesting but irrelevant.**

### Three Tests
| Test | Question | Fails when |
|---|---|---|
| **Down** | Does each box pose one question that the boxes beneath it fully answer? | Support answers a different question |
| **Across** | Is each level MECE? | Overlaps or gaps |
| **Up** | Do the grouped boxes yield the "so what" above them? | The top line is not really implied by the support |

### Ordering Logic Inside a Group
| Order | Use when |
|---|---|
| **Time / process** | Steps, phases, cause and effect |
| **Structure** | Parts of a whole (segments, regions, functions) |
| **Degree / importance** | Reasons ranked from most to least important |

### SCQA (the opening)
| Letter | Content | Test |
|---|---|---|
| **S**ituation | What the audience already agrees is true | No one argues |
| **C**omplication | What changed or what makes it hard | Creates tension |
| **Q**uestion | What must be decided or solved | Natural question that follows |
| **A**nswer | The governing thought | Answers the Q directly |

SCR (Situation, Complication, Resolution) is the same without the explicit question.

**Example**
- S: Regional hotel group grew RevPAR 6% a year for five years.
- C: Growth has stalled for four quarters while distribution costs rose 22%.
- Q: How does the group restore profitable growth without cutting service?
- A: Shift 20% of paid bookings to direct and corporate channels over two years. Worth $14-19M EBITDA.

### Deductive vs Inductive Groupings
- **Deductive:** A → B → therefore C. Use when the audience needs to follow a chain ("The market is shrinking. We have no share advantage. So we should exit").
- **Inductive:** Three parallel reasons support one conclusion. Use for most recommendations.

### Common Failures
- A "topic" governing thought ("Our analysis of the channel mix").
- Key lines that overlap ("Improve marketing" and "Improve acquisition").
- Support that answers "how" when the box asks "why."
- Exec summary that narrates the project instead of stating the answer.


## Seven-Step Problem Solving

**Purpose:** The backbone method most MBB-style engagements follow. Used by `/strategy-sprint`-style planning inside `/workplan`, and as the checklist for `/review-panel`.

**Source:** McKinsey's 7-step process (as documented in Staff Paper 66 and practitioner guides); BCG's equivalent success factors.

---

| # | Step | What you produce | Key tool | Skill |
|---|---|---|---|---|
| 1 | **Define the problem** | SMART key question; problem statement worksheet (question, context, success criteria, scope and constraints, stakeholders, key sources of insight) | Problem statement worksheet | `/problem-statement` |
| 2 | **Structure the problem** | Issue tree or hypothesis tree, MECE | Tree | `/issue-tree` |
| 3 | **Prioritize** | The few branches that matter | 2x2 impact vs ease | `/prioritize` |
| 4 | **Plan the analyses** | Workplan: for each branch, the analysis, end product, source, timing, owner | Workplan | `/workplan` |
| 5 | **Conduct analyses** | Findings that prove or kill hypotheses | Model, interviews, benchmarks | `/data-analysis` `/model-build` |
| 6 | **Synthesize** | The "so what" in a pyramid; Day-1 answer revised to Week-N | Pyramid, dot-dash | `/storyline` |
| 7 | **Communicate** | Recommendations, plan, executive summary, SteerCo deck | Deck | `/exec-summary` `/final-readout` |

### The Distinctiveness Practices (run through every step)
| Practice | Meaning | Prompt to ask |
|---|---|---|
| **Expand** | View the problem from other perspectives | What would the customer, supplier, frontline employee, or competitor say? How did another industry solve this? |
| **Link** | Find relationships among issues, hypotheses, findings | What depends on what? Where do two workstreams collide? |
| **Distill** | Find the essence | What 20% matters? What can I cut? |
| **Lead** | Stay one step ahead, then step back and revalidate | What will the client ask next? Does this pass the success criteria? |

### Workplan Horizons
Plan at three horizons. Near-term detail is high, long-term detail is low.
1. What is due at the end of the engagement
2. What is due at key progress reviews
3. What is due at daily and weekly team meetings

### Sources of Insight Checklist
Core team · Client leaders and frontline · Client customers and suppliers · Internal firm experts · External experts and published research · Communications specialists

### Organization Change Check (before finalizing recommendations)
- Does each person who must change understand what and why, and are they committed?
- Are leaders personally committed to behaving differently?
- Are formal mechanisms in place to reinforce the change?
- Do people have the skills and confidence to act in the new way?


## Storyline Patterns

**Purpose:** Proven shapes for the argument of a deck. Pick one before building the ghost deck. Used by `/storyline`, `/ghost-deck`, `/steerco-prep`.

---

### Pattern 1: Diagnose → Decide → Deliver (default for strategy)
1. Executive summary
2. Context and question (SCQA)
3. What we found: baseline, benchmarks, root causes
4. What it means: size of prize and options
5. What we recommend and why
6. What it takes: roadmap, owners, investment
7. Risks and mitigations
8. Decisions needed and next 30/60/90 days
9. Appendix

### Pattern 2: Case for Change
Burning platform (facts) → cost of inaction → vision → path → proof points → ask. Use when the audience does not yet agree there is a problem.

### Pattern 3: Options and Recommendation
Decision framing → criteria → options (one page each, same format) → comparison → recommendation → conditions to make it work. Use when the SteerCo must choose.

### Pattern 4: Status SteerCo
Where we are vs plan → what we learned → what changed in our answer → decisions needed → next period commitments → risks. Use for recurring SteerCos.

### Pattern 5: Workshop Deck
Objectives → ground rules → inputs (facts only) → exercises → outputs template → next steps. Mostly blank frames the room fills in.

### Pattern 6: Proposal
Situation → objectives → approach (phases) → deliverables → team → timeline → investment → why us → next steps.

### Pattern 7: Due Diligence Summary
Investment thesis → market → competitive position → customers → financial quality → risks and mitigants → value-creation levers → valuation implications.

### Pattern 8: Handover
What we did → what we found → what the plan is → how to run the model → who owns what → KPIs → how to get help.

---

### Slide Types in Any Pattern
| Type | Job |
|---|---|
| **Executive summary** | Whole answer on one page |
| **Section divider / tracker** | Orientation |
| **Fact page** | One finding, one chart, one so-what |
| **Framework page** | Structure the thinking (2x2, matrix, tree) |
| **Comparison page** | Options side by side with same criteria |
| **Quote page** | Voice of customer or employee, 3-4 quotes, with count of how many said it |
| **Roadmap page** | Timeline, owners, dependencies |
| **Financial page** | Bridge, scenarios, sensitivity |
| **Decision page** | The ask, options, recommendation |
| **Appendix page** | Method, detail, sources |

### Storyline Review Questions
1. Read only the titles. Does the argument hold?
2. Does the exec summary make sense without the deck?
3. Which three pages would the CEO challenge hardest?
4. Which pages could be deleted without losing the argument?
5. Is every recommendation backed by at least one fact page?


## Strategy Frameworks Cheat Sheet

**Purpose:** The standard frameworks consultants reach for, with when to use each and when to put it down. Used by `/industry-primer`, `/competitor-analysis`, `/issue-tree`, `/recommendation-roadmap`.

**Rule:** A framework is a starting structure, not an answer. Never paste one onto a slide without a client-specific finding.

---

| Framework | Use for | Core idea | Watch out |
|---|---|---|---|
| **Porter's Five Forces** | Industry attractiveness | Rivalry, entrants, substitutes, buyer power, supplier power | Static; needs a "so what" for the client's position |
| **Value chain** | Where margin and cost sit | Inbound, operations, outbound, marketing, service + support | Define activities at the right granularity |
| **Profit pool** | Where industry profit sits and shifts | Map profit by value-chain stage or segment | Data heavy |
| **3C (Company, Customers, Competitors)** | Quick strategic view | Fit between strengths, customer need, rival position | Shallow if used alone |
| **Ansoff matrix** | Growth options | Existing/new products × existing/new markets | Needs sizing per cell |
| **BCG growth-share matrix** | Portfolio allocation | Relative market share × market growth | Simplistic; define market carefully |
| **GE-McKinsey 9-box** | Portfolio with more nuance | Industry attractiveness × competitive strength | Scoring can be arbitrary |
| **Three Horizons** | Balancing now vs next vs later | H1 core, H2 emerging, H3 options | Define each horizon concretely |
| **McKinsey 7S** | Organization alignment | Strategy, structure, systems, shared values, skills, style, staff | Descriptive, not diagnostic by itself |
| **Business model canvas** | Business model design | Segments, value, channels, revenue, cost, key resources | Qualitative |
| **Customer segmentation** | Who to serve | Needs-based over demographic where possible | Segments must be actionable and sizable |
| **Customer journey** | Experience gaps | Stages × touchpoints × pain/gain | Pair with data |
| **Jobs to be done** | Why customers buy | Functional, emotional, social job | Needs interviews |
| **7 Powers** | Durable advantage | Scale, network, counter-positioning, switching costs, branding, cornered resource, process power | Use for defensibility analysis |
| **Wardley / capability maps** | Capability and dependency view | Evolution of components | Best with a technical audience |
| **SWOT** | Quick synthesis | Strengths, weaknesses, opportunities, threats | Weak unless quantified and prioritized |
| **PESTEL** | Macro scan | Political, economic, social, technological, environmental, legal | Pick the 2-3 that matter |
| **Pricing: value-based, cost-plus, competitor-based** | Price setting | Willingness to pay vs cost vs rivals | Needs elasticity evidence |
| **Make/buy/partner** | Capability sourcing | Control, speed, cost, risk | Decide criteria first |
| **Stage-gate** | Investment staging | Funding released at gates against criteria | Gate criteria must be measurable |

### Pairing Guide
| Question | Start with | Then |
|---|---|---|
| Should we enter this market? | Market sizing, Five Forces | Ability to win, entry mode, economics |
| Where should we grow? | Ansoff, segmentation | Sizing, capability fit |
| Why is profit falling? | Profit tree | Cost/price/mix deep dives |
| How do we compete? | 3C, 7 Powers | Customer needs, positioning |
| How do we organize? | 7S, spans and layers | Role design, transition plan |
| Should we acquire? | Strategic fit, synergies | Valuation, integration risk |
| How do we price? | Willingness to pay | Elasticity, competitor response |

### Pre-Built Slide Frameworks
MECE issue map · 2x2 · harvey ball comparison · capability heatmap · value chain with margin overlay · initiative one-pager · roadmap Gantt · RACI · risk heatmap. See `templates/ghost-deck-template.md`.


## Value Driver Trees and Bridges

**Purpose:** Connect an action to a financial outcome using drivers the client can measure. Used by `/value-sizing`, `/business-case`, `/model-spec`.

---

### Core Trees

#### Profit (EBITDA)
```
EBITDA
├── Revenue
│   ├── Volume (customers × frequency × units)
│   ├── Price (list × realization)
│   └── Mix
└── Cost
    ├── Variable (COGS, distribution, commissions)
    └── Fixed (people, facilities, IT, overhead)
```

#### Customer Revenue
```
Revenue = Customers acquired × ARPU × Retention curve
Customers acquired = Traffic × Conversion
ARPU = Base price + Upsell + Cross-sell
```

#### Unit Economics
`Contribution per unit = Price - Variable cost per unit`  ·  `LTV/CAC` ·  `Payback = CAC / (monthly contribution)`

#### Cost Take-Out
Spend cube: category × supplier × business unit × owner. Levers: demand (need less), specification (buy different), supplier (buy better), process (do differently).

### Rules for a Good Driver Tree
1. Each node is measurable with data the client has or can get.
2. The math works: parent equals a function of children.
3. Drivers are independent where possible (avoid double counting).
4. Stop where the lever becomes an action ("change commission plan").
5. Every lever has an owner on the client side.

### The Bridge (Waterfall)
Baseline → initiative 1 → initiative 2 → ... → target. Rules:
- Baseline agreed with the client finance partner.
- Initiatives are additive after removing overlaps (list the overlaps and how they were netted).
- Ranges, not points, in early versions. Show low / base / high.
- Separate run-rate from in-year impact; separate one-time costs from recurring.
- Label confidence: High (data-backed), Medium (benchmark-backed), Low (hypothesis).

### Sizing Template
| Initiative | Driver | Baseline | Target | Δ | Calculation | Low / Base / High | Confidence | One-time cost | Owner |
|---|---|---|---|---|---|---|---|---|---|

### Confidence Calibration
| Evidence | Haircut guidance (adjust to your firm's norms) |
|---|---|
| Client data, validated by owner | 0-10% |
| Benchmark from comparable peers | 20-30% |
| Analog from another industry | 30-50% |
| Pure hypothesis | 50%+ or exclude |

### Double-Counting Checklist
- Do two initiatives claim the same cost line?
- Do revenue initiatives share the same customer base?
- Are enabling costs (IT, change) netted?
- Do savings assume headcount that another initiative also removes?


# Part 3: Deck, model and writing standards

## How a Deck Gets Made

The deck is the argument. An MBB-style deck is built top-down from the answer, then filled bottom-up from evidence. Slide creation is roughly 30% of a consultant's working time in the middle weeks, so the process has to be fast and repeatable.

### The Pipeline (14 steps)

| # | Step | Owner | Output | Time | Skill |
|---|---|---|---|---|---|
| 1 | **Set the objective.** One sentence: what should the audience know, decide, or do? | EM | Objective line | 10 min | `/storyline` |
| 2 | **Pick the document type.** Live presentation (simpler, visual) or leave-behind / report (text-rich, self-explanatory, backup). If both are needed, build the leave-behind first, then cut it down. Keep separate files | EM | Format choice | 5 min | `/storyline` |
| 3 | **Write the Day-N answer.** The governing thought in one or two sentences | EM + Partner | Governing thought | 30 min | `/day-one-answer` |
| 4 | **Frame with SCQA.** Situation (common ground), Complication (what changed), Question (what must be solved), Answer (recommendation) | EM | SCQA box | 20 min | `/storyline` |
| 5 | **Build the pyramid.** Governing thought on top, 3-5 key lines beneath, supporting arguments below. Test it down (does each line answer one question?), across (MECE), and up (do the points add up to the so-what?) | EM | Pyramid | 1 hr | `/storyline` |
| 6 | **Dot-dash storyline.** Dots = top-level messages (become section dividers or key slides). Dashes = supporting facts (become slides). Post it on the team-room wall | EM | Dot-dash | 1 hr | `/storyline` |
| 7 | **Ghost deck.** One blank slide per dash: action title written, chart type sketched, data needed, source, owner, status | EM + Consultants | Ghost deck | 2-3 hrs | `/ghost-deck` |
| 8 | **Partner review of the ghost deck.** Read only the titles. Does the argument hold? (Horizontal flow test) | Partner | Redirected storyline | 45 min | `/deck-review` |
| 9 | **Pull data and run analyses.** Each ghost page gets filled as data arrives; the title may change when the data disagrees | Consultants + Analysts | Draft pages | Days | `/data-analysis` `/slide-build` |
| 10 | **Build exhibits.** Charts from the model into think-cell (or native PowerPoint), linked to Excel where possible | Analysts | Draft exhibits | Hours | `/slide-build` |
| 11 | **Self-review.** Check one message per slide, sources, units, labels, and "so what" in three seconds | Page owner | Clean draft | 15 min/page | `/deck-review` |
| 12 | **EM page turn.** Page by page, with the owner in the room | EM | Marked-up deck | 2-4 hrs | `/deck-review` |
| 13 | **Partner review, then graphics/production polish.** Request graphics support early for SteerCo and final decks | Partner, Graphics | Polished deck | Overnight to days | `/deck-review` |
| 14 | **Final QC and send.** Number tie-out to model, source lines, typos, template compliance, PDF export, version freeze, file naming | Deck owner | Final deck + PDF | 1-2 hrs | `/deck-review` |

**Rules that save the week:**
- Build the ghost deck in week 1 (a "strawman deck"), then iterate. Analysis may prove the early assumptions wrong. That is the point.
- Draft the final one-slide answer early (MVP thinking) and refine it all engagement long.
- Save versions often so deleted slides can be recovered.
- Pages that do not serve the storyline get deleted, however good the analysis.

---

### Storyline Craft

#### Pyramid Principle (Barbara Minto)
- Think bottom-up, present top-down.
- One governing thought. Supporting ideas form a hierarchy. Grouped ideas are the same kind and the same importance.
- Write each level as a declarative sentence, not a topic. "Expansion" is a topic. "We should expand into Europe first" is a message.

#### SCQA Opening
Situation (what everyone agrees on) → Complication (what changed or what is hard) → Question (what must be decided) → Answer (the recommendation).

#### Three Tests
- **Down:** Each governing thought poses one question that the boxes beneath it fully answer.
- **Across:** Each level is MECE.
- **Up:** The grouped boxes yield the so-what above them.

#### Dot-Dash Example
```
• We should shift 20% of paid media to partners in the next two quarters
  - Paid media returns are falling: CPA up 31% in 18 months [Slide 6: line chart]
  - Partner channel CAC is 40% below paid [Slide 7: bar chart + benchmark]
  - The partner pool can absorb the spend: 14 of 22 partners have capacity [Slide 8: table]
• The prize is $12-18M EBITDA by year 2
  - Waterfall from baseline to target [Slide 11]
  - Sensitivity: conversion drives 60% of the range [Slide 12]
• Delivery needs three decisions this quarter
  - ...
```

---

### Slide Standards

#### Anatomy
1. **Action title** (top, largest): a full-sentence conclusion, active voice, specific and quantified, ideally ≤15 words and never more than two lines. If it contains "and," consider splitting the slide.
2. **Subtitle or section header** (optional).
3. **Body:** the chart or table that proves the title. Every element must answer "Why should I believe the title?" Cut anything that does not.
4. **Source line** (bottom, smallest): "Source: [dataset or interview set, date]; [firm] analysis." Unsourced numbers destroy credibility.
5. **Tracker / sticker** (optional): marks section, status ("Preliminary," "Draft for discussion") or workstream.

#### Quality Checks (every page)
- **Accurate:** Data is right and not misleading.
- **Relevant:** Supports the storyline.
- **Actionable:** Leads to a decision or recommendation.
- **So-what test:** The implication is clear within three seconds.
- **Horizontal flow test:** Read only the titles across the deck. The full argument holds.
- **Vertical logic test:** Every body element supports its own title.

#### Formatting Norms (use the client's or firm's template where it exists)
- Margins respected; generous white space; content snapped to a grid; title position and size identical on every page.
- Two font sizes in the body, about two points apart. Typical ranges: titles 18-20pt, body 11-14pt, sources 9-10pt. Never shrink a font to make something fit; cut content.
- One or two font families. 3-4 colors used with meaning.
- Line spacing 1.1-1.3; lines of 8-12 words.
- Consistent number formats, units, and decimal places throughout.

#### Chart Selection
| Message | Chart |
|---|---|
| Bridge from A to B (revenue, EBITDA, cost) | Waterfall |
| Market share across segments with size | Marimekko (Mekko) |
| Comparison across categories | Bar |
| Trend over time | Line or column |
| Share of total | Stacked column or 100% stacked |
| Two variables, many items | Scatter or bubble |
| Timeline, phases, dependencies | Gantt / roadmap |
| Structured options | Matrix (2x2, harvey balls) |

Every chart carries: an action-oriented title, labeled axes with units, a legend if multiple series, a source line, and callouts on the key point. No 3D. Limit series to 3-5. Waterfalls sorted largest to smallest unless process order matters; positive and negative contributions colored differently.

---

### Typical Deck Architecture

#### SteerCo Deck (15-30 pages)
1. Executive summary (one page, the answer)
2. Status vs plan (progress, decisions needed, risks)
3. Key findings, 1 page each, action titles
4. Implications and options
5. Next steps and asks
6. Appendix: backup, methodology, interview list

#### Final Readout (can run 50-100+ pages including appendix)
1. Executive summary
2. Context and question (SCQA)
3. Diagnostic: where we are
4. Options considered and how we chose
5. Recommendation
6. Financial case (bridge, scenarios, sensitivities)
7. Roadmap and governance (Gantt, owners, KPIs)
8. Risks and mitigations
9. Decisions and next 30/60/90 days
10. Appendix (backup, methodology, detail, sources)

---

### Tools and Practice

| Tool/practice | What for |
|---|---|
| PowerPoint with firm/client master template | The deck of record |
| think-cell | Industry-standard charting add-in: waterfall (P&L walks, EBITDA bridges), Marimekko, Gantt with dependencies, difference/CAGR arrows. Charts can link to Excel so the whole deck refreshes from one master workbook |
| Mekko Graphics and similar add-ins | Alternatives for Mekko and complex charts |
| Slide libraries and templates | Reuse frameworks and capability models. Firms keep large template libraries; BCG's internal Deckster tool is reported to be trained on 800-900 templates |
| Alignment and distribution shortcuts | Speeds up layout cleanup |
| Graphics team | Builds from a sketch or beautifies a draft; selective use because of turnaround time |
| PDF export | What the client usually receives. Keep the .pptx as the editable master |

### Number Tie-Out (the step juniors skip)
Every number on a slide traces to a cell in the model. The deck owner keeps a **tie-out log**: slide number, figure, model tab and cell, source, checked by, date. This is the single best defense against the worst consulting error: a wrong number in front of the CEO.

### Versioning and Naming
`[Client]_[Deck]_[Audience]_[vYYMMDD]_[status]` (for example, `Northstar_SteerCo3_Sponsors_v261016_DRAFT`). One master; no copies on desktops; freeze a PDF when sent.

### Variant: Google Slides
Some teams, and many clients, work in Google Slides. The storyline, action titles, one-message-per-page rule, and number tie-out are identical. What changes: no think-cell, so charts are built on the model's Outputs tab and embedded as linked charts (they tie to the model by construction, but typed titles and callouts still need tie-out); theme and master are set once by hand; Slides never shrinks text; images need a public URL or a copy from the template. Freeze by updating linked charts, resolving comments, naming a version, and exporting PDF. Details: `advanced/google-workspace-option.md`.


## How an Excel Model Gets Made

The model is the evidence. A top-tier engagement lives or dies on whether the client's finance partner trusts the numbers. Consultants rarely write formal "financial models" the way bankers do. They build purpose-built models that answer a few specific questions, then stress-test them hard.

### The Lifecycle (9 steps)

| # | Step | Owner | Output | Skill |
|---|---|---|---|---|
| 1 | **Define the three questions the model must answer** and the hypothesis it tests. Write them on the first tab | Consultant | Model purpose | `/model-spec` |
| 2 | **Spec on paper first.** Drivers, structure (driver tree), tabs, inputs and sources, outputs, time axis, units, scenarios. Get the EM to approve the spec | Consultant | Model spec | `/model-spec` |
| 3 | **Prototype with dummy data** to confirm the mechanics work. Start rough; add detail where it matters | Analyst | Skeleton | `/model-build` |
| 4 | **Load real data** and document every source. Do not wait for every data point; get the key ones first | Analyst | Populated model | `/model-build` |
| 5 | **Build calculation logic** in a clean flow: inputs → calculations → outputs | Analyst | Working model | `/model-build` |
| 6 | **Add checks and sense checks.** Sum checks, reconciliations, error flags rolled up to a master check on the cover | Analyst | Check tab | `/model-build` |
| 7 | **Stress test.** Push inputs to extremes and confirm outputs move in the expected direction; test the biggest drivers; build scenarios and sensitivities | Consultant | Scenarios, tornado | `/scenario-sensitivity` |
| 8 | **Independent review.** Someone other than the builder reviews inputs, formulas, outputs, and adherence to standards; reconciles key outputs to independent sources | Reviewer | Review log | `/model-review` |
| 9 | **Lock, version, and hand over.** User guide, instructions tab, assumptions log, version log; client user runs it once | Model owner | Handover pack | `/transition-plan` |

**Working rules that experienced consultants repeat:**
- Share the model with the manager early and often. Do not build in private.
- Get to ~80% complete before adding nuance. Defer nice-to-have factors.
- Start with one scenario, finish it, then copy its rows so scenarios have parallel structure.
- In an A/B comparison, include only the variables that differ.
- Be able to say which variables have the largest effect on the outcome.
- Check that someone unfamiliar with the situation could follow the model.

---

### Sheet Architecture (default)

| Tab | Purpose |
|---|---|
| **Cover** | Title, purpose, owner, version, status, date, table of contents with hyperlinks, color key, master check |
| **Guide** | How to use the model; model structure diagram; top 4-5 components explained |
| **Inputs** | Every assumption and driver in one place; unit, source, owner, date, comment |
| **Data** | Raw client or external data, untouched. Cleaned data goes in a separate tab |
| **Calc_** | Calculation tabs by module, flowing top to bottom and left to right. One periodicity per sheet |
| **Scenarios** | Scenario selector and scenario-specific inputs |
| **Outputs** | Summary tables and chart sources that feed the slides. Tab names match slide references |
| **Checks** | All error checks and sense checks, summarized to one master flag |
| **Log** | Version log, change log, open issues, review sign-off |

Keep model content in one workbook where possible. Avoid external links unless necessary. Avoid hidden sheets. Any sheet reachable in two clicks from the contents list.

---

### Formatting and Color Conventions

**Pick one convention, show it on the Cover, and keep it the same on every tab.** Conventions differ by firm and client (the table shows the common default and two alternatives seen in published guidance).

| Element | Common default | Alternative seen |
|---|---|---|
| Hard-coded inputs and assumptions | **Blue font** (light yellow fill optional) | Black (inputs) with calculations in blue |
| Formulas / calculations | **Black font** | Blue, orange, or purple |
| Links from other sheets | **Green font** | Treated as calculations |
| Links to external files | Red or orange | |
| Check cells | Conditional format: green when OK, red when flagged | |
| Estimates not yet confirmed | Yellow highlight or "(Est.)" label | |
| Outputs | Bold, border, subtle fill | Green or red font for results |

If a client or firm template exists, use it. Otherwise use the default and document it. Keep to roughly 6-8 colors; use muted tones; check contrast.

**Number formatting:** negatives in brackets, zeros as dashes, consistent decimals, a units column on every line, display millions with number formats (do not divide the underlying value), label real vs nominal.

**Layout:** freeze panes with headers, labels, and checks visible; no merged cells (use Center Across Selection); consistent first-period column across sheets; one blank column after the time series; group and collapse rather than hide; hide gridlines on finished sheets; print setup (headers, margins, page numbers).

---

### Formula Rules

1. **No hard-codes inside formulas.** Only 1, 0, -1 (and occasionally 12 or 4) may appear in a formula. Everything else is an input cell.
2. **One formula per row**, copied across the whole time series. Same logic for actuals and forecasts.
3. **Enter each input once**, link to it everywhere else.
4. **Do not mix a link and a calculation in the same cell.**
5. **Avoid daisy-chaining.** Link to the original source cell.
6. **Avoid volatile and fragile functions:** OFFSET and INDIRECT are high risk. Use INDEX-MATCH or XLOOKUP over VLOOKUP/HLOOKUP. Use nested IF and array formulas only with a reason.
7. **No circular references.** Set calculation to automatic; iterative calculation off.
8. **Break complex formulas into steps.** If you cannot explain a formula in about 30 seconds, split it.
9. **Test errors specifically.** Do not wrap everything in IFERROR to hide problems.
10. **Avoid macros** unless unavoidable; never rely on recorder output.
11. **Replace references to blank cells with explicit zeros.**
12. **Use data validation drop-downs** (not form controls) for selectors.

---

### Checks

| Type | Examples |
|---|---|
| **Integrity checks** (must be zero) | Sub-totals equal totals; annual equals sum of monthly; assets equal liabilities plus equity (if applicable); allocated equals source; data row counts match |
| **Reconciliation** | Model baseline to the client's reported financials; external-link values to source |
| **Sense checks** (rule-of-thumb, do not necessarily mean error) | Growth rates within plausible bands; margin within benchmark; unit economics positive; price × volume ties to revenue |
| **Error flags** | No #REF!, #DIV/0!, #NUM! in outputs under any scenario |
| **Master check** | One cell on the cover, linked to all check totals, using a named tolerance (use ABS and 1/0 flags) |

---

### Documentation

- Cover: purpose, intended users, assumed knowledge, unusual sections.
- Every sheet and section described.
- Every input has Source, Owner, Date, and Comment.
- Instructions tab or cell comments for the top components.
- Plain-language explanation column beside key calculations.
- Version log: what changed, who, when.
- File naming: `[Model]_[STATUS]_[vYYYYMMDD]_[initials].xlsx` (internal edits tracked separately from external releases).

---

### Common Model Types on a Strategy Engagement

| Model | Core logic | Key checks |
|---|---|---|
| Market sizing | Top-down (market → segment → share) and bottom-up (units × price), triangulated | Two methods within an agreed band |
| Baseline / driver tree | Revenue or cost decomposed into drivers (price × volume × mix) | Ties to reported actuals |
| Opportunity sizing / EBITDA bridge | Baseline → initiatives with ranges → target | Sum of initiatives equals bridge; no double counting |
| Business case / NPV | Costs, benefits, timing, discount rate | Cash flows sum; sensitivity to ramp-up and one-time costs |
| Benchmarking database | Peer metrics normalized | Definitions consistent; source per row |
| Pricing / revenue model | Elasticity or price-volume scenarios | Revenue reconciles to current baseline |
| Capacity / operations model | Demand, throughput, utilization, headcount | Capacity ≥ demand in base case |
| Org / FTE model | Spans and layers, cost per FTE, transitions | Headcount ties to HR data |
| Cost take-out | Spend cube by category × supplier × owner; savings levers | Spend ties to ledger |

### Data Handling Tools
Excel (Power Query for repeatable cleaning, PivotTables, Power Pivot), SQL, Python or R for large files, Alteryx or similar for repeatable pipelines, Tableau or Power BI for exploration, Solver and what-if tools (Goal Seek, Scenario Manager, Data Tables) for optimization and scenarios. Keep raw data untouched; every transformation logged.

### Review Methods (mix at least three)
1. **Input review:** every input against its source.
2. **Formula review:** consistency across rows, no hard-codes, no broken ranges (trace precedents/dependents; Go To Special).
3. **Output review:** reasonableness vs rule of thumb and benchmark.
4. **Back-of-envelope triangulation:** can a 5-line mental model reproduce the answer within ±20%?
5. **Standards review:** adherence to this file.
6. **Independent rebuild** of the key calculation by a second person for high-stakes outputs.

### Model Owner Rule
One person holds the master workbook. Everyone else sends changes to that person or works on a branch copy that is merged at a fixed time. The owner publishes a new version number daily.

### Variant: Google Sheets
The architecture (Cover, Guide, Inputs, Calc, Scenarios, Outputs, Checks, Log), color convention, formula rules, and review methods carry over unchanged. What changes: calculation is live, so verification is reading values and scanning for error cells; versions are named in Version history and frozen by copying to FINAL; Calc, Outputs, and Checks are protected; avoid QUERY, ARRAYFORMULA, IMPORTRANGE, and GOOGLEFINANCE if the file may be exported to Excel; sensitivity tables are formula grids, not Data Tables. Heavy models and very large data stay in Excel. Details: `advanced/google-workspace-option.md`.


## Client Executive Writing Style

Use for SteerCo decks, sponsor emails, executive summaries, final readouts, and board materials.

### Characteristics

**Tone:** Confident, plain, specific. Calm when the news is hard.
**Audience:** CEO, sponsors, SteerCo, board members.
**Goal:** Get a decision.

### Rules

#### 1. Answer First
Open with the conclusion. Then the evidence.
- Avoid: "Over the past six weeks we analyzed..."
- Better: "Recommendation: shift 20% of paid media to partner channels. Worth $14-19M EBITDA by year two."

#### 2. One Message Per Page, Stated as a Sentence
Titles are conclusions with a number: "Partner CAC is 40% below paid, and the pool can absorb the spend."

#### 3. Quantify and Range
- Avoid: "Significant savings"
- Better: "$12-18M run-rate EBITDA (base $15M), 70% backed by client data"

#### 4. Name the Decision
Every executive document ends with the ask: what, by whom, by when.

#### 5. Show Options and a Recommendation
Option A, B, C with the same criteria, then our recommendation and the conditions that make it work.

#### 6. Be Honest About Confidence
Tag: Fact (client data) · Estimate (benchmark) · Hypothesis (to be tested). Executives forgive uncertainty and punish surprises.

#### 7. No Surprises
Nothing new appears in a SteerCo that the sponsor has not seen in a pre-wire.

### Structure for a Sponsor Update (one page)
1. **Overall health:** one sentence
2. **Progress against last period's three commitments**
3. **Three commitments for next period**
4. **Decisions needed** (with dates)
5. **Risks** (named before they surface)

### Structure for an Executive Summary
1. Situation and complication (2 sentences)
2. The answer (1-2 sentences)
3. Three supporting reasons, each with a number
4. What it takes (investment, timeline, owners)
5. The decision requested

### Voice Notes
- Short sentences. Active voice.
- "We recommend," not "it is suggested."
- No jargon the client does not use.
- No em dashes. No buzzwords (leverage, utilize, unlock, harness, streamline, robust, cutting-edge, synergy without a number).
- Numbers: units and period every time ($M, % YoY, FY27).

### Example
**Bad:**
```
We have conducted a comprehensive review of channel performance and identified several areas
of potential optimization that could drive meaningful value.
```
**Good:**
```
Paid-media CPA rose 31% in 18 months. Partner channels acquire at 40% lower cost and have
room for 20% of today's spend. Moving it adds $14-19M EBITDA by year two. We need your
approval to start three partner pilots in Q1.
```


## Internal Team Writing Style

Use for team messages, check-in notes, workstream briefs, review comments, and problem-solving session prep.

### Characteristics

**Tone:** Direct, collegial, fast. Candid about quality.
**Audience:** Partner, EM, teammates.
**Goal:** Move the work. Make the next step obvious.

### Rules

#### 1. Start with the So-What
"Channel CAC is 38% lower for partners in 2 of 3 regions. I think H1 holds. Need West region data to confirm."

#### 2. Brief, Backup, So-What, Ask
Every handoff message has all four (see `engagement-model/05-cadence-and-handoffs.md`).

#### 3. Be Specific About Time and Format
"Need chart v1 by 3pm. Bar chart by region, sorted by CAC, source line to CRM export dated Oct 10."

#### 4. Flag Problems Early
"Data in the CRM export has duplicates (about 8% of rows). Cleaning today. May slip page 12 by two hours."

#### 5. Review Comments Say What and Why
- Avoid: "Fix this."
- Better: "Title states a topic. Make it the conclusion: 'Partner CAC is 40% below paid'."

#### 6. Label Certainty
Fact · Client-provided · Estimate · Hypothesis.

#### 7. Respect the Review Ladder
Send work to the next reviewer with the model, sources, and open questions attached.

### Message Templates

**Assignment**
```
[Name], can you own [analysis]? Question we are answering: [ ]. Data: [ ]. Output: [chart type] by [time].
Expected finding: [ ]. Flag anything odd early. Backup in [model tab].
```

**Status**
```
Done: [ ]. In progress: [ ]. Blocked: [ ] (need [person] by [time]). Next: [ ]. Risk to Friday: [ ].
```

**Request for Review**
```
Page [n] attached. So-what: [ ]. Model tab: [ ]. Open question: [ ]. I need your reaction by [time].
```

### Voice Notes
- Contractions fine.
- Plain words. No buzzwords. No em dashes.
- Bullets for lists, short paragraphs for reasoning.
- Praise specific work in public; give hard feedback in person, same day.


## Proposal and Pursuit Writing Style

Use for proposals, SOW narratives, capability slides, follow-on pitches, and case studies.

### Characteristics

**Tone:** Confident, client-centered, concrete.
**Audience:** Sponsor, procurement, SteerCo.
**Goal:** Win the work on the right terms.

### Rules

#### 1. Start With Their Problem in Their Words
Use the sponsor's own language from the first meeting. Show you listened.

#### 2. Say What They Get
Outcomes and deliverables before method. "In 10 weeks you will have a prioritized plan worth $X, a model your finance team can run, and a 90-day launch plan."

#### 3. Make the Approach Concrete
Phases with weeks, activities, deliverables, and decisions at each gate. Name the first-two-week plan.

#### 4. Introduce the Team by What They Will Do
Role, relevant experience, time commitment. Avoid generic bios.

#### 5. Be Clear on What You Need From Them
Data owners, interview access, decision makers, space.

#### 6. Price Honestly
Fixed fee for well-diagnosed scope. T&M when scope is uncertain, and say why. Include change-control. If outcome-linked, define baseline and measurement.

#### 7. Prove With Specifics
One or two relevant cases with numbers and permission to cite. Anonymize unless approved.

### Structure
1. Situation and objectives
2. What success looks like
3. Our approach (phases, weeks, deliverables)
4. Team and governance
5. Timeline
6. Investment and terms
7. Why us (specific proof)
8. Next steps

### Voice Notes
- No em dashes. No buzzwords.
- "You" and "we." Short sentences.
- Replace claims with evidence.


## Technical and Analytic Writing Style

Use for model documentation, methodology appendices, data notes, assumption logs, and finance-partner communications.

### Characteristics

**Tone:** Precise, neutral, auditable.
**Audience:** Finance partners, analysts, data owners, model reviewers.
**Goal:** Let a skeptical reader reproduce the number.

### Rules

#### 1. Define Before You Use
State what each metric means, its unit, its period, and its source.
"Net revenue = gross bookings less cancellations and refunds, USD, fiscal year ending June."

#### 2. Show the Math
`10,000 eligible accounts x 30% adoption x $5 ARPU x 12 months = $180,000`

#### 3. Separate Facts from Assumptions
Use a table: Item · Value · Source · Date · Owner · Confidence.

#### 4. State Edge Cases and Exclusions
What was excluded and why. What was imputed and how. What changed between data pulls.

#### 5. Use Ranges and Say What Drives Them
"Base $15M; range $12-18M; conversion rate drives 60% of the spread."

#### 6. Version Everything
Model version, data pull date, reviewer, sign-off.

#### 7. Reconcile
Every baseline ties to a client-reported figure. State the variance and its explanation.

### Structure for a Methodology Note
1. Purpose and question answered
2. Data sources (with dates and owners)
3. Definitions
4. Method (steps, formulas)
5. Assumptions and sensitivities
6. Checks performed and results
7. Limitations
8. Reviewer and sign-off

### Voice Notes
- Plain sentences. Passive voice only when the actor is irrelevant.
- No em dashes. No marketing language.
- Units and periods on every number.

