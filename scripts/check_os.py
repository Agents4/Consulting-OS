#!/usr/bin/env python3
"""Checks Consulting-OS before you commit: skills, voice rules, links, manifest, counts, generated files.

Run from anywhere: python3 scripts/check_os.py
Exit code is 1 when there are errors. Standard library only.
"""
import filecmp, glob, json, os, re, shutil, subprocess, sys, tempfile

ROOT = os.environ.get("OS_ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
BANNED = ["delve", "leverage", "utilize", "unlock", "harness", "streamline", "robust", "cutting-edge"]
ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools",
                "disable-model-invocation", "user-invocable"}
errors, warns = [], []


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def rel(p):
    return os.path.relpath(p, ROOT)


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return (m.group(1), text[m.end():]) if m else (None, text)


def voice_hits(text):
    """Em dashes and banned words. A line that lists the banned words as a rule is exempt."""
    hits = []
    for i, line in enumerate(text.split("\n"), 1):
        if re.search(r"none of delve|Never: delve|never use.*delve", line, re.I):
            continue
        if "—" in line:
            hits.append((i, "em dash"))
        for w in BANNED:
            if re.search(rf"(?<![\w-]){re.escape(w)}(?![\w-])", line, re.I):
                hits.append((i, f"banned word '{w}'"))
    return hits


# ------------------------------------------------------------------ skills
skill_dirs = sorted(d for d in glob.glob(os.path.join(ROOT, ".claude", "skills", "*")) if os.path.isdir(d))
names = set()
for d in skill_dirs:
    folder = os.path.basename(d)
    sp = os.path.join(d, "SKILL.md")
    if not os.path.isfile(sp):
        errors.append(f"{rel(d)}: no SKILL.md")
        continue
    text = read(sp)
    fm, body = split_frontmatter(text)
    if fm is None:
        errors.append(f"{rel(sp)}: no frontmatter")
        continue
    keys = re.findall(r"(?m)^([A-Za-z][\w-]*):", fm)
    for k in keys:
        if k not in ALLOWED_KEYS:
            warns.append(f"{rel(sp)}: unknown frontmatter key '{k}'")
    nm = re.search(r"(?m)^name:\s*(.+)$", fm)
    ds = re.search(r"(?m)^description:\s*(.+)$", fm)
    if not nm or nm.group(1).strip() != folder:
        errors.append(f"{rel(sp)}: name must equal the folder name '{folder}'")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", folder) or len(folder) > 64:
        errors.append(f"{rel(sp)}: folder name must be lowercase letters, digits, single hyphens, 64 characters at most")
    names.add(folder)
    if not ds:
        errors.append(f"{rel(sp)}: description is missing")
        continue
    raw = ds.group(1).strip()
    if raw.startswith('"'):
        try:
            desc = json.loads(raw)
        except ValueError:
            errors.append(f"{rel(sp)}: quoted description is not valid (escape inner quotes with a backslash)")
            desc = raw
    else:
        desc = raw
        if ": " in raw or " #" in raw or raw[:1] in "[{&*!|>%@`'":
            errors.append(f"{rel(sp)}: quote the description. Strict YAML parsers reject an unquoted ': ' and skip the skill")
    if len(desc) > 1024:
        errors.append(f"{rel(sp)}: description is {len(desc)} characters; the limit is 1024")
    for i, what in voice_hits(desc):
        errors.append(f"{rel(sp)}: description has {what}")
    for i, what in voice_hits(body):
        errors.append(f"{rel(sp)}:{i + fm.count(chr(10)) + 3}: {what}")
    n = text.count("\n")
    if n > 500:
        errors.append(f"{rel(sp)}: {n} lines; the limit is 500")
    elif n > 250:
        warns.append(f"{rel(sp)}: {n} lines; consider moving detail to a reference file")

# ------------------------------------------------------------------ slash links
KNOWN_NON_SKILLS = {"engagement-init"}
for f in [os.path.join(ROOT, "CLAUDE.md")] + [os.path.join(d, "SKILL.md") for d in skill_dirs]:
    if not os.path.isfile(f):
        continue
    for tok in sorted(set(re.findall(r"`/([a-z][a-z0-9]*(?:-[a-z0-9]+)+)`", read(f)))):
        if tok not in names and tok not in KNOWN_NON_SKILLS:
            errors.append(f"{rel(f)}: refers to /{tok}, which is not a skill")

# ------------------------------------------------------------------ manifest
man = None
mp = os.path.join(ROOT, "os.manifest.json")
if not os.path.isfile(mp):
    errors.append("os.manifest.json is missing")
else:
    try:
        man = json.loads(read(mp))
    except ValueError as e:
        errors.append(f"os.manifest.json: invalid JSON ({e})")
