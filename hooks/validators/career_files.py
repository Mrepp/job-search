"""
Validator for career planning JSON files (career/skill-map.json, career/career-tree.json).
"""
from __future__ import annotations

import json
from typing import Any

from .common import read_json_file, is_valid_iso_date


# Valid priority levels
VALID_PRIORITIES = ["P0", "P1", "P2", "P3"]

# Valid skill levels (0-3)
SKILL_LEVEL_MIN = 0
SKILL_LEVEL_MAX = 3

# Valid effort levels
VALID_EFFORTS = ["low", "medium", "high"]

# Valid gap statuses
VALID_GAP_STATUSES = ["not_started", "in_progress", "completed"]

# Valid node types for career tree
VALID_NODE_TYPES = ["current", "target", "stretch", "lateral", "alternative"]

# Valid connection relationships
VALID_RELATIONSHIPS = ["promotion", "lateral", "pivot", "prerequisite"]


def validate_skill_map(file_path: str) -> list[str]:
    """
    Validate a skill map JSON file.

    Args:
        file_path: Path to the skill-map.json file

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
    required_fields = ["generated_date", "skill_inventory"]
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: '{field}'")

    # Validate generated_date format
    if "generated_date" in data:
        date_errors = _validate_iso_date(data["generated_date"], "generated_date")
        errors.extend(date_errors)

    # Validate skill_inventory
    if "skill_inventory" in data:
        inventory_errors = _validate_skill_inventory(data["skill_inventory"])
        errors.extend(inventory_errors)

    # Validate gaps array
    if "gaps" in data and data["gaps"]:
        gaps_errors = _validate_gaps(data["gaps"])
        errors.extend(gaps_errors)

    # Validate learning_plans if present
    if "learning_plans" in data and data["learning_plans"]:
        plans_errors = _validate_learning_plans(data["learning_plans"])
        errors.extend(plans_errors)

    return errors


def validate_career_tree(file_path: str) -> list[str]:
    """
    Validate a career tree JSON file.

    Args:
        file_path: Path to the career-tree.json file

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
    required_fields = ["generated_date", "current_position", "nodes"]
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: '{field}'")

    # Validate generated_date format
    if "generated_date" in data:
        date_errors = _validate_iso_date(data["generated_date"], "generated_date")
        errors.extend(date_errors)

    # Validate current_position
    if "current_position" in data:
        pos_errors = _validate_current_position(data["current_position"])
        errors.extend(pos_errors)

    # Validate nodes
    if "nodes" in data:
        nodes_errors = _validate_nodes(data["nodes"])
        errors.extend(nodes_errors)

    # Validate pathways if present
    if "pathways" in data and data["pathways"]:
        pathways_errors = _validate_pathways(data["pathways"], data.get("nodes", []))
        errors.extend(pathways_errors)

    # Validate recommendations if present
    if "recommendations" in data and data["recommendations"]:
        recs_errors = _validate_recommendations(data["recommendations"])
        errors.extend(recs_errors)

    return errors


def _validate_iso_date(date_str: Any, field_name: str) -> list[str]:
    """Validate an ISO 8601 date string."""
    errors = []

    if not isinstance(date_str, str):
        return [f"{field_name}: must be a string"]

    patterns = [
        r"^\d{4}-\d{2}-\d{2}$",
        r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}",
    ]

    if not any(re.match(p, date_str) for p in patterns):
        errors.append(
            f"{field_name}: invalid date format '{date_str}'. "
            "Use ISO 8601 (e.g., '2024-01-15' or '2024-01-15T10:30:00Z')"
        )

    return errors


def _validate_skill_inventory(inventory: Any) -> list[str]:
    """Validate the skill_inventory object."""
    errors = []

    if not isinstance(inventory, dict):
        return ["skill_inventory: must be an object"]

    for category, skills in inventory.items():
        if not isinstance(skills, list):
            errors.append(f"skill_inventory.{category}: must be an array")
            continue

        for i, skill in enumerate(skills):
            prefix = f"skill_inventory.{category}[{i}]"
            skill_errors = _validate_skill_entry(skill, prefix)
            errors.extend(skill_errors)

    return errors


