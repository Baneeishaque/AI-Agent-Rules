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
- If the folder is a submodule, follow all submodule commit and branch management rules (see git-submodule-rules.md).
- Don't manually scan or assume file changes; always rely on git for authoritative status.
- **Workflow-First Priority**: If changes involve CI/CD (workflows, scripts), fix and verify the logic **FIRST** before committing.

## Version Control Operations

### 1. Commits

- **Atomic Construction**: Before any commit operation, follow the [git-atomic-commit-construction-rules.md](./git-atomic-commit-construction-rules.md) to group and arrange changes.
- **Explicit Request Required**: Do NOT generate commit messages or execute `git commit` unless the user **explicitly** requests it.
- **Authorization Trigger**: The agent MUST NOT proceed with any commit until the user explicitly says **"start"**. Other commands like "commit" are insufficient.
- **No Auto-Commits**: Never assume a task completion implies a commit. Always wait for instruction.
- **Commit Messages**: When authorized, must strictly follow `git-commit-message-rules.md`.

### 2. Pushes and Synchronization

- **Status Check First**: Always run `git status` before any fetch, pull, or push operation to understand the current state.
- **Remote Check**: Use `git fetch --dry-run` or `git ls-remote` to check for remote changes WITHOUT fetching. Requires user confirmation.
- **Fetch Protocol**: Do NOT execute `git fetch` without explicit user confirmation.
- **Pull Protocol**: 
    - **Timing**: Pull BEFORE making commits, not after.
    - **Explicit Confirmation**: Always ask user before pulling.
    - **Rebase Option**: `git pull --rebase` requires separate explicit confirmation.
- **Push Protocol**:
    - **Explicit Request Required**: Do NOT execute `git push` unless the user **explicitly** requests it.
    - **No Auto-Pushes**: Even if a commit is requested, do not chain a push command unless specifically told to "commit and push".
    - **Offer, Don't Execute**: After commits, OFFER the user to push. Wait for explicit "yes" or "push" command.
- **Safety First (High-Risk Operations)**:
    - **`git reset`**: Strictly forbidden for synchronization or resolving conflicts. If unstaging is needed, use `git reset <file>`. Hard resets require explicit user confirmation after explaining the data loss risk.
    - **`git rebase`**: Requires explicit user confirmation.

### 3. Stash Workflow for Rebase Operations

When rebasing with unstaged changes, use `git stash` to temporarily save work.

- **Stash Before Rebase**:
  ```bash
  git stash push -m "Descriptive message for stash"
  git pull --rebase origin <branch>
  ```

- **Pop After Rebase**:
  ```bash
  git stash pop
  ```

- **Conflict Resolution**: If `git stash pop` creates conflicts, resolve them manually, then:
  ```bash
  git add <resolved-files>
  git stash drop  # Remove the stash entry after manual resolution
  ```

- **List Stashes**: View all stashed changes:
  ```bash
  git stash list
  ```
