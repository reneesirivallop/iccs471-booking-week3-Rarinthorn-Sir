## Identity

- Name: Rarinthorn Sirivallop
- Student ID: 6580229
- AI tool: Copilot SDK in VS Code.
- Discussion partners: None

## Review decision

The room overlap check in `rules.py / has_conflict` works well and covers all requirements. It excludes cancelled bookings, ensures room numbers match, and permits back-to-back reservations using half-open intervals. When moving a booking, validate the new room first and ignore the current booking during the conflict check.

## Checks

- Baseline command: `uv run --python 3.12 python -m unittest -v test_baseline` — 6 tests passed.
- Final suite command: `uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student` — 11 tests passed.
- Baseline commit: `ce156d0` (`Init: starter structure for week 3 exercises`).

## Remaining uncertainty

The tests do not settle which error message should take precedence when a move has multiple invalid inputs at once, such as both a blank room and an invalid interval; the specification permits any applicable rejection.
