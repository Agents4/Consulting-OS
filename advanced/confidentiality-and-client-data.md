# Confidentiality and Client Data

Consulting runs on trust. AI tools raise real questions about client data. Settle them before the first upload.

## Before You Start
- [ ] Read the engagement letter and NDA for data handling terms
- [ ] Ask the EM and the firm's risk or IT group what AI tools are approved
- [ ] Ask the client whether AI tools may touch their data, in writing
- [ ] Decide where data lives (client platform, firm platform, local encrypted drive)

## Working Rules
1. Use only approved tools on client data.
2. Strip or code client names, people, and sensitive fields where the analysis allows.
3. Do not paste client data into unapproved services.
4. Log each data pull: source, owner, date, permission basis, location.
5. `.gitignore` excludes `context-library/data/` and `client-materials/`. Do not override it.
6. Return or delete client data at the end as agreed. Log it in the handover pack.
7. Do not reuse client content in another engagement. Capture only anonymized learnings (`/knowledge-capture`).

## Personal Data
If a dataset includes personal data, ask the risk advisor (`sub-agents/risk-compliance-advisor.md`) before any processing.

## When in Doubt
Stop and ask the EM. The cost of a short pause is small.
