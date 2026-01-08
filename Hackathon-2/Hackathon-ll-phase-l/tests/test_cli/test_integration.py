"""
Integration tests for the menu-based CLI interface.
"""
import io
import sys
from contextlib import redirect_stdout
from unittest.mock import patch
from src.todo_app.cli.cli import TodoCLI


def test_full_workflow():
    """
    Test the complete workflow: add, view, update, complete, delete.
    """
    cli = TodoCLI()

    # Add a few todos using the service directly
    first_todo = cli.service.add_todo("First task")
    second_todo = cli.service.add_todo("Second task")

    # Verify they were added
    todos = cli.service.get_all_todos()
    assert len(todos) == 2
    assert todos[0].description == "First task"
    assert todos[1].description == "Second task"

    # Update the first todo
    success = cli.service.update_todo(1, "Updated first task")
    assert success is True

    # Verify the update
    updated_todo = cli.service.get_todo_by_id(1)
    assert updated_todo.description == "Updated first task"

    # Mark the second todo as complete
    success = cli.service.mark_complete(2)
    assert success is True

    # Verify it's marked as complete
    completed_todo = cli.service.get_todo_by_id(2)
    assert completed_todo.completed is True

    # Delete the first todo
    success = cli.service.delete_todo(1)
    assert success is True

    # Verify deletion
    todos = cli.service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].id == 2
    assert todos[0].completed is True


def test_error_scenarios():
    """
    Test various error scenarios.
    """
    cli = TodoCLI()

    # Try to update a non-existent todo
    success = cli.service.update_todo(999, "Non-existent task")
    assert success is False

    # Try to delete a non-existent todo
    success = cli.service.delete_todo(999)
    assert success is False

    # Try to mark complete a non-existent todo
    success = cli.service.mark_complete(999)
    assert success is False

    # Try to get a non-existent todo
    todo = cli.service.get_todo_by_id(999)
    assert todo is None


def test_menu_methods_exist():
    """
    Test that the menu methods exist in the CLI class.
    """
    cli = TodoCLI()

    # Just verify the CLI can be instantiated and has the required methods
    assert hasattr(cli, 'service')
    assert hasattr(cli, '_show_menu')
    assert hasattr(cli, '_add_todo')
    assert hasattr(cli, '_view_todos')
    assert hasattr(cli, '_update_todo')
    assert hasattr(cli, '_delete_todo')
    assert hasattr(cli, '_complete_todo')
    assert hasattr(cli, '_show_help_menu')