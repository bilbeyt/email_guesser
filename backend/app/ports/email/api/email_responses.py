from pydantic.dataclasses import dataclass


@dataclass
class EmailResponse:
    email: str
