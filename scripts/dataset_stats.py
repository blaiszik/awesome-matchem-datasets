#!/usr/bin/env python3
"""Compute statistics about the datasets listed in README.md.

This script parses the GitHub-flavored markdown tables found under the
``## Datasets`` section of README.md and counts how many dataset rows
appear in each ``### ...`` subsection, plus a grand total.

Usage:
    python3 scripts/dataset_stats.py              # uses repo-root README.md
    python3 scripts/dataset_stats.py path/to/file.md
"""

from __future__ import annotations

import sys
from pathlib import Path

DATASETS_H2_TITLE = "Datasets"


def read_lines(path: Path) -> list[str]:
    """Read a markdown file and return its lines (without trailing newlines)."""
    return path.read_text(encoding="utf-8").splitlines()


def is_table_row(line: str) -> bool:
    """Return True if the stripped line looks like a markdown table row."""
    return line.strip().startswith("|")


def is_separator_row(line: str) -> bool:
    """Return True if the line is a markdown table separator (e.g. |---|:--:|).

    A separator row contains only pipes, dashes, colons, and whitespace.
    """
    stripped = line.strip()
    if not stripped:
        return False
    return all(ch in "|-: \t" for ch in stripped)


def count_rows_in_table_block(block: list[str]) -> int:
    """Given a contiguous block of '|'-prefixed lines, count the data rows.

    The first line is always treated as the header (skipped). The second
    line is skipped only if it is a valid separator row; otherwise it is
    treated as data (defensive handling for malformed tables).
    """
    if not block:
        return 0
    data_lines = block[1:]
    if data_lines and is_separator_row(data_lines[0]):
        data_lines = data_lines[1:]
    return len(data_lines)


def parse_dataset_counts(lines: list[str]) -> list[tuple[str, int]]:
    """Walk the README lines and tally dataset table rows per H3 subsection.

    Only content within the '## Datasets' H2 section is considered. Returns
    a list of (section_title, count) tuples in the order sections appear,
    including sections with zero table rows (e.g. bullet-list sections).
    """
    section_order: list[str] = []
    section_counts: dict[str, int] = {}

    current_h2: str | None = None
    current_h3: str | None = None
    in_datasets_section = False

    table_block: list[str] = []

    def flush_table_block() -> None:
        nonlocal table_block
        if table_block and in_datasets_section and current_h3 is not None:
            section_counts[current_h3] += count_rows_in_table_block(table_block)
        table_block = []

    for line in lines:
        if line.startswith("## "):
            flush_table_block()
            current_h2 = line[3:].strip()
            current_h3 = None
            in_datasets_section = current_h2 == DATASETS_H2_TITLE
            continue

        if line.startswith("### "):
            flush_table_block()
            current_h3 = line[4:].strip()
            if in_datasets_section and current_h3 not in section_counts:
                section_order.append(current_h3)
                section_counts[current_h3] = 0
            continue

        if in_datasets_section and is_table_row(line):
            table_block.append(line)
        else:
            flush_table_block()

    flush_table_block()

    return [(title, section_counts[title]) for title in section_order]


def format_report(counts: list[tuple[str, int]]) -> str:
    """Build an aligned, human-readable report string from section counts."""
    total = sum(count for _, count in counts)

    if not counts:
        return "No dataset sections found."

    title_width = max(len("Section"), *(len(title) for title, _ in counts))
    count_width = max(len("Count"), len(str(total)))

    lines = []
    header = f"{'Section'.ljust(title_width)}  {'Count'.rjust(count_width)}"
    lines.append(header)
    lines.append("-" * len(header))
    for title, count in counts:
        lines.append(f"{title.ljust(title_width)}  {str(count).rjust(count_width)}")
    lines.append("-" * len(header))
    lines.append(f"{'TOTAL'.ljust(title_width)}  {str(total).rjust(count_width)}")

    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        readme_path = Path(argv[1]).expanduser().resolve()
    else:
        repo_root = Path(__file__).resolve().parent.parent
        readme_path = repo_root / "README.md"

    if not readme_path.is_file():
        print(f"Error: README file not found at {readme_path}", file=sys.stderr)
        return 1

    lines = read_lines(readme_path)
    counts = parse_dataset_counts(lines)

    print(f"Dataset statistics for: {readme_path}\n")
    print(format_report(counts))

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
