---
name: google-workspace-output
description: "Deliver a model, tracker, or deck as Google Sheets or Google Slides: check connectors, pick the route, build in place, verify, share safely."
disable-model-invocation: false
user-invocable: true
---

# Google Workspace Output

## Quick Start

```
/google-workspace-output
```
Then provide:
1. **What to deliver** (model, tracker, ghost deck, deck, or a conversion of an existing xlsx or pptx)
2. **Where it should live** (shared drive or folder)
3. **Who needs access** (team only, or a client counterpart)

I will check which Google connectors are available, choose the easiest route (CSV upload, copy of the Google starter, or in-place build), build it, verify the result, and set sharing the safe way.

**Output:** Saved to `outputs/mcp-integration-logs/google-output-[item]-[date].md`
**Time:** ~10 min for a tracker; ~30 to 60 min for a model or deck

**When to use:** The engagement uses Google Workspace, or a Google file is easier than building xlsx or pptx with Python

**Phase:** All  |  **Framework source:** `advanced/google-workspace-option.md`; `templates/google-workspace-starters.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Engagement Info | `context-library/engagement-info-template.md` | preferred output formats, approved platforms, confidentiality | Format choice and whether Google is approved for client data |
| Google Option Guide | `advanced/google-workspace-option.md` | tier, route, limits | Tiers, routes, standards |
| Starters | `templates/google-workspace-starters.md` | starter, check list | Conversion checks |
| Models and Decks | `outputs/models/*.md`, `outputs/ghost-decks/*.md`, `outputs/decks/*.md` | spec, ghost page, chart | What to build |
| Compliance | `sub-agents/risk-compliance-advisor.md` | client data, approved tools | Whether client data may go to Google |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If building an xlsx instead -> Link to `model-build`
- If building a pptx instead -> Link to `ghost-deck`
- If connectors missing -> Link to `connect-mcps`
- If client data concerns -> Link to `risk-compliance-advisor (sub-agent)`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/engagement-info-template.md`: Format choice and whether Google is approved for client data
- `advanced/google-workspace-option.md`: Tiers, routes, standards
- `templates/google-workspace-starters.md`: Conversion checks
- `outputs/models/*.md`, `outputs/ghost-decks/*.md`, `outputs/decks/*.md`: What to build
- `sub-agents/risk-compliance-advisor.md`: Whether client data may go to Google

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Engagement Info:** [Preferred formats and approved platforms]

**From Models and Decks:** [Spec or ghost deck to build]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Is Google Workspace approved for this client's data?
- Which Google connectors are enabled in this session (Drive, Sheets, Slides, Docs)?
- Shared drive or folder to hold the files

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Approval
**"Has the client approved Google Workspace for their data, in writing?"**

If not, stop. Use the Office path locally and ask the EM.

### Question 2: The Tier
**"Which Google connectors are enabled here?"**

Drive only means create and convert. Sheets and Slides editors mean in-place builds. If an editor is missing and the file already exists, I ask you to enable it instead of making a copy.

### Question 3: The Audience
**"Who opens the file, and do they need Excel or PowerPoint copies?"**

Decides whether to export .xlsx, .pptx, or PDF at the end.

---

## The Process

### Step 1: Check the format rule

Read Preferred output formats in engagement info. If blank, ask once and record the answer.

### Step 2: Check approval and tools

Confirm client approval for Google. List the connectors available. Pick Tier 1, 2, or 3.

### Step 3: Pick the route

Tracker or log: build a CSV and upload it to create a Google Sheet (Tier 1). Model: copy the Google starter, or create a blank Sheet and write inputs, formulas, and formats with the Sheets editor (Tier 2). Deck: copy the Slides starter and build pages with the Slides editor (Tier 3); charts are built on the Sheet Outputs tab and embedded as linked charts. Without the editor, deliver the spec and ask you to enable the connector.

### Step 4: Build in one pass per step

One write for the data and formulas, one batch for formatting and tabs, one for slides. Parsing follows the Sheets UI: numbers as numbers, years and IDs with a leading apostrophe.

### Step 5: Verify

Read values back. For models: no error values, Checks master flag is 0, Base outputs match the starter. For decks: read text, export a PDF where possible, check overflow, fonts, charts. If layout could not be checked visually, say so.

### Step 6: Share and log

Share with named people only; reader or commenter for the client; never anyone-with-link. Record file name, link, owner, version, access, and approval in `outputs/mcp-integration-logs/`.

---

## Common Mistakes

- **Making a second copy to avoid an edit**: Edits go into the same file. Ask to enable the editor connector instead.
- **Typed results**: Every derived number is a formula, not a pasted result.
- **Skipping the visual check**: Converted decks can change fonts and spacing. Check every page.

---

## Structured Output Template

```markdown
# Google Output Log: [Item]

**Date:** [ ]  |  **Owner:** [ ]  |  **Tier:** [1 / 2 / 3]  |  **Approval for client data:** [Y/N, where recorded]

| File | Type | Link | Route | Version | Shared with | Role |
|---|---|---|---|---|---|---|

## Verification
| Check | Result |
|---|---|
| Error values | |
| Master check | |
| Fonts and layout | |
| Charts linked | |

## Limits Noted
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/mcp-integration-logs/google-output-[item]-[date].md`
- When finalized and agreed with the EM or client: copy to `setup/mcp-log.md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/number-tie-out` - Linked Outputs tab and charts
- `/deck-qc` - Deck to check
- `/handover-pack` - Files to hand over

**Pulls from:**
- `/model-spec` - What to build
- `/ghost-deck` - Pages to build
- `/connect-mcps` - Connectors

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Client approval** for Google confirmed and recorded
- [ ] **Edits** went into the existing file, not a copy
- [ ] **Every derived number** is a formula
- [ ] **Values read back** with no error cells
- [ ] **Sharing** is to named people only
- [ ] **Log** saved
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `model-build` - Excel route
- `ghost-deck` - Deck spec
- `connect-mcps` - Enable connectors
