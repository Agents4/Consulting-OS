# Building Custom Skills and Agents

## Add a Skill
1. Create `.claude/skills/<name>/SKILL.md`.
2. Frontmatter: `name`, `description`, `disable-model-invocation: false`, `user-invocable: true`.
3. Follow the standard sections: Quick Start, Context Routing Logic, Step 0, Questions, Process, Output Template, Output Integration, Self-Check, Related Skills.
4. Route to the engagement files it needs. Save outputs to `outputs/`.
5. Test with three cases (`prompt-testing-guide.md`).

## Add a Reviewer Persona
Create `sub-agents/<role>.md` with: who they are, what they care about, the five questions they always ask, red flags, and a feedback format (top three issues, one strength, verdict).

## Good Candidates for New Skills
Firm-specific: practice templates, a client's reporting format, a recurring diligence checklist, an industry benchmark pull.

## Keep It Small
Each skill does one job and links to others. If a skill needs more than ~200 lines, split it.
