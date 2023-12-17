from ..abstract import Api as _AbstractApi


URL = "https://api.kinopoisk.dev/"
TOKEN_HEADER = "X-API-KEY"


class Api(_AbstractApi):
    """Kinopoisk api"""
