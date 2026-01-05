<!--
title: Git Commit Message Generation
description: Strict rules for generating git commit messages, enforcing Conventional Commits, contextual information in titles, and no redundancy between title and body.
category: Git & Repository Management
-->

# Git Commit Message Generation Rules

This document outlines the strict rules for generating Git commit messages. These rules ensure history is readable, automated tools can parse changes, and the intent of every change is clear.

---

### 1. Format Specification

-   **Standard**: Follow the **Conventional Commits** specification.
    -   Format: `type(scope): description`
    -   Common Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.
-   **Plain Text Only**: The final commit message must be **Plain Text**.
    -   **No Markdown**: Do not use bold (`**`), italics (`*`), or code blocks (`` ` ``).
    -   **Allowed Symbols**: You MAY use standard punctuation and symbols for clarity (e.g., `-`, `:`, `()`, `[]`).

---

### 2. Title Line (Header)

The first line is the most important part of the commit message.

-   **Content**: A strong, concise summary of the *entire* change.
-   **Context**: Include critical contextual information (e.g., dates for meetings, releases, or time-sensitive changes).
-   **Length**:
    -   **Ideal**: < 50 characters.
    -   **Hard Limit**: 72 characters.
-   **Case**: Use the **Imperative Mood** (e.g., "add feature" not "added feature" or "adds feature").
-   **Punctuation**: Do not end the title line with a period.
-   **Reference Style**: When referring to documentation sections, use the **Section Title** instead of the Section Number (e.g., use "Refine Migration, Verification & Secrets protocol" instead of "Update Section 9").

---

### 3. Body (Description)

The body provides the detailed context.

-   **Separation**: There must be a **blank line** between the Title and the Body.
-   **Structure**: Use **Bullet Points** (`- `) for all details. Do not use paragraphs of text.
-   **Wrapping**: Wrap all lines at **72 characters**.
-   **Content**:
    -   Focus on **What** changed and **Why**.
    -   Summarize the impact of the changes.
-   **No Redundancy**: Do not repeat information already stated in the title. Provide supplementary details ONLY.
-   **Meaningful Summaries**: Avoid exhaustive lists for repetitive changes (e.g., individual spell check words). Instead, provide a higher-level summary of the domain or impact (e.g., "Add 30+ project domain terms to workspace dictionary").
-   **Self-Documenting Titles**: For standard style cleanups or simple deletions, the body MAY be omitted entirely if the title is exhaustive. Avoid adding "filler" or "gibberish" to satisfy a structure requirement.

---

### 4. Example

**Correct Format:**

```text
feat(auth): implement JWT token refresh strategy

Update the authentication flow to handle expired tokens automatically
without forcing a user logout.

- Add 'RefreshToken' service to handle token rotation.
- Update 'AuthInterceptor' to catch 401 errors.
- Add unit tests for token expiration scenarios.
- Update API documentation with new endpoint details.
```

**Incorrect Format:**

```text
Added new auth features

I added a new way to handle tokens so that users don't get logged out.
It uses a new service and I also updated the interceptor.
**Changes:**
* `RefreshToken` service
* Tests
```

### 5. Submodule Sync Commits (Parent Repository)

- Title must summarize the submodule update and its impact (e.g., chore(submodule): sync [submodule-name] with [key change]).
- Body must list key changes introduced by the submodule update, based on the submodule’s commit messages.
- Do not include only the commit SHA; always summarize the actual changes.
- Do not repeat information from the title in the body.
- Use bullet points for all details, wrap at 72 characters, and follow all other formatting and style rules.
