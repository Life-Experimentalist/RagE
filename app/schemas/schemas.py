from pydantic import BaseModel
from typing import List, Optional

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class Message(BaseModel):
    content: str
    sender_id: int
    recipient_id: int

class MessageCreate(Message):
    pass

class MessageResponse(Message):
    id: int

    class Config:
        orm_mode = True

class ResponseModel(BaseModel):
    success: bool
    data: Optional[List[Item]] = None
    message: Optional[str] = None