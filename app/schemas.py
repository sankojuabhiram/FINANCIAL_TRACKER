
from pydantic import BaseModel, Field
from datetime import date

class TransactionCreate(BaseModel):
    amount: float = Field(..., gt=0)
    type: str
    category: str
    date: date
    notes: str

class TransactionResponse(TransactionCreate):
    id: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    role: str
