import uuid
from typing import Annotated
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.mqtt.client import fast_mqtt
from app.database import get_db
from app.models import Transaction
from app.schemas.transction import TransactionRequest

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/")
async def publishe_message_transction(db: db_dependency, transction_request: TransactionRequest):
    transction_model = Transaction(**transction_request.model_dump())

    db.add(transction_model)
    db.commit()
    db.refresh(transction_model)

    fast_mqtt.publish(
        message_or_topic="/messages",
        payload=str(transction_request.dict())
    )
    return {"result": True, "message": "Published", "payload": transction_model}
