<!--
title: AI Agent Session Documentation Rules
description: Protocol for documenting AI agent sessions or conversations as Markdown, including file attachment references, structured data, and traceability.
category: Core Agent Behavior
-->


# AI Agent Session Documentation Rules (Sensitive Data & Relevance)

## 1. Core Principle

All significant AI agent sessions or conversations must be documented in Markdown, with clear references to any files or artifacts involved. This ensures traceability, reproducibility, and context for future reviews or audits.

**Sensitive Data & Relevance Principle:**
Regardless of whether the document is public or private, do not include any unrelated documents, data, or session-irrelevant information. All sensitive data must be redacted or replaced with placeholders (e.g., `[REDACTED]`, `[PLACEHOLDER]`).


## 2. Documentation Protocol (Sensitive Data & Relevance)

- **Session Log Location:** Store session logs in a dedicated folder (e.g., `docs/conversations/`).
- **File Naming:** Use a timestamped, descriptive filename (e.g., `2025-12-27-session-topic.md`).
- **Session Metadata:** Begin each log with metadata including date, topic/objective, and participants (if relevant).
- **Conversation Order:** Document the session in strict chronological order, alternating user questions and agent responses. Each entry should be clearly marked as a user or agent message.
- **Attachment References:** For every file referenced or attached, include the full path and a brief description in a dedicated section. Do not include attachments or references that are not directly relevant to the session.
- **Structured Data:** Where possible, include structured data (tables, code blocks, configuration blocks, etc.) to summarize key points, requirements, or outcomes. Do not include unrelated or session-irrelevant data.
- **Cross-References:** Link only to related rule files, previous sessions, or relevant documentation that is directly relevant to the session.
- **Execution Confirmation:** Clearly log any commands run, their output, and the working directory, but only if directly relevant to the session objective. Omit unrelated execution details.
- **Change Tracking:** If the session results in file changes, document the before/after state, the rationale, and the method used (e.g., `git mv`, two-step rename), but only for session-relevant changes.
- **Rule References:** Explicitly list only the rules or protocols referenced or followed during the session.
- **Summary Table:** At the end, provide a summary table of requirements, actions, and references, but only for session-relevant items.

## 3. Advanced Best Practices (Sensitive Data & Relevance)

- **Explicit Sectioning:** Use clear section headers for each major phase: Request, Analysis, Planning, Execution, Confirmation, and Summary.
- **Sensitive Data Review:** Before finalizing, review the document for any sensitive or unrelated data and redact or remove as needed.
- **Session Relevance:** Exclude unrelated execution logs, attachments, references, or next steps. Only include information directly relevant to the session’s topic and actions.
- **Problem & Resolution:** If an issue arises (e.g., platform-specific behavior, workflow failure), document the problem, analysis, and the resolution strategy, but only if relevant to the session.
- **Implementation Plan:** For technical changes, include a step-by-step plan and note user approval before execution, but only if relevant.
- **Artifacts:** List only artifacts produced that are relevant and non-sensitive.
- **Rule Compliance:** Note compliance only with rules actually applied in the session.
- **Session Continuity:** Link sessions only if directly relevant.

## 4. Example Structure (Sensitive Data & Relevance)

```markdown
# Conversation Log: <Session Topic>

**Date:** 2025-12-27  
**Objective:** <Session Objective>

---

## 1. Request
> <User's question or request, with sensitive info replaced by [REDACTED] if needed>

### Agent Response
<Agent's answer, including any actions taken or recommendations, with sensitive info redacted.>

---

## 2. Analysis & Planning
<Agent's analysis, plan, and any user approvals, with only session-relevant, non-sensitive content.>

---

## 3. Execution
- [Summary of actions taken, omitting unrelated or sensitive details.]

---

## 4. Confirmation & Outcome
- [Session-relevant summary and follow-up actions.]

---

## 5. Attachments & References

| File/Artifact | Path | Description |
|---------------|------|-------------|
| [REDACTED]    | [REDACTED] | [REDACTED] |

- Related Rule: [ai-agent-planning-rules.md](../ai-agent-planning-rules.md)

---

## 6. Structured Data

### Requirements Table

| Requirement | Solution/Action | Reference |
|-------------|----------------|-----------|
| ...         | ...            | ...       |

---

## 7. Summary
<Concise, session-relevant summary. Sensitive or unrelated next steps omitted.>
```

---

This enhanced rule incorporates all best practices observed in your attached session logs, including explicit problem/solution documentation, structured data, artifact tracking, and rule compliance. It ensures every session is fully auditable, reproducible, and reference-friendly for future agents and users.
