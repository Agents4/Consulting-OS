# Prompt and Skill Testing Guide

Test skills the way you would test a new analyst: with a realistic task and a known good answer.

## Test Set
Keep 3 test cases per skill in `outputs/skill-test-results/`:
- A clean, well-specified input
- A messy input with gaps
- An input with a trap (conflicting numbers, a leading question)

## What to Check
| Check | Pass when |
|---|---|
| Context use | Reads the right files; does not ask for what exists |
| Answer first | The so-what leads |
| Sourcing | Every number has a source or is marked as an assumption |
| Voice | No em dashes or banned words |
| Template | Follows the output template |
| Questions | Asks only what files cannot answer |

## Compare Versions
When you edit a skill, run the same cases and diff the outputs. Keep a short log: date, change, result.

## Report
Write results to `outputs/skill-test-results/[skill]-[date].md`. Feed lessons into `context-library/consulting-os-learning-log.md`.
