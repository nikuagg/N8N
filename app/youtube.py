import os
import requests

def fetch_youtube_workflows(api_key):
    """Fetch popular n8n workflows from YouTube."""
    workflows = []
    search_queries = [
        "n8n automation",
        "n8n workflow",
        "n8n tutorial",
        "n8n integrations"
    ]
    
    for query in search_queries:
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
                    "views": 0,      # placeholder, can fetch with videos.list
                    "likes": 0,
                    "comments": 0,
                    "like_to_view_ratio": 0,
                    "comment_to_view_ratio": 0
                },
                "country": "US"
            }
            workflows.append(workflow)
    return workflows
