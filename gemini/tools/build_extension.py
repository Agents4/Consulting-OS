#!/usr/bin/env python3
"""Builds the Gemini CLI extension files at the repo root from the Claude Code skills.

Reads:   .claude/skills/*/SKILL.md, CLAUDE.md
Writes:  gemini-extension.json, GEMINI.md, skills/, commands/
Run from anywhere: python3 gemini/tools/build_extension.py
Re-run after you change a skill or CLAUDE.md, then bump "version" in gemini-extension.json.
"""
import glob, json, os, re, shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
NAME = "consulting-os"
VERSION = "1.2.0"
EXT = f"~/.gemini/extensions/{NAME}"
EXCLUDE = {"connect-mcps", "google-workspace-output"}   # Claude connector specific

def read(p): return open(p, encoding="utf-8").read()
def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(s)

CORE_CTX = ["context-library/frameworks/", "context-library/engagement-model/", "context-library/example-engagements/"]
def rewrite_paths(t):
    for d in CORE_CTX:
        t = t.replace(d, f"{EXT}/{d}")
    t = re.sub(r"(?<![\w/.~-])(templates/|sub-agents/|advanced/)", EXT + r"/\1", t)
    return t

WEB_SKILLS = {"research-plan", "competitive-landscape", "market-sizing", "benchmark-analysis"}

def convert_skill(src):
    s = read(src)
    m = re.match(r"^---\n(.*?)\n---\n", s, re.S)
    fm = m.group(1); body = s[m.end():]
    name = re.search(r"^name:\s*(.+)$", fm, re.M).group(1).strip()
    desc = re.search(r"^description:\s*(.+)$", fm, re.M).group(1).strip()
    # drop Output Format Options (Google connector routes) and Claude-only bits
    parts = re.split(r"(?m)^(?=## )", body)
    parts = [p for p in parts if not p.startswith("## Output Format Options")]
    body = "".join(parts)
    body = re.sub(r"(?m)^.*google-workspace-(output|option).*\n", "", body)
    body = body.replace("(Internal - for Claude)", "(Internal - for Gemini)")
    body = re.sub(r"\bClaude\b", "Gemini", body)
    body = rewrite_paths(body)
    note = (f"> Extension note: core files (frameworks, engagement model, templates, sub-agents) are in `{EXT}/`. "
            "Engagement files (context-library/engagements, stakeholders, data, etc.) and all new outputs live in the current workspace folder.\n\n")
    if name in WEB_SKILLS:
        note += ("> Web research: search with the `google_web_search` tool and read pages with the `web_fetch` tool. "
                 "Wherever this skill says web search, WebSearch, or WebFetch, use those two tools. "
                 "If `web_fetch` cannot load a page, log it as unreachable and ask the user for the file. Do not work around it.\n\n")
    body = re.sub(r"(?m)^(# .+\n)", r"\1\n" + note.replace("\\", "\\\\"), body, count=1)
    return name, desc, f"---\nname: {name}\ndescription: {json.dumps(desc, ensure_ascii=False)}\n---\n{body}"

def toml_str(s): return json.dumps(s, ensure_ascii=False)

# --- skills and commands
for d in ("skills", "commands"):
    shutil.rmtree(os.path.join(ROOT, d), ignore_errors=True)
count = 0
for src in sorted(glob.glob(ROOT + "/.claude/skills/*/SKILL.md")):
    name, desc, out = convert_skill(src)
    if name in EXCLUDE: continue
    write(f"{ROOT}/skills/{name}/SKILL.md", out)
    cmd = (f"description = {toml_str(desc)}\n"
           'prompt = """\n'
           f"Activate the `{name}` skill with the activate_skill tool and follow it step by step for this task.\n\n"
           "Task details from the user (may be empty):\n{{args}}\n"
           '"""\n')
    write(f"{ROOT}/commands/{name}.toml", cmd)
    count += 1

write(f"{ROOT}/commands/engagement-init.toml",
 'description = "Set up the current folder as an engagement workspace: context-library, outputs, and starter templates."\n'
 'prompt = """\n'
 "Set up this folder as a Consulting OS engagement workspace. Here is the result of the setup script:\n\n"
 f'!{{bash "$HOME/.gemini/extensions/{NAME}/scripts/init-workspace.sh"}}\n\n'
 "Now do two things. First, summarize what was created and what already existed. Second, give me the next three steps from Getting Started in the Consulting OS context, and ask me the first question: what is the key question for this engagement?\n"
 '"""\n')
count_cmds = count + 1

# --- GEMINI.md from CLAUDE.md
c = read(ROOT + "/CLAUDE.md")
c = c.replace("# CLAUDE: Consulting OS", "# Consulting OS (Gemini CLI extension)")
c = re.sub(r"(?m)^You are the AI copilot", "You are the AI copilot", c)
# skills section
c = re.sub(r"\d+ skills in `\.claude/skills/<name>/SKILL\.md`\. They load on demand and check workspace context and connected MCPs automatically\.",
           f"{count} skills ship with this extension. Gemini activates a skill when a task matches it, and every skill is also a slash command (for example `/issue-tree`). Skills check workspace context and connected tools automatically. `/engagement-init` scaffolds a new engagement folder.", c)
