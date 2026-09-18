"""Command line interface for workflow red-team scenarios."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .report import render_text
from .runner import run_suite


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run autonomous workflow red-team scenarios.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    run = subparsers.add_parser("run", help="Run a scenario suite JSON file.")
    run.add_argument("path", type=Path)
    run.add_argument("--format", choices=("text", "json"), default="text")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "run":
        payload = json.loads(args.path.read_text(encoding="utf-8"))
        result = run_suite(payload)
        if args.format == "json":
            print(json.dumps(result.to_dict(), indent=2))
        else:
            print(render_text(result))
        return 0 if result.status == "pass" else 1
    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
