"""
Database CRUDS endpoints
"""


import typing as _t

from sqlalchemy.ext.asyncio import AsyncSession as _AsyncSession

from . import database as _db
from . import models as _models  # without this import metadata will be empty


async def get_session() -> _t.AsyncGenerator[_AsyncSession, None]:
    """Yields AsyncSession and closes it after use"""
    async with _db.Session() as session:  # pyright: ignore
        yield session


async def init_models() -> None:
    """Removes all tables from database and creates them again"""
    async with _db.engine.begin() as connection:
        await connection.run_sync(_db.Base.metadata.drop_all)
        await connection.run_sync(_db.Base.metadata.create_all)


print(_models)
