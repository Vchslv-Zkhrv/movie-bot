"""
Module with basic database objects.

To switch to another SQL dialect / driver, change DB_CONNECT_URL.
"""


from sqlalchemy.ext.asyncio import AsyncSession as _AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.ext.declarative import declarative_base as _delarative_base
from sqlalchemy.orm import sessionmaker as _sessionmaker

from config import env as _env


engine = _create_async_engine(_env.db_connect_url)
Base = _delarative_base()
Session = _sessionmaker(
    engine=engine, class_=_AsyncSession, expire_on_commit=False
)
