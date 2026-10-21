---
name: issue-tree
description: Build a MECE issue tree from the key question, tag branches with hypotheses and analyses.
disable-model-invocation: false
user-invocable: true
---

# Issue Tree

## Quick Start

```
/issue-tree
```
Then provide:
1. **The key question**
2. **Any existing structure or framework** you want to test
3. **Depth needed** (default 3 levels)

I will build a MECE tree, test it for gaps and overlaps, tag each leaf with a hypothesis and analysis, and flag where the answer is most uncertain.

**Output:** Saved to `outputs/issue-trees/issue-tree-[engagement]-[date].md`
**Time:** ~25 min

**When to use:** Right after the problem statement, and when a new branch emerges

**Phase:** Mobilize  |  **Framework source:** Barbara Minto; `context-library/frameworks/issue-trees-mece.md`; `templates/issue-tree-template.md`

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Problem Statement | `outputs/problem-statements/*.md` | key question, scope | Root of the tree |
| Frameworks | `context-library/frameworks/issue-trees-mece.md`, `value-driver-trees.md` | MECE, driver tree, profit | Tree types and tests |
| Interviews | `context-library/interviews/*.md` | cause, driver, issue | Candidate branches from the field |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If profit or value is the question -> Link to `value-driver-tree`
- If branches need prioritizing -> Link to `prioritize-analyses`
- If leaves need hypotheses -> Link to `hypothesis-draft`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `outputs/problem-statements/*.md`: Root of the tree
- `context-library/frameworks/issue-trees-mece.md`, `value-driver-trees.md`: Tree types and tests
- `context-library/interviews/*.md`: Candidate branches from the field

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Problem Statement:** [Key question and scope]

**From Interviews:** [Candidate drivers]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Which tree type fits (diagnostic, solution, driver)
- Level of detail the sponsor expects

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Tree Type
**"Is this a why tree, a how tree, or a driver tree?"**

Mixing types is the commonest MECE failure.

### Question 2: The Cut
**"What is the cleanest first split (customers, products, channels, time, cost vs revenue)?"**

The first split sets all later branches.

---

## The Process

### Step 1: Choose tree type

Diagnostic (why), solution (how), or value-driver.

### Step 2: Draft level 1

Two to five branches. Test: mutually exclusive, collectively exhaustive.

### Step 3: Draft levels 2 and 3

Stop at leaves that can be tested with a specific analysis.

### Step 4: Run the MECE test

Look for overlaps (same item in two branches) and gaps (what is missing).

### Step 5: Tag leaves

For each leaf: hypothesis, analysis, data, owner, confidence.

---

## Structured Output Template

```markdown
# Issue Tree: [Engagement]

**Key question:** [ ]  |  **Tree type:** [Diagnostic / Solution / Driver]

```
Key question
|- 1. [Branch]
|   |- 1.1 [Leaf] - H[ ] - [analysis]
|   |- 1.2 [Leaf]
|- 2. [Branch]
```

## MECE Test
| Check | Result | Fix |
|---|---|---|

## Leaf Tags
| Leaf | Hypothesis | Analysis | Data | Owner | Confidence |
|---|---|---|---|---|---|
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/issue-trees/issue-tree-[engagement]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/hypotheses/issue-tree-[engagement].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/hypothesis-draft` - Branches to hypothesize on
- `/workplan-build` - Modules
- `/prioritize-analyses` - Leaves to rank

**Pulls from:**
- `/problem-statement` - Root question
- `/interview-synthesis` - Field evidence

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Siblings** are mutually exclusive
- [ ] **Branches** together cover the question
- [ ] **No leaf** is untestable
- [ ] **Depth** is consistent across branches
- [ ] **Tree type** is not mixed
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `hypothesis-draft` - Write hypotheses per branch
- `prioritize-analyses` - Rank leaves
- `value-driver-tree` - Quantify drivers
