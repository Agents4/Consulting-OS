# Consulting Operating System

An AI copilot for strategy engagements run the way McKinsey, BCG, and Bain run them. Built for Claude Code. Same architecture as PM OS, rebuilt around the consulting engagement: roles, phases, cadence, handoffs, hypotheses, models, and decks.

## Philosophy

- **Context over prompting.** The engagement's question, hypotheses, stakeholders, data, and past decisions live in `context-library/`, so every output sounds like it came from someone on the team.
- **Workflows, not chat.** 54 slash commands cover the engagement from proposal to handover. Each one builds on the others and routes through the same files.
- **Answer first, then test it.** Day-1 answer, hypothesis log, ghost deck. Work is organized to prove or kill the answer, not to explore everything.
- **Numbers tie.** Model checks, tie-out logs, independent audit. A page does not leave the team until every number traces to a source.
- **You are the owner.** Claude works in the analyst seat: drafts, tests, flags. The consultant, EM, and partner own the recommendation.

## What You Get

- **Engagement model library** (`context-library/engagement-model/`): roles and team structure, skills by role, lifecycle and gates, tasks by phase, cadence and handoffs, deck and Excel production, support functions and tools, AI in consulting, glossary, sources.
- **Framework library** (`context-library/frameworks/`): Pyramid Principle and SCQA, issue trees and MECE, hypothesis-driven approach, 7-step problem solving, prioritization, value-driver trees, market sizing, strategy cheatsheet, interviewing, change, storylines.
- **54 skills** across mobilize, structure, diagnose, model, develop, deck, governance, and close.
- **10 reviewer sub-agents:** partner, engagement manager, skeptic, client sponsor, client CFO, model auditor, data scientist, risk and compliance, implementation lead, production QC.
- **17 templates**, including `model-starter-template.xlsx` and `ghost-deck-starter.pptx`.
- **A worked example** (`context-library/example-engagements/project-northstar-worked-example.md`) for format reference only. It is fictional.

## Quick Start

### 1. Install Claude Code
```bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version
```

### 2. Open this folder
```bash
cd Consulting-OS
claude
```

### 3. Initialize
```
init
```
Claude reads `CLAUDE.md` and learns how to work with you.

### 4. First moves
```
/problem-statement   # Turn the brief into a signable key question
/day-one-answer      # State the best current answer
/kickoff-plan        # Plan the first two weeks
```

## Directory Structure

```
Consulting-OS/
├── CLAUDE.md                  # Master instructions
├── README.md
├── .claude/skills/            # 54 slash-command skills
├── sub-agents/                # 10 reviewer personas
├── templates/                 # Working templates (md, xlsx, pptx)
├── context-library/
│   ├── engagement-info-template.md
│   ├── client-stakeholder-template.md
│   ├── team-roster-template.md
│   ├── writing-style-*.md     # client exec, internal, technical, proposal
│   ├── personal-context-*.md
│   ├── consulting-os-learning-log.md
│   ├── engagement-model/      # How engagements run (the research)
│   ├── frameworks/            # Problem-solving and strategy frameworks
│   ├── example-engagements/   # Fictional worked example
│   └── engagements/ hypotheses/ interviews/ models/ decks/
│       decisions/ meetings/ research/ data/ client-materials/
│       stakeholders/ other/    # Your files (empty at start)
├── outputs/                   # Everything Claude writes
├── setup/                     # Installation and first-session checklist
└── advanced/                  # Context, plan mode, parallel agents, prompt testing, custom agents
```

## Skills by Phase

| Phase | Skills |
|---|---|
| Pursuit and mobilize | `/proposal-draft` `/problem-statement` `/kickoff-plan` `/stakeholder-map` `/workplan-build` `/data-request` `/connect-mcps` |
| Structure | `/day-one-answer` `/issue-tree` `/hypothesis-draft` `/prioritize-analyses` |
| Diagnose | `/interview-guide` `/interview-synthesis` `/survey-design` `/fact-base` `/data-exploration` `/market-sizing` `/benchmark-analysis` `/competitive-landscape` `/value-driver-tree` `/root-cause-analysis` |
| Model | `/initiative-sizing` `/model-spec` `/model-build` `/model-audit` `/scenario-sensitivity` `/number-tie-out` |
| Develop and recommend | `/options-evaluation` `/recommendation` `/roadmap-build` `/change-plan` |
| Storyline and deck | `/storyline` `/ghost-deck` `/slide-draft` `/exec-summary` `/deck-qc` `/final-readout` |
| Rhythm and governance | `/daily-plan` `/weekly-plan` `/weekly-review` `/status-update` `/steerco-prep` `/partner-session-prep` `/handoff-brief` `/meeting-agenda` `/meeting-notes` `/decision-doc` `/risk-register` `/client-update-email` `/engagement-health-check` `/review-panel` |
| Close | `/handover-pack` `/retrospective` `/knowledge-capture` |

## How It Maps to PM OS

| PM OS | Consulting OS |
|---|---|
| Business info | Engagement info |
| Stakeholder template | Client stakeholder template and team roster |
| `strategy/` frameworks | `frameworks/` and `engagement-model/` |
| PRD lifecycle | Engagement spine: problem statement → hypotheses → analyses → model → storyline → deck → readout |
| Engineer / designer / exec reviewers | Partner / EM / sponsor / CFO / model auditor / QC reviewers |
| `outputs/prds/` | `outputs/models/`, `outputs/decks/`, `outputs/hypotheses/` |

## Rules That Do Not Bend

1. Claude writes to `outputs/`. You move finished work into `context-library/`.
2. Client data stays on approved platforms. Confirm client IT policy before connecting tools.
3. Every number ties. Every model is independently reviewed.
4. No em dashes. No delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge.

## About the Research

The model is built from public sources: firm career and insight pages, consulting-prep material, practitioner writing, and published modeling standards. Public information on how firms work is partial and often anecdotal. `context-library/engagement-model/sources.md` rates each source and lists known gaps. Treat it as a strong default, then adjust to your firm's practice. Nothing here is proprietary to McKinsey, BCG, or Bain.

## Next Steps

1. Read `setup/installation-guide.md` and run `setup/first-session-checklist.md`.
2. Read `context-library/engagement-model/00-overview.md`.
3. Fill in the three template files, then run `/problem-statement`.
