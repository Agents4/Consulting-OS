---
name: ingest-materials
description: "Ingest new client materials and data: digest each file, find conflicts, and propose approved updates to the fact base, hypotheses, stakeholders, decisions, and risks."
---

# Ingest Materials

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/ingest-materials
```
Then provide (all optional):
1. **Folders to scan** (default: `context-library/client-materials/` and `context-library/data/`)
2. **Files to prioritize or skip**
3. **Depth**: quick scan (digests only) or deep read (digests plus reconciliation)

I will find new and changed files, read each one in any format, write a one-page digest per file, check what it means for what we already know, and propose exact updates to the fact base, hypotheses, stakeholders, decisions, risks, and data requests. Nothing in `context-library/` changes until you approve each file.

**Output:** Digests and the update proposal in `outputs/research-synthesis/ingest-[date]/`. Running index at `outputs/research-synthesis/ingest-index.md`.
**Time:** ~5 min per document, plus ~15 min for the cross-check and proposal

**When to use:** After you drop files into `client-materials/` or `data/`, after every client data delivery, and before `/fact-base`, `/hypothesis-draft`, or a SteerCo

**Phase:** Mobilize through Recommend, and weekly  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/engagement-model/04-tasks-by-phase.md` (data and document intake); `~/.gemini/extensions/consulting-os/context-library/frameworks/hypothesis-driven-approach.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md`, `context-library/engagement-info-template.md` | key question, scope, approved platforms, confidentiality | The question the files must help answer, and which platforms and tools are approved for client data |
| Ingest Index | `outputs/research-synthesis/ingest-index.md` | file, hash, ingested | What was already ingested, so only new and changed files are read |
| Client Materials | `context-library/client-materials/*` (any format) | n/a | New and changed files |
| Data | `context-library/data/*` (any format; skip `fact-base-*` and `data-profile-*`) | n/a | New and changed files |
| Hypotheses | `context-library/hypotheses/*.md`, `outputs/hypotheses/*.md` | H1, supported, weakened | Hypotheses the new evidence touches |
| Fact Base | `context-library/data/fact-base-*.md`, `outputs/analyses/fact-base-*.md` | baseline, metric | Numbers already agreed |
| Stakeholders | `context-library/stakeholders/*.md`, `context-library/client-stakeholder-template.md` | name, role, stance | People and org facts to update |
| Decisions and Risks | `context-library/decisions/*.md` | definition, risk | Agreed definitions, open risks |
| Data Requests | `outputs/data-requests/*.md`, `context-library/data/data-request-tracker.md` | requested, received | Requests this file closes or opens |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If numbers conflict across files -> Link to `fact-base`
- If a file is a large dataset -> Link to `data-exploration`
- If evidence moves a hypothesis -> Link to `hypothesis-draft`
- If new people or politics appear -> Link to `stakeholder-map`
- If a file satisfies or opens a request -> Link to `data-request`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/research-synthesis/ingest-index.md`: What was already ingested
- `context-library/engagements/*.md`: The question and approved platforms
- `context-library/hypotheses/*.md`: What the evidence has to test
- `context-library/data/fact-base-*.md`: Numbers already agreed

List candidate files with a hash so changed files are caught, not only new ones:

```bash
find context-library/client-materials context-library/data -type f \
  ! -name '.gitkeep' ! -name 'fact-base-*' ! -name 'data-profile-*' \
  -exec sha256sum {} + | sort -k2
```

Compare with the index. A file is **new** if its path is not in the index, **changed** if the hash differs, **unchanged** otherwise.

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**Inventory:** [N new, N changed, N unchanged, N skipped]

**Context:** [Key question, current governing thought, hypotheses open]

### Gaps in Knowledge

I will list what is missing before I read anything, for example:
- Whether each file is cleared for this tool (approved platform)
- Which files matter most this week
- Files I cannot read (scanned, password protected, audio)

If the gaps are material, I ask for them first. If they are minor, I proceed with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: Clearance
**"Is every file in the list cleared to be read here, under the platforms approved in engagement info?"**

Skip anything marked restricted, or that holds personal data (HR, customer names, health), until you confirm. When in doubt, skip and log it.

### Question 2: Priority
**"Which two or three files matter most this week, and which hypothesis or slide do they feed?"**

Read those first and in depth. The rest get a quick scan.

### Question 3: Depth
**"Quick scan (digests only) or deep read (digests plus reconciliation to the fact base)?"**

Default to quick scan above 10 files.

---

## The Process

### Step 1: Inventory and classify

Build one table: file, type (SOW, annual report, board deck, KPI pack, org chart, contract, policy, prior consultant report, data extract, email thread), size, file date, hash, status (new, changed, unchanged, skipped), sensitivity (public, client confidential, restricted), and cleared (yes, no, ask). Show it and confirm before reading.

### Step 2: Read each file in its own format

- **.md, .txt, .csv:** Read directly. For a CSV, read headers and a sample, never print the whole file.
- **.docx, .pptx:** Convert with `markitdown` or `pandoc`. Keep slide numbers and speaker notes.
- **.pdf:** `pdftotext -layout` for text. For scanned pages, render and read them, and mark the figures as lower confidence.
- **.xlsx:** Use `openpyxl` to list sheets, used ranges, headers, and which cells are formulas. Record sheet and cell references. Do not paste tables. Large datasets go to `/data-exploration`.
- **Images and charts:** View them. Read values only where they are printed on the chart.
- **Email exports (.eml, .msg):** Headers, thread order, and the ask.
- **Audio and video:** Ask for a transcript. Do not guess.
- **Google Docs, Sheets, Slides:** Read through the Drive connector only with your approval.
- **Cannot read it:** Log it as unreadable and say why. Never infer contents from the file name.

### Step 3: Write one digest per file

Use the digest template below. Rules: every number carries its unit, period, and location (page, slide, sheet and cell). Quotes are exact and carry a location. Mark what the document **claims** versus what the data **shows**. Record the author and the date.

### Step 4: Cross-check against what we know

For each digest, compare with:
- **Fact base:** agrees, conflicts, or new for each metric.
- **Hypotheses:** supports, weakens, or no effect, with strength (strong: client data, validated; medium: partial data or benchmark; weak: opinion or analogy).
- **Stakeholders:** new names, role changes, stance signals, reporting lines.
- **Decisions:** definitions or approvals the file implies.
- **Risks:** data quality, scope, confidentiality, political.
- **Data requests:** items satisfied, partly satisfied, or newly needed.
- **Other files:** the same metric with different values. Never pick silently. Show both and ask which the sponsor treats as the source of truth.

### Step 5: Write the update proposal

One numbered list, grouped by target file. Each update has an ID (U1, U2), the target file and section, the action (add, change, close), the exact text to paste, the evidence (file and location), a confidence, and a decision box (Approve, Edit, Skip). Lead with a "So what" of the three findings that change the answer or the plan.

### Step 6: Get approval, then apply

Show the proposal and ask which updates to apply. For each approved target:
1. Write the updated copy of the file to `outputs/research-synthesis/ingest-[date]/updates/`, mirroring its path in `context-library/`.
2. Only after you say "apply" for that specific file, save a copy of the original to `outputs/research-synthesis/ingest-[date]/backup/`, then write the update into `context-library/`.

Never apply an update you have not approved, and never delete or overwrite a client file in `client-materials/` or `data/`. If you say "apply all", I still list every file I changed.

### Step 7: Update the index

Append one row per file to `outputs/research-synthesis/ingest-index.md`: path, hash, date ingested, digest path, updates applied. Files you skipped or left unapproved stay marked **pending** so the next run raises them again.

### Step 8: Hand off

Name the next skills the findings call for, for example `/fact-base` for a number conflict, `/hypothesis-draft` for a moved hypothesis, `/stakeholder-map` for new people, `/risk-register` for a new risk, `/decision-doc` for a definition, `/data-request` for a gap.

---

## Common Mistakes

- **Ingesting everything at once**: Set a priority and a depth first. Ten files read well beat fifty skimmed.
- **A digest with no locations**: A fact without a page or cell cannot be tied out later.
- **Picking between conflicting numbers silently**: Show both, ask, and log the decision.
- **Treating a client claim as data**: Label claims. A slide saying "churn is 5%" is a claim until the data shows it.
- **Updating the knowledge base without approval**: Proposals first. Edits only on your explicit approval, file by file.
- **Digesting a big dataset**: Profile it with `/data-exploration`. Digest what it is and where it lives.
- **Reading restricted or personal data**: Ask first. Skip and log when unsure.

---

## Structured Output Template

```markdown
# Digest: [File name]

**Path:** [ ]  |  **Type:** [ ]  |  **Author / source:** [ ]  |  **Date:** [ ]  |  **Sensitivity:** [ ]
**Read in full:** [Y / partial / N]  |  **Hash:** [first 12 characters]

## What it is and why it matters
[2 to 3 sentences. Which question or hypothesis it feeds.]

## Key facts
| ID | Fact | Value | Unit | Period | Location (page / slide / cell) | Claim or data | Confidence |
|---|---|---|---|---|---|---|---|
| F1 | | | | | | | |

## Definitions and terms the client uses
- [Term]: [definition] ([location])

## Quotes worth keeping
- "[Exact quote]" ([location], [who])

## People and organization
- [Name, role, what the document says about them or their stance]

## Checks against what we know
- Fact base: [agrees / conflicts / new, with IDs]
- Hypotheses: [H#: supports / weakens / no effect, strength]
- Other files: [conflicts]

## Open questions
- [ ]
```

```markdown
# Ingest Proposal: [Engagement], [date]

**Files read:** [N]  |  **Skipped:** [N, why]  |  **Pending approval:** [N]

## So what
1. [Finding that changes the answer or the plan]
2. [ ]
3. [ ]

## Conflicts to resolve
| Metric | Source A | Source B | Which does the sponsor treat as correct? |
|---|---|---|---|

## Proposed updates
| ID | Target file and section | Action | Exact text | Evidence (file, location) | Confidence | Decision |
|---|---|---|---|---|---|---|
| U1 | | add / change / close | | | | Approve / Edit / Skip |

## Next skills
- [ ]
```

```markdown
# Ingest Index

| Path | Hash (12) | Ingested | Digest | Updates applied | Status |
|---|---|---|---|---|---|
| | | | | | ingested / pending / skipped / unreadable |
```

---

## Output Integration

### Where to Save

- Digests: `outputs/research-synthesis/ingest-[date]/digest-[file-stem]-[date].md`
- Proposal: `outputs/research-synthesis/ingest-[date]/ingest-proposal-[date].md`
- Draft updates: `outputs/research-synthesis/ingest-[date]/updates/` (mirrors `context-library/` paths)
- Backups of replaced files: `outputs/research-synthesis/ingest-[date]/backup/`
- Index: `outputs/research-synthesis/ingest-index.md` (updated each run)
- Gemini writes to `context-library/` only for an update you approved by name, as in Step 6. Everything else stays in `outputs/`.

### Cross-Skill Integration

**Feeds into:**
- `/fact-base` - New and conflicting numbers
- `/hypothesis-draft` - Evidence for and against
- `/stakeholder-map` - People and stance signals
- `/risk-register` - New risks
- `/decision-doc` - Definitions to agree
- `/data-request` - Requests closed and opened

**Pulls from:**
- `/data-request` - What was asked for
- `/hypothesis-draft` - What the evidence has to test
- `/fact-base` - Numbers already agreed

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Every file** is accounted for: read, skipped with a reason, or unreadable
- [ ] **Clearance** checked before reading each file
- [ ] **Every number** has a unit, a period, and a location
- [ ] **Quotes** are exact and located
- [ ] **Claims and data** are labeled apart
- [ ] **Conflicts** are shown with both values, not resolved silently
- [ ] **Each proposed update** has exact text, evidence, and a decision box
- [ ] **No file in `context-library/`** changed without your approval for that file, and a backup exists for each
- [ ] **Index** updated, with pending files marked
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, with context changes made only as approved

---

## Related Skills

- `fact-base` - Agree one number per metric
- `data-exploration` - Profile large datasets
- `hypothesis-draft` - Update the hypothesis log
- `stakeholder-map` - Update people and stance
- `risk-register` - Log new risks
- `decision-doc` - Log definitions
- `data-request` - Close and open requests
- `interview-synthesis` - Same method for interview notes
