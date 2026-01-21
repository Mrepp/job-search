#!/usr/bin/env python3
"""
Main entry point for job-search plugin validation hooks.
Routes file validation to appropriate validators based on file path.
"""
import json
import sys
import os

# Add validators directory to path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from validators.user_profile import validate_user_profile
from validators.company_file import validate_company_file
from validators.job_file import validate_job_file
from validators.career_files import validate_skill_map, validate_career_tree


def block_with_reason(reason: str) -> None:
    """Output block decision and exit with code 2."""
    output = {
        "decision": "block",
        "reason": reason
    }
    print(json.dumps(output))
    sys.exit(2)


def determine_file_type(file_path: str) -> str | None:
    """
    Determine the type of file based on its path.
    Returns: 'user_profile', 'company', 'job', 'skill_map', 'career_tree', or None
    """
    # Normalize path separators
    normalized = file_path.replace("\\", "/")

    # User profile JSON
    if normalized.endswith("self/user.json"):
        return "user_profile"

    # Company research files
    if "/companies/" in normalized and normalized.endswith(".md"):
        return "company"

    # Job posting files - check for status directories
    job_statuses = ["interested", "applied", "interviewed", "offered", "rejected"]
    for status in job_statuses:
        if f"/jobs/{status}/" in normalized and normalized.endswith(".md"):
            return "job"

    # Career files
    if normalized.endswith("career/skill-map.json"):
        return "skill_map"

    if normalized.endswith("career/career-tree.json"):
        return "career_tree"

    # Not a file we validate
    return None


def main():
    """Main entry point for validation hook."""
    try:
        # Read hook input from stdin
        input_data = json.load(sys.stdin)

        # Extract file path from tool input
        tool_input = input_data.get("tool_input", {})
        file_path = tool_input.get("file_path", "")

        if not file_path:
            # No file path, nothing to validate
            sys.exit(0)

        # Check if file exists (for Edit operations, it should)
        # For Write operations, we validate the content that will be written
        file_type = determine_file_type(file_path)

        if file_type is None:
            # Not a file type we validate - pass through
            sys.exit(0)

        # Read the file content if it exists
        if not os.path.exists(file_path):
            # File doesn't exist yet - this might be a new file creation
            # We can't validate content that isn't written yet
            # The PostToolUse hook runs AFTER the write, so file should exist
            sys.exit(0)

        # Route to appropriate validator
        if file_type == "user_profile":
            errors = validate_user_profile(file_path)
        elif file_type == "company":
            errors = validate_company_file(file_path)
        elif file_type == "job":
            errors = validate_job_file(file_path)
        elif file_type == "skill_map":
            errors = validate_skill_map(file_path)
        elif file_type == "career_tree":
            errors = validate_career_tree(file_path)
        else:
            errors = []

        if errors:
            # Format errors as actionable feedback
            error_msg = "Validation failed:\n\n" + "\n".join(f"- {e}" for e in errors)
            block_with_reason(error_msg)

        # Validation passed
        sys.exit(0)

    except json.JSONDecodeError as e:
        # Invalid JSON input - don't block, just log
        print(f"Warning: Invalid JSON input to validator: {e}", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        # Unexpected error - don't block, but log
        print(f"Warning: Validation error: {e}", file=sys.stderr)
        sys.exit(0)


if __name__ == "__main__":
    main()
