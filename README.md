# AWS ALB Traffic Analyzer

A Streamlit-based dashboard for parsing, analyzing, and visualizing AWS Application Load Balancer (ALB) access logs. Syncs logs from S3, parses them, stores data in SQLite, and presents interactive charts and metrics.

## Features

- Sync ALB access logs directly from S3
- Parse gzipped ALB log files into structured data
- Interactive dashboard with date filtering
- Metrics: total requests, unique APIs, unique clients, avg response time
- Top APIs bar chart
- Status code distribution (pie chart)
- Requests per hour timeline
- Export parsed logs to CSV
- Multi-organization support (XLP, TPH)

## Tech Stack

| Component | Technology |
|-----------|------------|
| Dashboard | Streamlit |
| Visualization | Plotly, Matplotlib |
| Data Processing | Pandas, NumPy |
| Database | SQLite |
| Cloud Storage | AWS S3 (boto3) |
| Language | Python 3.x |

## Project Structure

```
Log_analyzer/
├── app.py                      # Main Streamlit application
├── config/
│   ├── settings.py             # AWS & S3 configuration
│   └── organizations.py        # Multi-org configuration
├── dashboard/
│   ├── charts.py               # Chart components
│   └── filters.py              # Filter components
├── database/
│   └── db.py                   # SQLite schema & connection
├── parser/
│   ├── alb_parser.py           # ALB log parsing logic
│   ├── models.py               # Data models
│   └── s3_downloader.py        # S3 log sync/download
├── data/                       # SQLite database (gitignored)
├── Logs/                       # Downloaded log files (gitignored)
├── exports/                    # Exported CSV files
├── reports/                    # Generated reports
└── requirements.txt            # Python dependencies
```

## Setup

### Prerequisites

- Python 3.9+
- AWS credentials with access to the ALB logs S3 bucket

### Installation

```bash
# Clone the repository
git clone https://github.com/sreenidhipalimar98/alb-log-analyzer.git
cd alb-log-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. Update `config/settings.py` with your AWS credentials and S3 bucket details:

```python
AWS_ACCESS_KEY = "<your-access-key>"
AWS_SECRET_KEY = "<your-secret-key>"
AWS_REGION = "us-east-1"
S3_BUCKET = "<your-alb-logs-bucket>"
S3_PREFIX = "AWSLogs/<account-id>/elasticloadbalancing/<region>/"
```

2. For multi-org setups, configure `config/organizations.py` with each organization's AWS credentials and bucket info.

> **Security Note:** Never commit real AWS credentials. Use environment variables or AWS profiles in production.

### Initialize Database

```bash
python database/db.py
```

## Usage

### Run the Dashboard

```bash
streamlit run app.py
```

### Sync Logs from S3

Either click the "Sync From S3" button in the dashboard, or run manually:

```bash
python parser/s3_downloader.py
```

### Parse Logs Standalone

```bash
python parser/alb_parser.py
```

## Kiro IDE Setup

This project includes a `.kiro/` configuration directory for use with [Kiro IDE](https://kiro.dev):

- **GitHub MCP Server** — enables branch creation, pull requests, and issue management directly from the IDE
- **Safety Hooks** — blocks dangerous shell commands and sensitive file reads
- **Steering Files** — provides workspace context and task workflow guidance

See `KIRO_SETUP_GUIDE.md` for full details on the Kiro configuration.

## License

Private — Internal use only.
