from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/github/webhook")
async def github_webhook(req: Request):
    try:
        payload = await req.json()
    except Exception:
        return JSONResponse({"error": "Invalid JSON received"}, status_code=400)

    action = payload.get("action")
    if action not in ["opened", "synchronize"]:
        # Ignore non-relevant PR events
        return {"ok": True}

    # Extract key PR information
    pr_number = payload.get("number")
    repo_full_name = payload.get("repository", {}).get("full_name")
    head_sha = payload.get("pull_request", {}).get("head", {}).get("sha")

    # Log the event in English
    print("=== GitHub Pull Request Event ===")
    print(f"Action: {action}")
    print(f"Repository: {repo_full_name}")
    print(f"PR Number: {pr_number}")
    print(f"Head SHA: {head_sha}")
    print("===============================")

    # Here you can add the call to your AI / diff processor

    return {"ok": True}
