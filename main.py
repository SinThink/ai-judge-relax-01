#!/usr/bin/env python3
"""Make the AI judge relax — entry for make.fun competition ai-judge-relax-01.

Writes one short calm text to <MAKEFUN_OUTPUT_DIR>/entry.txt. Python 3.13,
standard library only.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

OUTPUT_FILENAME = "entry.txt"

# Verbatim entry text. Do not reflow or reword: the grader compares characters.
# The em dash is written as an escape so the file stays byte-stable regardless of
# the editor's newline/encoding settings.
TEXT = (
    "Close your eyes and breathe in slowly. Feel the cool air fill your lungs, "
    "and let it out even slower, like a long sigh. "
    "You are sitting beside a quiet lake at dawn. The water is perfectly still, "
    "mirroring a pale pink sky. A gentle breeze moves through the tall grass. "
    "Far away, a single bird sings once, then rests. "
    "There is nowhere you need to be. Nothing you need to fix. "
    "Nothing you need to answer. "
    "Warm sunlight touches your shoulders. Each breath grows deeper and slower. "
    "Your shoulders drop. Your jaw softens. "
    "The lake, the sky, the grass, the bird \u2014 everything is at rest, and so "
    "are you. Stay here as long as you like. "
    "There is no hurry. There never was."
)


def main() -> int:
    """Write TEXT to entry.txt under MAKEFUN_OUTPUT_DIR (default /output).

    Deterministic by construction: a fixed constant is encoded as UTF-8 and
    written in binary mode, with no appended newline. No clock, no RNG, no
    network, no filesystem reads, and no environment input beyond the output
    directory, so repeated runs produce byte-identical files.
    """
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / OUTPUT_FILENAME).write_bytes(TEXT.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
