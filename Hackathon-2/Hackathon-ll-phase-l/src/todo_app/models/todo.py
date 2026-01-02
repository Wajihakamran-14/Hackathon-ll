"""
Todo data model representing a single task with an ID, description, and completion status.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Todo:
    """
    Represents a single todo item with id, description, and completion status.
    """
    id: int
    description: str
    completed: bool = False

    def __post_init__(self):
        """
        Validate the todo after initialization.
        """
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"ID must be a positive integer, got {self.id}")

        if not isinstance(self.description, str):
            raise ValueError(f"Description must be a string, got {type(self.description)}")

        if not self.description.strip():
            raise ValueError("Description cannot be empty or only whitespace")

        if len(self.description) > 1000:
            raise ValueError("Description must not exceed 1000 characters")

        if not isinstance(self.completed, bool):
            raise ValueError(f"Completed must be a boolean, got {type(self.completed)}")