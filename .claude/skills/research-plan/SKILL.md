---
name: research-plan
description: "Plan and run research from the issue tree: locked definitions, MECE ranked questions, source and method plan, compliance check, midpoint check-in, triangulated and graded sources, and a synthesis that updates the hypotheses."
disable-model-invocation: false
user-invocable: true
---

# Research Plan

## Quick Start

```
/research-plan
```
Then provide:
1. **The question or hypothesis** the research must help answer (or let me pull it from the hypothesis log)
2. **The decision or slide it feeds**, who will use the findings, in what format, and by when
3. **Time box and depth**: quick (about 10 searches), standard (about 25), or deep (50 or more)
4. **Which paid sources and experts the team can reach** (databases, expert network, firm knowledge base)

I will write a one-page research brief, lock the definitions, build MECE research questions from the issue tree, rank them by impact, and plan the sources and method for each one, including the questions the open web cannot answer. You approve the plan before I search. After that I run the research, check in with you at the halfway point, log every source with a grade, triangulate the numbers that matter, and write a synthesis that says what moved and what is still open.

**Output:** Plan saved to `outputs/research-synthesis/research-plan-[topic]-[date].md`. Findings and source log saved to `outputs/research-synthesis/research-[topic]-[date].md`.
**Time:** ~10 min to plan, plus ~30 min to run a standard pass

**When to use:** Before `/competitive-landscape`, `/market-sizing`, or `/benchmark-analysis` when the question is open; whenever a hypothesis needs outside evidence; when the sponsor asks "what do we know about X?"

