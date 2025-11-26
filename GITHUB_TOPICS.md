# Recommended GitHub Topics for AI-Agent-Rules Repository

This document contains the recommended GitHub topics and tags for this repository to improve discoverability and classification.

## Recommended Topics (20 max allowed by GitHub)

Based on a deep analysis of this repository's content, the following topics are recommended:

### Primary Topics (Core Identity)

| Topic | Description |
|-------|-------------|
| `ai-agent-rules` | Primary identifier for AI agent rule configurations |
| `ai-rules` | General AI rules and guidelines |
| `ai-coding-assistant` | Rules for AI coding assistants |
| `agent-guidelines` | Guidelines for AI agent behavior |
| `prompt-engineering` | Prompt and instruction engineering for AI |

### AI Tools & Platforms

| Topic | Description |
|-------|-------------|
| `warp-terminal` | Rules for Warp terminal AI configuration |
| `github-copilot` | Applicable to GitHub Copilot |
| `cursor-rules` | Applicable to Cursor IDE |
| `claude-code` | Applicable to Claude Code |
| `ai-assistant` | General AI assistant configurations |

### Development Domains

| Topic | Description |
|-------|-------------|
| `flutter` | Flutter app development rules |
| `github-actions` | CI/CD with GitHub Actions |
| `devops` | DevOps and CI/CD best practices |
| `cicd` | Continuous Integration/Deployment |

### Technologies & Concepts

| Topic | Description |
|-------|-------------|
| `best-practices` | Development best practices |
| `coding-guidelines` | Coding guidelines and conventions |
| `documentation` | Documentation and knowledge base |
| `automation` | Development automation rules |
| `shell-scripting` | Shell execution and scripting rules |
| `git` | Git workflow and repository management |

## How to Add Topics to Your GitHub Repository

### Method 1: Via GitHub Web Interface

1. Go to your repository on GitHub: https://github.com/Baneeishaque/AI-Agent-Rules
2. Click the ⚙️ gear icon next to "About" on the right sidebar
3. In the "Topics" field, enter the topics one by one (separated by spaces or commas)
4. Click "Save changes"

### Method 2: Via GitHub CLI

```bash
# Add all recommended topics at once
gh repo edit Baneeishaque/AI-Agent-Rules \
  --add-topic ai-agent-rules \
  --add-topic ai-rules \
  --add-topic ai-coding-assistant \
  --add-topic agent-guidelines \
  --add-topic prompt-engineering \
  --add-topic warp-terminal \
  --add-topic github-copilot \
  --add-topic cursor-rules \
  --add-topic claude-code \
  --add-topic ai-assistant \
  --add-topic flutter \
  --add-topic github-actions \
  --add-topic devops \
  --add-topic cicd \
  --add-topic best-practices \
  --add-topic coding-guidelines \
  --add-topic documentation \
  --add-topic automation \
  --add-topic shell-scripting \
  --add-topic git
```

### Method 3: Via GitHub API

```bash
curl -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer YOUR_GITHUB_TOKEN" \
  https://api.github.com/repos/Baneeishaque/AI-Agent-Rules/topics \
  -d '{
    "names": [
      "ai-agent-rules",
      "ai-rules",
      "ai-coding-assistant",
      "agent-guidelines",
      "prompt-engineering",
      "warp-terminal",
      "github-copilot",
      "cursor-rules",
      "claude-code",
      "ai-assistant",
      "flutter",
      "github-actions",
      "devops",
      "cicd",
      "best-practices",
      "coding-guidelines",
      "documentation",
      "automation",
      "shell-scripting",
      "git"
    ]
  }'
```

## Complete Topics List (Copy-Paste Ready)

```
ai-agent-rules
ai-rules
ai-coding-assistant
agent-guidelines
prompt-engineering
warp-terminal
github-copilot
cursor-rules
claude-code
ai-assistant
flutter
github-actions
devops
cicd
best-practices
coding-guidelines
documentation
automation
shell-scripting
git
```

## Topic Guidelines Followed

- ✅ All topics use lowercase letters, numbers, and hyphens only
- ✅ Each topic is under 50 characters
- ✅ 20 topics total (maximum allowed by GitHub)
- ✅ Topics are relevant to the repository content
- ✅ Topics follow GitHub's naming conventions

## Repository Description Suggestion

Consider updating the repository description to:

> A comprehensive collection of AI agent rules and guidelines for various AI coding assistants including Warp, GitHub Copilot, Cursor, and Claude Code. Covers Flutter, CI/CD, DevOps, Git workflows, and development best practices.

---

*Last updated: 2025-11-26*
