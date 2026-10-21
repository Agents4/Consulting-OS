# Prompt Library for the Copilot Prompt Gallery

Save these once, then run them from the Prompt Gallery inside any client Notebook. Replace bracketed items each run.

**To save a prompt:** run it, hover over your prompt in the conversation, click **Save prompt** (bookmark icon), and give it the name below. **To reuse:** open Copilot Chat, click the **Prompt Gallery** icon, pick the prompt, run it. **To share with the team:** open the Prompt Gallery, click **Share**, and choose a Teams team. Recipients get a copy of the prompt only. They run it against their own data and permissions.

Prompts reference the Notebook, so they work the same for every client.

| Gallery name | Prompt |
|---|---|
| CO 00 Start session | Read file 01 in this notebook. In two lines, state the phase, key question and current governing thought. Then list any context file that looks empty or stale. Then ask me what we are doing today. |
| CO 01 Run a playbook | Run the [playbook name] playbook from CORE-2 or CORE-3. Read files 01 and 03 first. Ask only the questions the files cannot answer. Then follow the playbook's process and output template. End with a FILING NOTE and CONTEXT UPDATES. |
| CO 02 Day-1 answer | Run the day-one-answer playbook for [client key question]. Use file 01 and anything I paste below. Give the governing thought, the three claims that must be true, and the first analyses to test each. [paste notes] |
| CO 03 Issue tree | Run the issue-tree playbook. Build a MECE tree from the key question in file 01, tag each leaf with a hypothesis and an analysis, and flag where the answer is most uncertain. |
| CO 04 Interview synthesis | Run the interview-synthesis playbook on the notes below. Give the top 3 takeaways, exact quotes worth using, which hypotheses in file 03 each supports or weakens, and follow-ups. [paste notes] |
| CO 05 Model spec | Run the model-spec playbook for [analysis]. Give tabs, inputs with sources, calculations, outputs, scenario switches and checks. List every formula in Excel syntax by sheet and cell. Do not build the model yet. |
| CO 06 Model audit | Run the model-audit playbook on the model summary below. Check structure, hardcodes, inputs against sources in file 04, sign and unit errors, and whether the checks roll up. List findings by severity. [paste formulas or tab summaries] |
| CO 07 Number tie-out | Run the number-tie-out playbook. For each number in the text below, name the model cell or source in file 04 it traces to, and flag any that do not tie. [paste slide text] |
| CO 08 Storyline | Run the storyline playbook. Write the governing thought, an SCQA, and the action titles in order so that the titles alone tell the story. Use file 03 for the evidence and file 06 for the current version. |
| CO 09 Slide spec | Run the slide-draft playbook for [slide topic]. Give the action title, layout, body text, chart type with the data table behind it, source line and speaker notes. One message per slide. |
| CO 10 Deck QC | Run the deck-qc playbook on the slide text below. Check that action titles tell the story, one message per page, numbers tie to file 04, source lines exist, and the ask is clear. [paste deck text] |
| CO 11 SteerCo prep | Run the steerco-prep playbook for the SteerCo on [date]. Use files 01, 03 and 05. Give the decisions we need, the pre-wires by stakeholder from file 02, the agenda, and the pages we need. |
| CO 12 Status update | Run the status-update playbook for [week]. Use files 01, 03 and 05. Lead with the answer, then progress against the plan, risks, and asks. Audience: [sponsor / EM / partner]. |
| CO 13 Weekly review | Run the weekly-review playbook. Compare this week's work with the plan in file 01, list what changed in the hypotheses in file 03, and give the three priorities for next week with owners. |
| CO 14 Challenge me | Play the skeptic. Read file 03. Give the five strongest objections to our current governing thought, what evidence would settle each, and which stakeholder in file 02 is most likely to raise it. |
| CO 15 Wrap up | Wrap up. List outputs produced today and where to file them, context updates not yet pasted into files 01 to 06, open questions, and the next three actions with owners. |
