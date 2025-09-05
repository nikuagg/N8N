🚀 N8N Popularity System

Collect and analyze workflow popularity data from multiple platforms like YouTube, Forum, and StackOverflow, and serve it through a FastAPI-based REST API.

✨ Features

📡 Multi-source workflow collection: YouTube, n8n Forum, StackOverflow

🔄 Automated fetching & merging of results

📂 JSON dataset export (output/*.json)

🔑 API access via FastAPI with auto-generated docs

🏆 Popularity scoring system (views, likes, comments, ratios, etc.)

🌍 Country segmentation (US & India)

⚙️ Setup Instructions
1. Clone the repository
git clone <your-repo-url>
cd n8n-popularity-system
2. Create a virtual environment
python -m venv .venv
# Activate
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables

Copy .env.example → .env and add your keys:

Variable	Description
YOUTUBE_API_KEY	YouTube Data API v3 key (required for YouTube)

Other sources (Forum, StackOverflow) work without API keys.

📡 Fetching Data

Run the data collector:

python -m app.fetch_data


This generates JSON files under output/:

youtube.json

forum.json

stackoverflow.json

all_data.json (merged)

Each run fetches slightly different results (randomized queries) to keep datasets fresh.

🗄 Data Model

Each workflow entry looks like:

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

| Field                | Description                                     |
| -------------------- | ----------------------------------------------- |
| `workflow`           | Title / description of the workflow             |
| `platform`           | Source (YouTube, Forum, StackOverflow)          |
| `popularity_metrics` | Engagement stats (views, likes, comments, etc.) |
| `country`            | Region of origin (US or India)                  |


Workflows are scored per platform using weighted formulas:

| **Source**        | **Formula**                                                           |
| ----------------- | --------------------------------------------------------------------- |
| **YouTube**       | `0.45*views + 0.25*likes + 0.15*comments + 0.15*(like_to_view_ratio)` |
| **Forum**         | `0.4*views + 0.3*likes + 0.3*comments`                                |
| **StackOverflow** | `0.5*score + 0.3*answers + 0.2*views` (simplified for relevance)      |
| **Google Search** | Placeholder = 0 (can be extended later)                               |


🚀 Running the API

Start FastAPI server:

uvicorn app.main:app --reload


API available at:

Swagger UI → http://localhost:8000/docs

Redoc → http://localhost:8000/redoc

🔌 Core API Endpoints

| Endpoint          | Method | Description                               |
| ----------------- | ------ | ----------------------------------------- |
| `/`               | GET    | API metadata & health check               |
| `/workflows`      | GET    | Fetch all stored workflows                |
| `/workflows/{id}` | GET    | Fetch single workflow by ID               |
| `/collect`        | POST   | Trigger new data collection (all sources) |

