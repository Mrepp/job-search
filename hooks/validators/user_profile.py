"""
Validator for user profile files (self/user.json).
"""
from __future__ import annotations

import json
import re
from typing import Any

from .common import load_schema, read_json_file, is_valid_iso_date


def validate_user_profile(file_path: str) -> list[str]:
    """
    Validate a user profile JSON file.

    Args:
        file_path: Path to the user.json file

    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []

    try:
        data = read_json_file(file_path)
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"]
    except FileNotFoundError:
        return [f"File not found: {file_path}"]

    # Load schema for reference (using it for validation rules)
    try:
        schema = load_schema("user-profile.schema.json")
    except Exception:
        # If schema can't be loaded, do basic validation
        schema = None

    # Required fields
    required_fields = ["name", "email", "skills", "target_titles"]
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: '{field}'")
        elif data[field] is None:
            errors.append(f"Required field '{field}' cannot be null")
        elif isinstance(data[field], str) and not data[field].strip():
            errors.append(f"Required field '{field}' cannot be empty or whitespace")

    # Validate email format if present
    # Pattern requires: alphanumeric/special chars, @, domain, TLD (2+ chars)
    if "email" in data and data["email"]:
        email = data["email"]
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_pattern, email):
            errors.append(f"Invalid email format: '{email}'")

    # Validate remote_preference enum
    valid_remote_prefs = ["remote", "hybrid", "onsite", "flexible"]
    if "remote_preference" in data:
        pref = data["remote_preference"]
        if pref and pref not in valid_remote_prefs:
            errors.append(
                f"Invalid remote_preference: '{pref}'. "
                f"Must be one of: {', '.join(valid_remote_prefs)}"
            )

    # Validate experience_years
    if "experience_years" in data:
        years = data["experience_years"]
        if years is not None and (not isinstance(years, (int, float)) or years < 0):
            errors.append(
                f"Invalid experience_years: '{years}'. Must be a non-negative number"
            )

    # Validate skills array
    if "skills" in data:
        skills = data["skills"]
        if not isinstance(skills, list):
            errors.append("'skills' must be an array")
        elif len(skills) == 0:
            errors.append("'skills' array cannot be empty")
        else:
            for i, skill in enumerate(skills):
                skill_errors = _validate_skill(skill, i)
                errors.extend(skill_errors)

    # Validate target_titles array
    if "target_titles" in data:
        titles = data["target_titles"]
        if not isinstance(titles, list):
            errors.append("'target_titles' must be an array")
        elif len(titles) == 0:
            errors.append("'target_titles' array cannot be empty")
        else:
            for i, title in enumerate(titles):
                if not isinstance(title, str) or not title.strip():
                    errors.append(f"target_titles[{i}]: must be a non-empty string")

    # Validate salary_expectations
    if "salary_expectations" in data and data["salary_expectations"]:
        salary_errors = _validate_salary_expectations(data["salary_expectations"])
        errors.extend(salary_errors)

    # Validate last_updated format (ISO 8601)
    if "last_updated" in data and data["last_updated"]:
        last_updated = data["last_updated"]
        if not is_valid_iso_date(last_updated):
            errors.append(
                f"Invalid last_updated format: '{last_updated}'. "
                "Use ISO 8601 format (e.g., '2024-01-15T10:30:00Z')"
            )

    return errors


def _validate_skill(skill: Any, index: int) -> list[str]:
    """Validate a single skill object."""
    errors = []
    prefix = f"skills[{index}]"

    if not isinstance(skill, dict):
        return [f"{prefix}: must be an object with 'name' and 'confidence' fields"]

    # Required fields
    if "name" not in skill:
        errors.append(f"{prefix}: missing required field 'name'")
    elif not isinstance(skill["name"], str) or not skill["name"].strip():
        errors.append(f"{prefix}.name: must be a non-empty string")

    if "confidence" not in skill:
        errors.append(f"{prefix}: missing required field 'confidence'")
    else:
        confidence = skill["confidence"]
        if confidence not in [1, 2, 3]:
            errors.append(
                f"{prefix}.confidence: '{confidence}' is invalid. "
                "Must be 1 (Basic), 2 (Proficient), or 3 (Expert)"
            )

    # Optional years field
    if "years" in skill:
        years = skill["years"]
        if years is not None and (not isinstance(years, (int, float)) or years < 0):
            errors.append(f"{prefix}.years: must be a non-negative number")

    return errors


def _validate_salary_expectations(salary: Any) -> list[str]:
    """Validate salary_expectations object."""
    errors = []

    if not isinstance(salary, dict):
        return ["salary_expectations: must be an object"]

    # Validate minimum
    if "minimum" in salary and salary["minimum"] is not None:
        min_val = salary["minimum"]
        if not isinstance(min_val, (int, float)) or min_val < 0:
            errors.append("salary_expectations.minimum: must be a non-negative number")

    # Validate target
    if "target" in salary and salary["target"] is not None:
        target_val = salary["target"]
        if not isinstance(target_val, (int, float)) or target_val < 0:
            errors.append("salary_expectations.target: must be a non-negative number")

    # Check that target >= minimum if both present
    if (
        "minimum" in salary
        and "target" in salary
        and isinstance(salary.get("minimum"), (int, float))
        and isinstance(salary.get("target"), (int, float))
    ):
        if salary["target"] < salary["minimum"]:
            errors.append(
                "salary_expectations: target salary cannot be less than minimum"
            )

    return errors


def _is_valid_iso_date(date_str: str) -> bool:
    """Check if a string is a valid ISO 8601 date/datetime."""
    # Accept various ISO 8601 formats
    patterns = [
        r"^\d{4}-\d{2}-\d{2}$",  # YYYY-MM-DD
        r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$",  # YYYY-MM-DDTHH:MM:SS
        r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$",  # YYYY-MM-DDTHH:MM:SSZ
        r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$",  # With timezone
    ]
    return any(re.match(pattern, date_str) for pattern in patterns)
