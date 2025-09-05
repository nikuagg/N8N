n8n Popularity System

FastAPI service for collecting, aggregating, and serving popularity data of n8n workflows from multiple public platforms.
Currently supports: YouTube, n8n Forum, StackOverflow.

✨ Features

Multi-source collection: YouTube, Forum, StackOverflow (Google planned)

Automatic merging of results into a single dataset (all_data.json)

Popularity scoring per workflow (views, likes, comments, votes, ratios)

JSON outputs for each source + unified dataset

REST API (FastAPI) to browse, query, and serve results

Environment-based config (.env)

📂 Project Structure
n8n-popularity-system/
│── app/
│   ├── crud.py            # Database operations
│   ├── database.py        # SQLite setup (SQLAlchemy)
│   ├── fetch_data.py      # Orchestrates collection & merging
│   ├── forum.py           # Forum scraper
│   ├── main.py            # FastAPI entrypoint
│   ├── models.py          # SQLAlchemy models
│   ├── stackoverflow.py   # StackOverflow fetcher
│   ├── utils.py           # Helpers
│   ├── youtube.py         # YouTube fetcher
│── output/                # JSON snapshots
│   ├── all_data.json
│   ├── forum.json
│   ├── stackoverflow.json
│   ├── youtube.json
│── .env                   # Local config (ignored in git)
│── .env.example           # Example env config
│── requirements.txt       # Dependencies
│── README.md              # Documentation

⚙️ Setup
1. Clone repo
git clone <your-repo-url>
cd n8n-popularity-system

2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Setup environment variables

Copy .env.example → .env and fill in required values.

cp .env.example .env

🔑 Environment Variables
Variable	Description
YOUTUBE_API_KEY	API key for YouTube Data API (required for live fetching)

(Forum & StackOverflow fetchers run without keys.)

📡 Data Collection

Run the collector:

python -m app.fetch_data


This will fetch fresh data and update JSON files in output/:

youtube.json

forum.json

stackoverflow.json

all_data.json (merged + deduped)

🗄️ Output Format

Each JSON file is a list of workflow entries:

{
  "workflow": "Email Automation with Gmail",
  "platform": "YouTube",
  "country": "Global",
  "evidence": "https://youtube.com/watch?v=XXXX",
  "popularity_score": 87
}


Fields:

workflow → Workflow title

platform → Source platform

country → Country if available, else "Global"

evidence → URL or reference

popularity_score → Computed score

🧮 Scoring

Each source has its own formula:

Source	Formula
YouTube	0.45*views + 0.25*likes + 0.15*comments + 0.15*like_to_view_ratio
Forum	0.4*views + 0.3*likes + 0.3*comments
StackOverflow	Based on votes + answer_count + view_count (weighted)

Final popularity_score is normalized and comparable across sources.

🚀 Running the API

Start the server:

uvicorn app.main:app --reload


Visit:

Swagger UI → http://localhost:8000/docs

ReDoc → http://localhost:8000/redoc

🔌 API Endpoints
Endpoint	Method	Description
/	GET	Health check / metadata
/workflows	GET	Get all workflows (from all_data.json)
/workflows/{platform}	GET	Get workflows from specific platform (youtube, forum, stackoverflow)

Example:

curl http://127.0.0.1:8000/workflows/youtube

✅ Deliverables

Working FastAPI service

Dataset of 50+ workflows across multiple sources (output/all_data.json)

Scoring formulas for each platform

Documentation (this README)

🔮 Next Steps

Add Google Trends as data source

Add Reddit & GitHub collectors

Improve scoring via time-based weighting

Export in CSV / JSONL history