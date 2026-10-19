# Parallel Agents Guide

Some work splits cleanly into independent pieces that can run at the same time.

## Good Candidates
- Benchmarking five peers, one agent per peer
- Summarizing ten interview transcripts
- Running reviewer personas on a deck at once (see `/review-panel`)
- QC of separate sections of a long appendix

## Poor Candidates
- Work where each step depends on the last (model logic)
- Anything touching the same file
- Judgment calls that need the full engagement context

## Rules
1. Give each agent a self-contained brief: question, inputs, output format, where to save.
2. Use the four-part handoff: Brief, Backup, So-what, Ask.
3. Define the output schema so results merge cleanly.
4. Save each result in `outputs/` under its own name.
5. Synthesize yourself. Reconcile conflicts and tie numbers before anything goes on a page.

## Check Each Result
Every agent output gets a tie-out against sources. Do not trust a number because an agent reported it.
