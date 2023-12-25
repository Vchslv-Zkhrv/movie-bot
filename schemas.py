"""
Data structures used in the project.
"""


from enum import Enum as _Enum

from pydantic import BaseModel as _BaseModel
from pydantic import Field as _Field


class ApiName(_Enum):
    kinopoisk = "kinopoisk"
    ivi = "ivi"


class Environment(_BaseModel):
    db_connect_url: str = _Field(alias="DB_CONNECT_URL")
    telegram_token: str = _Field(alias="TELEGRAM_TOKEN")
    api_token: str = _Field(alias="API_TOKEN")
    api_name: ApiName = _Field(alias="API_NAME")


class BotCommand(_Enum):
    start = "start"
    history = "history"
