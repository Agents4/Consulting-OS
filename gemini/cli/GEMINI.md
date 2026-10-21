# Consulting OS: [CLIENT]

@../../00_Core/Consulting-OS/CLAUDE.md

## Gemini and folder mapping (these rules override the imported file)

This folder is one client workspace inside a Google Drive tree. Read the imported file as the Consulting OS rules, with these changes:

- Where it says Claude, read Gemini.
- `context-library/engagements/`, `stakeholders/`, `hypotheses/`, `interviews/`, `decisions/`, `meetings/`, `data/`, `models/`, `decks/`, `research/`, `client-materials/` map to the files in `./00_Context/` and `./02_Data/` in this folder.
- `context-library/frameworks/`, `engagement-model/` and `writing-style-*.md` map to `../../00_Core/Consulting-OS/context-library/`.
- `templates/` maps to `../../00_Core/Consulting-OS/templates/`.
- `outputs/` maps to `./01_Outputs/`. Write all new files there, in the matching subfolder. Never edit `./00_Context/` or `../../00_Core/` unless the user approves the exact change.
- Skills are model-activated, not slash commands. When the user types `/issue-tree` or "run the issue-tree skill", activate the skill with that name.
- Output formats: follow Preferred output formats in `./00_Context/01 Engagement-Brief`. When the format is Google Docs, Sheets or Slides, follow the Google section of the imported file and `../../00_Core/Consulting-OS/advanced/google-workspace-option.md`.
- Client data stays in this folder tree on the approved account.
