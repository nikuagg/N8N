from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json
import os

from app.scheduler import start_scheduler   # ⬅️ NEW

app = FastAPI(title="n8n Workflow Popularity System")

# Output folder
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../output")

def load_json(filename):
    """Load JSON file safely."""
    path = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

@app.on_event("startup")
def startup_event():
    """Start background scheduler when API boots."""
    start_scheduler()

@app.get("/workflows")
def get_all_workflows():
    """Return all workflows combined."""
    workflows = load_json("all_data.json")
    return JSONResponse(content=workflows)

@app.get("/workflows/{platform}")
def get_workflows_by_platform(platform: str):
    """Return workflows filtered by platform."""
    platform = platform.lower()
    all_workflows = load_json("all_data.json")

    # Dynamically detect platforms
    available_platforms = {w.get("platform", "").lower() for w in all_workflows}
    if platform not in available_platforms:
        raise HTTPException(
            status_code=404,
            detail=f"Platform not found. Available: {', '.join(sorted(available_platforms))}"
        )

    filtered = [w for w in all_workflows if w.get("platform", "").lower() == platform]
    return JSONResponse(content=filtered)
