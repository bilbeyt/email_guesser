from typing import Annotated

from fastapi import Depends

from app.domains.email.email_service import EmailService
from app.ports.email.db.postgres.postgres_email_repository import PostgresEmailRepository


def get_repo() -> PostgresEmailRepository:
    return PostgresEmailRepository()


def get_service(repo: Annotated[PostgresEmailRepository, Depends(get_repo)]) -> EmailService:
    return EmailService(repo)
