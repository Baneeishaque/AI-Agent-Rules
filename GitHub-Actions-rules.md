<!--
title: GitHub Actions
description: Rules for GitHub Actions workflows, covering trigger preferences, security, performance, and integrations.
category: CI/CD & DevOps
-->

# Enhanced GitHub Actions Rules

This document provides a comprehensive guide for an AI tool on how to implement and manage GitHub Actions workflows. It expands upon the core principles outlined in the `CI-CD-rules.md` file and serves as a foundational reference for automating development workflows, ensuring code quality, and streamlining the path from code to production.

---

### 1. Core Principles 💡

The primary purpose of GitHub Actions is to automate tasks in the software development lifecycle. All workflows must adhere to these principles:

* **Automation is Mandatory**: All non-manual tasks, from code linting and testing to deployment, must be automated using GitHub Actions.
* **Reproducibility**: Workflows should be deterministic, meaning they produce the same result every time they are run with the same input.
* **Security**: Workflows must be designed with security in mind, leveraging best practices for handling secrets and permissions.
* **Performance**: Workflows should be optimized for speed and efficiency to minimize feedback loops and resource consumption.
* **Verbosity by Default**: All execution commands in workflows **MUST** include verbose flags (e.g., `--verbose`, `-v`, or `--info` for Gradle) to facilitate debugging and ensure maximum transparency. AI Agents **MUST** also use these flags during local verification *before* applying changes to the codebase.

---

### 2. Workflow Structure and Configuration ⚙️

#### Workflow File Naming
* All GitHub Actions workflow files must be located in the `.github/workflows/` directory.
* **Naming**: File names must be descriptive (e.g., `gradle-build.yml` instead of `ci.yml`) and end with `.yml` or `.yaml`, reflecting the specific technology and purpose.

#### Triggers
* **Event-Driven Priorities**:
    * The preferred trigger for complex, event-driven workflows is **Supabase Functions**, followed by **GitHub's native webhook triggers**. This allows for highly specific workflows not limited to standard events.
* **Standard CI Triggers**:
    * `push`: Trigger on main branches (e.g., `master`, `main`).
    * `workflow_dispatch`: Always include for manual runs.
    * **No Redundant PR Triggers**: Do NOT enable `pull_request` trigger if `push` configuration already covers PR branches/commits to avoid double execution, unless specific PR-only logic is needed.

#### Permissions
* Define explicit permissions for the `GITHUB_TOKEN` to adhere to the principle of least privilege.
* Common requirements:
    * `contents: write` (Required for dependency submission and git operations).
    * `pull-requests: write` (Required for PR comments).

#### Jobs and Steps
* **Jobs**: A workflow is composed of one or more jobs. Each job runs in a separate virtual environment.
* **Steps**: Steps within a job execute commands or run actions. All steps must be clearly named.
* **Matrix Strategy**: For running jobs across multiple versions or environments (e.g., Node.js versions, OS), use a matrix strategy to avoid code duplication.

---

### 3. Optimization and Best Practices 🚀

* **Checkout Action**: Always use `actions/checkout` with `fetch-depth: 1` (or sufficient depth for the task). This retrieves only the latest commit, significantly reducing the amount of data to download. Where applicable, use `sparse-checkout` to retrieve only necessary directories.
* **Caching**:
    * Implement caching for dependencies (e.g., `pub cache` for Flutter, `npm cache` for Node.js) to drastically reduce build times. Caches should be configured to be invalidated when the dependency manifest file changes (`pubspec.lock`, `package-lock.json`).
    * **Gradle Caching**:
        * `cache-cleanup`: Set to `'on-success'`.
        * `gradle-home-cache-includes`: Explicitly list `'caches,notifications,wrapper'`.
        * **Configuration Cache**: Enable in `gradle.properties` (`org.gradle.configuration-cache=true`).
        * **Encryption**: MUST use a GitHub Secret for `cache-encryption-key` (Input: `cache-encryption-key: ${{ secrets.GRADLE_CACHE_ENCRYPTION_KEY }}`).
