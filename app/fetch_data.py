import os
import json
from dotenv import load_dotenv

from app.youtube import fetch_youtube_workflows
from app.forum import fetch_forum_workflows

# Load environment variables
load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_json(data, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"💾 Saved {len(data)} → {path}")

def load_json(filename):
    path = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def merge_workflows(existing, new):
    # Merge and remove duplicates based on workflow name + platform
    combined = {f"{w['workflow']}_{w['platform']}": w for w in existing}
    for w in new:
        key = f"{w['workflow']}_{w['platform']}"
        combined[key] = w
    return list(combined.values())

def main():
    all_workflows = []

    # Load existing YouTube + Forum workflows
    existing_youtube = load_json("youtube.json")
    existing_forum = load_json("forum.json")

    # Fetch YouTube workflows
    if YOUTUBE_API_KEY:
        youtube_data = fetch_youtube_workflows(YOUTUBE_API_KEY)
        youtube_merged = merge_workflows(existing_youtube, youtube_data)
        save_json(youtube_merged, "youtube.json")
        all_workflows.extend(youtube_merged)
    else:
        print("❌ Missing YOUTUBE_API_KEY, skipping YouTube fetch.")

    # Fetch Forum workflows
    forum_data = fetch_forum_workflows()
    forum_merged = merge_workflows(existing_forum, forum_data)
    save_json(forum_merged, "forum.json")
    all_workflows.extend(forum_merged)

    # Save combined data
    save_json(all_workflows, "all_data.json")
    print("🎉 All workflows saved to output/")

if __name__ == "__main__":
    main()
