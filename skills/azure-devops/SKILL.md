---
name: azure-devops
description: Azure DevOps pipeline security, YAML structure, variable management, and deployment patterns
---

## Azure DevOps Pipelines Code Review Rules

### Security
- Use service connections with minimal permissions
- Store secrets in Variable Groups linked to Key Vault
- Use secure files for certificates/keys
- Enable branch policies for protected branches
- Require approvals for production environments
- Scan pipeline YAML for hardcoded secrets/credentials
- Review inline scripts for security vulnerabilities
- Avoid echoing secrets in script output
- Use credential scanning tools in PR validation

### Variables
- Use Variable Groups for shared configuration
- Mark sensitive variables as secret (masked in logs)
- Use template expressions `${{ }}` for compile-time, `$()` for runtime
- Don't hardcode environment-specific values
- Follow naming conventions: use camelCase or UPPER_SNAKE_CASE
- Name Variable Groups clearly (e.g., `prod-app-config`)
- Understand variable override precedence (job > stage > root > variable group)
- Document variable purpose in Variable Group descriptions

### Task Management
- Pin task versions (`task@2` not `task`)
- Use built-in tasks over script when available
- Set `continueOnError` only when intentional
- Use `condition` for conditional execution
- Explicitly specify agent pool (`pool: vmImage` or `pool: name`)
- Review custom scripts for embedded secrets or insecure code
- Avoid inline scripts for complex logic (use script files)
- Set task timeouts to prevent hanging jobs

### Stages and Jobs
- Use stages for environment progression (dev -> staging -> prod)
- Use deployment jobs for environment deployments
- Define explicit `dependsOn` for job ordering
- Use parallel jobs where independent
- Follow naming conventions: use descriptive stage/job names
- Set resource limits (`pool.demands`) when needed
- Configure concurrency limits for deployment jobs
- Use meaningful `displayName` for stages and jobs

### Environments
- Create environments for each deployment target
- Configure approvals and checks on environments
- Use environment variables for environment-specific config
- Track deployments in environment history

### Templates
- Extract reusable steps into templates
- Use parameters for template customization
- Store templates in a shared repository
- Version template references
- Document template purpose and parameters
- Validate template compatibility before use
- Handle template inclusion errors gracefully
- Test template changes before merging

### Best Practices
- Use `checkout: self` with `fetchDepth: 1` for faster clones
- Cache dependencies with `Cache@2` task
- Set reasonable `timeoutInMinutes`
- Use `PublishPipelineArtifact` for outputs
- Validate pipelines with Azure Pipelines schema or linters
- Test pipeline changes in feature branches before merging
- Document complex pipeline logic with comments
- Maintain pipeline documentation (README or wiki)
