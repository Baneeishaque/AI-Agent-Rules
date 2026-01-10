<!--
title: Homebrew Management Rules
description: Comprehensive SSOT for Homebrew operations, including installation preferences, keg-only handling, and exclusion-based upgrade workflows.
category: Package Management
-->

# Homebrew Management Rules

This document serves as the Single Source of Truth (SSOT) for all Homebrew operations. It ensures consistent, high-fidelity package management with a focus on reliability and visibility.

***

### 1. Global Preferences & Performance

Before running any `brew` command, the agent MUST ensure maximum visibility and reliability:

- **Sequential Downloads**: To maintain stability on limited bandwidth, always prefix commands with `HOMEBREW_DOWNLOAD_CONCURRENCY=1` if not already set in the environment.
- **Verbose Logging**: Every command MUST include the `--verbose` flag.
- **Example**:
  ```bash
  HOMEBREW_DOWNLOAD_CONCURRENCY=1 brew install --verbose <package>
  ```

***

### 2. Installation & Keg-Only Protocol

When installing new formulas, the agent MUST handle path configurations for non-linked (keg-only) formulas automatically.

- **Auto-Detection**: Run `brew info <package>` immediately after installation.
- **Path Injection**: If the output contains a "keg-only" warning, guide the user to add the package-specific PATH to `~/.zshenv`.
- **Minimalist Configuration**: Only add the `PATH` export. Do NOT add `LDFLAGS`, `CPPFLAGS`, or `PKG_CONFIG_PATH` unless explicitly required for a compilation task.

#### 2.1 Common Keg-Only Examples
- `curl`, `openssl`, `sqlite`, `icu4c`.

***

### 3. Upgrade with Exclusions Workflow

When a user requests to upgrade packages while excluding specific ones, follow this surgical lifecycle:

1. **Outdated Analysis**: Run `brew upgrade --greedy --dry-run` to fetch all pending updates.
2. **Filter Exclusions**: Identify both formulas and casks that the user explicitly wants to skip.
3. **Explicit Command Generation**: Construct a single, explicit command listing all desired packages, excluding the skipped ones.
4. **Manual Presentation**: Present the full command to the user for manual execution. Do NOT execute automatically.

- **Greedy Strategy**: Always include the `--greedy` flag to catch auto-updating casks.
- **Example**:
  ```bash
  # User: upgrade except google-chrome
  # Agent constructs:
  brew upgrade --greedy --verbose gh supabase-beta node postman whatsapp@beta
  ```
