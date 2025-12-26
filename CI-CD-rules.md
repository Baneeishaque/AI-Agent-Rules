<!--
title: CI/CD
description: Principles and practices for CI/CD, including protected branches, security, observability, advanced deployment strategies, and automated rollbacks.
category: CI/CD & DevOps
-->

# CI/CD Rules and Best Practices

This document outlines the Continuous Integration and Continuous Deployment (CI/CD) rules and best practices for our projects. It serves as a comprehensive guide for automating development workflows, ensuring code quality, and streamlining the path from code commit to production.

---

### General Principles & Environment Management

* **Reference Rulebook**: For specific implementation details on our primary platform, refer to `GitHub-Actions-rules.md`.
* **Configuration Management:** All environment-specific variables and secrets will be stored in a private, secure repository or secret manager. This configuration data will be consumed by the CI/CD pipeline using repository-level secrets, adhering to the principle of least privilege. **Rationale:** Centralizing configuration ensures a single source of truth and full auditability of all changes to the build environment.
* **Protected Branches:** All deployment branches (e.g., `main`) must be **protected**. This protection includes requiring status checks to pass, mandating a minimum number of code reviews, and disallowing direct pushes.
* **Pipeline Optimization:** Pipelines should be optimized for speed. Techniques like shallow clones, caching dependencies, sparse checkouts, and **Conditional Step Execution** (skipping steps if relevant files haven't changed) should be employed where the CI provider supports them.
* **Principle of Least Privilege:** All CI/CD processes must operate with the minimum level of access required. **Never use a single, all-powerful personal access token (PAT).** Instead, use scoped tokens or **OpenID Connect (OIDC)** to obtain short-lived credentials directly from cloud providers (e.g., AWS, GCP). **Rationale:** OIDC eliminates the need for long-lived, high-risk secrets by using verifiable, short-term identities.
* **Environment Standardization:** The CI/CD environment must be reproducible. We will use tools like **Docker** to containerize the build environment, ensuring that the same set of tools and dependencies is used for every build, eliminating "works on my machine" issues.

---

### NestJS & React Application Architecture and Deployment

* **Monorepo vs. Polyrepo:** We will maintain separate repositories for the NestJS API (`api`) and the React web client (`web`). This "polyrepo" approach provides a clear separation of concerns, simplifies access control, and allows for independent versioning. The two services are unified at build and deploy time, allowing them to be treated as a single, co-located application.
* **Client Base URL:** The React client's base URL will be configured as `/` at build time. The API base URL will be set as an environment variable (`REACT_APP_API_BASE` or `VITE_API_BASE` for Vite projects) with the value `/api`. This strategy simplifies routing by ensuring the client always makes API requests relative to the web server's root, regardless of the deployment environment.
* **Single Web Service Deployment:** The unified NestJS and React application will be deployed as a **single Node.js web service**. This simplifies the infrastructure, reduces hosting costs, and streamlines maintenance by managing a single process.
* **Orchestration:** The deployment workflow follows a `Supabase → Pipeline Executor → Render` pattern.
    * **Supabase:** Serves as the central router and orchestrator. A single Supabase webhook will be configured to listen for events from all relevant repositories (`api`, `web`, `app`). This centralizes configuration for routing, environments, and notification rules. It also prevents duplicate deployments by storing delivery IDs to avoid them.
    * **Pipeline Executor:** Receives the webhook payload from Supabase, runs the build and test jobs, and, upon success, triggers the deployment.
    * **Render:** Serves as the runtime environment. It hosts the unified Node.js application.
* **Controlled Deployments:** The API will only be deployed when both the API and web-related criteria pass. This ensures that the frontend and backend are in a compatible state, preventing the deployment of a new API version that is not supported by the currently available web client.
* **Render Cloud Application Platform:** The deployment process on Render will be automated via the Render API. The workflow is as follows: `Build → (optionally publish artifact) → Trigger Render deploy → Fail fast on errors → Post logs on failure`.
* **Render CLI & DNS Automation:**
    * **Deployment Triggering:** We will use the Render CLI to trigger deployments manually for debugging or hotfixes. This provides flexibility outside of the automated workflow.
    * **DNS Automation:** To ensure service continuity, DNS automation will be implemented. This is crucial if a service is re-created, as the `onrender.com` host might change. During deployment, the CI/CD pipeline will fetch the service's current external URL and automatically update the DNS records via a provider API (e.g., Cloudflare, AWS Route 53).
    * **Synchronous Deployment:** The `create deploy` command will use a `--wait` flag. This flag blocks the CI/CD job until the deployment is fully complete or has failed, providing a clear and synchronous view of the deployment status.
* **Containerization:** The entire application will be built into a single Docker image. This guarantees a consistent environment from development to production.
* **Unified Build:** A single `npm` command will orchestrate the build process for both the frontend and backend. We will use `npm-run-all` or `concurrently` to run scripts in parallel or sequence, ensuring the frontend is built before being embedded in the backend's distribution folder.

---

### Mobile Application (Flutter) CI/CD

* **Build Artifacts & Distribution:**
    * **Android:** For distributing builds to testers, we will use **Firebase App Distribution** or the **Internal/App Bundle tracks in Google Play** due to their fast propagation times. Links will be shared with testers via WhatsApp.
    * **iOS:** TestFlight invites will be sent via email, and release notes links will be posted in WhatsApp.
* **App Store Publishing:** The entire App Store publishing process will be automated via CI/CD, from building the app to uploading it to the App Store Connect or Google Play Console.
* **Artifact Management (Supabase Storage):**
    * **Short-Lived Testing:** For frequent feature branch builds, we will use Supabase Storage with a short retention policy to conserve storage space. A scheduled cleanup job will automatically prune old artifacts.
    * **Long-Term Versioning:** For stable releases, client-specific branches, or builds intended for the publishing process, artifacts will be stored long-term in Supabase Storage. Each artifact will be tagged with a consistent naming convention (e.g., `client-name/version/environment`) for easy identification and retrieval. Pre-release builds will be marked for tester-only channels.
    * **Automated Workflow:** The CI/CD pipeline will automate the entire artifact management process: upload builds from the executor, generate pre-signed links for testers, and apply lifecycle policies to automatically expire old builds.
* **CI/CD Strategy:** The pipeline should be triggered on code pushes to main branches or pull requests. It must run static analysis and tests (e.g., `flutter analyze` and `flutter test --coverage`) to ensure code quality and coverage.
* **Automated Distribution:** Upon a successful release build, the artifact should be automatically uploaded to distribution platforms (e.g., Firebase App Distribution, TestFlight) using the pipeline. Sensitive credentials like signing keys must be securely stored as encrypted secrets within the platform.
* **Automated Notifications:** Once a new build is ready for testing, the CI/CD pipeline will send an automated WhatsApp message to a designated group.
    * **Format:** The message will follow a standardized format. The WhatsApp link will not contain the `?mode` portion, and the `<SOCIAL_HANDLE>` Instagram handle will be included.

---

### Notifications & Issue Tracking

* **Notification Strategy:**
    * **Urgent Notifications:** For critical events like build failures, we will use a dedicated service like **WhatsApp Cloud API** or a provider like **Twilio** to send direct, 1:1 messages to the committer and the relevant team list.
    * **Team Channels:** For general bot notifications (e.g., PR updates, daily summaries), team channels on platforms like **Slack, Telegram, or Discord** are more suitable.
* **Failure Handling:** Upon a build failure, the CI/CD pipeline will:
    1.  Send a WhatsApp message to the committer and team.
    2.  Open a new GitHub issue with the full build logs and context.
    3.  Comment on the associated pull request (if applicable) with a link to the issue and logs.
* **VCS Issue Auto-creation:** A failure handler step will be configured to automatically create a GitHub issue with relevant context (commit SHA, branch name, error logs) and assign the committer. This ensures that every failure is immediately documented and assigned to the person who can most effectively resolve it.
* **Google Sheets Tracking:** A Google Sheets tracking system will be implemented to log key development events.
    * **Mechanism:** Using a service account JSON stored as a secure pipeline secret, the Sheets API will be called from a pipeline step to append rows.
    * **Data Points:** Key events to track include PR opened, reviewer assigned, review outcome, requested changes, merge time, and release tags.
    * **Idempotency:** To prevent duplicate entries, each row will be keyed by a combination of the PR number and commit SHA.
    * **Centralized View:** A single "Ops" sheet with dedicated tabs for each repository provides a centralized, human-readable view of the development lifecycle.
* **Webhooks:** We will use webhooks to automate real-time notifications for critical CI/CD events.

---

### Code Review & Quality Automation

* **Baseline Automation:** A standard set of automated checks will be run on every pull request to enforce code quality and security.
    * **Mandatory Checks:** Linting, formatting, unit tests, type checks, and security scans (`npm audit`, Snyk).
* **Code Coverage:** Code coverage reports will be integrated with services like Codecov or Coveralls. Coverage will be uploaded using a token stored as a secret, and a badge will be displayed on the project's `README.md` file.
* **Static Analysis & Quality Gates:** Static analysis tools like SonarQube will be used to enforce quality gates. This can be integrated by installing an organization/repository-level application or by running open-source analyzers directly within the CI/CD pipeline.
* **AI-Assisted Code Review:** An AI-powered job should run on every pull request to:
    1.  Summarize changes in a concise, human-readable format.
    2.  Flag potential risks or areas of concern.
    3.  Post a structured comment directly on the PR.
* **Automation:** A majority of the CI/CD logic will be driven by secrets and CLI/API calls, requiring no manual intervention once configured. This provides a high level of security and efficiency.
* **Automated Reviewer Assignment:** We will implement logic to automatically request reviews from team members based on pre-defined rules (e.g., code ownership, round-robin assignments).
* **Conventional Commits:** We will adopt **Conventional Commits** for all new projects. This enables automated changelog generation and semantic versioning based on commit messages, which streamlines the release process.

---

### Advanced Practices

* **Observability:** We will prioritize observability by implementing structured logging and collecting runtime metrics (e.g., CPU, memory, request latency). This data will be piped to a centralized dashboard (e.g., Grafana, Datadog) to provide real-time insights into application health and performance. We will also configure automated alerts for critical thresholds.
* **Security:** To enhance security, we will use dedicated vulnerability scanners like Snyk to check for known vulnerabilities. Additionally, all secrets and credentials will be subject to an automated rotation policy.
* **Deployment Strategy:** For mission-critical applications, we will adopt more advanced deployment strategies such as **Canary** or **Blue/Green** deployments. This allows new versions to be tested on a small user subset or in a separate environment before a full rollout, minimizing risk and providing a quick rollback path.
* **Infrastructure as Code (IaC):** For managing the configuration and deployment of our services on platforms like Render, we will use an Infrastructure as Code (IaC) tool like **Terraform** or **Pulumi**. This allows us to define and manage our infrastructure in version-controlled code, providing a single source of truth and enabling automated, reproducible infrastructure changes.
* **Rollback Strategy:** We will implement an automated rollback strategy. In the event of a critical failure, a new deployment will automatically revert to the last known stable version.
* **General Adherence:** Adhere to all general rule documents, including `AI-Agent-rules.md`, `AI-Tools-rules.md`, and `Shell-Execution-rules.md`, to ensure a unified and secure development environment.
