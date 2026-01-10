<!--
title: Git .gitignore Handling Rules
description: Protocols for generating, maintaining, and customizing .gitignore files using standard APIs.
category: Git & Repository Management
-->

# Git .gitignore Handling Rules

This document defines the mandatory protocol for managing `.gitignore` files. The goal is to separate standard, auto-generated exclusions (OS, IDE, Language) from project-specific custom rules using a "Generated Foundation + User Delta" approach.

---

## 1. Source of Truth: The API

Whenever standardized gitignore rules are required (e.g., for Linux, macOS, Windows, VisualStudioCode), the agent **MUST** source them directly from the `gitignore.io` API (via toptal.com) rather than attempting to write them manually or copy-paste partial hunks.

- **API Endpoint**: `https://www.toptal.com/developers/gitignore/api/<list,of,templates>`
- **Example**: `https://www.toptal.com/developers/gitignore/api/linux,macos,windows`
- **Reference list**: `https://docs.gitignore.io/use/api#get-all-templates`

---

## 2. Workflow: Generated vs. Custom Separation

When processing a `.gitignore` file that contains both standard and custom rules:

### Step 1: Backup and Analysis

1. **Backup** the existing `.gitignore` file (if it exists) to a tailored backup location (e.g., `.gitignore.bak`).
2. **Analyze** the backup to identify:
    - Standard categories (OS, IDE, Frameworks).
    - User-defined customizations (specific file exclusions, un-ignore rules, or modified standard rules).

### Step 2: Commit A - The Standard Foundation

1. **Fetch** the standard rules using the API.

    ```bash
    curl -L -s https://www.toptal.com/developers/gitignore/api/linux,macos,windows > .gitignore
    ```

    *(Note: Add/Remove templates as appropriate for the specific commit scope).*
2. **Commit** this clean, generated file.
    - **Title Format**: `chore(git): add <template1>, <template2> gitignore rules`
    - **Body**: Explicitly state the source.

        ```text
        Sourced from gitignore.io (https://www.toptal.com/developers/gitignore/api/...)
        ```

### Step 3: Commit B - The User Delta

1. **Compare** the current API-generated `.gitignore` with the backup (`.gitignore.bak`).
2. **Identify the Delta**: Find lines present in the backup that are NOT in the API version. These are the user's custom rules.
3. **Apply** these valid custom rules to the `.gitignore` file (append or patch).
4. **Commit** the user-defined rules.
    - **Strategy**:
        - **Single Commit**: If the delta is small or logically unified (e.g., all Supabase rules), commit as one unit.
        - **Multiple Commits**: If the delta contains distinct concerns (e.g., Supabase rules + unrelated private file exclusions), split them into separate atomic commits.
    - **Title Format**: `feat(git): add project-specific gitignore rules` or `config(<scope>): add custom ignore rules`
    - **Body**: Describe the specific custom rules being added.

---

## 3. Rule Specificity & Standards

- **Markdown Standards**: All documentation and rule files MUST adhere to **[Markdown Generation Rules](./markdown-generation-rules.md)**.
- **Do not mix scopes**: If you are adding OS rules, do not slip in IDE rules in the same commit if they can be separated.
- **No "Jiggling"**: Do not modify the auto-generated content manually unless fixing a strict conflict. Keep the API output intact to ensure reproducibility.
- **Cleanliness**: Remove the backup file (`.gitignore.bak`) only after the final verification is complete.
