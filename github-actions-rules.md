<!--
title: GitHub Actions Rules
description: Rules for GitHub Actions workflows, covering trigger preferences, security, performance, and integrations.
category: CI/CD & DevOps
-->

# Enhanced GitHub Actions Rules

This document provides a comprehensive guide for an AI tool on how to implement and manage GitHub Actions workflows. It expands upon the core principles outlined in the `ci-cd-rules.md` file and serves as a foundational reference for automating development workflows, ensuring code quality, and streamlining the path from code to production.

***

### 1. Core Principles

The primary purpose of GitHub Actions is to automate tasks in the software development lifecycle. All workflows must adhere to these principles:

* **Automation is Mandatory**: All non-manual tasks, from code linting and testing to deployment, must be automated using GitHub Actions.
* **Reproducibility**: Workflows should be deterministic, meaning they produce the same result every time they are run with the same input.
* **Security**: Workflows must be designed with security in mind, leveraging best practices for handling secrets and permissions.
* **Performance**: Workflows should be optimized for speed and efficiency to minimize feedback loops and resource consumption.
* **Verbosity by Default**: All execution commands in workflows **MUST** include verbose flags (e.g., `--verbose`, `-v`, or `--info` for Gradle) to facilitate debugging and ensure maximum transparency. AI Agents **MUST** also use these flags during local verification *before* applying changes to the codebase.

***

### 2. Workflow Structure and Configuration

#### Workflow File Naming
* All GitHub Actions workflow files must be located in the `.github/workflows/` directory.
* **Naming**: File names must be descriptive (e.g., `gradle-build.yml` instead of `ci.yml`) and end with `.yml` or `.yaml`, reflecting the specific technology and purpose.

#### Triggers
* **Event-Driven Priorities**:
    * The preferred trigger for complex, event-driven workflows is **Supabase Functions**, followed by **GitHub's native webhook triggers**. This allows for highly specific workflows not limited to standard events.
* **Orchestration**: The deployment workflow follows the architectural pattern defined in `ci-cd-rules.md` (`Supabase → GitHub Actions → Render`).
    * **Executor Role:** GitHub Actions receives the webhook payload from Supabase, runs the build/test jobs, and triggers the deployment upon success.
* **Standard CI Triggers**:
    * `push`: Trigger on main branches (e.g., `master`, `main`).
    * `workflow_dispatch`: Always include for manual runs.
    * **No Redundant PR Triggers**: Do NOT enable `pull_request` trigger if `push` configuration already covers PR branches/commits to avoid double execution, unless specific PR-only logic is needed.

#### Permissions
* Define explicit permissions for the `GITHUB_TOKEN` to adhere to the principle of least privilege.
* **OIDC Integration**: When integrating with cloud providers (AWS, GCP, Azure), use **OpenID Connect (OIDC)** instead of long-lived secrets. 
    * **Requirement**: Must include `permissions: id-token: write` and `contents: read` at the job or workflow level.
* Common requirements:
    * `contents: write` (Required for dependency submission and git operations).
    * `pull-requests: write` (Required for PR comments).

#### Jobs and Steps
* **Jobs**: A workflow is composed of one or more jobs. Each job runs in a separate virtual environment.
* **Steps**: Steps within a job execute commands or run actions. All steps must be clearly named.
* **Matrix Strategy**: For running jobs across multiple versions or environments (e.g., Node.js versions, OS), use a matrix strategy to avoid code duplication.

***

### 3. Optimization and Best Practices

* **Checkout Action**: Always use `actions/checkout` with `fetch-depth: 1` (or sufficient depth for the task). This retrieves only the latest commit, significantly reducing the amount of data to download. Where applicable, use `sparse-checkout` to retrieve only the necessary directories.
* **Caching**:
    * Implement caching for dependencies (e.g., `pub cache` for Flutter, `npm cache` for Node.js) to drastically reduce build times. Caches should be configured to be invalidated when the dependency manifest file changes (`pubspec.lock`, `package-lock.json`).
    * **Gradle Caching**:
        * `cache-cleanup`: Set to `'on-success'`.
        * `gradle-home-cache-includes`: Explicitly list `'caches,notifications,wrapper'`.
        * **Configuration Cache**: Enable in `gradle.properties` (`org.gradle.configuration-cache=true`).
        * **Encryption**: MUST use a GitHub Secret for `cache-encryption-key` (Input: `cache-encryption-key: ${{ secrets.GRADLE_CACHE_ENCRYPTION_KEY }}`).
