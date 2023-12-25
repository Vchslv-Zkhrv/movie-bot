"""
Module with database tables definition.
"""


import typing as _t
from datetime import datetime as _dt

import sqlalchemy as _sa
from sqlalchemy import orm as _orm

import schemas as _schemas

from .database import Base as _Base


class User(_Base):
    __tablename__ = "User"

    chat_id: _orm.Mapped[str] = _orm.mapped_column(
        _sa.Integer, primary_key=True
    )
    username: _orm.Mapped[str] = _orm.mapped_column(
        _sa.String, unique=True, nullable=False, index=True
    )
    first_name: _orm.Mapped[str] = _orm.mapped_column(
        _sa.String, nullable=False
    )
    last_name: _orm.Mapped[_t.Optional[str]] = _orm.mapped_column(
        _sa.String, nullable=True
    )
    created: _orm.Mapped[_dt] = _orm.mapped_column(
        _sa.DateTime, nullable=False, index=True, default=_dt.utcnow
    )

    history: _orm.Mapped[_t.List["UserHistory"]] = _orm.relationship(
        back_populates="user"
    )


class UserHistory(_Base):
    __tablename__ = "UserHistory"

    chat_id: _orm.Mapped[int] = _orm.mapped_column(
        _sa.Integer, _sa.ForeignKey("User.chat_id"), primary_key=True
    )
    command: _orm.Mapped[_schemas.BotCommand] = _orm.mapped_column(
        _sa.Enum(_schemas.BotCommand), nullable=False, index=True
    )
    value: _orm.Mapped[_t.Optional[str]] = _orm.mapped_column(
        _sa.String, nullable=True
    )
    resieved: _orm.Mapped[_dt] = _orm.mapped_column(
        _sa.DateTime, nullable=False, default=_dt.utcnow, index=True
    )
    responded: _orm.Mapped[_dt] = _orm.mapped_column(
        _sa.DateTime, nullable=True, index=True
    )
    succeeded: _orm.Mapped[bool] = _orm.mapped_column(
        _sa.Boolean, nullable=False, index=True
    )
    api: _orm.Mapped[_schemas.ApiName] = _orm.mapped_column(
        _sa.Enum(_schemas.ApiName), nullable=True
    )

    user: _orm.Mapped["User"] = _orm.relationship(back_populates="history")
