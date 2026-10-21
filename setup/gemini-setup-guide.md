# Gemini Setup Guide: Consulting OS with Per-Client Google Drive

Run Consulting OS in Gemini, with one Gem and one Drive folder per client. Context and outputs live in Google Drive, so a client's whole engagement sits in one place you can share, audit and archive.

**Time:** about 45 minutes once, then about 10 minutes per new client.
**Last checked:** October 2026. Gemini changes quickly. Check each limit against the sources at the end before you rely on it.

## Pick your path

| | Path A: Gemini app + Gems (recommended) | Path B: command line agent |
|---|---|---|
| What it is | One Gem per client in gemini.google.com, with your Drive docs attached as knowledge | Gemini CLI or Antigravity CLI working inside a Drive-synced client folder |
| Skills | 55 of the 56 skills become "playbooks" in 3 knowledge files (connect-mcps does not apply). Trigger by name | Real skill folders, activated by the agent |
| Writes to Drive | No. You export and file | Yes, through the synced folder |
| Best for | Most consultants. No install, works on any device | Power users who want files written for them |
| Account needed | Any Google account with Gems. Use your approved work account | Paid API key, Gemini Code Assist Standard or Enterprise, or Antigravity CLI (see Path B) |

Start with Path A. Add Path B later if you want files written straight into Drive.

---

## Step 0: Confidentiality check (5 minutes, before any client data)

Consulting OS rule 7: client data stays on approved platforms. Before you put a client's information into Gemini:

1. **Confirm Google Workspace is an approved platform** for this client. Record where the approval lives in doc 01, "Approved platforms for client data". Without written approval, stop and use a client-approved tool.
2. **Use the approved work account, not a personal Gmail.** Sign out of other Google accounts in that browser. Being signed into a personal and a work account at once can cause Gem save failures.
3. **Know which data terms apply.** Google's help page says that on consumer accounts, with Keep Activity on, chats can be used to improve Google services including training, and a subset is read by human reviewers. It says work and school accounts may be subject to different data handling terms and points to the Workspace privacy hub. Ask your IT or Workspace admin to confirm the terms for your account. If a personal account is ever involved, turn Keep Activity off, and still do not put client data in it.
4. **Check admin controls.** An admin can disable Gems sharing or limit it to your domain, and can limit Drive sharing. If sharing a Gem fails, this is the usual cause.
5. **Use codenames in prompts** if the client asked for it. Never paste another client's material.

## Step 1: Build the shared Core folder (once)

1. In Google Drive (work account), create a folder named **Consulting Engagements**. Inside it create **00_Core**.
2. Upload the three files in `gemini/knowledge-pack/` to `00_Core`. Use the `.docx` versions:
   - `CORE-1_Engagement-Model-Frameworks-Standards.docx` (roles, lifecycle, frameworks, deck and model standards, writing style)
   - `CORE-2_Playbooks-Mobilize-to-Diagnose.docx` (21 playbooks)
   - `CORE-3_Playbooks-Model-Deck-Rhythm-Close.docx` (34 playbooks)
3. Optional: right-click each file in Drive, choose Open with Google Docs, then File > Save as Google Docs. A Google Doc stays live if you edit it. An uploaded `.docx` is a static snapshot, which is fine because the core rarely changes.
4. Upload `gem-instructions.md`, the `client-kit/` folder and `apps-script/NewClientWorkspace.gs` here too, so you have them next time.
5. If you plan to use Path B, also copy the whole `Consulting-OS` folder into `00_Core/`.

If you already sync Drive to your computer (Drive for desktop), copy the folders into the synced `Consulting Engagements/00_Core` folder and they upload on their own.

## Step 2: Create a client workspace (per client, about 5 minutes)

### Option 1: automatic with the script (recommended)

1. Go to script.google.com while signed in with the approved account. Click **New project**.
2. Open `gemini/apps-script/NewClientWorkspace.gs`, copy all of it, and paste it over the contents of `Code.gs`.
3. Edit the first two constants: `CLIENT_NAME` and `ENGAGEMENT_NAME`.
4. In the function menu choose `createClientWorkspace`, click **Run**, and approve the Drive, Docs and Sheets permissions.
5. Open **Execution log**. It prints a link to every file created.

It builds this tree. Re-running it reuses folders and skips files that exist.

```
Consulting Engagements/
  00_Core/                      shared playbooks and frameworks (Step 1)
  Clients/
    [Client]/
      00_Context/               6 Google Docs the Gem reads
      01_Outputs/               everything you export or build, by subfolder
        Proposals and Workplans / Hypotheses and Issue Trees / Interviews and Research /
        Analyses and Models / Storyline and Decks / Reviews / SteerCo and Status /
        Meetings and Decisions / Recommendations and Roadmaps / Transition and Retro
      02_Data/                  client data extracts (approved storage only)
      03_Trackers/              data request tracker, risk register, workplan (Google Sheets)
      04_Archive/               old versions and retired context
```

### Option 2: by hand

Create the same folders. Create six Google Docs in `00_Context` by pasting each file from `gemini/client-kit/` (headings and tables paste correctly). Create the three trackers as Google Sheets in `03_Trackers`.

