from enum import Enum
from fastapi import APIRouter, HTTPException

from app.mqtt.client import fast_mqtt

router = APIRouter()


@router.get("/")
async def publishe_message_transction():
    fast_mqtt.publish(message_or_topic="/messages", payload=str({"1": "testando..."}))  # publishing mqtt topic
    return {"result": True, "message": "Published"}
