
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

---

## 1. The Commit Compass: Reference Map

This section provides a visual mapping of how to arrange commits using the cardinal directions of the **Commit Compass** (authoritative logic in [git-atomic-commit-construction-rules.md](./git-atomic-commit-construction-rules.md)).

| Direction | Domain | Authoritative Rule |
| :--- | :--- | :--- |
| **North** | Architecture & Global Config | [git-operation-rules.md](./git-operation-rules.md) |
| **East** | Logic & Feature Implementation | [git-atomic-commit-construction-rules.md](./git-atomic-commit-construction-rules.md) |
| **West** | Verification & Automated Tests | [git-operation-rules.md](./git-operation-rules.md) |
| **South** | Documentation & Rule Sync | [git-commit-message-rules.md](./git-commit-message-rules.md) |

### Synchronization Workflows
- **Submodule Pointer Sync**: Follow [Submodule Sync Commits](./git-commit-message-rules.md#5-submodule-sync-commits-parent-repository).
- **Remote Reconciliation**: Use `git pull` or `git pull --rebase` (with approval). **Never** `git reset` for sync.

---

## 2. PDF Context Extraction for Commit Messages (Practical Example)

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

---

## 3. Troubleshooting & Best Practices

- If `git add <submodule-path>` fails, verify you are in the parent repo root and the path matches `git submodule status` output.
- If PDF extraction fails, check the filename, path, and tool installation.
- Always document every step and confirm with git output.
- Never assume context; always extract and verify.
- Use extracted document content and folder structure for maximum commit clarity.
- Clean up any temporary files created during PDF extraction.

---

## 4. References (Single Source of Truth)

- [Git Commit Message Generation Rules](./git-commit-message-rules.md)
- [Git Submodule Management Rules](./git-submodule-rules.md)
- [Git Operation Rules](./git-operation-rules.md)
- [PDF CLI Extraction Tool Guide](./docs/conversations/2025-12-26-pdf-cli-extraction-tool.md)

---

**This document is a workflow and example guide. For all authoritative rules, always refer to the referenced documents above.**
