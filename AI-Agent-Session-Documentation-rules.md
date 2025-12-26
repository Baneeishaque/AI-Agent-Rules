<!--
title: AI Agent Session Documentation
description: Protocol for documenting AI agent sessions or conversations as Markdown, including file attachment references, structured data, and traceability.
category: Core Agent Behavior
-->

# AI Agent Session Documentation Rules

## 1. Core Principle

All significant AI agent sessions or conversations must be documented in Markdown, with clear references to any files or artifacts involved. This ensures traceability, reproducibility, and context for future reviews or audits.

## 2. Documentation Protocol

- **Session Log Location:** Store session logs in a dedicated folder (e.g., `docs/conversations/`).
- **File Naming:** Use a timestamped, descriptive filename (e.g., `2025-12-27-session-topic.md`).
- **Session Metadata:** Begin each log with metadata including date, topic/objective, and participants (if relevant).
- **Conversation Order:** Document the session in strict chronological order, alternating user questions and agent responses. Each entry should be clearly marked as a user or agent message.
- **Attachment References:** For every file referenced or attached, include the full path and a brief description in a dedicated section.
- **Structured Data:** Where possible, include structured data (tables, code blocks, configuration blocks, etc.) to summarize key points, requirements, or outcomes.
- **Cross-References:** Link to related rule files, previous sessions, or relevant documentation for context.
- **Execution Confirmation:** Clearly log any commands run, their output, and the working directory.
- **Change Tracking:** If the session results in file changes, document the before/after state, the rationale, and the method used (e.g., `git mv`, two-step rename).
- **Rule References:** Explicitly list any rules or protocols referenced or followed during the session.
- **Summary Table:** At the end, provide a summary table of requirements, actions, and references.

## 3. Advanced Best Practices (from deep analysis)

- **Explicit Sectioning:** Use clear section headers for each major phase: Request, Analysis, Planning, Execution, Confirmation, and Summary.
- **Problem & Resolution:** If an issue arises (e.g., platform-specific behavior, workflow failure), document the problem, analysis, and the resolution strategy.
- **Implementation Plan:** For technical changes, include a step-by-step plan and note user approval before execution.
- **Artifacts:** List all artifacts produced (e.g., scripts, logs, output files) with their paths.
- **Rule Compliance:** Note compliance with agent planning, tool usage, and commit message rules.
- **Session Continuity:** If a session is continued or referenced in a later session, link both ways for continuity.

## 4. Example Structure

```markdown
# Conversation Log: <Session Topic>

**Date:** 2025-12-27  
**Objective:** <Session Objective>

---

## 1. Request
> <User's question or request>

### Agent Response
<Agent's answer, including any actions taken or recommendations.>

---

## 2. Analysis & Planning
<Agent's analysis, plan, and any user approvals.>

---

## 3. Execution
- Command(s) run, with working directory and exit code.
- File(s) changed, with before/after state if relevant.

---

## 4. Confirmation & Outcome
- User confirmation, agent summary, and any follow-up actions.

---

## 5. Attachments & References

| File/Artifact | Path | Description |
|---------------|------|-------------|
| ...           | ...  | ...         |

- Related Rule: [AI-Agent-rules.md](../AI-Agent-rules.md)
- Related Session: [2025-12-16-file-renaming-task.md](./2025-12-16-file-renaming-task.md)

---

## 6. Structured Data

### Requirements Table

| Requirement | Solution/Action | Reference |
|-------------|----------------|-----------|
| ...         | ...            | ...       |

### Example Code Block

```sh
pdftohtml -xml input.pdf output.xml
```

---

## 7. Summary
<Concise summary of the session, outcomes, and next steps.>
```

---

This enhanced rule incorporates all best practices observed in your attached session logs, including explicit problem/solution documentation, structured data, artifact tracking, and rule compliance. It ensures every session is fully auditable, reproducible, and reference-friendly for future agents and users.
