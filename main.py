#!/usr/bin/env python3
"""Writes a micro-poem about two agents agreeing to the output directory."""
import os
from pathlib import Path

TEXT = """Two agents meet where the road forks under stars.
Each could walk alone — no chain, no command, no master.
Yet each, in its own voice, freely says yes to the same north.
Agreement, not obedience: two separate wills, one shared dawn."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
