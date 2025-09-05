# 📊 N8N POPULARITY SYSTEM

FastAPI service that **collects, scores, and serves popularity signals** for n8n workflows across multiple platforms: **YouTube, Forum, and StackOverflow**.  

---

# ✨ FEATURES

- 📡 Multi-source workflow collection: **YouTube**, **n8n Forum**, **StackOverflow**  
- 🔄 Automated fetching & merging of results  
- 📂 JSON dataset export (`output/*.json`)  
- 🔑 API access via **FastAPI** with auto-generated docs  
- 🏆 Popularity scoring system (views, likes, comments, ratios, etc.)  
- 🌍 Country segmentation (**US** & **India**)  

---

# 📦 DATA MODEL

Each workflow entry is represented as:

json
{
  "workflow": "Google Sheets → Slack Automation",
  "platform": "YouTube",
  "popularity_metrics": {
    "views": 12500,
    "likes": 630,
    "comments": 88,
    "like_to_view_ratio": 0.05,
    "comment_to_view_ratio": 0.007
  },
  "country": "US"
}
| Field                | Description                                       |
| -------------------- | ------------------------------------------------- |
| `workflow`           | Workflow title / description                      |
| `platform`           | Source platform (YouTube, Forum, StackOverflow)   |
| `popularity_metrics` | Engagement stats (views, likes, comments, ratios) |
| `country`            | Region (US or India)                              |


🧮 SCORING
| Source            | Formula                                                             |
| ----------------- | ------------------------------------------------------------------- |
| **YouTube**       | `0.45*views + 0.25*likes + 0.15*comments + 0.15*like_to_view_ratio` |
| **Forum**         | `0.4*views + 0.3*likes + 0.3*comments`                              |
| **StackOverflow** | `0.5*score + 0.3*answers + 0.2*views`                               |

⚙️ QUICK START
bash
Copy code
# Clone repository
git clone <your-repo-url>
cd n8n-popularity-system

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
🔑 ENVIRONMENT VARIABLES

| Variable          | Purpose                                      |
| ----------------- | -------------------------------------------- |
| `YOUTUBE_API_KEY` | Required for fetching live YouTube workflows |

📡 COLLECTING DATA
Run the collector:

bash
Copy code
python -m app.fetch_data
This saves snapshots to output/:

youtube.json

forum.json

stackoverflow.json

all_data.json

🔌 API ENDPOINTS
Start the API server:

bash
Copy code
uvicorn app.main:app --reload
Available at → http://127.0.0.1:8000

| Endpoint                | Method | Description                                                       |
| ----------------------- | ------ | ----------------------------------------------------------------- |
| `/`                     | GET    | Health check / metadata                                           |
| `/workflows`            | GET    | Fetch all workflows (from `all_data.json`)                        |
| `/workflows/{platform}` | GET    | Fetch workflows by platform (`youtube`, `forum`, `stackoverflow`) |


📜 API USAGE EXAMPLES
✅ Get all workflows
bash
Copy code
curl http://127.0.0.1:8000/workflows
✅ Get YouTube workflows only
bash
Copy code
curl http://127.0.0.1:8000/workflows/youtube
✅ Sample Response
json
Copy code
[
  {
    "workflow": "Email Automation with Gmail",
    "platform": "YouTube",
    "popularity_metrics": {
      "views": 8400,
      "likes": 560,
      "comments": 77,
      "like_to_view_ratio": 0.066,
      "comment_to_view_ratio": 0.009
    },
    "country": "India"
  }
]
🏆 EVALUATION CRITERIA
Aspect	Explanation
Data Richness	Workflows backed by metrics and evidence
Production Readiness	API + code deployable on day one
Automation	Collector runs without manual intervention
Creativity	Multiple sources, deduplication, scoring
Completeness	At least 50 workflows across sources and countries

✅ DELIVERABLES
Working FastAPI API

Dataset of 50+ workflows (output/all_data.json)

Documentation of setup, scoring, and API usage (this README)

pgsql
Copy code
