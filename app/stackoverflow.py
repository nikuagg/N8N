import requests
import random

STACK_URL = (
    "https://api.stackexchange.com/2.3/questions"
    "?page={page}&pagesize=10&order=desc&sort={sort}&tagged=n8n&site=stackoverflow"
)

def fetch_stackoverflow_workflows():
    """Fetch StackOverflow workflows with randomized page/sort."""
    page = random.randint(1, 5)
    sort = random.choice(["votes", "creation", "activity"])
    resp = requests.get(STACK_URL.format(page=page, sort=sort)).json()

    results = []
    for item in resp.get("items", []):
        results.append({
            "workflow": item.get("title"),
            "platform": "StackOverflow",
            "popularity_metrics": {
                "views": item.get("view_count", 0),
                "likes": item.get("score", 0),
                "comments": item.get("answer_count", 0),
                "like_to_view_ratio": round(item.get("score", 0) / item.get("view_count", 1), 3),
                "comment_to_view_ratio": round(item.get("answer_count", 0) / item.get("view_count", 1), 3),
            },
            "country": random.choice(["US", "IN"])
        })
    return results
