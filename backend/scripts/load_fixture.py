import json
import logging
from pathlib import Path

import psycopg2 as pg2

from app.config import settings
from app.ports.email.api.email_deps import get_repo, get_service
from app.ports.email.db.postgres.postgres_email_queries import CREATE_TABLE_QUERY

logging.basicConfig(level=logging.DEBUG if settings.debug_logs else logging.INFO)


def create_table() -> None:
    with pg2.connect(dsn=settings.database_url) as conn:
        with conn.cursor() as cur:
            cur.execute(CREATE_TABLE_QUERY)


def run() -> None:
    create_table()
    repo = get_repo()
    service = get_service(repo)
    fixture_path = Path(settings.fixture_path)
    with open(fixture_path, "r") as f:
        data = json.load(f)
    count = 0
    for full_name, email in data.items():
        if service.save_email_format_by_full_name_and_email(full_name, email):
            count += 1
    logging.info("%d emails saved", count)


if __name__ == "__main__":
    run()
