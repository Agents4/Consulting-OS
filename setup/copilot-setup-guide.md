# Microsoft Copilot Setup Guide: Consulting OS with Per-Client SharePoint or OneDrive Folders

Run Consulting OS in Microsoft 365 Copilot **without creating any agents**. You use one Copilot Notebook per client, a client folder in SharePoint or OneDrive, saved prompts, and Copilot inside Word, Excel and PowerPoint.

**Time:** about 40 minutes once, then about 10 minutes per client.
**Last checked:** October 2026. Copilot changes often, and menu names vary by tenant and rollout. Check limits against the sources at the end.

## How it works without agents

| Need | What you use instead |
|---|---|
| A per-client assistant | A **Copilot Notebook** per client. It answers from only the files you add, and holds custom instructions |
| Skills and slash commands | 54 **playbooks** inside three Word files in the Notebook. You say "Run the issue-tree playbook" |
| Per-client memory | Six context **Word files** you keep current. Notebook references stay current as the files change |
| Files written for you | Not available. You copy Copilot's output into Office, save it in the client folder, and paste the context updates it gives you |
| Reusable commands | **Saved prompts** in the Prompt Gallery, shareable to a Teams team |
| Building decks and models | **Copilot in PowerPoint and Excel**, driven by specs from the Notebook |

If you cannot see Notebooks in your tenant, use the plain Chat fallback in Step 3.

## What you need

- A Microsoft 365 Copilot or Copilot Chat license on your work account. Notebooks need a SharePoint or OneDrive service plan.
- Reference limits: with Microsoft 365 Copilot you can add more than 300 references and the first 300 are used. With Copilot Chat you can add 50 and all 50 are used. This guide needs fewer than 20.
- Copilot in Word, Excel and PowerPoint needs the Microsoft 365 Copilot license.
- Microsoft also ships Word, Excel and PowerPoint agents that you can call with @Word, @Excel or @PowerPoint. They need the Frontier program and Anthropic models enabled in your tenant. They are built by Microsoft, not by you, and this guide works without them.

---

## Step 0: Confidentiality check (5 minutes, before any client data)

Consulting OS rule 7: client data stays on approved platforms.

1. **Confirm Microsoft 365 is an approved platform** for this client. Record where the approval lives in file 01, "Approved platforms for client data". If it is not approved, stop.
2. **Know what the protection covers.** Microsoft states that prompts, responses and data accessed through Microsoft Graph aren't used to train foundation models, and that Copilot respects your identity model and permissions. Its page does not say whether humans can review prompts, so ask your admin or read the Microsoft 365 Copilot privacy page.
3. **Handle web search separately.** Web queries sent to Bing run under separate terms, and Microsoft acts as an independent controller for them. Do not put client details into prompts that use web search. Use the work-only setting if your tenant shows one.
4. **Watch Memory.** Copilot Memory keeps details from your chats. Review it under Personalization settings, keep client facts out of it, and ask your admin whether you can turn it off.
5. **Check regional rules.** Microsoft says Anthropic models are excluded from the EU Data Boundary and in-country processing commitments. If a client has data residency terms, ask your admin which models are on.
6. **Permissions are your safety net.** Copilot only uses files you can open. Share each client folder with named people only.

## Step 1: Build the shared Core folder (once)

1. In SharePoint (preferred, so the team can share) or OneDrive, create **Consulting Engagements**, and inside it **00_Core** and **Clients**.
2. Upload the three files in `copilot/knowledge-pack/` to `00_Core`:
   - `CORE-1_Engagement-Model-Frameworks-Standards.docx`
   - `CORE-2_Playbooks-Mobilize-to-Diagnose.docx` (21 playbooks)
   - `CORE-3_Playbooks-Model-Deck-Rhythm-Close.docx` (33 playbooks)
3. Also upload `notebook-instructions.md` and `prompt-library.md` from `copilot/` so you have them next time.

The Copilot pack differs from the Gemini pack only in its output lines (Word and Excel, not Google formats) and in leaving out the Google playbook.

## Step 2: Create a client workspace (per client, 5 minutes)

1. Unzip `copilot/Client-Workspace-Starter.zip`. You get a folder named `CLIENT-NAME`. Rename it to the client name or codename you are allowed to store.
2. Upload that folder into `Consulting Engagements/Clients/` (drag and drop in SharePoint or OneDrive on the web).

