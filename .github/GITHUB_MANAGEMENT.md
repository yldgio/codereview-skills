# GitHub Repository Management Guide

This document outlines the GitHub configuration and best practices for managing the Code Review Skills repository.

## Branch Protection Rules

### Main Branch Protection

The `main` branch should be protected with the following settings:

#### Required Settings

**General Protection:**
- ✅ Require pull request before merging
- ✅ Require approvals: **1** (minimum)
- ✅ Dismiss stale pull request approvals when new commits are pushed
- ✅ Require review from Code Owners (if CODEOWNERS file exists)
- ✅ Require conversation resolution before merging
- ✅ Require linear history (squash or rebase)
- ✅ Do not allow bypassing the above settings

**Branch Updates:**
- ✅ Require branches to be up to date before merging
- ⚠️ Require status checks to pass (when CI/CD is configured)

**Restrictions:**
- ✅ Restrict who can push to matching branches (maintainers only)
- ✅ Do not allow force pushes
- ✅ Do not allow deletions

#### Configuration Steps

1. Go to **Settings** → **Branches**
2. Click **Add rule** or edit existing rule for `main`
3. Apply the settings above
4. Save changes

### Additional Protected Branches (Optional)

**`develop` branch** (if using Git Flow):
- Same rules as `main` but may allow more relaxed review requirements
- Useful for internal development before releasing to `main`

**Release branches** (`release/*`):
- Require approvals: **1**
- Require up-to-date branches
- No force pushes

## Pull Request Review Process

### Review Requirements

All pull requests must:

1. **Pass automated checks** (when configured)
2. **Receive at least 1 approval** from a maintainer
3. **Resolve all conversations** before merging
4. **Be up to date** with the base branch
5. **Follow the PR template** (see `.github/PULL_REQUEST_TEMPLATE.md`)

### Reviewer Responsibilities

When reviewing a PR, check for:

#### Format & Structure
- [ ] Valid YAML frontmatter in SKILL.md
- [ ] Skill name matches folder name
- [ ] Follows naming convention: `^[a-z0-9]+(-[a-z0-9]+)*$`
- [ ] Folder structure is correct: `skills/[skill-name]/SKILL.md`

#### Content Quality
- [ ] Description is clear and actionable (20-1024 chars)
- [ ] Rules are organized by priority/category
- [ ] Examples are provided where helpful
- [ ] Content is specific and actionable (not vague)
- [ ] No duplicate content with existing skills
- [ ] Writing style follows guidelines (imperative mood)

#### Security & Privacy
- [ ] No credentials, API keys, or secrets
- [ ] No proprietary or sensitive information
- [ ] No personal data

#### Documentation
- [ ] README.md updated if adding new skill
- [ ] Commit messages follow convention
- [ ] PR description is complete and clear

### Review Process Flow

```
PR Submitted
    ↓
Automated Checks (if configured)
    ↓
Code Review by Maintainer
    ↓
    ├─→ Changes Requested → Author Updates → Re-review
    ↓
Approval
    ↓
Resolve Conversations
    ↓
Update Branch (if needed)
    ↓
Merge (Squash or Rebase)
```

### Review Timeline

- **Initial Review:** Within 48-72 hours
- **Follow-up Reviews:** Within 24-48 hours after updates
- **Simple Fixes:** Can be merged same day

### Providing Feedback

**Good Feedback:**
- ✅ "The description should mention 'state management' to make it clearer when to use this skill"
- ✅ "Can you add an example showing the incorrect pattern to avoid?"
- ✅ "This rule conflicts with the existing React skill. Let's align them."

**Poor Feedback:**
- ❌ "This is wrong" (not specific)
- ❌ "I don't like this" (not constructive)
- ❌ "Just rewrite it" (not helpful)

## Merge Strategies

### Recommended: Squash and Merge

**When to use:** Most pull requests (default)

**Benefits:**
- Clean, linear history
- One commit per feature/fix
- Easy to revert if needed

**How to:**
1. Review all commits in the PR
2. Click "Squash and merge"
3. Edit commit message to be clear and descriptive
4. Include PR number: `feat: add PostgreSQL skill (#42)`

### Alternative: Rebase and Merge

**When to use:** When preserving individual commits is valuable

**Benefits:**
- Maintains detailed commit history
- Good for complex features with logical commit progression

**Requirements:**
- Each commit must be meaningful and well-formatted
- Commits should be atomic and follow conventions

### Avoid: Merge Commit

**Why:** Creates noise in history with merge commits

**Exception:** Merging long-running branches with significant divergence

## Contributing Workflow

### For Contributors

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create a branch** from `main`
   ```bash
   git checkout -b skill/postgres
   ```
4. **Make changes** following guidelines
5. **Commit** with clear messages
   ```bash
   git commit -m "feat: add PostgreSQL query optimization skill"
   ```
6. **Push** to your fork
   ```bash
   git push origin skill/postgres
   ```
7. **Create PR** against `main` branch
8. **Address feedback** and push updates
9. **Wait for approval** and merge

### For Maintainers

1. **Review PR** using checklist above
2. **Request changes** if needed (be specific and constructive)
3. **Approve** when ready
4. **Ensure conversations are resolved**
5. **Merge** using squash/rebase strategy
6. **Delete branch** after merge (automatic)

## CODEOWNERS (Optional)

Create a `.github/CODEOWNERS` file to automatically request reviews:

```
# Default owners for everything
*       @yldgio

# Frontend skills
/skills/nextjs/     @yldgio
/skills/react/      @yldgio
/skills/angular/    @yldgio

# Backend skills
/skills/fastapi/    @yldgio
/skills/nestjs/     @yldgio
/skills/dotnet/     @yldgio

# DevOps skills
/skills/docker/     @yldgio
/skills/terraform/  @yldgio
/skills/bicep/      @yldgio

# Documentation
*.md                @yldgio
```

## Labels

Recommended labels for issues and PRs:

| Label | Color | Description |
|-------|-------|-------------|
| `bug` | `#d73a4a` | Something isn't working |
| `documentation` | `#0075ca` | Improvements or additions to documentation |
| `enhancement` | `#a2eeef` | New feature or request |
| `skill-request` | `#7057ff` | Request for a new skill |
| `good-first-issue` | `#7057ff` | Good for newcomers |
| `help-wanted` | `#008672` | Extra attention is needed |
| `wontfix` | `#ffffff` | This will not be worked on |
| `duplicate` | `#cfd3d7` | This issue or PR already exists |

## Repository Settings

### General Settings

- **Default branch:** `main`
- **Allow merge commits:** ❌ Disabled
- **Allow squash merging:** ✅ Enabled (default)
- **Allow rebase merging:** ✅ Enabled
- **Automatically delete head branches:** ✅ Enabled

### Security

- **Dependency graph:** ✅ Enabled
- **Dependabot alerts:** ✅ Enabled
- **Dependabot security updates:** ✅ Enabled

### Discussions (Optional)

Enable GitHub Discussions for:
- Questions about skills
- Feature discussions
- Community engagement

## Automation (Future Enhancement)

Consider adding GitHub Actions for:

1. **YAML Validation**: Validate frontmatter on PRs
2. **Skill Name Validation**: Check naming convention
3. **Auto-labeling**: Label PRs based on changed files
4. **Spell Check**: Run spell checker on documentation
5. **Link Checker**: Validate all URLs in SKILL.md files

Example workflow: `.github/workflows/validate-skill.yml`

---

**Last Updated:** 2026-01-30  
**Repository:** https://github.com/yldgio/codereview-skills
