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
- **The Commit Preview**: Present the proposed "Arranged Commits" to the user for approval. Use a format similar to:
    - **Commit 1**: `feat(scope): title` -> Files: `A`, `B` (hunk 1)
    - **Commit 2**: `fix(scope): title` -> Files: `B` (hunk 2), `C`

***

### 3. Phase 3: Interactive Hunk-Based Staging

When a file contains mixed concerns, the agent MUST use interactive staging tools.

- **Command**: `git add -p <file>`
- **Logic**: Selectively stage only the lines (hunks) belonging to the current atomic commit.
- **Verification**: Run `git diff --cached` after staging to ensure no unrelated lines were accidentally included.

***

### 4. Phase 4: Execution & Verification

- **Step-by-Step**: Execute commits one-by-one according to the approved arrangement.
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
