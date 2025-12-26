# Conversation Log: CI/CD Rulebooks Refinement and De-duplication

**Date:** 2025-12-26  
**Topic:** Establishing a Clear Hierarchy and Single Source of Truth for CI/CD Rules

## Objective
The goal was to refactor the project's CI/CD rulebooks (`CI-CD-rules.md`, `GitHub-Actions-rules.md`, and `GitHub-Action-Creation-rules.md`) to establish a clear separation between high-level agnostic strategy and platform-specific technical implementation, ensuring no duplication or overlap of information.

## Key Changes and Design Decisions

### 1. Hierarchy and Single Source of Truth
- **`CI-CD-rules.md` (Strategy Lead)**: Transformed into a platform-agnostic master document. It now owns all architectural patterns (e.g., Supabase Router → Executor → Render), overall deployment strategies (Canary/Blue-Green), failure handling logic (3-step sequence), and environment standardization policies (Docker).
- **`GitHub-Actions-rules.md` (Implementation Manual)**: Re-focused strictly on the "how-to" for GitHub Actions. Pruned broad strategic descriptions and replaced them with precise implementation details (secret names, specific actions, permission scopes).
- **`GitHub-Action-Creation-rules.md` (Marketplace Specialist)**: Aligned to strictly handle the construction and publishing of Marketplace Actions, offloading general quality standards (version pinning, linting) to the central GHA manual.

### 2. High-Fidelity Restoration
A significant portion of the session was dedicated to restoring precise, high-fidelity technical blocks that were previously condensed or generalized. This ensured that no critical intelligence—such as specific failure handling logic, distribution particulars, or tracking mechanics—was lost.

### 3. Integrated Technical Specifics
Based on deep verification rounds, technical specifics were integrated directly into descriptive logic:
- **Mobile Distribution**: Explicitly linked Firebase App Distribution with the `willynohilly/firebase-app-distribution` action and required secrets (`GOOGLE_SERVICE_ACCOUNT_KEY`, `FLUTTER_SIGNING_KEYS`).
- **Ops Tracking**: Defined the use of `google-github-actions/setup-gcloud` and `${{ secrets.GOOGLE_SHEETS_SERVICE_ACCOUNT }}` for Google Sheets automation.
- **Workflow Fixer Persona**: Integrated "Code Quality Standards 💎" for unified enforcement of version pinning, ShellCheck, Actionlint, and Least Privilege.

### 4. Placeholder Generalization
All project-specific hard-coded values (versions, social handles, job names) were replaced with universal placeholders (e.g., `<SOCIAL_HANDLE>`, `<LTS_VERSION>`, `<MISE_VERSION>`) to make the rulebooks reusable as templates.

## Final State of Rulebooks
- **`CI-CD-rules.md`**: Agnostic, strategy-focused, defines the "What" and "Why".
- **`GitHub-Actions-rules.md`**: Specific, implementation-focused, defines the "How" for GHA.
- **`GitHub-Action-Creation-rules.md`**: Specialized, publishing-focused.

## Dependencies and Tools
- GitHub CLI (`gh`)
- Actionlint & ShellCheck
- Supabase (Orchestrator)
- Render (Runtime)
- Firebase App Distribution (Mobile)
- OIDC (Security)
