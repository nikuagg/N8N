# 🚀 N8N POPULARITY SYSTEM

**FastAPI service that collects, scores, and serves popularity signals for n8n workflows** across three public platforms: **YouTube**, **n8n Forum**, and **StackOverflow**.

---

## ✨ FEATURES

- **Multi-source collection**: YouTube, n8n Forum, StackOverflow  
- **Deduplication** across sources and stable IDs  
- **Popularity scoring** with per-source formulas and normalized rankings  
- **JSON snapshots** per-source + unified `all_data.json`  
- **FastAPI** endpoints (Swagger UI & ReDoc) to browse/query data  
- **Country segmentation** (US & India) where available

---

## 📦 DATA MODEL

Each workflow entry follows this schema (JSON sample):

```json
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
  "country": "US",
  "evidence": "https://youtube.com/watch?v=XXXX",
  "collected_at": "2025-09-02T10:30:00Z"
}
```

| Field                | Type    | Description |
|----------------------|---------|-------------|
| `workflow`           | string  | Workflow title / short description |
| `platform`           | string  | Source: `YouTube`, `Forum`, `StackOverflow` |
| `popularity_metrics` | object  | `{ views, likes, comments, ratios }` |
| `country`            | string  | Country code (US / IN) or `Global` |
| `evidence`           | string  | URL or reference backing the entry |
| `collected_at`       | string  | ISO8601 timestamp of collection |

---

## 🧮 SCORING (per-source formulas)

The scoring below is applied per-entry and optionally normalized across sources for unified rankings.

| Source           | Scoring formula (raw) |
|------------------|------------------------|
| **YouTube**      | `0.45*views + 0.25*likes + 0.15*comments + 0.15*like_to_view_ratio` |
| **Forum**        | `0.4*views + 0.3*likes + 0.3*comments` |
| **StackOverflow**| `0.5*score + 0.3*answers + 0.2*views` |

> **Notes:**  
> - Ratios (`like_to_view_ratio`, `comment_to_view_ratio`) are stored for transparency and used in scoring where supported.  
> - Final `popularity_score` is normalized to a [0..100] scale for cross-platform comparability.

---

## ⚙️ QUICK START (one-shot copy)

```bash
# 1. Clone
git clone <your-repo-url>
cd n8n-popularity-system

# 2. Virtual env
python -m venv .venv
# activate:
# Mac/Linux: source .venv/bin/activate
# Windows   : .venv\Scripts\activate

# 3. Install deps
pip install -r requirements.txt

# 4. Configure
cp .env.example .env
# Edit .env to add YOUTUBE_API_KEY if you want live YouTube data

# 5. Run the collector
python -m app.fetch_data

# 6. Run the API
uvicorn app.main:app --reload
# Open http://127.0.0.1:8000/docs
```

---

## 🔑 ENVIRONMENT VARIABLES (essential)

| Variable | Default | Purpose |
|---------:|:-------:|---------|
| `YOUTUBE_API_KEY` | _unset_ | YouTube Data API v3 key (optional; required for live YouTube fetch) |
| `RUN_MODE` | `demo` | `demo` or `live` (demo works without API keys) |

---

## 📡 COLLECTING DATA

Run:

```bash
python -m app.fetch_data
```

Outputs written to `output/` (atomic writes):

- `youtube.json` — YouTube snapshot  
- `forum.json` — Forum snapshot  
- `stackoverflow.json` — StackOverflow snapshot  
- `all_data.json` — merged + deduped dataset

---

## 🔌 API ENDPOINTS & USAGE

Start server:

```bash
uvicorn app.main:app --reload
```

Base: `http://127.0.0.1:8000`

| Endpoint | Method | Description |
|---------:|:------:|------------|
| `/` | GET | Health & metadata |
| `/workflows` | GET | All workflows (reads `all_data.json`) |
| `/workflows/{platform}` | GET | Workflows for `youtube`, `forum`, or `stackoverflow` |

### Examples

- Get all workflows:

```bash
curl http://127.0.0.1:8000/workflows
```

- Get only YouTube workflows:

```bash
curl http://127.0.0.1:8000/workflows/youtube
```

Sample response (truncated):

```json
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
    "country": "India",
    "evidence": "https://www.youtube.com/watch?v=...",
    "collected_at": "2025-09-02T10:30:00Z"
  }
]
```

---

## ⏰ Auto Scheduler

The project includes an **automatic scheduler (APScheduler)** that refreshes workflow data without manual intervention.

### 🔎 How It Works
- Runs as a **background task inside FastAPI**  
- Executes the fetch job at fixed times  
- Command executed:  
  ```bash
  python -m app.fetch_data
  
⚙️ Default Schedule
Schedule Type	Expression	Description
Daily fetch	hour=2, minute=0	Runs every day at 2:00 AM
🔧 Customization

Edit app/scheduler.py to change timings:
  ```bash
scheduler.add_job(fetch_job, "cron", hour=2, minute=0)
```

Examples:

Weekly: scheduler.add_job(fetch_job, "cron", day_of_week="sun", hour=2, minute=0)

Every 6 hours: scheduler.add_job(fetch_job, "interval", hours=6)

🚀 Running with Scheduler

Start the API normally — the scheduler is enabled automatically:

  ```bash
uvicorn app.main:app --reload
```

---

## 🔧 TROUBLESHOOTING (common)

| Symptom | Quick fix |
|--------:|-----------|
| Empty `all_data.json` | Run `python -m app.fetch_data` and check logs. Ensure `YOUTUBE_API_KEY` set for YouTube live mode. |
| Tables render as code on GitHub | Ensure there are no open triple-backtick fences above the table and no leading spaces before `|` characters. |
| YouTube metrics show `hidden` likes | YouTube may hide `likeCount`; views/comments should still be present. |

---

## ✅ DELIVERABLES

1. **Working FastAPI API** — `uvicorn app.main:app`  
2. **Dataset** — `output/all_data.json` (≥ 50 workflows)  
3. **Documentation** — this README (copy saved to repo)

---

## 📄 LICENSE

MIT — add a `LICENSE` file if distributing.

---

*File generated for you — copy the entire contents above and save as `README.md`. This file uses only standard Markdown (no surrounding triple-backtick wrapper for the whole document), so GitHub will render headings, tables, and code blocks correctly.* 
