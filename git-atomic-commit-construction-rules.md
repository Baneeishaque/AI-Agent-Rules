<!--
title: Git Atomic Commit Construction
description: Authoritative protocol for analyzing, grouping, and arranging changes into logical, independent atomic units before execution.
category: Git & Repository Management
-->

# Git Atomic Commit Construction Rules

This document defines the mandatory protocol for creating "Arranged Commits"—logical, independent, and atomic units of change. This approach ensures high-quality history and minimizes regression risks.

***

### 1. Phase 1: Deep Change Analysis

Before staging any files, the agent MUST perform a dependency analysis of all modifications.

- **Shared Identifiers**: Group changes that modify the same functions, classes, or constants across different files.
- **Cross-File References**: If file A depends on a change in file B (e.g., an import or a link), they MUST be part of the same atomic commit.
- **Categorical Alignment**: Group changes by their architectural layer (e.g., UI, Logic, Docs) unless they are functionally coupled.

***

### 2. Phase 2: Logical Grouping (Arrangement)

The agent must "arrange" the detected changes into a proposed sequence of commits.

- **Independence**: Each commit should be able to stand alone. If the repository were checked out at that commit, it should still build/function (or at least be logically coherent).
- **Atomic Principle**: Never commit half of a logical change. If a file contains two unrelated changes, use **Hunk-Based Staging**.
- **The Commit Preview (Mandatory Display)**:
    - Present the proposed "Arranged Commits" to the user for approval using the following structured format:
    ```markdown
    ## Arranged Commits Preview
    
    ### Commit 1: [type] [title]
    - **Files**: [file1.md], [file2.md]
    - **Message**:
      ```
      [type](scope): [title]
      
      [Body line 1]
      [Body line 2]
      ```
    
    ### Commit 2: [type] [title]
    - **Files**: [file3.md]
    - **Message**:
      ```
      [type](scope): [title]
      
      [Body line 1]
      ```
    
    ---
    Please say "start" to begin the sequential execution of these atomic commits.
    ```
- **Start Trigger**: The agent MUST NOT proceed with any commit execution until the user explicitly says **"start"**.

***

### 3. Phase 3: Interactive Hunk-Based Staging

When a file contains mixed concerns, the agent MUST use interactive staging tools.

- **Command**: `git add -p <file>`
- **Philosophy (Chunk Committing)**: Also known as "hunk-based staging". This is the mandatory method for ensuring no "unrelated noise" or "piggybacked" style fixes leak into functional commits. Every modified line must be evaluated: "Does this line belong to the *current* atomic goal?"
- **Hunk-by-Hunk Execution**: During interactive staging, the agent MUST evaluate and respond to each hunk individually (`y`, `n`, `s`, etc.). Do not batch responses. This ensures each decision is deliberate and minimizes the risk of staging unrelated changes.
- **Granular Hygiene**: If a grammatical fix is discovered while implementing a feature, it MUST be staged and committed separately (either before or after) unless it is part of the same logical chunk. Continuous use of `git add -p` ensures high-quality, noise-free history.
- **Verification**: Run `git diff --cached` after staging each chunk to guarantee strictly atomic contents.

***

### 4. Phase 4: Execution & Verification

- **Step-by-Step**: Execute commits one-by-one according to the approved arrangement.
- **Unstaged Changes During Rebase**: If rebase fails due to unstaged changes, use the stash workflow (see git-operation-rules.md Section 3).
- **Pull Before Push**: Always `git pull` (or `git pull --rebase` upon explicit approval) before pushing to incorporate latest remote changes.
- **Recovery**: If a mistake is made during staging, use `git reset <file>` to unstage, or `git checkout -p` to selectively discard. **WARNING**: Never use `git reset --hard` for synchronization; always prefer `git pull`.

***

### 5. The Commit Compass (GitKraken Philosophy)

Imagine a compass where each cardinal direction is a logical area of the codebase.
- **North**: Architectural/Schema changes.
- **East**: Logic/Feature implementation.
- **West**: Testing/Verification.
- **South**: Documentation/Refinement.

A high-quality commit history moves clearly through these directions without "spinning" (mixing logic and documentation in one commit).
