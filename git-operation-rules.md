<!--
title: Git Operation Rules
description: Strict protocols for standard Git operations (commits & pushes), mandating explicit user requests and forbidding auto-actions.
category: Git & Repository Management
-->

# Git Operation Rules


## 0. Operational Protocol for Change Detection and Commit Scope

- Always use git commands to detect unstaged and staged changes in the folder or repository specified by the user.
- When asked to commit staged files, only consider files that are staged (use git diff --cached or git status --short).
- Always respect the folder, repository, or submodule specified by the user. If not specified, use the workspace root or known repositories.
- If the folder is a submodule, follow all submodule commit and branch management rules (see Git-Submodule-rules.md).
- Do not manually scan or assume file changes; always rely on git for authoritative status.

## Version Control Operations

### 1. Commits

- **Atomic Construction**: Before any commit operation, follow the [Git-Atomic-Commit-Construction-rules.md](./Git-Atomic-Commit-Construction-rules.md) to group and arrange changes.
- **Explicit Request Required**: Do NOT generate commit messages or execute `git commit` unless the user **explicitly** requests it.
- **No Auto-Commits**: Never assume a task completion implies a commit. Always wait for instruction.
- **Commit Messages**: When authorized, must strictly follow `Git-Commit-Message-rules.md`.

### 2. Pushes and Synchronization

- **Explicit Request Required**: Do NOT execute `git push` unless the user **explicitly** requests it.
- **No Auto-Pushes**: Even if a commit is requested, do not chain a push command unless specifically told to "commit and push".
- **Safety First (High-Risk Operations)**:
    - **`git reset`**: Strictly forbidden for synchronization or resolving conflicts. If unstageing is needed, use `git reset <file>`. Hard resets require explicit user confirmation after explaining the data loss risk.
    - **`git rebase`**: Requires explicit user confirmation.
    - **Preferred Method**: Always preference `git pull` or `git pull --rebase` (with approval) to incorporate latest remote changes.
