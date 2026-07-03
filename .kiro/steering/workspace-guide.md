---
inclusion: auto
---

# Log Analyzer — Workspace Guide

## Project Overview

AWS ALB Traffic Analyzer — a Streamlit-based dashboard that parses, stores, and visualizes AWS Application Load Balancer access logs. Logs are synced from S3, parsed, stored in SQLite, and displayed via interactive charts.

## Technology Stack

| Layer | Technology |
|-------|------------|
| Frontend/Dashboard | Streamlit |
| Visualization | Plotly, Matplotlib |
| Data Processing | Pandas, NumPy |
| Database | SQLite |
| Cloud | AWS S3 (boto3) |
| Language | Python 3.x |

## Project Structure

```
Log_analyzer/
├── app.py                  # Main Streamlit application
├── config/
│   ├── organizations.py    # Organization configurations
│   └── settings.py         # Application settings
├── dashboard/
│   ├── charts.py           # Chart/visualization components
│   └── filters.py          # Dashboard filter components
├── database/
│   └── db.py               # SQLite database operations
├── parser/
│   ├── alb_parser.py       # ALB log parsing logic
│   ├── models.py           # Data models
│   └── s3_downloader.py    # S3 log sync/download
├── data/
│   └── alb_logs.db         # SQLite database (local)
├── Logs/                   # Downloaded log files
├── exports/                # Exported CSV files
└── reports/                # Generated reports
```

## GitHub Context

| Item | Value |
|------|-------|
| Repository | `sreenidhipalimar98/alb-log-analyzer` |
| Default Branch | `main` |
| Development Branch | `develop` |
| Branch Strategy | Branch from `develop`, PRs to `develop` |

## Task Workflow

1. Create/pick a GitHub issue
2. Create a feature branch from `develop`
3. Implement changes
4. Create a Pull Request to `develop`
5. Review and merge

## Common Commands

```bash
# Run the Streamlit app
streamlit run app.py

# Install dependencies
pip install -r requirements.txt

# Sync logs from S3
python -c "from parser.s3_downloader import sync_logs; sync_logs()"
```

## AWS Context

- Logs are stored in S3 and synced locally
- ALB access logs follow standard AWS ALB log format
- boto3 is used for all AWS interactions

## Rules

- Never commit the `data/` directory (contains local SQLite DB)
- Never commit the `Logs/` directory (contains raw log files)
- Never commit `.env` or credential files
- Keep `venv/` out of version control
- Always branch from `develop`, never push directly to `main`
