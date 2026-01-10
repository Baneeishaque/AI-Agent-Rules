<!--
title: Git Text Normalization Rules
description: Rules to ensure Git treats text files correctly across encodings and platforms, preventing binary diffs and EOL churn.
category: Git & Repository Management
-->

# Git Text Normalization Rules

Apply this rule when converting file encodings, adding `.gitattributes`, resolving “Binary files differ” diffs, or normalizing line endings across Windows, macOS, and Linux contributors. Stakeholders: repository maintainers, committers, CI owners, and release engineers.

***

### 1. Scope Statement

This rule ensures files are stored and diffed as text in Git repositories, prevents accidental binary classification (for example, UTF‑16 with embedded NULs), and coordinates cross‑platform line ending normalization with minimal disruption.

***

### 2. Core Directives

#### 2.1 Encoding and Binary Heuristic
- **MUST** treat files containing embedded NUL bytes (common in UTF‑16) as binary until the repository blob is replaced with a text blob.  
- **MUST** convert working files to UTF‑8 before staging if the intent is to store them as text.  
- **MUST** verify both working tree and committed blobs for NUL bytes when diagnosing binary diffs.

#### 2.2 .gitattributes Policy
- **MUST** prefer path‑scoped attributes when only a few files require normalization:
```gitattributes
# Prefer narrow scope; mark only the specific file as text
requirements.txt text
```
- **MUST NOT** add broad patterns (for example, `*.txt text`) without team coordination because they can trigger large renormalize commits.
- **MUST** commit `.gitattributes` before renormalizing files so the rule is in effect for subsequent adds.

#### 2.3 LFS and Attributes Interaction
- **MUST** verify Git LFS tracking before changing attributes:

```bash
git lfs ls-files
```
- **MUST NOT** assume `.gitattributes` removes LFS tracking; untrack and re-add following LFS procedures if normal Git behavior is desired.

### 3. Operational Procedures

#### 3.1 Safe Conversion Workflow: Single File
Convert file on disk to UTF‑8 and replace the working file:

```bash
iconv -f utf-16le -t utf-8 requirements.txt > requirements.txt.utf8
mv requirements.txt.utf8 requirements.txt
```

Verify no NULs in working tree and HEAD:

```bash
od -An -tx1 -v requirements.txt | grep -qw '00' && echo "NULs found" || echo "no NULs"
git show HEAD:requirements.txt | od -An -tx1 -v | grep -qw '00' && echo "NULs in HEAD" || echo "no NULs in HEAD"
```

Stage and commit the UTF‑8 blob:

```bash
git add requirements.txt
git commit -m "fix(text): convert requirements.txt to UTF-8"
```

#### 3.2 Renormalize with Minimal Disruption
Preview renormalization before committing:

```bash
git add --renormalize --dry-run requirements.txt
git status --porcelain
```

Apply renormalization only after review:

```bash
git add --renormalize requirements.txt
git commit -m "chore(text): renormalize requirements.txt line endings"
```

#### 3.3 Replace Remote Blob When Needed
If remote still contains a binary blob, **MUST** push the commit to update remote:

```bash
git push origin <branch>
```

If push is not possible or LFS is involved, use:

```bash
git rm --cached requirements.txt
git add requirements.txt
git commit -m "chore(text): replace binary blob with UTF-8 text"
git push
```

### 4. Cross Platform Considerations

#### 4.1 Line Ending Strategy
**MUST** recommend platform settings:

- **Windows**: `core.autocrlf=true`
- **macOS/Linux**: `core.autocrlf=input` or `false`

**MUST** document the chosen strategy in `CONTRIBUTING.md`.

#### 4.2 Team Coordination
- **MUST** announce renormalization changes before applying them.
- **MUST** perform renormalize commits in a single, small commit and schedule during low‑activity windows to reduce merge conflicts.
- **MUST** instruct contributors to stash or commit local work and run:

```bash
git pull --rebase
git reset --hard HEAD   # only after stashing or committing local changes
```

### 5. Verification and Rollback

#### 5.1 Verification Steps
**MUST** confirm HEAD and origin blobs contain no NULs:

```bash
git fetch origin
git show origin/<branch>:requirements.txt | od -An -tx1 -v | grep -qw '00' && echo "NULs in origin" || echo "no NULs in origin"
```

**MUST** verify diffs render as text in code review tools after push.

#### 5.2 Rollback and Recovery
If renormalization causes unexpected churn, **MUST** revert the renormalize commit:

```bash
git revert <commit-sha>
```

For history rewrite only with explicit team approval, use interactive rebase or `filter‑branch`/BFG with coordination and clear communication.

### 6. Prohibited Behaviors and Commit Guidance

- **MUST NOT** add `*.txt text` repository‑wide without prior team approval when multiple platforms are in use.
- **MUST NOT** use `git reset --hard` as a default synchronization method; require explicit confirmation and explain data loss risk.
- **MUST** follow Conventional Commits for renormalization and encoding changes:

```text
chore(text): normalize line endings for requirements.txt
fix(text): convert requirements.txt from UTF-16LE to UTF-8
```

### 7. Verification Checklist
- [ ] **Blob check**: HEAD and origin contain no NULs.
- [ ] **Diff check**: GitHub or Git client shows textual diff.
- [ ] **LFS check**: File not tracked by LFS unless intended.
- [ ] **Team notice**: Contributors informed and given pull instructions.