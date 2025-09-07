### Flutter Application Development Rules

This document outlines the rules and best practices for developing Flutter applications to ensure high quality, consistency, and long-term maintainability. It serves as a foundational guide for a disciplined and collaborative development workflow, emphasizing a balance between strict reproducibility and staying current.

-----

### 1\. Environment & Setup

  - **Flutter Version:** We will pin the SDK to a fixed version for deterministic builds. To avoid build breaks from new, potentially incompatible updates, we will pin the Flutter SDK to a specific, fixed version. However, we will manually check for and adopt new stable releases with the help of `mise` to benefit from the newest features, performance improvements, and bug fixes. The AI tool will also continuously monitor for and suggest the latest stable SDK versions.
  - **Mise-en-place (Mise):** Use **Mise**, a powerful and fast polyglot tool version manager, to manage Flutter and Dart versions.
      - **Detail:** Mise provides a consistent development environment across different projects and team members. It uses a project-level configuration file, so a new team member only needs to run `mise install` to set up the correct toolchain. This makes it ideal for handling multiple projects that may require different SDK versions.
      - **Configuration:** Use a `mise.toml` file in the project root to pin the **Flutter** version. As Flutter includes a compatible Dart SDK, pinning the Flutter version is sufficient.
      - **Commands:**
          * `mise install`: Installs the specified versions from `mise.toml`.
          * `mise use <tool>@<version>`: Sets a local version for a tool and updates the `mise.toml` file.
          * `mise ls-remote flutter`: Lists available Flutter versions.
          * `mise help`: Provides general help for `mise` commands.
  - **IDE/Editor:** Use a recommended IDE like Visual Studio Code or Android Studio/IntelliJ IDEA with the official Flutter and Dart plugins installed.
      - **Detail:** These IDEs provide a rich development experience with features like code completion, hot reload, hot restart, and integrated debugging, which are essential for a productive workflow.
      - **Configuration:** Regularly check for and install updates to the Flutter and Dart plugins to take advantage of new tooling features and performance improvements.

-----

