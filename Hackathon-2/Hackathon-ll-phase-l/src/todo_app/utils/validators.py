"""
Input validation utilities for the Todo application.
"""


def validate_todo_description(description: str) -> tuple[bool, str]:
    """
    Validate a todo description according to the business rules.

    Args:
        description: The description to validate

    Returns:
        A tuple of (is_valid, error_message) where is_valid is True if the
        description is valid, and error_message contains details if it's not.
    """
    if not isinstance(description, str):
        return False, "Description must be a string"

    if not description.strip():
        return False, "Description cannot be empty or only whitespace"

    if len(description) > 1000:
        return False, "Description must not exceed 1000 characters"

    return True, ""


def validate_todo_id(todo_id: int) -> tuple[bool, str]:
    """
    Validate a todo ID according to the business rules.

    Args:
        todo_id: The ID to validate

    Returns:
        A tuple of (is_valid, error_message) where is_valid is True if the
        ID is valid, and error_message contains details if it's not.
    """
    if not isinstance(todo_id, int):
        return False, f"ID must be an integer, got {type(todo_id).__name__}"

    if todo_id <= 0:
        return False, f"ID must be a positive integer, got {todo_id}"

    return True, ""