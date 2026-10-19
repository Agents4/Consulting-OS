# Installation Guide

Get Consulting OS running in about 15 minutes.

## What You Need
- A computer (macOS, Linux, or Windows with WSL)
- A Claude account (Pro, Max, Team, or Enterprise) or an Anthropic API key
- Python 3 with `openpyxl` and `pandas` (for building Excel models)
- Node.js with `pptxgenjs` (for building decks), optional
- LibreOffice (to recalculate models and render decks), optional but recommended
- Client approval to use AI tools on client data (see `advanced/confidentiality-and-client-data.md`)

## Step 1: Install Claude Code
```bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version
```

## Step 2: Get the Folder
Place `Consulting-OS/` where you keep working files. Avoid nesting it inside another Claude Code project folder: parent `CLAUDE.md` files load too and their instructions mix with these.

## Step 3: Install Build Tools
```bash
pip install openpyxl pandas
npm install pptxgenjs
# LibreOffice: install from libreoffice.org (macOS: brew install --cask libreoffice)
```

## Step 4: Launch
```bash
cd Consulting-OS
claude
```
Type `init`. Claude reads `CLAUDE.md`.

## Step 5: Check the Skills
Type `/` and confirm skills such as `/problem-statement` and `/model-build` appear.

## Troubleshooting
| Problem | Fix |
|---|---|
| Skills do not appear | Confirm you launched `claude` inside `Consulting-OS/`, and `.claude/skills/` exists |
| Instructions look mixed | A parent folder has its own `CLAUDE.md`. Move this folder to a standalone location |
| Model has formula errors | Recalculate with LibreOffice; see `advanced/excel-and-deck-production-with-claude.md` |
| Cannot connect a tool | Check client IT policy first, then `setup/environment-keys.md` |
