"""
Comprehensive integration tests for all CLI commands working together.
"""
import io
import sys
from contextlib import redirect_stdout
from src.todo_app.cli.cli import TodoCLI


def test_full_workflow():
    """
    Test the complete workflow: add, view, update, complete, delete.
    """
    cli = TodoCLI()

    # Capture output for each step
    output_log = []

    # Add a few todos
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_add('"First task"')
    output_log.append(captured_output.getvalue().strip())

    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_add('"Second task"')
    output_log.append(captured_output.getvalue().strip())

    # View all todos
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_view()
    output_log.append(captured_output.getvalue().strip())

    # Update the first todo
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_update('1 "Updated first task"')
    output_log.append(captured_output.getvalue().strip())

    # Mark the second todo as complete
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_complete('2')
    output_log.append(captured_output.getvalue().strip())

    # View all todos again to see changes
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_view()
    output_log.append(captured_output.getvalue().strip())

    # Delete the first todo
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_delete('1')
    output_log.append(captured_output.getvalue().strip())

    # View all todos to confirm deletion
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_view()
    output_log.append(captured_output.getvalue().strip())

    # Verify the expected outputs
    assert "Added todo with ID 1: First task" in output_log[0]
    assert "Added todo with ID 2: Second task" in output_log[1]
    assert "ID: 1 - First task - [Incomplete]" in output_log[2]
    assert "ID: 2 - Second task - [Incomplete]" in output_log[2]
    assert "Updated todo with ID 1" in output_log[3]
    assert "Marked todo with ID 2 as complete" in output_log[4]
    assert "ID: 1 - Updated first task - [Incomplete]" in output_log[5]
    assert "ID: 2 - Second task - [Complete]" in output_log[5]
    assert "Deleted todo with ID 1" in output_log[6]
    assert "ID: 2 - Second task - [Complete]" in output_log[7]
    assert "ID: 1 - Updated first task - [Incomplete]" not in output_log[7]  # Verify deletion


def test_error_scenarios():
    """
    Test various error scenarios.
    """
    cli = TodoCLI()

    # Try to update a non-existent todo
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_update('999 "Non-existent task"')
    output = captured_output.getvalue().strip()
    assert "Error: Todo with ID 999 not found" in output

    # Try to delete a non-existent todo
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_delete('999')
    output = captured_output.getvalue().strip()
    assert "Error: Todo with ID 999 not found" in output

    # Try to mark complete a non-existent todo
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_complete('999')
    output = captured_output.getvalue().strip()
    assert "Error: Todo with ID 999 not found" in output

    # Try to add a todo with empty description
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._handle_add('""')
    output = captured_output.getvalue().strip()
    assert "Error: Description cannot be empty" in output


def test_help_command():
    """
    Test the help command.
    """
    cli = TodoCLI()

    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        cli._show_help()
    output = captured_output.getvalue()

    # Verify help contains expected commands
    assert "add" in output
    assert "view" in output
    assert "update" in output
    assert "delete" in output
    assert "complete" in output
    assert "help" in output
    assert "quit" in output