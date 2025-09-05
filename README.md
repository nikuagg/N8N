Here’s a professional version for your project:

# 📊 n8n Popularity System (FastAPI)

This project tracks the popularity of **n8n workflows** across platforms (YouTube + Forum).  
It fetches workflow mentions, stores them locally, and serves results via a **FastAPI REST API**.

---

## 🚀 Features
- Fetches **YouTube workflows** (via YouTube Data API).
- Fetches **Forum workflows** (via scraping/discussions).
- Merges & deduplicates results automatically.
- Stores data as JSON inside `/output` (ignored in git).
- REST API endpoints to query workflows:
  - `GET /workflows` → all workflows
  - `GET /workflows/youtube` → YouTube only
  - `GET /workflows/forum` → Forum only

---

## 📂 Project Structure


n8n-popularity-system/
│── app/
│ ├── main.py # FastAPI entrypoint
│ ├── youtube.py # Fetch from YouTube API
│ ├── forum.py # Fetch forum workflows
│ ├── fetch_data.py # Fetch + save workflows
│ ├── utils.py # Helpers
│ └── ...
│── output/ # Local JSON results (ignored in git)
│── .env # API keys (ignored in git)
│── .env.example # Example environment file
│── requirements.txt # Python dependencies
│── README.md # Documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/nikuagg/N8N.git
cd N8N

2️⃣ Create & activate a virtual environment
python -m venv .venv
.venv\Scripts\activate   # On Windows
source .venv/bin/activate  # On Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup environment variables

Copy .env.example → .env and add your YouTube API key:

YOUTUBE_API_KEY=your_api_key_here

▶️ Running the Fetch Script

To fetch latest workflows:

python -m app.fetch_data


Results will be saved in:

output/youtube.json

output/forum.json

output/all_data.json

🌐 Running the API

Start FastAPI with Uvicorn:

uvicorn app.main:app --reload


API will be available at:

Swagger docs → http://127.0.0.1:8000/docs

All workflows → http://127.0.0.1:8000/workflows

YouTube workflows → http://127.0.0.1:8000/workflows/youtube

Forum workflows → http://127.0.0.1:8000/workflows/forum

📦 Deployment Guide
Local (Developer Mode)

Run uvicorn app.main:app --reload

