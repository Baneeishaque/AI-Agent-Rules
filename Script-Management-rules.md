# Scripts: PowerShell Management, Standards, and Execution (with Write-Message Safeguard)

**Rule ID:** SAMPLE_RULE_ID_3

When "script" is mentioned, default to PowerShell (.ps1) scripts unless explicitly stated otherwise (e.g., "bash script", "python script"). All PowerShell scripts must be saved to ~/sample/path/Sample_Scripts/ repository and committed with proper conventional commit messages. Scripts must be compatible with Windows PowerShell 5.1+ and PowerShell Core 7+. Execute PowerShell scripts using pwsh-preview as the preferred executable, with pwsh as fallback if pwsh-preview is not available. This applies to all script execution contexts including direct terminal commands, shell configuration files (zsh/bash), and automated workflows. Always include proper documentation headers with .SYNOPSIS, .DESCRIPTION, .PARAMETER, and .EXAMPLE sections.

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
- Repository: ~/sample/path/Sample_Scripts/
- Execution priority: pwsh-preview → pwsh (fallback)
- Cross-platform compatibility required
- Comprehensive documentation mandatory
- Safeguard against empty messages in output/logging functions

**Usage Examples:**
- "Create a script" → PowerShell script created
- "Run script from zsh" → pwsh-preview -File script.ps1
- "Create bash script" → Bash script (explicit override)
- "Write-Message" calls always checked for empty strings
