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
    timestamp: 1684941136153
    sender: Id
    recipient: Id
    message: Msg