**Phase:** Diagnose  |  **Framework source:** `context-library/frameworks/hypothesis-driven-approach.md`; `context-library/engagement-model/04-tasks-by-phase.md` (research and fact finding)

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md`, `context-library/engagement-info-template.md` | key question, scope, approved platforms, confidentiality, AI policy | The question, the scope limits, and whether web tools may be used on this engagement |
| Issue Tree | `outputs/issue-trees/*.md` | branch, leaf, MECE | The branch this research serves and its leaves, so questions map to the tree |
| Hypotheses | `context-library/hypotheses/*.md`, `outputs/hypotheses/*.md` | H1, confidence, test | The hypotheses the research must test, and what evidence is still missing |
| Prioritization | `outputs/analyses/prioritization-*.md` | impact, effort, rank | Where this research sits among the analyses already ranked |
| Firm Knowledge | `context-library/other/*.md`, `context-library/research/*.md`, `context-library/example-engagements/*` | prior engagement, benchmark, expert | Prior work and expert contacts that can answer a question before we search |
| Research | `context-library/research/*.md`, `outputs/research-synthesis/*.md` | topic, competitor, market, source | Work already done, and sources already logged |
| Ingest Digests | `outputs/research-synthesis/ingest-*/digest-*.md` | topic, claim | What the client already told us, so we do not research it again |
| Fact Base | `context-library/data/fact-base-*.md`, `outputs/analyses/fact-base-*.md` | metric | Numbers already agreed, which the research may check but not replace |
| Interviews | `context-library/interviews/*.md` | expert, quote | Views to corroborate or contradict |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If there is no issue tree for this branch -> Link to `issue-tree`
- If more than seven questions survive scoping -> Link to `prioritize-analyses`
- If the research is a competitor map -> Link to `competitive-landscape`
- If it needs a market number -> Link to `market-sizing`
- If it needs peer metrics -> Link to `benchmark-analysis`
- If it moves a hypothesis -> Link to `hypothesis-draft`
- If it needs an expert or customer voice -> Link to `interview-guide`
- If it needs client data -> Link to `data-request`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/research-synthesis/` and `context-library/research/*.md`: Research and source logs already on file
- `outputs/research-synthesis/ingest-*/`: What the client's own documents already say
- `context-library/hypotheses/*.md`: What needs outside evidence
- `outputs/issue-trees/*.md`: The branch and leaves this research serves
- `context-library/other/*.md` and `context-library/example-engagements/`: Firm knowledge and prior engagements (strip client identifiers before reuse)
- `context-library/engagements/*.md`: Confidentiality, AI policy, expert network and compliance rules

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**Question:** [The question or hypothesis]

**Already known:** [Findings and sources on file, with dates]

**Client's own view:** [What their documents claim, labeled as claims]

### Gaps in Knowledge

I will list what is missing before I plan, for example:
- Whether web tools are approved for this engagement
- Which paid databases, expert networks, and firm knowledge sources the team can reach
- Whether the client, or any company we will research, is publicly listed (this changes the compliance check)
- What the search may and may not mention (client names, deal names, internal numbers)
- Which findings are stale and need a refresh

If the gaps are material, I ask for them first. If they are minor, I proceed with clearly marked assumptions.

---

## Step 1: Diagnostic Questions

### Question 1: The decision and the user
**"What decision or slide does this research feed, who uses it, in what format, by when, and what would change your mind?"**

Research with no decision behind it becomes a reading list. Name the hypothesis, the result that would weaken it, the person who will use the findings (partner, EM, client team), and the format they want (one page, fact pack, backup slides).

### Question 2: The confidentiality line
**"Is there anything I must keep out of search queries?"**

Default: no client name, no project code name, no internal figures, no names of people we interviewed. Search on the market, the competitor set, or the metric, never on the client's situation.

### Question 3: Access
**"Which paid databases, expert networks, and firm knowledge sources can the team use on this engagement?"**

List what the team holds (for example Capital IQ, Bloomberg, Factiva, Gartner, Forrester, Euromonitor, Statista, PitchBook, GLG, AlphaSights, the firm's own knowledge base). I plan only on what you confirm. For anything we lack, I flag it in the plan so you can request access early.

### Question 4: Depth and stop rule
**"Quick, standard, or deep? And when do we stop?"**

Default stop rule: stop a research question when two independent sources of grade A or B agree, or when the time box ends. Report what is still open.

---

## The Process

### Phase A: Plan (show it, get approval, then search)

**1. Write the research brief.** Five lines: the decision this feeds, the user of the findings, the format they want, the due date, and the depth. Add the midpoint check-in (see Phase B, step 15) and name who gets it.

**2. Lock the definitions.** Before any question, write a definitions table: each key term (for example "market", "booking", "active customer"), its scope, period, geography, and unit. Most conflicting numbers come from two definitions of one word. If a definition is the client's to set, ask the sponsor or EM to confirm it. Log the agreed definitions with `/decision-doc`.

**3. Build the research questions from the issue tree.** Take the branch this research serves from `outputs/issue-trees/`. Write one research question for each leaf that needs outside evidence. Then run the MECE check against the parent branch: no two questions answer the same thing, and together they cover the branch. Show any leaf you left out and why (client data answers it, or it is out of scope). If no issue tree exists for this branch, run `/issue-tree` first, or sketch a one-level tree and mark it as a draft. Each question names the hypothesis it tests and the result that would weaken it. Phrase it so it can be answered: "What share of [segment] bookings went through [channel] in the last two full years?" beats "Understand the channel landscape."

**4. Rank and cut.** Score every question on three things, High, Medium, or Low:
- **Impact on the answer:** would the result change the recommendation or a number on a page?
- **Evidence gap:** how little do we already know?
- **Reach:** can we get a reliable answer in the time box with the sources we can access?

Run the High-impact, High-gap questions first. Park or kill Low-impact ones. Keep the plan to five to seven questions. If you have more, use `/prioritize-analyses`. Show the ranking and what you cut.

**5. Plan the sources beyond the open web.** For each question, list sources in this order and mark reach as **have**, **ask** (request access), or **no**:
1. Client data and the ingest digests (what they already told us)
2. Firm knowledge base, prior engagements, and benchmarks (strip client identifiers)
3. Licensed databases and research firms (confirmed in Question 3)
4. Public primary sources: regulator filings, annual reports and 10-Ks, statistical agencies, investor decks, standards bodies, official price lists
5. Reputable secondary sources: industry associations, major business press, peer-reviewed research, analyst summaries with a stated method
6. Experts and customers: expert network calls, client interviews (`/interview-guide`)

Source grades: **A** primary, **B** reputable secondary, **C** weak (vendor blogs, press releases without data, unsourced lists, opinion, forums; a lead, never the proof of a number).

Then list the questions the open web cannot answer on its own (paywalled data, proprietary prices, internal client figures, expert judgment). For each, say what we need and request it now: database access, an expert call, or a `/data-request`. Do not leave these to the end.

**6. Choose the method for each question.** For any number we will size or estimate, plan two independent routes:
- **Top-down and bottom-up:** for example total market times share, against units times price
- **Analog:** a comparable market, company, or geography, with the adjustment stated
- **Source against expert:** a filing or dataset checked against an expert's view

Say which two routes you will use. A fact that exists in one authoritative source (a filed revenue figure, a published rate) needs the source and its date, not a second method.

**7. Draft the search plan.** For each web question: three to five queries, the sites or publishers to favor, and the date window. Add the year to queries about current facts.

**8. Set the budget.** Searches and page fetches allowed, expert calls allowed, the time box, and the stop rule.

**9. Run the confidentiality and compliance check.**
- Read every draft query. Remove client identifiers, code names, internal figures, and interviewee names. If web tools are not approved for this engagement, stop and say so.
- If the client or any company we research is publicly listed, take no material non-public information from experts, insiders, or leaked documents, and stop the research if you receive some. Follow the firm's policy and ask compliance when unsure. I do not give legal advice.
- Before booking an expert call, confirm the firm's expert network rules: no current employees of the client or a competitor on topics that touch confidential information, the required call script, and compliance approval where the policy asks for it.

**10. Show the plan** in the template below and ask for approval or edits before running anything.

### Phase B: Run

**11. Search in batches by research question.** Send independent searches together. Read the result list, then fetch the pages that look primary. Read the page itself, not just the snippet.

**12. Log every source you use** in the source log: ID (S1, S2), URL or reference, publisher, author or body, publication date, date accessed, source type, and grade (A, B, C).

**13. Record each finding as a claim.** One line each: the claim, the number with unit and period (using the locked definitions), the source ID and location (section, table, page), and a status:
- **Sourced:** stated in a grade A or B source
- **Corroborated:** two independent sources agree
- **Triangulated:** two independent methods agree within the tolerance
- **Inferred:** our calculation from sourced inputs (show the inputs)
- **Unverified:** single weak source, or conflicting sources

Any number that drives the answer needs two independent sources or two methods, or it is flagged single-source.

**14. Triangulate.** For each estimated number, put the routes side by side in the triangulation table. If they differ by more than the tolerance (default 25%, set it for the engagement and mark it as an assumption), find the reason before you report: a definition, a period, a scope, or a wrong input. Do not average two numbers that disagree.

**15. Check in at the halfway point.** When about half the time box or budget is spent, send the EM a short note: what we found, what changed or surprised us, what we will cut or add, and any question we need a steer on. Wait for the steer before you spend the second half, unless the user said to continue.

**16. Check recency.** For any "current" fact (a price, a rank, a share, a rule in force), find the date. If the newest source is more than 12 months old, say so on the claim.

**17. Handle conflicts and walls.** When sources disagree, show both values and the reason they may differ (definition, period, scope). Do not pick silently. When a page is paywalled, blocked, or will not load, log it as unreachable and ask the user to supply the file. Do not try to get around it.

**18. Stop** by the stop rule. List what is still open.

### Phase C: Synthesize

**19. Write the answer first.** Three sentences: what we learned, what it means for the hypothesis, and what we still do not know.

**20. Findings by research question,** each with its claims, grades, method, and the effect on the hypothesis (supports, weakens, no effect) with strength: strong (grade A and corroborated or triangulated), medium (grade B or one A), weak (grade C or inferred).

**21. Close the gaps.** For each open item name the next move: an expert interview (`/interview-guide`), a client data request (`/data-request`), a database request, a model run, or park it.

**22. Hand off.** Propose the updates to the hypothesis log, fact base, definitions, and risk register as a list. Apply nothing to `context-library/` yourself.

---

## Common Mistakes

- **Searching before planning**: Twenty random searches produce a pile, not an answer. Write the brief and the research questions first.
- **Questions that do not map to the issue tree**: They overlap or leave a hole. Run the MECE check against the branch.
- **Researching everything**: Rank by impact and cut. Seven questions answered well beat fifteen skimmed.
- **Planning on web search alone**: Prices, share data, and internal figures sit behind databases, experts, or the client. Flag them in the plan and request access early.
- **Averaging two numbers that disagree**: Find why they differ. Do not blend them.
- **Skipping the halfway check-in**: Find out at 50% of the budget that the research is off target, not at 100%.
- **Leaving definitions loose**: Lock the terms first or the numbers will not compare.
- **Taking non-public information on a listed company**: Stop and ask compliance.
- **Putting client details in a query**: Search the market, never the client. Check every query.
- **Trusting the snippet**: Open the page. Snippets drop the period, the unit, and the caveat.
- **Treating a vendor claim as a fact**: A press release saying "40% savings" is a claim from an interested party. Grade it C.
- **One source for a number that drives the answer**: Find a second independent source or flag it.
- **Mixing definitions**: Two "market size" figures often differ in scope or year. Compare the definitions before the numbers.
- **Stale facts stated as current**: Date every current-state claim.
- **Researching what the client already told us**: Read the ingest digests first.
- **Never stopping**: Use the stop rule. Report the open items instead of searching forever.

---

## Structured Output Template

```markdown
# Research Plan: [Topic], [date]

## So what
[Question, decision it feeds, and what would change our mind]

## Research brief
**Decision:** [ ] **User:** [ ] **Format:** [ ] **Due:** [ ] **Depth and time box:** [ ]
**Midpoint check-in:** [date, who]

## Definitions (locked)
| Term | Scope | Period | Geography | Unit | Confirmed by |
|---|---|---|---|---|---|

## Research questions (from issue tree branch [ID])
| ID | Leaf | Research question | Hypothesis tested | Result that would weaken it | Impact | Gap | Reach | Rank |
|---|---|---|---|---|---|---|---|---|
| R1 | | | H1 | | H | H | M | 1 |

**MECE check:** [Overlaps: none / list. Gaps: none / list. Leaves left out and why.]
**Parked or cut:** [Questions and why]

## Source and method plan
| ID | Sources in order (reach: have / ask / no) | Method (two routes) | Queries | Date window |
|---|---|---|---|---|
| R1 | 1 client data (have); 3 Capital IQ (ask); 4 10-K (have) | Top-down and bottom-up | | |

## Questions the web cannot answer alone
| ID | What we need | How | Owner | Needed by |
|---|---|---|---|---|

## Budget and stop rule
[Searches, fetches, expert calls, time box, stop rule, triangulation tolerance (assumption)]

## Confidentiality and compliance check
[Terms kept out of queries. Web tools approved: yes/no. Listed companies involved: yes/no, MNPI rule noted. Expert network rules confirmed: yes/no/not needed.]

## Decision needed
[Approve / edit / cut]
```

```markdown
# Research: [Topic], [date]

## So what
[Three sentences: what we learned, effect on the hypothesis, what is still open]

## Midpoint note (sent [date])
[What we found, what changed, what we cut or added, the steer received]

## Findings
### R1: [Research question]
**Effect on H1:** [supports / weakens / no effect], [strong / medium / weak]
| Claim | Number, unit, period | Source ID and location | Status |
|---|---|---|---|
| | | S1, p. | sourced |

## Triangulation
| Number | Route 1 | Route 2 | Gap % | Within tolerance | Reason for gap |
|---|---|---|---|---|---|

## Conflicts
[Both values, likely reason, who should rule]

## Still open
| Item | Next move | Owner |
|---|---|---|

## Proposed updates
[Hypothesis log, fact base, definitions, risk register: exact text, evidence, confidence]

## Source log
| ID | URL or reference | Publisher | Date published | Date accessed | Type | Grade |
|---|---|---|---|---|---|---|
| S1 | | | | | | A |

## Unreachable
[Pages that were blocked or paywalled, and what we needed from them]
```

---

## Output Integration

### Where to Save

- Plan: `outputs/research-synthesis/research-plan-[topic]-[date].md`
- Findings and source log: `outputs/research-synthesis/research-[topic]-[date].md`
- Claude writes nothing to `context-library/`. The proposed updates stay in `outputs/` until you move them.

### Cross-Skill Integration

**Feeds into:**
- `/competitive-landscape`, `/market-sizing`, `/benchmark-analysis` - Sourced inputs
- `/hypothesis-draft` - Evidence for and against
- `/fact-base` - External numbers with grades
- `/interview-guide` - Questions the web could not answer
- `/data-request` - Client data the research showed we need
- `/risk-register` - Risks the research surfaced
- `/decision-doc` - Agreed definitions

**Pulls from:**
- `/issue-tree` - The branch and leaves the questions map to
- `/prioritize-analyses` - Ranking when many questions compete
- `/hypothesis-draft` - What needs outside evidence
- `/ingest-materials` - What the client already told us
- `/fact-base` - Numbers already agreed

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Research brief** names the decision, user, format, due date, and check-in
- [ ] **Definitions** are locked and confirmed
- [ ] **Research questions** map to issue-tree leaves, and the MECE check is shown
- [ ] **Questions are ranked** by impact, gap, and reach, with cuts listed
- [ ] **Plan approved** before any search ran
- [ ] **Every research question** ties to a hypothesis and a decision
- [ ] **Sources beyond the web** are planned, with reach marked have, ask, or no
- [ ] **Questions the web cannot answer** each have a request and an owner
- [ ] **Two methods** planned for every estimated number
- [ ] **Compliance check** done: listed companies, MNPI, expert network rules
- [ ] **Midpoint check-in** sent and the steer recorded
- [ ] **No client identifiers** appear in any query
- [ ] **Every source** is in the log with URL, date published, date accessed, and a grade
- [ ] **Every number** has a unit, a period, and a source location
- [ ] **Numbers that drive the answer** have two independent sources or two methods, or are flagged single-source
- [ ] **Triangulation gaps** above tolerance are explained, not averaged
- [ ] **Current-state claims** carry a date
- [ ] **Conflicts** are shown with both values
- [ ] **Blocked pages** are logged as unreachable, not worked around
- [ ] **Open items** each have a next move
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every claim has a source or is marked inferred or unverified
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/research-synthesis/`

---

## Related Skills

- `competitive-landscape` - Map competitors once the facts are in
- `market-sizing` - Size the market from sourced inputs
- `benchmark-analysis` - Compare to peers
- `hypothesis-draft` - Update the hypothesis log
- `ingest-materials` - Digest what the client gave us
- `issue-tree` - Source of the research questions
- `prioritize-analyses` - Rank and cut when questions pile up
- `decision-doc` - Log agreed definitions
- `interview-guide` - Cover what the web cannot
- `data-request` - Ask the client for what only they hold
- `fact-base` - Agree one number per metric
