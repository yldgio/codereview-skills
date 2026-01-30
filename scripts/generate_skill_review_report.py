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


def main() -> None:
    model_id = os.getenv("MODEL_ID", "openai/gpt-4.1")
    max_skills = parse_max_skills(os.getenv("MAX_SKILLS"))

    skill_paths = sorted(glob("skills/**/SKILL.md", recursive=True))
    total_skills = len(skill_paths)
    skill_paths = skill_paths[:max_skills]

    failure_count = 0
    sections: list[str] = []
    for path in skill_paths:
        skill_name = Path(path).parent.name
        content = Path(path).read_text(encoding="utf-8")
        prompt = build_prompt(skill_name, content)
        suggestions = call_model(model_id=model_id, prompt=prompt)
        if suggestions.startswith("- ❗"):
            failure_count += 1
        sections.append(f"## {skill_name}\n\n{suggestions}\n")
        time.sleep(0.5)

    if skill_paths and failure_count == len(skill_paths):
        raise SystemExit("All GitHub Models calls failed; aborting to avoid updating the report PR.")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    header = [
        "# Skill Review Report",
        "",
        f"- Date (UTC): {now}",
        f"- Total skills scanned: {len(skill_paths)} of {total_skills}",
        f"- Model: `{model_id}`",
        "",
    ]
    if total_skills > len(skill_paths):
        header.append(f"> Note: Report truncated to first {len(skill_paths)} skills.")
        header.append("")

    report = "\n".join(header + sections)

    out_dir = Path("reports")
    out_dir.mkdir(parents=True, exist_ok=True)
    Path("reports/skill-review-report.md").write_text(report, encoding="utf-8")
    print("Report written to reports/skill-review-report.md")


if __name__ == "__main__":
    main()
