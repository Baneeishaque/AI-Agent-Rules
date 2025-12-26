<div align="center">

# 🤖 AI Agent Rules

**A comprehensive, modular framework of rules and best practices for AI agents and development workflows**

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/Baneeishaque/AI-Agent-Rules)
[![Markdown](https://img.shields.io/badge/Format-Markdown-lightgrey?logo=markdown)](https://daringfireball.net/projects/markdown/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Baneeishaque/AI-Agent-Rules/pulls)

*Establish trust, transparency, and consistency in AI-assisted development*

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Quick Start](#-quick-start)
- [Rule Categories](#-rule-categories)
- [Architecture](#-architecture)
- [Detailed Rule Reference](#-detailed-rule-reference)
- [Usage Examples](#-usage-examples)
- [Integration Guide](#-integration-guide)
- [Contributing](#-contributing)
- [Development Setup](#-development-setup)
- [License](#-license)

---

## 🎯 Overview

**AI Agent Rules** is a comprehensive collection of standardized rules, best practices, and protocols designed to govern AI agent behavior in software development workflows. This framework ensures:

- **Transparency**: Every AI action is visible and auditable
- **User Control**: Users maintain ultimate authority over all operations
- **Consistency**: Standardized patterns across all development activities
- **Security**: Principle of least privilege and explicit permission protocols

The repository provides a modular, extensible rule system that can be adopted by AI coding assistants, development tools, and automated workflows to establish a trustworthy and effective interaction model.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🎯 **Modular Architecture** | Each rule domain is maintained in a separate markdown file for easy management |
| 📖 **Self-Documenting** | Rules are written in clear, unambiguous language with examples |
| 🔗 **Cross-Referenced** | Rules reference each other to form a cohesive framework |
| 🛡️ **Security-First** | Emphasis on permissions, secrets management, and safe operations |
| 🔄 **CI/CD Ready** | Rules designed to integrate with GitHub Actions and deployment pipelines |
| 📱 **Multi-Platform** | Covers Flutter, NestJS, React, Docker, and more |

---

## 🚀 Quick Start

### Clone the Repository

```bash
# Using GitHub CLI (recommended)
gh repo clone Baneeishaque/AI-Agent-Rules

# Using Git
git clone https://github.com/Baneeishaque/AI-Agent-Rules.git
```

### Browse Rules

1. Start with [`agent-rules.md`](./agent-rules.md) - the central index of all rules
2. Explore specific domain rules based on your needs
3. Reference rules in your AI tool configuration or workflow documentation

### Integrate with Your AI Tool

Reference specific rule files in your AI assistant's context or system prompt:

```markdown
Follow the guidelines in:
- AI-Agent-rules.md for planning protocols
- AI-Tools-rules.md for tool execution guidelines
- Shell-Execution-rules.md for command-line operations
```

---

## 📚 Rule Categories

### Android Development
| Rule File | Purpose |
|-----------|---------|
| [`Android-App-Launch-rules.md`](./Android-App-Launch-rules.md) | Automated protocol for emulator setup and deployment, optimized for M2 machines, with architecture and device fallbacks. |

### CI/CD & DevOps
| Rule File | Purpose |
|-----------|---------|
| [`CI-CD-rules.md`](./CI-CD-rules.md) | Principles and practices for CI/CD, including protected branches, security, observability, advanced deployment strategies, and automated rollbacks. |
| [`Docker-rules.md`](./Docker-rules.md) | Guidelines for Docker containerization, best practices for Dockerfiles, and image optimization. |
| [`GitHub-Actions-rules.md`](./GitHub-Actions-rules.md) | Rules for GitHub Actions workflows, covering trigger preferences, security, performance, and integrations. |
| [`Render-Cloud-Application-Platform-rules.md`](./Render-Cloud-Application-Platform-rules.md) | Deployment configurations for Render, including environment variables and custom domains. |

### Code Quality & Linting
| Rule File | Purpose |
|-----------|---------|
| [`ShellCheck-Fixer-rules.md`](./ShellCheck-Fixer-rules.md) | Specialized rules for repairing shell scripts to meet ShellCheck standards. |

### Core Agent Behavior
| Rule File | Purpose |
|-----------|---------|
| [`AI-Agent-Session-Documentation-rules.md`](./AI-Agent-Session-Documentation-rules.md) | Protocol for documenting AI agent sessions or conversations as Markdown, including file attachment references, structured data, and traceability. |
| [`AI-Agent-rules.md`](./AI-Agent-rules.md) | Guidelines for agent planning, including the core directive to plan before acting and a protocol for iterative plan revisions. |
| [`AI-Tools-rules.md`](./AI-Tools-rules.md) | Comprehensive rules for AI tool usage, including mandates for output visibility, explicit user confirmation for file writes, and integration with agent planning and security protocols. |
| [`GitHub-CLI-Permission-rules.md`](./GitHub-CLI-Permission-rules.md) | Explicit permission protocol for running `gh` commands, ensuring user control and transparency. |
| [`Shell-Execution-rules.md`](./Shell-Execution-rules.md) | Guidelines for shell command execution, ensuring transparency, user control, and adherence to security protocols. |

### Development Frameworks
| Rule File | Purpose |
|-----------|---------|
| [`Flutter-Android-App-rules.md`](./Flutter-Android-App-rules.md) | Specific guidelines for Android configurations within Flutter projects. |
| [`Flutter-App-rules.md`](./Flutter-App-rules.md) | Rules for Flutter app development, including version pinning with `mise`, dependency management, and mandatory documentation. |
| [`NestJS-React-App-rules.md`](./NestJS-React-App-rules.md) | Guidelines for developing NestJS backends with React frontends. |
| [`NestJS-React-App-with-Flutter-Client-rules.md`](./NestJS-React-App-with-Flutter-Client-rules.md) | Full-stack guidelines for NestJS/React web apps with an accompanying Flutter mobile client. |

### Git & Repository Management
| Rule File | Purpose |
|-----------|---------|
| [`Git-Repo-Cloning-rules.md`](./Git-Repo-Cloning-rules.md) | CLI-based cloning protocols, supporting submodule initialization and directory management. |
| [`Git-Repository-Indexing-rules.md`](./Git-Repository-Indexing-rules.md) | Rules for auto-indexing codebases within git repositories for improved agent context. |
| [`Git-Repository-rules.md`](./Git-Repository-rules.md) | Standardized rules for creating new repositories, including naming conventions, essential file generation, and initial commit best practices. |
| [`GitHub-Pull-Request-Processing-rules.md`](./GitHub-Pull-Request-Processing-rules.md) | Sequential, CLI-first protocols for handling Pull Requests, emphasizing security for private repositories and explicit user handoff. |
| [`GitHub-Repository-Metadata-Management-rules.md`](./GitHub-Repository-Metadata-Management-rules.md) | Ultra-Lean Industrial protocols for Metadata-as-Code (MaC), using README.md as the absolute Single Source of Truth with visible markers for automation. |
| [`Repository-Search-rules.md`](./Repository-Search-rules.md) | Multi-platform repository discovery and smart cloning workflows. |
| [`git-atomic-commit-construction-rules.md`](./git-atomic-commit-construction-rules.md) | Authoritative protocol for analyzing, grouping, and arranging changes into logical, independent atomic units before execution. |
| [`git-commit-message-rules.md`](./git-commit-message-rules.md) | Strict rules for generating git commit messages, enforcing Conventional Commits, contextual information in titles, and no redundancy between title and body. |
| [`git-operation-rules.md`](./git-operation-rules.md) | Strict protocols for standard Git operations (commits & pushes), mandating explicit user requests and forbidding auto-actions. |
| [`git-submodule-rules.md`](./git-submodule-rules.md) | Protocols for managing submodules, preventing detached HEAD states, proper branch tracking, and descriptive parent commit messages. |

### GitHub Actions
| Rule File | Purpose |
|-----------|---------|
| [`GitHub-Action-Creation-rules.md`](./GitHub-Action-Creation-rules.md) | Strict guidelines for creating, structuring, and publishing GitHub Composite Actions to the Marketplace. enforce "Industrial" standards. |

### Package Management
| Rule File | Purpose |
|-----------|---------|
| [`Brew-Common-rules.md`](./Brew-Common-rules.md) | Common Homebrew rules and settings shared across install/upgrade operations. |
| [`Brew-Install-rules.md`](./Brew-Install-rules.md) | Prefer head/source builds and verbose logging for Homebrew installations. |
| [`Brew-Upgrade-rules.md`](./Brew-Upgrade-rules.md) | Upgrade all packages except specified ones with explicit command generation. |
| [`Mise-Plugin-Backend-Management-rules.md`](./Mise-Plugin-Backend-Management-rules.md) | Intelligent backend selection for mise plugin installations with fallback handling and user prompts. |

### Rule-Management
| Rule File | Purpose |
|-----------|---------|
| [`AI-Agent-Rule-Standard-Creation-rules.md`](./AI-Agent-Rule-Standard-Creation-rules.md) | Craftsmanship standards for developing "Ultra-Lean Industrial" AI Agent Rules, ensuring consistent formatting, structural hierarchy, and pedagogical clarity. |

### Tooling & Workflows
| Rule File | Purpose |
|-----------|---------|
| [`Rule-Management-rules.md`](./Rule-Management-rules.md) | Documentation sync and update workflow, including metadata management for rule indexing. |
| [`Script-Management-rules.md`](./Script-Management-rules.md) | Script standards, folder usage, and safeguards for helper scripts. |
| [`Warp-rules.md`](./Warp-rules.md) | Backup and reference for Warp AI Agent specific configurations. |


---

## 🏗️ Architecture

```
AI-Agent-Rules/
├── 📄 agent-rules.md                    # Central index (start here!)
│
├── 🧠 Core Agent Rules
│   ├── AI-Agent-rules.md               # Planning & workflow protocols
│   ├── AI-Tools-rules.md               # Tool execution guidelines
│   └── Shell-Execution-rules.md        # Command-line safety
│
├── 🔐 Security & Permissions
│   └── GitHub-CLI-Permission-rules.md  # Permission protocols
│
├── 📱 Development Frameworks
│   ├── Flutter-App-rules.md            # Flutter best practices
│   ├── Flutter-Android-App-rules.md    # Flutter Android specific
│   ├── NestJS-React-App-rules.md       # NestJS + React
│   └── NestJS-React-App-with-Flutter-Client-rules.md
│
├── ⚙️ CI/CD & DevOps
│   ├── CI-CD-rules.md                  # Pipeline principles
│   ├── GitHub-Actions-rules.md         # Workflow configuration
│   ├── Docker-rules.md                 # Container guidelines
│   └── Render-Cloud-Application-Platform-rules.md
│
├── 🗃️ Repository Management
│   ├── Git-Repository-rules.md         # Repo creation standards
│   ├── Git-Repo-Cloning-rules.md       # Cloning protocols
│   ├── Git-Repository-Indexing-rules.md
│   └── Repository-Search-rules.md
│
├── 📦 Package & Script Management
│   ├── Brew-Install-rules.md           # Homebrew installation
│   ├── Brew-Upgrade-rules.md           # Package upgrades
│   └── Script-Management-rules.md      # Script organization
│
├── 🔧 Tooling
│   ├── Android-App-Launch-rules.md     # Emulator management
│   ├── Rule-Management-rules.md        # Documentation sync
│   └── Warp-rules.md                   # Terminal configurations
│
└── 📂 Configuration
    ├── .gitignore                      # Git ignore patterns
    └── .vscode/                        # VS Code settings
        ├── settings.json               # Editor configuration
        └── extensions.json             # Recommended extensions
```

---

## 📖 Detailed Rule Reference

### Core Planning Protocol (AI-Agent-rules.md)

The foundational rule that all agents must follow:

```markdown
1. Deconstruct the Request → Analyze user intent
2. Formulate the Plan    → Create step-by-step approach
3. Present for Approval  → Seek user confirmation
4. Execute the Plan      → Implement approved steps
5. Report Progress       → Summarize completion
```

**Key Principles:**
- ✅ Always plan before acting
- ✅ Plans must be explicit and actionable
- ✅ Support iterative plan revisions
- ✅ Handle ambiguous requests with clarification

### Tool Execution Protocol (AI-Tools-rules.md)

```markdown
Core Principles:
- Transparency      → Full visibility of all tool actions
- User Control      → User maintains ultimate authority
- Full Output       → Never truncate stdout/stderr
- Least Privilege   → Minimum necessary permissions
```

**Mandatory User Confirmation Required For:**
- File write operations
- GitHub CLI commands
- Any destructive operations

### Shell Execution Guidelines (Shell-Execution-rules.md)

```bash
# Always explain critical commands before execution
# Display full output (stdout + stderr)
# Prefer non-interactive commands when possible
# Use background processes (&) for long-running tasks
```

### Flutter Development (Flutter-App-rules.md)

**Environment Setup:**
```bash
# Use Mise for version management
mise install              # Install SDK versions from mise.toml
mise use flutter@3.x.x    # Pin Flutter version
```

**Code Quality:**
```bash
flutter analyze           # Lint with zero warnings
dart format .             # Format all code
flutter test --coverage   # Run tests with coverage
```

**Project Structure:**
```
lib/
├── src/
│   ├── features/         # Feature modules
│   │   ├── feature_name/
│   │   │   ├── domain/   # Business logic
│   │   │   ├── presentation/  # UI
│   │   │   └── data/     # Data sources
│   ├── common/           # Shared utilities
│   ├── core/             # App configuration
│   └── main.dart
```

### CI/CD Best Practices (CI-CD-rules.md)

**GitHub Actions Optimization:**
```yaml
- uses: actions/checkout@v3
  with:
    fetch-depth: 1        # Shallow clone for speed
    sparse-checkout: true # Only needed directories
```

**Security:**
- Use OIDC for cloud authentication
- Never hardcode secrets
- Protected branches required
- Automated secret rotation

**Deployment Orchestration:**
```
Supabase → GitHub Actions → Render
   ↓            ↓              ↓
  Router     Executor      Runtime
```

---

## 💡 Usage Examples

### Example 1: Planning a Feature Implementation

```markdown
Agent: I will implement the user authentication feature. Here is my plan:

1. Create the authentication model in `lib/src/features/auth/domain/`
2. Implement the auth repository with Firebase integration
3. Build the login screen widget
4. Add unit tests for auth logic
5. Run `flutter analyze` and `flutter test`

Do you approve this plan?
```

### Example 2: Safe Shell Execution

```markdown
Agent: I need to run the following command to install dependencies:

Command: npm install
Purpose: Install project dependencies from package.json
Location: ~/projects/my-app/

Do you want me to proceed?
```

### Example 3: GitHub CLI with Permission

```markdown
Agent: I need to clone the repository. Here is the command:

gh repo clone Baneeishaque/AI-Agent-Rules ~/sample/path/AI-Agent-Rules

This will clone the repository to your local machine.
Do you approve this command? Yes/No
```

### Example 4: Brew Upgrade with Exclusions

```bash
# User: "upgrade except google-chrome@canary"

# Agent runs dry-run, filters results, presents:
brew upgrade --greedy --verbose gh node ollama discord@ptb postman
```

---

## 🔌 Integration Guide

### With Warp Terminal

1. Open Warp Terminal settings
2. Navigate to AI Agent configuration
3. Reference rule files from this repository
4. Rules sync automatically across devices

### With VS Code

Recommended extensions are pre-configured in `.vscode/extensions.json`. Key extensions include:

```json
{
  "recommendations": [
    "eamodio.gitlens",
    "mhutchie.git-graph",
    "github.vscode-pull-request-github",
    "semanticdiff.semanticdiff"
  ],
  "onlyVscodeSupported": [
    "github.copilot",
    "github.copilot-chat"
  ]
}
```

> **Note**: See `.vscode/extensions.json` for the complete list of recommended extensions organized by platform support.

### With Custom AI Assistants

Include rule files in your system prompt or context:

```python
# Example: Loading rules into context
with open('AI-Agent-rules.md', 'r') as f:
    agent_rules = f.read()
    
system_prompt = f"""
You are an AI assistant. Follow these rules:
{agent_rules}
"""
```

### With GitHub Actions

Reference CI/CD rules in your workflow:

```yaml
name: CI Pipeline
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 1  # As per CI-CD-rules.md
```

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Adding New Rules

1. **Create a new rule file**: `<Domain>-rules.md`
   ```markdown
   # Domain Name Rules
   
   Brief description of the rule domain.
   
   ---
   
   ### 1. First Principle
   
   Explanation and examples...
   ```

2. **Update the index**: Add entry to `agent-rules.md`
   ```markdown
   | Rule Domain | [Domain-rules.md](./Domain-rules.md) | Description |
   ```

3. **Commit with conventional message**:
   ```bash
   git commit -m "feat: Add Domain-rules.md for X functionality"
   ```

### Modifying Existing Rules

1. Edit the relevant `*-rules.md` file
2. Ensure cross-references remain valid
3. Update `agent-rules.md` description if needed
4. Use conventional commits:
   ```bash
   git commit -m "docs: Update Flutter-App-rules.md with state management section"
   ```

### Style Guidelines

- Use clear, unambiguous language
- Include practical examples
- Add emoji icons for visual organization 💡 🛡️ 📜 🔗
- Keep rules actionable and specific
- Reference other rule files when appropriate

### Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/new-rule-domain`
3. Make your changes
4. Run spell check (VS Code cSpell is configured)
5. Submit a pull request with a clear description

### Repository Topics

Please tag your PR/Repository with relevant topics. See [GITHUB_TOPICS.md](./GITHUB_TOPICS.md) for the complete list and guidelines.

---

## 🛠️ Development Setup

### Prerequisites

- Git 2.x+
- VS Code (recommended) or any markdown editor
- GitHub CLI (`gh`) for repository operations

### Setup Steps

```bash
# 1. Clone the repository
gh repo clone Baneeishaque/AI-Agent-Rules

# 2. Navigate to directory
cd AI-Agent-Rules

# 3. Open in VS Code
code .

# 4. Install recommended extensions (prompted automatically)
```

### VS Code Configuration

The repository includes pre-configured settings:

- **Spell checking**: Custom dictionary for technical terms
- **Markdown preview**: Native support
- **Git integration**: GitLens, Git Graph, and more
- **GitHub integration**: PR and issue management

### File Organization

| Path | Purpose |
|------|---------|
| `*.md` | Rule documentation files |
| `.vscode/settings.json` | Editor configuration |
| `.vscode/extensions.json` | Recommended extensions |
| `.gitignore` | Git ignore patterns |

---

## 📊 Rule Statistics

| Metric | Count |
|--------|-------|
| Total Rule Files | 24 |
| Fully Documented Rules | 17 |
| Placeholder/Empty Rules | 4 |
| Core Agent Rules | 4 |
| Development Framework Rules | 4 |
| CI/CD & DevOps Rules | 4 |
| Repository Management Rules | 4 |
| Other Domain Rules | 8 |

> **Note**: Some rule files are placeholders awaiting documentation. Check the rule categories table for current status.

---

## 🔗 Related Resources

- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Flutter Documentation](https://flutter.dev/docs)
- [Mise Version Manager](https://mise.jdx.dev/)
- [Warp Terminal](https://www.warp.dev/)

---

## 📄 License

This project is open source. License information will be added soon.

---

<div align="center">

**Made with ❤️ for the AI-assisted development community**

*Establish trust through transparency, consistency, and user control*

[⬆ Back to Top](#-ai-agent-rules)

</div>
