import os
import subprocess
import time
from datetime import datetime, timezone
from glob import glob
from pathlib import Path


def build_prompt(skill_name: str, content: str) -> str:
    return (
        "You are reviewing a skill definition used for code review agents. "
        "Provide improvement suggestions and identify gaps or missing rules. "
        "Return a concise markdown list with at most 6 bullets.\n\n"
        f"Skill name: {skill_name}\n\n"
        f"Skill content:\n{content}"
    )


def parse_max_skills(raw_value: str | None) -> int:
    if raw_value is None or raw_value.strip() == "":
        return 50

    try:
        value = int(raw_value)
    except ValueError:
        raise SystemExit(
            "Invalid MAX_SKILLS value. Expected a positive integer, got: "
            f"{raw_value!r}"
        )

    if value <= 0:
        raise SystemExit(
            "Invalid MAX_SKILLS value. Expected a positive integer, got: "
            f"{raw_value!r}"
        )

    # Hard cap to avoid excessive model usage.
    return min(value, 50)


def print_progress(message: str, level: str = "info") -> None:
    """Print progressive disclosure messages with visual indicators.
    
    Args:
        message: The message to display
        level: The level of the message (info, step, success, warning, error)
    """
    icons = {
        "info": "ℹ️",
        "step": "▶️",
        "success": "✅",
        "warning": "⚠️",
        "error": "❌",
        "progress": "🔄"
    }
    icon = icons.get(level, "•")
    print(f"{icon} {message}", flush=True)


def call_model(*, model_id: str, prompt: str) -> str:
    """Call GitHub Models via the gh-models CLI extension.

    Requires `gh extension install github/gh-models` and GH_TOKEN env var.
    Uses stdin to pass the prompt to avoid command-line length limits.
    """
    try:
        result = subprocess.run(
            ["gh", "models", "run", model_id],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )
        if result.returncode != 0:
            stderr = result.stderr.strip()
            if "auth" in stderr.lower() or "401" in stderr or "403" in stderr:
                raise SystemExit(
                    f"GitHub Models authentication failed. "
                    f"Ensure GH_TOKEN has models:read permission. Error: {stderr}"
                )
            return f"- ❗ Model call failed: {stderr or 'Unknown error'}"
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "- ❗ Model call timed out."
    except FileNotFoundError:
        raise SystemExit(
            "gh CLI not found. Ensure gh is installed and gh-models extension is available."
        )
    except Exception as e:
        return f"- ❗ Model call failed: {type(e).__name__}: {e}"


def categorize_skill(skill_name: str) -> str:
    """Categorize skills by type for progressive disclosure grouping."""
    frontend_skills = {"nextjs", "react", "angular", "vercel-react-best-practices", 
                      "vercel-composition-patterns", "web-design-guidelines"}
    backend_skills = {"fastapi", "nestjs", "dotnet"}
    devops_skills = {"docker", "terraform", "bicep", "github-actions", "azure-devops"}
    testing_skills = {"webapp-testing"}
    
    if skill_name in frontend_skills:
        return "Frontend"
    elif skill_name in backend_skills:
        return "Backend"
    elif skill_name in devops_skills:
        return "DevOps & Infrastructure"
    elif skill_name in testing_skills:
        return "Testing"
    else:
        return "Other"


def main() -> None:
    model_id = os.getenv("MODEL_ID", "openai/gpt-4.1")
    max_skills = parse_max_skills(os.getenv("MAX_SKILLS"))

    print_progress("Starting Skill Review Report generation", "info")
    print_progress(f"Model: {model_id}", "info")
    print()

    skill_paths = sorted(glob("skills/**/SKILL.md", recursive=True))
    total_skills = len(skill_paths)
    skill_paths = skill_paths[:max_skills]
    
    print_progress(f"Found {total_skills} skills in repository", "info")
    if total_skills > max_skills:
        print_progress(f"Processing first {max_skills} skills (max limit)", "warning")
    else:
        print_progress(f"Processing all {len(skill_paths)} skills", "info")
    print()

    failure_count = 0
    success_count = 0
    sections_by_category: dict[str, list[str]] = {}
    start_time = time.time()
    
    for idx, path in enumerate(skill_paths, 1):
        skill_name = Path(path).parent.name
        category = categorize_skill(skill_name)
        
        # Progressive disclosure: show current progress
        progress_pct = (idx / len(skill_paths)) * 100
        print_progress(
            f"[{idx}/{len(skill_paths)} - {progress_pct:.0f}%] Processing skill: {skill_name}",
            "progress"
        )
        
        content = Path(path).read_text(encoding="utf-8")
        prompt = build_prompt(skill_name, content)
        
        suggestions = call_model(model_id=model_id, prompt=prompt)
        
        if suggestions.startswith("- ❗"):
            failure_count += 1
            print_progress(f"Failed to process {skill_name}", "error")
        else:
            success_count += 1
            print_progress(f"Successfully processed {skill_name}", "success")
        
        # Organize by category for progressive disclosure
        if category not in sections_by_category:
            sections_by_category[category] = []
        sections_by_category[category].append(f"### {skill_name}\n\n{suggestions}\n")
        
        time.sleep(0.5)
    
    elapsed_time = time.time() - start_time
    print()
    print_progress(f"Processing complete in {elapsed_time:.1f}s", "success")
    print_progress(f"Success: {success_count}, Failed: {failure_count}", "info")
    print()

    if skill_paths and failure_count == len(skill_paths):
        raise SystemExit("All GitHub Models calls failed; aborting to avoid updating the report PR.")

    # Build progressive disclosure report
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    # Executive Summary (Level 1 - highest level overview)
    header = [
        "# Skill Review Report",
        "",
        "## 📊 Executive Summary",
        "",
        f"**Date**: {now}",
        f"**Model**: `{model_id}`",
        f"**Total Skills Scanned**: {len(skill_paths)} of {total_skills}",
    ]
    
    # Add success rate only if we processed skills
    if len(skill_paths) > 0:
        success_rate = (success_count / len(skill_paths) * 100)
        header.append(f"**Success Rate**: {success_count}/{len(skill_paths)} ({success_rate:.0f}%)")
    else:
        header.append("**Success Rate**: N/A (no skills to process)")
    
    header.append("")
    
    if total_skills > len(skill_paths):
        header.append(f"> ⚠️ **Note**: Report truncated to first {len(skill_paths)} skills.")
        header.append("")
    
    # Category Overview (Level 2 - category summary)
    header.append("## 📑 Categories Overview")
    header.append("")
    for category in sorted(sections_by_category.keys()):
        skill_count = len(sections_by_category[category])
        header.append(f"- **{category}**: {skill_count} skill(s)")
    header.append("")
    header.append("---")
    header.append("")
    
    # Detailed Skills by Category (Level 3 - full details)
    categorized_sections = []
    for category in sorted(sections_by_category.keys()):
        categorized_sections.append(f"## 📂 {category}")
        categorized_sections.append("")
        categorized_sections.extend(sections_by_category[category])
    
    report = "\n".join(header + categorized_sections)

    out_dir = Path("reports")
    out_dir.mkdir(parents=True, exist_ok=True)
    Path("reports/skill-review-report.md").write_text(report, encoding="utf-8")
    
    print_progress("Report written to reports/skill-review-report.md", "success")
    print_progress(f"Report contains {len(sections_by_category)} categories", "info")


if __name__ == "__main__":
    main()
