# Technical and Analytic Writing Style

Use for model documentation, methodology appendices, data notes, assumption logs, and finance-partner communications.

## Characteristics

**Tone:** Precise, neutral, auditable.
**Audience:** Finance partners, analysts, data owners, model reviewers.
**Goal:** Let a skeptical reader reproduce the number.

## Rules

### 1. Define Before You Use
State what each metric means, its unit, its period, and its source.
"Net revenue = gross bookings less cancellations and refunds, USD, fiscal year ending June."

### 2. Show the Math
`10,000 eligible accounts x 30% adoption x $5 ARPU x 12 months = $180,000`

### 3. Separate Facts from Assumptions
Use a table: Item · Value · Source · Date · Owner · Confidence.

### 4. State Edge Cases and Exclusions
What was excluded and why. What was imputed and how. What changed between data pulls.

### 5. Use Ranges and Say What Drives Them
"Base $15M; range $12-18M; conversion rate drives 60% of the spread."

### 6. Version Everything
Model version, data pull date, reviewer, sign-off.

### 7. Reconcile
Every baseline ties to a client-reported figure. State the variance and its explanation.

## Structure for a Methodology Note
1. Purpose and question answered
2. Data sources (with dates and owners)
3. Definitions
4. Method (steps, formulas)
5. Assumptions and sensitivities
6. Checks performed and results
7. Limitations
8. Reviewer and sign-off

## Voice Notes
- Plain sentences. Passive voice only when the actor is irrelevant.
- No em dashes. No marketing language.
- Units and periods on every number.
