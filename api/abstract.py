from abc import ABC as _ABC
from abc import abstractmethod as _amethod


class Api(_ABC):

    """Abstract class describing api interface"""

    @_amethod
    def __init__(self, token: str):
        ...

    @_amethod
    async def get_movie(self, id: int):
        """Get movie by id"""
