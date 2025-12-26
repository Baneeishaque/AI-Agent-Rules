
# Git Commit and Submodule Workflow: Practical Guide & Reference Map

## Purpose

This document is a practical, example-driven workflow guide for managing file and submodule commits, especially with document/PDF context extraction. **All authoritative rules are defined in the following documents:**

- [Git Commit Message Generation Rules](AI-Agent-Rules/Git-Commit-Message-rules.md)
- [Git Submodule Management Rules](AI-Agent-Rules/Git-Submodule-rules.md)
- [Git Operation Rules](AI-Agent-Rules/Git-Operation-rules.md)
- [PDF CLI Extraction Tool Guide](AI-Agent-Rules/docs/conversations/2025-12-26-pdf-cli-extraction-tool.md)

**This file does not duplicate rules.** Instead, it provides:
- A step-by-step workflow referencing the above rules
- Practical examples and new guidance (e.g., PDF extraction for commit context)
- Troubleshooting and best practices

---

## 1. Workflow Overview (Reference Steps)

1. **Detect changes**
  - Use `git status --short` and `git diff --cached` to see staged/unstaged changes
  - See: [Operational Protocol for Change Detection](AI-Agent-Rules/Git-Commit-Message-rules.md#0-operational-protocol-for-change-detection-and-commit-scope)

2. **If working in a submodule**
  - Always check out the main branch and verify with `git status`
  - See: [Submodule Management Rules](AI-Agent-Rules/Git-Submodule-rules.md#1-core-principle-branch-tracking)

3. **Stage and commit changes**
  - Only commit staged files (never assume unstaged changes)
  - See: [Git Operation Rules](AI-Agent-Rules/Git-Operation-rules.md#1-commits)

4. **Push submodule changes** (if authorized)
  - See: [Git Operation Rules](AI-Agent-Rules/Git-Operation-rules.md#2-pushes)

5. **Update parent repository**
  - Move to parent repo root, use `git submodule status` to confirm submodule path
  - Stage and commit the submodule pointer update
  - See: [Submodule Sync Commits](AI-Agent-Rules/Git-Commit-Message-rules.md#5-submodule-sync-commits-parent-repository)

6. **Generate commit messages**
  - Follow Conventional Commits and all message rules
  - See: [Commit Message Generation Rules](AI-Agent-Rules/Git-Commit-Message-rules.md)

7. **Extract PDF/document context (if needed)**
  - Use CLI tools (see below) to extract text for commit context
  - See: [PDF CLI Extraction Tool Guide](AI-Agent-Rules/docs/conversations/2025-12-26-pdf-cli-extraction-tool.md)

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
- For more, see: [PDF CLI Extraction Tool Guide](AI-Agent-Rules/docs/conversations/2025-12-26-pdf-cli-extraction-tool.md)

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

- [Git Commit Message Generation Rules](AI-Agent-Rules/Git-Commit-Message-rules.md)
- [Git Submodule Management Rules](AI-Agent-Rules/Git-Submodule-rules.md)
- [Git Operation Rules](AI-Agent-Rules/Git-Operation-rules.md)
- [PDF CLI Extraction Tool Guide](AI-Agent-Rules/docs/conversations/2025-12-26-pdf-cli-extraction-tool.md)

---

**This document is a workflow and example guide. For all authoritative rules, always refer to the referenced documents above.**
