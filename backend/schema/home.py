from schema.base import BaseModel


class Id(BaseModel):
    id: int


class Msg(BaseModel):
    msg_id: int
    text: str


class PayloadMsg(BaseModel):
    app_id: int
    user_id_by_app: int
    event_name: str
    timestamp: int
    sender: Id
    recipient: Id
    message: Msg