### Fill in doc 01 first

Open `01 Engagement-Brief - [Client]`. Fill in the key question, scope, gates, firm standards, and approved platforms. This is the one doc the Gem reads at the start of every session. Leave the others as templates and let them fill as you work.

## Step 3: Create the client Gem

1. Go to **gemini.google.com**, signed in with the approved account. In the left sidebar click **Explore Gems**, then **New Gem**. Gems are created on the web. The mobile apps run them.
2. **Name:** `Consulting OS | [Client]`.
3. **Instructions:** open `gemini/gem-instructions.md`, copy the box, replace `[CLIENT]` and `[ENGAGEMENT]`, and paste.
4. **Knowledge:** click add files, choose **Drive**, and attach these 9 files one at a time. Drive folders cannot be attached, only files.

| Slot | File | Why |
|---|---|---|
| 1 | CORE-1 Engagement Model, Frameworks, Standards | How engagements run and how to build well |
| 2 | CORE-2 Playbooks, Mobilize to Diagnose | 21 task playbooks |
| 3 | CORE-3 Playbooks, Model to Close | 34 task playbooks |
| 4 | 01 Engagement-Brief | Key question, scope, gates, standards |
| 5 | 02 Stakeholders-and-Team | Who matters and how to engage them |
| 6 | 03 Hypotheses-and-Issue-Tree | The live answer and its tests |
| 7 | 04 Fact-Base-and-Data-Notes | Numbers, sources, assumptions |
| 8 | 05 Decisions-Meetings-Interviews-Log | What was decided and heard |
| 9 | 06 Storyline-and-Deck-Text | Current story and slide text |
| 10 | Spare | A client data summary or the latest SteerCo pre-read |

A Gem holds up to 10 knowledge files, each up to 100 MB. Google Docs and Sheets attached from Drive stay live and show their latest version. Other file types are snapshots from the moment you add them. That is why the six context docs are native Google Docs.

5. Click **Save**. Testing in the preview panel does not save the Gem. If you close the page first, the Gem is lost.
6. Test it: type `Run the day-one-answer playbook`. It should read doc 01, state the phase and key question, then ask only what the docs cannot answer.

### Share it with the team (optional)

Open the Gem manager, choose share, and add teammates by email with viewer or editor access. Gemini prompts you to share the attached files too. Teammates need Drive access to the client folder, and your admin may restrict Gem sharing.

## Step 4: The daily working loop

1. **Open the client Gem.** Say what you are doing today. Or run a playbook by name: `Run the interview-synthesis playbook`, `Run the model-spec playbook`, `Run the steerco-prep playbook`.
2. **Answer its questions.** Paste raw material (interview notes, a data summary) straight into the chat. Never paste data you are not cleared to store in Gemini.
3. **Export the result.**
   - Memos, plans, agendas and summaries: under the response, click **Share & export** > **Export to Docs**. A new Doc lands in Drive.
   - Tables and trackers: click **Export to Sheets** at the bottom right of the table. Only responses with a table qualify, and tables with images cannot export.
   - Emails: **Share & export** > **Draft in Gmail**.
4. **File it.** Move the exported file to `Clients/[Client]/01_Outputs/[subfolder]/`. Rename it as the Gem's FILING NOTE says.
5. **Update the context.** The Gem ends each output with CONTEXT UPDATES. Paste those lines into the named doc and section. Because the docs are live, the Gem sees the change next session. This is your "learning loop". Skip it and the Gem drifts from reality.
6. **Close the day.** Say `wrap up`.

**Weekly (15 minutes):** run `Run the weekly-review playbook`, re-read docs 03 and 04, archive stale log entries to `04_Archive`, and check that doc 01's phase and next gate are current.

## Step 5: Building the actual deliverables

Gemini returns chat text and tables. The Gem turns them into specs you finish in Google's editors.

| Deliverable | What the Gem gives you | How you finish it |
|---|---|---|
| Memo, workplan, SteerCo agenda | Formatted text | Export to Docs |
| Tracker, risk register, data requests | A table | Export to Sheets, or paste into the tracker in `03_Trackers` |
| Excel-style model | Model spec, one table per tab, formulas in Sheets syntax listed by cell | Build in Google Sheets. If your plan has Gemini in Sheets, open the same client Gem from the side panel and ask it to enter the formulas. Run the model-audit and number-tie-out playbooks before sending |
| Deck | Storyline, then a slide-by-slide spec (action title, layout, chart and its data, source, notes) | Build in Google Slides from your firm template, or use Gemini in Slides if your plan includes it. The Gemini app export menu does not list Slides |
| Final readout | Outline and talking points | Same as deck. Run the deck-qc playbook last |

Eligible Workspace users can see their Gems in the side panel of Docs, Gmail and Sheets, which puts the client Gem next to the file you are editing.

**Quality gates you still run yourself:** the model-audit playbook (formulas, checks, hardcodes), the number-tie-out playbook (every number on a page to a cell or source), and a human review. Gemini can miss formula errors.

---

## Path B: command line agent writing straight into Drive

