"""
Unit tests for the TodoService.
"""
import pytest
from src.todo_app.services.todo_service import TodoService
from src.todo_app.models.todo import Todo


def test_add_todo_basic(todo_service):
    """
    Test adding a basic todo item.
    """
    result = todo_service.add_todo("Test task")

    assert isinstance(result, Todo)
    assert result.id == 1
    assert result.description == "Test task"
    assert result.completed is False

    # Verify it's in the service
    todos = todo_service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].id == 1
    assert todos[0].description == "Test task"
    assert todos[0].completed is False


def test_add_multiple_todos_sequential_ids(todo_service):
    """
    Test adding multiple todos results in sequential IDs.
    """
    todo1 = todo_service.add_todo("First task")
    todo2 = todo_service.add_todo("Second task")
    todo3 = todo_service.add_todo("Third task")

    assert todo1.id == 1
    assert todo2.id == 2
    assert todo3.id == 3

    todos = todo_service.get_all_todos()
    assert len(todos) == 3
    assert todos[0].id == 1
    assert todos[1].id == 2
    assert todos[2].id == 3


def test_get_all_todos_empty(todo_service):
    """
    Test getting all todos when none exist.
    """
    todos = todo_service.get_all_todos()
    assert len(todos) == 0


def test_get_all_todos_with_items(todo_service):
    """
    Test getting all todos when some exist.
    """
    todo_service.add_todo("Task 1")
    todo_service.add_todo("Task 2")

    todos = todo_service.get_all_todos()
    assert len(todos) == 2
    assert todos[0].description == "Task 1"
    assert todos[1].description == "Task 2"


def test_get_todo_by_id_found(todo_service):
    """
    Test getting a todo by ID when it exists.
    """
    added_todo = todo_service.add_todo("Test task")

    found_todo = todo_service.get_todo_by_id(added_todo.id)
    assert found_todo is not None
    assert found_todo.id == added_todo.id
    assert found_todo.description == added_todo.description
    assert found_todo.completed == added_todo.completed


def test_get_todo_by_id_not_found(todo_service):
    """
    Test getting a todo by ID when it doesn't exist.
    """
    todo_service.add_todo("Test task")

    found_todo = todo_service.get_todo_by_id(999)
    assert found_todo is None


def test_update_todo_success(todo_service):
    """
    Test updating a todo's description successfully.
    """
    original_todo = todo_service.add_todo("Original task")

    success = todo_service.update_todo(original_todo.id, "Updated task")

    assert success is True

    # Verify the update
    updated_todo = todo_service.get_todo_by_id(original_todo.id)
    assert updated_todo.description == "Updated task"


def test_update_todo_not_found(todo_service):
    """
    Test updating a todo that doesn't exist.
    """
    success = todo_service.update_todo(999, "New description")

    assert success is False


def test_delete_todo_success(todo_service):
    """
    Test deleting a todo successfully.
    """
    todo_to_delete = todo_service.add_todo("Task to delete")

    success = todo_service.delete_todo(todo_to_delete.id)

    assert success is True

    # Verify it's gone
    remaining_todos = todo_service.get_all_todos()
    assert len(remaining_todos) == 0

    # Verify it can't be retrieved by ID
    found_todo = todo_service.get_todo_by_id(todo_to_delete.id)
    assert found_todo is None


def test_delete_todo_not_found(todo_service):
    """
    Test deleting a todo that doesn't exist.
    """
    success = todo_service.delete_todo(999)

    assert success is False


def test_mark_complete_success(todo_service):
    """
    Test marking a todo as complete successfully.
    """
    todo_to_complete = todo_service.add_todo("Task to complete")

    # Verify it starts as incomplete
    assert todo_to_complete.completed is False

    success = todo_service.mark_complete(todo_to_complete.id)

    assert success is True

    # Verify it's now complete
    completed_todo = todo_service.get_todo_by_id(todo_to_complete.id)
    assert completed_todo.completed is True


def test_mark_complete_not_found(todo_service):
    """
    Test marking a todo as complete when it doesn't exist.
    """
    success = todo_service.mark_complete(999)

    assert success is False