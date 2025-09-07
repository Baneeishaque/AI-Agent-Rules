# AI Rules Index

This file serves as the central index for all rule files in this repository. Each rule is maintained in a dedicated markdown file for modularity, scalability, and ease of maintenance.

## How to Use
- **Browse:** Find the rule domain below and follow the link to its file.
- **Add/Modify Rules:** Create or update the appropriate domain file, then update this index.
- **Sync:** Always keep this index up-to-date when rules are added or changed.

## Rule Files

| Rule Domain | File Name | Description |
|---|---|---|
| Flutter Android App | [Flutter-Android-App-rules.md](./Flutter-Android-App-rules.md) | (empty) |
| Flutter App | [Flutter-App-rules.md](./Flutter-App-rules.md) | Rules for Flutter app development, including version pinning with `mise`, dependency management, and mandatory documentation. |
| NestJS React App | [NestJS-React-App-rules.md](./NestJS-React-App-rules.md) | (empty) |
| NestJS React App with Flutter Client | [NestJS-React-App-with-Flutter-Client-rules.md](./NestJS-React-App-with-Flutter-Client-rules.md) | (empty) |
| Render Cloud Application Platform | [Render-Cloud-Application-Platform-rules.md](./Render-Cloud-Application-Platform-rules.md) | Use env vars, custom domains |
| Warp | [Warp-rules.md](./Warp-rules.md) | Backup/reference for Warp AI Agent configs |
| CI/CD | [CI-CD-rules.md](./CI-CD-rules.md) | Principles and practices for CI/CD, including protected branches, security, observability, advanced deployment strategies, and automated rollbacks. |
| GitHub Actions | [GitHub-Actions-rules.md](./GitHub-Actions-rules.md) | Rules for GitHub Actions workflows, covering trigger preferences, security, performance, and integrations. |
| GitHub CLI Permission | [GitHub-CLI-Permission-rules.md](./GitHub-CLI-Permission-rules.md) | Explicit permission protocol for running `gh` commands, ensuring user control and transparency. |
| Git Repository Creation | [Git-Repository-rules.md](./Git-Repository-rules.md) | Standardized rules for creating new repositories, including naming conventions, essential file generation, and initial commit best practices. |
| Script Management | [Script-Management-rules.md](./Script-Management-rules.md) | Script standards, folder usage, and safeguards |
| Git Repo Indexing | [Git-Repository-Indexing-rules.md](./Git-Repository-Indexing-rules.md) | Auto-index codebases in git repos |
| Git Repo Cloning | [Git-Repo-Cloning-rules.md](./Git-Repo-Cloning-rules.md) | CLI-based cloning, submodule support |
| Brew Install Preferences | [Brew-Install-rules.md](./Brew-Install-rules.md) | Prefer head/source builds, verbose logging |
| Rule Management Workflow | [Rule-Management-rules.md](./Rule-Management-rules.md) | Documentation sync and update workflow |
| Repository Search | [Repository-Search-rules.md](./Repository-Search-rules.md) | Multi-platform repo discovery and smart cloning |
| Android App Launch | [Android-App-Launch-rules.md](./Android-App-Launch-rules.md) | Automated protocol for emulator setup and deployment, optimized for M2 machines, with architecture and device fallbacks. |
| Agent Planning | [AI-Agent-rules.md](./AI-Agent-rules.md) | Guidelines for agent planning, including the core directive to plan before acting and a protocol for iterative plan revisions. |
| AI Tools Output Visibility | [AI-Tools-rules.md](./AI-Tools-rules.md) | Comprehensive rules for AI tool usage, including mandates for output visibility, explicit user confirmation for file writes, and integration with agent planning and security protocols. |
| Shell Execution | [Shell-Execution-rules.md](./Shell-Execution-rules.md) | Guidelines for shell command execution, ensuring transparency, user control, and adherence to security protocols. |

## Adding New Rules
1. Create a new markdown file named `<Domain>-rules.md`.
2. Add your rule(s) with clear descriptions and examples.
3. Update the table above with the new file and a short description.
4. Commit changes with a conventional commit message.
