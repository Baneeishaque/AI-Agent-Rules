<!--
title: GitHub Repo Metadata Rules
description: Ultra-Lean Industrial protocols for Metadata-as-Code (MaC), using README.md as the absolute Single Source of Truth with visible markers for automation.
category: Git & Repository Management
-->

# GitHub Repository Metadata Management Rules

This document defines the "Ultra-Lean Industrial" pattern for repository metadata. It transitions management to a "Metadata-as-Code" (MaC) approach where the **README.md** is the **Single Source of Truth** to ensure reliable parsing while keeping content professional and human-readable.

***

### 1. The "Ultra-Lean Industrial" Strategy

In this pattern, all metadata (description and topics) is managed directly within the visible content of the `README.md`. A GitHub Action parses this document to synchronize settings with the GitHub repository.

-   **Single Source of Truth**: The **`README.md`** file in the root.
-   **Visible Markers**: Automation uses markers around human-readable content.
-   **No Redundant Files**: No separate `GITHUB_TOPICS.md` or metadata documentation is required.

***

### 2. Standard Implementation (README-as-Source)

#### 2.1 Metadata Markers
The AI must use the following visible markers to ensure reliable parsing while maintaining a professional appearance:

-   **Badges**: 
    ```markdown
    <!-- START_BADGES -->
    [![Badge1](URL1)](Link1) [![Badge2](URL2)](Link2)

    [![Badge3](URL3)](Link3)
    <!-- END_BADGES -->
    ```
-   **Description**: 
    ```markdown
    <!-- START_DESCRIPTION -->
    A professional one-sentence summary of the project.
    <!-- END_DESCRIPTION -->
    ```
-   **Topics Section**: 
    ```markdown
    ## 🏷️ GitHub Topics
    <!-- START_METADATA -->
    | Category | Topics |
    | :--- | :--- |
    | **Category Name** | `topic-1` `topic-2` |
    <!-- END_METADATA -->
    ```

#### 2.2 Automation Workflow (`.github/workflows/sync-metadata.yml`)
The AI must create a **GitHub Action** which serves as the **Executor**. The Action MUST implement the following logic:
1.  **Track**: Listen for changes specifically to `README.md`.
2.  **Parse**: Extract content between `START_DESCRIPTION` and `END_DESCRIPTION`.
3.  **Extract**: Identify all topics from the table between `START_METADATA` and `END_METADATA`.
4.  **Prioritize**: The **first 20 topics** discovered in the table (Top-to-Bottom, Left-to-Right) are designated for GitHub repository settings.
5.  **Sync**: 
    -   **Primary (GH CLI)**: `gh repo edit ${{ github.repository }} --description "$DESC" --add-topic topic1 --add-topic topic2 ...`
    -   **Secondary Fallback (Rest API)**: If the CLI is unavailable inside the runner, attempt a direct API call:
        ```bash
        curl -L -X PUT -H "Accept: application/vnd.github+json" \
          -H "Authorization: Bearer ${{ secrets.GITHUB_TOKEN }}" \
          https://api.github.com/repos/${{ github.repository }}/topics -d "{\"names\":$TOPICS_JSON}"
        ```

***

### 3. AI Architecture & SEO Governance

These rules govern the AI's role as the **Project Architect** for metadata:

-   **SEO Analysis & Keyword Ranking**: 
    -   The AI must investigate the code to identify the most descriptive summary and maximum high-traffic technical keywords.
    -   **Ranking System**: Any number of topics can be identified, but they must be **ranked by impact**. The most powerful, high-traffic keywords MUST be placed in the **first 20 slots** of the metadata table to ensure they are synchronized to GitHub's functional search settings.
-   **Topic Format & Visibility**: 
    -   **Format**: Strictly lowercase, hyphen-separated (kebab-case).
    -   **Full Visibility**: The `README.md` must display **ALL** suggested topics (categorized) to maximize human discoverability, project documentation, and overall SEO.
-   **Badge Discovery & Popularity Ranking**: 
    -   The AI must analyze the tech stack and identify appropriate [Shields.io](https://shields.io/) badges.
    -   **Ranking & Arrangement**:
        -   Badges must be **ranked by popularity and impact**.
        -   **Categorization**: Group badges by category (e.g., Core Tech, Status/Quality, License, Deployment).
        -   **Single-Line Layout**: Place badges from the **same category on a single line**, space-separated.
        -   **Visual Separation**: Use **line breaks between different categories** to ensure a professional, industrial aesthetic.
-   **Incremental Placement**: If markers or content already exist and are correct, the AI will skip redundant placements to minimize commit noise.

***

### 4. Onboarding & Verification Protocol

To implement this pattern, the AI agent must:

1.  **Draft**: Identify description, badges, and categorized keywords (Maximum visibility).
2.  **Initialize Source**: 
    - Create/Update `README.md` with badges, description, and topics wrapped in markers.
    - If modifying a submodule, strictly follow [Git-Submodule-rules.md](./Git-Submodule-rules.md) (e.g., branch checkout before edits).
3.  **Establish Automation**: Create and commit the `sync-metadata.yml` workflow.
4.  **Commit**: Use strict [Git-Commit-Message-rules.md](./Git-Commit-Message-rules.md) (e.g., `docs: initialize automated metadata-as-code workflow`).
5.  **Watch & Verify**: 
    - Monitor the Action execution following [github-actions-rules.md](./github-actions-rules.md).
    - Once successful, perform a final, one-time verification of repository metadata via `gh repo view --json repositoryTopics,description`.

*Updated: December 2025*
