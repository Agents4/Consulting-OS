import json, glob, os
# Rebuilds apps-script/NewClientWorkspace.gs from the client-kit markdown files.
G = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
docs = {os.path.basename(p)[:-3]: open(p, encoding="utf-8").read() for p in sorted(glob.glob(G + "/client-kit/*.md"))}
js = '''/**
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

const CONTEXT_DOCS = ''' + json.dumps(docs, indent=1, ensure_ascii=False) + ''';

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
  return text.replace(/\\[Client\\]/g, CLIENT_NAME).replace(/\\[Engagement\\]/g, ENGAGEMENT_NAME);
}

function getOrCreateFolder_(parent, name) {
  const it = parent.getFoldersByName(name);
  return it.hasNext() ? it.next() : parent.createFolder(name);
}

function fileExists_(folder, name) {
  return folder.getFilesByName(name).hasNext();
}

function renderMarkdown_(body, md) {
  const lines = md.split('\\n');
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (/^\\|/.test(line)) {
      const rows = [];
      while (i < lines.length && /^\\|/.test(lines[i])) {
        const l = lines[i];
        const isSep = /^\\|[\\s\\-:|]+\\|?\\s*$/.test(l) && l.indexOf('-') > -1;
        if (!isSep) {
          rows.push(l.replace(/^\\||\\|\\s*$/g, '').split('|').map(function (c) { return plain_(c.trim()); }));
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
    } else if ((m = line.match(/^(\\s*)- (.*)$/))) {
      body.appendListItem(plain_(m[2])).setGlyphType(DocumentApp.GlyphType.BULLET).setNestingLevel(Math.min(Math.floor(m[1].length / 2), 3));
    } else if ((m = line.match(/^\\d+\\. (.*)$/))) {
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
  return s.replace(/\\*\\*/g, '').replace(/`/g, '');
}
'''
open(G + "/apps-script/NewClientWorkspace.gs", "w", encoding="utf-8").write(js)
print(len(js))
