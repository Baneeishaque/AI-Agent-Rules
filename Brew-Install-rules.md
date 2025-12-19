<!--
title: Brew Install Preferences
description: Prefer head/source builds and verbose logging for Homebrew installations.
category: Package Management
-->

# Brew: Ensure Maximum logs

> **Prerequisite:** Follow [Brew-Common-rules.md](./Brew-Common-rules.md) for sequential download and verbose logging requirements.

---

**Installation Instructions:**
1. Always use verbose logging: --verbose flag

## Keg-Only Package Handling

**Auto-Detection Protocol:**
Whenever a formula is installed using brew, automatically check if it is keg-only by running `brew info {package}` after installation.

**If Keg-Only (output contains "keg-only" warning):**
1. Guide user to add package-specific PATH to `~/.zshenv` after the brew shellenv line
2. Only add the PATH export line: `export PATH="/opt/homebrew/opt/{package}/bin:$PATH"`
3. Do NOT add LDFLAGS, CPPFLAGS, or PKG_CONFIG_PATH unless user explicitly needs them for compilation/linking
4. These compilation flags can be used temporarily when needed

**Common keg-only packages:** curl, openssl, sqlite, etc.

**Example:**
```bash
# After installing curl
brew info curl  # Check if keg-only

# If keg-only, add to ~/.zshenv:
export PATH="/opt/homebrew/opt/curl/bin:$PATH"

# Only if compilation needed (temporary or permanent):
export LDFLAGS="-L/opt/homebrew/opt/curl/lib $LDFLAGS"
export CPPFLAGS="-I/opt/homebrew/opt/curl/include $CPPFLAGS"
export PKG_CONFIG_PATH="/opt/homebrew/opt/curl/lib/pkgconfig:$PKG_CONFIG_PATH"
```
