<!--
title: Rule Management Workflow
description: Documentation sync and update workflow, including metadata management for rule indexing.
category: Tooling & Workflows
-->

# Rule Management: Documentation Sync Workflow

## Automated Synchronization
The `README.md` and `agent-rules.md` files are **automatically generated** from the individual rule files. **Do not edit them manually.**

### Workflow
1.  **Modify/Add Rule**: Edit or create a `*-rules.md` file.
2.  **Add Metadata**: Ensure the file starts with the required metadata block:
    ```markdown
    <!--
    title: [Short Title for Index]
    description: [Summary for Index]
    category: [Category Name]
    -->
    ```
    *   **Note**: You can define *any* category name. New categories will automatically create new sections in the `README.md`.
3.  **Commit**: Push your changes.
4.  **Auto-Update**: The GitHub Actions workflow (`update-rules`) will:
    *   Validate metadata.
    *   Regenerate `README.md` and `agent-rules.md`.
    *   Commit the changes automatically.
    *   **Fail** if metadata is invalid/missing (check Action logs).
3.  **Craftsmanship Standards**: All new rules must adhere to the formatting and structural requirements defined in [ai-rule-standardization-rules.md](./ai-rule-standardization-rules.md).

## Manual Indexing (Legacy/Fallback)
If automation fails or is incomplete, follow the legacy process below ONLY as a fallback.


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
