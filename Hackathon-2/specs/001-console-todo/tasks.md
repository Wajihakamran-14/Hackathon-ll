# Implementation Tasks: Console Todo App

**Feature**: Console Todo App
**Branch**: 001-console-todo
**Created**: 2026-01-02
**Input**: specs/001-console-todo/spec.md, plan.md, data-model.md, contracts/

## Implementation Strategy

**MVP First**: Implement User Story 1 (Add Todo) as the minimum viable product, then incrementally add other features.

**Incremental Delivery**: Complete each user story independently, ensuring it can be tested and demonstrated separately.

**Parallel Opportunities**: Models, services, and CLI components can be developed in parallel after foundational setup.

## Dependencies

- **User Story 2 (View Todos)** requires User Story 1 (Add Todo) functionality to have data to view
- **User Stories 3-5** (Update, Delete, Complete) require the Todo model and service layer from User Story 1
- **CLI interface** requires all underlying services to be implemented first

## Parallel Execution Examples

- **User Story 1**: Can be developed independently with its own tests
- **User Story 2**: Can be developed in parallel with User Story 1 after model is established
- **User Stories 3-5**: Can be developed in parallel after User Story 1 foundation is complete

---

## Phase 1: Setup

**Goal**: Initialize project structure and dependencies

- [X] T001 Create project directory Hackathon-ll-phase-l/
- [X] T002 Initialize Python project with UV in Hackathon-ll-phase-l/
- [X] T003 Create project structure per implementation plan: src/todo_app/{models,services,cli,utils} and tests/{test_models,test_services,test_cli}
- [X] T004 Create pyproject.toml with Python 3.13+ requirement and pytest dependency
- [X] T005 Create README.md with project description
- [X] T006 Create __init__.py files in all directories
- [X] T007 Create .env.example file

## Phase 2: Foundational

**Goal**: Establish core architecture and shared components

- [X] T008 [P] Create Todo model in src/todo_app/models/todo.py with id, description, completed attributes
- [X] T009 [P] Create TodoService in src/todo_app/services/todo_service.py with in-memory storage
- [X] T010 [P] Create validators module in src/todo_app/utils/validators.py for input validation
- [X] T011 Create base test structure with conftest.py
- [X] T012 Create basic CLI framework in src/todo_app/cli/cli.py

## Phase 3: User Story 1 - Add Todo Item (Priority: P1)

**Goal**: Implement functionality to add new todo items with unique IDs and default incomplete status

**Independent Test Criteria**:
- Can add a new todo and verify it appears in the list with correct status and ID
- Invalid inputs (empty descriptions) are handled gracefully

**Tasks**:

- [X] T013 [US1] Implement Todo model validation for description (not empty, max 1000 chars)
- [X] T014 [US1] Implement TodoService.add_todo() method with auto ID assignment
- [X] T015 [US1] Implement validator for todo description validation
- [X] T016 [US1] Create CLI command handler for 'add' command
- [X] T017 [US1] Implement error handling for empty description in add command
- [X] T018 [US1] Add success message output for todo creation with assigned ID
- [X] T019 [US1] Create unit tests for Todo model validation
- [X] T020 [US1] Create unit tests for TodoService.add_todo() method
- [X] T021 [US1] Create integration tests for add command functionality
- [X] T022 [US1] Test acceptance scenario: Add todo with description creates item with unique ID and incomplete status
- [X] T023 [US1] Test acceptance scenario: Add todo with empty description shows error message

## Phase 4: User Story 2 - View All Todos (Priority: P1)

**Goal**: Implement functionality to display all todos with their IDs, descriptions, and completion status

**Independent Test Criteria**:
- Can add some todos and then view the complete list to verify all items are displayed correctly
- Shows appropriate message when no todos exist

**Tasks**:

- [X] T024 [US2] Implement TodoService.get_all_todos() method
- [X] T025 [US2] Implement TodoService.get_todo_by_id() method
- [X] T026 [US2] Create CLI command handler for 'view' command
- [X] T027 [US2] Format output to show "ID: [id] - [description] - [completed/Incomplete]"
- [X] T028 [US2] Handle case when no todos exist (show appropriate message)
- [X] T029 [US2] Create unit tests for get_all_todos method
- [X] T030 [US2] Create unit tests for get_todo_by_id method
- [X] T031 [US2] Create integration tests for view command functionality
- [X] T032 [US2] Test acceptance scenario: View command shows all todos with ID, description, and status
- [X] T033 [US2] Test acceptance scenario: View command with no todos shows appropriate message

