import gzip
import shlex
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd

LOG_DIR = Path("logs")


def parse_logs():

    rows = []

    for logfile in LOG_DIR.glob("*.log.gz"):

        print(f"Reading {logfile.name}")

        with gzip.open(logfile, "rt", encoding="utf-8") as f:

            for line in f:

                try:

                    fields = shlex.split(line)

                    request = fields[12].split()

                    method = request[0]

                    url = request[1]

                    version = request[2]

                    parsed = urlparse(url)

                    rows.append({
                        "timestamp": fields[1],
                        "method": method,
                        "path": parsed.path,
                        "status": int(fields[8]),
                        "target_status": int(fields[9]),
                        "client": fields[3].split(":")[0],
                        "response_time": float(fields[6]),
                        "bytes_sent": int(fields[11])
                    })

                except Exception:
                    continue

    return pd.DataFrame(rows)


if __name__ == "__main__":

    df = parse_logs()

    print(df.head())

    print()

    print(df.info())
