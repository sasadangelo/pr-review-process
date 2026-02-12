# Domain Model

## Concepts
- **Pull Request (PR)**: a proposed code change, includes metadata like author, title, branch, additions/deletions.
- **User**: contributor to the repository, can open PRs or review them.
- **Webhook Event**: JSON payload from GitHub describing an action on the repository.
- **FastAPI Handler**: server endpoint receiving webhook events and performing business logic.

## Relationships
- Each PR is associated with a repository and a user.
- PR events trigger actions in the FastAPI handler.
