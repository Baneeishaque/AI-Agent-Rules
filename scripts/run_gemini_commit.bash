#!/bin/bash
# Run Gemini commit message generator
# Usage: run_gemini_commit.bash <python_executable>
# Example: run_gemini_commit.bash "mise exec -- python"

set -euo pipefail

PYTHON_CMD="${1:?Error: Python executable parameter required (e.g., 'python' or 'mise exec -- python')}"

# Make scripts executable
chmod +x scripts/generate_commit_msg.py

# Stage the relevant files so the python script can diff them
git add README.md agent-rules.md

# Run generator with specific files
# We capture stdout. If script fails or returns empty, we handle it.
MSG=$($PYTHON_CMD scripts/generate_commit_msg.py --files README.md agent-rules.md) || true

if [ -z "$MSG" ]; then
  MSG="docs(rules): sync rule indices (AI generation failed)"
fi

# Output to GitHub Env for the next step
echo "COMMIT_MSG<<EOF" >> $GITHUB_ENV
echo "$MSG" >> $GITHUB_ENV
echo "EOF" >> $GITHUB_ENV
