# Tasks: Calculator CLI Core (Python)

**Input**: Design documents from `specs/001-calc-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included in the task list as they are necessary for verifying core arithmetic accuracy and error handling as per the specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

**Mandatory Review**: After completing each phase, implementation MUST pause for human review. Proceed to the next phase only after receiving explicit approval.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in `src/` and `tests/`
- [X] T002 Initialize project with `uv init` and add `pytest` as a development dependency
- [X] T003 [P] Configure `ruff` for linting and formatting in `pyproject.toml`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Setup basic logging infrastructure in `src/utils/logger.py`
- [X] T005 [P] Setup package initializers in `src/calculator/__init__.py` and `src/utils/__init__.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: Enter simple arithmetic expressions and see results with dynamic precision and correct precedence.

**Independent Test**: Run `main.py`, type `5 + 3`, and verify output is `8`. Type `1 / 3` and verify output is `0.3333333333`.

### Tests for User Story 1

- [X] T006 [P] [US1] Create unit tests for basic arithmetic (+, -, *, /) in `tests/unit/test_evaluator.py`
- [X] T007 [P] [US1] Create unit tests for expression parsing (including precedence) in `tests/unit/test_parser.py`

### Implementation for User Story 1

- [X] T008 [US1] Implement AST-based expression parser in `src/calculator/parser.py`
- [X] T009 [US1] Implement arithmetic evaluator using `decimal` for high precision in `src/calculator/evaluator.py`
- [X] T010 [US1] Implement dynamic result formatting (integer for whole numbers, up to 10 decimals for fractions) in `src/calculator/evaluator.py`
- [X] T011 [US1] Implement REPL loop with `calc > ` prompt in `src/main.py`
- [X] T012 [US1] Implement support for negative number prefixes in `src/calculator/parser.py`
- [X] T013 [US1] Implement `exit`, `quit`, and `clear` commands in `src/main.py`
- [X] T014 [US1] Create integration tests for core CLI flow in `tests/integration/test_cli.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Robust Error Handling (Priority: P1)

**Goal**: Handle division by zero and syntax errors gracefully without crashing.

**Independent Test**: Run `main.py`, type `10 / 0`, and verify output is `Error: Division by zero`. Type `5 ++ 3` and verify output is `Error: Invalid syntax`.

### Tests for User Story 2

- [X] T015 [P] [US2] Create error case unit tests for division by zero in `tests/unit/test_evaluator.py`
- [X] T016 [P] [US2] Create unit tests for invalid syntax scenarios in `tests/unit/test_parser.py`

### Implementation for User Story 2

- [X] T017 [US2] Implement division by zero protection in `src/calculator/evaluator.py`
- [X] T018 [US2] Implement syntax error detection and handling in `src/calculator/parser.py`
- [X] T019 [US2] Implement error message display logic in `src/main.py`
- [X] T020 [US2] Create integration tests for error scenarios in `tests/integration/test_cli.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Code Maintainability (Priority: P2)

**Goal**: Ensure code is clean, PEP 8 compliant, and well-documented with docstrings and comments.

**Independent Test**: Run `ruff check src/` and verify zero errors/warnings. Verify docstrings in all source files.

### Implementation for User Story 3

- [X] T021 [US3] Add descriptive docstrings and inline comments to all core functions in `src/`
- [X] T022 [P] [US3] Run final formatting and linting check with `ruff` on all source and test files

**Checkpoint**: All user stories should now be independently functional and meet quality standards.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final documentation and validation

- [X] T023 [P] Update `README.md` with usage instructions and technical stack details
- [X] T024 Final validation of all scenarios defined in `specs/001-calc-cli/quickstart.md`
- [X] T025 [P] Run `pytest` to confirm 100% pass rate for all unit and integration tests

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - starts the project
- **Foundational (Phase 2)**: Depends on Phase 1 completion - BLOCKS implementation
- **User Stories (Phase 3-5)**: All depend on Foundational completion
  - US1 (Arithmetic) is the highest priority (P1) and should be completed first as the MVP core
  - US2 (Error Handling) is also P1 and can be worked on after US1 core is stable
  - US3 (Maintainability) is P2 and can be finalized after functional logic is complete
- **Polish (Phase 6)**: Final validation after all stories are implemented

### Parallel Opportunities

- T003 (Ruff config) can run in parallel with project initialization
- T005 (Initializers) can run in parallel with logger setup
- T006 and T007 (Tests for US1) can run in parallel
- T015 and T016 (Tests for US2) can run in parallel
- Unit tests can generally be written in parallel with or before implementation tasks

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 & 2 (Setup & Foundational)
2. Complete Phase 3 (User Story 1 - Basic Arithmetic)
3. **STOP and VALIDATE**: Verify that the REPL works for basic expressions with dynamic precision.

### Incremental Delivery

1. Foundation ready (Phase 1 & 2)
2. Add Basic Arithmetic (Phase 3) -> MVP functional
3. Add Error Handling (Phase 4) -> Robustness improved
4. Add Maintainability (Phase 5) -> Code quality verified
5. Final Polish (Phase 6) -> Delivery ready
