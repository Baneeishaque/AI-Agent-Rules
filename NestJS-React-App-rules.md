* NestJS serves React statically: After building React, copy its build folder into a public directory that NestJS can serve (e.g., using serve-static).
* Single Web Service: Deploy this unified Node.js app as a single Web Service. Eg: - Single Render Web Service
* Keep repos separate; unify at build/deploy time
* Client base URL: set it to “/” at build time
* Orchestration: Supabase → GitHub Actions → Render => Supabase as router/orchestrator, Actions as executors, Render as runtime.
* Single webhook for API, Web & App. Repos: Maintain a config map (repo → service(s), branches, environments)
