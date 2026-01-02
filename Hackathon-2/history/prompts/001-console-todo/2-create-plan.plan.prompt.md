---
id: 2
title: Create Plan
stage: plan
date: 2026-01-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-console-todo
branch: 001-console-todo
user: Claude Code
command: sp.plan
labels: [planning, architecture, todo-app]
links:
  spec: specs/001-console-todo/spec.md
  plan: specs/001-console-todo/plan.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-console-todo/plan.md
 - specs/001-console-todo/research.md
 - specs/001-console-todo/data-model.md
 - specs/001-console-todo/quickstart.md
 - specs/001-console-todo/contracts/todo-api-contract.md
tests:
 - none
---

## Prompt

```text
In-Memory Console Todo App (Phase I)

Scope:
Implement Phase I only: an in-memory, console-based Todo application.
All work must be contained inside the `Hackathon-ll-phase-l/` directory.

Development workflow:
- Follow agentic dev flow strictly:
  spec → plan → tasks → implementation

Project setup:
- Create root directory: `Hackathon-ll-phase-l/`
- Initialize Python project using UV
- Target runtime: Python 3.13+

Implementation steps:
1. Project scaffolding
   - Set up clean Python project structure inside `Hackathon-ll-phase-l/`
   - Separate modules for:
     - Data model
     - Business logic
     - CLI interface

2. Core todo model
   - Define in-memory todo representation
   - Include: ID, description, completion status

3. Todo operations
   - Implement functions for:
     - Add todo
     - View todos
     - Update todo
     - Delete todo
     - Mark todo as complete

4. CLI interface
   - Implement menu- or command-based interaction
   - Route user input to business logic
   - Validate input and handle errors gracefully

5. Integration & validation
   - Connect CLI with todo operations
   - Manually test all five features via console
   - Verify no persistence beyond runtime

Completion criteria:
- Application runs from terminal
- All required features function correctly
- No files or databases used
- Code is clean, modular, and readable
- All content resides within `Hackathon-ll-phase-l/`

Out of scope:
- Web or GUI interface
- Persistence
- AI or agent integration
- Phase II+ features
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/bash/setup-plan.sh --json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/bash/update-agent-context.sh claude`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.

## Response snapshot

Completed the implementation plan for the In-Memory Console Todo App with the following artifacts:

1. **Implementation Plan**: specs/001-console-todo/plan.md
   - Technical context with Python 3.13+, in-memory storage, pytest testing
   - Constitution check showing all principles are satisfied
   - Detailed project structure with clean architecture

2. **Research Document**: specs/001-console-todo/research.md
   - Project structure decisions and rationale
   - In-memory storage approach
   - CLI interface strategy
   - Error handling approach

3. **Data Model**: specs/001-console-todo/data-model.md
   - Todo entity with id, description, and completion status
   - Validation rules and state transitions
   - Todo collection operations

4. **Quickstart Guide**: specs/001-console-todo/quickstart.md
   - Setup instructions with UV package manager
   - Project directory structure
   - Running and testing instructions
   - Available CLI commands

5. **API Contract**: specs/001-console-todo/contracts/todo-api-contract.md
   - Todo data structure definition
   - CLI commands contract with inputs, outputs, and error cases

6. **Agent Context**: Updated CLAUDE.md with project technologies

All planning artifacts are complete and follow the spec-driven development approach. The plan satisfies all constitution principles and is ready for the tasks phase.

## Outcome

- ✅ Impact: Created comprehensive implementation plan with all required artifacts
- 🧪 Tests: none
- 📁 Files: plan.md, research.md, data-model.md, quickstart.md, contracts/todo-api-contract.md
- 🔁 Next prompts: Proceed to tasks phase with /sp.tasks
- 🧠 Reflection: Plan follows clean architecture and meets all specification requirements

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A