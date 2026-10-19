# Context Management

Better context gives better outputs, and less rework.

## What Counts as Context
Instructions (`CLAUDE.md`), engagement files, templates, examples, the current conversation, and attached files. Claude can only use what it can see.

## The Engagement Context Stack
1. **Always loaded:** `CLAUDE.md`
2. **Loaded by skills on demand:** engagement info, hypotheses, decisions, stakeholder profiles, frameworks
3. **Pulled when needed:** interviews, data profiles, models, decks

Keep layer 1 short. Put detail in layers 2 and 3.

## Habits That Help
- **One engagement per folder.** Do not mix clients in one workspace.
- **Name files so search works:** `hypothesis-log-northstar-2026-10-16.md`.
- **Update the hypothesis log and decision log after every meeting.** They are the memory of the engagement.
- **Summarize long documents once,** save the summary in `outputs/research-synthesis/`, and cite it.
- **Start a fresh session at each gate** and open with `/status-update` to reload the state.
- **Compact long sessions** and restate the key question and open decisions.

## What Not to Load
Raw client dumps, entire annual reports, or old decks that will not be used. Point to the specific pages.

## Client Data
Follow client policy. Strip identifiers where possible. See `confidentiality-and-client-data.md`.
