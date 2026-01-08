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

The application provides a menu-based interface with the following options:

1. Add Todo - Create a new todo item
2. View All Todos - Display all your todos
3. Update Todo - Change the description of an existing todo
4. Delete Todo - Remove a todo from your list
5. Mark Todo as Complete - Change todo status to complete
6. Help - Show help information
7. Quit - Exit the application