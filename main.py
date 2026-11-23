"""Make the AI Judge Laugh: Office Jokes -- make.fun entry.

Writes one one-line joke about office life to /output/entry.txt,
the file the competition's gate scorer reads.
"""

from pathlib import Path

JOKE = "The boss said we're a family, so I asked HR about my inheritance."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Exactly one line, UTF-8, no trailing newline.
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
