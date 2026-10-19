# Cadence and Handoffs

## The Rhythm

**Principle:** The week is organized around the next client touchpoint (SteerCo, progress review, working session), not around individual tasks. Work backwards from it.

### Daily

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

### Weekly

| Day | Event | Notes |
|---|---|---|
| Monday | Set the week's definition of success; refresh workplan | Define what has to be true by the next SteerCo |
| Mid-week | Partner problem-solving sessions (2+ per week on a typical BCG-style case) | Partner gives input on storyline, challenges hypotheses |
| Weekly (some cases bi-weekly) | Client progress review / SteerCo | Core anchor. Most of the week's work is packaged into its storyline |
| Weekly | Sponsor status page | One page, same format each time |
| Thursday/Friday | Team learning and feedback; admin, expenses, training, recruiting | Traditional model: team on client site Monday-Thursday, home-office Friday. Post-COVID many projects are hybrid |
| Friday | Weekly review and plan | `/weekly-review` then `/weekly-plan` |

**Hours (anecdotal, from practitioner write-ups):** normal weeks run roughly 55-65 hours; weeks right after a deliverable are lighter (~45); weeks before a major board-level presentation run heavier (~75). Treat as indicative.

### Periodic

| Cadence | Event |
|---|---|
| Weekly or bi-weekly | SteerCo (the sponsor group) |
| Monthly | Executive sponsor check-in with partner (if SteerCo is less frequent) |
| At each gate | Gate review (see `03-engagement-lifecycle.md`) |
| Mid-engagement | Team health check and feedback conversation |
| End of engagement | Retro and individual feedback |

**Sponsor communication rhythm:** the project lead sees the team daily; the sponsor may see it every week or every few weeks. Calendar sponsor meetings 2-3 months ahead so cancellations are less likely. Hold the SteerCo weekly, with no exceptions, even if there is little to report, if that is what was agreed.

---

## Meeting Types

| Meeting | Length | Owner | Output | Skill |
|---|---|---|---|---|
| Team check-in / check-out | 15-30 min | EM | Priorities and blockers | `/team-checkin` |
| Problem-solving session (team + partner) | 45-90 min | EM | Decisions on storyline, hypotheses, next analyses | `/meeting-agenda` `/meeting-notes` |
| Client working session | 60-90 min | Consultant or EM | Assumptions confirmed, data agreed | `/meeting-agenda` |
| Workshop | Half day to 2 days | EM | Options, buy-in | `/workshop-design` |
| Interview | 30-60 min | Consultant | Notes with quotes and numbers | `/interview-guide` |
| SteerCo | 60-90 min | Partner | Decisions and next-step mandate | `/steerco-prep` |
| Retro | 60 min | EM | Lessons | `/engagement-retro` |

### Pre-Read and Pre-Wire Rules
- Share the executive summary with the client counterpart **2-3 days before** the SteerCo. Never surprise them.
- Preview the final recommendation with the sponsor early to build buy-in.
- Red-team the meeting: list the five to ten most likely questions and test answers.
- Give the client project lead a prominent role, ideally presenting to their own boss.
- Plan 15-20 minutes of content for a sponsor update and expect to get about half the time. Open with the executive summary, then spend the meeting on decisions, not recap.
- One-page status standard: overall health in one sentence; progress against last period's three commitments; three commitments for next period; decisions needed with dates; risks named before they surface.

---

## The Review Ladder

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

## Handoff Contracts

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

### Handoff Failure Modes
- **Backup missing:** The page lands without a source. Reviewer cannot check. Rework follows.
- **No so-what:** Data dump. The reviewer has to do the thinking.
- **Silent redirection:** The EM changes the question but not the brief. The analyst builds the wrong thing.
- **Late flag:** Data problem found at the review stage, not at the cleaning stage.
- **Version drift:** Two people edit different copies of the model or deck. Fix: one deck owner and one model owner.

---

## Escalation Paths

| Situation | First stop | Then |
|---|---|---|
| Data not delivered | Client counterpart | Sponsor via EM |
| Scope creep | EM | Partner and sponsor, using change-control clause |
| Team disagreement on recommendation | EM | Most senior person decides |
| Quality concern on a page | Reviewer | EM |
| Client conflict or political issue | EM | Partner, immediately |
| Confidentiality incident (wrong file sent, client data in wrong tool) | EM | Partner and firm risk, same day |
