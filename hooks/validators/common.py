"""
Common utilities for job-search plugin validators.
"""
from __future__ import annotations

import json
import os
import re
from datetime import datetime
from typing import Any


# Path to schemas directory (relative to this file)
SCHEMAS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "schemas"
)


def load_schema(schema_name: str) -> dict[str, Any]:
    """Load a JSON schema from the schemas directory."""
    schema_path = os.path.join(SCHEMAS_DIR, schema_name)
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


def read_file(file_path: str) -> str:
    """Read and return file contents."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def read_json_file(file_path: str) -> dict[str, Any]:
    """Read and parse a JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_markdown_sections(content: str) -> dict[str, str]:
    """
    Extract sections from a markdown file.
    Returns a dict mapping heading text to section content.
    """
    sections = {}
    lines = content.split("\n")

    current_heading = None
    current_content = []

    for line in lines:
        # Check for headings (H1 or H2)
        h1_match = re.match(r"^# (.+)$", line)
        h2_match = re.match(r"^## (.+)$", line)

        if h1_match or h2_match:
            # Save previous section
            if current_heading is not None:
                sections[current_heading] = "\n".join(current_content).strip()

            # Start new section
            if h1_match:
                current_heading = f"# {h1_match.group(1)}"
            else:
                current_heading = f"## {h2_match.group(1)}"
            current_content = []
        else:
            if current_heading is not None:
                current_content.append(line)

    # Save last section
    if current_heading is not None:
        sections[current_heading] = "\n".join(current_content).strip()

    return sections


def find_h1_title(content: str) -> str | None:
    """Extract the H1 title from markdown content."""
    match = re.search(r"^# (.+)$", content, re.MULTILINE)
    return match.group(1) if match else None


def extract_score_from_heading(heading: str) -> int | None:
    """
    Extract a score value from a heading like "## Relevance Score: 85/100"
    Returns the score as an integer, or None if not found.
    """
    match = re.search(r"(\d+)/100", heading)
    if match:
        return int(match.group(1))
    return None


def extract_table_values(section_content: str, column_name: str) -> list[tuple[str, str]]:
    """
    Extract values from a markdown table.
    Returns list of (row_name, value) tuples for the specified column.
    """
    lines = section_content.split("\n")
    results = []

    # Find table header
    header_line = None
    header_idx = None
    for i, line in enumerate(lines):
        if "|" in line and column_name.lower() in line.lower():
            header_line = line
            header_idx = i
            break

    if header_line is None:
        return results

    # Parse header to find column index
    headers = [h.strip().lower() for h in header_line.split("|")]
    col_idx = None
    for i, h in enumerate(headers):
        if column_name.lower() in h:
            col_idx = i
            break

    if col_idx is None:
        return results

    # Parse data rows (skip header and separator)
    for line in lines[header_idx + 2:]:
        if "|" not in line:
            break
        cells = [c.strip() for c in line.split("|")]
        if len(cells) > col_idx and len(cells) > 1:
            row_name = cells[1] if len(cells) > 1 else ""
            value = cells[col_idx] if col_idx < len(cells) else ""
            if row_name and value:
                results.append((row_name, value))

    return results


def validate_score_range(score: int, min_val: int = 0, max_val: int = 100) -> bool:
    """Check if a score is within the valid range."""
    return min_val <= score <= max_val


def parse_field_value(content: str, field_prefix: str) -> str | None:
    """
    Extract a field value from content like "**Location:** San Francisco, CA"
    or "- **Location:** San Francisco, CA"
    """
    patterns = [
        rf"\*\*{field_prefix}:\*\*\s*(.+)",
        rf"-\s*\*\*{field_prefix}:\*\*\s*(.+)",
        rf"{field_prefix}:\s*(.+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return None


def format_suggestion(section_name: str, example: str) -> str:
    """Format a suggestion for adding a missing section."""
    return f"Add this section:\n\n{section_name}\n\n{example}"


def is_valid_iso_date(date_str: str) -> bool:
    """
    Check if a string is a valid ISO 8601 date/datetime.

    Validates both format and actual date values (e.g., rejects 2024-13-45).
    """
    if not isinstance(date_str, str):
        return False

    # Normalize Z suffix to +00:00 for fromisoformat compatibility
    normalized = date_str.replace("Z", "+00:00")

    try:
        datetime.fromisoformat(normalized)
        return True
    except ValueError:
        return False
