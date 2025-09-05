import os
import json
from dotenv import load_dotenv

from app.youtube import fetch_youtube_workflows
from app.forum import fetch_forum_workflows
from app.stackoverflow import fetch_stackoverflow_workflows

# Load environment variables
load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_json(data, filename):
    """Save data as JSON to the output directory."""
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"💾 Saved {len(data)} → {path}")


def load_json(filename):
    """Load JSON if exists, else return empty list."""
    path = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"⚠️ Failed to parse {filename}, returning empty list.")
                return []
    return []


def merge_workflows(existing, new):
    """
    Merge workflows from existing + new, deduplicate by workflow+platform,
    and skip invalid entries gracefully.
    """
    combined = {}

    def add_valid(workflows, source):
        for w in workflows:
            if "workflow" in w and "platform" in w:
                key = f"{w['workflow']}_{w['platform']}"
                combined[key] = w
            else:
                print(f"⚠️ Skipping invalid entry from {source}: {w}")

    add_valid(existing, "existing")
    add_valid(new, "new")

    return list(combined.values())


def main():
    all_workflows = []

    # --- YouTube ---
    existing_youtube = load_json("youtube.json")
    if YOUTUBE_API_KEY:
        youtube_data = fetch_youtube_workflows(YOUTUBE_API_KEY)
        youtube_merged = merge_workflows(existing_youtube, youtube_data)
        save_json(youtube_merged, "youtube.json")
        all_workflows.extend(youtube_merged)
    else:
        print("❌ Missing YOUTUBE_API_KEY, skipping YouTube fetch.")

    # --- Forum ---
    existing_forum = load_json("forum.json")
    forum_data = fetch_forum_workflows()
    forum_merged = merge_workflows(existing_forum, forum_data)
    save_json(forum_merged, "forum.json")
    all_workflows.extend(forum_merged)

    # --- Stack Overflow ---
    existing_stack = load_json("stackoverflow.json")
    stack_data = fetch_stackoverflow_workflows()
    stack_merged = merge_workflows(existing_stack, stack_data)
    save_json(stack_merged, "stackoverflow.json")
    all_workflows.extend(stack_merged)

    # --- Combined data ---
    save_json(all_workflows, "all_data.json")
    print("🎉 All workflows saved to output/")


if __name__ == "__main__":
    main()
