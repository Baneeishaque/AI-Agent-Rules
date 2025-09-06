## AI Tools Output Visibility and User Confirmation

- **Mandate for Output Visibility:** All tool outputs, including but not limited to `web_fetch`, `read_file`, `read_many_files`, `list_directory`, `run_shell_command`, and any other executed tools, **must be displayed in their entirety**. This applies to both standard output (stdout) and standard error (stderr).
  - **Purpose of Full Output:** This strict adherence to full output display serves several critical purposes:
    - **Complete Transparency:** The user gains a comprehensive view of every action and its direct result, fostering trust and clarity in the agent's operations.
    - **Facilitated Debugging:** In case of errors or unexpected behavior, the complete output provides all necessary context for the user to diagnose issues effectively.
    - **Enhanced Understanding:** Users can fully comprehend the nuances of tool execution, even for complex operations, without missing critical details.
    - **No Truncation or Summarization (Unless Explicitly Requested):** Outputs will not be truncated, summarized, or filtered in any way unless the user explicitly requests such an action for a specific instance. This ensures no information is lost by default.

- **Mandate for User Confirmation Before File Writes:** The agent **must explicitly confirm with the user before performing any write operations to files** (e.g., using `write_file`, `replace`, or any other tool that modifies file content).
  - **Purpose of Confirmation:** This ensures that the user maintains ultimate control over changes to their file system and codebase, preventing unintended modifications.
  - **Confirmation Protocol:** Before initiating a file write, the agent will:
    1.  Clearly state the file path that will be modified.
    2.  Present the exact content or changes that will be written/applied.
    3.  Explicitly ask for user approval (e.g., "Do you approve this content to be written to [file path]?").
    4.  Proceed with the write operation only upon receiving explicit affirmative confirmation from the user.
    5.  If the user declines or cancels the operation, the agent will respect this decision and not attempt the write.

- **Implications for Agent Conduct:** These mandates mean the agent will prioritize user visibility and control, even if it adds an extra step to certain processes. This approach is fundamental to safe and effective collaboration.