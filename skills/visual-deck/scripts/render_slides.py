#!/usr/bin/env python3
import argparse
import json
import re
import shlex
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path


DEFAULT_JOBS = 4
DEFAULT_SIZE = "1536x1024"
DEFAULT_QUALITY = "high"


def fail(message, status_code=1, **extra):
    payload = {"ok": False, "error": message}
    payload.update(extra)
    print(json.dumps(payload, ensure_ascii=False))
    raise SystemExit(status_code)


def now_iso():
    return datetime.now().isoformat(timespec="seconds")


def extract_field(path, field, default):
    if not path.exists():
        return default
    pattern = re.compile(rf"^\s*{re.escape(field)}:\s*([^#\n]+)", re.MULTILINE)
    match = pattern.search(path.read_text(encoding="utf-8"))
    if not match:
        return default
    return match.group(1).strip().strip("\"'")


def extract_slide_id(prompt_path):
    match = re.fullmatch(r"slide-(\d+)\.md", prompt_path.name)
    if not match:
        fail(f"Invalid prompt filename: {prompt_path.name}")
    return f"slide-{int(match.group(1)):02d}"


def extract_role(prompt_text):
    match = re.search(r"^\s*-\s*role:\s*([a-z-]+)\s*$", prompt_text, re.MULTILINE)
    return match.group(1) if match else "unknown"


def skill_root():
    return Path(__file__).resolve().parents[1]


def visual_gen_paths():
    visual_gen_dir = skill_root().parent / "visual-gen"
    return {
        "choose_python": visual_gen_dir / "scripts" / "choose_python.sh",
        "visual_gen": visual_gen_dir / "scripts" / "visual_gen.py",
    }


def choose_python(paths):
    chooser = paths["choose_python"]
    if not chooser.exists():
        fail(f"visual-gen chooser not found: {chooser}")
    proc = subprocess.run(
        ["bash", str(chooser)],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        fail("No usable Python 3.11+ found for visual-gen", stderr=proc.stderr.strip())
    return shlex.split(proc.stdout.strip())


def run_preflight(python_argv, visual_gen_script):
    proc = subprocess.run(
        [*python_argv, str(visual_gen_script), "--show-config"],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        fail(
            "visual-gen preflight failed",
            stdout=proc.stdout.strip(),
            stderr=proc.stderr.strip(),
        )


def parse_visual_gen_stdout(stdout):
    lines = [line for line in stdout.splitlines() if line.strip()]
    if not lines:
        raise RuntimeError("visual-gen returned no JSON output")
    try:
        return json.loads(lines[-1])
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"visual-gen returned invalid JSON: {exc}") from exc


def render_one(prompt_path, slides_dir, size, quality, python_argv, visual_gen_script):
    slide_id = extract_slide_id(prompt_path)
    prompt_text = prompt_path.read_text(encoding="utf-8")
    role = extract_role(prompt_text)
    final_path = slides_dir / f"{slide_id}.png"

    cmd = [
        *python_argv,
        str(visual_gen_script),
        "--mode",
        "generate",
        "--prompt",
        prompt_text,
        "--size",
        size,
        "--quality",
        quality,
        "--output-format",
        "png",
        "--out-dir",
        str(slides_dir),
        "--n",
        "1",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        return {
            "ok": False,
            "slide": slide_id,
            "role": role,
            "error": "visual-gen failed",
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
        }

    try:
        data = parse_visual_gen_stdout(proc.stdout)
    except RuntimeError as exc:
        return {"ok": False, "slide": slide_id, "role": role, "error": str(exc)}

    if not data.get("ok"):
        return {
            "ok": False,
            "slide": slide_id,
            "role": role,
            "error": data.get("error") or "visual-gen returned ok=false",
        }

    paths = data.get("paths") or []
    if not paths:
        return {"ok": False, "slide": slide_id, "role": role, "error": "visual-gen returned no paths"}

    generated = Path(paths[0])
    if not generated.is_absolute():
        generated = Path.cwd() / generated
    generated.replace(final_path)

    return {
        "ok": True,
        "slide": slide_id,
        "role": role,
        "path": str(final_path),
    }


def append_log(run_dir, results, style, jobs):
    log_path = run_dir / "revisions.log"
    with log_path.open("a", encoding="utf-8") as handle:
        for item in sorted(results, key=lambda value: value["slide"]):
            handle.write(
                f"{now_iso()} render {item['slide']} role={item.get('role', 'unknown')} "
                f"style={style} ok={str(item['ok']).lower()} mode=parallel jobs={jobs}\n"
            )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--jobs", type=int, default=DEFAULT_JOBS)
    parser.add_argument("--size")
    parser.add_argument("--quality", default=DEFAULT_QUALITY)
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    prompt_dir = run_dir / "prompts"
    slides_dir = run_dir / "slides"
    outline_path = run_dir / "outline.md"
    jobs = max(1, args.jobs)

    if not prompt_dir.exists():
        fail(f"Prompt directory not found: {prompt_dir}")

    prompt_paths = sorted(prompt_dir.glob("slide-*.md"), key=extract_slide_id)
    if not prompt_paths:
        fail(f"No slide prompts found in {prompt_dir}")

    size = args.size or extract_field(outline_path, "size", DEFAULT_SIZE)
    style = extract_field(outline_path, "style", "unknown")
    slides_dir.mkdir(parents=True, exist_ok=True)

    paths = visual_gen_paths()
    visual_gen_script = paths["visual_gen"]
    if not visual_gen_script.exists():
        fail(f"visual-gen script not found: {visual_gen_script}")
    python_argv = choose_python(paths)
    run_preflight(python_argv, visual_gen_script)

    results = []
    with ThreadPoolExecutor(max_workers=jobs) as pool:
        futures = [
            pool.submit(
                render_one,
                prompt_path,
                slides_dir,
                size,
                args.quality,
                python_argv,
                visual_gen_script,
            )
            for prompt_path in prompt_paths
        ]
        for future in as_completed(futures):
            item = future.result()
            results.append(item)
            print(
                f"[{item['slide']} ok={str(item['ok']).lower()}]",
                file=sys.stderr,
                flush=True,
            )

    append_log(run_dir, results, style, jobs)
    failures = [item for item in results if not item["ok"]]
    if failures:
        fail("One or more slides failed", failures=failures)

    rel_paths = [
        str(Path("slides") / f"{item['slide']}.png")
        for item in sorted(results, key=lambda value: value["slide"])
    ]
    summary = {
        "style": style,
        "size": size,
        "count": len(rel_paths),
        "render_mode": "parallel",
        "max_concurrency": jobs,
        "slides": rel_paths,
        "outline": "outline.md",
        "ts": now_iso(),
    }
    summary_path = run_dir / "last_run.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "paths": rel_paths, "last_run": str(summary_path)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