Use this if you want files written for you. The quickest route is the packaged extension: see `setup/gemini-cli-extension.md` (one install command, 54 skills, 55 slash commands). The manual steps below are the alternative. It needs Drive for desktop so the Drive folder appears on your computer.

**Check your access first.** Google announced that Gemini CLI stops serving consumer Google AI Pro, Ultra and free individual users on June 18, 2026, and replaced it for them with the Antigravity CLI. Gemini CLI stays available through paid Gemini API keys and Gemini Code Assist Standard or Enterprise licenses. Antigravity CLI supports Agent Skills, so the skill folders work there too, but Google says feature parity is not 1:1, and the announcement does not mention `GEMINI.md`. Check which CLI your account can use before you install.

1. **Install Drive for desktop** and sign in with the approved account. Your Drive appears as a folder (on a Mac, under `~/Library/CloudStorage/GoogleDrive-[account]/My Drive`).
2. **Install Gemini CLI** (Node.js 20 or later): `npm install -g @google/gemini-cli`, then run `gemini` and sign in. Antigravity users follow Google's migration guide instead.
3. **Put the full OS in the Core folder.** Copy the `Consulting-OS` folder to `Consulting Engagements/00_Core/Consulting-OS`.
4. **Install the skills at user level.** Skills load from `~/.gemini/skills/` (or `~/.agents/skills/`). Copy the folders in `Consulting-OS/.claude/skills/` there, then run `/skills reload` and `/skills list`. Skill activation is model-driven. Type "run the issue-tree skill" rather than a slash command.
5. **Add the client context file.** Copy `gemini/cli/GEMINI.md` into `Clients/[Client]/`, replace `[CLIENT]`, and open that folder in your terminal before you run `gemini`. The file imports the Core rules with an `@` import and maps the OS paths to your client folder. Run `/memory show` to confirm it loaded.
6. **Optional: Workspace extension.** The Google Workspace extension for Gemini CLI reads Drive, Docs, Sheets, Slides, Gmail and Calendar. Install it from its GitHub page (`gemini-cli-extensions/workspace`) using the command in its README. Its limits: Drive has no upload tool (only search, find folder, create folder, download, rename, trash); Docs can be created and edited; Sheets and Slides are read-only. For Google formats, the agent writes files to `01_Outputs/` in the synced folder and Drive for desktop syncs them; convert to Sheets or Slides from the Drive web UI.

Path B writes files, but the same human gates apply.

---

## Limits and gotchas

| Issue | What to do |
|---|---|
| 10 knowledge files per Gem | The 9 slots above leave 1 spare. Merge docs if you need more context |
| Drive folders cannot be attached | Attach files one at a time. New files need re-attaching to each Gem |
| Non-Google files are snapshots | Keep context in native Google Docs and Sheets so edits flow through |
| The Gem cannot write to Drive | Export, file, and paste CONTEXT UPDATES yourself. This is the main cost of Path A |
| Slides export is not in the Gemini app menu | Build decks in Slides from the Gem's slide spec |
| Export to Sheets only works on tables | Ask the Gem for "a table" per tab, no images in cells |
| Playbooks, not slash commands | Say "Run the [name] playbook". Names are in CORE-2 and CORE-3 |
| Long chats drift | Start a new chat per task. The context docs carry the state |
| Gem not saving | Click Save before closing the preview. Use a single signed-in account |
| Gem will not share | Your admin may restrict sharing. Also share the attached files |
| Retrieval may miss a rule | If an answer ignores a standard, name the playbook or doc: "Use the numbers-tie rule in CORE-1" |
| Gemini can be wrong | It can invent numbers or formulas. Tie out every number. Do not send unreviewed output |
| Playbook files go stale | After you change a skill or framework, run `python3 gemini/tools/build_pack.py` (needs pandoc), then replace the 3 files in `00_Core` and re-attach them to each Gem |

## When a client engagement ends

1. Run the handover-pack, retrospective and knowledge-capture playbooks.
2. Export the final decks and models to `01_Outputs/` and move the Gem's context docs to `04_Archive/`.
3. Delete the Gem, or stop using it. Ask the client about retention rules for data in `02_Data/`.
4. Remove client identifiers before reusing any lesson on another engagement.

## Sources

- [Gemini Gems file limit (fast.io)](https://fast.io/resources/gemini-gems-file-limit/)
- [Creating Gems: knowledge files, sharing, accounts (geotoolbox.ai)](https://geotoolbox.ai/blog/gemini-gems)
- [Export responses from Gemini Apps (Google)](https://support.google.com/gemini/answer/14184041)
- [Gemini Apps privacy and Keep Activity (Google)](https://support.google.com/gemini/answer/13594961)
- [Install Gemini CLI](https://geminicli.com/docs/get-started/installation/)
- [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/skills/)
- [Gemini CLI GEMINI.md context files](https://geminicli.com/docs/cli/gemini-md/)
- [Build Gemini CLI extensions](https://geminicli.com/docs/extensions/writing-extensions/)
- [Gemini CLI Workspace extension](https://gemini-cli-extensions.github.io/workspace/)
- [Transitioning Gemini CLI to Antigravity CLI (Google Developers Blog)](https://developers.googleblog.com/en/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
