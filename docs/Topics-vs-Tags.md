# Knowledge Session: GitHub Topics vs. Git Tags

Understanding the distinction between discovery metadata (Topics) and versioned history (Tags) is critical for professional repository management.

***

### 1. GitHub Topics (The "Map")
-   **Purpose**: Discovery, categorization, and SEO. 
-   **Scope**: Global to the repository, regardless of the current branch or commit.
-   **Limit**: 20 "Active" topics (platform limit). Unlimited "Extended" topics can be indexed if written in repository files.
-   **Lifecycle**: Evolve with the project's domain and tech stack. They do not represent specific code states.

### 2. Git Tags (The "Checkpoint")
-   **Purpose**: Versioning, release management, and reproducibility.
-   **Scope**: Tied to a specific commit hash.
-   **Format**: Usually Semantic Versioning (`v1.0.0`, `v2.1.0-beta`).
-   **Lifecycle**: Immutable once created. They represent exactly what the code looked like at a specific point in time.

### 3. The Intersection: GitHub Releases
When a **Git Tag** is pushed, it often triggers a **GitHub Release**. The **Topics** defined for the repository help categorize that release in the GitHub Marketplace or in user searches, but the tag ensures the user gets the correct version of the code.

| Feature | GitHub Topics | Git Tags |
| :--- | :--- | :--- |
| **Primary Goal** | How people *find* the repo | Which *version* they use |
| **Storage** | GitHub Database (Metadata) | Git Object Database (Ref) |
| **Mutability** | High (current project state) | Immutable (historical snapshot) |
| **Limit** | 20 for platform UI | Virtually unlimited |

***

*Created: December 2025*
