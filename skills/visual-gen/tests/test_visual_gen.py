import importlib.util
import re
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "visual_gen.py"
SPEC = importlib.util.spec_from_file_location("visual_gen", SCRIPT_PATH)
visual_gen = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(visual_gen)


def test_responses_images_only_503_falls_back_to_images_endpoint():
    error = visual_gen.ApiHTTPError(
        503,
        "model gpt-image-2 is only supported on /v1/images/generations and /v1/images/edits",
    )

    assert visual_gen.should_fall_back_to_images(error)


def test_lone_visual_gen_api_key_env_does_not_block_fallback(monkeypatch):
    monkeypatch.setenv("VISUAL_GEN_API_KEY", "dummy")
    monkeypatch.delenv("VISUAL_GEN_API_BASE", raising=False)
    args = type("Args", (), {"api_base": None, "api_key": None, "api_key_env": None})()

    assert visual_gen.load_direct_settings(args, {}, None, "gpt-image-2") is None


def test_lone_legacy_figforge_api_key_env_does_not_block_fallback(monkeypatch):
    monkeypatch.delenv("VISUAL_GEN_API_KEY", raising=False)
    monkeypatch.delenv("VISUAL_GEN_API_BASE", raising=False)
    monkeypatch.setenv("FIGFORGE_GEN_API_KEY", "dummy")
    monkeypatch.delenv("FIGFORGE_GEN_API_BASE", raising=False)
    args = type("Args", (), {"api_base": None, "api_key": None, "api_key_env": None})()

    assert visual_gen.load_direct_settings(args, {}, None, "gpt-image-2") is None


def test_default_output_dir_uses_unified_runtime_root(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)

    output_dir = visual_gen.resolve_output_dir(None)

    assert output_dir.parent == tmp_path / ".visual-anything" / "runs" / "gen"
    assert re.fullmatch(r"\d{8}-\d{6}", output_dir.name)


def test_relative_output_dir_is_still_resolved_from_cwd(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)

    assert visual_gen.resolve_output_dir("custom-out") == tmp_path / "custom-out"
