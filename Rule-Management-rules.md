# Rule Management: Documentation Sync Workflow

Whenever the user mentions adding or modifying a AI rule, always remind them to update the agent-rules.md documentation. The workflow is: 1) Help craft the rule name and description, 2) User adds/modifies rule in Warp first, 3) Remind user to say "Update agent-rules.md with the new/modified rule", 4) Update the markdown file and commit with conventional commit message. This ensures documentation stays synchronized with actual Warp rules.

**Workflow Steps:**
1. Rule Creation/Modification - Help craft proper rule name and description
2. Warp Update First - User adds/modifies rule in Warp interface
3. Documentation Sync - Remind user to request markdown update
4. Commit Changes - Update agent-rules.md and commit with proper message

**Trigger Phrases:**
- "I want to add a rule for..."
- "New rule: when I do X, you should Y"
- "Let's create a rule that..."
- "Modify the rule for..."
