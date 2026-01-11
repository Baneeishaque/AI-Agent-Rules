<!--
title: Git History Refinement Rules
description: Protocols for refining existing commit history using backup branches, jq for JSON atomicity, and tree parity verification.
category: Git & Repository Management
-->

# Git History Refinement Rules

This document defines the mandatory protocol for refining or reconstructing existing git commit history. This is used when commits contain mixed concerns (e.g., non-atomic JSON changes) that need to be split or re-ordered while preserving history quality and tree integrity.

***

## 1. Safety First: The Backup Protocol

The agent **MUST** create a backup branch before performing any destructive history operations (`reset --hard`, `rebase`, etc.).

### 1.1 Incremental Branch Naming

To prevent overwriting existing backups and to maintain a trail of refinement attempts, use an incrementing suffix:

1. **Prefix**: `backup/pre-settings-split-` (or descriptive equivalent).
2. **Check**: Run `git branch --list "prefix*"` to see current versions.
3. **Increment**: Select the first integer `n` that does NOT have a corresponding branch (e.g., if `-1` and `-2` exist, use `-3`).
4. **Workspace Preservation**: Before creating the branch, stage all local changes and create a temporary "state preservation" commit. This ensures the backup captures the exact state of the workspace including uncommitted changes.
5. **Creation**: Create the branch using `git branch <name>`. **DO NOT** use `-f` to force-move a branch.

***

## 2. Methodology: Reconstruction via Extraction

When splitting changes across existing commits, use the "Reset and Restore" strategy to reconstruct the history atop a clean baseline.

### 2.1 The Baseline Reset

Reset the active branch (e.g., `master`) to the last known "clean" commit before the messy historical segment.

```bash
git reset --hard <clean-commit-hash>
```

#### 2.1.1 Root Commit Refinement

If the refinement involves the first commit (root) of the repository, use an orphan branch:

```bash
git checkout --orphan temp-master
git rm -rf .
```

This allows reconstructing the history from scratch while preserving the repository's identity.

### 2.2 Atomic JSON Manipulation (jq)

When a JSON file (like `.vscode/settings.json`) needs to be split across commits, use `jq` to extract exactly the relevant keys for the current atomic unit.

1. **Extract Original**: Fetch the final version from the backup.

    ```bash
    git show <backup-branch>:<path/to/file.json> > <file.json>.bak
    ```

2. **Filter with jq**: Create a valid JSON containing only the commit-specific keys.

    ```bash
    jq '{ "specific.key": .["specific.key"] }' <file.json>.bak > <file.json>
    ```

3. **Verification**: The agent MUST verify the generated JSON is valid before staging.

    ```bash
    jq . <file.json>
    ```

#### 2.2.1 Canonical Sorting and Formatting

When manipulating JSON arrays (e.g., `cSpell.words`), the agent **MUST** preserve or enforce the project's standard sort order to prevent history misalignment across commits.

1. **Inspection**: Examine neighboring commits to determine the expected sort order (e.g., ASCII vs. case-insensitive natural sort).
2. **Consistency**: Ensure the sort order is applied identically at every stage of the reconstruction.
3. **Tooling**: Prefer stable sorting tools or scripts (e.g., Python's `sorted(key=str.lower)`) over standard `jq` sort if case-insensitivity is required.

### 2.3 Metadata Preservation

When re-creating commits that originally had specific messages and timestamps, use the original commit's hash to preserve metadata.

```bash
git commit -C <original-hash>
```

### 2.4 Sequential Integrity (Protocol Files)

When refining history for documents containing numbered phases or state-dependent protocols (e.g., `git-atomic-commit-construction-rules.md`), the agent **MUST** maintain structural validity at *every* intermediate commit.

- **The Valid-Sequence Rule**: Every commit in the refined history MUST result in a valid 1-N sequence of phases. No gaps, no duplicates, and no "broken" intermediate states.
- **Micro-Renumbering**: If a commit adds Phases 4 and 5, and the original file already had a Phase 4 (now 6), the agent MUST renumber all subsequent phases within that same atomic unit to preserve immediate validity.

### 2.5 Remote Baseline Reconciliation

Before starting any history refinement, the agent MUST synchronize with the remote source of truth to prevent divergence.

1. **Mandatory Fetch**: `git fetch origin <branch>`
2. **Reconciliation**: If `origin/<branch>` contains commits not present in the local branch, the agent MUST:
   - Identify the latest remote commit as the new "Refinement Baseline".
   - Re-execute the reconstruction atop this reconciled baseline.
3. **Submodule Awareness**: This protocol applies recursively to submodules. Never begin a submodule refinement without a `git -C <path> pull` or fetch.

***

## 3. Verification & Parity

The "Arranged Result" of the refined history MUST match the "Original Result" in final state (the code tree), even if the intermediate steps differ.

### 3.1 Content-Level Verification

After each commit in the reconstruction, use `git show` to confirm only the intended changes were introduced.

```bash
git show HEAD
```

### 3.2 Tree Parity Check (Mandatory)

After the final commit in the refinement process, the current branch MUST be compared to the backup.

```bash
git diff <current-branch> <backup-branch>
```

**Constraint**: The diff MUST be empty. Any discrepancy indicates a regression introduced during the refinement process.

***

## 4. Finalization

The agent is **BLOCKED** from deleting backup branches automatically.

- **Protocol**: Provide a walkthrough of the refined history.
- **Authorization**: Request explicit user confirmation before deleting any backup branches created under Section 1. The agent is **PROHIBITED** from deleting these automatically.
