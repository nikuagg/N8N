import json
import os

def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_json(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def dedupe_workflows(existing, new):
    seen = {w["workflow"]: w for w in existing}
    for w in new:
        if w["workflow"] not in seen:
            seen[w["workflow"]] = w
    return list(seen.values())