```
Consulting Engagements/
  00_Core/                       shared playbooks and frameworks (Step 1)
  Clients/
    [Client]/
      00_Context/                6 Word files Copilot reads (01 to 06)
      01_Outputs/                everything you build, by subfolder (10 subfolders)
      02_Data/                   client data extracts, approved storage only
      03_Trackers/               Engagement-Trackers.xlsx (data requests, risk register, workplan)
      04_Archive/                old versions and retired context
      05_Templates/              model-starter-template.xlsx, ghost-deck-starter.pptx
```

3. Open `01_Engagement-Brief` and fill in the key question, scope, gates, firm standards and approved platforms. Copilot reads this file at the start of every session. Leave files 02 to 06 as templates and fill them as you work.
4. Share the client folder with named teammates only, using SharePoint permissions.

## Step 3: Create the client Notebook

1. Open the **Microsoft 365 Copilot app** and go to **Notebooks**. Create a new notebook named `Consulting OS | [Client]`. Menu names vary a little by tenant.
2. In the Content pane, select **Add references** and add these. You can search, upload, paste a link, use the OneDrive picker, or drag and drop.
   - **Add these files directly** (direct adds are always included): the 3 CORE files and the 6 context files in `00_Context`.
   - **Add these as folders:** `01_Outputs` and `03_Trackers`. For a folder, Copilot picks the most relevant supported files you can access, up to 300.
   - Supported types: .docx, .pptx, .xlsx, .pdf, .loop, .page, .txt, .rtf, and OneNote pages. Links to OneDrive or SharePoint items work. External web links must be public.
3. Open the notebook's custom instructions, and paste the **Client Notebook instructions** from `copilot/notebook-instructions.md` with `[CLIENT]` and `[ENGAGEMENT]` filled in.
4. Test it: type `Run the day-one-answer playbook`. It should read file 01, state the phase and key question, then ask only what the files cannot answer.
5. Share the Notebook with your team if you want. Check that they have access to the client folder too.

### Fallback: no Notebook, plain Copilot Chat

Open Copilot Chat. Paste the **session starter** from `copilot/notebook-instructions.md`, and attach or link files 01 to 06 and the CORE files. You must repeat this each session, and file limits in chat are tighter than in a Notebook, so attach only the files the task needs.

### Set your personal defaults once

Paste the short global custom instructions from `copilot/notebook-instructions.md` into **Settings and more > Chat settings > Personalization > Custom instructions**. Keep client facts out of them.

## Step 4: Save the prompt library (10 minutes, once)

Open `copilot/prompt-library.md`. For each of the 16 prompts: paste it into chat, run it, hover over your prompt, click **Save prompt** (bookmark icon), and use the name in the table. To share with the team, open the Prompt Gallery, click **Share**, and pick a Teams team. Recipients get the prompt only and run it on their own access.

## Step 5: The daily working loop

1. **Open the client Notebook.** Run `CO 00 Start session` from the Prompt Gallery.
2. **Run playbooks.** Use the saved prompts, or say `Run the [name] playbook`. Answer its questions. Paste raw notes straight into chat.
3. **Copy the output to Office.** Paste memos into Word, tables into Excel, and slide specs into PowerPoint. Copilot's chat answers have copy options under the response, and some tenants show export options as well. Look for them.
4. **Save in the client folder.** Use the FILING NOTE at the end of the answer for the subfolder and file name.
5. **Update the context.** Paste each CONTEXT UPDATES line into the file and section it names. Because the Notebook references stay current, it sees the change next time. Skipping this is how the Notebook drifts from reality.
6. **Close the day** with `CO 15 Wrap up`.

**Weekly (15 minutes):** run `CO 13 Weekly review`, re-read files 03 and 04, move log entries older than 6 weeks to `04_Archive`, and check that file 01's phase and next gate are current.

## Step 6: Building the deliverables

| Deliverable | What the Notebook gives you | How you finish it |
|---|---|---|
| Memo, workplan, SteerCo agenda | Formatted text | Paste into Word, or ask Copilot in Word to tighten it |
| Tracker, risk register, data requests | A table | Paste into `Engagement-Trackers.xlsx` in `03_Trackers` |
| Model | Model spec, one table per tab, every formula by sheet and cell | Copy `model-starter-template.xlsx` from `05_Templates`, build in Excel. Use Copilot in Excel for formulas and charts. Then run `CO 06 Model audit` and `CO 07 Number tie-out` |
| Deck | Storyline, then a slide spec (action title, layout, text, chart data, source, notes) | Copy `ghost-deck-starter.pptx` or your firm template. Ask Copilot in PowerPoint to build slides from the spec, choosing your template. Then run `CO 10 Deck QC` |
| Final readout | Outline and talking points | Same as deck |

