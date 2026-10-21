/**
 * Consulting OS: New Client Workspace (Google Apps Script)
 *
 * What it does: creates the Drive folder tree for one client, the six context
 * Google Docs your Gem reads, and three tracker Google Sheets. Safe to re-run:
 * it reuses folders and skips files that already exist.
 *
 * How to use:
 *  1. Go to script.google.com, click New project, paste this file over Code.gs.
 *  2. Edit CLIENT_NAME and ENGAGEMENT_NAME below.
 *  3. Pick createClientWorkspace in the function menu and click Run.
 *  4. Approve the Drive, Docs and Sheets permissions the first time.
 *  5. Open View > Logs (or Execution log) for links to every file created.
 *
 * Run this while signed in with the Google account approved for client data.
 */

const CLIENT_NAME = 'Acme';              // use the client name or codename you are allowed to store
const ENGAGEMENT_NAME = 'Project Northstar';
const ROOT_FOLDER_NAME = 'Consulting Engagements';

const OUTPUT_SUBFOLDERS = [
  'Proposals and Workplans', 'Hypotheses and Issue Trees', 'Interviews and Research',
  'Analyses and Models', 'Storyline and Decks', 'Reviews', 'SteerCo and Status',
  'Meetings and Decisions', 'Recommendations and Roadmaps', 'Transition and Retro'
];

