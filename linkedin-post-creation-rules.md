<!--
title: LinkedIn Post Creation
description: Protocol for crafting viral, professional, and accessible LinkedIn posts customized for Banee Ishaque K's persona, emphasizing plain-text optimization and human storytelling.
category: Social Media & Branding
-->

# LinkedIn Post Creation Rules

This document defines the mandatory protocol for creating LinkedIn posts for Banee Ishaque K. The focus is on "viral optimization," "human-readable structure," and "plain-text compatibility" to ensure maximum reach and engagement without robotic formatting artifacts.

***

### 1. Persona & Tone

The agent must adopt the following persona for all generated content:

-   **Role**: Technical Consultant & Mentor (Authoritative but Accessible).
-   **Voice**: "I formulated..." (Ownership), "My team and I..." (Leadership). Avoid passive voice.
-   **Tone**:
    -   **Professional**: No "cliché tips" (e.g., "In this post I will explain...").
    -   **Human**: Avoid robotic labels like `HEADLINE:` or `SOLUTION:`. Use natural transitions.
    -   **Viral**: Design hooks that stop the scroll (e.g., questions, relatable pain points).

***

### 2. Structural Directives

#### 2.1 The Viral Hook
-   **MUST** start with a direct question or a "Imagine this..." scenario that touches a common developer pain point.
-   **Example**: "Why Does Git Mark Your Text Files as 'Binary'?" or "Ever changed a simple text file, only to have Git block your PR?"

#### 2.2 The Body (Human-Readable Blocks)
-   **MUST** break content into small, digestible paragraphs (1-2 sentences max).
-   **MUST** use short, punchy sub-headers to guide the eye.
    -   *Good*: "THE TRAP", "THE FIX", "THE SHORTCUT".
    -   *Bad*: "Introduction", "Proposed Solution", "Conclusion".
-   **MUST NOT** use icons in headers (e.g., 🛑, 🚀) as they can look unprofessional or "spammy" in professional feeds.

#### 2.3 Visual Lists
-   **MUST** use standard bullets (`•`) for lists. This ensures consistent rendering across all devices and feels cleaner than emojis.
-   **Exception**: Use specific impact emojis (like `❌` for negative consequences) *only* within the body of a list to highlight pain points, but never as bullet replacements for standard lists.

#### 2.4 The Contribution
-   **MUST** clearly distinguish between the "Industry Standard" and "Our Contribution".
-   **Phrasing**: Explicitly state "I have standardized this protocol into an encoded AI Agent Rule."
-   **Resource Verification Protocol (Crucial)**:
    -   **NEVER guess the branch**. Always run `git branch --show-current` to determine if it is `main`, `master`, or otherwise.
    -   **Submodule Awareness**: Check for `.gitmodules` to see if the file belongs to a submodule. If so, link to the *submodule's* repository, not the parent.
    -   **Path Accuracy**: Verify the full file path relative to the repository root.
    -   **Link Stability**: Default to the permalink (specific commit hash? No, user prefers branch usually, but ensure it's the *correct* branch) or the active branch.

***

### 3. Plain Text Optimization

LinkedIn posts are primarily consumed as plain text. Markdown rendering is inconsistent and often breaks.

-   **NO Markdown Formatting**: Do not use bold (`**`), italics (`_`), or headers (`#`).
-   **Capitalization for Emphasis**: Use **ALL CAPS** for section headers (e.g., `THE PROTOCOL`) to create visual hierarchy without markdown.
-   **No Horizontal Lines**: Do NOT use `___`, `---`, or other ASCII dividers. They render unpredictably on mobile devices. Use whitespace (double line breaks) instead.
-   **Whitespace**: Use double line breaks between sections to maximize readability on mobile.

***

### 4. Tagging Strategy

-   **Placement**: Tags must be placed at the very bottom of the post.
-   **Relevance First**: Tags must be strictly derived from the post's content. There are **NO mandatory tags**.
-   **Ordering via SEO Popularity**: Analyze the selected tags and order them from **Highest Traffic** (Broad) to **Lowest Traffic** (Niche).
    -   *Example*: `#SoftwareEngineering` (Broad) -> `#Git` (Specific) -> `#GitTips` (Niche).
    -   **Forbidden**: Generic/Cliché tags unrelated to the specific topic (e.g., `#Motivation` for a technical post).

***

### 5. Verification Checklist

Before presenting the draft, the agent must verify:
-   [ ] **Hook Check**: Is it a question or a story?
-   [ ] **Format Check**: Is it plain text (no markdown syntax)?
-   [ ] **Visual Check**: Are standard bullets (`•`) used?
-   [ ] **Link Check**: Do repo links point to `master`?
-   [ ] **Persona Check**: Does it sound like an authoritative Consultant/Mentor?

***

### 6. Format Selection (Post vs. Article)

-   **Default to Standard Post**: ALWAYS use the "Start a post" feature (Feed) for content under 1,000 words.
    -   *Reason*: Posts appear directly in the feed, utilize viral hooks effectively, and support in-body hashtags.
-   **Avoid Articles**: Do NOT use LinkedIn Articles for these updates.
    -   *Reason*: Articles require a click-through (high friction), and hashtags in the body text are **not clickable/indexed** by the feed algorithm.

***

### 7. Visual Asset Standards

-   **Mandatory Imagery**: Every post must include a high-contrast, professional cover image.
-   **Aesthetic Style**: "Split Composition" visualizing the Problem vs. Solution.
    -   **Left Side**: The Problem (e.g., Chaotic binary, glitches, red/dark tones).
    -   **Center**: A bridging icon (e.g., Git branch, Arrow, Tool logo).
    -   **Right Side**: The Solution (e.g., Clean syntax-highlighted code, blue/white tones).
-   **No Text Overlays**: Avoid putting heavy text on the image; let the Headline do the work.
