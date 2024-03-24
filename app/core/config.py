from decouple import config
from fastapi_mqtt.fastmqtt import MQTTConfig


mqtt_config = MQTTConfig(
    host=config("HOST"),
    port=config("PORT"),
    keepalive=config("KEEPALIVE")
)
