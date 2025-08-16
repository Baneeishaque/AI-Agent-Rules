* Use environments & environment credentials from configuration file under a private repo. Repo is configured via. ecrets.
* NestJS React App.: Keep repos separate; unify at build/deploy time
* NestJS React App.: Client base URL: set it to “/” at build timefor Vite. Pass REACT_APP_API_BASE=/api (or Vite’s VITE_API_BASE=/api) at build time.
* NestJS React App.: Single Web Service => Deploy this unified Node.js app as a single Web Service. Eg: - Single Render Web Service
* NestJS React App.: Orchestration: Supabase → GitHub Actions → Render => Supabase as router/orchestrator, Actions as executors, Render as runtime.
* NestJS React App.: Single Supabase webhook for API, Web & App. Repos => Central config: repo → services, branches, environments, notification rules.. Route by repo and branch. Store delivery IDs to avoid duplicates.
* NestJS React App.: API deploys only when both API and web criteria pass.

* NestJS React App. on Render Cloud Application Platform: Build → (optionally publish artifact) → Trigger Render deploy → Fail fast on errors → Post logs on failure.

* On Render Cloud Application Platform Deploys: Use Render CLI to trigger deployments manually.
* On Render Cloud Application Platform Deploys: Instruct to setup DNS automation => If re-create the service and the onrender.com host changes, Fetch the current external URL at deploy time (env) and update DNS via provider API (Cloudflare/Route53).
* On Render Cloud Application Platform Deploys: Calls “create deploy” on the service and uses a “--wait” flag to block until complete.

* Notifications: WhatsApp - WhatsApp Cloud API (Meta) or providers like Twilio. 1:1 messages to opted-in numbers.
* Notifications: Team channel better suited for bots (Slack/Telegram/Discord).
* Notifications: On build failure: send WhatsApp messages to the committer + team list; open a GitHub issue with logs; comment on PR.
* Notifications: On PR open/update: run CI; post inline PR comments with lint/test/AI review summary.
* Notifications: On successful release: message team, host web, build app, upload artifacts, and DM testers with links.
* VCS Hosting Provider (Eg:- GitHub, GitLab, etc.) Issues auto-creation: Add a failure handler step that creates an issue with context (commit, branch, logs) and assigns the committer.

* Flutter App.: Shipping builds to testers, Android: use Firebase App Distribution or Internal/App Bundle tracks in Google Play (fast propagation); share link in WhatsApp.
* Flutter App.: Shipping builds to testers, iOS: TestFlight invites via email; post release notes link in WhatsApp.
* Flutter App.: App Store Publishing via CI/CD.

* Google Sheets tracking (code review requests, PR states, merges): Use a service account JSON (stored as a secret) and call the Sheets API from Actions to append rows for: PR opened, reviewer assigned, review outcome, requested changes, merge time, release tag, etc. Keep a single “Ops” sheet with tabs per repo.
* Google Sheets tracking (code review requests, PR states, merges): Idempotency => use PR number + commit SHA as keys.

* Code review automation: Baseline automation => Lint, format, unit tests, type checks, security scan (npm audit, Snyk), license compliance.
* Code review automation: Conventional commits + changelog generation for Releases.
* Code review automation: Coverage reports with badges (Codecov/Coveralls); use token-based upload.
* Code review automation: Static analysis and quality gates => Sonar (needs org/repo app install) or run OSS analyzers in Actions.
* Code review automation: AI assist => Run a PR job that summarizes changes, flags risks, and posts a structured comment.
* Code review automation: Do a lot purely with secrets and CLI/API calls where tokens suffice.
* Code review automation: auto-request reviewers.
