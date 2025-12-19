<!--
title: GitHub Action Creation Rules
description: Strict guidelines for creating, structuring, and publishing GitHub Composite Actions to the Marketplace. enforce "Industrial" standards.
category: GitHub Actions
-->

# GitHub Action Creation Rules

> [!IMPORTANT]
> These rules apply **ONLY** to repositories dedicated to creating and publishing **GitHub Actions** (Composite, Docker, or JavaScript actions) to the Marketplace. Standard application repositories using GitHub Actions workflows should follow `GitHub-Actions-rules.md`.

This document outlines the **Mandatory Standard Operating Procedure (SOP)** for creating new GitHub Actions. All Actions created by the AI Agent must follow this structure to ensure maintainability, extensibility, and Marketplace compatibility.

---

### 1. Naming Conventions

-   **Repository Name**: Must end with `-action` (e.g., `my-tool-setup-action`).
    -   *Constraint*: Must strictly follow **kebab-case** as per `Git-Repository-rules`.
-   **Action Name**: Kebab-case, concise (e.g., `my-tool-setup`).
    -   *Location*: `action.yml` -> `name:`.
-   **Usage**: `uses: <owner>/<repo-name>@<full-semantic-version>` (e.g., `@2.0.0`, `@v1.0.0`).
-   **Discovery**: Always check the Marketplace for the latest stable version before implementation.

---

### 2. Industrial Directory Structure

The repository **MUST** follow this structure. Do not dump scripts in the root.

```text
.
├── .github/
│   └── workflows/
│       └── test.yml        # Self-test logic (REQUIRED)
├── src/
│   └── main.sh             # Core logic scripts (or main.js)
├── tests/
│   └── test-config.toml    # Configuration files specific to testing
├── action.yml              # Action definition
├── README.md               # Documentation
├── LICENSE                 # MIT License
├── CONTRIBUTING.md         # Community guidelines
├── SECURITY.md             # Security policy
├── CODE_OF_CONDUCT.md      # Contributor Covenant
└── .gitignore              # Generated via gitignore.io
```

---

### 3. Essential File Standards

#### `action.yml`
-   **Inputs**: Must define `required: true/false` and `description`.
-   **Branding**: Must include `icon` and `color`.
-   **Runs**: Use `using: "composite"` for shell-based actions.
    -   *Pathing*: Use `${{ github.action_path }}/src/...` to reference scripts.

#### `README.md`
-   **Badges**: Must include Shield.io badges for:
    -   GitHub Release (`v/release`)
    -   Workflow Status (`workflow/status`)
    -   License (`license`)
-   **Usage Example**: Provide a clear YAML snippet of how to use the action.
-   **Features**: Bullet points listing key capabilities.
-   **Inputs Table**: Detailed table of all inputs.

#### `.gitignore`
-   **Generation**: MUST use the `gitignore.io` API.
-   **Command**: `curl -L https://www.gitignore.io/api/windows,linux,macos,visualstudiocode,git > .gitignore`

#### `.github/workflows/test.yml`
-   **Trigger**: `on: [push, pull_request]`.
-   **Job**: Must actually run the action locally (`uses: ./`) and verify output.
-   **Purpose**: Ensures the action is broken before release.

---

### 4. Platinum Linting Standards 💎

To achieve "Platinum" quality, all Actions **MUST** include a `lint` job in their CI pipeline (`test.yml`).

#### Requirements
1.  **Script Analysis**: Use `shellcheck` for all shell scripts.
    -   *Action*: `ludeeus/action-shellcheck`
2.  **Workflow Analysis**: Use `actionlint` to verify `action.yml` and workflow syntax.
    -   *Action*: `reviewdog/action-actionlint`
    -   *Config*: Must set `fail_level: error`.

#### CI Configuration Example
```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run ShellCheck
        uses: ludeeus/action-shellcheck@2.0.0
        with:
          scandir: './src'
      - name: Run actionlint
        uses: reviewdog/action-actionlint@v1
        with:
          fail_level: error
  test:
    needs: lint
    # ... test steps
```

---

### 5. Creation & Publishing Workflow

Follow this sequence strictly.

#### Phase 1: Local Setup
1.  **Scaffold**: Create directories (`src`, `tests`, `.github`) and files.
2.  **Git Init**: `git init -b main`.
3.  **Commit**: `git add . && git commit -m "feat: Initial repository setup"`.

#### Phase 2: Remote & Metadata
4.  **Create Repo**:
    ```bash
    gh repo create <owner>/<repo-name> --public --source=. --remote=origin --push
    ```
5.  **Edit Metadata** (CRITICAL for Discovery):
    -   **Requirement**: Add as many relevant topics as possible.
    ```bash
    gh repo edit <owner>/<repo-name> \
      --description "Clear description..." \
      --add-topic "github-actions" \
      --add-topic "ci-cd" \
      --add-topic "automation" \
      --add-topic "devops" \
      --add-topic "workflow" \
      --add-topic "developer-tools" \
      --add-topic "action"
    ```

#### Phase 3: Release & Marketplace
6.  **Create Release**:
    ```bash
    gh release create v1.0.0 --title "v1.0.0 Initial Release" --generate-notes
    ```
7.  **Manual Verification (Agent Instructions)**:
    -   **Display URL**: You MUST provide the direct link to the Release page for the user.
    -   **Fetch Categories**: You MUST first **search online** (or use `gh` / GitHub API) to verify the current list of valid GitHub Marketplace categories. Do NOT guess.
    -   **Suggest Categories**: Explicitly suggest the best fitting **Primary** and **Secondary** categories based on the fetched list.
    -   **Instructions**:
        1.  Go to **GitHub Release UI** (link provided).
        2.  Click **Edit** on `v1.0.0`.
        3.  **Check**: `[x] Publish this Action to the GitHub Marketplace`.
        4.  **Select Categories**: (As suggested above).
        5.  **Accept Terms**: Required for the first release of any account.

---

### 6. Maintenance
-   **Refactoring**: If moving files, ensure `action.yml` paths are updated.
-   **Versioning**: Use Semantic Versioning (`v1.0.0`, `v1.1.0`).
-   **Marketplace Hygiene**: Regularly verify that the latest version recommended in the "Use latest version" popup on the Marketplace matches your implementation.
