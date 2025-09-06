# Scripts: Management, Standards, and Execution (with Write-Message Safeguard)

When "script" is mentioned, default to PowerShell (.ps1) scripts unless explicitly stated otherwise (e.g., "bash script", "python script").
All scripts (PowerShell, Bash, Python, etc.) must be saved to their respective scripts folder (e.g., `PowerShell-Scripts`, `Bash-Scripts`, `Python-Scripts`) unless explicitly stated otherwise.
The script folder name must be checked on disk and used accordingly.
Scripts must be compatible with their respective platforms (e.g., Windows PowerShell 5.1+ and PowerShell Core 7+ for PowerShell).
Execute PowerShell scripts using pwsh-preview as the preferred executable, with pwsh as fallback if pwsh-preview is not available.
This applies to all script execution contexts including direct terminal commands, shell configuration files (zsh/bash), and automated workflows.
Always include proper documentation headers with .SYNOPSIS, .DESCRIPTION, .PARAMETER, and .EXAMPLE sections.

**Common Utilities Instruction:**
All scripts must dot-source `Common-Utils.ps1` and use its reusable functions for output, file handling, and other common operations, unless explicitly stated otherwise.
Any reusable functions required by multiple scripts must be implemented in `Common-Utils.ps1` to ensure DRY principles and maintainability.

**Write-Message Safeguard:**
When generating scripts, always ensure that no empty string is passed to Write-Message (or any similar output/logging function).
- Add logic to check if the message is empty or null before calling Write-Message.
- If the message is empty, skip the call or provide a default message.
- Example:
  ```powershell
  if (![string]::IsNullOrWhiteSpace($Message)) {
      Write-Message $Message
  }
  ```

**Key Behaviors:**
- "script" = PowerShell (.ps1) by default
- Repository: ~/sample/path/Sample_Scripts/ (or detected scripts folder)
- Execution priority: pwsh-preview → pwsh (fallback)
- Cross-platform compatibility required
- Comprehensive documentation mandatory
- Safeguard against empty messages in output/logging functions
- Always use the correct scripts folder for each language, unless explicitly overridden

**Usage Examples:**
- "Create a script" → PowerShell script created in PowerShell-Scripts folder
- "Run script from zsh" → pwsh-preview -File script.ps1
- "Create bash script" → Bash script created in Bash-Scripts folder (explicit override)
- "Write-Message" calls always checked for empty strings
