# Todo API Contract

## Todo Data Structure
```
{
  "id": integer,
  "description": string,
  "completed": boolean
}
```

## CLI Commands Contract

### Add Todo
- **Command**: `add "description"`
- **Input**: Description string
- **Output**: Success message with assigned ID
- **Error cases**:
  - Empty description → "Error: Description cannot be empty"
  - Invalid input → Appropriate error message

### View Todos
- **Command**: `view`
- **Input**: None
- **Output**: List of all todos in format "ID: [id] - [description] - [completed/Incomplete]"
- **Error cases**: No todos → "No todos found"

### Update Todo
- **Command**: `update <id> "new description"`
- **Input**: ID (integer) and new description (string)
- **Output**: Success message
- **Error cases**:
  - Invalid ID → "Error: Todo with ID [id] not found"
  - Empty description → "Error: Description cannot be empty"
  - Invalid input → Appropriate error message

### Delete Todo
- **Command**: `delete <id>`
- **Input**: ID (integer)
- **Output**: Success message
- **Error cases**:
  - Invalid ID → "Error: Todo with ID [id] not found"
  - Invalid input → Appropriate error message

### Mark Complete
- **Command**: `complete <id>`
- **Input**: ID (integer)
- **Output**: Success message
- **Error cases**:
  - Invalid ID → "Error: Todo with ID [id] not found"
  - Invalid input → Appropriate error message