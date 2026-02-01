# Code Review Skills

> **Note:** All provided skills in this repository are explicitly designed for use in code reviews.

A curated collection of agent skills for AI coding assistants. Skills provide specialized guidance for code reviews, including development best practices and infrastructure patterns.

## Installation

Install skills using the [skills.sh](https://skills.sh) CLI:

```bash
# Install a specific skill
npx skills add https://github.com/yldgio/codereview-skills --skill nextjs

# Install multiple skills
npx skills add https://github.com/yldgio/codereview-skills --skill docker --skill terraform
```

## Available Skills

### Frontend

| Skill | Description |
|-------|-------------|
| `nextjs` | Next.js App Router patterns, RSC, data fetching, and performance |
| `react` | React patterns, hooks, state management, and performance optimization |
| `angular` | Angular architecture, RxJS patterns, change detection, and best practices |
| `vercel-react-best-practices` | 57 React/Next.js performance rules from Vercel Labs |
| `vercel-composition-patterns` | React composition patterns and component design from Vercel |
| `web-design-guidelines` | UI/UX accessibility audit and design best practices from Vercel |

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

### Testing

| Skill | Description |
|-------|-------------|
| `webapp-testing` | Playwright testing patterns and E2E best practices from Anthropic |

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
git clone https://github.com/yldgio/codereview-skills.git /tmp/codereview-skills

# Copy a skill to your project
cp -r /tmp/codereview-skills/skills/docker .opencode/skills/
# or for Claude-compatible tools
cp -r /tmp/codereview-skills/skills/docker .claude/skills/
```

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:

- Development workflow and branching strategy
- Pull request process and review criteria
- Skill creation guidelines and best practices
- Branch protection rules and merge requirements

**Quick Start:**
1. Fork the repository
2. Create a branch: `git checkout -b skill/your-skill-name`
3. Follow skill format in [AGENTS.md](AGENTS.md)
4. Submit a PR with clear description
5. Address review feedback

For questions, open a GitHub Discussion or Issue.

## Weekly Skill Review Report

This repository includes a scheduled GitHub Actions workflow that generates a consolidated skill review report and opens/updates a single PR.

- Workflow: `.github/workflows/skill-review-report.yml`
- Script: `scripts/generate_skill_review_report.py`
- Schedule: weekly (Monday 09:00 UTC) + manual trigger
- Output: `reports/skill-review-report.md` in branch `skill-review-report`
- Required secret (for model calls): `GH_MODELS_TOKEN` (PAT or fine-grained token with access to GitHub Models, e.g. `models:read`)

### Progressive Disclosure Pattern

The workflow implements a **progressive disclosure pattern** to make the review process more transparent and manageable:

**During Execution:**
- Real-time progress indicators showing which skills are being processed
- Step-by-step status updates with visual icons (✅ success, ❌ errors)
- Grouped GitHub Actions logs for easy navigation
- Processing statistics and time tracking

**In Reports:**
- **Level 1 - Executive Summary**: High-level overview with key metrics
- **Level 2 - Category Overview**: Skills organized by type (Frontend, Backend, DevOps, Testing)
- **Level 3 - Detailed Reviews**: Full improvement suggestions per skill

This structure allows users to quickly grasp the overall status and drill down into relevant details only when needed.

For more details, see [PROGRESSIVE_DISCLOSURE.md](PROGRESSIVE_DISCLOSURE.md).

## License

MIT License - see [LICENSE](LICENSE) for details.
