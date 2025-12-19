<!--
title: Brew Common Rules
description: Common Homebrew rules and settings shared across install/upgrade operations.
category: Package Management
-->

# Brew: Common Rules

## Sequential Download Requirement

**Before running any `brew install` or `brew upgrade` command:**
1. Check if `HOMEBREW_DOWNLOAD_CONCURRENCY` is set to `1` in the environment
2. If NOT set, prefix the command with: `HOMEBREW_DOWNLOAD_CONCURRENCY=1`

This ensures packages download one at a time (sequential), which is better for slow/limited bandwidth connections.

**Example:**
```bash
HOMEBREW_DOWNLOAD_CONCURRENCY=1 brew install --verbose package-name
HOMEBREW_DOWNLOAD_CONCURRENCY=1 brew upgrade --greedy --verbose package-name
```

## Verbose Logging

Always use `--verbose` flag for maximum logging output.
