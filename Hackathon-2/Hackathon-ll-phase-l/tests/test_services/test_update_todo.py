"""
Unit tests specifically for the update todo functionality.
"""
from src.todo_app.services.todo_service import TodoService


def test_update_todo_success():
    """
    Test that update_todo successfully updates a todo's description.
    """
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Original task")
    todo_id = todo.id

    # Update the description
    result = service.update_todo(todo_id, "Updated task")

    # Verify it was successful
    assert result is True

    # Verify the todo has the new description
    found_todo = service.get_todo_by_id(todo_id)
    assert found_todo is not None
    assert found_todo.description == "Updated task"
    # Verify other attributes remain unchanged
    assert found_todo.id == todo_id
    assert found_todo.completed is False


def test_update_todo_not_found():
    """
    Test that update_todo returns False when todo doesn't exist.
    """
    service = TodoService()

    # Add one todo
    service.add_todo("Test task")

    # Try to update a non-existent todo
    result = service.update_todo(999, "New description")

    # Verify it returns False
    assert result is False


def test_update_todo_with_same_description():
    """
    Test that update_todo works when updating to the same description.
    """
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Same task")
    todo_id = todo.id

    # Update to the same description
    result = service.update_todo(todo_id, "Same task")

    # Verify it returns True (update successful)
    assert result is True

    # Verify the todo still exists with the same description
    found_todo = service.get_todo_by_id(todo_id)
    assert found_todo is not None
    assert found_todo.description == "Same task"


def test_update_todo_multiple_times():
    """
    Test that update_todo can be called multiple times on the same todo.
    """
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Original task")
    todo_id = todo.id

    # Update the description multiple times
    result1 = service.update_todo(todo_id, "First update")
    assert result1 is True

    result2 = service.update_todo(todo_id, "Second update")
    assert result2 is True

    # Verify the final description
    found_todo = service.get_todo_by_id(todo_id)
    assert found_todo is not None
    assert found_todo.description == "Second update"