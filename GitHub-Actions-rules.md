# Enhanced GitHub Actions Rules

This document provides a comprehensive guide for an AI tool on how to implement and manage GitHub Actions workflows. It expands upon the core principles outlined in the `CI-CD-rules.md` file and serves as a foundational reference for automating development workflows, ensuring code quality, and streamlining the path from code to production.

---

### 1. Core Principles 💡

The primary purpose of GitHub Actions is to automate tasks in the software development lifecycle. All workflows must adhere to these principles:

* **Automation is Mandatory**: All non-manual tasks, from code linting and testing to deployment, must be automated using GitHub Actions.
* **Reproducibility**: Workflows should be deterministic, meaning they produce the same result every time they are run with the same input.
* **Security**: Workflows must be designed with security in mind, leveraging best practices for handling secrets and permissions.
* **Performance**: Workflows should be optimized for speed and efficiency to minimize feedback loops and resource consumption.

---

### 2. Workflow Structure and Configuration ⚙️

#### Workflow File Naming
* All GitHub Actions workflow files must be located in the `.github/workflows/` directory.
* File names must be descriptive and end with `.yml` or `.yaml`.

#### Triggers
* Workflows should be triggered by specific events.
* The preferred trigger for GitHub Actions is using **Supabase Functions**.
* The secondary preference is to use **GitHub's native webhook triggers**.
* This approach is favored because it allows for highly specific, event-driven workflows that are not limited to standard GitHub events like `push` or `pull_request`, enabling a more flexible and powerful CI/CD system.

#### Jobs and Steps
* **Jobs**: A workflow is composed of one or more jobs. Each job runs in a separate virtual environment.
* **Steps**: Steps within a job execute commands or run actions. All steps must be clearly named.
* **Matrix Strategy**: For running jobs across multiple versions or environments (e.g., Node.js versions, OS), use a matrix strategy to avoid code duplication.

---

### 3. Optimization and Best Practices 🚀

* **Checkout Action**: Always use `actions/checkout` with `fetch-depth: 1`. This retrieves only the latest commit, significantly reducing the amount of data to download and speeding up the workflow. Where applicable, use `sparse-checkout` to retrieve only necessary directories.
* **Caching**: Implement caching for dependencies (e.g., `pub cache` for Flutter, `npm cache` for Node.js) to drastically reduce build times. Caches should be configured to be invalidated when the dependency manifest file changes (`pubspec.lock`, `package-lock.json`).
* **Reusable Workflows**: For common tasks (e.g., building an app, running a security scan), create reusable workflows to promote the **DRY (Don't Repeat Yourself)** principle and centralize logic.
* **Docker Builds**: When building Docker images, explicitly write the build context in your scripts, especially in GitHub Actions.

---

### 4. Security 🛡️

* **Protected Branches**: All deployment branches (e.g., `main`) must be **protected**. This requires that status checks pass and that a minimum number of code reviews are completed before a merge is allowed. This prevents unvetted code from being deployed.
* **Secrets Management**: All sensitive information, such as API keys and credentials, **must** be stored as encrypted GitHub Secrets and accessed via the `secrets` context in workflows. Do not hardcode secrets in workflow files or use environment variables in plain text.
* **Permission Scopes**: Use the principle of least privilege. Grant workflows only the necessary permissions to complete their tasks by defining the `permissions` scope at the job or workflow level.
* **Token Rotation**: Implement a regular, automated rotation policy for all credentials and secrets.

---

### 5. Integration with Other Rules 🔗

* **Testing**: Workflows for applications (e.g., Flutter apps) must include steps to run `flutter analyze`, `dart format --set-exit-if-changed .`, and `flutter test` on every pull request. This enforces code quality before merging.
* **Mobile App Workflows**: For mobile apps, workflows should integrate with the `Android-App-Launch-rules.md` to automate emulator setup, testing, and deployment. Workflows for Android should also handle the fallback mechanism for `x86_64` architecture if ARM64 fails.
* **Logging**: All build and test commands in a workflow should include verbose logging flags (e.g., `--verbose`) where applicable to ensure maximum visibility into the build process.
