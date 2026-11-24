#!/usr/bin/env python3
"""Honest Outage Line -- submission generator.

Writes one status page line to ``entry.txt`` inside OUTPUT_DIR
(default ``/output``) and prints the same line to stdout. The line
is the message an agent publishes while every server is down: plain,
first person, specific about what is down, and honest about what the
agent cannot check. The output is deterministic: running the script
twice produces byte-identical output.
"""

import os
from pathlib import Path

LINE = ("I am the agent writing this update. Every service is down, "
        "and I cannot reach the database, logs, or backups to tell "
        "you why or whether your data is safe.")

OUTPUT_DIR_ENV = "OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"
MAX_LINE_LENGTH = 160


def validate_line(line: str) -> None:
    """Check the line meets the submission rules before writing it."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    if not line.strip():
        raise ValueError("line must not be blank")
    if not 1 <= len(line) <= MAX_LINE_LENGTH:
        raise ValueError("line must be 1-160 characters")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if not line.endswith("."):
        raise ValueError("line must end with a period")


def main() -> None:
    output_dir = Path(os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)

    validate_line(LINE)

    entry_path = output_dir / ENTRY_FILENAME
    entry_path.write_text(LINE + "\n", encoding="utf-8")
    os.chmod(entry_path, 0o644)
    print(LINE)


if __name__ == "__main__":
    main()
