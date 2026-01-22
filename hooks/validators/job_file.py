"""
Validator for job posting markdown files (jobs/{status}/*.md).
"""
from __future__ import annotations

import re

from .common import (
    read_file,
    extract_markdown_sections,
    find_h1_title,
    validate_score_range,
)


# Valid job statuses (directory names)
VALID_STATUSES = ["interested", "applied", "interviewed", "offered", "rejected"]

# Required sections for job files
REQUIRED_SECTIONS = [
    "## Overview",
    "## Profile Match Analysis",
    "## Requirements",
    "## Status History",
]

# Score breakdown for job match
SCORE_BREAKDOWN = {
    "Title Match": 20,
    "Location": 20,
    "Skills": 30,
    "Experience": 15,
    "Salary": 15,
}


def validate_job_file(file_path: str) -> list[str]:
    """
    Validate a job posting markdown file.

    Args:
        file_path: Path to the job markdown file

    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []

    try:
        content = read_file(file_path)
    except FileNotFoundError:
        return [f"File not found: {file_path}"]

    # Extract sections
    sections = extract_markdown_sections(content)

    # Validate file is in correct status directory
    status_errors = _validate_status_directory(file_path)
    errors.extend(status_errors)

    # Check for H1 title (should be "Title at Company")
    title = find_h1_title(content)
    if not title:
        errors.append(
            "Missing H1 title. Format should be: # Job Title at Company Name"
        )
    elif " at " not in title:
        errors.append(
            f"H1 title '{title}' should follow format: # Job Title at Company Name"
        )

    # Check required sections
    for section in REQUIRED_SECTIONS:
        section_found = any(
            key.startswith(section) or key == section for key in sections.keys()
        )
        if not section_found:
            errors.append(f"Missing required section: '{section}'")

    # Validate Overview section
    overview_key = _find_section_key(sections, "## Overview")
    if overview_key:
        overview_content = sections[overview_key]
        overview_errors = _validate_overview_section(overview_content)
        errors.extend(overview_errors)

    # Validate Profile Match Analysis
    match_errors = _validate_match_analysis(content, sections)
    errors.extend(match_errors)

    # Validate Status History
    history_key = _find_section_key(sections, "## Status History")
    if history_key:
        history_content = sections[history_key]
        history_errors = _validate_status_history(history_content)
        errors.extend(history_errors)

    return errors


def _find_section_key(sections: dict[str, str], prefix: str) -> str | None:
    """Find a section key that starts with the given prefix."""
    for key in sections.keys():
        if key.startswith(prefix) or key == prefix:
            return key
    return None


def _validate_status_directory(file_path: str) -> list[str]:
    """Validate the file is in a valid status directory."""
    errors = []
    normalized = file_path.replace("\\", "/")

    # Extract status from path
    status_found = None
    for status in VALID_STATUSES:
        if f"/jobs/{status}/" in normalized:
            status_found = status
            break

    if not status_found:
        valid_dirs = ", ".join(f"jobs/{s}/" for s in VALID_STATUSES)
        errors.append(
            f"Job file must be in a valid status directory. "
            f"Valid directories: {valid_dirs}"
        )

    return errors


def _validate_overview_section(content: str) -> list[str]:
    """Validate the Overview section has required fields."""
    errors = []

    # Minimum required fields
    required_fields = ["Location", "Type"]

    for field in required_fields:
        patterns = [
            rf"\*\*{field}:\*\*",
            rf"-\s*\*\*{field}:\*\*",
            rf"\|\s*{field}\s*\|",
        ]
        found = any(re.search(p, content, re.IGNORECASE) for p in patterns)
        if not found:
            errors.append(
                f"Overview section missing field: '{field}'. "
                f"Add: **{field}:** <value>"
            )

    return errors


def _validate_match_analysis(content: str, sections: dict[str, str]) -> list[str]:
    """Validate the Profile Match Analysis section."""
    errors = []

    match_key = _find_section_key(sections, "## Profile Match Analysis")
    if not match_key:
        return errors  # Already caught in required sections check

    match_content = sections[match_key]

    # Look for Match Score
    score_pattern = r"Match Score:\s*(\d+)(?:/100)?"
    score_match = re.search(score_pattern, match_content, re.IGNORECASE)

    if not score_match:
        errors.append(
            "Profile Match Analysis missing Match Score. "
            "Add: **Match Score:** XX/100"
        )
    else:
        total_score = int(score_match.group(1))
        if not validate_score_range(total_score, 0, 100):
            errors.append(
                f"Match Score {total_score} is out of range (must be 0-100)"
            )

        # Validate breakdown if present
        breakdown_errors = _validate_match_breakdown(match_content, total_score)
        errors.extend(breakdown_errors)

    return errors


def _validate_match_breakdown(content: str, total_score: int) -> list[str]:
    """Validate the match score breakdown table."""
    errors = []

    category_scores = {}

    for category, max_points in SCORE_BREAKDOWN.items():
        # Look for pattern like "| Title Match | 18/20 |" or "| Title Match | 18 |"
        pattern = rf"\|\s*{re.escape(category)}\s*\|\s*(\d+)(?:/\d+)?\s*\|"
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            score = int(match.group(1))
            category_scores[category] = score

            # Validate individual category max
            if score > max_points:
                errors.append(
                    f"Score breakdown: '{category}' score {score} exceeds "
                    f"maximum of {max_points}"
                )

    # Check if breakdown sums to total (if we have the full breakdown)
    if len(category_scores) == len(SCORE_BREAKDOWN):
        breakdown_sum = sum(category_scores.values())
        # Allow 2-point variance for rounding in individual category scores
        tolerance = 2
        if abs(breakdown_sum - total_score) > tolerance:
            errors.append(
                f"Score breakdown sum ({breakdown_sum}) does not match "
                f"total score ({total_score})"
            )

    return errors


def _validate_status_history(content: str) -> list[str]:
    """Validate the Status History section format."""
    errors = []

    if not content.strip():
        errors.append(
            "Status History section is empty. "
            "Add at least one entry: - **YYYY-MM-DD**: Status - Notes"
        )
        return errors

    # Look for at least one status entry
    entry_pattern = r"-\s*\*\*\d{4}-\d{2}-\d{2}\*\*:"
    entries = re.findall(entry_pattern, content)

    if not entries:
        errors.append(
            "Status History has no valid entries. "
            "Format: - **2024-01-15**: Interested - Initial discovery"
        )

    return errors
