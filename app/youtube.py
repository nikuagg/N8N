import os
import requests
import random

def fetch_youtube_workflows(api_key):
    """Fetch popular n8n workflows from YouTube with query rotation."""
    workflows = []
    search_queries = [
        "n8n automation",
        "n8n workflow",
        "n8n tutorial",
        "n8n integrations",
        "n8n zapier alternative",
        "n8n examples",
        "n8n productivity",
        "n8n business automation"
    ]

    # Pick 2 random queries per run
    queries = random.sample(search_queries, k=2)

    for query in queries:
        url = (
            "https://www.googleapis.com/youtube/v3/search"
            f"?part=snippet&q={query}&type=video&maxResults=10&key={api_key}"
        )
        response = requests.get(url)
        if response.status_code != 200:
            print(f"❌ YouTube fetch failed for '{query}': {response.status_code}")
            continue

        data = response.json()
        for item in data.get("items", []):
            snippet = item["snippet"]
            workflow = {
                "workflow": snippet["title"],
                "platform": "YouTube",
                "popularity_metrics": {
                    "views": 0,
                    "likes": 0,
                    "comments": 0,
                    "like_to_view_ratio": 0,
                    "comment_to_view_ratio": 0
                },
                "country": random.choice(["US", "IN"])  # simple random country split
            }
            workflows.append(workflow)

    return workflows
