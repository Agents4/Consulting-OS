# Google Sheets and Google Slides Option

Consulting OS defaults to Excel (.xlsx) and PowerPoint (.pptx). This guide adds a second path: build models and trackers as **Google Sheets** and decks as **Google Slides**. The Google path is often easier than writing Python, because formulas and slides are written straight into the file, nothing needs recalculating, and the team co-edits live.

Set the choice once in `context-library/engagement-info-template.md` under **Preferred output formats**. Skills read it. If it is blank, Claude asks once and records the answer.

---

## 1. Which Path Fits

| Situation | Use |
|---|---|
| Client or firm requires its own PowerPoint master, think-cell, macros, or offline files | **Office path** (xlsx, pptx) |
| Team co-edits the same model or deck all day; client works in Google Workspace | **Google path** |
| Trackers and logs (data requests, risks, decisions, workplan, hypotheses) | **Google Sheets**, nearly always easier |
| Light to medium model (up to a few tens of thousands of formulas, small data) | Either |
| Heavy model, very large data, VBA, or Power Query | **Excel** |
| Designed deck with brand-precise layouts | **pptx** (then upload or Save as Google Slides if needed) |
| Quick SteerCo or working deck with charts that must tie to a model | **Google Slides with linked Sheets charts** |
| Write-ups (decision docs, status, proposals) | Markdown in `outputs/`; optional Google Doc via HTML upload |

**Confidentiality comes first.** Use Google Workspace for client data only if the client has approved it in writing. Record the approval under **Confidentiality rules** in engagement info. If unsure, use the Office path locally and ask the EM. See `confidentiality-and-client-data.md`.

---

## 2. What Claude Can Do Depends on Connectors

Check which Google tools are available in the session before choosing a route.

| Tier | Connectors | What works |
|---|---|---|
| 1 | Google Drive only | Create blank Sheets, Slides, Docs. Upload CSV, HTML, xlsx, or pptx and convert it. Copy, rename, move, share, read as text, export PDF. **Cannot edit contents after creation.** |
| 2 | Drive + Google Sheets editor | Tier 1 plus write values and formulas, format cells, add tabs, validation, conditional formats, charts, in place |
| 3 | Drive + Sheets editor + Slides editor | Tier 2 plus build slides, edit text and tables, embed linked Sheets charts, in place |

**Rules:**
- A change to an existing file goes into the same file, so the link stays the same. Without the editor connector, Claude asks you to turn it on. It does not make a second copy.
- Claude never trashes a file unless you ask.
- To enable connectors, use `/connect-mcps connect to Google Drive` (and Sheets, Slides, Docs), after confirming client approval.

---

## 3. What Is Easier Than Python

| Task | Office path | Google path |
|---|---|---|
| Tracker or log (data request, risk register, decision log, workplan, hypothesis log) | Build md, or openpyxl | Upload a CSV: Drive converts it to a Google Sheet (Tier 1). Done in one call. |
| Model build | openpyxl, then LibreOffice recalc, then check | Write formulas directly with the Sheets editor (Tier 2). Sheets calculates live. No recalc step. |
| Model change after review | Rebuild file, recalc, version | Edit in place; version history records it |
| Chart on a slide | Native pptx chart, number copied from the model | Chart built on the Sheet's Outputs tab, embedded as a linked chart (Tier 3). Click Update in Slides to refresh. |
| Review | Email files, track changes | Comments and suggestions, resolved before send |
| Sharing | Attachments, version confusion | One link with named people |

---

## 4. Google-Format Starters

The starters live in `templates/` as `model-starter-template.xlsx` and `ghost-deck-starter.pptx`. Make Google copies once:

1. In Drive, open `model-starter-template.xlsx`. Choose **Open with > Google Sheets**, then **File > Save as Google Sheets**.
2. Do the same with `ghost-deck-starter.pptx` using **Google Slides**.
3. Rename them **TEMPLATE - Consulting-OS Model Starter** and **TEMPLATE - Consulting-OS Ghost Deck Starter**. Keep them in a Templates folder.
4. Run the check list in `templates/google-workspace-starters.md` once, and fix anything the conversion changed.
5. For each engagement, copy the template (`/google-workspace-output` does this) and rename it `[Model]_[STATUS]_[vYYYYMMDD]_[initials]`.

Claude can also create the Google files itself by uploading with Drive. Uploads travel inside the call and are slow for files above roughly 20 KB, so manual conversion is more reliable for the two starters.

---

## 5. Sheets Model Standards (Google variant)

Same architecture as `engagement-model/07-excel-modeling-standards.md`: Cover, Guide, Inputs, Data_Raw, Calc, Scenarios, Outputs, Checks, Log. Same colors: blue inputs, black formulas, green cross-tab links, yellow fill for key selectors. Differences:

