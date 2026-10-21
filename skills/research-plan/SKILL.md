---
name: research-plan
description: "Plan and run web research tied to a hypothesis: research questions, source map, search plan, a logged and graded source trail, and a synthesis that updates the hypotheses."
---

# Research Plan

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.

> Web research: search with the `google_web_search` tool and read pages with the `web_fetch` tool. Wherever this skill says web search, WebSearch, or WebFetch, use those two tools. If `web_fetch` cannot load a page, log it as unreachable and ask the user for the file. Do not work around it.


## Quick Start

```
/research-plan
```
Then provide:
1. **The question or hypothesis** the research must help answer (or let me pull it from the hypothesis log)
2. **The decision or slide it feeds**
3. **Time box and depth**: quick (about 10 searches), standard (about 25), or deep (50 or more)

I will turn the question into a short list of research questions, map the best sources for each, and show you the plan before I search. After you approve it, I run the searches, log every source with a grade, and write a synthesis that says what moved and what is still open.

**Output:** Plan saved to `outputs/research-synthesis/research-plan-[topic]-[date].md`. Findings and source log saved to `outputs/research-synthesis/research-[topic]-[date].md`.
**Time:** ~10 min to plan, plus ~30 min to run a standard pass

**When to use:** Before `/competitive-landscape`, `/market-sizing`, or `/benchmark-analysis` when the question is open; whenever a hypothesis needs outside evidence; when the sponsor asks "what do we know about X?"

**Phase:** Diagnose  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/frameworks/hypothesis-driven-approach.md`; `~/.gemini/extensions/consulting-os/context-library/engagement-model/04-tasks-by-phase.md` (research and fact finding)

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md`, `context-library/engagement-info-template.md` | key question, scope, approved platforms, confidentiality, AI policy | The question, the scope limits, and whether web tools may be used on this engagement |
| Hypotheses | `context-library/hypotheses/*.md`, `outputs/hypotheses/*.md` | H1, confidence, test | The hypotheses the research must test, and what evidence is still missing |
| Research | `context-library/research/*.md`, `outputs/research-synthesis/*.md` | topic, competitor, market, source | Work already done, and sources already logged |
| Ingest Digests | `outputs/research-synthesis/ingest-*/digest-*.md` | topic, claim | What the client already told us, so we do not research it again |
| Fact Base | `context-library/data/fact-base-*.md`, `outputs/analyses/fact-base-*.md` | metric | Numbers already agreed, which the research may check but not replace |
| Interviews | `context-library/interviews/*.md` | expert, quote | Views to corroborate or contradict |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
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
- `context-library/engagements/*.md`: Confidentiality and AI policy

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**Question:** [The question or hypothesis]

**Already known:** [Findings and sources on file, with dates]

**Client's own view:** [What their documents claim, labeled as claims]

### Gaps in Knowledge

I will list what is missing before I plan, for example:
- Whether web tools are approved for this engagement
- What the search may and may not mention (client names, deal names, internal numbers)
- Which findings are stale and need a refresh

If the gaps are material, I ask for them first. If they are minor, I proceed with clearly marked assumptions.

---

## Step 1: Diagnostic Questions

### Question 1: The decision
**"What decision or slide does this research feed, and what would change your mind?"**

Research with no decision behind it becomes a reading list. Name the hypothesis and the result that would weaken it.

### Question 2: The confidentiality line
**"Is there anything I must keep out of search queries?"**

Default: no client name, no project code name, no internal figures, no names of people we interviewed. Search on the market, the competitor set, or the metric, never on the client's situation.

### Question 3: Depth and stop rule
**"Quick, standard, or deep? And when do we stop?"**

Default stop rule: stop a research question when two independent sources of grade A or B agree, or when the time box ends. Report what is still open.

---

## The Process

### Phase A: Plan (show it, get approval, then search)

**1. Turn the question into research questions.** Five to seven at most. Each one is specific and answerable: "What share of [segment] bookings went through [channel] in the last two full years?" beats "Understand the channel landscape." For each, write the hypothesis it tests and the result that would weaken it.

**2. Map the sources.** For each research question, list the best source types in order, and why:
- **Grade A, primary:** regulator filings, annual reports and 10-Ks, statistical agencies, company investor decks, court records, standards bodies, official price lists
- **Grade B, reputable secondary:** industry associations, major business press, peer-reviewed research, analyst summaries with stated method
- **Grade C, weak:** vendor blogs, press releases without data, unsourced listicles, opinion, forums. Use only to find a lead, never as the proof of a number.

**3. Draft the search plan.** For each question: three to five queries, the sites or publishers to favor, and the date window. Prefer primary sources and add the year to queries about current facts.

**4. Set the budget.** Searches and page fetches allowed, time box, and the stop rule.

**5. Run the confidentiality check.** Read every draft query. Remove client identifiers. If web tools are not approved for this engagement, stop and say so.

**6. Show the plan** as the table below and ask for approval or edits before running anything.

### Phase B: Run

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

### Phase C: Synthesize

**13. Write the answer first.** Three sentences: what we learned, what it means for the hypothesis, and what we still do not know.

**14. Findings by research question,** each with its claims, grades, and the effect on the hypothesis (supports, weakens, no effect) with strength: strong (grade A, corroborated), medium (grade B or one A), weak (grade C or inferred).

**15. Close the gaps.** For each open item name the next move: an expert interview (`/interview-guide`), a client data request (`/data-request`), a model run, or park it.

**16. Hand off.** Propose the updates to the hypothesis log, fact base, and risk register as a list. Apply nothing to `context-library/` yourself.

---

## Common Mistakes

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

## Structured Output Template

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

## Output Integration

### Where to Save

- Plan: `outputs/research-synthesis/research-plan-[topic]-[date].md`
- Findings and source log: `outputs/research-synthesis/research-[topic]-[date].md`
- Gemini writes nothing to `context-library/`. The proposed updates stay in `outputs/` until you move them.

### Cross-Skill Integration

**Feeds into:**
- `/competitive-landscape`, `/market-sizing`, `/benchmark-analysis` - Sourced inputs
- `/hypothesis-draft` - Evidence for and against
- `/fact-base` - External numbers with grades
- `/interview-guide` - Questions the web could not answer
- `/data-request` - Client data the research showed we need
- `/risk-register` - Risks the research surfaced

**Pulls from:**
- `/hypothesis-draft` - What needs outside evidence
- `/ingest-materials` - What the client already told us
- `/fact-base` - Numbers already agreed

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

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
- [ ] **Saved** to `outputs/research-synthesis/`

---

## Related Skills

- `competitive-landscape` - Map competitors once the facts are in
- `market-sizing` - Size the market from sourced inputs
- `benchmark-analysis` - Compare to peers
- `hypothesis-draft` - Update the hypothesis log
- `ingest-materials` - Digest what the client gave us
- `interview-guide` - Cover what the web cannot
- `data-request` - Ask the client for what only they hold
- `fact-base` - Agree one number per metric
