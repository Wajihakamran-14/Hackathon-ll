"""
Integration tests for the CLI interface.
"""
import io
import sys
from contextlib import redirect_stdout
import pytest
from src.todo_app.cli.cli import TodoCLI


def test_add_command_valid():
    """
    Test the add command with valid input.
    """
    cli = TodoCLI()

    # Capture output
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_add('"Test task description"')

    output = captured_output.getvalue().strip()
    assert "Added todo with ID 1: Test task description" in output

    # Verify the todo was actually added
    todos = cli.service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].id == 1
    assert todos[0].description == "Test task description"
    assert todos[0].completed is False


def test_add_command_empty_description():
    """
    Test the add command with empty description.
    """
    cli = TodoCLI()

    # Capture output
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_add('""')

    output = captured_output.getvalue().strip()
    assert "Error: Description cannot be empty" in output

    # Verify no todo was added
    todos = cli.service.get_all_todos()
    assert len(todos) == 0


def test_add_command_whitespace_description():
    """
    Test the add command with whitespace-only description.
    """
    cli = TodoCLI()

    # Capture output
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_add('"   "')

    output = captured_output.getvalue().strip()
    assert "Error: Description cannot be empty" in output

    # Verify no todo was added
    todos = cli.service.get_all_todos()
    assert len(todos) == 0


def test_view_command_empty():
    """
    Test the view command when no todos exist.
    """
    cli = TodoCLI()

    # Capture output
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_view()

    output = captured_output.getvalue().strip()
    assert "No todos found." in output


def test_view_command_with_todos():
    """
    Test the view command when todos exist.
    """
    cli = TodoCLI()

    # Add some todos first
    cli.service.add_todo("First task")
    cli.service.add_todo("Second task")

    # Capture output
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_view()

    output = captured_output.getvalue().strip()
    assert "Your todos:" in output
    assert "ID: 1 - First task - [Incomplete]" in output
    assert "ID: 2 - Second task - [Incomplete]" in output


def test_update_command_valid():
    """
    Test the update command with valid input.
    """
    cli = TodoCLI()

    # Add a todo first
    cli.service.add_todo("Original task")

    # Capture output
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_update('1 "Updated task"')

    output = captured_output.getvalue().strip()
    assert "Updated todo with ID 1" in output

    # Verify the update
    todos = cli.service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].description == "Updated task"


def test_update_command_invalid_id():
    """
    Test the update command with invalid ID.
    """
    cli = TodoCLI()

    # Capture output
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_update('999 "Updated task"')

    output = captured_output.getvalue().strip()
    assert "Error: Todo with ID 999 not found" in output


def test_delete_command_valid():
    """
    Test the delete command with valid input.
    """
    cli = TodoCLI()

    # Add a todo first
    cli.service.add_todo("Task to delete")

    # Capture output
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_delete('1')

    output = captured_output.getvalue().strip()
    assert "Deleted todo with ID 1" in output

    # Verify the todo was deleted
    todos = cli.service.get_all_todos()
    assert len(todos) == 0


def test_delete_command_invalid_id():
    """
    Test the delete command with invalid ID.
    """
    cli = TodoCLI()

    # Capture output
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_delete('999')

    output = captured_output.getvalue().strip()
    assert "Error: Todo with ID 999 not found" in output


def test_complete_command_valid():
    """
    Test the complete command with valid input.
    """
    cli = TodoCLI()

    # Add a todo first
    cli.service.add_todo("Task to complete")

    # Capture output
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_complete('1')

    output = captured_output.getvalue().strip()
    assert "Marked todo with ID 1 as complete" in output

    # Verify the todo is now complete
    todos = cli.service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].completed is True


def test_complete_command_invalid_id():
    """
    Test the complete command with invalid ID.
    """
    cli = TodoCLI()

    # Capture output
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_complete('999')

    output = captured_output.getvalue().strip()
    assert "Error: Todo with ID 999 not found" in output