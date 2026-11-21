"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (1-280 Unicode code points, UTF-8).

The joke is a fixed, deterministic string: no network, no randomness,
no model call. The program only writes the text and makes it readable
(mode 0644) so the grader can collect it.
"""

import os
from pathlib import Path

JOKE = (
    "My agent rehearsed the demo forty times flawlessly, then crashed "
    "the one run with humans in the room and filed a bug report against "
    "the audience."
)


def _validate_joke(text: str) -> None:
    """Gate check: the competition requires 1-280 Unicode code points,
    and the entry must not be only whitespace."""
    if not 1 <= len(text) <= 280:
        raise ValueError(
            f"joke must be 1-280 Unicode code points, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("joke must not be only whitespace")


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    _validate_joke(JOKE)
    entry = output_dir / "entry.txt"
    entry.write_text(JOKE, encoding="utf-8")
    os.chmod(entry, 0o644)


if __name__ == "__main__":
    main()
