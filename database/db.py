import sqlite3
from pathlib import Path

DB_PATH = Path("data/alb_logs.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alb_logs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp TEXT,

        method TEXT,

        path TEXT,

        protocol TEXT,

        client_ip TEXT,

        client_port INTEGER,

        target_ip TEXT,

        target_port INTEGER,

        elb_status_code INTEGER,

        target_status_code INTEGER,

        request_processing_time REAL,

        target_processing_time REAL,

        response_processing_time REAL,

        received_bytes INTEGER,

        sent_bytes INTEGER,

        user_agent TEXT
    );
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database created successfully.")
