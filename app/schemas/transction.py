from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class TransactionRequest(BaseModel):
    status: str


class TranstionReponse(BaseModel):
    id: UUID
    status: str
    date: datetime
