#!/usr/bin/env bash
# Scaffolds the current folder as a Consulting OS engagement workspace.
# Copies starter templates from the extension. Never overwrites an existing file.
set -eu
EXT="$(cd "$(dirname "$0")/.." && pwd)"
WS="$(pwd)"
created=0; kept=0

mk() { if [ -d "$1" ]; then :; else mkdir -p "$1"; fi; }
cp_new() {
  if [ -e "$2" ]; then kept=$((kept+1)); echo "exists:  $2"
  else cp "$1" "$2"; created=$((created+1)); echo "created: $2"; fi
}

for d in engagements stakeholders hypotheses interviews models decks decisions meetings research data client-materials other; do
  mk "$WS/context-library/$d"
done
for d in proposals problem-statements kickoff stakeholder-maps workplans data-requests issue-trees hypotheses interviews research-synthesis analyses models storylines ghost-decks decks reviews steerco status-updates meeting-notes decisions recommendations roadmaps transition retros daily-plans weekly-plans weekly-reviews team-messages workshops skill-test-results; do
  mk "$WS/outputs/$d"
done

for f in engagement-info-template.md client-stakeholder-template.md team-roster-template.md consulting-os-learning-log.md; do
  [ -f "$EXT/context-library/$f" ] && cp_new "$EXT/context-library/$f" "$WS/context-library/$f"
done
for f in "$EXT"/context-library/writing-style-*.md "$EXT"/context-library/personal-context-*.md; do
  [ -f "$f" ] && cp_new "$f" "$WS/context-library/$(basename "$f")"
done

echo
echo "Workspace: $WS"
echo "Created $created file(s), kept $kept existing."
echo "Next: fill context-library/engagement-info-template.md, then run /problem-statement or /day-one-answer."
echo "Client data: keep context-library/data and client-materials out of git and on approved platforms."
