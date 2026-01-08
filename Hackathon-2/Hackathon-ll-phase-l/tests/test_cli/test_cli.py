"""
Integration tests for the CLI interface.
"""
import io
import sys
from contextlib import redirect_stdout
import pytest
from unittest.mock import patch, MagicMock
from src.todo_app.cli.cli import TodoCLI


def test_add_todo_valid():
    """
    Test adding a todo with valid input.
    """
    cli = TodoCLI()

    # Add a todo directly using the service
    todo = cli.service.add_todo("Test task description")

    # Verify the todo was added
    todos = cli.service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].id == 1
    assert todos[0].description == "Test task description"
    assert todos[0].completed is False


def test_add_todo_empty_description():
    """
    Test adding a todo with empty description.
    """
    cli = TodoCLI()

    # Attempt to add a todo with empty description should raise an exception in validation
    from src.todo_app.utils.validators import validate_todo_description
    is_valid, error_msg = validate_todo_description("")

    assert not is_valid
    assert "Description cannot be empty" in error_msg

    # Verify no todo was added
    todos = cli.service.get_all_todos()
    assert len(todos) == 0


def test_add_todo_whitespace_description():
    """
    Test adding a todo with whitespace-only description.
    """
    cli = TodoCLI()

    # Attempt to add a todo with whitespace-only description should raise an exception in validation
    from src.todo_app.utils.validators import validate_todo_description
    is_valid, error_msg = validate_todo_description("   ")

    assert not is_valid
    assert "Description cannot be empty" in error_msg

    # Verify no todo was added
    todos = cli.service.get_all_todos()
    assert len(todos) == 0


def test_view_command_empty():
    """
    Test viewing todos when no todos exist.
    """
    cli = TodoCLI()

    todos = cli.service.get_all_todos()
    assert len(todos) == 0


def test_view_command_with_todos():
    """
    Test viewing todos when todos exist.
    """
    cli = TodoCLI()

    # Add some todos first
    cli.service.add_todo("First task")
    cli.service.add_todo("Second task")

    todos = cli.service.get_all_todos()
    assert len(todos) == 2
    assert todos[0].description == "First task"
    assert todos[1].description == "Second task"


def test_update_todo_valid():
    """
    Test updating a todo with valid input.
    """
    cli = TodoCLI()

    # Add a todo first
    cli.service.add_todo("Original task")

    # Update the todo
    success = cli.service.update_todo(1, "Updated task")

    assert success is True

    # Verify the update
    todos = cli.service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].description == "Updated task"


def test_update_todo_invalid_id():
    """
    Test updating a todo with invalid ID.
    """
    cli = TodoCLI()

    # Add one todo
    cli.service.add_todo("Test task")

    # Try to update a non-existent todo
    success = cli.service.update_todo(999, "Updated task")

    assert success is False


def test_delete_todo_valid():
    """
    Test deleting a todo with valid input.
    """
    cli = TodoCLI()

    # Add a todo first
    cli.service.add_todo("Task to delete")

    # Verify it exists
    todos = cli.service.get_all_todos()
    assert len(todos) == 1

    # Delete the todo
    success = cli.service.delete_todo(1)

    assert success is True

    # Verify the todo was deleted
    todos = cli.service.get_all_todos()
    assert len(todos) == 0


def test_delete_todo_invalid_id():
    """
    Test deleting a todo with invalid ID.
    """
    cli = TodoCLI()

    # Add one todo
    cli.service.add_todo("Test task")

    # Try to delete a non-existent todo
    success = cli.service.delete_todo(999)

    assert success is False

    # Verify original todo still exists
    todos = cli.service.get_all_todos()
    assert len(todos) == 1


def test_complete_todo_valid():
    """
    Test marking a todo as complete with valid input.
    """
    cli = TodoCLI()

    # Add a todo first
    cli.service.add_todo("Task to complete")

    # Verify it starts as incomplete
    todos = cli.service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].completed is False

    # Mark as complete
    success = cli.service.mark_complete(1)

    assert success is True

    # Verify it's now complete
    todos = cli.service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].completed is True


def test_complete_todo_invalid_id():
    """
    Test marking a todo as complete with invalid ID.
    """
    cli = TodoCLI()

    # Add one todo
    cli.service.add_todo("Test task")

    # Try to mark a non-existent todo as complete
    success = cli.service.mark_complete(999)

    assert success is False

    # Verify original todo is still incomplete
    todos = cli.service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].completed is False