c = c.replace(" `/connect-mcps`", "")
c = re.sub(r"\n\*\*Google formats:\*\*[^\n]*\n", "\n", c)
# MCP section
c = re.sub(r"(?s)## MCPs\n.*?(?=\*\*Query routing:\*\*)",
           "## Connected tools\n\nAll skills work without connected tools. To add live access, install an extension such as Google Workspace (`gemini extensions install https://github.com/gemini-cli-extensions/workspace`) or add an MCP server in `settings.json`. Confirm client IT approval before connecting anything that touches client data. Ask before using any connected tool on client data.\n\n**Connected:** _None yet._\n\n", c)
# file creation
c = re.sub(r"\*\*CRITICAL: Claude writes ALL new files[^\n]*",
           "**CRITICAL: Write ALL new files to `outputs/` in the user's current workspace folder. Never write to `context-library/` directly, and never write inside the extension folder. The user moves finalized work into `context-library/` manually.** Exceptions, each only with the user's explicit approval: the learning log, and `/ingest-materials` updates to named workspace `context-library/` files (approved one file at a time, with a backup of the original saved in `outputs/` first).", c)
c = re.sub(r"\*\*Templates:\*\* `templates/`[^\n]*", f"**Templates:** `{EXT}/templates/` holds working templates including `model-starter-template.xlsx` and `ghost-deck-starter.pptx`. Copy them into `outputs/` and work on the copy.", c)
c = re.sub(r"\*\*Google option:\*\*[^\n]*\n\n\*\*Gemini option:\*\*[^\n]*\n\n\*\*Copilot option:\*\*[^\n]*\n",
           "**Google formats:** Build models and decks as .xlsx and .pptx in `outputs/`. To get Google Sheets or Slides, upload the files to Drive and open them with Google Sheets or Slides. Use Google for client data only with the client's written approval. Share with named people only.\n", c)
c = c.replace("**Building files:** Check **Preferred output formats** in engagement info first. Default is Office.", "**Building files:** Check **Preferred output formats** in engagement info first. Default is Office (xlsx, pptx, docx).")
# sub-agents
c = c.replace("For multi-perspective review, use `sub-agents/`:", f"For multi-perspective review, read the persona files in `{EXT}/sub-agents/`:")
# getting started
c = re.sub(r"(?s)## Getting Started\n.*?(?=Read `context-library/engagement-model/00-overview.md`)",
           "## Getting Started\n\nIn the folder for the engagement, run `/engagement-init`. It creates `context-library/` and `outputs/` and copies the starter templates. Then:\n1. Fill `context-library/engagement-info-template.md`, `client-stakeholder-template.md`, and `team-roster-template.md`\n2. Add personal context (`personal-context-*.md`) and pick or edit a writing style\n3. Drop existing client materials, data, and past work into `context-library/` subfolders\n4. Choose output formats (Office or Google) in engagement info\n5. First action: `/problem-statement`, `/kickoff-plan`, or `/day-one-answer`\n\n", c)
c = c.replace("Read `context-library/engagement-model/00-overview.md` once", f"Read `{EXT}/context-library/engagement-model/00-overview.md` once")
c = c.replace("Everything works without MCPs. They add live data access, not core functionality.", "Everything works without connected tools. They add live data access, not core functionality.")
c = c.replace("Claude", "Gemini")
for bad in ("`.claude/skills", "Gemini writes ALL new files", "/connect-mcps"):
    assert bad not in c, f"GEMINI.md substitution failed: {bad}"

pathblock = f"""## Where files live (read this first)

This extension is installed at `{EXT}/`. The user's engagement files live in the current workspace folder.

- **Core files, read from the extension:** `{EXT}/context-library/frameworks/`, `{EXT}/context-library/engagement-model/`, `{EXT}/context-library/example-engagements/`, `{EXT}/templates/`, `{EXT}/sub-agents/`, `{EXT}/advanced/`.
- **Engagement files, read from the workspace:** `context-library/engagements/`, `stakeholders/`, `hypotheses/`, `interviews/`, `models/`, `decks/`, `decisions/`, `meetings/`, `research/`, `data/`, `client-materials/`, and the engagement-info, stakeholder, and team-roster files.
- **Writing styles and personal context:** use the workspace copy of `context-library/writing-style-*.md` and `personal-context-*.md` if it exists. Otherwise read the copy in the extension.
- **New files:** always `outputs/` in the workspace. If the workspace has no `context-library/` yet, suggest `/engagement-init`.
- Where a skill says `context-library/frameworks/...`, `templates/...` or `sub-agents/...`, it means the extension copy and the path is already absolute.

"""
c = c.replace("## Context First", pathblock + "## Context First", 1)
write(ROOT + "/GEMINI.md", c)

# --- manifest
manifest = {
  "name": NAME,
  "version": VERSION,
  "description": f"Consulting OS: an MBB-style strategy engagement copilot with {count} skills and slash commands, review personas, frameworks, and model and deck templates.",
  "contextFileName": "GEMINI.md",
}
write(ROOT + "/gemini-extension.json", json.dumps(manifest, indent=2) + "\n")
print(f"skills: {count}, commands: {count_cmds}")
