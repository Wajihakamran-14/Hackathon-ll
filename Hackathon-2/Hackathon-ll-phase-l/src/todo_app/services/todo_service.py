"""
TodoService handles all business logic for todo operations using in-memory storage.
"""
from typing import List, Optional
from ..models.todo import Todo


class TodoService:
    """
    Service class that manages all todo operations using in-memory storage.
    """
    def __init__(self):
        """
        Initialize the service with an empty list of todos and a counter for IDs.
        """
        self.todos: List[Todo] = []
        self._next_id = 1

    def add_todo(self, description: str) -> Todo:
        """
        Add a new todo with the given description.

        Args:
            description: The description of the todo item

        Returns:
            The newly created Todo object with assigned ID
        """
        # Create a new todo with the next available ID
        new_todo = Todo(
            id=self._next_id,
            description=description,
            completed=False
        )

        # Add to the list
        self.todos.append(new_todo)

        # Increment the ID counter for the next todo
        self._next_id += 1

        return new_todo

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos in the system.

        Returns:
            A list of all Todo objects
        """
        return self.todos.copy()

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Get a specific todo by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The Todo object if found, None otherwise
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, new_description: str) -> bool:
        """
        Update the description of an existing todo.

        Args:
            todo_id: The ID of the todo to update
            new_description: The new description for the todo

        Returns:
            True if the todo was found and updated, False otherwise
        """
        for todo in self.todos:
            if todo.id == todo_id:
                todo.description = new_description
                return True
        return False

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was found and deleted, False otherwise
        """
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                return True
        return False

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a todo as complete by its ID.

        Args:
            todo_id: The ID of the todo to mark as complete

        Returns:
            True if the todo was found and marked as complete, False otherwise
        """
        for todo in self.todos:
            if todo.id == todo_id:
                todo.completed = True
                return True
        return False