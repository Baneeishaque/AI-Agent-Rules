# Repository Search: Multi-Platform Discovery and Smart Cloning

When asked to clone repositories (without a specified provider), always follow this search order:

1. User GitHub Repositories:
   - Search under the authenticated GitHub account using gh repo list (personal and organization repos).
2. User GitLab Repositories:
   - Search under the authenticated GitLab account using glab repo list (personal and organization repos).
3. GitHub Public Search:
   - Use gh search repos [keyword] --limit 10 for public/global discovery.
4. GitLab Public Search:
   - Use glab repo search [keyword] for public/global discovery.
5. Fallback:
   - If not found in any of the above, prompt for manual repo URL or use git clone [url] ~/Lab_Data/[repo-name] as last resort.

**Fallback Cloning Procedure:**
- If CLI tools do not find the repository, request the user to provide the direct repository URL.
- Use git clone [url] ~/Lab_Data/[repo-name] to clone manually.
- After cloning, check for submodules and run git submodule update --init --recursive if .gitmodules exists.

**Cloning Workflow:**
- Destination: Always clone to ~/Lab_Data/ directory.
- Naming: Preserve original repository name (hyphenated format preferred).
- CLI Tools: Use gh repo clone or glab repo clone for authentication and features.
- Submodules: After cloning, run git submodule update --init --recursive if .gitmodules exists.

**Enhanced Features:**
- Interactive Selection: When multiple matches found, present options to user.
- Repository Info: Show basic repo info (stars, description, language) before cloning.
- Branch Selection: Clone default branch unless specified otherwise.
- Authentication: Leverage CLI tool authentication (gh auth, glab auth).

**Usage Examples:**
- gh repo list → Search your own GitHub repos first.
- gh search repos flutter todo --limit 5 → Search public GitHub repos.
- glab repo list → Search your own GitLab repos.
- glab repo search mobile-app → Search public GitLab repos.
- gh repo clone user/awesome-project → ~/Lab_Data/awesome-project/
- glab repo clone group/mobile-app → ~/Lab_Data/mobile-app/
