# System Architecture

## Overview
The system uses a webhook-based integration between GitHub and FastAPI to automate PR handling.

## Components
- **GitHub Repository**: source code and PRs.
- **Webhook**: triggers FastAPI on PR events.
- **FastAPI Server**: processes PR events, logs information, and can trigger automated actions.
- **Optional Database**: store PR history, statuses, and analytics.

## Flow
1. Developer opens a PR on GitHub.
2. GitHub sends a POST request to the FastAPI webhook.
3. FastAPI parses the PR payload and logs details.
4. Optional: FastAPI triggers additional actions (comments, CI/CD, labels).

## Diagram

GitHub PR Events --> Webhook --> FastAPI --> [Database / CI / Notifications]