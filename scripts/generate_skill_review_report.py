import json
import os
import textwrap
import time
from datetime import datetime, timezone
from glob import glob
from pathlib import Path
from urllib import error, request


def build_prompt(skill_name: str, content: str) -> str:
    return textwrap.dedent(
        f"""\
        You are reviewing a skill definition used for code review agents.
        Provide improvement suggestions and identify gaps or missing rules.
        Return a concise markdown list with at most 6 bullets.
        Skill name: {skill_name}

        Skill content:
        {content}
        """
    )


def call_model(*, token: str, model_id: str, prompt: str) -> str:
    payload = {
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}],
    }

    req = request.Request(
        "https://models.github.ai/inference/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        method="POST",
    )

    try:
        with request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data["choices"][0]["message"]["content"].strip()
    except error.HTTPError as e:
        return f"- ❗ Model call failed (HTTP {e.code})."
    except Exception as e:
        return f"- ❗ Model call failed: {type(e).__name__}: {e}"


def main() -> None:
    model_id = os.getenv("MODEL_ID", "openai/gpt-4.1")
    max_skills = int(os.getenv("MAX_SKILLS", "50"))
    token = os.getenv("GH_MODELS_TOKEN") or os.getenv("GITHUB_TOKEN")

    if not token:
        raise SystemExit("Missing GH_MODELS_TOKEN or GITHUB_TOKEN.")

    skill_paths = sorted(glob("skills/**/SKILL.md", recursive=True))
    total_skills = len(skill_paths)
    skill_paths = skill_paths[:max_skills]

    sections: list[str] = []
    for path in skill_paths:
        skill_name = Path(path).parent.name
        content = Path(path).read_text(encoding="utf-8")
        suggestions = call_model(token=token, model_id=model_id, prompt=build_prompt(skill_name, content))
        sections.append(f"## {skill_name}\n\n{suggestions}\n")
        time.sleep(0.5)

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
