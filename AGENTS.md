# Agent Instructions

This repository contains reusable skills for AI coding agents. Follow these instructions when working with or contributing to this repository.

## Repository Structure

```
anomalyco/
├── README.md           # User documentation
├── AGENTS.md           # This file - agent instructions
├── LICENSE             # MIT License
└── skills/             # Skill definitions
    ├── <skill-name>/
    │   └── SKILL.md    # Skill definition file
    └── ...
```

## Skill Format

Each skill is a folder containing a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: skill-name
description: Brief description of what this skill provides (20-1024 chars)
license: MIT
metadata:
  author: yldgio
  version: "1.0.0"
---

# Skill Content

Markdown content with rules, guidelines, and examples.
```

### Frontmatter Requirements

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Lowercase alphanumeric with hyphens, must match folder name |
| `description` | Yes | Clear description for agent selection (20-1024 chars) |
| `license` | No | License identifier (default: MIT) |
| `metadata` | No | Additional key-value pairs |

### Name Validation

Skill names must:
- Be 1-64 characters
- Use lowercase alphanumeric characters
- Use single hyphens as separators (no `--`)
- Not start or end with hyphen
- Match the containing folder name

Regex: `^[a-z0-9]+(-[a-z0-9]+)*$`

## Content Guidelines

### Structure

Organize skill content by priority/impact:

1. **When to Apply** - Conditions that trigger this skill
2. **Critical Rules** - High-impact guidelines
3. **Best Practices** - Standard recommendations
4. **Examples** - Code patterns (correct and incorrect)

### Writing Style

- Use imperative mood ("Use X" not "You should use X")
- Be specific and actionable
- Include code examples where helpful
- Organize rules in tables or lists for scannability

### Example Skill Structure

```markdown
## When to Apply

Use this skill when:
- Working with [technology]
- Reviewing [type of code]
- Implementing [feature type]

## Rules by Priority

### Critical
- Rule 1: Description
- Rule 2: Description

### High
- Rule 3: Description

## Examples

### Correct
\`\`\`typescript
// Good pattern
\`\`\`

### Incorrect
\`\`\`typescript
// Anti-pattern to avoid
\`\`\`
```

## Available Skills

| Category | Skills |
|----------|--------|
| Frontend | `nextjs`, `react`, `angular` |
| Backend | `fastapi`, `nestjs`, `dotnet` |
| DevOps | `docker`, `terraform`, `bicep`, `github-actions`, `azure-devops` |

## Contributing New Skills

1. Create a folder: `skills/<skill-name>/`
2. Add `SKILL.md` with valid frontmatter
3. Ensure name matches folder name
4. Include clear description for agent discovery
5. Organize content by priority
6. Test with an AI coding agent

## Skill Discovery

Agents discover skills via the `skill` tool. The description field is critical - it determines when the agent loads this skill.

Good description:
> "React and Next.js performance optimization guidelines. Use when writing, reviewing, or refactoring React/Next.js code for optimal performance."

Bad description:
> "React stuff"

## Versioning

Use semantic versioning in metadata:
- `1.0.0` - Initial release
- `1.1.0` - New rules added
- `2.0.0` - Breaking changes to rule structure
