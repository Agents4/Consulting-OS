#!/usr/bin/env python3
"""Fail if lines added since BASE contain an em dash or a banned word.

Usage: python3 scripts/check_voice.py [BASE_REF]   (default: origin/main)

Checks hand-written markdown only. Generated files (GEMINI.md, skills/,
commands/, knowledge packs) inherit from the sources, so they are skipped.
Only added lines are checked, so old text never blocks a new change.
"""
import re
import subprocess
import sys

BANNED = ["delve", "leverage", "utilize", "unlock", "harness", "streamline", "robust", "cutting-edge"]
PATHS = [".claude/skills", "setup", "templates", "evals", "sub-agents", "advanced",
         "README.md", "CLAUDE.md"]
EM_DASH = "—"


def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
    out = subprocess.run(
        ["git", "diff", "-U0", f"{base}...HEAD", "--", *PATHS],
        capture_output=True, text=True, check=True).stdout
    word = re.compile(r"\b(" + "|".join(re.escape(w) for w in BANNED) + r")(s|d|ed|ing|es)?\b", re.I)
    path, bad = "", []
    for line in out.splitlines():
        if line.startswith("+++ "):
            path = line[6:] if line.startswith("+++ b/") else ""
        elif line.startswith("+") and not line.startswith("+++") and path.endswith(".md"):
            text = line[1:]
            if EM_DASH in text:
                bad.append((path, "em dash", text.strip()[:120]))
            m = word.search(text)
            if m:
                bad.append((path, f"banned word '{m.group(0)}'", text.strip()[:120]))
    for p, why, t in bad:
        print(f"{p}: {why}: {t}")
    print(f"voice check: {len(bad)} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
