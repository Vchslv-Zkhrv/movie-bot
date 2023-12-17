import punq as _punq
from dotenv import dotenv_values as _dotenv_values

import api as _api
import schemas as _schemas
from api import ivi as _ivi
from api import kinopoisk as _kinopoisk


env = _schemas.Environment(**_dotenv_values(".env"))  # pyright: ignore


api_container = _punq.Container()
if env.api_name == "ivi":
    api_container.register(_api.abstract.Api, _ivi.Api)
elif env.api_name == "kinopoisk":
    api_container.register(_api.abstract.Api, _kinopoisk.Api)