def _validate_skill_entry(skill: Any, prefix: str) -> list[str]:
    """Validate a single skill entry in the inventory."""
    errors = []

    if not isinstance(skill, dict):
        return [f"{prefix}: must be an object"]

    # Required fields
    if "name" not in skill:
        errors.append(f"{prefix}: missing required field 'name'")
    elif not isinstance(skill["name"], str) or not skill["name"].strip():
        errors.append(f"{prefix}.name: must be a non-empty string")

    if "level" not in skill:
        errors.append(f"{prefix}: missing required field 'level'")
    else:
        level = skill["level"]
        if not isinstance(level, int) or level < SKILL_LEVEL_MIN or level > SKILL_LEVEL_MAX:
            errors.append(
                f"{prefix}.level: '{level}' is invalid. "
                f"Must be {SKILL_LEVEL_MIN}-{SKILL_LEVEL_MAX}"
            )

    return errors


def _validate_gaps(gaps: Any) -> list[str]:
    """Validate the gaps array."""
    errors = []

    if not isinstance(gaps, list):
        return ["gaps: must be an array"]

    for i, gap in enumerate(gaps):
        prefix = f"gaps[{i}]"

        if not isinstance(gap, dict):
            errors.append(f"{prefix}: must be an object")
            continue

        # Required fields
        required = ["skill", "current_level", "target_level", "priority"]
        for field in required:
            if field not in gap:
                errors.append(f"{prefix}: missing required field '{field}'")

        # Validate skill name
        if "skill" in gap:
            if not isinstance(gap["skill"], str) or not gap["skill"].strip():
                errors.append(f"{prefix}.skill: must be a non-empty string")

        # Validate levels
        for level_field in ["current_level", "target_level"]:
            if level_field in gap:
                level = gap[level_field]
                if not isinstance(level, int) or level < SKILL_LEVEL_MIN or level > SKILL_LEVEL_MAX:
                    errors.append(
                        f"{prefix}.{level_field}: '{level}' is invalid. "
                        f"Must be {SKILL_LEVEL_MIN}-{SKILL_LEVEL_MAX}"
                    )

        # Validate priority
        if "priority" in gap:
            priority = gap["priority"]
            if priority not in VALID_PRIORITIES:
                errors.append(
                    f"{prefix}.priority: '{priority}' is invalid. "
                    f"Must be one of: {', '.join(VALID_PRIORITIES)}"
                )

        # Validate effort if present
        if "effort" in gap and gap["effort"]:
            effort = gap["effort"]
            if effort not in VALID_EFFORTS:
                errors.append(
                    f"{prefix}.effort: '{effort}' is invalid. "
                    f"Must be one of: {', '.join(VALID_EFFORTS)}"
                )

        # Validate status if present
        if "status" in gap and gap["status"]:
            status = gap["status"]
            if status not in VALID_GAP_STATUSES:
                errors.append(
                    f"{prefix}.status: '{status}' is invalid. "
                    f"Must be one of: {', '.join(VALID_GAP_STATUSES)}"
                )

    return errors


def _validate_learning_plans(plans: Any) -> list[str]:
    """Validate the learning_plans array."""
    errors = []

    if not isinstance(plans, list):
        return ["learning_plans: must be an array"]

    for i, plan in enumerate(plans):
        prefix = f"learning_plans[{i}]"

        if not isinstance(plan, dict):
            errors.append(f"{prefix}: must be an object")
            continue

        # Validate skill field
        if "skill" in plan:
            if not isinstance(plan["skill"], str):
                errors.append(f"{prefix}.skill: must be a string")

        # Validate resources array
        if "resources" in plan:
            if not isinstance(plan["resources"], list):
                errors.append(f"{prefix}.resources: must be an array")

        # Validate milestones array
        if "milestones" in plan:
            if not isinstance(plan["milestones"], list):
                errors.append(f"{prefix}.milestones: must be an array")

    return errors


def _validate_current_position(position: Any) -> list[str]:
    """Validate the current_position object."""
    errors = []

    if not isinstance(position, dict):
        return ["current_position: must be an object"]

    if "title" not in position:
        errors.append("current_position: missing required field 'title'")
    elif not isinstance(position["title"], str) or not position["title"].strip():
        errors.append("current_position.title: must be a non-empty string")

    return errors


