"""
Test configuration and fixtures for the Todo application tests.
"""
import pytest
from src.todo_app.services.todo_service import TodoService


@pytest.fixture
def todo_service():
    """
    Fixture that provides a fresh TodoService instance for each test.
    """
    return TodoService()