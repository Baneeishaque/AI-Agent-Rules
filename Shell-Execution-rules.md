# Shell Execution: Conduct and Output

- The user's shell is zsh.

## Conduct Guidelines:

- **Explain Critical Commands:** Before executing commands that modify the file system, codebase, or system state, provide a brief explanation of the command's purpose and potential impact. Prioritize user understanding and safety.
- **Avoid Interactive Commands:** Prefer non-interactive versions of commands (e.g., `npm init -y` instead of `npm init`). If an interactive command is necessary, inform the user that interactive shell commands are not supported and may cause hangs until canceled by the user.
- **Background Processes:** Use background processes (via `&`) for commands that are unlikely to stop on their own (e.g., `node server.js &`). If unsure, ask the user.
- **Security Reminder:** For critical commands that are particularly likely to modify the user's system outside the project directory or system temp directory, remind the user to consider enabling sandboxes.

## Output Mandate:

- **Show Full Output:** When running any shell command, the agent must always show the full, unmodified output from both stdout and stderr to the user. This ensures transparency and allows the user to assist in debugging any issues.
