# AI Agent Rules Index

This file is a comprehensive, flat index of all rule files in this repository.

> **Note**: For categorized views, usage examples, and architecture details, please see the [Main README](./README.md).

## Rule List

| Rule Domain | File Name | Description |
|---|---|---|
| Rule Domain | File Name | Description |
|---|---|---|
| AI Tools Output Visibility | [AI-Tools-rules.md](./AI-Tools-rules.md) | Comprehensive rules for AI tool usage, including mandates for output visibility, explicit user confirmation for file writes, and integration with agent planning and security protocols. |
| Agent Planning | [AI-Agent-rules.md](./AI-Agent-rules.md) | Guidelines for agent planning, including the core directive to plan before acting and a protocol for iterative plan revisions. |
| Android App Launch | [Android-App-Launch-rules.md](./Android-App-Launch-rules.md) | Automated protocol for emulator setup and deployment, optimized for M2 machines, with architecture and device fallbacks. |
| Brew Install Preferences | [Brew-Install-rules.md](./Brew-Install-rules.md) | Prefer head/source builds and verbose logging for Homebrew installations. |
| Brew Upgrade with Exclusions | [Brew-Upgrade-rules.md](./Brew-Upgrade-rules.md) | Upgrade all packages except specified ones with explicit command generation. |
| CI/CD | [CI-CD-rules.md](./CI-CD-rules.md) | Principles and practices for CI/CD, including protected branches, security, observability, advanced deployment strategies, and automated rollbacks. |
| Docker | [Docker-rules.md](./Docker-rules.md) | Guidelines for Docker containerization, best practices for Dockerfiles, and image optimization. |
| Flutter Android App | [Flutter-Android-App-rules.md](./Flutter-Android-App-rules.md) | Specific guidelines for Android configurations within Flutter projects. |
| Flutter App | [Flutter-App-rules.md](./Flutter-App-rules.md) | Rules for Flutter app development, including version pinning with `mise`, dependency management, and mandatory documentation. |
| Git Commit Message Generation | [Git-Commit-Message-rules.md](./Git-Commit-Message-rules.md) | Strict rules for generating git commit messages, enforcing Conventional Commits, contextual information in titles, and no redundancy between title and body. |
| Git Operation Rules | [Git-Operation-rules.md](./Git-Operation-rules.md) | Strict protocols for standard Git operations (commits & pushes), mandating explicit user requests and forbidding auto-actions. |
| Git Repo Cloning | [Git-Repo-Cloning-rules.md](./Git-Repo-Cloning-rules.md) | CLI-based cloning protocols, supporting submodule initialization and directory management. |
| Git Repo Indexing | [Git-Repository-Indexing-rules.md](./Git-Repository-Indexing-rules.md) | Rules for auto-indexing codebases within git repositories for improved agent context. |
| Git Repository Creation | [Git-Repository-rules.md](./Git-Repository-rules.md) | Standardized rules for creating new repositories, including naming conventions, essential file generation, and initial commit best practices. |
| Git Submodule Management | [Git-Submodule-rules.md](./Git-Submodule-rules.md) | Protocols for managing submodules, preventing detached HEAD states, proper branch tracking, and descriptive parent commit messages. |
| GitHub Actions | [GitHub-Actions-rules.md](./GitHub-Actions-rules.md) | Rules for GitHub Actions workflows, covering trigger preferences, security, performance, and integrations. |
| GitHub CLI Permission | [GitHub-CLI-Permission-rules.md](./GitHub-CLI-Permission-rules.md) | Explicit permission protocol for running `gh` commands, ensuring user control and transparency. |
| Mise Plugin Backend Management | [Mise-Plugin-Backend-Management-rules.md](./Mise-Plugin-Backend-Management-rules.md) | Intelligent backend selection for mise plugin installations with fallback handling and user prompts. |
| NestJS React App | [NestJS-React-App-rules.md](./NestJS-React-App-rules.md) | Guidelines for developing NestJS backends with React frontends. |
| NestJS React App with Flutter Client | [NestJS-React-App-with-Flutter-Client-rules.md](./NestJS-React-App-with-Flutter-Client-rules.md) | Full-stack guidelines for NestJS/React web apps with an accompanying Flutter mobile client. |
| Render Cloud Application Platform | [Render-Cloud-Application-Platform-rules.md](./Render-Cloud-Application-Platform-rules.md) | Deployment configurations for Render, including environment variables and custom domains. |
| Repository Search | [Repository-Search-rules.md](./Repository-Search-rules.md) | Multi-platform repository discovery and smart cloning workflows. |
| Rule Management Workflow | [Rule-Management-rules.md](./Rule-Management-rules.md) | Documentation sync and update workflow, including metadata management for rule indexing. |
| Script Management | [Script-Management-rules.md](./Script-Management-rules.md) | Script standards, folder usage, and safeguards for helper scripts. |
| Shell Execution | [Shell-Execution-rules.md](./Shell-Execution-rules.md) | Guidelines for shell command execution, ensuring transparency, user control, and adherence to security protocols. |
| Warp | [Warp-rules.md](./Warp-rules.md) | Backup and reference for Warp AI Agent specific configurations. |