**Copilot in Excel, what to know:**
- Copilot editing works only when Calculation Options are set to **Automatic**.
- Files that require check-out in SharePoint will not work with Copilot in the desktop apps. Excel for the web does.
- Save as .xlsx. Unsupported formats such as Strict Open XML give an "Unsupported file state" error.
- Saved Copilot changes are visible to anyone with file access, including coauthors. You can undo them or view earlier versions.
- Microsoft says Copilot can make mistakes and advises you to review, edit and verify anything it creates. Do not rely on it alone for financial work. Keep the model rules: inputs, calculations and outputs separated, no hardcodes in formulas, checks rolling up, independent review.

**Copilot in PowerPoint:** open a new presentation, open Copilot Chat, describe the deck, answer its clarifying questions about audience, length and template, and it builds from your chosen template. If your organization publishes a Brand Kit, pick it under Select brand. Paste the slide spec from the Notebook into your prompt. Microsoft's page does not describe building from a Word file, so paste the text.

**Quality gates you still run yourself:** model audit, number tie-out, deck QC, and a human review before anything goes to the client.

---

## Limits and gotchas

| Issue | What to do |
|---|---|
| Copilot cannot save files or write to folders | Copy, save, and paste CONTEXT UPDATES yourself. This is the main cost of having no agents |
| Notebook reference limits | 300 used with Microsoft 365 Copilot, 50 with Copilot Chat. A folder reference picks the most relevant files, so add must-have files directly |
| Retrieval may miss a rule | Name the file or playbook: "Use the number tie rule in CORE-1" |
| Long chats drift | Start a new chat per task. The context files carry the state |
| Notebook not visible | Needs a SharePoint or OneDrive service plan and a Copilot license. Use the chat fallback and ask your admin |
| Excel formulas look right but are wrong | Audit them. Check the master check, then trace three outputs by hand |
| Chat export differs by tenant | Use copy and paste if you do not see export options |
| Web search sends text to Bing | Keep client details out of web-grounded prompts |
| Playbook files go stale | After you change a skill or framework, run `python3 gemini/tools/build_pack.py copilot` (needs pandoc), replace the 3 files in `00_Core`, and re-add them to each Notebook |
| Copilot can be wrong | It can invent numbers or formulas. Tie out every number |

## When an engagement ends

1. Run the handover-pack, retrospective and knowledge-capture playbooks.
2. Save final decks and models in `01_Outputs`, move the context files to `04_Archive`, and delete or stop using the Notebook.
3. Ask the client about retention rules for `02_Data`.
4. Remove client identifiers before reusing any lesson on another engagement.

## Sources

- [How Microsoft 365 Copilot Notebooks works](https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-notebooks-works)
- [Add references to your Copilot Notebook](https://support.microsoft.com/topic/73048ee1-fd1d-4f7b-b850-b011029e09f2)
- [Customize how Microsoft 365 Copilot responds to you](https://support.microsoft.com/en-us/microsoft-365-copilot/customize-how-microsoft-365-copilot-responds-to-you)
- [Enterprise data protection in Microsoft 365 Copilot](https://learn.microsoft.com/en-us/copilot/microsoft-365/enterprise-data-protection)
- [Frequently asked questions about Copilot in Excel](https://support.microsoft.com/office/7a13758f-d61e-4a56-8440-f2c9a07802ec)
- [Create a new presentation with Copilot in PowerPoint](https://support.microsoft.com/en-us/office/create-a-new-presentation-with-copilot-in-powerpoint-3222ee03-f5a4-4d27-8642-9c387ab4854d)
- [Word, Excel and PowerPoint agents in Microsoft 365 Copilot (MC1187799, via itelio)](https://www.itelio.com/en/microsoft-message-center/MC1187799)
- [Saving and sharing prompts (A Guide to Cloud)](https://aguidetocloud.com/guided/ab-730/domain-2/saving-sharing-prompts/)
- [Personalizing your experience in Copilot (University of Iowa ITS)](https://its.uiowa.edu/news/2026/07/personalizing-your-experience-copilot)
