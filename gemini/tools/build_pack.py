import re, glob, os, subprocess, sys
# Rebuilds gemini/knowledge-pack from the skills, engagement model and frameworks. Needs pandoc.
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
TARGET = sys.argv[1] if len(sys.argv) > 1 else "gemini"   # gemini or copilot
OUT = ROOT + ("/copilot/knowledge-pack" if TARGET == "copilot" else "/gemini/knowledge-pack")
DELIVER = ("Delivered in chat. Copy into Word or Excel and file in the client Outputs folder." if TARGET == "copilot" else "Delivered in chat. Export to Google Docs or Sheets and file in the client Outputs folder.")
os.makedirs(OUT, exist_ok=True)

def read(p): return open(p, encoding="utf-8").read()

def demote(md, n=1):
    # shift headings down n levels (outside code fences)
    out, fence = [], False
    for line in md.split("\n"):
        if line.startswith("```"): fence = not fence
        if not fence and re.match(r"^#{1,5} ", line):
            line = "#" * n + line
        out.append(line)
    return "\n".join(out)

def clean_refs(t):
    t = t.replace("`templates/model-starter-template.xlsx`", "the model starter template (inputs, calc, scenarios, outputs, checks, log tabs)")
    t = t.replace("`context docs/interviews/`", "the client Context folder")
    t = t.replace("`outputs/", "`Client folder 01_Outputs/")
    t = t.replace("outputs/", "01_Outputs/")
    t = t.replace("context-library/", "context docs/")
    return t

def doc_section(path):
    return demote(clean_refs(read(path)), 1)

def skill_to_playbook(path):
    s = read(path)
    s = re.sub(r"^---\n.*?\n---\n", "", s, count=1, flags=re.S)
    name = os.path.basename(os.path.dirname(path))
    # drop Context Routing Logic and Step 0 sections (Gem reads the knowledge files itself)
    parts = re.split(r"(?m)^(?=## )", s)
    kept = []
    for p in parts:
        if re.match(r"## Context Routing Logic", p) or re.match(r"## Step 0", p):
            continue
        kept.append(p)
    s = "".join(kept)
    # drop Output Format Options entirely; trim Output Integration to cross-skill links
    parts = re.split(r"(?m)^(?=## )", s)
    kept = []
    for p in parts:
        if p.startswith("## Output Format Options"):
            continue
        if p.startswith("## Output Integration"):
            sub = re.split(r"(?m)^(?=### )", p)
            sub = [x for x in sub if not x.startswith("### Where to Save") and not x.startswith("### Handoff Format")]
            p = "".join(sub).rstrip() + "\n\nWhen this output goes to a teammate or reviewer, attach a handoff cover note: Brief, Backup, So-what, Ask. Never send a page without all four.\n\n---\n\n"
        kept.append(p)
    s = "".join(kept)
    s = re.sub(r"(?m)^- \[ \] \*\*Saved\*\*.*\n", "", s)
    # framework source line: drop file paths
    s = re.sub(r"[ \t]*\|?[ \t]*\*\*Framework source:\*\*[^\n]*", "", s)
    s = re.sub(r"(?m)\|\s*$", lambda m: m.group(0), s)
    # quick start slash command block -> plain trigger phrase
    s = re.sub(r"```\n/" + re.escape(name) + r"[^\n]*\n```", f"Say: **Run the {name} playbook**", s)
    s = re.sub(r"(?m)^\*\*Output:\*\*.*$", "**Output:** " + DELIVER, s)
    s = re.sub(r"(?m)^\s*-?\s*`/([a-z0-9-]+)`", lambda m: f"- the {m.group(1)} playbook", s)
    s = re.sub(r"`/([a-z0-9-]+)`", r"the \1 playbook", s)
    s = re.sub(r"(?<![\w/])/([a-z]+(?:-[a-z]+)+)\b", r"the \1 playbook", s)
    s = clean_refs(s)
    s = re.sub(r"^# ", f"# PLAYBOOK: {name}\n\n# ", s, count=1) if False else s
    s = re.sub(r"^# (.*)$", rf"# Playbook: \1 (name: {name})", s, count=1, flags=re.M)
    return demote(s, 1)

