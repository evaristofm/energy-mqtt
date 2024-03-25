from typing import Optional

from pydantic import BaseModel


class TopicSubscriptionBase(BaseModel):
    topic: Optional[str] = None
    qos: Optional[int] = 0


class TopicSubscriptionSchema(TopicSubscriptionBase):
    id_: Optional[str] = None


class TopicSubscriptionCreateSchema(TopicSubscriptionBase):
    topic: str
