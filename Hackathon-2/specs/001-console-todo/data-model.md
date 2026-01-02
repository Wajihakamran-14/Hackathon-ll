# Data Model: Console Todo App

## Todo Entity

### Attributes
- **id**: Integer - Unique identifier for the todo item
  - Auto-generated when todo is created
  - Sequential numbering starting from 1
  - Required field

- **description**: String - Description of the todo task
  - User-provided text describing the task
  - Required field (cannot be empty)
  - Maximum length: 1000 characters

- **completed**: Boolean - Completion status of the todo
  - Initially set to False when todo is created
  - Can be updated to True when marked as complete
  - Required field

### State Transitions
- **Creation**: `id` assigned, `description` set, `completed` = False
- **Completion**: `completed` changes from False to True
- **Update**: `description` can be modified while preserving `id` and `completed` status

### Validation Rules
- ID must be a positive integer
- Description must not be empty or only whitespace
- Description must not exceed 1000 characters
- Todo must exist before update/delete/complete operations

## Todo Collection

### Structure
- **todos**: List/Array of Todo entities
- Maintained in memory during application runtime
- Provides methods for CRUD operations

### Operations
- **Add**: Append new Todo to the collection
- **Get All**: Return all todos in the collection
- **Get by ID**: Find and return specific todo by ID
- **Update by ID**: Modify existing todo by ID
- **Delete by ID**: Remove specific todo from collection
- **Mark Complete by ID**: Update completion status of specific todo