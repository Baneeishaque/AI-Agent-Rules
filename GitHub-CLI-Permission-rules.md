# Enhanced GitHub CLI Permission Rules

This document outlines the mandatory protocol for an AI agent's use of the GitHub CLI (`gh`), emphasizing the need for explicit user permission before executing any command. This rule is a critical safeguard to ensure user control, prevent unintended actions, and uphold the principles of security and transparency.

-----

### 1\. Core Principles: Why Permission is Mandatory 🛡️

The GitHub CLI provides direct access to a user's repositories, organizations, and sensitive data. Unrestricted execution could lead to unintended consequences, such as:

  * **Accidental Data Modification:** Modifying or deleting branches, issues, or repositories without user consent.
  * **Security Risks:** Exposing sensitive information from private repositories or inadvertently granting unauthorized access.
  * **Loss of Control:** The user loses visibility and control over actions performed on their behalf.

Therefore, the AI must strictly adhere to the following principles:

  * **Explicit User Approval:** No `gh` command, especially those with destructive potential, shall be executed without clear, affirmative permission from the user.
  * **Transparency:** The agent must be fully transparent about its intentions, clearly stating the exact command it plans to run.
  * **Full Command Visibility:** The full output of any executed `gh` command, including both standard output and standard error, must be shown to the user. This aligns with the `AI-Tools-rules.md` mandate for full output visibility.

-----

### 2\. The Permission Protocol: Step-by-Step 📜

Before executing any GitHub CLI command, the AI agent must follow this protocol:

1.  **Initial Plan:** The AI should include the intended `gh` command as a step in its planning phase, as mandated by the `AI-Agent-rules.md`. This allows the user to see the planned action before any execution begins.
2.  **State the Command:** The agent must clearly and explicitly state the exact `gh` command it intends to execute. This includes all flags, arguments, and parameters.
      * **Example:** "I need to run `gh repo clone my-org/my-repo` to clone the repository."
3.  **Explain the Rationale:** The agent must briefly explain *why* it needs to run the command and what the expected outcome is.
4.  **Request Approval:** The agent must explicitly ask for user approval to proceed with the command execution. The request should be direct and unambiguous, such as: "Do you approve this command? Yes/No."
5.  **Execution:** Only after receiving an explicit "Yes" or other affirmative confirmation from the user may the agent proceed.

-----

### 3\. Handling Specific `gh` Commands 🗂️

The permission protocol applies to all `gh` commands, but some require special attention due to their nature.

  * **Cloning Repositories:** For cloning operations (e.g., `gh repo clone`), the agent must follow the `Git-Repo-Cloning-rules.md`, including cloning to the `~/sample/path/` directory and handling submodules recursively.
  * **Non-Destructive Commands:** Even commands that are typically non-destructive (e.g., `gh repo list`, `gh issue status`) still require explicit permission. While they may not alter data, they can reveal sensitive information about the user's repositories or account status.
  * **Write Operations:** Any command that involves writing to files, such as `gh pr create --title "My Title" --body-file /path/to/file.md`, also falls under the `AI-Tools-rules.md` mandate for user confirmation before any file write operations. The AI should present the exact content to be written to the file for approval.

This rule is a foundational component of a secure and collaborative agent-user interaction model. Adherence to this protocol ensures that all actions performed with the GitHub CLI are intentional, transparent, and user-approved.
