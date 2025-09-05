# n8n Workflow Popularity System

Identify the most popular **n8n** workflows across **YouTube**, **n8n Forum (Discourse)**, and **Google Trends** with clear, numeric evidence. API-ready and cron-friendly.

## Features
- YouTube: views, likes, comments + engagement ratios
- Forum: views, likes, replies, contributors + ratios
- Trends: average interest (US/IN)
- Country segmentation: **US** and **IN**
- REST API (FastAPI) to query results
- Automation ready (cron / Task Scheduler / GitHub Actions)

## Quick Start
```bash
git clone https://github.com/<you>/n8n-popularity-system.git
cd n8n-popularity-system
cp .env.example .env  # fill YOUTUBE_API_KEY
pip install -r requirements.txt

# fetch and write JSON
python -m app.fetch_data

# run API
uvicorn app.main:app --reload
# http://127.0.0.1:8000/workflows?platform=YouTube&country=US&sort_by=views&limit=50
