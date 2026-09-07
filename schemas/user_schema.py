from typing import Optional
from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    email: str
    department: str
    age: int


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    department: Optional[str] = None
    age: Optional[int] = None

    