# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI(title="n8n Workflow Popularity System")

# Output folder where JSON files are saved
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

@app.get("/workflows")
def get_all_workflows():
    """Return all workflows combined."""
    workflows = load_json("all_data.json")
    return JSONResponse(content=workflows)

@app.get("/workflows/{platform}")
def get_workflows_by_platform(platform: str):
    """Return workflows filtered by platform: youtube or forum."""
    platform = platform.lower()
    if platform not in ["youtube", "forum"]:
        raise HTTPException(status_code=404, detail="Platform not found")
    
    # Load combined data
    all_workflows = load_json("all_data.json")
    filtered = [w for w in all_workflows if w.get("platform", "").lower() == platform]
    return JSONResponse(content=filtered)
