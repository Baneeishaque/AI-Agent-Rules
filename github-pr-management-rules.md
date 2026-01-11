<!--
title: GitHub PR Management Rules
description: Sequential, CLI-first protocols for handling Pull Requests, emphasizing security for private repositories and explicit user handoff.
category: Git & Repository Management
-->

# GitHub Pull Request Processing Rules

This document defines the mandatory protocols for AI agents when processing Pull Requests (PRs). These rules prioritize security, focus, and explicit user control.

***

### 1. Security & Tooling Strategy

The agent must use the **GitHub CLI (`gh`)** for all PR-related operations to ensure accessibility to private repositories and protected resources.

-   **Pre-Authenticated Environment**: The `gh` CLI is assumed to be authenticated and configured within the user's workspace.
-   **Security Restriction**: Agents are **prohibited** from using `search_web` or `read_url_content` for PR links or branch details. The `gh` CLI is the ONLY Single Source of Truth for PR metadata.

***

### 2. Operational Protocol (One-at-a-Time)

To maintain focus and prevent technical drift, agents must handle PRs sequentially.

1.  **Discovery**: Prepare a list of active PRs using `gh pr list`.
2.  **Selection**: Pick exactly **ONE** PR to process. 
3.  **Analysis**: Use `gh pr view <number>` to understand the requirements and `gh pr checkout <number>` to begin implementation.
4.  **No Multitasking**: Do NOT jump to the next PR or switch tasks until the current PR is finalized.

***

### 3. Explicit Handoff & SEO Governance

Consistent with the "Project Architect" role, the agent must ensure a clean handoff.

-   **Confirmation Workflow**: Upon completing a PR, notify the user. The agent is **Blocked** from proceeding to the next PR until the user explicitly confirms completion (e.g., "done", "next", or "approved").
-   **Documentation**: Ensure all PR-related edits (e.g., to README) follow the [github-repo-metadata-management-rules.md](./github-repo-metadata-management-rules.md).
-   **Commit Quality**: All PR-related commits must adhere to [Git-Commit-Message-rules.md](./Git-Commit-Message-rules.md).

***

### 4. Prohibited Behaviors

-   **No Auto-Transition**: Never move to the next PR without user input.
-   **No External Leakage**: Never share or search for private PR details on external platforms.
-   **No Branch Drift**: Ensure you are on the correct PR branch before making edits.