if man:
    for key in ("manifest_version", "name", "rules_file", "skills", "commands"):
        if key not in man:
            errors.append(f"os.manifest.json: missing '{key}'")
    for k in ("validate", "build"):
        if k not in man.get("commands", {}):
            errors.append(f"os.manifest.json: commands.{k} is required")
    for p in (man.get("rules_file"), man.get("skills", {}).get("source")):
        if p and not os.path.exists(os.path.join(ROOT, p)):
            errors.append(f"os.manifest.json: path '{p}' does not exist")
    # registries
    for reg in man.get("registries", []):
        kind, f = reg.get("check"), reg.get("file", "")
        if not kind:
            continue
        fp = os.path.join(ROOT, f)
        if not os.path.isfile(fp):
            errors.append(f"registry {f}: file not found")
            continue
        text = read(fp)
        if kind == "lists_skills":
            skip = set(reg.get("except", []))
            missing = [n for n in sorted(names - skip) if not re.search(rf"(?<![\w-]){re.escape(n)}(?![\w-])", text)]
            if missing:
                errors.append(f"registry {f}: does not mention {', '.join(missing)}. {reg.get('update', '')}")
        else:
            warns.append(f"registry {f}: unknown check '{kind}'")
    # counts
    n = len(names)
    for c in man.get("counts", []):
        f = c["file"]
        fp = os.path.join(ROOT, f)
        if not os.path.isfile(fp):
            errors.append(f"counts: {f} not found")
            continue
        m = re.fullmatch(r"n([+-]\d+)?", c["expect"])
        want = n + (int(m.group(1)) if m and m.group(1) else 0)
        found = re.findall(c["pattern"], read(fp))
        if not found:
            errors.append(f"counts: {f}: pattern {c['pattern']!r} found nothing (text changed? update os.manifest.json)")
        for v in sorted(set(found), key=str):
            if int(v) != want:
                errors.append(f"counts: {f} says {v} for {c['pattern']!r}; expected {want}")

# ------------------------------------------------------------------ generated files
def tree_diff(a, b):
    out = []
    for dp, dirs, files in os.walk(a):
        for fn in files:
            pa = os.path.join(dp, fn)
            pb = os.path.join(b, os.path.relpath(pa, a))
            if not os.path.isfile(pb):
                out.append(f"missing {rel(pb)}")
            elif not filecmp.cmp(pa, pb, shallow=False):
                out.append(f"changed {rel(pb)}")
    for dp, dirs, files in os.walk(b):
        for fn in files:
            pb = os.path.join(dp, fn)
            if not os.path.isfile(os.path.join(a, os.path.relpath(pb, b))):
                out.append(f"stale {rel(pb)}")
    return out


tmp = tempfile.mkdtemp(prefix="cos-check-")
try:
    shutil.copytree(os.path.join(ROOT, ".claude"), os.path.join(tmp, ".claude"))
    shutil.copy(os.path.join(ROOT, "CLAUDE.md"), tmp)
    shutil.copytree(os.path.join(ROOT, "gemini", "tools"), os.path.join(tmp, "gemini", "tools"))
    os.makedirs(os.path.join(tmp, "advanced"), exist_ok=True)
    shutil.copytree(os.path.join(ROOT, "scripts"), os.path.join(tmp, "scripts"))
    r = subprocess.run([sys.executable, os.path.join(tmp, "gemini", "tools", "build_extension.py")],
                       capture_output=True, text=True, env={**os.environ, "OS_ROOT": tmp})
    if r.returncode != 0:
        errors.append("build_extension.py failed: " + (r.stderr.strip().splitlines() or ["unknown error"])[-1])
    else:
        drift = []
        for d in ("skills", "commands"):
            drift += tree_diff(os.path.join(tmp, d), os.path.join(ROOT, d))
        for f in ("GEMINI.md", "gemini-extension.json"):
            if read(os.path.join(tmp, f)) != read(os.path.join(ROOT, f)):
                drift.append(f"changed {f}")
        if drift:
            errors.append("generated extension files are out of date (run python3 gemini/tools/build_extension.py): " + "; ".join(drift[:5]) + (" ..." if len(drift) > 5 else ""))
    bundle_tmp = os.path.join(tmp, "bundle.zip")
    r = subprocess.run([sys.executable, os.path.join(tmp, "scripts", "build_bundle.py"), bundle_tmp],
                       capture_output=True, text=True, env={**os.environ, "OS_ROOT": ROOT})
    cur = os.path.join(ROOT, "advanced", "skills-bundle.zip")
    if r.returncode != 0:
        errors.append("build_bundle.py failed: " + (r.stderr.strip().splitlines() or ["unknown error"])[-1])
    elif not os.path.isfile(cur) or open(cur, "rb").read() != open(bundle_tmp, "rb").read():
        errors.append("advanced/skills-bundle.zip is out of date (run python3 scripts/build_bundle.py)")
finally:
    shutil.rmtree(tmp, ignore_errors=True)

# ------------------------------------------------------------------ evals
cases = os.path.join(ROOT, "evals", "cases")
covered = set()
if os.path.isdir(cases):
    for c in sorted(glob.glob(os.path.join(cases, "*"))):
        if not os.path.isdir(c):
            continue
        ip, ep = os.path.join(c, "input.md"), os.path.join(c, "expected.md")
        if not (os.path.isfile(ip) and os.path.isfile(ep)):
            errors.append(f"eval {os.path.basename(c)}: needs input.md and expected.md")
            continue
        m = re.match(r"Skill:\s*([a-z0-9-]+)", read(ep))
        if not m:
            errors.append(f"eval {os.path.basename(c)}: expected.md must start with 'Skill: <name>'")
        elif m.group(1) not in names:
            errors.append(f"eval {os.path.basename(c)}: skill '{m.group(1)}' does not exist")
        else:
            covered.add(m.group(1))
else:
    warns.append("no evals/cases folder")
if covered:
    warns.append(f"evals: {len(covered)} of {len(names)} skills have a case")

for w in warns:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"{len(names)} skills checked: {len(errors)} errors, {len(warns)} warnings")
sys.exit(1 if errors else 0)
