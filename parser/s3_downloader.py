import sys
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import boto3

from config.settings import (
    AWS_ACCESS_KEY,
    AWS_SECRET_KEY,
    AWS_REGION,
    S3_BUCKET,
    S3_PREFIX,
)

LOCAL_LOG_DIR = PROJECT_ROOT / "logs"
LOCAL_LOG_DIR.mkdir(exist_ok=True)


def get_s3_client():
    return boto3.client(
        "s3",
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
    )


def sync_logs():

    s3 = get_s3_client()

    paginator = s3.get_paginator("list_objects_v2")

    downloaded = 0
    skipped = 0

    for page in paginator.paginate(
        Bucket=S3_BUCKET,
        Prefix=S3_PREFIX
    ):

        if "Contents" not in page:
            continue

        for obj in page["Contents"]:

            key = obj["Key"]

            if not key.endswith(".log.gz"):
                continue

            filename = os.path.basename(key)

            local_file = LOCAL_LOG_DIR / filename

            if local_file.exists():
                skipped += 1
                continue

            print(f"Downloading {filename}")

            s3.download_file(
                S3_BUCKET,
                key,
                str(local_file)
            )

            downloaded += 1

    print()
    print(f"Downloaded : {downloaded}")
    print(f"Skipped     : {skipped}")


if __name__ == "__main__":
    sync_logs()
