# Quickstart: Console Todo App

## Prerequisites
- Python 3.13+ installed
- UV package manager installed

## Setup

1. **Create the project directory:**
   ```bash
   mkdir Hackathon-ll-phase-l
   cd Hackathon-ll-phase-l
   ```

2. **Initialize Python project with UV:**
   ```bash
   uv init
   ```

3. **Create the directory structure:**
   ```bash
   mkdir -p src/todo_app/{models,services,cli,utils}
   mkdir -p tests/{test_models,test_services,test_cli}
   ```

## Project Structure
```
Hackathon-ll-phase-l/
├── pyproject.toml
├── README.md
├── src/
│   └── todo_app/
│       ├── __init__.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── todo.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── todo_service.py
│       ├── cli/
│       │   ├── __init__.py
│       │   └── cli.py
│       └── utils/
│           ├── __init__.py
│           └── validators.py
├── tests/
│   ├── __init__.py
│   ├── test_models/
│   │   └── test_todo.py
│   ├── test_services/
│   │   └── test_todo_service.py
│   ├── test_cli/
│   │   └── test_cli.py
│   └── conftest.py
└── .env.example
```

## Running the Application
```bash
# Install dependencies
uv sync

# Run the application
uv run src/todo_app/cli/cli.py
```

## Running Tests
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_models/test_todo.py
```

## Available Commands
- `add "description"` - Add a new todo with the given description
- `view` - Display all todos with their ID, description, and status
- `update <id> "new description"` - Update the description of a todo
- `delete <id>` - Delete a todo by its ID
- `complete <id>` - Mark a todo as complete
- `help` - Show available commands
- `quit` - Exit the application