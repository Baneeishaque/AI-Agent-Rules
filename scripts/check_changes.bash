#!/bin/bash
# Check if specific files have changed and set step output

set -euo pipefail

if [[ -n $(git status --porcelain README.md agent-rules.md) ]]; then
  echo "has_changes=true" >> "$GITHUB_OUTPUT"
else
  echo "has_changes=false" >> "$GITHUB_OUTPUT"
fi
