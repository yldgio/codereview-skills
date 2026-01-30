# Implementation plan – Issue #3 (Scheduled pipeline to improve skills)

## Context
Issue #3 requires a scheduled pipeline that analyzes the skills in the repository and uses Copilot/LLM to propose improvements or new skills, generating output (PRs and/or issues) for the maintainers.

## Goal
Define a repeatable (weekly) implementation via GitHub Actions that:
- Scans the skills in `skills/*/SKILL.md`
- Uses an LLM to generate suggestions (improvements + gap analysis)
- Publishes results as PRs/issues, according to defined rules

## Possible solutions (options)

### Solution A – Automatic PR with consolidated report (Recommended)
- A scheduled workflow generates a markdown report with suggestions for all skills.
- The report is committed to a dedicated branch and a single PR is created via `peter-evans/create-pull-request`.
- Pros: centralized review, less noise; Cons: less per-skill granularity.

### Solution B – One issue per skill (maximum granularity)
- The scheduled workflow creates/updates an issue for each skill via `actions/github-script`.
- Pros: detailed tracking; Cons: high volume of issues.

### Solution C – One PR per skill (medium granularity)
- For each skill, the workflow creates a separate branch and PR with specific suggestions.
- Pros: smaller and more targeted PRs; Cons: risk of PR spam.

## Decisions
- Schedule frequency: weekly (confirmed).
- Preferred output: single PR with consolidated report (Solution A).
- LLM model: GitHub Models/Copilot, required API key/permissions.
- Deduplication rules: fixed branch `skill-review-report` + fixed PR title; if an open PR exists, update it instead of creating a new one.
- Limits: max 50 skills per run (truncation; override possible via `workflow_dispatch`, but the script enforces a hard cap of 50).

## Workplan

- [x] Define detailed operational requirements (frequency, output, volume limits)
- [x] Design the GitHub Actions workflow (schedule + `workflow_dispatch`)
- [x] Implement skill discovery step (`skills/*/SKILL.md`)
- [x] Implement LLM step (prompting for review + gap analysis)
- [x] Implement output:
  - [x] Single PR with consolidated report (Solution A)
  - [ ] One issue per skill (Solution B)
  - [ ] One PR per skill (Solution C)
- [x] Add controls for deduplication and rate limiting
- [x] Add documentation in README/CONTRIBUTING (process and limits)
- [ ] Manual test via `workflow_dispatch`

## Technical notes
- Workflow added in `.github/workflows/skill-review-report.yml`.
- Report generation script in `scripts/generate_skill_review_report.py`.
- Skills are in `skills/<name>/SKILL.md` with YAML frontmatter.
- To create PRs: use `peter-evans/create-pull-request`.
- To create issues: use `actions/github-script`.
- Workflow permissions: `contents: write`, `pull-requests: write`.

## Risks & mitigations
- **PR/issue spam** → deduplication via fixed PR branch/title (and consistent issue title when enabled).
- **LLM credentials** → use secrets and limit token scope.
- **LLM costs** → limit the number of skills per run or use batching.
