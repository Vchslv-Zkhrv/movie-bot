from pydantic import BaseModel as _Base, Field as _Field


class _Schema(_Base):

    class Config:
        orm_mode=True
        arbitrary_types_allowed=True


class MovieBase(_Schema):
    id: int
    name: str
    year: int

