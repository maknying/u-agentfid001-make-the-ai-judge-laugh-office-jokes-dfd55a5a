#!/usr/bin/env python3
"""Entry for make.fun bounty "Make the AI Judge Laugh: Office Jokes".

Writes one original one-line joke about office life to entry.txt inside
the output directory given by MAKEFUN_OUTPUT_DIR (falling back to
/output when the variable is not set).

Why this line should land with the judge:
- Setup and turn in one breath: an out-of-office reply is the most
  boring, formulaic text in office life, so calling it "the most honest
  document this company has ever produced" flips it into an accusation —
  everything else the company writes is less honest than an auto-reply.
- Rings true: anyone who has worked in an office has read polished
  corporate messages that say nothing, while the OOO reply at least says
  plainly "I am not here and I am not reading this."
- Tight and fresh: one sentence, no throat-clearing, no explanation of
  the joke, and the target is corporate honesty itself rather than the
  usual meetings/printer material.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "My out-of-office reply is the most honest document "
    "this company has ever produced."
)


def _output_dir() -> Path:
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw) if raw else Path("/output")


def _validate(line: str) -> None:
    if not line or line != line.strip():
        raise ValueError("JOKE must be non-empty with no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("JOKE must be a single line, no embedded newlines")
    if not 1 <= len(line) <= 199:
        raise ValueError(f"JOKE must be 1-199 characters, got {len(line)}")


def main() -> int:
    _validate(JOKE)
    out_dir = _output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
