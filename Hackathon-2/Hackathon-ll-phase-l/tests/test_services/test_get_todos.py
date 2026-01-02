"""
Unit tests specifically for the get all todos and get todo by ID functionality.
"""
import pytest
from src.todo_app.services.todo_service import TodoService


def test_get_all_todos_empty_initially():
    """
    Test that get_all_todos returns an empty list initially.
    """
    service = TodoService()
    todos = service.get_all_todos()

    assert len(todos) == 0


def test_get_all_todos_after_adding():
    """
    Test that get_all_todos returns all added todos.
    """
    service = TodoService()

    # Add some todos
    service.add_todo("First task")
    service.add_todo("Second task")
    service.add_todo("Third task")

    todos = service.get_all_todos()

    assert len(todos) == 3
    assert todos[0].description == "First task"
    assert todos[1].description == "Second task"
    assert todos[2].description == "Third task"


def test_get_todo_by_id_found():
    """
    Test that get_todo_by_id returns the correct todo when it exists.
    """
    service = TodoService()

    # Add a todo
    added_todo = service.add_todo("Test task")
    todo_id = added_todo.id

    # Retrieve by ID
    found_todo = service.get_todo_by_id(todo_id)

    assert found_todo is not None
    assert found_todo.id == todo_id
    assert found_todo.description == "Test task"
    assert found_todo.completed is False


def test_get_todo_by_id_not_found():
    """
    Test that get_todo_by_id returns None when todo doesn't exist.
    """
    service = TodoService()

    # Add one todo
    service.add_todo("Test task")

    # Try to get a non-existent ID
    found_todo = service.get_todo_by_id(999)

    assert found_todo is None


def test_get_all_todos_returns_copy():
    """
    Test that get_all_todos returns a copy, not the internal list.
    """
    service = TodoService()

    # Add a todo
    service.add_todo("Test task")

    # Get the list
    todos = service.get_all_todos()

    # Modify the returned list
    todos.clear()

    # Verify internal list is not affected
    internal_todos = service.get_all_todos()
    assert len(internal_todos) == 1
    assert internal_todos[0].description == "Test task"