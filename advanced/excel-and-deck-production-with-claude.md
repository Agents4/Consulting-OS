# Excel and Deck Production with Claude

How Consulting OS builds the two core artifacts.

## Excel Models
1. `/model-spec` first. Three questions, structure, inputs, checks, owner, reviewer.
2. `/model-build` copies `templates/model-starter-template.xlsx` and builds with openpyxl.
3. Formulas only. Inputs live on the Inputs tab. Blue = input, black = formula, green = link.
4. Recalculate with LibreOffice until zero errors. Confirm the Cover shows all integrity checks OK.
5. Use broadly compatible functions (INDEX/MATCH, SUMIFS, IFERROR). Avoid functions LibreOffice or older Excel cannot calculate.
6. `/model-audit` for independent review. Fix. Re-run checks.
7. `/scenario-sensitivity` for cases and tornado. Paste scenario results as values with date on the Log tab.
8. File name: `[Model]_[STATUS]_[vYYYYMMDD]_[initials].xlsx`.

## Decks
1. `/storyline` then `/ghost-deck`: titles and chart sketches before any data.
2. Build pages with pptxgenjs or python-pptx on the client or firm template. Use native charts so numbers stay editable.
3. One message per page. Action titles. Source and units on every chart.
4. `/number-tie-out`: every number traced to a model cell or source.
5. `/deck-qc`: horizontal read test, formatting, language, file hygiene.
6. Render to images and look at every page. Fix overflow, overlap, and low contrast.
7. Save an editable master and a PDF. Freeze the version.

## What Claude Does Not Replace
Firm-specific think-cell charts, brand templates behind a login, and partner judgment. Hand those steps to the production team or to you.
