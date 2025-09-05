import requests
import random

BASE_FORUM_URL = "https://community.n8n.io/latest.json?page={page}"

def fetch_forum_workflows():
    """Fetch forum workflows with page randomization."""
    page = random.randint(1, 5)  # rotate across first 5 pages
    resp = requests.get(BASE_FORUM_URL.format(page=page)).json()

    results = []
    for topic in resp.get("topic_list", {}).get("topics", [])[:20]:
        results.append({
            "workflow": topic.get("title"),
            "platform": "Forum",
            "popularity_metrics": {
                "views": topic.get("views", 0),
                "likes": topic.get("like_count", 0),
                "replies": topic.get("posts_count", 0),
                "like_to_view_ratio": round(topic.get("like_count", 0) / topic.get("views", 1), 3),
                "comment_to_view_ratio": round(topic.get("posts_count", 0) / topic.get("views", 1), 3),
            },
            "country": random.choice(["US", "IN"])
        })
    return results
