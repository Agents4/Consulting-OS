# The Strategy Engagement Model: Overview

**Purpose:** Reference model of how a McKinsey, BCG, or Bain style strategy engagement actually runs. Every skill, sub-agent, and template in Consulting-OS is built on this model. Claude reads these files before it plans, drafts, or reviews anything.

**Compiled:** October 2026, from public firm material, practitioner guides, and press coverage (see `sources.md`). Firms do not publish their internal playbooks. Where sources agree, this file states the practice as typical. Where they conflict or the claim is anecdotal, the file says so. Replace any default here with your firm's or client's real standard in `context-library/engagement-info-template.md`.

---

## The Engagement on a Page

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

## Title Map (the three firms side by side)

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

## How This Folder Is Organized

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

## What Consulting-OS Does With This Model

Consulting-OS gives Claude a seat on the team. You tell it which seat you hold (or which seat you want it to play), and it:

- Works the **analyst seat**: pulls data, builds exhibits, drafts model tabs, formats slides, cleans notes.
- Works the **consultant seat**: structures a workstream, drafts the analysis plan, synthesizes interviews, writes the first storyline.
- Plays the **reviewer seats** through sub-agents: engagement manager, partner, client sponsor, CFO, skeptic, model auditor.
- Keeps the **rhythm**: daily plans, check-ins, weekly SteerCo prep, status updates.

You stay accountable for the answer. See `09-ai-in-consulting-2026.md` for the verification rules.
