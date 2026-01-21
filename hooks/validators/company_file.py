"""
Validator for company research markdown files (companies/*.md).
"""
from __future__ import annotations

import re

from .common import (
    read_file,
    extract_markdown_sections,
    find_h1_title,
    extract_score_from_heading,
    extract_table_values,
    validate_score_range,
    format_suggestion,
)


# Required sections for company files
REQUIRED_SECTIONS = [
    "## Overview",
    "## Company Description",
    "## Culture Analysis",
]

# Required fields in Overview section
OVERVIEW_REQUIRED_FIELDS = ["Industry", "Size", "Location"]

# Score breakdown categories
SCORE_CATEGORIES = ["Location Match", "Industry Match", "Skills Match", "Culture Match"]
CATEGORY_MAX_POINTS = 25


def validate_company_file(file_path: str) -> list[str]:
    """
    Validate a company research markdown file.

    Args:
        file_path: Path to the company markdown file

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

    # Check for H1 title
    title = find_h1_title(content)
    if not title:
        errors.append(
            "Missing H1 title (company name). "
            + format_suggestion("# Company Name", "# Stripe")
        )

    # Check required sections
    for section in REQUIRED_SECTIONS:
        section_found = any(
            key.startswith(section) or key == section for key in sections.keys()
        )
        if not section_found:
            errors.append(f"Missing required section: '{section}'")

    # Check Overview section fields
    overview_key = _find_section_key(sections, "## Overview")
    if overview_key:
        overview_content = sections[overview_key]
        overview_errors = _validate_overview_section(overview_content)
        errors.extend(overview_errors)

    # Check Relevance Score section
    score_errors = _validate_relevance_score(content, sections)
    errors.extend(score_errors)

    # Check Research Date
    date_errors = _validate_research_date(content, sections)
    errors.extend(date_errors)

    return errors


def _find_section_key(sections: dict[str, str], prefix: str) -> str | None:
    """Find a section key that starts with the given prefix."""
    for key in sections.keys():
        if key.startswith(prefix) or key == prefix:
            return key
    return None


def _validate_overview_section(content: str) -> list[str]:
    """Validate the Overview section has required fields."""
    errors = []

    for field in OVERVIEW_REQUIRED_FIELDS:
        # Look for field patterns like "**Industry:** Tech" or "- **Industry:** Tech"
        patterns = [
            rf"\*\*{field}:\*\*",
            rf"-\s*\*\*{field}:\*\*",
            rf"\|\s*{field}\s*\|",
        ]
        found = any(re.search(p, content, re.IGNORECASE) for p in patterns)
        if not found:
            errors.append(
                f"Overview section missing required field: '{field}'. "
                f"Add: **{field}:** <value>"
            )

    return errors


def _validate_relevance_score(content: str, sections: dict[str, str]) -> list[str]:
    """Validate the Relevance Score section."""
    errors = []

    # Find relevance score heading
    score_pattern = r"^## Relevance Score:\s*(\d+)/100"
    score_match = re.search(score_pattern, content, re.MULTILINE)

    if not score_match:
        errors.append(
            "Missing Relevance Score section. "
            + format_suggestion(
                "## Relevance Score: XX/100",
                "## Relevance Score: 85/100\n\n"
                "| Category | Score | Notes |\n"
                "|----------|-------|-------|\n"
                "| Location Match | 20/25 | ... |\n"
                "| Industry Match | 25/25 | ... |\n"
                "| Skills Match | 20/25 | ... |\n"
                "| Culture Match | 20/25 | ... |",
            )
        )
        return errors

    # Extract and validate score
    total_score = int(score_match.group(1))
    if not validate_score_range(total_score, 0, 100):
        errors.append(f"Relevance Score {total_score} is out of range (must be 0-100)")

    # Find the score section content
    score_section_key = _find_section_key(sections, "## Relevance Score")
    if score_section_key:
        score_content = sections[score_section_key]
        breakdown_errors = _validate_score_breakdown(score_content, total_score)
        errors.extend(breakdown_errors)

    return errors


def _validate_score_breakdown(content: str, total_score: int) -> list[str]:
    """Validate the score breakdown table sums correctly."""
    errors = []

    # Extract scores from table
    category_scores = {}

    for category in SCORE_CATEGORIES:
        # Look for pattern like "| Location Match | 20/25 |" or "| Location Match | 20 |"
        pattern = rf"\|\s*{re.escape(category)}\s*\|\s*(\d+)(?:/\d+)?\s*\|"
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            category_scores[category] = int(match.group(1))

    # Check if we found any scores
    if not category_scores:
        # No breakdown table found - this is acceptable if just the total is present
        return errors

    # Validate individual category scores
    for category, score in category_scores.items():
        if score < 0 or score > CATEGORY_MAX_POINTS:
            errors.append(
                f"Score breakdown: '{category}' score {score} is out of range "
                f"(must be 0-{CATEGORY_MAX_POINTS})"
            )

    # Check if breakdown sums to total (with tolerance)
    if len(category_scores) == len(SCORE_CATEGORIES):
        breakdown_sum = sum(category_scores.values())
        tolerance = 2  # Allow small rounding differences
        if abs(breakdown_sum - total_score) > tolerance:
            errors.append(
                f"Score breakdown sum ({breakdown_sum}) does not match "
                f"total score ({total_score}). Difference: {abs(breakdown_sum - total_score)}"
            )

    return errors


def _validate_research_date(content: str, sections: dict[str, str]) -> list[str]:
    """Validate the Research Date section."""
    errors = []

    # Look for Research Date section or inline date
    date_section = _find_section_key(sections, "## Research Date")

    if not date_section:
        # Also accept inline format
        date_patterns = [
            r"Research Date:\s*\d{4}-\d{2}-\d{2}",
            r"\*\*Research Date:\*\*\s*\d{4}-\d{2}-\d{2}",
        ]
        found = any(re.search(p, content, re.IGNORECASE) for p in date_patterns)

        if not found:
            errors.append(
                "Missing Research Date. Add either:\n"
                "- A '## Research Date' section with ISO date (YYYY-MM-DD)\n"
                "- Or inline: **Research Date:** 2024-01-15"
            )
        return errors

    # Validate date format in section
    section_content = sections[date_section]
    date_match = re.search(r"\d{4}-\d{2}-\d{2}", section_content)
    if not date_match:
        errors.append(
            "Research Date section must contain a date in ISO format (YYYY-MM-DD)"
        )

    return errors