* **Reusable Workflows**: For common tasks (e.g., building an app, running a security scan), create reusable workflows to promote the **DRY (Don't Repeat Yourself)** principle and centralize logic.
* **Docker Builds**: When building Docker images, explicitly write the build context in your scripts, especially in GitHub Actions.

---

### 4. Security 🛡️

* **Protected Branches**: All deployment branches (e.g., `main`) must be **protected**. This requires that status checks pass and that a minimum number of code reviews are completed before a merge is allowed. This prevents unvetted code from being deployed.
* **Secrets Management**:
    * All sensitive information, such as API keys and credentials, **must** be stored as encrypted GitHub Secrets and accessed via the `secrets` context. Do not hardcode secrets in workflow files or use environment variables in plain text.
* **Permission Scopes**: Use the principle of least privilege. Grant workflows only the necessary permissions to complete their tasks by defining the `permissions` scope at the job or workflow level.
* **Token Rotation**: Implement a regular, automated rotation policy for all credentials and secrets.

---

### 5. Integration with Other Rules 🔗

* **Testing**: Workflows for applications (e.g., Flutter apps) must include steps to run `flutter analyze`, `dart format --set-exit-if-changed .`, and `flutter test` on every pull request. This enforces code quality before merging.
* **Mobile App Workflows**: For mobile apps, workflows should integrate with the `Android-App-Launch-rules.md` to automate emulator setup, testing, and deployment. Workflows for Android should also handle the fallback mechanism for `x86_64` architecture if ARM64 fails.
* **Logging**: All build and test commands in a workflow **MUST** include verbose logging flags (e.g., `--verbose`, `-v`, or `--info` for Gradle) where applicable to ensure maximum visibility into the build process and facilitate debugging.

---

### 6. Java & Gradle Workflow Specifics ☕

#### Runner & Environment
* **Runner**: Use specific LTS versions (e.g., `ubuntu-24.04`) instead of `ubuntu-latest`.
* **Java Setup (Conditional)**:
    * **Identify Version**: Extract the required JDK version from the source Azure pipeline (e.g., `JavaToolInstaller` step).
    * **Research Runners**: Always verify specific GitHub runner capabilities (e.g., Ubuntu 24.04) online to identify pre-installed JDKs and default `JAVA_HOME`. Do NOT rely on static or historical information.
    * **Strategy**: Use dynamic checks for the *specific* identified version environment variable. This approach offers significant advantages by ensuring robustness against runner environment changes and pre-installed JDK path variations. It provides time profit by reducing manual maintenance (especially when Java is already pre-installed, avoiding unnecessary installation time), preventing pipeline failures due to incorrect `JAVA_HOME` settings, and accelerating debugging of Java setup issues.
    * **Scripting**: Use **standalone Bash scripts** (must use `.bash` extension) instead of inline YAML logic for complex checks. This improves readability and testability.
    * **Distribution**: Prefer `oracle` as the **primary choice**. Fall back to `temurin` ONLY if `oracle` does not support the required version. Always verify availability in `actions/setup-java` documentation.
    * **Code Example**:
    ```yaml
    - name: Ensure Java <VERSION>
      id: java-setup
      run: ./.github/scripts/ensure-java.bash
      env:
         REQUIRED_VERSION: '<VERSION>'
      shell: bash

    - name: Install Java <VERSION>
      if: steps.java-setup.outputs.skipped == 'false'
      uses: actions/setup-java@v4
      with:
        distribution: 'oracle' # First choice. Use 'temurin' only if Oracle misses the version.
        java-version: '<VERSION>'
        java-package: 'jdk'
    ```
    *Example `ensure-java.bash`:*
    ```bash
    #!/bin/bash
    # Verify variable name online first! (e.g., JAVA_HOME_21_X64)
    VAR_NAME="JAVA_HOME_${REQUIRED_VERSION}_X64"
    if [ -n "${!VAR_NAME}" ]; then
      echo "Java found at ${!VAR_NAME}. Setting JAVA_HOME."
      echo "JAVA_HOME=${!VAR_NAME}" >> $GITHUB_ENV
      echo "skipped=true" >> $GITHUB_OUTPUT
    else
      echo "Java ${REQUIRED_VERSION} not found. Will install."
      echo "skipped=false" >> $GITHUB_OUTPUT
    fi
    ```

#### Gradle Configuration
* **Action**: Use `gradle/actions/setup-gradle`.
* **Versioning**: Explicitly set `gradle-version: 'wrapper'`.
* **Caching**: Refer to the "Optimization and Best Practices" section for detailed caching configuration (cleanup, includes, encryption).
* **Reporting & Scans**:
    * **Build Scans**:
        * `build-scan-publish: true`
        * `build-scan-terms-of-use-url: 'https://gradle.com/terms-of-service'`
        * `build-scan-terms-of-use-agree: 'yes'`
    * **Dependency Graph**:
        * `dependency-graph: generate-and-submit`
        * **Failure Handling**: Use `continue-on-error: ${{ github.event_name == 'pull_request' }}` to prevent PR blocks on submission failure.
    * **PR Summaries**: Set `add-job-summary-as-pr-comment: 'always'`.
* **Artifacts**: Upload build reports (e.g., `**/build/reports/**`, `**/build/test-results/**`, `**/build/jacoco/**`).

### 7. Workflow Verification & Linting 🔍

*   **Static Analysis (Linting)**:
    *   **Mandatory**: All repositories should implement **Actionlint** to catch syntax errors, missing keys, and security issues in workflow files *before* they fail at runtime.
    *   **Tool**: Use `reviewdog/action-actionlint`.
    *   **Configuration**: Set `fail_level: error` to ensure the build fails on issues.
    ```yaml
    - name: Run actionlint
      uses: reviewdog/action-actionlint@v1
      with:
        fail_level: error
    ```

---

### 8. Mise Tool Management 🔧

#### Action
* Use `jdx/mise-action@v3` to manage tool versions via mise.
* **Version Pinning**: Always specify a mise version to avoid surprises (e.g., `version: '2025.12.9'`).
* **Explicit Install**: Set `install: true` explicitly for clarity.

#### Configuration
* **Config File**: Place `mise.toml` in the appropriate folder (project root, `scripts/`, or any relevant directory).
* **Working Directory Context**:
    * The `working_directory` input in `jdx/mise-action` only applies to the **installation phase** of that specific action.
    * It does **NOT** configure `mise` globally for subsequent steps in the same job.
* **Environment Variable Prefix**:
    * To use a non-root `mise.toml` in subsequent steps without changing the working directory, always prefix the command with `MISE_CONFIG_FILE=<path/to/mise.toml>`.
    * **Example**: `MISE_CONFIG_FILE=scripts/mise.toml mise exec -- <command>`
    * This approach is preferred over using the `-C` or `--cd` flag of `mise exec` if the command being executed relies on the repository root context (e.g., finding project templates, metadata, or other rule files).
* **Caching**: Enable `cache: true` for faster subsequent runs.

#### Code Example
```yaml
- name: Set up tools with mise
  id: mise
  uses: jdx/mise-action@v3
  with:
    version: '2025.12.9'
    install: true
    cache: true
    working_directory: scripts  # Context for installation

- name: Run script with mise
  run: MISE_CONFIG_FILE=scripts/mise.toml mise exec -- ./scripts/my-script.py
```

*Example `mise.toml`:*
```toml
[tools]
python = "3.11"
```

---

### 9. Migration, Verification & Secrets 🕵️

#### Secret Management
* **Secret Creation (Non-Interactive)**:
    * Use `openssl` and `gh secret set` with redirection to avoid interactive prompts and history leaks.
    ```bash
    openssl rand -base64 16 > key.txt
    gh secret set GRADLE_CACHE_ENCRYPTION_KEY < key.txt
    rm key.txt
    ```

#### Verification Protocol
* **Secret Identification & Verification**:
    * Before triggering a workflow for verification, scan the YAML for all `${{ secrets.<NAME> }}` references.
    * Verify that **all** identified secrets (e.g., `SERVER_API_ADDRESS`, `GRADLE_CACHE_ENCRYPTION_KEY`) are correctly configured in the target repository. Do not assume any secret is pre-existing unless verified.
    * For new or missing secrets, follow the "Secret Creation (Non-Interactive)" protocol.
* **Commit & Push Protocol**:
    * **Commit Message**: MUST follow strict rules defined in `Git-Commit-Message-rules.md` (e.g., `ci(workflow): migrate Azure pipeline...`).
    * **Action**: Commit and push changes *before* running verification to ensure the remote state matches the workflow being tested.
* **Automated Monitoring**:
    * Use `gh run list` with JSON output to dynamically grab the Run ID and `gh run watch` to monitor execution.
    ```bash
    # Trigger
    gh workflow run <WORKFLOW_FILE>
    
    # Monitor
    RUN_ID=$(gh run list --workflow <WORKFLOW_FILE> -L 1 --json databaseId -q '.[0].databaseId')
    gh run watch $RUN_ID
    ```

---

### 10. Platinum Standards for Application Workflows 💎

For standard application repositories (not standalone Action repos), follow these "Platinum" practices:

#### 10.1 Folder Structure
* **Workflows**: `.github/workflows/*.yml`
* **Scripts**: `.github/scripts/*.bash` (Keep scripts associated with workflows inside the `.github` directory to clearly separate CI logic from application code).

#### 10.2 Industrial Linting
* **Always** include a `lint` job.
* **ShellCheck**: **Mandatory** for all Bash scripts (e.g., in `.github/scripts/`). All scripts must pass ShellCheck without errors.
* **Actionlint**: Required for workflow syntax, set to `fail_level: error`.
* **Dependencies**: The primary `build` or `deploy` job MUST `need` the `lint` job to ensure quality before execution.

#### 10.3 Version Pinning
* **Mandatory Semantic Versioning**: All GitHub Actions (`uses: ...`) **MUST** be pinned to a specific, full semantic version (e.g., `@2.0.0`, `@v4.1.7`).
* **Marketplace Discovery**: Before using any action, the AI Agent **MUST** visit the GitHub Marketplace to identify the absolute latest stable version/tag.
* **Prohibited Tags**: Do **NOT** use mutable tags such as `@v2`, `@master`, or `@main`. This prevents unexpected breaks.
* **Version Format**: Be aware that some actions (e.g., `ludeeus/action-shellcheck`) use semantic versions **without** the `v` prefix. Always verify the correct tag format on the Marketplace.
* **Example**: `uses: actions/checkout@v4.1.7` (latest semantic) instead of `@v4`.

#### 10.4 Configuration Example
```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run ShellCheck
        uses: ludeeus/action-shellcheck@2.0.0
        with:
          scandir: './.github/scripts'
      - name: Run actionlint
        uses: reviewdog/action-actionlint@v1
        with:
          fail_level: error

  build:
    needs: lint
    runs-on: ubuntu-latest
    # ...
```