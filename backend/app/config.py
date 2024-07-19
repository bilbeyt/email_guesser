from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = ""
    fixture_path: str = ""
    echo_sql: bool = False
    debug_logs: bool = False
    test: bool = False
    project_name: str = "email_guesser"


settings = Settings()
