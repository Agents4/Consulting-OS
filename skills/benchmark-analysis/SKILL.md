---
name: benchmark-analysis
description: "Compare the client to peers on selected metrics, normalize for comparability, and size the gap."
---

# Benchmark Analysis

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.

> Web research: search with the `google_web_search` tool and read pages with the `web_fetch` tool. Wherever this skill says web search, WebSearch, or WebFetch, use those two tools. If `web_fetch` cannot load a page, log it as unreachable and ask the user for the file. Do not work around it.


## Quick Start

```
/benchmark-analysis
```
Then provide:
1. **The metrics** to benchmark
2. **Peer set** and why they are comparable
3. **Client data** for the same metrics and period

I will normalize definitions, build the peer comparison, size the gap to median and top quartile, and caveat comparability.

**Output:** Saved to `outputs/analyses/benchmark-[topic]-[date].md`
**Time:** ~30 min

**When to use:** Diagnose phase; sizing improvement potential; supporting a target

**Phase:** Diagnose  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/frameworks/strategy-frameworks-cheatsheet.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Research | `context-library/research/*.md` | peer, benchmark, quartile, margin | Peer data with date and source |
| Client Data | `context-library/data/*.md` | KPI, cost, margin | Client values and definitions |
| Competitors | `context-library/research/competitive-*.md` | peer, competitor | Peer set rationale |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If the question is still open and needs sourced web research -> Link to `research-plan`
- If gap needs sizing -> Link to `initiative-sizing`
- If peers are unclear -> Link to `competitive-landscape`
- If gap needs cause -> Link to `root-cause-analysis`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/research/*.md`: Peer data with date and source
- `context-library/data/*.md`: Client values and definitions
- `context-library/research/competitive-*.md`: Peer set rationale

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Research:** [Peer data]

**From Client Data:** [Client metric values]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Definition differences
- Peer data dates
- Size or mix differences

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Peer Set
**"Which peers would the sponsor accept as fair comparison?"**

A benchmark the sponsor rejects will not drive action.

### Question 2: The Definition
**"How does each source define the metric?"**

Mismatched definitions are the main benchmarking error.

---

## The Process

### Step 1: Choose metrics and peers

Limit to metrics that connect to the key question.

### Step 2: Normalize

Align period, currency, scope, and definition; log adjustments.

### Step 3: Compare

Median, quartiles, best-in-class; show client position.

### Step 4: Size the gap

Gap x client base = value if closed; show a haircut.

### Step 5: Caveat

What the benchmark cannot tell us; what would a skeptic say.

---

## Structured Output Template

```markdown
# Benchmark: [Topic]

## So-What
[Client is X vs median; closing half the gap is worth $Y]

## Peer Set and Rationale
| Peer | Why included | Source | Year |
|---|---|---|---|

## Normalization Log
| Adjustment | Reason | Effect |
|---|---|---|

## Comparison
| Metric | Client | Median | Top quartile | Gap | Value of gap |
|---|---|---|---|---|---|

## Caveats
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/analyses/benchmark-[topic]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/research/benchmark-[topic].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/initiative-sizing` - Gap to size
- `/slide-draft` - Chart
- `/hypothesis-draft` - Evidence

**Pulls from:**
- `/competitive-landscape` - Peer set
- `/data-request` - Client data

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Definitions** are aligned
- [ ] **Adjustments** are logged
- [ ] **Sources and years** are cited
- [ ] **Gap value** has a haircut
- [ ] **Caveats** are stated
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `initiative-sizing` - Convert gap to value
- `root-cause-analysis` - Explain the gap
- `slide-draft` - Make the chart
