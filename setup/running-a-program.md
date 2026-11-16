# Running a Program: One Team, Many Projects

Use this when one team and one SteerCo run a transformation made of many projects, and you want a living knowledge base. Consulting-OS treats one engagement as one key question. A program adds a layer above it: a program question, a register of projects, and one card per project.

## The model

| Level | Holds |
|---|---|
| Program (once) | Program key question and scope, program hypotheses (PH IDs), stakeholders and SteerCo, one fact base, decision log, cross-project risks |
| Register | One row per project: ID, owner, phase, key question, the program hypothesis it serves, status and why, next gate, dependencies, card link |
| Project card | One page per project: key question, answer so far, hypotheses with confidence, numbers, decisions, risks, next gate, evidence links |

The card is the unit of knowledge. Detail lives in linked evidence docs. Templates: `templates/project-register-template.md` and `templates/project-card-template.md`.

## Starting from projects you already have

Do not retype them. Run `/program-import` on the folder that holds the charters, plans, status reports, decks and trackers. It groups the files by project, drafts a card and a register row for each from the documents alone, and marks every gap as Unknown with a named owner to ask. It copies status from the source and does not assign one. Where documents disagree on a number it shows both. You approve each project and the program hypothesis it maps to, then move the agreed cards into the program folder. Work in batches if there are many projects.

## Skills

| When | Skill |
|---|---|
| Projects already exist | `/program-import` (once, in batches) |
| A new project joins | `/project-intake` |
| After a meeting, a decision or a result | `/project-card` |
| Weekly, and before every SteerCo | `/program-rollup`, then `/steerco-prep` and `/status-update` |

## Local layout

```
context-library/engagements/[program]/
  program.md          program brief, PH hypotheses, fact base pointers
  register.md         the project register
  projects/[ID].md    one card per project
outputs/programs/[program]/
  intake-[ID]-[date].md  cards/  rollup-[date].md
```

Claude writes drafts to `outputs/programs/`. You move agreed versions into `context-library/engagements/`.

## Google route (Gem and Notebook)

Use one Gem and one Notebook for the whole program. A Gem per project does not scale past a few projects.

| Piece | Holds |
|---|---|
| Gem | CORE-1, CORE-2, CORE-3, the program brief, the shared fact base, the stakeholders doc, the decision log, the project register (a Google Sheet), and one slot for the active project card. That is 9 to 10 files, so check the limit in your tenant |
| Notebook | Every project card and its evidence, as the searchable knowledge base |

Working loop:

1. Ask the Notebook across projects: what do we know about X, which projects depend on each other, where do two cards disagree.
2. To work on one project, attach or paste its card as the Gem's active-project file, then run the playbook.
3. Paste the Gem's REGISTER UPDATE and CONTEXT UPDATES into the register and the card.
4. Weekly, 15 minutes: refresh changed cards and the register, then run `/program-rollup`.
5. Monthly: move closed projects' cards out of the Notebook into an archive folder. Keep their register rows.

Limits to plan for: Notebook sources per notebook are 50, 100 or 300 by tier. At one card plus one to three evidence docs per project, 20 projects is roughly 40 to 80 sources. Confirm your tier with IT. Everyone with access to a Notebook reads every source, so add only projects the whole team may see.

Get written approval that your Workspace is an approved place for the data before you load anything. See `setup/gemini-setup-guide.md`, Step 0.

## Rules that keep it honest

- Every project serves at least one program hypothesis. If it serves none, ask why the project exists.
- One fact base for the program. A number that differs between two cards is a flag for the owner, not a choice for the tool.
- Status needs a reason.
- Re-read the card before changing it. Apply only the requested change.
- Prefix every output with the project ID, for example `P2_pricing-model_2026-11-16_v1`.
