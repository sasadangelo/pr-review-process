# AI-Powered PR Review

This is a minimal MVP for an **AI-powered Pull Request review system**.
It uses **FastAPI** to receive GitHub webhook events and can be connected to an AI model to generate automatic code review comments.

## Features

- Receive GitHub **Pull Request webhook events**
- Filter relevant events (`opened` and `synchronize`)
- Extract key information from the PR:
  - PR number
  - Repository full name
  - Head SHA
- Ready to integrate with AI models for automatic code review
- Logs all PR events in English for easy debugging

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/pr-review-process.git
cd pr-review-process
```

2. Set up virtual environment and Install dependencies

```bash
uv sync
```

3. Start the FastAPI server

```bash
uv run src/app.sh
```

By default, the app runs on http://localhost:8000.

1. Expose your local server with ngrok

```bash
ngrok http 8000
```

Copy the HTTPS URL provided by ngrok to use as your GitHub webhook URL.

Example:

https://abc123.ngrok-free.app/github/webhook


6. Configure GitHub Webhook
Go to your repository: Settings → Webhooks → Add webhook

Payload URL: https://<ngrok-hostname>/github/webhook

Content type: application/json

Events: select Pull requests

Save

Now your FastAPI app will receive PR events from GitHub.

7. How to Test
Using GitHub
Open or update a PR

Check the terminal where FastAPI runs for logs:

=== GitHub Pull Request Event ===
Action: opened
Repository: sasadangelo/pr-review-process
PR Number: 12
Head SHA: abc123def456
===============================

Using curl
curl -X POST https://<ngrok-hostname>/github/webhook \
     -H "Content-Type: application/json" \
     -d '{"action":"opened","number":1,"repository":{"full_name":"sasadangelo/pr-review-process"},"pull_request":{"head":{"sha":"abc123"}}}'

8. Next Steps (MVP)
Fetch the full diff of the PR using GitHub API

Load internal knowledge from .ai/ folder

Build prompt for AI model

Generate automatic code review comments and post them back to GitHub

9. Project Structure
pr-review-process/
├─ src/
│  └─ app.py          # FastAPI webhook
├─ .ai/               # Knowledge base for AI
├─ app.sh             # Script to start the server
├─ pyproject.toml     # Project dependencies and dev tools
└─ README.md

10. Dependencies
Python >= 3.10

FastAPI

Uvicorn

Requests

Pre-commit hooks (black, isort, flake8, etc.)

11. License
MIT License
