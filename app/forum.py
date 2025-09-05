import requests

FORUM_URL = "https://community.n8n.io/latest.json"  # Discourse API

def fetch_forum_workflows():
    resp = requests.get(FORUM_URL).json()
    results = []
    for topic in resp.get("topic_list", {}).get("topics", [])[:20]:
        results.append({
            "workflow": topic.get("title"),
            "platform": "Forum",
            "popularity_metrics": {
                "views": topic.get("views", 0),
                "likes": topic.get("like_count", 0),
                "replies": topic.get("posts_count", 0)
            },
            "country": "US"
        })
    return results
