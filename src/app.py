from fastapi import FastAPI, Request
import json
from urllib.parse import parse_qs

app = FastAPI()


@app.post("/github/webhook")
async def github_webhook(req: Request):
    content_type = req.headers.get("Content-Type", "")
    body = await req.body()

    if "application/json" in content_type:
        payload = await req.json()
    elif "application/x-www-form-urlencoded" in content_type:

        body_str = body.decode("utf-8")
        form = parse_qs(body_str)
        payload = json.loads(form["payload"][0])
    else:
        return {"error": "Unsupported content type"}

    event_type = req.headers.get("X-GitHub-Event")
    action = payload.get("action")
    print(f"Event type: {event_type}, action: {action}")

    if event_type == "pull_request":
        pr = payload.get("pull_request", {})
        pr_number = pr.get("number")
        pr_title = pr.get("title")
        pr_url = pr.get("html_url")
        pr_user = pr.get("user", {}).get("login")
        pr_branch_head = pr.get("head", {}).get("ref")
        pr_branch_base = pr.get("base", {}).get("ref")
        pr_additions = pr.get("additions")
        pr_deletions = pr.get("deletions")
        pr_changed_files = pr.get("changed_files")

        print(f"PR #{pr_number} opened by {pr_user}")
        print(f"Title: {pr_title}")
        print(f"URL: {pr_url}")
        print(f"Branches: {pr_branch_head} → {pr_branch_base}")
        print(f"Changes: +{pr_additions}/-{pr_deletions} in {pr_changed_files} files")

    return {"ok": True}
