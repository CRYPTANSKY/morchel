from __future__ import annotations

import argparse
import json
from pathlib import Path

from .pipeline import run_pipeline


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the read-only MORCHEL prototype")
    parser.add_argument("observation", type=Path, help="path to a launch observation JSON file")
    args = parser.parse_args(argv)

    try:
        raw = json.loads(args.observation.read_text(encoding="utf-8"))
        result = run_pipeline(raw)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2))
    return 0

