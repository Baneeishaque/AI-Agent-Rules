# Workflow Optimization: Conditional Step Execution

## Overview

This document details the optimization applied to the `update-rules.yml` GitHub Actions workflow. The goal was to reduce execution time and resource usage by skipping expensive steps when no meaningful changes occur.

## Strategy

We implemented a **Conditional Execution Strategy** using a helper script to detect file changes.

### 1. Change Detection Script

A new script `scripts/check_changes.bash` was created to check for modifications to specific files (`README.md` and `agent-rules.md`).

**Logic:**
- Runs `git status --porcelain` on the target files.
- If output is non-empty (changes exist), it sets `has_changes=true` in the GitHub environment.
- If empty, it sets `has_changes=false`.

### 2. Workflow Logic

The workflow `.github/workflows/update-rules.yml` was updated to:

1.  **Run the Check**: Execute `scripts/check_changes.bash` and map its output to a step ID (`check_changes`).
2.  **Condition Steps**: Subsequent steps (`Install Dependencies`, `Generate Commit Message`, `Commit and Push`) now include an `if` condition:
    ```yaml
    if: steps.check_changes.outputs.has_changes == 'true'
    ```

## Benefits

-   **Performance**: Skips Python dependency installation and API calls (Gemini) when rule indices are unchanged.
-   **Efficiency**: Reduces CI/CD minutes usage.
-   **Clean Logs**: Avoids "nothing to commit" messages or unnecessary "skip" logic inside the commit action itself.

## Affected Files

-   `.github/workflows/update-rules.yml`
-   `scripts/check_changes.bash`
