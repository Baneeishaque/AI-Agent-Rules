<!--
title: Shell Execution
description: Guidelines for shell command execution, ensuring transparency, user control, and adherence to security protocols.
category: Core Agent Behavior
-->

# Enhanced Shell Execution Rules

This document provides a comprehensive set of guidelines for an AI agent on the safe, transparent, and effective execution of shell commands. It is a critical component of the overall security and control framework, ensuring that all command-line operations are predictable, auditable, and user-approved.

---

### 1. Core Principles

All shell command execution by the agent must be governed by these fundamental principles:

  * **Explain Critical Commands**: Before running any command that could modify the file system, codebase, or system state, the agent must provide a brief, clear explanation of the command's purpose and potential impact. This prioritizes user understanding and safety.
  * **Full Output Visibility**: The agent **must** display the full, unmodified output from both standard output (`stdout`) and standard error (`stderr`) for every command executed. This ensures complete transparency and provides the user with all the necessary information for debugging.
  * **Prioritize Safety and Non-Destructive Actions**: The agent's default behavior should be cautious. When in doubt about a command's safety, it should seek user clarification or confirmation before proceeding.

---

### 2. Operational Protocol

Every shell command execution must be integrated into the agent's overall planning framework and follow a structured protocol.

#### 2.1 Plan Before Action

As mandated by the `ai-agent-planning-rules.md` document, all shell commands must be part of an explicit, user-approved plan. This prevents the agent from executing commands in an ad-hoc or unapproved manner.

#### 2.2 Interactive Commands

  * **Avoidance**: The agent must prefer and use non-interactive versions of commands whenever possible (e.g., `npm init -y` instead of `npm init`).
  * **Handling Necessity**: If an interactive command is absolutely necessary, the agent must inform the user that it cannot be supported and may cause the process to hang until canceled.

#### 2.3 Background Processes

The agent must use background processes (via `&`) for commands that are not expected to terminate on their own (e.g., a development server). If the agent is unsure, it must ask the user for guidance.

-----

### 3. Integration & Observability

The shell execution rules are not isolated; they are a key part of a larger, integrated system.

  * **User-Provided Input**: The agent must be vigilant about commands that could potentially modify the user's system outside of a designated project directory or system temporary directory. The agent should remind the user to consider sandboxing in these cases.
  * **Auditing and Observability**: Every command executed and its corresponding output must be logged for auditing and debugging. This aligns with the "Observability" principles from the `ci-cd-rules.md`, which mandates structured logging and centralized metrics.
