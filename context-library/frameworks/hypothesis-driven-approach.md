# Hypothesis-Driven Approach

**Purpose:** Reference for working from an early answer instead of from all the data. Used by `/hypothesis-log`, `/day-one-answer`, `/workplan`, `/data-analysis`.

**Source:** McKinsey and BCG problem-solving material; BCG partner deck at Aalto University (March 2022).

---

## The Idea
Form a testable answer on day 1. Direct every analysis at proving or killing it. Revise as evidence arrives. The alternative (collect everything, then think) boils the ocean.

A hypothesis is not an answer. Explain this to clients, who may be nervous about a solution reached early. The hypothesis structures the work; the evidence decides.

## What Makes a Good Hypothesis
| Test | Question |
|---|---|
| **Falsifiable** | Can it be proven or disproven with data? |
| **Debatable** | Could a smart person disagree? A statement that cannot be wrong teaches nothing |
| **Material** | If reversed, would the overall logic change? |
| **Non-obvious** | Would it sound naive if you said it to the CEO? |
| **Actionable** | Does it point to something the client could do? |

## Burden of Proof
Decide how strong the evidence must be before the audience will accept it. The ladder, weakest to strongest:
1. Expert opinion or anecdote
2. Case studies and analogs
3. Benchmarks
4. Client data analysis
5. Statistical test or correlation
6. Analytic model or pilot

Raise the bar when the finding is controversial, the decision is large, or the audience is skeptical.

## Day-1, Week-1, Week-N Answers
- Write the answer on day 1, even with little data.
- Rewrite after every analytical step. Keep a version history (this is what `/hypothesis-log` does).
- Always have an answer and communicate frequently.
- When a hypothesis dies, log why. A killed hypothesis is a finding.

## Analysis Prioritization (BCG grid)
| | Low effort | High effort |
|---|---|---|
| **High importance** | **Quick win:** do first and use to shape the rest | **Big win:** invest time, plan carefully, iterate |
| **Low importance** | **Wild shot:** try without spending much | **Trap:** ask whether it is really needed or whether an analog exists |

## Hypothesis Log Structure
| ID | Hypothesis | Parent branch | Evidence needed | Burden of proof | Status | Evidence so far | Confidence | Last updated |
|---|---|---|---|---|---|---|---|---|
| H1 | Partner channel CAC is 40% below paid | Grow revenue | Channel-level CAC, 24 months | Client data | Testing | CAC 38% lower in 2 of 3 regions | Medium | Oct 12 |

Status values: Open · Testing · Supported · Weakened · Killed · Replaced.

## Common Failure Modes
- **Anchoring:** Falling in love with H1 and reading ambiguous data as support.
- **Unfalsifiable hypothesis:** "We can improve performance."
- **No update trail:** Nobody can tell why the answer changed.
- **Too many hypotheses:** More than five at the top level means the tree is not prioritized.
- **Hiding the hypothesis from the client:** Share it as a working view, not a conclusion.

## Helpful Habit: Ask "What Would Have to Be True?"
For a proposed recommendation, list the conditions that must hold. Test each. If any cannot hold, the recommendation fails or must change.
