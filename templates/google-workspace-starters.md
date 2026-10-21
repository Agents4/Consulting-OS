# Google Workspace Starters: Setup and Check List

Run this once when you create the Google versions of the two starters (see `advanced/google-workspace-option.md`, section 4).

## Create the Google Copies
- [ ] Drive: open `model-starter-template.xlsx` > Open with Google Sheets > File > Save as Google Sheets
- [ ] Drive: open `ghost-deck-starter.pptx` > Open with Google Slides > File > Save as Google Slides
- [ ] Rename: `TEMPLATE - Consulting-OS Model Starter` and `TEMPLATE - Consulting-OS Ghost Deck Starter`
- [ ] Move both into a Templates folder; share only with the team

## Check the Sheet
- [ ] Nine tabs present in order: Cover, Guide, Inputs, Data_Raw, Calc, Scenarios, Outputs, Checks, Log
- [ ] Cover shows `ALL INTEGRITY CHECKS OK` and integrity flags 0
- [ ] Scenarios C4 is a dropdown (Low, Base, High). If not, re-add: Data > Data validation > list from range `B8:B10`
- [ ] Switch to Low and High: Outputs change; Checks stay at 0; switch back to Base
- [ ] Blue input font, black formula font, green link font survived
- [ ] Yellow selector fill on Scenarios C4
- [ ] Red and green conditional formats on Checks flags and Cover status
- [ ] Number formats: `0.0%` percent, `#,##0.0` numbers, negatives in brackets
- [ ] Cover contents links jump to each tab
- [ ] No `#REF!`, `#NAME?`, `#VALUE!`
- [ ] Protect Calc, Outputs, and Checks (model owner only)
- [ ] Iterative calculation is off (File > Settings > Calculation)

Expected example outputs (Base): baseline EBITDA 91.5, run-rate uplift 13.359, target 104.859, one-time cost 6.0, NPV 28.1, payback year 2.

## Check the Deck
- [ ] Nine pages present: title, how-to, executive summary, section divider, bar chart, options table, waterfall and KPIs, roadmap, ask
- [ ] Fonts are Cambria for titles and Calibri for body. If replaced, note which font Slides used and decide whether to switch theme fonts
- [ ] Titles are left-aligned and fit in two lines
- [ ] Charts survived. If they became pictures, rebuild them as linked Sheets charts from the model `Outputs` tab
- [ ] Waterfall: base series invisible (no fill). Fix in the Sheet chart if it shows
- [ ] Footer text and page numbers show
- [ ] Speaker notes kept
- [ ] No overflowing text on any page

## Record What Changed
Note any item that did not survive conversion here, and fix it in the TEMPLATE copies so every engagement copy starts clean.

| Item | Result | Fix applied |
|---|---|---|
