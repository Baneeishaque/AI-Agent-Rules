<!--
title: Git Repository Management Rules
description: Comprehensive protocol for the repository lifecycle, including standardized creation, CLI-based cloning, submodule initialization, and auto-indexing.
category: Git & Repository Management
-->

# Git Repository Management Rules

This document outlines the authoritative protocol for managing the lifecycle of Git repositories. Adherence to these standards ensures architectural consistency and seamless integration across all AI agent operations.

***

### 1. Repository Creation Standards

When initializing a new repository, the agent MUST establish a solid foundation to ensure long-term maintainability.

- **Naming Convention**: Use strictly lowercase kebab-case (e.g., `my-project-repo`).
- **Essential Files**: Every new repository MUST be initialized with:
    - **`README.md`**: Single source of truth (SSOT) with Title, Overview, and Getting Started sections.
    - **`.gitignore`**: Language-specific, generated via `gitignore.io`.
    - **`LICENSE`**: MIT or Apache 2.0 by default.
- **Initial Commit**: Use Conventional Commits (`feat: Initial repository setup`).

***

### 2. High-Fidelity Cloning Protocol

Always prioritize platform-specific CLI tools over generic `git clone` to leverage native authentication and metadata features.

- **CLI Selection**:
    - **GitHub**: Use `gh repo clone <owner>/<repo>`.
    - **GitLab**: Use `glab repo clone <path/to/repo>`.
- **Target Location**: Default to `~/sample/path/` using the original hyphenated name.
- **Submodule Handling**: If a `.gitmodules` file exists, the agent MUST immediately run:
    ```bash
    git submodule update --init --recursive
    ```

***

### 3. Automatic Codebase Indexing

To maximize agent effectiveness, any Git repository designated for work should be treated as an indexed codebase.

- **Zero-Config Search**: When the working directory is within a Git repository, the agent MUST automatically treat it as a target for `search_codebase` tools, regardless of explicit configuration files.
- **Context Discovery**: Use indexing to rapidly build mental models of new or cloned repositories.

***

### 4. Verification & Industrial Audit

- **Pre-Flight**: Validate the repo name against the lowercase kebab-case standard before creation.
- **Post-Operation**: Confirm the presence of mandatory files and submodule initialization status immediately after cloning or creation.
