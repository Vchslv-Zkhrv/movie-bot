from pydantic import BaseModel as _Base


class _Schema(_Base):
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class MovieBase(_Schema):
    id: int
    name: str
    year: int
