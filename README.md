# Anomalyco Agent Skills

A curated collection of agent skills for AI coding assistants. Skills provide specialized knowledge for code review, development best practices, and infrastructure patterns.

## Installation

Install skills using the [skills.sh](https://skills.sh) CLI:

```bash
# Install a specific skill
npx skills add https://github.com/yldgio/anomalyco --skill nextjs

# Install multiple skills
npx skills add https://github.com/yldgio/anomalyco --skill docker --skill terraform
```

## Available Skills

### Frontend

| Skill | Description |
|-------|-------------|
| `nextjs` | Next.js App Router patterns, RSC, data fetching, and performance |
| `react` | React patterns, hooks, state management, and performance optimization |
| `angular` | Angular architecture, RxJS patterns, change detection, and best practices |

### Backend

| Skill | Description |
|-------|-------------|
| `fastapi` | FastAPI patterns, async operations, Pydantic models, and security |
| `nestjs` | NestJS architecture, decorators, modules, and TypeScript patterns |
| `dotnet` | .NET/C# patterns, async/await, Entity Framework, and API design |

### DevOps & Infrastructure

| Skill | Description |
|-------|-------------|
| `docker` | Dockerfile best practices, multi-stage builds, security, and optimization |
| `terraform` | Terraform IaC patterns, state management, modules, and security |
| `bicep` | Azure Bicep patterns, parameterization, modules, and security |
| `github-actions` | GitHub Actions workflows, reusable actions, and CI/CD patterns |
| `azure-devops` | Azure Pipelines, templates, stages, and deployment strategies |

## Usage

Once installed, skills are automatically available to your AI coding assistant. The agent will load relevant skills based on the task context.

**Example prompts:**

```
Review this Next.js component for performance issues
```

```
Help me write a secure Dockerfile for this Node.js app
```

```
Check this Terraform module for best practices
```

## Skill Structure

Each skill contains a `SKILL.md` file with:

- **Frontmatter**: Name, description, and metadata
- **Rules**: Actionable guidelines organized by category
- **Examples**: Code patterns showing correct usage

```
skills/
├── nextjs/
│   └── SKILL.md
├── docker/
│   └── SKILL.md
└── ...
```

## Manual Installation

If you prefer not to use the CLI, copy the skill folder to your project:

```bash
# Clone the repository
git clone https://github.com/yldgio/anomalyco.git /tmp/anomalyco

# Copy a skill to your project
cp -r /tmp/anomalyco/skills/docker .opencode/skills/
# or for Claude-compatible tools
cp -r /tmp/anomalyco/skills/docker .claude/skills/
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Each skill must have a `SKILL.md` with valid YAML frontmatter
2. Include `name` and `description` in frontmatter
3. Organize rules by priority/category
4. Provide concrete examples where helpful

## License

MIT License - see [LICENSE](LICENSE) for details.
