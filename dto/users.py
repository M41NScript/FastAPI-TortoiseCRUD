from pydantic import BaseModel
from typing import Optional


class UserIn(BaseModel):
    name: str
    username: Optional[str] = None
    email: str
    password: str
    

class UserOut(BaseModel):
    name: str
    username: Optional[str] = None
    email: str
    password: str
    created_at: str
    updated_at: str
    

class UserDel(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    

class UserUpd(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None