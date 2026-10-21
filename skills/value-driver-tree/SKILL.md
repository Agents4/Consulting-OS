---
name: value-driver-tree
description: "Build a quantified driver tree (revenue, cost, margin, cash) linking operational levers to financial outcomes."
---

# Value Driver Tree

> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `~/.gemini/extensions/consulting-os/`. Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.


## Quick Start

```
/value-driver-tree
```
Then provide:
1. **The financial outcome** (EBITDA, margin, NPV, cash)
2. **Baseline data**
3. **Candidate levers**

I will build the driver tree to measurable leaves, attach baseline values, and mark which drivers are controllable and which carry the most value.

**Output:** Saved to `outputs/analyses/value-driver-tree-[topic]-[date].md`
**Time:** ~30 min

**When to use:** Sizing improvement, linking operations to the P&L, setting targets

**Phase:** Diagnose and Develop  |  **Framework source:** `~/.gemini/extensions/consulting-os/context-library/frameworks/value-driver-trees.md`

## Context Routing Logic (Internal - for Gemini)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Client Data | `context-library/data/*.md` | P&L, volume, price, cost | Baseline values |
| Issue Trees | `outputs/issue-trees/*.md` | branch, profit | Alignment with the question |
| Frameworks | `~/.gemini/extensions/consulting-os/context-library/frameworks/value-driver-trees.md` | driver, lever, flow-through | Tree patterns |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`~/.gemini/extensions/consulting-os/context-library/frameworks/`, `~/.gemini/extensions/consulting-os/context-library/engagement-model/`)

**Cross-Skill Links:**
- If levers need sizing -> Link to `initiative-sizing`
- If model needed -> Link to `model-spec`
- If benchmark values -> Link to `benchmark-analysis`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/data/*.md`: Baseline values
- `outputs/issue-trees/*.md`: Alignment with the question
- `~/.gemini/extensions/consulting-os/context-library/frameworks/value-driver-trees.md`: Tree patterns

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Client Data:** [Baseline P&L and KPIs]

**From Issue Trees:** [Relevant branches]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Baseline at leaf level
- Definitions of volume and price

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Outcome
**"Which single financial number must move?"**

All drivers must roll up to it.

---

## The Process

### Step 1: State the outcome

Pick one metric and its baseline.

### Step 2: Decompose

Revenue = volume x price x mix; cost by fixed/variable and by activity.

### Step 3: Attach values

Baseline per leaf; mark source and quality.

### Step 4: Rate each driver

Controllable? Sensitivity? Evidence for a lever?

### Step 5: Rank

Sensitivity x controllability gives the shortlist of levers.

---

## Structured Output Template

```markdown
# Value Driver Tree: [Outcome]

```
[Outcome]
|- Revenue
|   |- Volume x Price x Mix
|- Cost
|   |- Variable / Fixed
```

## Driver Table
| Driver | Baseline | Unit | Source | Controllable? | Sensitivity | Lever idea |
|---|---|---|---|---|---|---|

## Shortlist of Levers
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/analyses/value-driver-tree-[topic]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/research/value-driver-tree-[topic].md`
- Gemini never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/initiative-sizing` - Levers to size
- `/model-spec` - Model structure
- `/slide-draft` - Tree graphic

**Pulls from:**
- `/issue-tree` - Structure
- `/data-exploration` - Baseline

### Handoff Format

When this output goes to a teammate or reviewer, attach a `~/.gemini/extensions/consulting-os/templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Tree rolls up** exactly to the outcome
- [ ] **Baseline** ties to a source
- [ ] **Controllable** vs not is marked
- [ ] **Leaves** are measurable
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `initiative-sizing` - Size levers
- `model-spec` - Plan the model
- `benchmark-analysis` - Target values
