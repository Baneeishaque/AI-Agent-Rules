<!--
title: Brew Upgrade with Exclusions
description: Upgrade all packages except specified ones with explicit command generation.
category: Package Management
-->

# Brew Upgrade with Exclusions

## Rule: brew-upgrade-with-exclusions

When user says to upgrade brew packages except/excluding specific package(s), follow this workflow:

### 1. USER SPECIFIES EXCLUSIONS
- User will say "upgrade except package-x" or "exclude package-x and package-y from upgrade"
- Note all packages to exclude (can be formulas or casks)

### 2. DRY RUN CHECK
- Run: `brew upgrade --greedy --dry-run`
- Parse output to get all outdated formulas and casks

### 3. FILTER & BUILD COMMAND
- Remove excluded package(s) from the list
- Build explicit command: `brew upgrade --greedy --verbose [pkg1] [pkg2] ...` (without excluded packages)

### 4. PRESENT COMMAND
- Show the complete command for user to execute manually
- Do not execute automatically

## Key Behaviors
- Always use `--greedy` flag (includes auto-update casks)
- Always use `--verbose` flag (maximum logging)
- List all packages explicitly in the command
- Support multiple exclusions (package-x, package-y, package-z, etc.)
- User executes the command manually

## Trigger Phrases
- "upgrade except [package-name]"
- "upgrade excluding [package-name]"
- "upgrade but not [package-name]"
- "upgrade all except [package-x] and [package-y]"

## Example Workflow

**User Input:**
```
upgrade except google-chrome@canary
```

**Agent Actions:**
1. Run `brew upgrade --greedy --dry-run`
2. Parse output showing:
   - Formulas: gh, supabase-beta, gemini-cli, node, ollama
   - Casks: amazon-q, discord@ptb, google-chrome@canary, postman, visual-studio-code@insiders, warp@preview, whatsapp@beta
3. Exclude `google-chrome@canary` from the list
4. Present command:
```bash
brew upgrade --greedy --verbose gh supabase/tap/supabase-beta gemini-cli node ollama amazon-q discord@ptb postman visual-studio-code@insiders warp@preview whatsapp@beta
```
