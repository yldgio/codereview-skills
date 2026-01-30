# Skill Review Report

- Date (UTC): 2026-01-30
- Total skills scanned: 15 of 15
- Model: `openai/gpt-4.1`

## angular

- **Testing**: Add rules for unit testing components, services, and pipes, including required coverage thresholds and use of Angular Testing Utilities.
- **Accessibility**: Include checks for accessibility (a11y) compliance, such as proper use of ARIA attributes and keyboard navigation.
- **Styling**: Address best practices for component styles, e.g., preferring Angular's ViewEncapsulation, avoiding global CSS, and using SCSS or other preprocessors.
- **State Management**: Consider guidelines for state management patterns (e.g., when to use NgRx, Akita, or services for state).
- **Code Consistency & Linting**: Reference the importance of following Angular style guide and enforcing rules via linters (e.g., ESLint, Angular CLI built-in checks).
- **Performance**: Add checks for bundle size, avoiding unnecessary imports, and using lazy loading for routes and modules.

## azure-devops

```markdown
- Clarify secret management: Explicitly prohibit storing secrets directly in pipeline YAML or non-secure variables.
- Add rule for linting/validation: Recommend using tools like `yamllint` or Azure Pipelines validation to catch syntax errors early.
- Enforce naming conventions: Include guidelines for consistent naming of pipelines, variables, templates, and environments for maintainability.
- Recommend error handling: Suggest standardized error/failure notifications and logging practices.
- Address pipeline triggers: Add rules for safe configuration of triggers (`pr`, `push`, scheduled) to avoid unintended runs.
- Include code review & documentation: Require comments/documentation for complex pipeline logic; suggest peer review for pipeline changes.
```

## bicep

```markdown
- **Add Resource Tagging Rules:** Enforce tagging for cost, environment, owner, and other governance purposes.
- **Include Error Handling Guidance:** Suggest using deployment-level outputs/errors and validate parameter values to catch misconfigurations early.
- **Enforce Version Pinning:** Mandate explicit API/version specifications for resources/modules to avoid breaking changes from provider updates.
- **Document Template Readability/Structure:** Recommend organization for comments, sections, and logical ordering to improve maintainability.
- **Test and Validate Templates:** Require pre-deployment validation, linting, or test deployments (e.g., using `bicep linter` or preview mode).
- **Missing Documentation Standards:** State that all modules and resources should have meaningful descriptions and usage documentation within the template.
```

## docker

- **Add rule to minimize image layers**: Explicitly recommend minimizing total number of layers to reduce image size and complexity.
- **Clarify `USER` usage in multi-stage builds**: Specify that all runtime stages (not just build) must avoid running as root.
- **Enforce reproducible builds**: Include rule to pin package versions and avoid non-deterministic build contexts (e.g., avoid `curl`ing latest files).
- **Expand `.dockerignore` guidance**: Suggest checking for secrets, build artifacts, and git folders specifically.
- **Address environment variables**: Add rule to avoid hardcoding sensitive information in `ENV` or other instructions.
- **Include documentation expectations**: Recommend a comment header explaining the purpose of the Dockerfile and image entrypoint.

## dotnet

- **Error Handling**: Add rules for structured error responses (e.g., ProblemDetails), avoiding generic exception catches, and logging with correlation IDs.
- **Testing**: No rules for unit/integration testing—suggest enforcing test coverage, using in-memory databases, and patterns like Arrange-Act-Assert.
- **Input & Output Validation**: Missing rules for handling overposting attacks, whitelist/blacklist property binding, and response shaping.
- **API Versioning**: No guidance on organizing or versioning REST APIs (e.g., URL vs header versioning).
- **Performance**: Lacks caching (e.g., `IMemoryCache`, response caching), connection pooling, and async streaming guidelines.
- **Documentation & Comments**: Encourage XML comments for public APIs, using tools like Swagger/OpenAPI, and updating documentation with code changes.

## fastapi

```markdown
- Add rules for OpenAPI documentation: ensure endpoints/models have descriptive docstrings, and document error responses.
- Missing guidance on response content: recommend consistent response shapes (e.g., always returning JSON with a schema that includes status/data/message).
- Specify versioning best practices for endpoints (e.g., prefix routes with `/v1/`).
- No mention of CORS configuration—add rules for secure and explicit CORS policy management.
- Suggest using type hints consistently for all endpoint parameters for better validation and editor support.
- Recommend automated tests for endpoints using TestClient or similar tools, and guidance for coverage expectations.
```

## github-actions

- Add guidance to regularly update pinned action SHAs and re-audit third-party actions (to address supply chain risks).
- Include rule to validate workflow YAML syntax and consider using linting tools for reliability.
- Specify logging practices: capture essential info, avoid logging unnecessary data, and ensure logs are secure.
- Recommend use of matrix strategies for efficient multi-version or platform testing.
- Highlight need for documentation or inline comments explaining complex workflow steps for maintainability.
- Suggest monitoring and alerting integration (e.g., on workflow failures or security events) to improve visibility.

## nestjs

- Add rules for **testing**: mandate unit/e2e tests for modules, controllers, and services.
- Missing guidance on **async patterns**: suggest avoiding unhandled promises and following best practices for async methods.
- No explicit mention of **middleware**: include rules for when and how to use NestJS middleware.
- Expand on **architecture**: recommend clearly separating domain, infrastructure, and application layers for scalability.
- Add rule for **logging**: enforce consistent use of NestJS Logger and never log sensitive data.
- No coverage of **API documentation**: suggest using Swagger decorators and keeping API docs up-to-date.

