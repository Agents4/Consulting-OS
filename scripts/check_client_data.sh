#!/usr/bin/env bash
# Fail if the change adds client data. Usage: scripts/check_client_data.sh [BASE_REF]
set -euo pipefail
base="${1:-origin/main}"
bad=$(git diff --name-only --diff-filter=AM "$base"...HEAD -- \
  'context-library/data' 'context-library/client-materials' | grep -v '/\.gitkeep$' || true)
if [ -n "$bad" ]; then
  echo "Client data must not be committed:"; echo "$bad"; exit 1
fi
echo "client data check: clean"
