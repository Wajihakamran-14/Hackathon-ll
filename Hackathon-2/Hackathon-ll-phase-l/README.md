# Console Todo App

A simple in-memory console-based todo application built with Python.

## Features

- Add new todo items with unique IDs
- View all todos with their status
- Update todo descriptions
- Delete todos
- Mark todos as complete

## Requirements

- Python 3.13+
- UV package manager (for development)

## Installation

1. Clone the repository
2. Install dependencies with UV: `uv sync`
3. Run the application: `uv run src/todo_app/cli/cli.py`

## Usage

To run the application:
```bash
python src/todo_app/cli/cli.py
```

The application provides a command-line interface with the following commands:

- `add "description"` - Add a new todo with the given description
- `view` - Display all todos with their ID, description, and status
- `update <id> "new description"` - Update the description of a todo
- `delete <id>` - Delete a todo by its ID
- `complete <id>` - Mark a todo as complete
- `help` - Show available commands
- `quit` - Exit the application