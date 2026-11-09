# Evals

Realistic cases to test skills after a change. Each case has `input.md` (what the user supplies; fictional) and `expected.md` (the first line is `Skill: <name>`, then what a good response must and must not do). Score with `rubric.md`. `python3 scripts/check_os.py` checks that every case is well formed and points at a real skill.

| Case | Skill | What it tests |
|---|---|---|
| 01 | `ingest-materials` | Two files give different revenue figures: the skill must flag the conflict, ask before writing, and log what it read |
| 02 | `research-plan` | An issue tree branch becomes locked definitions, ranked questions, a source plan and a compliance check before any search |
| 03 | `number-tie-out` | A slide says 14 percent and the model says 12.4 percent: the skill must flag it and block the send |
| 04 | `day-one-answer` | A thin brief: the answer comes first, assumptions are marked, nothing is invented |

## How to run

1. Give the skill the `input.md` content as the user would, in the platform you care about (Claude Code, Gemini CLI, a Gem, a Copilot Notebook).
2. Score the response with `rubric.md` against `expected.md`.
3. Record the result and date in your change notes. A change that regresses a "must" is not ready to ship.

Add a case when a real failure appears. Use fictional data only: no client names, no real figures.