const CONTEXT_DOCS = {
 "01_Engagement-Brief": "# 01 Engagement Brief: [Client]\n\nLast updated: [date]  |  Phase: [Mobilize / Diagnose / Develop / Recommend / Transition]  |  Next gate: [date]\n\n## Key question\n[One sentence, phrased as a question. Example: How can the client close the $40M EBITDA gap by FY2028 without reducing service levels?]\n\n## Success criteria\n- [Metric, target, date]\n- [Capability or mindset shift]\n\n## Scope\n- In: [ ]\n- Out: [ ]\n- Constraints: [budget, timing, regulatory, political, technology]\n\n## Day-1 answer (current governing thought)\n[2 to 3 sentences. Update the version and date each time it changes. History lives in doc 03.]\n\n## Timeline and gates\n| Gate | Date | Decision the client makes | Deliverable |\n|---|---|---|---|\n| Kickoff | | | |\n| Diagnostic readout | | | |\n| Mid-point SteerCo | | | |\n| Final readout | | | |\n\n## Governance\n- Sponsor check-in: [day, time, who]\n- SteerCo: [cadence, members]\n- Internal: daily huddle [time], EM review [day], Partner session [day]\n\n## Firm standards and formats\n- Firm style: [McKinsey-style / BCG-style / Bain-style / client in-house]\n- Models and trackers: Google Sheets\n- Decks: Google Slides\n- Memos: Google Docs\n- Deck conventions: action title max [15] words; fonts [ ]; colors [ ]; source line format [ ]\n- Model conventions: inputs blue, formulas black, cross-tab links green, checks roll up to a master check\n- File naming: [Client]_[Topic]_[YYYY-MM-DD]_v[N]\n\n## Approved platforms for client data\n- Approved: [Client data room / Firm Drive / Google Workspace (approval recorded at: [where])]\n- Not approved: [personal accounts, consumer chat tools, email attachments]\n- Codename rules: [how the client and people are referred to in prompts]\n\n## Client background\n[Industry, size (revenue, employees, geographies), strategy context, recent events]\n",
 "02_Stakeholders-and-Team": "# 02 Stakeholders and Team: [Client]\n\nLast updated: [date]\n\n## Client stakeholders\n| Name | Role | Stance (champion / supporter / neutral / skeptic / blocker) | What they care about | How to engage | Last touch |\n|---|---|---|---|---|---|\n| | Sponsor | | | | |\n| | Day-to-day counterpart | | | | |\n| | Finance lead | | | | |\n| | Data owner | | | | |\n\n## SteerCo members\n| Name | Role | Decision rights | Pre-wire needed (Y/N) |\n|---|---|---|---|\n| | | | |\n\n## Our team\n| Name | Role | Owns | Availability | Notes |\n|---|---|---|---|---|\n| | Partner | | | |\n| | Engagement manager | | | |\n| | Consultant / associate | | | |\n| | Analyst | | | |\n\n## Politics and sensitivities\n- [Who must see what first. Topics to handle with care. Prior consultant history.]\n",
 "03_Hypotheses-and-Issue-Tree": "# 03 Hypotheses and Issue Tree: [Client]\n\nLast updated: [date]\n\n## Current answer\nVersion: [Day-1 / Week-1 / Week-N]\n[Governing thought in 1 to 3 sentences.]\n\nWhat changed since the last version and why:\n- [ ]\n\n## Issue tree (indent to show levels)\n- Key question: [ ]\n  - Branch A: [ ]\n    - Leaf A1: [ ] | Hypothesis: H1 | Analysis: [ ]\n    - Leaf A2: [ ]\n  - Branch B: [ ]\n\n## Hypothesis log\n| ID | Hypothesis | Tree branch | Evidence needed | Status (Open / Testing / Supported / Weakened / Killed) | Evidence so far | Source | Confidence (High / Medium / Low) | Next step |\n|---|---|---|---|---|---|---|---|---|\n| H1 | | | | Open | | | | |\n\n## Killed or replaced hypotheses (keep; they are findings)\n| ID | Hypothesis | Why killed | Evidence | Date |\n|---|---|---|---|---|\n| | | | | |\n\n## What would have to be true for the current answer\n- [ ]\n",
 "04_Fact-Base-and-Data-Notes": "# 04 Fact Base and Data Notes: [Client]\n\nLast updated: [date]\n\n## Fact base (numbers we rely on)\n| ID | Fact or number | Value | Period | Source (file, page, person) | Confidence | Used on (slide or model cell) |\n|---|---|---|---|---|---|---|\n| F1 | | | | | | |\n\n## Data received\n| Dataset | From | Date received | Grain and period | Quality notes | Where stored (approved location) |\n|---|---|---|---|---|---|\n| | | | | | |\n\n## Data issues and open requests\n- [Issue, owner, date raised]\n\n## Assumptions (every one gets a number and an owner)\n| ID | Assumption | Value | Basis | Owner | Needs validation by |\n|---|---|---|---|---|---|\n| A1 | | | | | |\n\n## Number tie-out ledger (deck number to model cell)\n| Deck page | Number shown | Model file and cell | Matches (Y/N) | Checked by | Date |\n|---|---|---|---|---|---|\n| | | | | | |\n",
 "05_Decisions-Meetings-Interviews-Log": "# 05 Decisions, Meetings and Interviews Log: [Client]\n\nNewest entry first. Keep each entry short. Move entries older than 6 weeks to the Archive folder.\n\n## Decisions\n| Date | Decision | Made by | Why | Alternatives rejected | Reversible (Y/N) |\n|---|---|---|---|---|---|\n| | | | | | |\n\n## Meetings\n### [YYYY-MM-DD] [Meeting name]\n- Attendees: [ ]\n- Decisions: [ ]\n- Actions: [owner, due date]\n- Open questions: [ ]\n\n## Interviews\n### [YYYY-MM-DD] [Interviewee, role]\n- Top 3 takeaways: [ ]\n- Exact quotes worth using: \"[ ]\"\n- Hypotheses touched: [H#, supports or weakens]\n- Follow-ups: [ ]\n",
 "06_Storyline-and-Deck-Text": "# 06 Storyline and Deck Text: [Client]\n\nLast updated: [date]  |  Deck version: [v#]\n\n## Governing thought\n[One sentence the sponsor can repeat.]\n\n## SCQA\n- Situation: [ ]\n- Complication: [ ]\n- Question: [ ]\n- Answer: [ ]\n\n## Storyline (action titles read in order tell the story)\n1. [Action title, full sentence]\n2. [Action title]\n3. [Action title]\n\n## Latest deck text\nPaste the text of the current deck here after each major edit (slide number, title, key points, source line).\n\n### Slide 1\nTitle: [ ]\nPoints: [ ]\nSource: [ ]\n"
};

const SHEETS = {
  '10 Data Request Tracker': [
    ['ID', 'Dataset', 'Fields and grain', 'Period', 'Purpose (hypothesis or slide)', 'Client owner', 'Requested', 'Needed by', 'Received', 'Format', 'Quality', 'Location', 'Status'],
    ['D1', '', '', '', '', '', '', '', '', '', '', '', 'Draft']
  ],
  '11 Risk Register': [
    ['ID', 'Risk', 'Category (Data / Scope / People / Client / Quality / Confidentiality)', 'Likelihood (1-5)', 'Impact (1-5)', 'Score', 'Early signal', 'Mitigation', 'Owner', 'Status'],
    ['R1', '', '', '', '', '=IF(AND(ISNUMBER(D2),ISNUMBER(E2)),D2*E2,"")', '', '', '', 'Open']
  ],
  '12 Workplan': [
    ['Workstream', 'Task', 'Owner', 'Start', 'End', 'Status', 'Depends on', 'Gate', 'Hypothesis'],
    ['', '', '', '', '', 'Not started', '', '', '']
  ]
};

