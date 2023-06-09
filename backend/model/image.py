from model.base import BaseModel
from peewee import IntegerField, CharField
from datetime import datetime
from fastapi.responses import FileResponse
from config.get_env import VUE_APP_API_URL
from uuid import uuid4


class Image(BaseModel):
    url = CharField()
    path = CharField()

    class Meta:
        db_table = 'image'

    @classmethod
    def create(cls, image, unique=None):
        # image: UploadFile
        # save file into image folder and save into database
        dir = 'image'
        time_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        path = f"{dir}/{time_now}{unique if unique else ''}.jpg"
        with open(path, "wb+") as file_object:
            file_object.write(image)

        url = f'{VUE_APP_API_URL}/image/?path={path}'

        return super().create(url=url, path=path)