- **Live calculation.** No recalc step. Verification means reading displayed values and scanning for `#REF!`, `#DIV/0!`, `#NAME?`, `#VALUE!`, `#N/A`.
- **Master check.** `Checks` rolls up to the Cover. Integrity flags must be 0.
- **Parsing.** Sheets parses typed input like the UI. Send numbers as numbers. Write years and IDs with a leading apostrophe (`'2026`, `'00123`) so they stay text. Percentages are fractions (0.15 shows 15.0%).
- **Scenario selector.** Data validation dropdown on `Scenarios`. Sensitivity tables are grids of formulas (odd size, base case in the center), not Excel Data Tables.
- **Protection.** Protect `Calc`, `Outputs`, and `Checks` so only the model owner edits them (Data > Protect sheets and ranges). Leave `Inputs` editable.
- **Versioning.** Name a version at each gate and before every client send (File > Version history > Name current version). Make a copy named `..._FINAL_vYYYYMMDD_xx` for frozen outputs.
- **Functions.** The starter uses INDEX, MATCH, SUM, IF, MAX, ABS, SUMPRODUCT, COUNT, which port to Excel. Sheets also has XLOOKUP, FILTER, UNIQUE, SORT. If the file may go to Excel, avoid QUERY, ARRAYFORMULA, IMPORTRANGE, GOOGLEFINANCE. IMPORT* and IMAGE formulas show `#REF!` until someone clicks Allow access.
- **No cross-file links.** Avoid IMPORTRANGE between engagement files. It breaks when permissions change. Paste values with date on `Log` instead.
- **Iterative calculation off.** No circular references.
- **Size.** Google caps a spreadsheet at 10 million cells and slows well before that. Keep raw data lean; use Excel for heavy models.
- **Audit.** The auditor uses version history, Show formulas (Ctrl+`), comments for findings, and the `Checks` tab. See `sub-agents/model-auditor.md`.
- **Hand to a client who needs Excel.** File > Download > .xlsx, then open it and confirm validation, conditional formats, and totals.

---

## 6. Slides Deck Standards (Google variant)

Same discipline as `engagement-model/06-deliverable-production-decks.md`: storyline first, one message per page, action titles, source line, number tie-out.

- **Ghost deck.** One slide per page: action title, a sketched chart or placeholder shape, status tag (Ghost, Draft, Tied, Final), source and owner in speaker notes.
- **Template.** Start from the converted Google starter or the client's master. Set theme colors and fonts once. Editors cannot reliably change a master through connectors, so do that by hand.
- **Fonts.** Use fonts Google Slides has (Arial, Calibri, Cambria, Roboto, Lato). If a client font is missing, tell the EM before building.
- **Charts.** Build each chart on the model's `Outputs` tab, then embed it as a linked chart. Chart numbers then tie by construction. Remove the chart's own title and put the label in a text box above. The waterfall is a stacked column with an invisible base series. A linked chart cannot carry custom callouts or growth arrows, so add those as text boxes and shapes.
- **Numbers in text.** Titles and callouts are typed. Log each in `/number-tie-out`.
- **Fit.** Slides never shrinks text. Check each slide for overflow and clipped text.
- **Images.** Inserting an image needs a public URL. Copy logos from the template instead.
- **Freeze.** Click Update on every linked chart, resolve comments, name a version, copy to `..._FINAL`, export PDF. For a client who needs PowerPoint, File > Download > .pptx and check fonts and charts.
- **Visual check.** Export a PDF and look at every page. Without that, tell the EM the layout was not visually checked.

---

## 7. Workflows

**Model in Google Sheets**
1. `/model-spec` (same spec for both formats)
2. `/google-workspace-output` copies the Google starter, or builds blank (Tier 2)
3. Write Inputs, Calc, Outputs, Checks as formulas; format; add dropdown and conditional formats
4. Read back values; master check must be 0
5. `/model-audit`: reviewer works in a copy or comments; findings logged on `Log`
6. `/scenario-sensitivity`: paste scenario results as values with date
7. Name version; copy as FINAL; protect

**Deck in Google Slides**
1. `/storyline` then `/ghost-deck`
2. `/google-workspace-output` copies the Slides starter and builds the ghost pages (Tier 3), or hands you a build spec
3. Build charts on the Sheet `Outputs` tab; embed as linked charts
4. `/slide-draft` per page; `/number-tie-out` against `Outputs`
5. `/deck-qc`: read slide text, export PDF, check pages
6. `/review-panel`; fix; name version; export PDF

**Trackers**
Ask for the tracker; Claude uploads a CSV and returns a Google Sheet. Share with the client counterpart only if the EM agrees, and only the tracker tab or file.

---

## 8. Sharing and Control

- Share with named people only. No "anyone with the link".
- Give the client reader or commenter by default. Editor only with the EM's OK.
- Claude shares a file only when you ask.
- Ownership: the person who creates a file owns it. Create engagement files in a shared drive owned by the firm, not a personal drive, so access survives staffing changes.
- At close, export PDF and .xlsx or .pptx copies for the handover pack, then follow the data return or deletion terms (`/handover-pack`).

---

## 9. Limits

- Editing in place needs the Sheets or Slides editor connector. Drive alone can create and convert only.
- Converting pptx to Slides can change fonts and spacing, and may turn native charts into images. Always check the converted starter.
- Uploads are slow for large files. Keep uploads small.
- No think-cell. No macros. Apps Script is possible but not part of this OS.
- A Slides chart must exist in a Sheet first.
- Slides edits may need a browser reload to appear.
- Heavy models and very large data belong in Excel.
