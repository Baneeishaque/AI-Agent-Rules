<!--
title: Mise Plugin Backend Management Rules
description: Intelligent backend selection for mise plugin installations with fallback handling and user prompts.
category: Package Management
-->

# Mise Plugin Backend Management Rules

## Rule: mise-plugin-backend-management

When installing mise plugins, handle backend selection intelligently based on context:

### For 'mise install [plugin]':
- Check if plugin has multiple backends in mise registry
- If multiple backends exist, prompt user to choose which backend to use
- Install chosen backend: `mise plugins install [plugin] https://github.com/[org]/[repo].git`
- Then run: `mise install [plugin]`

### For 'mise install' (in project folder):
- Follow the project's mise.toml configuration
- If installation fails with plugin errors, check if the failed plugin has alternative backends
- If alternatives exist, prompt user to choose different backend
- Uninstall problematic backend: `mise plugins uninstall [plugin]`
- Install chosen alternative: `mise plugins install [plugin] https://github.com/[org]/[repo].git`
- Retry: `mise install`

## Key Behaviors:
- Always use full GitHub URLs: `https://github.com/[org]/[repo].git`
- Never use `vfox:` or `asdf:` prefix (causes SSH errors)
- User chooses backend per plugin
- Respect mise.toml unless installation fails
- Verify with: `mise plugins --urls --user`

## Example:
- User: "mise install dart" → Prompt: "dart has asdf and vfox backends, which do you prefer?"
- mise.toml install fails → Prompt: "dart installation failed, try vfox backend instead?"