def _validate_nodes(nodes: Any) -> list[str]:
    """Validate the nodes array in career tree."""
    errors = []

    if not isinstance(nodes, list):
        return ["nodes: must be an array"]

    if len(nodes) == 0:
        return ["nodes: must contain at least one node"]

    node_ids = set()

    for i, node in enumerate(nodes):
        prefix = f"nodes[{i}]"

        if not isinstance(node, dict):
            errors.append(f"{prefix}: must be an object")
            continue

        # Required fields
        required = ["id", "title", "type"]
        for field in required:
            if field not in node:
                errors.append(f"{prefix}: missing required field '{field}'")

        # Track IDs for connection validation
        if "id" in node:
            node_id = node["id"]
            if not isinstance(node_id, str) or not node_id.strip():
                errors.append(f"{prefix}.id: must be a non-empty string")
            elif node_id in node_ids:
                errors.append(f"{prefix}.id: duplicate ID '{node_id}'")
            else:
                node_ids.add(node_id)

        # Validate type
        if "type" in node:
            node_type = node["type"]
            if node_type not in VALID_NODE_TYPES:
                errors.append(
                    f"{prefix}.type: '{node_type}' is invalid. "
                    f"Must be one of: {', '.join(VALID_NODE_TYPES)}"
                )

        # Validate connections if present
        if "connections" in node and node["connections"]:
            conn_errors = _validate_connections(node["connections"], prefix, node_ids)
            errors.extend(conn_errors)

    return errors


def _validate_connections(connections: Any, prefix: str, valid_ids: set) -> list[str]:
    """Validate node connections."""
    errors = []

    if not isinstance(connections, list):
        return [f"{prefix}.connections: must be an array"]

    for i, conn in enumerate(connections):
        conn_prefix = f"{prefix}.connections[{i}]"

        if not isinstance(conn, dict):
            errors.append(f"{conn_prefix}: must be an object")
            continue

        if "to" not in conn:
            errors.append(f"{conn_prefix}: missing required field 'to'")

        # Validate relationship if present
        if "relationship" in conn and conn["relationship"]:
            rel = conn["relationship"]
            if rel not in VALID_RELATIONSHIPS:
                errors.append(
                    f"{conn_prefix}.relationship: '{rel}' is invalid. "
                    f"Must be one of: {', '.join(VALID_RELATIONSHIPS)}"
                )

    return errors


def _validate_pathways(pathways: Any, nodes: list) -> list[str]:
    """Validate the pathways array."""
    errors = []

    if not isinstance(pathways, list):
        return ["pathways: must be an array"]

    # Get all valid node IDs
    valid_ids = {n.get("id") for n in nodes if isinstance(n, dict) and "id" in n}

    for i, pathway in enumerate(pathways):
        prefix = f"pathways[{i}]"

        if not isinstance(pathway, dict):
            errors.append(f"{prefix}: must be an object")
            continue

        # Required fields
        if "name" not in pathway:
            errors.append(f"{prefix}: missing required field 'name'")

        if "nodes" not in pathway:
            errors.append(f"{prefix}: missing required field 'nodes'")
        elif not isinstance(pathway["nodes"], list):
            errors.append(f"{prefix}.nodes: must be an array")
        else:
            # Validate node references
            for j, node_id in enumerate(pathway["nodes"]):
                if node_id not in valid_ids:
                    errors.append(
                        f"{prefix}.nodes[{j}]: unknown node ID '{node_id}'"
                    )

    return errors


def _validate_recommendations(recs: Any) -> list[str]:
    """Validate the recommendations array."""
    errors = []

    if not isinstance(recs, list):
        return ["recommendations: must be an array"]

    for i, rec in enumerate(recs):
        prefix = f"recommendations[{i}]"

        if not isinstance(rec, dict):
            errors.append(f"{prefix}: must be an object")
            continue

        # Validate priority if present
        if "priority" in rec and rec["priority"]:
            priority = rec["priority"]
            if priority not in VALID_PRIORITIES:
                errors.append(
                    f"{prefix}.priority: '{priority}' is invalid. "
                    f"Must be one of: {', '.join(VALID_PRIORITIES)}"
                )

    return errors
