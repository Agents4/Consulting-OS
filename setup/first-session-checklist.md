# First Session Checklist

Verify Consulting OS works and load your real engagement. Time: 30 to 40 minutes.

## Pre-Flight
```bash
pwd                 # should end in Consulting-OS
claude --version
ls CLAUDE.md README.md .claude/skills | head
```

## Step 1: Fill the Core Templates
- [ ] Copy `context-library/engagement-info-template.md` to `context-library/engagements/` and fill it (key question, scope, phase, gates)
- [ ] Fill `context-library/client-stakeholder-template.md` for sponsor and SteerCo
- [ ] Fill `context-library/team-roster-template.md`
- [ ] Fill `context-library/personal-context-consulting-background.md` and `personal-context-working-preferences.md`
- [ ] Pick a writing style (`writing-style-client-exec.md` is the default for client work)

## Step 2: Add Existing Material
- [ ] Put the SOW, RFP, or brief in `context-library/client-materials/`
- [ ] Put any data in `context-library/data/` (only if approved)
- [ ] Put earlier decks, models, and notes in the matching subfolders

## Step 3: Test Three Skills
- [ ] `/problem-statement`: Claude reads your engagement info and drafts the key question
- [ ] `/day-one-answer`: states a first answer with conditions
- [ ] `/kickoff-plan`: produces an agenda and two-week plan

Check that outputs land in `outputs/` and that no em dashes appear.

## Step 4: Test the Model Path
- [ ] Run `/model-spec` on a small question
- [ ] Run `/model-build` and confirm the file recalculates with zero errors and the Cover shows "ALL INTEGRITY CHECKS OK"

## Step 5: Test the Deck Path
- [ ] Run `/storyline` then `/ghost-deck`
- [ ] Open `templates/ghost-deck-starter.pptx` and review the layouts

## Step 6: Review
- [ ] Run `/review-panel` on the ghost deck
- [ ] Add one correction and say "Add a rule so you don't do that again" to test the learning loop

## Done When
You have a problem statement, a Day-1 answer, a kickoff plan, one model with green checks, and one ghost deck reviewed.
