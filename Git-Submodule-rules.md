<!--
title: Git Submodule Management
description: Protocols for managing submodules, preventing detached HEAD states, proper branch tracking, and descriptive parent commit messages.
category: Git & Repository Management
-->

# Git Submodule Management Rules

This document outlines the strict protocols for managing Git submodules to prevent "detached HEAD" states, lost commits, and synchronization issues.

***

### 1. Core Principle: Branch Tracking

-   **Never Commit to Detached HEAD**: Submodules often check out a specific commit SHA by default, placing them in a "detached HEAD" state.
-   **Mandatory Checkout**: Before making ANY changes to a submodule, you MUST explicitly check out a branch (usually `main` or `master`).
    -   Command: `cd <submodule-dir> && git checkout main`
-   **Verification**: Run `git status` inside the submodule to confirm you are "On branch main" before creating files or committing.

***

### 2. Workflow for Updating Submodules

When you need to add files, update rules, or modify content within a submodule:

1.  **Enter & Checkout**:
    ```bash
    cd <submodule-path>
    git checkout main  # or master
    git pull origin main # Ensure you are up to date
    ```

2.  **Make Changes**: Create or edit files as needed.

3.  **Commit in Submodule**:
    ```bash
    git add .
    git commit -m "feat(scope): description..."
    ```

4.  **Push Submodule (Optional but Recommended)**:
    -   If you have write access, push the submodule changes immediately to avoid them existing only locally.
    -   `git push origin main`

5.  **Update Parent Repository**:
    -   Return to the parent root: `cd ..`
    -   Stage the submodule folder: `git add <submodule-path>`
    -   Commit the pointer update (describe what changed, not just that it updated):
        ```bash
        git commit -m "chore(submodule): update <submodule-name> with <change-summary>

        - Describe specific changes made in the submodule
        - Follow standard commit message rules"
        ```

***

### 3. Recovery from Detached HEAD

If you accidentally commit to a detached HEAD:

1.  **Identify the Commit**: Run `git log -1` or `git reflog` to get the SHA of your new commit.
2.  **Checkout Branch**: `git checkout main`
3.  **Cherry-Pick**: `git cherry-pick <commit-sha>`
4.  **Push & Sync**: Push the branch and update the parent repository as described above.

***

### 4. Automation Safeguards

-   **AI Tooling**: When an AI agent is tasked with modifying a submodule, it must first execute `git checkout <default-branch>` as a prerequisite step.
-   **Status Check**: The agent should verify `git status` output does not contain "HEAD detached" before proceeding with edits.
