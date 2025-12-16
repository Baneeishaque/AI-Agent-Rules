#!/bin/bash
set -e

# Make scripts executable
chmod +x scripts/generate_commit_msg.py

# Stage the relevant files so the python script can diff them
git add README.md agent-rules.md

# Run generator with specific files
# We capture stdout. If script fails or returns empty, we handle it.
MSG=$(./scripts/generate_commit_msg.py --files README.md agent-rules.md)

if [ -z "$MSG" ]; then
  MSG="docs(rules): sync rule indices (AI generation failed)"
fi

# Output to GitHub Env for the next step
echo "COMMIT_MSG<<EOF" >> $GITHUB_ENV
echo "$MSG" >> $GITHUB_ENV
echo "EOF" >> $GITHUB_ENV
