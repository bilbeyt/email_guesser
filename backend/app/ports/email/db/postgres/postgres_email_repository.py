import logging

import psycopg2 as pg2

import app.ports.email.db.postgres.postgres_email_queries as queries
from app.config import settings
from app.domains.email.email import EmailFormat, EmailFormatEnum
from app.domains.email.email_repository import EmailRepository


class PostgresEmailRepository(EmailRepository):

    def get_email_format_by_domain(self, domain: str) -> EmailFormat | None:
        email_format = None
        try:
            with pg2.connect(dsn=settings.database_url) as conn:
                with conn.cursor() as cur:
                    cur.execute(queries.GET_EMAIL_FORMAT_BY_DOMAIN_QUERY, (domain,))
                    result = cur.fetchone()
                    if result is None:
                        logging.info("No email found for domain: %s", domain)
                    else:
                        email_format = EmailFormat(result[0], EmailFormatEnum(result[1]))
        except Exception as e:
            logging.exception("Can not query email format: %s", e)
        return email_format

    def create_email_format(self, email_format: EmailFormat) -> bool:
        try:
            with pg2.connect(dsn=settings.database_url) as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        queries.INSERT_EMAIL_FORMAT_QUERY,
                        (email_format.domain, email_format.format.value),
                    )
                    conn.commit()
                    return True
        except Exception as e:
            logging.exception("Can not insert email format: %s", e)
        return False
