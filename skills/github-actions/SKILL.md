---
name: github-actions
description: GitHub Actions workflow security, performance optimization, and best practices
metadata:
  version: "1.1.0"
---

## GitHub Actions Code Review Rules

### Security (Critical)
- **Expression Safety**: Always sanitize or restrict values injected into `${{ }}` expressions. Escape or validate all user-provided data before use. Never interpolate untrusted user input
- **Variable Exposure**: Do not expose or output `${{ }}` expressions in workflow logs or error messages. Ensure all variables are declared and sourced safely
- **Secret Management**: Never echo secrets or use them in URLs as this can result in inadvertent disclosure. Always review log output and sanitize URLs to prevent leaks
- Pin actions to full commit SHA (not `@v1` or `@main`)
- Use minimal `permissions` block (principle of least privilege)
- Use `secrets.GITHUB_TOKEN` instead of PATs when possible
- Audit third-party actions before use
- Validate all inputs to reusable workflows and custom actions

### Permissions (Essential)
```yaml
permissions:
  contents: read  # Minimal by default
  # Add only what's needed:
  # pull-requests: write
  # issues: write
```

### Secrets (Essential)
- Store secrets in repository/organization secrets
- Use environments for production secrets with approvals
- Don't pass secrets as command arguments (visible in logs)
- Mask sensitive output with `::add-mask::`
- **Never write secrets to files or artifacts** (can be exposed)

### Secrets (Advanced)
- Avoid passing secrets via environment variables unless absolutely required
- Secrets in env vars can be visible in process listings

### Performance (Essential)
- Use caching for dependencies (`actions/cache` or built-in)
- Run independent jobs in parallel
- Use `concurrency` to cancel redundant runs
- Consider self-hosted runners for heavy workloads

### Workflow Structure (Essential)
- Use reusable workflows for common patterns
- Use composite actions for shared steps
- Set appropriate `timeout-minutes` to prevent hung jobs
- Use `if:` conditions to skip unnecessary jobs

### Workflow Structure (Advanced)
- Separate CI (testing), CD (deployments), and PR checks into distinct workflows
- Use environments to distinguish between dev, staging, and production
- Avoid mixing all concerns in a single monolithic workflow

### Triggers
- Be specific with `paths` and `branches` filters
- Use `workflow_dispatch` for manual triggers
- Consider `pull_request_target` security implications

### Common Anti-patterns
- Avoid `actions/checkout` with `persist-credentials: true` unless needed
- Avoid running on `push` to all branches
- Avoid hardcoding versions that need updates

### Action Updates and Maintenance
- Monitor pinned action SHAs for security fixes
- Subscribe to security advisories for actions you use
- Update actions regularly to get new features and fixes
- Document why specific SHAs are pinned (security, stability)
- Consider using Dependabot for action version updates

### Testing and Validation
- Lint workflows with tools like `actionlint`
- Test complex workflows in feature branches before merging
- Validate workflow syntax before committing
- Use workflow templates for consistency
- Add job-level tests for workflow logic validation

### Error Handling
- Use `continue-on-error: false` as default (explicit failure)
- Set `fail-fast: true` for matrix jobs to stop on first failure
- Only use `continue-on-error: true` when failure is acceptable
- Provide clear error messages in job outputs
- Use status checks to ensure critical jobs pass

### Documentation
- Add inline comments for complex workflow logic
- Document workflow purpose and triggers
- Maintain workflow README or documentation
- Explain environment variables and their usage
- Document required secret names and their purpose (never include actual secret values)
