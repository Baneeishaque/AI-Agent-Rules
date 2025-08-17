# Git Repos: Auto-clone to sample/path with CLI tools (with Submodule Support)

**Rule ID:** SAMPLE_RULE_ID_5

When cloning repositories, always use platform-specific CLI tools instead of 'git clone' to leverage authentication and features. For GitHub repositories, use 'gh repo clone'. For GitLab repositories, use 'glab repo clone'. Clone all repositories to ~/sample/path/ directory following the hyphenated naming convention (matching the original repo name). Use respective search commands ('gh repo list', 'gh search repos', 'glab repo list', 'glab repo search') to find repositories before cloning.

**Submodule Handling:**
If the cloned repository contains submodules, always initialize and update them recursively:
- After cloning, run:
  - git submodule update --init --recursive
  - Ensure all submodules are properly fetched and initialized.

**Platform-Specific Behaviors:**
- GitHub: Use gh repo clone instead of git clone
- GitLab: Use glab repo clone instead of git clone
- Default location: ~/sample/path/
- Consistent naming: Maintain original repository naming (hyphenated)
- CLI authentication: Leverage platform-specific authentication

**Usage Examples:**
- GitHub: gh repo clone user/repository-name → ~/sample/path/repository-name/
- GitLab: glab repo clone group/project-name → ~/sample/path/project-name/
- Search: gh repo list, gh search repos, glab repo list, glab repo search keyword
- Self-hosted: Configure with glab auth login --hostname your-gitlab.com
- Submodules: After cloning, run git submodule update --init --recursive if .gitmodules exists.
