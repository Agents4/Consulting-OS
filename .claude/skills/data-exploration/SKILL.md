---
name: data-exploration
description: Profile and clean client data: completeness, outliers, definitions, reconciliations to reported figures.
disable-model-invocation: false
user-invocable: true
---

# Data Exploration

## Quick Start

```
/data-exploration
```
Then provide:
1. **The data file(s)**
2. **What the data should show** (and a reported figure to reconcile to)
3. **The analysis it feeds**

I will profile each field, flag quality issues, reconcile to a reported total, document cleaning steps, and produce a clean, versioned dataset.

**Output:** Saved to `outputs/analyses/data-profile-[dataset]-[date].md`
**Time:** ~30 min

**When to use:** Every time new client data arrives, before any analysis uses it

**Phase:** Diagnose  |  **Framework source:** `sub-agents/data-scientist.md`; `context-library/engagement-model/07-excel-modeling-standards.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Data | `context-library/data/*.md` | dataset, definition, extract | Dictionary and prior profiles |
| Data Requests | `outputs/data-requests/*.md` | fields, owner | What was asked for and by whom |
| Models | `context-library/models/*.md` | input, tab | Where this data will be used |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If data fails reconciliation -> Link to `data-request`
- If data is ready for modeling -> Link to `model-spec`
- If need a second opinion -> Link to `data-scientist (sub-agent)`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/data/*.md`: Dictionary and prior profiles
- `outputs/data-requests/*.md`: What was asked for and by whom
- `context-library/models/*.md`: Where this data will be used

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Data:** [Known issues]

**From Data Requests:** [Expected fields]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Reported control total
- Field definitions
- Extraction date

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Control Total
**"Which reported number should the data reconcile to?"**

Without a control total, errors are invisible.

---

## The Process

### Step 1: Inventory

Rows, columns, period, keys, date received.

### Step 2: Profile

Missing, duplicates, ranges, outliers per field.

### Step 3: Reconcile

Sum to the reported figure; explain gaps.

### Step 4: Clean

Rules logged one by one; never overwrite raw data.

### Step 5: Document

Data dictionary and a list of open questions for the client.

---

## Structured Output Template

```markdown
# Data Profile: [Dataset]

**Source / owner / date:** [ ]  |  **Rows:** [ ]  |  **Period:** [ ]

## Reconciliation
| Check | Data | Reported | Gap | Explanation |
|---|---|---|---|---|

## Field Profile
| Field | Type | Missing % | Distinct | Min / Max | Issue |
|---|---|---|---|---|---|

## Cleaning Log
| # | Rule | Rows affected | Rationale |
|---|---|---|---|

## Open Questions to Client
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/analyses/data-profile-[dataset]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/data/data-profile-[dataset].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/model-spec` - Clean inputs
- `/root-cause-analysis` - Reliable data
- `/benchmark-analysis` - Client values

**Pulls from:**
- `/data-request` - Source and owner

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Reconciled** to a reported total
- [ ] **Cleaning steps** are logged
- [ ] **Raw file** is untouched
- [ ] **Open questions** go back to the client
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `data-request` - Ask for corrections
- `model-spec` - Plan the model
- `root-cause-analysis` - Find causes
