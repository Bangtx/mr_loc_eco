from fastapi import APIRouter
from model.user import User as UserModel
from schema.user import User, UserCreate
from typing import List

router = APIRouter()


@router.get('/', response_model=List[User])
def get_user():
    return UserModel.get_list()


@router.post('/', response_model=User)
def create_user(user: UserCreate):
    return UserModel.create(**user.dict())


