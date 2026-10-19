# AI in Consulting (as of October 2026)

**Reliability note:** Figures below come from press coverage in 2025-2026 quoting firm leaders. They conflict in places and change fast. Use them for direction, not for quotation. Re-check before you cite.

## What the Firms Report

| Firm | Reported tooling and use |
|---|---|
| **McKinsey** | Lilli, an in-house generative AI platform on the firm's knowledge base (launched 2023). Reported monthly use above 70-75% of staff. Used for research, summarization, analysis, brainstorming, drafting proposals, and building slides from prompts through agents. A "Tone of Voice" tool checks report tone. Client data may go only into Lilli (not into outside chatbots). Leadership has described a workforce of humans and AI agents; reported agent counts range from about 20,000 to 25,000. Headcount reported falling from above 45,000 to about 40,000. QuantumBlack reported at about 1,700 people and about 40% of the firm's work. Shift reported from fee-for-service toward outcome-linked business cases |
| **BCG** | ChatGPT Enterprise to all staff (reported 33,000); 18,000+ custom GPTs; Deckster, a slide editor reported as trained on 800-900 templates with a "review this" button that grades slides against best practice (about 40% of associates reported using it weekly); GENE, a conversational assistant; an agent-building platform in beta. AI advisory work reported at about a fifth of revenue |
| **Bain** | Sage, an internal assistant built on OpenAI models |
| **Others** | Deloitte (Sidekick, Zora AI agents, Ascend), PwC/Strategy& (Microsoft Copilot) |

## What Is Changing on the Engagement

| Work | Before | Now |
|---|---|---|
| First-draft slides | Analyst builds from sketch | Agent drafts from prompt and template; human edits |
| Research and prior-work search | Research desk and knowledge team | Knowledge-base assistant with internal expert pointers |
| Interview notes and synthesis | Manual | Transcript → structured notes → theme clustering |
| Data cleaning and first-pass analysis | Analyst in Excel/Alteryx | Assisted code and formulas, still reviewed by a person |
| Slide QC | Manager and graphics review | Automated checks against best-practice rules, then human review |
| Proposals | Weeks of EM and AP time | Drafted from knowledge base in hours |
| Tone and house style | Partner edits | Style agents |

Reported implication: routine drafting and slide production shifts to AI; people focus on client-facing, judgment-heavy work. Leaders say this does not necessarily mean fewer analysts. Critics on anonymous forums call current tools "functional enough" for low-stakes tasks.

## What Does Not Change
- **Accountability.** The partner and EM own the answer. The client pays for judgment.
- **Layered review.** AI output enters the review ladder at analyst level, no higher.
- **Burden of proof.** A claim that will be used to commit money needs sources and a second check.
- **Confidentiality.** Client data goes only into approved environments.
- **Relationships.** Pre-wiring, trust, and facilitation stay human.

## Operating Rules for Consulting-OS

1. **Claude takes the analyst and junior-consultant seats; the human holds EM, AP, and Partner.** You can ask Claude to play a reviewer seat through sub-agents, but you make the call.
2. **Every number gets a source and a tie-out.** If Claude cannot cite where a figure came from, it marks it `[UNSOURCED]` and does not put it on a slide.
3. **Facts vs assumptions are labeled.** Claude tags each statement as Sourced Fact, Client-Provided, Estimate, or Hypothesis.
4. **No client data in unapproved tools.** Confirm your environment (see `setup/environment-keys.md`). If you are not sure the environment is approved, use anonymized or synthetic data.
5. **Do not invent quotes, benchmarks, or citations.** Placeholders are labeled `[PLACEHOLDER: need source]`.
6. **Check arithmetic by running it.** Claude recomputes totals and sensitivities in code or in the model, not in prose.
7. **Review AI drafts like an analyst's.** Run `/deck-review` or `/model-review` before anything goes upstream.
8. **Disclose AI use where the client or firm requires it.** Check the SOW and firm policy.

## Pricing Direction
Reported movement toward outcome-linked and shared-risk arrangements raises the importance of baselines, measurement, and the transition plan. `/value-sizing`, `/business-case`, and `/transition-plan` include a "measurement and baseline" section for that reason.

## Skills the Team Now Needs More Of
Verification habits, prompt and context design, ability to define a good analysis precisely enough to delegate it, and the judgment to know when the output is plausible but wrong.
