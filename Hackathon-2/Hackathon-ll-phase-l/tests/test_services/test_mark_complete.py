"""
Unit tests specifically for the mark complete functionality.
"""
from src.todo_app.services.todo_service import TodoService


def test_mark_complete_success():
    """
    Test that mark_complete successfully marks a todo as complete.
    """
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Test task")
    todo_id = todo.id

    # Verify it starts as incomplete
    assert todo.completed is False

    # Mark as complete
    result = service.mark_complete(todo_id)

    # Verify it was successful
    assert result is True

    # Verify the todo is now complete
    found_todo = service.get_todo_by_id(todo_id)
    assert found_todo is not None
    assert found_todo.completed is True


def test_mark_complete_not_found():
    """
    Test that mark_complete returns False when todo doesn't exist.
    """
    service = TodoService()

    # Add one todo
    service.add_todo("Test task")

    # Try to mark a non-existent todo as complete
    result = service.mark_complete(999)

    # Verify it returns False
    assert result is False


def test_mark_complete_already_complete():
    """
    Test that mark_complete works even if todo is already complete.
    """
    service = TodoService()

    # Add and mark a todo as complete
    todo = service.add_todo("Test task")
    todo_id = todo.id
    service.mark_complete(todo_id)

    # Verify it's complete
    found_todo = service.get_todo_by_id(todo_id)
    assert found_todo.completed is True

    # Try to mark it as complete again
    result = service.mark_complete(todo_id)

    # Should still return True
    assert result is True

    # Should still be complete
    found_todo = service.get_todo_by_id(todo_id)
    assert found_todo.completed is True