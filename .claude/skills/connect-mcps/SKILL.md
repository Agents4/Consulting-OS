---
name: connect-mcps
description: Connect data and collaboration tools via MCP (drive, slides, spreadsheets, calendar, chat) and log permissions.
disable-model-invocation: false
user-invocable: true
---

# Connect MCPs

## Quick Start

```
/connect-mcps
```
Then provide:
1. **Tools used on the engagement**
2. **Client IT rules**
3. **Data sensitivity**

I will list the tools worth connecting, the permissions needed, the security considerations, and a log of what is connected.

**Output:** Saved to `outputs/mcp-integration-logs/mcp-[tool]-[date].md`
**Time:** ~15 min

**When to use:** At setup and when a new tool is needed

**Phase:** Mobilize  |  **Framework source:** `context-library/engagement-model/08-support-functions-and-tools.md`; `sub-agents/risk-compliance-advisor.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Compliance | `sub-agents/risk-compliance-advisor.md` | confidential, NDA | Rules for client data |
| Tools | `context-library/engagement-model/08-support-functions-and-tools.md` | tool, platform | Standard stack |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If data rules -> Link to `risk-compliance-advisor (sub-agent)`
- If setup -> Link to `data-request`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `sub-agents/risk-compliance-advisor.md`: Rules for client data
- `context-library/engagement-model/08-support-functions-and-tools.md`: Standard stack

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Tools:** [Standard stack]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Client IT policy

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Policy
**"Does the client allow AI tools and external connectors on their data?"**

If not, work only on approved platforms.

---

## The Process

### Step 1: List candidate tools



### Step 2: Check client policy



### Step 3: Connect with least privilege



### Step 4: Test read and write



### Step 5: Log



---

## Structured Output Template

```markdown
# MCP Integration Log

| Tool | Purpose | Permissions | Approved by | Date | Notes |
|---|---|---|---|---|---|
```

---

## Output Format Options

Check **Preferred output formats** in `context-library/engagement-info-template.md`. Default is Office files (xlsx, pptx). If it is blank, ask once and record the answer. Full guide: `advanced/google-workspace-option.md`.

Google connectors worth enabling when the client allows it: Drive (create, convert, copy, share, read), Sheets editor (in-place model and tracker builds), Slides editor (in-place deck builds), Docs editor (memos). Without the editors, Drive can create and convert files but not edit them in place. Confirm client approval first and log each connection.

---

## Output Integration

### Where to Save

- Working draft: `outputs/mcp-integration-logs/mcp-[tool]-[date].md`
- When finalized and agreed with the EM or client: copy to `setup/mcp-log.md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/data-request` - Access

**Pulls from:**
- `/kickoff-plan` - Logistics

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Client approval** for any connector touching client data
- [ ] **Least privilege**
- [ ] **Log** updated
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `data-request` - Data
- `kickoff-plan` - Logistics
