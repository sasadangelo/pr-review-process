# Project Conventions

## Git & GitHub
- Branch naming: `feature/<name>`, `bugfix/<name>`, `hotfix/<name>`
- Commit messages: `type(scope): short description`
  - Example: `feat(api): add webhook validation`
- PR title: `<Type>: <Brief Description>` (Type = feat, fix, docs, chore)

## Code Style
- Python: follow PEP8 and Black formatting.
- Docstrings for all public functions/classes.
- Logging for all webhook events.

## Reviews
- Every PR must have at least one reviewer.
- No PR merge without passing CI/CD checks.