## Phase 5: User Story 3 - Mark Todo as Complete (Priority: P2)

**Goal**: Implement functionality to mark a specific todo as complete by its ID

**Independent Test Criteria**:
- Can mark a todo as complete and then view the list to confirm the status change
- Invalid IDs are handled gracefully

**Tasks**:

- [X] T034 [US3] Implement TodoService.mark_complete() method
- [X] T035 [US3] Add validation to ensure todo exists before marking complete
- [X] T036 [US3] Create CLI command handler for 'complete <id>' command
- [X] T037 [US3] Implement error handling for invalid todo IDs
- [X] T038 [US3] Add success message output when todo is marked complete
- [X] T039 [US3] Create unit tests for mark_complete method
- [X] T040 [US3] Create integration tests for complete command functionality
- [X] T041 [US3] Test acceptance scenario: Complete command with valid ID changes todo status to complete
- [X] T042 [US3] Test acceptance scenario: Complete command with invalid ID shows error message

## Phase 6: User Story 4 - Update Todo Description (Priority: P3)

**Goal**: Implement functionality to update the description of an existing todo by its ID

**Independent Test Criteria**:
- Can update a todo description and then view the list to confirm the change
- Invalid IDs and empty descriptions are handled gracefully

**Tasks**:

- [X] T043 [US4] Implement TodoService.update_todo() method
- [X] T044 [US4] Add validation to ensure todo exists before updating
- [X] T045 [US4] Add validation to ensure new description is not empty
- [X] T046 [US4] Create CLI command handler for 'update <id> "new description"' command
- [X] T047 [US4] Implement error handling for invalid todo IDs
- [X] T048 [US4] Implement error handling for empty new descriptions
- [X] T049 [US4] Add success message output when todo is updated
- [X] T050 [US4] Create unit tests for update_todo method
- [X] T051 [US4] Create integration tests for update command functionality
- [X] T052 [US4] Test acceptance scenario: Update command with valid ID and description changes todo description
- [X] T053 [US4] Test acceptance scenario: Update command with invalid ID shows error message

## Phase 7: User Story 5 - Delete Todo Item (Priority: P3)

**Goal**: Implement functionality to remove a todo item from the list by its ID

**Independent Test Criteria**:
- Can delete a todo and then view the list to confirm it's no longer present
- Invalid IDs are handled gracefully

**Tasks**:

- [X] T054 [US5] Implement TodoService.delete_todo() method
- [X] T055 [US5] Add validation to ensure todo exists before deletion
- [X] T056 [US5] Create CLI command handler for 'delete <id>' command
- [X] T057 [US5] Implement error handling for invalid todo IDs
- [X] T058 [US5] Add success message output when todo is deleted
- [X] T059 [US5] Create unit tests for delete_todo method
- [X] T060 [US5] Create integration tests for delete command functionality
- [X] T061 [US5] Test acceptance scenario: Delete command with valid ID removes todo from list
- [X] T062 [US5] Test acceptance scenario: Delete command with invalid ID shows error message

## Phase 8: Polish & Cross-Cutting Concerns

**Goal**: Complete CLI interface, error handling, and final integration

- [X] T063 Implement main CLI loop with command parsing for all commands
- [X] T064 Add graceful error handling for all invalid user inputs
- [X] T065 Implement command help functionality
- [X] T066 Add quit/exit command to the CLI
- [X] T067 Create comprehensive integration tests for all CLI commands working together
- [X] T068 Test all edge cases: invalid commands, non-numeric IDs, very long descriptions
- [X] T069 Update README.md with usage instructions
- [X] T070 Run complete end-to-end tests for all 5 core features
- [X] T071 Verify application runs successfully on Python 3.13+ without runtime errors
- [X] T072 Verify all invalid inputs are handled gracefully with appropriate error messages
- [X] T073 Final integration test: Add, view, update, delete, and mark todos to verify complete functionality