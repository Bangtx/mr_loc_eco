from schema.base import BaseSchema
from fastapi import UploadFile


class Image(BaseSchema):
    file: str
