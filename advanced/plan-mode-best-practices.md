# Plan Mode Best Practices

Use Plan Mode when a task is large, hard to reverse, or spans several files.

## Use It For
- Building a model from a spec (structure first, then formulas)
- Restructuring a storyline or ghost deck
- A data cleaning pipeline over several client files
- Any change that touches many outputs (for example a definition change)

## Skip It For
Single-page edits, meeting notes, and emails.

## Pattern
1. State the goal and the constraint ("Deck for Thursday SteerCo, 12 pages, numbers tie to the model").
2. Ask Claude to plan: files to read, steps, outputs, checks.
3. Challenge the plan: "What could go wrong? What is the first check?"
4. Approve. Claude executes in order and runs the checks.
5. Review the outputs against the plan.

## Good Plans for Consulting Work
- **Model:** spec → copy starter → inputs → calcs → outputs → checks → recalc → audit
- **Deck:** storyline → ghost → draft pages → tie-out → QC → panel review
- **Analysis:** data profile → reconcile → analysis → so-what → page
