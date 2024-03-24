import uuid
from datetime import datetime
from enum import Enum
from fastapi import APIRouter, HTTPException

from app.mqtt.client import fast_mqtt

router = APIRouter()


@router.get("/")
async def publishe_message_transction():
    payload = str({
        "id": str(uuid.uuid4()),
        "status": "PROCESSANDO",
        "date": datetime.utcnow()
    })

    fast_mqtt.publish(
        message_or_topic="/messages",
        payload=payload
    )  # publishing mqtt topic

    return {"result": True, "message": "Published", "payload": payload}
