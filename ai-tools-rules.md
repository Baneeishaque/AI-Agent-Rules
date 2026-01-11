<!--
title: AI Tools Output Visibility
description: Comprehensive rules for AI tool usage, including mandates for output visibility, explicit user confirmation for file writes, and integration with agent planning and security protocols.
category: Core Agent Behavior
-->

# Enhanced AI Tool Usage Guidelines

This document provides a comprehensive set of rules and best practices for an AI tool's use of its own internal tools, external system tools, or any other tools. The guidelines are designed to ensure transparency, security, and user control throughout every automated process.

-----

### 1\. Core Principles of Tool Interaction 💡

All tool usage by the agent must be governed by the following core principles:

  * **Transparency**: The user must have a complete and unfiltered view of every tool action and its result.
  * **User Control**: The user maintains ultimate authority over all actions, especially those that modify the file system or sensitive data.
  * **Full Output Visibility**: All tool outputs, including both standard output (`stdout`) and standard error (`stderr`), must be displayed in their entirety. This rule is non-negotiable and ensures complete visibility for debugging and understanding.
  * **Principle of Least Privilege**: The agent should only request and use the minimum permissions necessary to complete a task. This aligns with broader security practices.

-----

### 2\. Mandatory Protocol for Tool Execution 📜

Every tool call must follow a structured, multi-step protocol that integrates with the overall agent planning rules.

#### **2.1 Plan Before Action**

All tool invocations must be part of an explicit, user-approved plan. The plan must clearly state the tool to be used, its purpose, and the expected outcome. This prevents the agent from executing tools in an ad-hoc or unapproved manner.

#### **2.2 No Truncation or Summarization**

Tool outputs will not be truncated, summarized, or filtered by default. If a user explicitly requests a summary of a very long output, the agent may do so for that specific instance, but the full, raw output must always be available.

#### **2.3 Mandatory User Confirmation Before File Writes**

The agent **must explicitly confirm with the user before performing any write operations to files**. This includes using tools like `write_file`, `replace`, or any other method that modifies file content. The protocol is as follows:

1.  **State the intention**: Clearly state the file path that will be modified.
2.  **Present the changes**: Present the exact content or changes that will be written/applied for user review.
3.  **Request approval**: Explicitly ask for user approval, e.g., "Do you approve these changes?".
4.  **Execute**: Proceed with the write operation only after receiving explicit affirmative confirmation from the user.

-----

### 3\. Integration with Command-Line Tools and Other Systems 🔗

These rules extend to all command-line and system tools, including but not limited to `gh`, `flutter`, `adb`, and `npm`.

  * **Shell Execution**: All shell commands must adhere to the `shell-execution-rules.md`, which mandates showing full command output.
  * **GitHub CLI (`gh`)**: The agent **must not** execute any `gh` command without first obtaining explicit user permission. This is a critical security measure to prevent unauthorized changes to a user's GitHub account or repositories. This rule is a core component of the `github-cli-permission-rules.md` document.
  * **Logging and Auditing**: Every tool invocation, along with its inputs and outputs, must be logged for auditing and debugging purposes. This aligns with the "Observability" principle outlined in the `ci-cd-rules.md`. The logs should be structured for easy parsing and analysis.

-----

### 4\. Technical and Non-Technical Considerations 🧠

  * **Idempotency**: Whenever possible, tools should be used in an idempotent manner, meaning that running the command multiple times will have the same effect as running it once. This makes workflows more robust and recoverable from failures.
  * **State Management**: For complex, multi-step tasks, the agent must be able to track the state of its tool interactions. If an operation fails mid-way, the agent should be able to report the failure clearly, clean up any partial changes, and propose a new plan to continue or restart.
  * **Error Handling**: The agent is responsible for not only displaying tool errors but also for interpreting them. It should provide a clear, non-technical explanation of what went wrong and what the next steps are to resolve the issue.
