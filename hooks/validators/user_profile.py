"""
Validator for user profile files (self/user.json).
"""
from __future__ import annotations

import json
import re
from typing import Any

from .common import read_json_file, is_valid_iso_date


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
    """Validate a single skill tree object."""
    errors = []
    prefix = f"skills[{index}]"

    if not isinstance(skill, dict):
        return [f"{prefix}: must be an object with 'name' and 'facets' fields"]

    # Required: name
    if "name" not in skill:
        errors.append(f"{prefix}: missing required field 'name'")
    elif not isinstance(skill["name"], str) or not skill["name"].strip():
        errors.append(f"{prefix}.name: must be a non-empty string")

    # Required: facets (skill tree structure)
    if "facets" not in skill:
        errors.append(f"{prefix}: missing required field 'facets'")
    else:
        facets = skill["facets"]
        if not isinstance(facets, dict):
            errors.append(f"{prefix}.facets: must be an object")
        elif len(facets) == 0:
            errors.append(f"{prefix}.facets: must have at least one facet")
        else:
            facet_errors = _validate_facets(facets, prefix)
            errors.extend(facet_errors)

    # Optional years field
    if "years" in skill:
        years = skill["years"]
        if years is not None and (not isinstance(years, (int, float)) or years < 0):
            errors.append(f"{prefix}.years: must be a non-negative number")

    # Optional last_used field (date format)
    if "last_used" in skill:
        last_used = skill["last_used"]
        if last_used is not None and not is_valid_iso_date(last_used):
            errors.append(f"{prefix}.last_used: must be a valid date (YYYY-MM-DD)")

    # Optional evidence field
    if "evidence" in skill:
        evidence_errors = _validate_evidence(skill["evidence"], prefix)
        errors.extend(evidence_errors)

    # Optional computed_score field
    if "computed_score" in skill:
        score = skill["computed_score"]
        if score is not None:
            if not isinstance(score, (int, float)) or score < 0 or score > 100:
                errors.append(f"{prefix}.computed_score: must be a number between 0 and 100")

    # Optional tags field
    if "tags" in skill:
        tags = skill["tags"]
        if not isinstance(tags, list):
            errors.append(f"{prefix}.tags: must be an array of strings")
        elif not all(isinstance(t, str) for t in tags):
            errors.append(f"{prefix}.tags: all items must be strings")

    return errors


def _validate_facets(facets: Any, prefix: str) -> list[str]:
    """Validate skill facets (sub-skills)."""
    errors = []

    if not isinstance(facets, dict):
        return [f"{prefix}.facets: must be an object"]

    for facet_name, facet in facets.items():
        facet_prefix = f"{prefix}.facets.{facet_name}"

        if not isinstance(facet, dict):
            errors.append(f"{facet_prefix}: must be an object")
            continue

        # Required: facet confidence (0-3, where 0 = none)
        if "confidence" not in facet:
            errors.append(f"{facet_prefix}: missing required field 'confidence'")
        else:
            conf = facet["confidence"]
            if conf not in [0, 1, 2, 3]:
                errors.append(
                    f"{facet_prefix}.confidence: '{conf}' is invalid. "
                    "Must be 0 (None), 1 (Basic), 2 (Proficient), or 3 (Expert)"
                )

        # Optional evidence_count
        if "evidence_count" in facet:
            count = facet["evidence_count"]
            if not isinstance(count, int) or count < 0:
                errors.append(f"{facet_prefix}.evidence_count: must be a non-negative integer")

        # Optional components array
        if "components" in facet:
            components = facet["components"]
            if not isinstance(components, list):
                errors.append(f"{facet_prefix}.components: must be an array of strings")
            elif not all(isinstance(c, str) for c in components):
                errors.append(f"{facet_prefix}.components: all items must be strings")

    return errors


def _validate_evidence(evidence: Any, prefix: str) -> list[str]:
    """Validate skill evidence array."""
    errors = []

    if not isinstance(evidence, list):
        return [f"{prefix}.evidence: must be an array"]

    valid_types = ["job", "project", "certification", "contribution", "education", "self_reported"]

    for i, item in enumerate(evidence):
        item_prefix = f"{prefix}.evidence[{i}]"

        if not isinstance(item, dict):
            errors.append(f"{item_prefix}: must be an object")
            continue

        # Validate type
        if "type" in item:
            if item["type"] not in valid_types:
                errors.append(
                    f"{item_prefix}.type: '{item['type']}' is invalid. "
                    f"Must be one of: {', '.join(valid_types)}"
                )

        # Validate description
        if "description" in item:
            if not isinstance(item["description"], str):
                errors.append(f"{item_prefix}.description: must be a string")

        # Validate weight
        if "weight" in item:
            weight = item["weight"]
            if not isinstance(weight, (int, float)) or weight < 0.1 or weight > 1.0:
                errors.append(f"{item_prefix}.weight: must be a number between 0.1 and 1.0")

        # Validate facets_demonstrated
        if "facets_demonstrated" in item:
            facets = item["facets_demonstrated"]
            if not isinstance(facets, list):
                errors.append(f"{item_prefix}.facets_demonstrated: must be an array of strings")
            elif not all(isinstance(f, str) for f in facets):
                errors.append(f"{item_prefix}.facets_demonstrated: all items must be strings")

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
