---
name: competitive-landscape
description: Map competitors, positioning, and moves relevant to the key question, with sources.
disable-model-invocation: false
user-invocable: true
---

# Competitive Landscape

## Quick Start

```
/competitive-landscape
```
Then provide:
1. **The client and market**
2. **Competitors to include** (or let me suggest)
3. **What decision** the landscape informs

I will build a competitor profile set and a positioning map focused on the decision, with evidence and gaps flagged.

**Output:** Saved to `outputs/analyses/competitive-landscape-[market]-[date].md`
**Time:** ~35 min with web research

**When to use:** Diagnose phase; market entry; positioning; pricing

**Phase:** Diagnose  |  **Framework source:** `context-library/frameworks/strategy-frameworks-cheatsheet.md` (Five Forces, positioning)

## Context Routing Logic (Internal - for Claude)

**Automatic Context Checks:**
When this skill is invoked, immediately check:

| Source | Files/Folders | Search Terms | What to Extract |
|--------|---------------|--------------|-----------------|
| Engagement Info | `context-library/engagements/*.md` | key question, scope, client, phase, deadline | The agreed key question, scope, constraints, current phase, gate dates |
| Research | `context-library/research/*.md` | competitor, share, pricing | Existing intelligence |
| Client Materials | `context-library/client-materials/*.md` | strategy, positioning, customers | Client's own view |
| Interviews | `context-library/interviews/*.md` | competitor, switch, win, loss | Customer and expert views |

**Context Priority:**
1. Engagement context FIRST (engagement info, hypotheses, decisions, prior outputs)
2. Client data and connected tools SECOND (data room, MCPs, client materials)
3. Framework guidance LAST (`context-library/frameworks/`, `context-library/engagement-model/`)

**Cross-Skill Links:**
- If numbers needed -> Link to `benchmark-analysis`
- If size of market -> Link to `market-sizing`
- If slide needed -> Link to `slide-draft`

---

## Step 0: Understanding What Already Exists

Before starting, check the engagement folders for existing work so nothing is rebuilt:

- `context-library/research/*.md`: Existing intelligence
- `context-library/client-materials/*.md`: Client's own view
- `context-library/interviews/*.md`: Customer and expert views

**Based on what I find, I will show you:**

### Internal Intelligence Summary

**From Research:** [Known competitors and data]

**From Interviews:** [Why customers choose]

### Gaps in Knowledge

I will list what is missing before I draft anything, for example:
- Private competitor data
- Pricing
- Recent moves

If the gaps are material, I ask for them first. If they are minor, I draft with clearly marked assumptions and carry on.

---

## Step 1: Diagnostic Questions

Instead of a generic intake, I ask only what the files cannot answer:

### Question 1: The Decision
**"What would we do differently if a competitor moved?"**

Scope the landscape to what drives a decision.

### Question 2: The Axes
**"Which two dimensions matter most to customers?"**

They define the positioning map.

---

## The Process

### Step 1: Define the field

Direct, indirect, new entrants, substitutes.

### Step 2: Profile each

Offer, price, scale, strengths, moves, evidence.

### Step 3: Map positioning

Two axes chosen from customer evidence.

### Step 4: Draw implications

Where the client wins, loses, and what moves are likely.

### Step 5: List gaps

What we could not verify and who could.

---

## Structured Output Template

```markdown
# Competitive Landscape: [Market]

## So-What
[Implication for the client]

## Competitor Profiles
| Competitor | Offer | Scale | Price | Strengths | Weaknesses | Recent moves | Source |
|---|---|---|---|---|---|---|---|

## Positioning Map
[Axes and placement]

## Implications
[ ]

## Gaps
[ ]
```

---

## Output Integration

### Where to Save

- Working draft: `outputs/analyses/competitive-landscape-[market]-[date].md`
- When finalized and agreed with the EM or client: copy to `context-library/research/competitive-landscape-[market].md`
- Claude never writes to `context-library/`. The user promotes finished files there by hand.

### Cross-Skill Integration

**Feeds into:**
- `/benchmark-analysis` - Peer set
- `/storyline` - Context pages
- `/slide-draft` - Visual

**Pulls from:**
- `/interview-synthesis` - Customer view
- `/market-sizing` - Size

### Handoff Format

When this output goes to a teammate or reviewer, attach a `templates/handoff-brief-template.md` cover note (Brief, Backup, So-what, Ask). Never send a page without all four.

---

## Output Quality Self-Check

Before delivering, verify:

- [ ] **Every claim** has a source and date
- [ ] **Axes** come from customer evidence
- [ ] **Implications** link to the decision
- [ ] **Gaps** are listed
- [ ] **Answer first**: the so-what leads, the detail follows
- [ ] **Sourced**: every number and claim has a source or is marked as an assumption
- [ ] **Voice**: no em dashes; none of delve, leverage, utilize, unlock, harness, streamline, robust, cutting-edge
- [ ] **Saved** to `outputs/`, not `context-library/`

---

## Related Skills

- `benchmark-analysis` - Quantify the gap
- `market-sizing` - Size the market
- `slide-draft` - Visualize
