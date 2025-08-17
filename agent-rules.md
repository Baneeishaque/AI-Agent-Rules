# Microsoft Copilot AI Rules Index

This file serves as the central index for all rule files in this repository. Each rule is maintained in a dedicated markdown file for modularity, scalability, and ease of maintenance.

## How to Use
- **Browse:** Find the rule domain below and follow the link to its file.
- **Add/Modify Rules:** Create or update the appropriate domain file, then update this index.
- **Sync:** Always keep this index up-to-date when rules are added or changed.

## Rule Files

| Rule Domain                | File Name                                   | Description |
|----------------------------|---------------------------------------------|-------------|
| Flutter Build Logging      | [Flutter-Build-rules.md](./Flutter-Build-rules.md) | Maximum logging for Flutter builds |
| Git Repository Creation    | [Git-Repository-rules.md](./Git-Repository-rules.md) | Standard structure, naming, and documentation |
| Script Management          | [Script-Management-rules.md](./Script-Management-rules.md) | PowerShell script standards and safeguards |
| Git Repo Indexing          | [Git-Repository-Indexing-rules.md](./Git-Repository-Indexing-rules.md) | Auto-index codebases in git repos |
| Git Repo Cloning           | [Git-Repo-Cloning-rules.md](./Git-Repo-Cloning-rules.md) | CLI-based cloning, submodule support |
| Brew Install Preferences   | [Brew-Install-rules.md](./Brew-Install-rules.md) | Prefer head/source builds, verbose logging |
| Rule Management Workflow   | [Rule-Management-rules.md](./Rule-Management-rules.md) | Documentation sync and update workflow |
| Repository Search          | [Repository-Search-rules.md](./Repository-Search-rules.md) | Multi-platform repo discovery and smart cloning |
| Android App Launch         | [Android-App-Launch-rules.md](./Android-App-Launch-rules.md) | Automated emulator setup and deployment |

## Adding New Rules
1. Create a new markdown file named `<Domain>-rules.md`.
2. Add your rule(s) with clear descriptions and examples.
3. Update the table above with the new file and a short description.
4. Commit changes with a conventional commit message.

---
_Last updated: 2025-08-17_
