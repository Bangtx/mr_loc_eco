import os

from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.responses import FileResponse
from model.image import Image
router = APIRouter()


@router.get('/')
def get_images(path):
    return FileResponse(path)


@router.delete('/{id}')
def delete_image(id: int):
    image = Image.get_or_none(id=id)
    if not image:
        raise HTTPException(400, 'Image not exists')
    path = image.path
    os.remove(path)
    return Image.delete().where(Image.id == id).execute()


