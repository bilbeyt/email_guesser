from enum import Enum

from pydantic.dataclasses import dataclass


class EmailFormatEnum(Enum):
    FIRST_NAME_LAST_NAME = 0
    FIRST_NAME_INITIAL_LAST_NAME = 1


@dataclass
class EmailFormat:
    domain: str
    format: EmailFormatEnum
