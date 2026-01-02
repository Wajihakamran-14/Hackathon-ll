"""
Unit tests specifically for the delete todo functionality.
"""
from src.todo_app.services.todo_service import TodoService


def test_delete_todo_success():
    """
    Test that delete_todo successfully removes a todo.
    """
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Task to delete")
    todo_id = todo.id

    # Verify it exists
    assert len(service.get_all_todos()) == 1
    assert service.get_todo_by_id(todo_id) is not None

    # Delete the todo
    result = service.delete_todo(todo_id)

    # Verify it was successful
    assert result is True

    # Verify the todo is gone
    assert len(service.get_all_todos()) == 0
    assert service.get_todo_by_id(todo_id) is None


def test_delete_todo_not_found():
    """
    Test that delete_todo returns False when todo doesn't exist.
    """
    service = TodoService()

    # Add one todo
    service.add_todo("Test task")

    # Try to delete a non-existent todo
    result = service.delete_todo(999)

    # Verify it returns False
    assert result is False

    # Verify the existing todo is still there
    todos = service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].description == "Test task"


def test_delete_todo_with_multiple_todos():
    """
    Test that delete_todo removes only the specified todo.
    """
    service = TodoService()

    # Add multiple todos
    todo1 = service.add_todo("First task")
    todo2 = service.add_todo("Second task")
    todo3 = service.add_todo("Third task")

    # Verify all exist
    assert len(service.get_all_todos()) == 3

    # Delete the second todo
    result = service.delete_todo(todo2.id)

    # Verify it was successful
    assert result is True

    # Verify only the specified todo was removed
    todos = service.get_all_todos()
    assert len(todos) == 2
    # Verify the correct todos remain
    remaining_ids = [t.id for t in todos]
    assert todo1.id in remaining_ids
    assert todo3.id in remaining_ids
    assert todo2.id not in remaining_ids


def test_delete_all_todos():
    """
    Test that all todos can be deleted one by one.
    """
    service = TodoService()

    # Add multiple todos
    service.add_todo("First task")
    service.add_todo("Second task")
    service.add_todo("Third task")

    # Verify all exist
    assert len(service.get_all_todos()) == 3

    # Delete all todos
    result1 = service.delete_todo(1)
    result2 = service.delete_todo(2)
    result3 = service.delete_todo(3)

    # Verify all deletions were successful
    assert result1 is True
    assert result2 is True
    assert result3 is True

    # Verify no todos remain
    assert len(service.get_all_todos()) == 0


def test_delete_todo_id_reuse():
    """
    Test that deleted todo IDs are not reused.
    """
    service = TodoService()

    # Add a todo and delete it
    todo = service.add_todo("Task to delete")
    original_id = todo.id
    service.delete_todo(original_id)

    # Add a new todo
    new_todo = service.add_todo("New task")

    # Verify the new todo has a different ID
    assert new_todo.id != original_id
    assert new_todo.id == original_id + 1