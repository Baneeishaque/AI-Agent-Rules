<!--
title: AI Agent Rule Standardization Rules
description: Craftsmanship standards for developing "Ultra-Lean Industrial" AI Agent Rules, ensuring consistent formatting, structural hierarchy, and pedagogical clarity.
category: Rule-Management
-->

# AI Agent Rule Standard Creation

This document defines the craftsmanship standards for creating new AI Agent Rules. Adhering to these protocols ensures that all rules remain professional, machine-parseable, and human-readable.

***

### 1. Preparation & Context Assembly (Crucial)

Before drafting a rule file, the agent MUST:
1. **Assemble Conversation Points**: Review the entire conversation history to capture specific user preferences, edge cases discussed, and implied constraints (e.g., "plain text only", "no icons").
2. **Identify Edge Cases**: Explicitly document "what not to do" based on user feedback (e.g., "Articles don't support tags").
3. **Synthesize Limitations**: If a platform or tool has limitations (e.g., LinkedIn Article tags), the rule MUST address them.

***

### 2. File Naming & Meta-Data

All rule files must be stored in the `AI-Agent-Rules` directory.

- **Fine Naming**: Use strictly lowercase, kebab-case ending in `-rules.md` (e.g., `git-submodule-rules.md`).
- **YAML Frontmatter**: Every file MUST start with the following metadata block:
    ```markdown
    <!--
    title: [Short, Impactful Title]
    description: [One-sentence summary of the rule's scope]
    category: [Existing or New Category]
    -->
    ```

***

### 2. Structural Hierarchy

Rule files must follow a predictable, industrialized structure to maximize readability:

1. **H1 Title**: Matches the YAML title but is more formal (e.g., `# Git Submodule Management Rules`).
2. **Scope Statement**: A brief paragraph defining *why* the rule exists and who the stakeholders are.
3. **Section Dividers**: Use `***` (horizontal rules) between major H3 sections.
4. **Numbered Sections**: Use H3 headers with sequential numbering (e.g., `### 1. Preparation & Context Assembly`).
5. **Sub-sections**: Use H4 for specific technical details (e.g., `#### 1.1 Command Syntax`).

***

### 3. Content Philosophy (Ultra-Lean Industrial)

The content must balance conciseness with technical depth:

- **Zero Noise**: Avoid introductory fluff, "happy to help" phrases, or redundant explanations.
- **Pedagogical Snippets**: Use code blocks to demonstrate correct command usage or file formats.
- **Prohibited Behaviors**: Explicitly list actions the agent is forbidden from taking.
- **Mandatory Protocols**: Use clear, imperative language (e.g., "The agent MUST...", "The agent is BLOCKED from...").

***

### 4. Verification & Commit

Before finalizing a new rule:
1. **Cross-Reference**: Check for existing rules to avoid duplication.
2. **Lint Check**: Ensure all content complies with **[Markdown Generation Rules](./markdown-generation-rules.md)**.
3. **Sync Trigger**: Remind the user to trigger the `agent-rules.md` update workflow.
4. **Commit Message**: Use Conventional Commits (e.g., `feat: establish standard creation rules for AI agents`).