def write(name, title, intro, body):
    md = f"# {title}\n\n{intro}\n\n{body}\n"
    p_md = f"{OUT}/{name}.md"
    open(p_md, "w", encoding="utf-8").write(md)
    p_docx = f"{OUT}/{name}.docx"
    subprocess.run(["pandoc", p_md, "-f", "markdown-smart", "-o", p_docx], check=True)
    print(name, len(md)//1024, "KB md,", os.path.getsize(p_docx)//1024, "KB docx")

EM = ROOT + "/context-library/engagement-model/"
FW = ROOT + "/context-library/frameworks/"
CL = ROOT + "/context-library/"


EM = ROOT + "/context-library/engagement-model/"
FW = ROOT + "/context-library/frameworks/"
CL = ROOT + "/context-library/"
em_files = ["00-overview","01-roles-and-team-structure","02-skills-by-role","03-engagement-lifecycle","04-tasks-by-phase","05-cadence-and-handoffs","08-support-functions-and-tools","09-ai-in-consulting-2026","10-glossary"]
std = [EM+"06-deliverable-production-decks.md", EM+"07-excel-modeling-standards.md"] + sorted(glob.glob(CL+"writing-style-*.md"))
fw_files = sorted(glob.glob(FW+"*.md"))
def sect(title, files): return f"# {title}\n\n" + "\n\n".join(doc_section(f) for f in files)
body = sect("Part 1: How an engagement runs", [EM+f+".md" for f in em_files]) + "\n\n" + sect("Part 2: Frameworks", fw_files) + "\n\n" + sect("Part 3: Deck, model and writing standards", std)
write("CORE-1_Engagement-Model-Frameworks-Standards", "Consulting OS Core 1: Engagement Model, Frameworks and Standards",
      "Roles, lifecycle, tasks, cadence and handoffs, frameworks, deck and model standards, voice by audience. Shared across all clients. Reference only. Client facts live in the client context docs.", body)
order_a = ["proposal-draft","problem-statement","kickoff-plan","stakeholder-map","workplan-build","data-request","ingest-materials","day-one-answer","issue-tree","hypothesis-draft","prioritize-analyses","interview-guide","interview-synthesis","survey-design","fact-base","data-exploration","market-sizing","benchmark-analysis","competitive-landscape","value-driver-tree","root-cause-analysis"]
order_b = ([x for x in ["initiative-sizing","model-spec","model-build","model-audit","scenario-sensitivity","number-tie-out","options-evaluation","recommendation","roadmap-build","change-plan","storyline","ghost-deck","slide-draft","exec-summary","deck-qc","final-readout"]] if TARGET == "copilot" else None) or ["initiative-sizing","model-spec","model-build","model-audit","scenario-sensitivity","number-tie-out","options-evaluation","recommendation","roadmap-build","change-plan","storyline","ghost-deck","slide-draft","exec-summary","deck-qc","final-readout","google-workspace-output"]
order_c = ["daily-plan","weekly-plan","weekly-review","status-update","steerco-prep","partner-session-prep","handoff-brief","meeting-agenda","meeting-notes","decision-doc","risk-register","client-update-email","engagement-health-check","review-panel","handover-pack","retrospective","knowledge-capture"]
allskills = {os.path.basename(os.path.dirname(p)) for p in glob.glob(ROOT+"/.claude/skills/*/SKILL.md")}
print("unassigned:", allskills - set(order_a+order_b+order_c))
ING_NOTE = ("\n\n## How this playbook works in " + ("Copilot" if TARGET == "copilot" else "Gemini") + "\n\n"
  + ("Add each new file to the Notebook as a reference, then say: Run the ingest-materials playbook on [file names]. " if TARGET == "copilot" else "Upload the new file to the Gem's Knowledge (or attach it in chat), then say: Run the ingest-materials playbook on [file names]. ")
  + "There is no file hashing here. Treat a file as new when its name and modified date are not in the ingest index doc. Read each file as provided, write one digest per file, and end with the update proposal (U1, U2 and so on). "
  + "I cannot write to your files, so each approved update comes back as a CONTEXT UPDATES block: the target context doc, the section, and the exact text to paste. Paste approved updates yourself, then add the ingested files to the ingest index doc.\n\n---\n\n")
def pb(order): return "\n\n".join(skill_to_playbook(f"{ROOT}/.claude/skills/{n}/SKILL.md") + (ING_NOTE if n == "ingest-materials" else "") for n in order)
intro = "Each playbook is one task. In " + ("Copilot" if TARGET == "copilot" else "Gemini") + ", trigger one by saying: Run the [name] playbook. Follow its questions, process and template. Deliver in chat."
write("CORE-2_Playbooks-Mobilize-to-Diagnose", "Consulting OS Core 2: Playbooks, Mobilize to Diagnose", intro, pb(order_a))
write("CORE-3_Playbooks-Model-Deck-Rhythm-Close", "Consulting OS Core 3: Playbooks, Model, Recommend, Deck, Rhythm and Close", intro,
      "# Section A: Model, recommend, storyline and deck\n\n" + pb(order_b) + "\n\n# Section B: Rhythm, governance and close\n\n" + pb(order_c))
