<!--
title: Git Repository Creation
description: Standardized rules for creating new repositories, including naming conventions, essential file generation, and initial commit best practices.
category: Git & Repository Management
-->

# Git Repository Creation Rules

This document outlines a comprehensive set of rules and best practices for creating new Git repositories, specifically tailored for an AI tool to ensure consistency, quality, and long-term maintainability. The goal is to establish a foundational, self-documenting, and easily navigable project from its very first commit.

***

### 1. Core Principles

-   **Reproducibility**: A new repository must be initialized in a way that allows any team member or automated system to clone it and begin work with minimal friction.
-   **Consistency**: Adherence to a single standard ensures that all projects share a common structure and naming, reducing cognitive load and errors across the board.
-   **Clarity**: The repository's purpose, structure, and usage instructions must be immediately clear from the top-level files. The **`README.md`** is the primary tool for this.
-   **Automation**: The process should be fully automatable, from naming to initial file generation, requiring no manual intervention from the AI.

***

### 2. Naming Convention

-   **Default Convention**: All new Git repository and corresponding project folder names must use **`hyphenated-names`** (kebab-case). This convention is widely supported, highly readable, and avoids issues with case-insensitivity on some operating systems.
    -   **Example**: `flutter-todo-app`, `web-api-service`, `personal-blog-project`.
-   **Exceptions**:
    -   **Tool-Specific Requirements**: If a specific tool or language ecosystem mandates a different convention (e.g., Dart packages typically use `snake_case`), this rule can be overridden. The AI tool must be aware of these exceptions and apply them as necessary.
    -   **AI Tooling**: The AI itself should be configured to handle these naming exceptions gracefully and only when a clear, documented rule exists for a specific project type.
-   **Location**: All repositories will be cloned or created in a designated root directory, such as `~/projects/` or `~/sample/path/`. This centralization simplifies management and discovery.

***

### 3. Essential Files and Initial Commit

The first commit to any new repository is critical. It should establish a solid foundation by including all essential files.

-   **`README.md`**: A comprehensive `README.md` file must be generated automatically. It should be the single source of truth for the project.
    -   **Sections to Include**:
        -   **Title and Overview**: A clear, concise project title and a one-sentence summary of its purpose.
        -   **Getting Started**: Detailed, step-by-step instructions for setting up the development environment and running the project for the first time.
        -   **Key Commands**: A list of common commands (e.g., `npm run dev`, `flutter run`, `docker-compose up`).
        -   **File Structure**: A brief overview of the top-level directory structure.
        -   **Contributing**: A link to a `CONTRIBUTING.md` file if applicable.
        -   **License**: A reference to the chosen license.
-   **`.gitignore`**: A language or framework-specific `.gitignore` file must be generated to prevent unnecessary files (e.g., `node_modules`, `build/`, `.idea/`) from being committed to the repository. The AI should use a robust, pre-configured template for the specific project type.
-   **`LICENSE`**: A `LICENSE` file must be included. The AI tool should default to a standard open-source license (e.g., MIT, Apache 2.0) unless a different license is specified in the user's request.
-   **Initial Commit Message**: The very first commit must have a standardized, descriptive message following the **Conventional Commits** specification.
    -   **Format**: `feat: Initial repository setup` or `chore: Initial project creation`.

***

### 4. Project Structure

A standardized folder structure improves clarity and navigation for all developers.

-   **Source Code (`src/` or `lib/`)**: All application source code should reside in a top-level `src/` or `lib/` directory. This separates the core logic from configuration and documentation.
-   **Documentation (`docs/`)**: For extensive documentation, a dedicated `docs/` folder should be created to house project guides, API references, and architectural decisions.
-   **Assets (`assets/`)**: All static assets, such as images, fonts, and icons, should be organized in a separate `assets/` directory.
-   **Configurations (`config/`)**: Configuration files for various environments (e.g., `development`, `production`) can be grouped in a `config/` folder.

***

### 5. Adherence and Verification

The AI tool is responsible for ensuring these rules are followed in every repository it creates.

-   **Pre-Flight Check**: Before initiating the repository creation, the AI should validate the proposed name and location against these rules.
-   **Post-Creation Audit**: After creating the repository, the AI must perform a quick audit to confirm the presence of all mandatory files (`README.md`, `.gitignore`, `LICENSE`) and the correct initial commit message.
-   **Error Reporting**: If any rule is violated during the process, the AI must log the error, halt the process, and report the issue to the user with a clear explanation of what went wrong and how to fix it.
