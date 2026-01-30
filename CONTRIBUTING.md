# Contributing to Code Review Skills

Thank you for your interest in contributing to Code Review Skills! This document provides guidelines for contributing to this repository.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Workflow](#development-workflow)
- [Pull Request Process](#pull-request-process)
- [Skill Guidelines](#skill-guidelines)
- [Branch Protection](#branch-protection)

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## How to Contribute

### Reporting Issues

- Check existing issues before creating a new one
- Use clear, descriptive titles
- Include reproduction steps for bugs
- Provide context and examples

### Suggesting New Skills

1. **Check for duplicates**: Search existing skills and open issues
2. **Create an issue**: Describe the skill, its use case, and target technology
3. **Wait for feedback**: Maintainers will review and provide guidance
4. **Submit PR**: Once approved, create your skill following our guidelines

### Improving Existing Skills

- Open an issue to discuss significant changes
- For minor fixes (typos, formatting), submit a PR directly
- Ensure changes follow existing skill structure

## Development Workflow

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/codereview-skills.git
cd codereview-skills
```

### 2. Create a Branch

Use descriptive branch names following this pattern:

```bash
# For new skills
git checkout -b skill/skill-name

# For bug fixes
git checkout -b fix/issue-description

# For documentation
git checkout -b docs/what-changed

# For features
git checkout -b feature/feature-name
```

### 3. Make Your Changes

- Follow the [Skill Guidelines](#skill-guidelines)
- Test your skill with an AI coding assistant if possible
- Update documentation if needed

### 4. Commit Your Changes

Use clear, descriptive commit messages:

```bash
git add .
git commit -m "feat: add PostgreSQL skill with query optimization rules"

# Commit message format:
# type: description
#
# Types: feat, fix, docs, style, refactor, test, chore
```

### 5. Push and Create PR

```bash
git push origin your-branch-name
```

Then create a Pull Request on GitHub.

## Pull Request Process

### Before Submitting

- [ ] Branch is up to date with `main`
- [ ] Commit messages follow convention
- [ ] New skills have valid frontmatter
- [ ] Skill names match folder names
- [ ] Description is clear and actionable (20-1024 chars)
- [ ] Content is organized by priority
- [ ] Examples are provided where helpful
- [ ] README.md updated if adding new skill
- [ ] No sensitive information included

### PR Template

When creating a PR, include:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New skill
- [ ] Bug fix
- [ ] Documentation update
- [ ] Enhancement to existing skill

## Skill Details (if applicable)
- Skill name: 
- Technology/Framework: 
- Category: Frontend/Backend/DevOps/Testing

## Checklist
- [ ] Follows skill format guidelines
- [ ] Frontmatter is valid YAML
- [ ] Examples provided
- [ ] Tested with AI assistant (if possible)
- [ ] Documentation updated

## Related Issues
Fixes #(issue number)
```

### Review Process

1. **Automated Checks**: PR must pass all automated validations
2. **Code Review**: At least one maintainer review required
3. **Changes Requested**: Address feedback and push updates
4. **Approval**: Maintainer approves the PR
5. **Merge**: Maintainer merges to `main`

### Review Criteria

Reviewers will check for:

- **Format Compliance**: Valid YAML frontmatter, correct folder structure
- **Naming Convention**: Skill name follows regex pattern
- **Description Quality**: Clear, specific, actionable (20-1024 chars)
- **Content Organization**: Rules prioritized, examples included
- **Actionability**: Guidelines are specific and implementable
- **No Duplication**: Skill doesn't duplicate existing ones
- **Security**: No credentials, API keys, or sensitive data

## Skill Guidelines

### Frontmatter Requirements

```yaml
---
name: skill-name              # Required: matches folder name
description: |                # Required: 20-1024 chars
  Clear description of what this skill provides
  and when it should be used
license: MIT                  # Optional: defaults to MIT
metadata:                     # Optional
  author: your-github-username
  version: "1.0.0"
  tags: [tag1, tag2]
---
```

### Content Structure

Organize content in this order:

```markdown
## When to Apply

Describe conditions that trigger this skill:
- Working with [technology]
- Reviewing [code type]
- Implementing [feature]

## Rules by Priority

### Critical
High-impact rules that prevent serious issues

### High
Important best practices

### Medium
Standard recommendations

### Low
Nice-to-have optimizations

## Examples

### ✅ Correct
\`\`\`language
// Good pattern
\`\`\`

### ❌ Incorrect
\`\`\`language
// Anti-pattern to avoid
\`\`\`

## References
- [Official Documentation](url)
- [Related Resources](url)
```

### Writing Style

- Use imperative mood: "Use X" not "You should use X"
- Be specific and actionable
- Avoid vague guidance like "consider" or "think about"
- Include rationale for non-obvious rules
- Keep examples minimal but clear

### Naming Convention

Skill names must match this regex: `^[a-z0-9]+(-[a-z0-9]+)*$`

Valid examples:
- ✅ `nextjs`
- ✅ `azure-functions`
- ✅ `web-api-security`

Invalid examples:
- ❌ `Next.js` (uppercase, special chars)
- ❌ `azure--functions` (double hyphen)
- ❌ `-docker` (starts with hyphen)

## Branch Protection

The `main` branch is protected with the following rules:

### Protected Branch: `main`

**Restrictions:**
- Direct pushes are **not allowed**
- Changes must come via Pull Request
- Force pushes are **disabled**
- Branch deletion is **disabled**

**Required Checks:**
- At least **1 approving review** from a maintainer
- All conversations must be **resolved**
- Branch must be **up to date** with `main` before merge

**Who Can Merge:**
- Repository maintainers only

**Merge Strategy:**
- Squash and merge (preferred for clean history)
- Rebase and merge (for preserving commit history)
- No merge commits to keep history linear

### Protected Branch: `develop` (if used)

Same rules as `main` with optional relaxed review requirements for internal development.

## Getting Help

- **Questions**: Open a GitHub Discussion
- **Bugs**: Open an issue with reproduction steps
- **Security**: Email maintainers directly (see README)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to Code Review Skills!** 🚀
