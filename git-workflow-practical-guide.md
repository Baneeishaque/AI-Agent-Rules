
# Git Commit and Submodule Workflow: Practical Guide & Reference Map

## Purpose

This document is a practical, example-driven workflow guide for managing file and submodule commits, especially with document/PDF context extraction. **All authoritative rules are defined in the following documents:**

- [Git Commit Message Generation Rules](./git-commit-message-rules.md)
- [Git Submodule Management Rules](./git-submodule-rules.md)
- [Git Operation Rules](./git-operation-rules.md)
- [PDF CLI Extraction Tool Guide](./docs/conversations/2025-12-26-pdf-cli-extraction-tool.md)

**This file does not duplicate rules.** Instead, it provides:
- A step-by-step workflow referencing the above rules
- Practical examples and new guidance (e.g., PDF extraction for commit context)
- Troubleshooting and best practices

***

## 1. The Commit Compass & Operational Protocols

This section provides a visual mapping of how to arrange commits using the cardinal directions of the **Commit Compass** (authoritative logic in [git-atomic-commit-construction-rules.md](./git-atomic-commit-construction-rules.md)) and the mandatory operational sequences required before execution.

### Operational Sequence (Mandatory)
1.  **Workflow Finalization**: If changes impact CI/CD (workflows, scripts), fix and verify the logic **FIRST**.
2.  **Verbose Preview**: Present the "Arranged Commits Preview" with maximum details (hunks/previews).
3.  **Explicit Authorization**: Wait for the user to say **"commit"** before starting execution.

| Direction | Domain | Authoritative Rule |
| :--- | :--- | :--- |
| **North** | Architecture & Global Config | [git-operation-rules.md](./git-operation-rules.md) |
| **East** | Logic & Feature Implementation | [git-atomic-commit-construction-rules.md](./git-atomic-commit-construction-rules.md) |
| **West** | Verification & Automated Tests | [git-operation-rules.md](./git-operation-rules.md) |
| **South** | Documentation & Rule Sync | [git-commit-message-rules.md](./git-commit-message-rules.md) |

### Synchronization Workflows
- **Submodule Pointer Sync**: Follow [Submodule Sync Commits](./git-commit-message-rules.md#5-submodule-sync-commits-parent-repository).
- **Remote Reconciliation**: Use `git pull` or `git pull --rebase` (with approval). **Never** `git reset` for sync.

***

## 2. Case-Sensitive File Renaming (macOS & Windows)

Both macOS and Windows use case-insensitive filesystems by default. Renaming files to change only the case (e.g., `Git-Operation-rules.md` → `git-operation-rules.md`) requires a two-step workaround.

### The Two-Step `git mv` Technique

1. **First Move**: Rename to a temporary name
   ```bash
   git mv Git-Operation-rules.md temp-operation.md
   ```

2. **Second Move**: Rename to the final lowercase name
   ```bash
   git mv temp-operation.md git-operation-rules.md
   ```

### Why This Works

- Git tracks the rename in two separate operations
- The temporary name breaks the case-insensitive collision
- Both moves are staged automatically and can be committed together

### Windows Reserved Names Warning

Windows prohibits certain characters and names in filenames:

- **Reserved Characters**: `< > : " / \ | ? *`
- **Reserved Names**: `CON`, `PRN`, `AUX`, `NUL`, `COM1-COM9`, `LPT1-LPT9`
- **Trailing Issues**: Filenames cannot end with spaces or dots

**Best Practice**: Use lowercase kebab-case with alphanumeric characters and hyphens only (e.g., `git-operation-rules.md`).

### Batch Renaming Example

For multiple files, execute all first moves, then all second moves:
```bash
# First moves
git mv Git-Operation-rules.md temp-operation.md
git mv Git-Submodule-rules.md temp-submodule.md

# Second moves
git mv temp-operation.md git-operation-rules.md
git mv temp-submodule.md git-submodule-rules.md
```

***

## 3. PDF Context Extraction for Commit Messages (Practical Example)

To maximize context for PDF/document commits:

- Use CLI tools (e.g., `pdftohtml -xml`, `pdftotext`, `mutool`) to extract structured or plain text from PDFs.
- Use extracted content, file/folder names, and categorization to write precise, context-rich commit messages.

### Example: Extracting PDF Content

```sh
pdftohtml -xml input.pdf output.xml
head -n 80 output.xml # Review for context
```

- Clean up temporary files after extraction.
- For more, see: [PDF CLI Extraction Tool Guide](./docs/conversations/2025-12-26-pdf-cli-extraction-tool.md)

***

## 4. Troubleshooting & Best Practices

### Divergence Resolution

When local and remote branches have diverged:

1. **Check Status**: `git status` shows divergence
2. **Fetch**: `git fetch origin <branch>` (requires user approval)
3. **Analyze**: Use `git log` to compare:
   - Local ahead: `git log origin/<branch>..HEAD --oneline`
   - Remote ahead: `git log HEAD..origin/<branch> --oneline`
4. **Resolve**:
   - **Independent changes**: `git pull --rebase origin <branch>`
   - **Conflicting changes**: Manual merge or rebase with conflict resolution.
   - **Structural/Atomic Fixes**: If the divergence involves non-atomic history that requires surgery, follow the **[Git History Refinement Rules](./git-history-refinement-rules.md)**.

### Stash vs. Commit Decision

- **Use Stash**: Temporary, incomplete work that shouldn't be in history
- **Use Commit**: Logical, complete changes that belong in history
- **Never**: Mix stash and commit for the same logical change

### General Best Practices

- If `git add <submodule-path>` fails, verify you are in the parent repo root and the path matches `git submodule status` output.
- If PDF extraction fails, check the filename, path, and tool installation.
- Always document every step and confirm with git output.
- Never assume context; always extract and verify.
- Use extracted document content and folder structure for maximum commit clarity.
- Clean up any temporary files created during PDF extraction.

***

## 5. References (Single Source of Truth)

- [Git Commit Message Generation Rules](./git-commit-message-rules.md)
- [Git Submodule Management Rules](./git-submodule-rules.md)
- [Git Operation Rules](./git-operation-rules.md)
- [PDF CLI Extraction Tool Guide](./docs/conversations/2025-12-26-pdf-cli-extraction-tool.md)

***

**This document is a workflow and example guide. For all authoritative rules, always refer to the referenced documents above.**
