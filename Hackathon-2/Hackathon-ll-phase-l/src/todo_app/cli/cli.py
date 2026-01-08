"""
Menu-based interface for the Todo application.
"""
import sys
import os
from typing import List

# Add the src directory to the path to allow imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from todo_app.services.todo_service import TodoService
from todo_app.utils.validators import validate_todo_description, validate_todo_id


class TodoCLI:
    """
    Menu-based interface for interacting with the Todo application.
    """
    def __init__(self):
        """
        Initialize the CLI with a TodoService instance.
        """
        self.service = TodoService()

    def run(self):
        """
        Run the main menu loop, processing user choices until quit.
        """
        while True:
            self._show_menu()
            try:
                choice = input("\nEnter your choice (1-7): ").strip()

                if choice == "1":
                    self._add_todo()
                elif choice == "2":
                    self._view_todos()
                elif choice == "3":
                    self._update_todo()
                elif choice == "4":
                    self._delete_todo()
                elif choice == "5":
                    self._complete_todo()
                elif choice == "6":
                    self._show_help_menu()
                elif choice == "7":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a number between 1-7.")

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

    def _show_menu(self):
        """
        Display the main menu options.
        """
        print("\n" + "="*50)
        print("           TODO APPLICATION")
        print("="*50)
        print("1. Add Todo")
        print("2. View All Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Mark Todo as Complete")
        print("6. Help")
        print("7. Quit")
        print("="*50)

    def _add_todo(self):
        """
        Handle adding a new todo.
        """
        description = input("Enter todo description: ").strip()

        # Validate the description
        is_valid, error_msg = validate_todo_description(description)
        if not is_valid:
            print(f"Error: {error_msg}")
            return

        # Add the todo
        new_todo = self.service.add_todo(description)
        print(f"[OK] Added todo with ID {new_todo.id}: {new_todo.description}")

    def _view_todos(self):
        """
        Handle viewing all todos.
        """
        todos = self.service.get_all_todos()

        if not todos:
            print("No todos found.")
            return

        print("\nYour todos:")
        print("-" * 60)
        for todo in todos:
            status = "[COMPLETED]" if todo.completed else "[INCOMPLETE]"
            print(f"ID: {todo.id} | {todo.description} | [{status}]")
        print("-" * 60)

    def _update_todo(self):
        """
        Handle updating a todo's description.
        """
        try:
            todo_id = int(input("Enter todo ID to update: ").strip())
        except ValueError:
            print("Error: ID must be a number")
            return

        # Validate the ID
        is_valid, error_msg = validate_todo_id(todo_id)
        if not is_valid:
            print(f"Error: {error_msg}")
            return

        # Check if todo exists
        existing_todo = self.service.get_todo_by_id(todo_id)
        if not existing_todo:
            print(f"Error: Todo with ID {todo_id} not found")
            return

        print(f"Current description: {existing_todo.description}")
        new_description = input("Enter new description: ").strip()

        # Validate the new description
        is_valid, error_msg = validate_todo_description(new_description)
        if not is_valid:
            print(f"Error: {error_msg}")
            return

        # Update the todo
        if self.service.update_todo(todo_id, new_description):
            print(f"[OK] Updated todo with ID {todo_id}")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def _delete_todo(self):
        """
        Handle deleting a todo.
        """
        try:
            todo_id = int(input("Enter todo ID to delete: ").strip())
        except ValueError:
            print("Error: ID must be a number")
            return

        # Validate the ID
        is_valid, error_msg = validate_todo_id(todo_id)
        if not is_valid:
            print(f"Error: {error_msg}")
            return

        # Delete the todo
        if self.service.delete_todo(todo_id):
            print(f"[OK] Deleted todo with ID {todo_id}")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def _complete_todo(self):
        """
        Handle marking a todo as complete.
        """
        try:
            todo_id = int(input("Enter todo ID to mark complete: ").strip())
        except ValueError:
            print("Error: ID must be a number")
            return

        # Validate the ID
        is_valid, error_msg = validate_todo_id(todo_id)
        if not is_valid:
            print(f"Error: {error_msg}")
            return

        # Mark as complete
        if self.service.mark_complete(todo_id):
            print(f"[OK] Marked todo with ID {todo_id} as complete")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def _show_help_menu(self):
        """
        Display help information for the menu options.
        """
        print("\n" + "="*50)
        print("                    HELP")
        print("="*50)
        print("1. Add Todo - Create a new todo item")
        print("2. View All Todos - Display all your todos")
        print("3. Update Todo - Change the description of an existing todo")
        print("4. Delete Todo - Remove a todo from your list")
        print("5. Mark Todo as Complete - Change todo status to complete")
        print("6. Help - Show this help message")
        print("7. Quit - Exit the application")
        print("="*50)

def main():
    """
    Main entry point for the CLI application.
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()