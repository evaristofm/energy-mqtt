from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.mqtt.client import fast_mqtt
from app.api.api_v1.api import api_router


def cerate_application() -> FastAPI:

    application = FastAPI()

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix="/api_v1")

    fast_mqtt.init_app(application)

    return application


app = cerate_application()