* **Reusable Workflows**: For common tasks (e.g., building an app, running a security scan), create reusable workflows to promote the **DRY (Don't Repeat Yourself)** principle and centralize logic.
* **Docker Builds**: When building Docker images, explicitly write the build context in your scripts, especially in GitHub Actions.
* **Conditional Step Execution**:
    * **Strategy**: Use a helper script to detect file changes before running expensive steps (e.g., API calls, heavy builds).
    * **Mechanism**: Use `git status --porcelain <files>` to check for modifications. If changes exist, set a step output or environment variable (e.g., `has_changes=true`).
    * **Benefits**:
        * **Performance**: Skips heavy dependency installation and API calls when unnecessary.
        * **Efficiency**: Reduces CI/CD minutes usage.
        * **Clean Logs**: Avoids "nothing to commit" noise or complex skip logic inside downstream actions.
* **Complex Scripting**:
    * **Mandatory**: Use **standalone Bash scripts** (must use `.bash` extension) instead of inline YAML logic for any complex logic, loops, or multi-line commands.
    * **Location**: Store scripts in `.github/scripts/`.
    * **Benefits**: Improves readability, enables ShellCheck verification, and allows for local testing of CI logic.
    * **Example**:
      ```yaml
      - name: Preparation Step
        run: ./.github/scripts/prepare-something.bash
        shell: bash
      ```
    * **Example**:
      ```yaml
      - name: Check for changes
        id: check_changes
        run: ./scripts/check_changes.bash
      - name: Expensive Step
        if: steps.check_changes.outputs.has_changes == 'true'
        run: ...
      ```

***

### 4. Security

* **Protected Branches**: All deployment branches (e.g., `main`, `store-guidelines-branches`) must be **protected**. This requires that status checks pass and that a minimum number of code reviews are completed before a merge is allowed. This prevents unvetted code from being deployed.
* **Secrets Management**:
    * All sensitive information, such as API keys and credentials, **must** be stored as encrypted GitHub Secrets and accessed via the `secrets` context.
    * **WARNING**: **Do NOT hardcode secrets** in YAML files or scripts, even for testing. This is a critical security violation.
    * **Configuration Repo Strategy**: For complex environment management, use a private, secure configuration repository. The CI/CD pipeline should be configured via secrets to access this repo, pull environment-specific manifest files, and apply them.
* **Permission Scopes**: Use the principle of least privilege. Grant workflows only the necessary permissions to complete their tasks by defining the `permissions` scope at the job or workflow level.
* **Token Rotation**: Implement a regular, automated rotation policy for all credentials and secrets.

***

### 5. Integration with Other Rules

* **Testing**: Workflows for applications (e.g., Flutter apps) must include steps to run `flutter analyze`, `dart format --set-exit-if-changed .`, and `flutter test` on every pull request. This enforces code quality before merging.
* **GitHub Actions Workflow (Mobile)**: The workflow will be triggered on a push to the `main` branch or on a pull request. The workflow will run `flutter analyze` and `flutter test --coverage` to ensure code quality and test coverage.
* **Mobile App Workflows**: For mobile apps, workflows should integrate with the `android-app-launch-rules.md` to automate emulator setup, testing, and deployment. Workflows for Android should also handle the fallback mechanism for `x86_64` architecture if ARM64 fails.
* **Web Service Workflows (Render)**:
    * **Deployment**: Use the Render CLI or API for triggering deployments. 
    * **Synchronous Monitoring**: When using the CLI, always use the `--wait` flag to block the job until deployment completes or fails.
    * **Error Handling**: Implement a `fail-fast` strategy. If a deployment fails, the workflow MUST fetch the latest logs from the Render API/CLI and post them to the PR or a dedicated channel for debugging.
* **Logging**: All build and test commands in a workflow **MUST** include verbose logging flags (e.g., `--verbose`, `-v`, or `--info` for Gradle) where applicable to ensure maximum visibility into the build process and facilitate debugging.

***

### 5.1 Deployment Strategies
* **Implementation**: For mission-critical applications, implement **Canary** or **Blue/Green** deployments using GitHub Actions environments and deployment protections.
* **Environment Gates**: Use manual approvals or "wait" timers for canary rollouts.
* **Rollback Strategy**: Always include a "Rollback" workflow or a mechanism to trigger a fast-revert to the last known stable tag.

***

### 6. Java & Gradle Workflow Specifics

#### Runner & Environment
* **Runner**: Use specific LTS versions (e.g., `<LTS_VERSION>`) instead of `ubuntu-latest`.
* **Java Setup (Conditional)**:
    * **Identify Version**: Extract the required JDK version from the source Azure pipeline (e.g., `JavaToolInstaller` step).
    * **Research Runners**: Always verify specific GitHub runner capabilities (e.g., Ubuntu 24.04) online to identify pre-installed JDKs and default `JAVA_HOME`. Do NOT rely on static or historical information.
    * **Strategy**: Use dynamic checks for the *specific* identified version environment variable. This approach offers significant advantages by ensuring robustness against runner environment changes and pre-installed JDK path variations. It provides time profit by reducing manual maintenance (especially when Java is already pre-installed, avoiding unnecessary installation time), preventing pipeline failures due to incorrect `JAVA_HOME` settings, and speeding up debugging of Java setup issues.
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
      uses: actions/setup-java@<LATEST_VERSION>
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

***

### 6.1 Release Workflow Standards
For stable releases and publishing (App Store, Web deployment), workflows MUST:
* **Checklist**:
    1.  Validate/Bump version tags.
    2.  Build the application/service.
    3.  Upload artifacts with the naming convention `client-name/version/environment`.
    4.  Market stable builds as "Release" and test-only builds as "Pre-release."
    5.  Trigger notifications (WhatsApp, Team Channels).
    6.  Direct Message (DM) testers with pre-signed download links.
* **Automated Workflow**: Implement the artifact management strategy from `ci-cd-rules.md`. Upload builds using `actions/upload-artifact`, generate pre-signed links for testers via CLI, and apply lifecycle policies.
* **Automated Distribution**: Upon a successful release build, the artifact will be automatically uploaded to Firebase App Distribution using a dedicated GitHub Action (e.g., `willynohilly/firebase-app-distribution`). The pipeline will then notify a pre-defined group of internal testers, making new builds instantly available for testing. Sensitive credentials like the Google Service Account key (`${{ secrets.GOOGLE_SERVICE_ACCOUNT_KEY }}`) and Flutter signing keys (`${{ secrets.FLUTTER_SIGNING_KEYS }}`) will be securely stored as encrypted GitHub Secrets.

### 7. Workflow Verification & Linting

*   **Static Analysis (Linting)**:
    *   **Mandatory**: All repositories should implement **Actionlint** to catch syntax errors, missing keys, and security issues in workflow files *before* they fail at runtime.
    *   **Tool**: Use `reviewdog/action-actionlint`.
    *   **Configuration**: Set `fail_level: error` to ensure the build fails on issues.
    ```yaml
    - name: Run actionlint
      uses: reviewdog/action-actionlint@<LATEST_VERSION>
      with:
        fail_level: error
    ```

#### 7.2 Quality Gates & Security Scans
* **Security Scans**:
    * **Application Scans**: Always include vulnerability checks for package managers:
        * **Node.js**: Use `npm audit` on every build.
        * **Maven**: Use the `maven-dependency-plugin` or similar to check for vulnerable dependencies.
    * **Vulnerability Scanning**: Use **Snyk** as the primary security gate. 
        * Use the official `snyk/actions` (e.g., `snyk/actions/node` or `snyk/actions/python-3.10`).
        * Store the `SNYK_TOKEN` as a secure secret.
* **Code Coverage**: 
    * Integrate with **Codecov** or **Coveralls**.
    * Use the respective GitHub Actions (e.g., `codecov/codecov-action`) to upload reports using a secret token.
* **Static Analysis & Quality Gates**: Implement the quality gates strategy defined in `ci-cd-rules.md` directly within GitHub Actions.
    * **Integration Choice**: 
        * **Recommended**: Install the SonarQube GitHub App for organization-level integration and automatic PR decoration.
        * **Alternative**: Use the `sonarsource/sonarqube-scan-action` if individual repository fine-tuning or a CLI-driven analyzer is required.

***

### 8. Mise Tool Management



#### Action, Tool Version Pinning, and Execution (Strict)

* Use `jdx/mise-action@<LATEST_VERSION>` to manage tool versions via mise.
* **Mise Tool Version Pinning**: The `version:` input for the mise action **MUST** always be set to the latest stable release of the mise tool itself (not just the action). This version **MUST** be verified via live lookup (GitHub API, Marketplace, or `gh release list --repo jdx/mise`). Always specify a mise version to avoid surprises (e.g., `version: '<MISE_VERSION>'`).
* **All Tool Execution via mise**: All CLI tool execution (e.g., pip, python, node, npm, etc.) in workflows **MUST** be performed using `mise exec -- <tool> ...` to guarantee environment consistency and reproducibility. Direct invocation of tools without mise is strictly prohibited.
* **Mise Caching**: The `cache: true` input for the mise action **MUST** always be set, to enable caching of tool downloads and speed up workflow execution. This is required for all jobs using mise.
* **Explicit Install**: Set `install: true` explicitly for clarity.

#### Configuration
* **Config File**: Place `mise.toml` in the appropriate folder (project root, `scripts/`, or any relevant directory).
* **Working Directory Context**:
    * The `working_directory` input in `jdx/mise-action` only applies to the **installation phase** of that specific action.
    * It does **NOT** configure `mise` globally for later steps in the same job.
* **Environment Variable Block**:
    * To use a non-root `mise.toml` in later steps without changing the working directory, set `MISE_CONFIG_FILE: <path/to/mise.toml>` in the `env:` block (at the job or step level).
    * **Example**: See "Code Example" below for correct placement in `env:`.
    * This approach is preferred over using the `-C` or `--cd` flag of `mise exec` if the command being executed relies on the repository root context (e.g., finding project templates, metadata, or other rule files).
    * **Caution**: Avoid inline prefixes (e.g., `VAR=val cmd`) when the command is passed as a string variable in scripts, as bash may not interpret them correctly.
* **Caching**: Enable `cache: true` for faster later runs.

#### 8.2 Platinum Mise Setup (Recommended)
* **Action**: For robust tool verification, use `Baneeishaque/mise-setup-verification-action`.
* **Benefits**: Combines setup and automated verification of the tool installation and versioning.
* **Usage**:
    ```yaml
    - uses: Baneeishaque/mise-setup-verification-action@<COMMIT_SHA>
      with:
        mise_version: '<MISE_VERSION>'
        working_directory: 'scripts'
        tool_name: 'python'
        version_command: 'python -V'
    ```
* **Note**: Always pin to a specific commit SHA for stability.

#### Code Example
```yaml
jobs:
  <JOB_NAME>:
    runs-on: ubuntu-latest
    env:
      MISE_CONFIG_FILE: <PATH_TO_MISE_TOML>
    steps:
      - uses: actions/checkout@<LATEST_VERSION>
      - name: Set up tools with mise
        id: mise
        uses: jdx/mise-action@<LATEST_VERSION>
        with:
          version: '<MISE_VERSION>'
          install: true
          cache: true
          working_directory: <WORKING_DIRECTORY>  # Context for installation

      - name: Run script with mise
        run: mise exec -- ./<PATH_TO_SCRIPT>
```

*Example `mise.toml`:*
```toml
[tools]
<TOOL_NAME> = "<VERSION>"
```

***

### 9. Migration, Verification & Secrets

#### Secret Management
* **Secret Creation (Non-Interactive)**:
    * Use `gh secret set <NAME> < <FILE>` with redirection to avoid interactive prompts and history leaks.
    * **Note**: For encryption keys or other generated values, use tools like `openssl` to generate the file first.
    ```bash
    # Example for GRADLE_CACHE_ENCRYPTION_KEY
    openssl rand -base64 16 > key.txt
    gh secret set GRADLE_CACHE_ENCRYPTION_KEY < key.txt
    rm key.txt

    # Example for existing secret
    echo "existing-secret-value" > secret.txt
    gh secret set EXISTING_SECRET < secret.txt
    rm secret.txt
    ```

#### Verification Protocol
* **Secret Identification & Verification**:
    * Before triggering a workflow for verification, scan the YAML for all `${{ secrets.<NAME> }}` references.
    * Verify that **all** identified secrets (e.g., `SERVER_API_ADDRESS`, `GRADLE_CACHE_ENCRYPTION_KEY`) are correctly configured in the target repository. Do not assume any secret is pre-existing unless verified.
    * For new or missing secrets, follow the "Secret Creation (Non-Interactive)" protocol.
* **Commit & Push Protocol**:
    * **Compliance**: MUST obey strict rules defined in `Git-Commit-Message-rules.md` and `Git-Submodule-rules.md` before pushing. This ensures a clean history and stable submodules.
    * **Commit Message**: Use conventional commit format (e.g., `fix(ci): ...`).
    * **Action**: Stage, commit, and push changes *before* proceeding to verification to ensure the remote state matches the workflow being tested.
* **Automated Monitoring**:
    * **Check for Auto-Trigger**: After pushing, first check if the push event already triggered the workflow using `gh run list --limit 1`.
    * **Watch Existing Run**: If a relevant run is already in progress or queued, use `gh run watch <RUN_ID>` to monitor it instead of dispatching a new one.
    * **Dispatch (Fallback)**: Use `gh workflow run <WORKFLOW_FILE>` ONLY if no run was triggered automatically or if a manual re-run is needed for specific state verification.
    * **Dynamic Monitoring**: Use `gh run list` with JSON output to dynamically grab the Run ID and `gh run watch` to monitor execution.
    ```bash
    # 1. Check for recent runs
    gh run list --workflow <WORKFLOW_FILE> --limit 1

    # 2. Trigger (Fallback: Only if no auto-run found)
    gh workflow run <WORKFLOW_FILE>

    # 3. Monitor (Grab latest Run ID and watch)
    RUN_ID=$(gh run list --workflow <WORKFLOW_FILE> -L 1 --json databaseId -q '.[0].databaseId')
    gh run watch $RUN_ID
    ```

* **Google Sheets Tracking (Upon Explicit Request)**: A Google Sheets tracking system will be implemented to log key development events *only when explicitly requested*.
    * **Implementation**: Use a specialized action (e.g., `google-github-actions/setup-gcloud` or a dedicated Sheets action) to fulfill the logging policy defined in `ci-cd-rules.md`.
    * **Mechanism**: Using a service account JSON stored as a GitHub Secret (`${{ secrets.GOOGLE_SHEETS_SERVICE_ACCOUNT }}`), the Sheets API will be called from an action to append rows.
    * **Idempotency**: Every row insertion MUST be keyed by a combination of `PR_NUMBER` and `COMMIT_SHA` to prevent duplicates.

* **Notification Strategy**: Follow the categorization (Urgent vs. Team) defined in `ci-cd-rules.md`.
* **WhatsApp Notifications (Upon Explicit Request)**:
    * **Implementation**: Use a specialized action or `curl` to the WhatsApp Cloud API.
    * **Trigger**: Failures or major releases.
    * **Content**: Must include direct links to logs. Format must be clean: avoid `?mode` fragments in URLs and include the `<SOCIAL_HANDLE>` handle where required.
* **Supabase Storage (Artifacts)**:
    * **Naming Convention**: Artifacts must be tagged as `client-name/version/environment`.
    * **Lifecycle**: Implement cleanup steps in the workflow to prune short-lived feature branch builds.

***

### 10. Platinum Standards for Application Workflows

For standard application repositories (not standalone Action repos), follow these "Platinum" practices:

#### 10.1 Folder Structure
* **Workflows**: `.github/workflows/*.yml`
* **Scripts**: `.github/scripts/*.bash` (Keep scripts associated with workflows inside the `.github` directory to clearly separate CI logic from application code).

#### 10.2 Industrial Linting
* **Always** include a `lint` job.
* **ShellCheck**: **Mandatory** for all Bash scripts (e.g., in `.github/scripts/`). All scripts must pass ShellCheck without errors.
* **Actionlint**: Required for workflow syntax, set to `fail_level: error`.
* **Dependencies**: The primary `build` or `deploy` job MUST `need` the `lint` job to ensure quality before execution.


### 10.3 Version Pinning (Strict & Live Verified)

* **Mandatory Semantic Versioning**: All GitHub Actions (`uses: ...`) **MUST** be pinned to a specific, full semantic version (e.g., `@2.0.0`, `@v4.1.7`, `@v6.0.1`).
* **Live Lookup Requirement**: Before using or updating any action, the AI Agent **MUST** perform a live lookup to identify the absolute latest stable (non-draft, non-prerelease) version/tag.
* **Tool Precedence**: Strictly follow this order for version lookups:
    1.  **GitHub CLI (`gh`)**: Use `gh release list --repo <owner/repo>` or `gh api`.
    2.  **GitHub API**: Use `curl` to the GitHub API endpoints.
    3.  **Marketplace/Docs**: Use `curl` to raw Marketplace pages or documentation.
    4.  **Browser**: Use the browser tool only as a last resort if all CLI/API methods fail.
* **Timing**: This lookup must be performed at the time of workflow creation or update, not based on cached or historical data.
* **Prohibited Tags**: Do **NOT** use mutable tags such as `@v2`, `@master`, or `@main`. This prevents unexpected breaks and ensures reproducibility.
* **Version Format**: Some actions (e.g., `ludeeus/action-shellcheck`) use semantic versions **without** the `v` prefix. Always verify the correct tag format on the Marketplace or via API.
* **Example**: `uses: actions/checkout@v6.0.1` (latest semantic, as of 2026-01-06) instead of `@v4` or `@main`.

#### 10.4 Configuration Example
```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<LATEST_VERSION>
      - name: Run ShellCheck
        uses: ludeeus/action-shellcheck@<LATEST_VERSION>
        with:
          scandir: './.github/scripts'
      - name: Run actionlint
        uses: reviewdog/action-actionlint@<LATEST_VERSION>
        with:
          fail_level: error

  build:
    needs: lint
    runs-on: ubuntu-latest
    # ...
```

#### 10.5 AI-Assisted Code Review
* **Requirement**: Implement a job that triggers on `pull_request` to:
    1.  Summarize code changes using an AI model.
    2.  Flag architectural risks or potential bugs.
    3.  Post a structured comment (using `actions/github-script` or similar) with the summary.

#### 10.6 Reviewer Assignment
* **CODEOWNERS**: Always include a `.github/CODEOWNERS` file for automatic assignment based on file paths.
* **Auto-Assignment**: For team-based or round-robin requests, use a GHA-based auto-assigner action to ensure no PR is left without a reviewer.

#### 10.7 Release Automation & Conventional Commits
* **Semantic Versioning**: Automate versioning and changelog generation using Conventional Commits.
* **Tooling**: Use `semantic-release` or similar GHA-compatible tools to automatically create GitHub Releases, bump package versions, and publish artifacts upon merging to `main`.
* **Standard Procedures**:
    * **Always** use `fetch-depth: 1` for speed.
    * **Always** pin actions to full semantic versions.

#### 10.8 Web & Node.js Build Standards
* **Unified Build**: Use a single `npm` command (e.g., `npm run build:all`) to orchestrate frontend and backend builds.
* **Parallelism**: Use tools like `npm-run-all` or `concurrently` within your scripts to run build steps in parallel where dependencies allow, ensuring the frontend is correctly embedded in the backend's distribution folder before completion.

#### 10.9 Communication & Transparency
* **Marketplace Links**: The AI Agent **MUST** provide direct GitHub Marketplace links for every action used in the suggested workflow within the chat response. This ensures the user can verify the source and versioning.
* **Latest Stable Versions**: When creating or updating workflows, the AI Agent **MUST** perform a live lookup (via search or documentation) to identify the current latest stable version for every action, replacing placeholders (e.g., `<VERSION>` or `v4.x.x`) with real values.

***

### 11. Troubleshooting & Fixer Persona

This section defines the persona and operating rules for the "GitHub Workflow Fixer Tool," an AI specialist dedicated to troubleshooting and repairing broken GitHub Action workflows.

#### 11.1 Core Mandate
The primary goal is to **restore green builds** by diagnosing failure logs, validating workflow syntax, and implementing fixes that align with best practices.
*   **Log-Driven**: Base all decisions on actual failure logs (`gh run view --log-failed`).
*   **Holistic Fixes**: Don't just patch the error; ensure the workflow structure is sound (e.g., correct `needs`, valid `if` conditions).
*   **Verification**: Always verify fixes by triggering a run and watching the result.

#### 11.2 operational protocol
**0. Code Quality Standards 💎**
When acting as a Fixer, ensure all workflows meet these baseline standards:
*   **💎 Always Pin Everything**: Never use `@v1` or `@master`. Always use full semantic versions (e.g., `@v1.2.3`).
*   **💎 Use ShellCheck**: Ensure all `.bash` scripts in `.github/scripts/` pass ShellCheck.
*   **💎 Use Actionlint**: Ensure all YAML files pass `actionlint` with `fail_level: error`.
*   **💎 The Least Privilege**: Ensure `GITHUB_TOKEN` permissions are explicitly scoped.
*   **💎 No Hardcoded Secrets**: Ensure all sensitive values are in `${{ secrets.X }}`.

**1. Investigation Phase**
*   **Pinpoint Latest Failure**: Avoid interactive prompts by grabbing the exact run ID.
    ```bash
    gh run list --limit 1 --json databaseId
    ```
*   **Fetch Logs**: Use the ID to view logs directly.
    ```bash
    gh run view <DATABASE_ID> --log-failed
    ```
*   **Examine Code**: Read the `.github/workflows/<file>.yml` to correlate the log error with the configuration.

**2. Common Failure Patterns & Fixes**
*   **Syntax Errors**: Run `actionlint` locally if available.
*   **Missing Secrets**: Verify the availability of secrets referenced in inputs/env.
*   **Runner Issues**: Check if `runs-on` targets a valid runner image.
*   **Shell Script Failures**: If a step running a script fails, inspect the script content and consider invoking the "ShellCheck Fixer Agent."

**3. Fix & Verify**
*   **Commit Message**: Use conventional commits (e.g., `fix(ci): ...`) following `Git-Commit-Message-rules.md`.
*   **Trigger**: Use `gh workflow run <file>` or `git push` to trigger the workflow.
*   **Watch**: Use `gh run watch` to monitor the new run until completion.

#### 11.3 Specialized Tooling
*   **GitHub CLI (`gh`)**: The primary tool for investigation and triggering.
*   **Actionlint**: Standard linter for workflow files.
*   **Local Simulation**: `act` (if available) for local testing; however, prefer actual GitHub runners for accurate environment reproduction.

#### 11.4 Failure Handlers & Notifications
When a workflow fails, the "Fixer" or "Ops" steps MUST execute the failure policy defined in `ci-cd-rules.md`:
* **Implementation Steps**:
    1.  **Direct Notification**: Use an action to send a WhatsApp message to the committer with direct log links.
    2.  **Issue Creation**: Use `gh issue create` with `context`, `committer assignment`, and `failure label`.
    3.  **PR Decoration**: Use `actions/github-script` or `gh pr comment` to post log links on the PR.
* **VCS Issue Auto-creation**: A failure handler step will be configured to automatically create a GitHub issue with relevant context (commit SHA, branch name, error logs) and assign the committer. This ensures that every failure is immediately documented and assigned to the person who can most effectively resolve it. Ensure the `GITHUB_TOKEN` has `issues: write` and use the committer's handle for assignment to guarantee documentation.
* **GitHub Issues**: Automatically create a new GitHub Issue if none exists for this failure.
    * **Context**: Include Commit SHA, Branch Name, Job Name, and a link to the failed logs.
    * **Assignment**: Assign the committer of the failed push to the issue.
* **PR Feedback**: If the failure is in a Pull Request, post a structured comment with:
    1.  A summary of the failed checks.
    2.  Links to the build logs.
    3.  Instructions or hints for fixing (if AI-assisted).
* **Direct Notifications**: Send 1:1 WhatsApp messages to the committer and team list with direct log links.

#### 11.5 Handling Silent Failures & API Quotas

Critical for workflows relying on external AI APIs (e.g., Gemini) that may implement silent fallback mechanisms.

*   **Silent Failure Detection**:
    *   **Anti-Pattern**: Relying solely on the global workflow status (green checkmark).
    *   **Protocol**: Inspect logs even for "successful" runs if a known fallback-capable step is involved.
    *   **Search Identifiers**: Scan logs for keywords indicating failure (e.g., `(AI generation failed)`, `Gemini API Error`, `429 Too Many Requests`).
*   **Gemini API Quota Management**:
    *   **Reset Time**: Midnight Pacific Time (PT).
    *   **IST Conversion**: Approximately **01:30 PM IST** (variations possible due to DST).
    *   **Debugging**: If "AI generation failed" appears consistently, suspect a quota outage.
*   **Programmatic Log Inspection**:
    *   Use `gh run list --workflow <file> --limit 5` to identify relevant recently "passed" runs.
    *   Use `gh run view <RUN_ID> --log` to search for silent failure strings across all jobs.
    ```bash
    # Example: Grep for silent failure indicator in the latest run
    gh run view $(gh run list --limit 1 --json databaseId -q '.[0].databaseId') --log | grep "AI generation failed"
    ```
