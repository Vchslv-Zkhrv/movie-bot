"""
Data structures used in the project.
"""


from enum import Enum as _Enum

from pydantic import BaseModel as _BaseModel
from pydantic import Field as _Field


class Environment(_BaseModel):

    db_connect_url: str = _Field(alias="DB_CONNECT_URL")
    telegram_token: str = _Field(alias="TELEGRAM_TOKEN")
    kinopoisk_token: str=  _Field(alias="KINOPOISK_TOKEN")


class BotCommand(_Enum):

    start = "start"
    history = "history"