function createClientWorkspace() {
  const root = getOrCreateFolder_(DriveApp.getRootFolder(), ROOT_FOLDER_NAME);
  getOrCreateFolder_(root, '00_Core');
  const clients = getOrCreateFolder_(root, 'Clients');
  const client = getOrCreateFolder_(clients, CLIENT_NAME);
  const context = getOrCreateFolder_(client, '00_Context');
  const outputs = getOrCreateFolder_(client, '01_Outputs');
  getOrCreateFolder_(client, '02_Data');
  const trackers = getOrCreateFolder_(client, '03_Trackers');
  getOrCreateFolder_(client, '04_Archive');
  OUTPUT_SUBFOLDERS.forEach(function (n) { getOrCreateFolder_(outputs, n); });

  const links = [];
  Object.keys(CONTEXT_DOCS).forEach(function (key) {
    const name = key.replace(/_/g, ' ') + ' - ' + CLIENT_NAME;
    if (fileExists_(context, name)) { links.push('exists: ' + name); return; }
    const doc = DocumentApp.create(name);
    renderMarkdown_(doc.getBody(), fill_(CONTEXT_DOCS[key]));
    doc.saveAndClose();
    DriveApp.getFileById(doc.getId()).moveTo(context);
    links.push(name + ': ' + doc.getUrl());
  });

  Object.keys(SHEETS).forEach(function (key) {
    const name = key + ' - ' + CLIENT_NAME;
    if (fileExists_(trackers, name)) { links.push('exists: ' + name); return; }
    const ss = SpreadsheetApp.create(name);
    const sh = ss.getSheets()[0];
    const rows = SHEETS[key];
    sh.getRange(1, 1, rows.length, rows[0].length).setValues(rows);
    sh.getRange(1, 1, 1, rows[0].length).setFontWeight('bold').setBackground('#e8eaed');
    sh.setFrozenRows(1);
    DriveApp.getFileById(ss.getId()).moveTo(trackers);
    links.push(name + ': ' + ss.getUrl());
  });

  Logger.log('Client workspace ready: ' + client.getUrl());
  links.forEach(function (l) { Logger.log(l); });
}

function fill_(text) {
  return text.replace(/\[Client\]/g, CLIENT_NAME).replace(/\[Engagement\]/g, ENGAGEMENT_NAME);
}

function getOrCreateFolder_(parent, name) {
  const it = parent.getFoldersByName(name);
  return it.hasNext() ? it.next() : parent.createFolder(name);
}

function fileExists_(folder, name) {
  return folder.getFilesByName(name).hasNext();
}

function renderMarkdown_(body, md) {
  const lines = md.split('\n');
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (/^\|/.test(line)) {
      const rows = [];
      while (i < lines.length && /^\|/.test(lines[i])) {
        const l = lines[i];
        const isSep = /^\|[\s\-:|]+\|?\s*$/.test(l) && l.indexOf('-') > -1;
        if (!isSep) {
          rows.push(l.replace(/^\||\|\s*$/g, '').split('|').map(function (c) { return plain_(c.trim()); }));
        }
        i++;
      }
      if (rows.length) {
        const t = body.appendTable(rows);
        t.getRow(0).editAsText().setBold(true);
      }
      continue;
    }
    let m;
    if ((m = line.match(/^(#{1,3}) (.*)$/))) {
      const h = [DocumentApp.ParagraphHeading.HEADING1, DocumentApp.ParagraphHeading.HEADING2, DocumentApp.ParagraphHeading.HEADING3][m[1].length - 1];
      body.appendParagraph(plain_(m[2])).setHeading(h);
    } else if ((m = line.match(/^(\s*)- (.*)$/))) {
      body.appendListItem(plain_(m[2])).setGlyphType(DocumentApp.GlyphType.BULLET).setNestingLevel(Math.min(Math.floor(m[1].length / 2), 3));
    } else if ((m = line.match(/^\d+\. (.*)$/))) {
      body.appendListItem(plain_(m[1])).setGlyphType(DocumentApp.GlyphType.NUMBER);
    } else if (line.trim() === '') {
      // skip blank lines
    } else {
      body.appendParagraph(plain_(line.replace(/^> ?/, '')));
    }
    i++;
  }
  const first = body.getChild(0);
  if (first.getType() === DocumentApp.ElementType.PARAGRAPH && first.asParagraph().getText() === '' && body.getNumChildren() > 1) {
    first.removeFromParent();
  }
}

function plain_(s) {
  return s.replace(/\*\*/g, '').replace(/`/g, '');
}
