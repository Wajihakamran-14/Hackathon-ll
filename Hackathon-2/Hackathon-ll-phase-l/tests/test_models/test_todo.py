"""
Unit tests for the Todo model.
"""
import pytest
from src.todo_app.models.todo import Todo


def test_todo_creation_valid():
    """
    Test creating a valid Todo object.
    """
    todo = Todo(id=1, description="Test task", completed=False)

    assert todo.id == 1
    assert todo.description == "Test task"
    assert todo.completed is False


def test_todo_creation_defaults():
    """
    Test creating a Todo object with default values.
    """
    todo = Todo(id=1, description="Test task")

    assert todo.id == 1
    assert todo.description == "Test task"
    assert todo.completed is False


def test_todo_invalid_id_negative():
    """
    Test creating a Todo with a negative ID raises ValueError.
    """
    with pytest.raises(ValueError, match="ID must be a positive integer"):
        Todo(id=-1, description="Test task")


def test_todo_invalid_id_zero():
    """
    Test creating a Todo with ID 0 raises ValueError.
    """
    with pytest.raises(ValueError, match="ID must be a positive integer"):
        Todo(id=0, description="Test task")


def test_todo_invalid_id_not_integer():
    """
    Test creating a Todo with non-integer ID raises ValueError.
    """
    with pytest.raises(ValueError, match="ID must be a positive integer"):
        Todo(id="invalid", description="Test task")


def test_todo_empty_description():
    """
    Test creating a Todo with empty description raises ValueError.
    """
    with pytest.raises(ValueError, match="Description cannot be empty"):
        Todo(id=1, description="")


def test_todo_whitespace_only_description():
    """
    Test creating a Todo with whitespace-only description raises ValueError.
    """
    with pytest.raises(ValueError, match="Description cannot be empty"):
        Todo(id=1, description="   ")


def test_todo_long_description():
    """
    Test creating a Todo with description longer than 1000 characters raises ValueError.
    """
    long_desc = "x" * 1001
    with pytest.raises(ValueError, match="Description must not exceed 1000 characters"):
        Todo(id=1, description=long_desc)


def test_todo_invalid_completed_type():
    """
    Test creating a Todo with non-boolean completed value raises ValueError.
    """
    with pytest.raises(ValueError, match="Completed must be a boolean"):
        Todo(id=1, description="Test task", completed="invalid")