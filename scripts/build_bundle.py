#!/usr/bin/env python3
"""Rebuilds advanced/skills-bundle.zip (one folder per skill, for upload to Claude.ai).

Reads:  .claude/skills/<name>/ (every file in each skill folder)
Writes: advanced/skills-bundle.zip
Run from anywhere: python3 scripts/build_bundle.py
"""
import os, sys, zipfile

ROOT = os.environ.get("OS_ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SRC = os.path.join(ROOT, ".claude", "skills")
OUT = os.path.join(ROOT, "advanced", "skills-bundle.zip")
FIXED = (2026, 1, 1, 0, 0, 0)   # fixed timestamps keep the zip identical between runs


def entries():
    for name in sorted(os.listdir(SRC)):
        d = os.path.join(SRC, name)
        if not os.path.isdir(d) or not os.path.isfile(os.path.join(d, "SKILL.md")):
            continue
        yield name + "/", None
        for dirpath, dirs, files in os.walk(d):
            dirs.sort()
            for f in sorted(files):
                if f == ".DS_Store":
                    continue
                p = os.path.join(dirpath, f)
                yield os.path.relpath(p, SRC).replace(os.sep, "/"), p


def build(path):
    n = 0
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for arc, p in entries():
            info = zipfile.ZipInfo(arc, FIXED)
            if p is None:
                info.external_attr = 0o40755 << 16
                z.writestr(info, b"")
            else:
                info.external_attr = 0o100644 << 16
                z.writestr(info, open(p, "rb").read(), zipfile.ZIP_DEFLATED)
                n += 1
    return n


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT
    print(f"wrote {os.path.relpath(out, ROOT) if out.startswith(ROOT) else out}: {build(out)} files")
