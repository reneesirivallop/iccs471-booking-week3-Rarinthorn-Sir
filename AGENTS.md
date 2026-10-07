**Project and context:** This prototype is for moving one in-memory meeting-room `Booking`; the main implementation is in `service.py` and uses the existing `models.py`, `rules.py`, and tests.

**Preservation and scope:** From `SPEC.md`, the project validate the target and proposed destination before mutation, ignores cancelled bookings and the target when checking conflicts, and updates the same object in place. Keep the model, creation behavior, public signatures, supplied tests, and fallback examples unchanged; do not add a database, room catalogue, or unrelated workflow.

**Checks:** From the repository root, run `uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student`. This checks existing creation behavior, supplied move behavior, and the two student checks together. If `uv` is unavailable, use the documented Python 3.12 equivalent.

**Review:** Before staging or committing, inspect `git status --short` and `git diff HEAD -- service.py rules.py test_student.py AGENTS.md`. Stop for the user’s decision if an edit would require changing files prohibited by `SPEC.md`, weakening supplied tests, or changing the agreed scope.