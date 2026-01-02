"""
Command-line interface for the Todo application.
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
    Command-line interface for interacting with the Todo application.
    """
    def __init__(self):
        """
        Initialize the CLI with a TodoService instance.
        """
        self.service = TodoService()

    def run(self):
        """
        Run the main CLI loop, processing user commands until quit.
        """
        print("Welcome to the Todo App!")
        print("Type 'help' for available commands or 'quit' to exit.")

        while True:
            try:
                # Get user input
                user_input = input("\n> ").strip()

                # Parse the command
                if not user_input:
                    continue

                # Split the command and arguments
                parts = user_input.split(maxsplit=1)
                command = parts[0].lower()

                # Get the rest of the input as arguments
                args = parts[1] if len(parts) > 1 else ""

                # Process the command
                if command == "quit":
                    print("Goodbye!")
                    break
                elif command == "help":
                    self._show_help()
                else:
                    # Process other commands
                    self._process_command(command, args)

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

    def _process_command(self, command: str, args: str):
        """
        Process a specific command with its arguments.
        """
        if command == "add":
            self._handle_add(args)
        elif command == "view":
            self._handle_view()
        elif command == "update":
            self._handle_update(args)
        elif command == "delete":
            self._handle_delete(args)
        elif command == "complete":
            self._handle_complete(args)
        else:
            print(f"Unknown command: {command}. Type 'help' for available commands.")

    def _handle_add(self, args: str):
        """
        Handle the 'add' command to add a new todo.
        """
        description = args.strip().strip('"\'')

        # Validate the description
        is_valid, error_msg = validate_todo_description(description)
        if not is_valid:
            print(f"Error: {error_msg}")
            return

        # Add the todo
        new_todo = self.service.add_todo(description)
        print(f"Added todo with ID {new_todo.id}: {new_todo.description}")

    def _handle_view(self):
        """
        Handle the 'view' command to display all todos.
        """
        todos = self.service.get_all_todos()

        if not todos:
            print("No todos found.")
            return

        print("Your todos:")
        for todo in todos:
            status = "Complete" if todo.completed else "Incomplete"
            print(f"ID: {todo.id} - {todo.description} - [{status}]")

    def _handle_update(self, args: str):
        """
        Handle the 'update' command to update a todo's description.
        """
        # Parse ID and new description
        parts = args.split(maxsplit=1)
        if len(parts) != 2:
            print("Usage: update <id> \"new description\"")
            return

        try:
            todo_id = int(parts[0])
        except ValueError:
            print("Error: ID must be a number")
            return

        # Validate the ID
        is_valid, error_msg = validate_todo_id(todo_id)
        if not is_valid:
            print(f"Error: {error_msg}")
            return

        new_description = parts[1].strip().strip('"\'')

        # Validate the new description
        is_valid, error_msg = validate_todo_description(new_description)
        if not is_valid:
            print(f"Error: {error_msg}")
            return

        # Update the todo
        if self.service.update_todo(todo_id, new_description):
            print(f"Updated todo with ID {todo_id}")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def _handle_delete(self, args: str):
        """
        Handle the 'delete' command to delete a todo.
        """
        if not args:
            print("Usage: delete <id>")
            return

        try:
            todo_id = int(args.strip())
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
            print(f"Deleted todo with ID {todo_id}")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def _handle_complete(self, args: str):
        """
        Handle the 'complete' command to mark a todo as complete.
        """
        if not args:
            print("Usage: complete <id>")
            return

        try:
            todo_id = int(args.strip())
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
            print(f"Marked todo with ID {todo_id} as complete")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def _show_help(self):
        """
        Display help information for available commands.
        """
        print("\nAvailable commands:")
        print("  add \"description\"     - Add a new todo with the given description")
        print("  view                - Display all todos with their ID, description, and status")
        print("  update <id> \"desc\"  - Update the description of a todo")
        print("  delete <id>         - Delete a todo by its ID")
        print("  complete <id>       - Mark a todo as complete")
        print("  help                - Show this help message")
        print("  quit                - Exit the application")


def main():
    """
    Main entry point for the CLI application.
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()