### 2\. Project Creation & Configuration

  - **Project Initialization:** Create new projects using the `flutter create` command.
      - **Detail:** The project should be configured to support all required target platforms (e.g., iOS, Android, Web, macOS, Windows, Linux) from the start. This proactive approach ensures maximum reach and avoids costly platform-specific refactoring later on.
      - **Command Example:** `flutter create --org com.example.mycompany --platforms android,ios,web,linux,windows,macos my_new_app`
          * `--org`: Specifies the organization's reverse domain name, which is used to generate the platform-specific package identifier (e.g., `com.example.mycompany.my_new_app`).
          * `--platforms`: Explicitly defines the platforms the project will support, setting up the necessary configuration files and code runners.
  - **Git Initialization:** Initialize a Git repository for the project immediately after creation.
      - **Detail:** Version control is the backbone of collaborative development. Committing regularly helps track changes, facilitates code reviews, and allows for safe experimentation and quick reverts.
      - **Adherence:** The `.gitignore` file should be comprehensive, combining the default Flutter-specific rules with general rules for the target operating systems (e.g., macOS, Windows, Linux) and common IDEs (e.g., VS Code, IntelliJ IDEA). We will use a dedicated service like [gitignore.io](https://www.toptal.com/developers/gitignore) to generate a standardized `.gitignore` file for all projects. This file must be committed from the very first commit.
  - **Project Structure:**
      - **Detail:** A consistent and logical folder structure is essential for project scalability and developer onboarding. The recommended structure separates concerns and makes code easier to find and manage.
      - **Recommended Layout:**
        ```
        lib/
        ├── src/
        │   ├── features/          # Code for distinct features (e.g., authentication, user profile)
        │   │   ├── feature_name/
        │   │   │   ├── domain/      # Models, repositories, use cases
        │   │   │   ├── presentation/  # UI widgets, screens, controllers/providers
        │   │   │   └── data/        # Data sources (APIs, databases)
        │   ├── common/            # Reusable widgets, services, or utilities used across features
        │   ├── core/              # Core application logic, dependencies, routing, etc.
        │   └── main.dart
        ```
  - **GitHub Integration:**
      - **Detail:** If using `gh` (GitHub CLI) for repository management, ensure all operations comply with internal security protocols.
      - **Adherence:** Adhere to the `GitHub-CLI-Permission-rules.md` document, which mandates explicit user permission before executing any command that could alter a repository or expose sensitive data.

-----

### 3\. Code Quality & Style

  - **Linting & Analysis:** All code must pass `flutter analyze` with zero warnings or errors.
      - **Detail:** Linting enforces a consistent coding style and identifies potential bugs or code smells early in the development cycle, leading to more robust and maintainable codebases.
      - **Configuration:** A `analysis_options.yaml` file with strict linting rules must be included in the project root. We will use the `flutter_lints` package as a baseline and customize rules as needed to enforce project-specific conventions.
      - **Command:** Run `flutter analyze` locally or as part of the CI/CD pipeline to validate code quality.
  - **Code Style:** All code must strictly follow the official Dart style guide.
      - **Detail:** Consistent formatting and style improve code readability, making it easier for multiple developers to work on the same codebase.
      - **Enforcement:** The `dart format .` command must be run before every commit. This ensures all code is automatically formatted, eliminating the need for manual style checks.
  - **Automation with Hooks:**
      - **Detail:** For robust enforcement, consider using a **pre-commit hook** with a tool like `husky` or `lint-staged`. This ensures that `dart format` and `flutter analyze` are run automatically on all staged files before a commit is even created.
  - **Naming Conventions:** Use `lower_case_with_underscores` for file names and `PascalCase` for class names, as per the Dart style guide.
      - **Detail:** Adhering to these conventions improves code discoverability and consistency across the entire project.
      - **Examples:**
          * File: `user_profile_screen.dart`
          * Class: `UserProfileScreen`
          * Function/Variable: `fetchUserData`, `isLoggedIn`

-----

### 4\. Dependencies

  - **Package Management:** Utilize community-supported Dart and Flutter packages from `pub.dev` to leverage existing solutions and accelerate development.
      - **Detail:** Before adding a dependency, evaluate its community health, documentation, and maintenance status. Prioritize packages from reputable authors or the Flutter team. Prefer pure **Dart packages**, which are platform-agnostic, over Flutter-only packages when possible. Platform support checks are primarily for Flutter-specific packages that may contain platform-specific code or use plugins that interact with the native OS.
  - **Platform Support:** Verify that all packages support the project's target platforms (e.g., iOS, Android, Web, Desktop) to avoid platform-specific issues and conditional code.
      - **Detail:** The "Platforms" section on the package's `pub.dev` page is the definitive source for compatibility information.
  - **Dependency Versions (Exact Pinning):** To ensure maximum build stability, all dependencies must be **exactly pinned** to a specific version in `pubspec.yaml`.
      - **Detail:** This approach, known as "exact pinning," guarantees that every machine and every build environment uses the identical package versions, eliminating the risk of a new, potentially breaking, update. It helps avoid "Dependency Hell," where a transitive dependency update on one team member's machine breaks the build for everyone else. Avoid using version constraints like `^` (compatible updates) or `any`.
      - **Example:**
        ```yaml
        dependencies:
          flutter:
            sdk: flutter
          provider: 6.0.5  # Exact version pinning
          http: 0.13.3     # Exact version pinning
        ```
  - **Dependency Audits and Security:**
      - **Detail:** Regularly audit your dependencies for known security vulnerabilities. The `pub.dev` site provides automated security warnings for packages with reported issues. Always verify the source and reputation of a package before adding it.
  - **`pubspec.lock`:** The `pubspec.lock` file **must always be committed** to the repository. This file contains the precise, resolved version of every single package in the dependency tree, including transitive dependencies. It is the single most important component for ensuring reproducible builds across all machines and CI environments.

-----

### 5\. State Management

  - **Consistent Approach:** A single state management approach must be chosen for the entire project.
      - **Detail:** This decision simplifies the codebase, reduces cognitive overhead, and makes it easier for new developers to onboard. The chosen pattern should be scalable to the project's complexity.
      - **Recommended Options:** Provider, BLoC (Business Logic Component), and Riverpod are excellent, community-vetted options.
  - **Choosing the Right Solution:**
      - **Detail:** The choice of state management depends on several factors:
          * **Project Scale:** Provider is excellent for small to medium apps. BLoC and Riverpod are often better for large, complex applications with intricate data flows.
          * **Team Familiarity:** Choose a solution the team is comfortable with to reduce the learning curve.
          * **Data Flow:** Consider the nature of your data. If data flows are complex and change frequently, a solution like Riverpod with its compile-time safety and dependency override features might be beneficial.
  - **Documentation:** The rationale for the chosen state management solution and its core usage patterns must be documented in a dedicated `ARCHITECTURE.md` file or the project's `README.md`.

-----

### 6\. Testing

  - **Comprehensive Testing:** All features must be accompanied by a robust suite of tests.
      - **Detail:** Testing is not optional. It is a mandatory step that ensures application reliability, prevents regressions, and simplifies future refactoring.
      - **Types of Tests:**
          * **Unit Tests:** Validate individual functions, methods, or business logic in isolation. For example, test a function that calculates a discount amount to ensure it returns the correct value for various inputs.
          * **Widget Tests:** Verify that UI components render correctly and behave as expected under various conditions. For example, test if a button's color changes when pressed or if a form validates input correctly.
          * **Integration Tests:** Test entire user flows and interactions across multiple screens to ensure the application works as a cohesive whole. For example, test the entire login process from the welcome screen to the home screen.
  - **Test Coverage:** Aim for a high test coverage percentage to ensure critical code paths are well-tested.
      - **Detail:** While 100% coverage is not always practical, a high percentage (e.g., **80%+**) on critical business logic is a good benchmark.
      - **Tools:** Use `flutter test --coverage` to generate coverage reports. This should be integrated into the CI/CD pipeline to track code health over time.
  - **Golden Testing:**
      - **Detail:** Golden testing involves capturing a "golden" image of a widget's rendering output. Subsequent tests compare the widget's current rendering to the golden image. This is an invaluable tool for preventing unintended visual changes and ensuring UI consistency across different Flutter versions, devices, and platforms.

-----

### 7\. CI/CD

  - **GitHub Actions:** Every project must have a GitHub Actions workflow file for Continuous Integration and Continuous Delivery.
      - **Detail:** Automating the build, test, and deployment process is critical for ensuring consistent quality and a faster release cycle.
  - **Secrets Management:**
      - **Detail:** All sensitive data, such as API keys and signing credentials, must be stored securely as encrypted secrets within GitHub Actions. They should never be hard-coded in the workflow file.
  - **Essential Steps:** The CI pipeline must run `flutter analyze`, `dart format --set-exit-if-changed .`, and `flutter test` on every pull request to enforce quality before merging.
  - **Matrix Build:** The workflow should include a matrix build to test across all supported operating systems (macOS, Windows, Linux) and a range of Flutter stable versions. This ensures cross-platform compatibility and prevents environment-specific failures.
  - **Example GitHub Actions Workflow:**
      - **Detail:** This basic workflow demonstrates how to set up a job that checks out the code, configures the environment, and runs the mandatory quality checks.
    <!-- end list -->
    ```yaml
    name: Flutter CI

    on:
      pull_request:
        branches: [ "main" ]

    jobs:
      build:
        runs-on: macos-latest # Use macos for iOS build, or matrix for all platforms

        steps:
          - uses: actions/checkout@v3
          - uses: subosito/flutter-action@v2
            with:
              flutter-version: '3.13.9' # Pin to a specific version

          - name: Get Dependencies
            run: flutter pub get

          - name: Check Code Style
            run: dart format . --set-exit-if-changed

          - name: Run Linter
            run: flutter analyze

          - name: Run Tests
            run: flutter test --coverage
    ```
  - **Adherence:** The workflow must strictly follow the rules outlined in `CI-CD-rules.md` and `GitHub-Actions-rules.md` for environment setup, secrets management, and trigger mechanisms.

-----

### 8\. Build Process

  - **Maximum Logging:** When running Flutter build commands, always use maximum logging by adding the `--verbose` flag to see detailed build process information.
      - **Usage Examples:**
          * `flutter build apk → flutter build apk --verbose`
          * `flutter build ios → flutter build ios --verbose`
          * `flutter build web → flutter build web --verbose`

-----

### 9\. General Guidelines

  - **Error Handling:** Implement a robust error handling and logging strategy.
      - **Detail:** Errors should be handled gracefully to prevent application crashes and provide meaningful feedback to users. Use a logging framework like `Sentry` or `Firebase Crashlytics` to capture and report errors for debugging and monitoring.
  - **Asset Management:** All assets (images, fonts, translations) must be organized in a clear and consistent directory structure within the `assets/` folder and declared in `pubspec.yaml`.
  - **Navigation:** For complex applications, use a declarative navigation package like `go_router` with Navigator 2.0.
      - **Detail:** A clear and well-defined navigation system simplifies deep linking, routing, and URL-based navigation, making the app more robust and easier to maintain.
  - **Security:**
      - **Sensitive Information:** **Never** store sensitive data (API keys, tokens, credentials) directly in the codebase. Use environment variables, secure storage solutions (e.g., `flutter_secure_storage`), or a backend service for secure access.
  - **Performance:**
      - **`const` Widgets:** Use `const` widgets and constructors wherever possible to optimize performance by preventing unnecessary widget rebuilds.
      - **Profiling:** Regularly profile the application in **profile mode** using **Flutter DevTools** to identify performance bottlenecks such as UI jank and memory leaks.
  - **Localization:**
      - **Detail:** For applications targeting multiple languages, use the built-in `flutter_localizations` package and the `arb` file format for managing translations. This ensures a scalable and maintainable approach to localization.
  - **Tooling:**
      - **Context7:** Use `context7` for comprehensive information about the project's tooling, including `mise`, `flutter`, `dart`, and GitHub Actions.
      - **AgentQL, Firecrawl, GitHub MCPs:** Utilize these Multi-Capability Platforms for advanced tasks such as data extraction, web scraping, or GitHub API interactions when necessary.
  - **Adherence to General Rules:** The team is expected to adhere to all general rule documents, including `AI-Agent-rules.md`, `AI-Tools-rules.md`, and `Shell-Execution-rules.md`, to ensure a unified and secure development environment.

  - **Sensitive Information:** **Never** store sensitive data (API keys, tokens, credentials) directly in the codebase. Use environment variables, secure storage solutions (e.g., `flutter_secure_storage`), or a backend service for secure access.

-----

### 10\. Debugging Flutter Apps

A systematic approach to debugging is essential for productivity:

1.  **Environment Check (`flutter doctor`):** Always begin by running `flutter doctor` to ensure the development environment is correctly set up. This command is a powerful first line of defense against many common setup and configuration issues.
2.  **Real-time Logs (`flutter logs`):** Use `flutter logs` to view the live log stream from a running application. This provides a crucial window into your app's runtime behavior, including `print` statements, errors, and framework messages.
3.  **IDE Debugger:** Leverage the full power of your IDE's integrated debugger to set breakpoints, inspect variables, step through code execution, and analyze the call stack. This is the most effective way to pinpoint the exact location and cause of a bug.

-----

### 11\. Dependency Management

Effective dependency management is a cornerstone of a healthy Flutter project:

1.  **`pubspec.yaml`:** All project dependencies, assets, and metadata must be explicitly declared in the `pubspec.yaml` file. This file serves as the project's manifest, and its integrity is vital for a stable build.
      * **Example:**
    <!-- end list -->
    ```yaml
    name: my_app
    description: A new Flutter project.
    version: 1.0.0+1

    environment:
        sdk: 3.8.2

    dependencies:
        flutter:
            sdk: flutter
        cupertino_icons: 1.0.2
        provider: 6.0.5

    dev_dependencies:
        flutter_test:
            sdk: flutter
        flutter_lints: 2.0.0

    flutter:
        uses-material-design: true
        assets:
            - assets/images/
            - assets/icons/
    ```
2.  **Get Dependencies (`flutter pub get`):** After modifying `pubspec.yaml` (e.g., adding or updating a dependency), always run `flutter pub get`. This command fetches and resolves all dependencies, creating or updating the `pubspec.lock` file to reflect the exact dependency tree.
3.  **Upgrade Dependencies (`flutter pub upgrade`):** While we use exact pinning, this command is still useful for a one-time, manual update of your dependencies. It will update packages to the highest allowed version **within their constraints**.
4.  **Clean Project (`flutter clean`):** When encountering build-related issues, especially after a Flutter SDK or dependency change, `flutter clean` is the first command to run. It removes the `build/` and `.dart_tool/` directories, forcing Flutter to rebuild the project from scratch. This resolves a wide range of problems caused by corrupted caches or temporary files.
      * **Detail:** `flutter clean` is a reset button for your build environment. It ensures that the next build process starts with a clean slate, using the exact dependencies specified in your `pubspec.yaml` and `pubspec.lock` files.

-----

### 12\. Documentation and Knowledge Sharing

Clear and comprehensive documentation is a mandatory component of a healthy project. It reduces friction for new team members and ensures that architectural decisions and project conventions are not lost.

  * **`README.md`:** This is the project's primary entry point. It must include:
      * A clear overview of the project's purpose.
      * Comprehensive setup instructions (including `mise` setup).
      * Key development commands (e.g., `flutter run`, `flutter test`).
      * Links to other relevant documents.
  * **`ARCHITECTURE.md`:** This file is for documenting significant technical decisions. It should explain:
      * The rationale behind the chosen state management solution.
      * The navigation strategy (e.g., `go_router` setup).
      * Major design patterns or architectural choices (e.g., repository pattern, clean architecture).
  * **Code Comments:** Use Dart's built-in documentation comments (`///`) to explain the purpose, parameters, and return values of public classes, methods, and functions. This allows IDEs and tools to provide helpful documentation on hover.
  * **Open Source Contribution Guidelines:** If the project is open source, include a `CONTRIBUTING.md` file to guide external contributors on how to submit issues and pull requests, and to ensure adherence to the project's rules.
