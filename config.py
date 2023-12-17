from dotenv import dotenv_values as _dotenv_values

from schemas import Environment as _Environment


environment = _Environment(**_dotenv_values(".env"))  # pyright: ignore
