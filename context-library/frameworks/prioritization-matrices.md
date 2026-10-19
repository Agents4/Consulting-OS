# Prioritization Matrices

**Purpose:** Choose which issues to analyze, which initiatives to recommend, and which tasks to do first. Used by `/prioritize`, `/issue-tree`, `/workplan`, `/recommendation-roadmap`.

---

## 1. Impact vs Ease (issues and initiatives)
| | Easy | Hard |
|---|---|---|
| **High impact** | Do now (quick wins) | Plan and invest (big bets) |
| **Low impact** | Do if free (fillers) | Drop |

**Scoring:** 1-5 on each axis with a written rationale. Impact: EBITDA or strategic value. Ease: time, cost, data, client control, dependencies.

## 2. Effort vs Importance (analyses) - BCG grid
Big win · Quick win · Wild shot · Trap (see `hypothesis-driven-approach.md`).

## 3. Value vs Risk (initiatives)
| | Low risk | High risk |
|---|---|---|
| **High value** | Commit | Pilot first |
| **Low value** | Backlog | Reject |

## 4. Weighted Scoring (when a committee must choose)
| Criterion | Weight | Option A | Option B | Option C |
|---|---|---|---|---|
| Financial value (NPV) | 30% | | | |
| Strategic fit | 20% | | | |
| Feasibility | 20% | | | |
| Risk | 15% | | | |
| Time to impact | 15% | | | |
| **Weighted score** | 100% | | | |

Agree the weights with the SteerCo before scoring, not after. Run a sensitivity on the weights.

## 5. Critical Path Triage (team tasks) - LNO adapted
| Class | Meaning | Rule |
|---|---|---|
| **Critical** | On the path to the next SteerCo or gate | Do first, protect time |
| **Multiplier** | Reusable asset that speeds later work (a model module, a template) | Do when it saves more than it costs |
| **Neutral** | Needed, low visibility | Do efficiently |
| **Overhead** | Admin | Batch it, delegate it |

## 6. Horizon View (roadmap)
- **0-90 days:** quick wins, mobilization
- **3-12 months:** core initiatives
- **12+ months:** structural bets

## Rules of Thumb
- Score in a group, then discuss the outliers.
- Show the ranges, not point estimates, when sizing.
- If the top three are close, the criteria are not discriminating. Add one.
- Re-run the matrix when new data lands.
