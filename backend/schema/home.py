from schema.base import BaseModel


class Id(BaseModel):
    id: str


class Msg(BaseModel):
    msg_id: str
    text: str


class PayloadMsg(BaseModel):
    app_id: str
    user_id_by_app: str
    event_name: str
    timestamp: str
    sender: Id
    recipient: Id
    message: Msg

{
  "app_id": "888726299105885743",
  "user_id_by_app": "8183171167172075287",
  "event_name": "user_send_text",
  "timestamp": "1685116916018",
  "sender": {
    "id": "3879973308021332925"
  },
  "recipient": {
    "id": "579745863508352884"
  },
  "message": {
    "msg_id": "This is message id",
    "text": "This is testing message"
  }
}