## nextjs

- **Deployment & Environment**: Add rules for correct environment variable usage—no secrets in public files, use `.env.local` for sensitive data.
- **Error Handling**: Specify guidelines for graceful error boundaries (`error.tsx`), handling async errors, and fallback UI.
- **API Route Practices**: Include best practices for `/api` routes—validating requests, rate limiting, ensuring correct method usage.
- **Testing**: Recommend writing tests (unit, integration, e2e) for pages, server functions, and critical components.
- **Accessibility & SEO**: Encourage semantic HTML, proper `Head` usage, metadata management, and accessibility checks.
- **Code Structure & Maintenance**: Stress consistency in folder naming, modular code, cleaning unused files, and avoiding large monolithic components.

**Missing rules/gaps:** No guidelines for environment/deployment, error handling, API routes, testing, accessibility, or maintenance practices.

## react

- **Missing JSX & TypeScript Rules**: Add guidelines for JSX practices (e.g., avoiding logic in JSX) and TypeScript usage (e.g., typing props and state).
- **Testing Requirements Gap**: Lack of rules for component/unit testing, e.g., requiring test coverage or preferred libraries (React Testing Library).
- **Styling Consistency**: No mention of CSS-in-JS, global vs. local styles, or preventing inline style anti-patterns.
- **Error Handling Oversight**: Missing rules for handling async operations, loading/error states, and edge cases in components.
- **Context Usage**: Needs more guidance on when/how to use context, especially for performance and encapsulation.
- **Documentation & Comments**: Should require documentation for complex custom hooks/components and explain non-obvious logic.

## terraform

```markdown
- Add rules for code/plan review comments—agents should flag potential drift, destructive changes, or resource recreation risks.
- Enforce documentation standards: require README files for root and all modules, and inline comments for complex logic.
- Specify rules for dependency management—recommend explicit provider and module source/versions, warn about registry sources vs. local modules.
- Require usage of pre- and post-apply hooks or run tasks (where applicable) to check for policy violations or guardrails (e.g., via Sentinel or OPA).
- Highlight rule for handling outputs: ensure sensitive outputs are not referenced in public or shared systems, and avoid excessive output of internal resource properties.
- Missing rules for resource lifecycle: recommend proper use of `lifecycle` blocks (`prevent_destroy`, `create_before_destroy`, etc.) for critical resources.
```

## vercel-composition-patterns

```markdown
- **Add explicit do/don't guidance:** Most rules are general; include actionable "do this" and "avoid that" examples for all patterns.
- **Missing context best practices:** No rules on context value memoization, context splitting to avoid unnecessary rerenders, or context size.
- **Insufficient coverage of accessibility:** No reference to accessibility patterns (e.g., keyboard navigation and aria attributes in compound components).
- **No migration guidelines:** React 19 rule lacks migration steps for teams upgrading, especially replacing removed APIs like `forwardRef`.
- **Testing and maintainability:** Skill omits advice on how to test composed components and ensure long-term maintainability.
- **Lack of links to deeper reference:** Skill content could provide links to external guides, official React docs, and composition pattern articles for further reading.
```

## vercel-react-best-practices

- Clearly define what "better-all for partial dependencies" means in `async-dependencies` for reviewer clarity.
- Add rules and guidance specific to Next.js App Router (e.g., usage of server vs. client components, data fetching conventions, route segment config).
- Provide cross-linking or references to accessibility best practices to ensure performance optimizations don't compromise UX.
- Add a section summarizing anti-patterns to explicitly avoid (e.g., excessive client-side logic, overuse of useEffect for data fetching).
- Include version applicability (e.g., "Best suited for Next.js 13+ and React 18+") to avoid misapplication in legacy projects.
- Consider a section on automated tooling/support (e.g., recommended ESLint, webpack, or bundle analyzer plugins) for actionable integration.

## web-design-guidelines

- **Clarify Rule Application**: Specify how to handle conflicting or ambiguous rules, and what to do if a guideline cannot be applied to a particular file type.
- **Report Severity & Suggest Fixes**: Add a requirement to categorize findings by severity (e.g., error, warning, info) and, where possible, suggest actionable fixes.
- **Configurable Scope**: Include an option to narrow review scope (e.g., only accessibility or performance rules) based on user preference.
- **File Type Support**: List supported file types (e.g., HTML, CSS, JS, React components) to prevent confusion when reviewing mixed-codebases.
- **Handling Third-Party Code**: Define rule applicability for dependencies, external libraries, or minified code included in the review.
- **Limitations & Exclusions**: Explain any limitations, such as guidelines not covering certain frameworks, outdated patterns, or partial coverage (e.g., only frontend, not backend logic).

## webapp-testing

- **Add guidance for handling auth flows:** Include instructions or examples on testing login-required pages and managing cookies/session state.
- **Specify error handling:** Suggest best practices for catching and reporting Playwright exceptions during test execution.
- **Address browser variability:** Recommend testing across multiple browsers (Chromium, Firefox, WebKit) unless project-specific constraints exist.
- **Clarify teardown steps:** Emphasize cleanup actions (e.g., closing the server, deleting temp data) after test runs to avoid residue.
- **Introduce parallel/repeatable testing:** Offer strategies for parallel test execution and ensuring tests start with a clean application state.
- **Include security/browser log inspection:** Give concrete examples or rules for inspecting browser logs and handling errors/warnings observed during testing.
