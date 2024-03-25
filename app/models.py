import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.database import Base


class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    status = Column(String(20))
    date = Column(DateTime, default=datetime.utcnow())

