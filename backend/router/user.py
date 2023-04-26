from fastapi import APIRouter
from model.user import User as UserModel
from schema.user import User, UserCreate, UserLogin
from typing import List
from playhouse.shortcuts import model_to_dict

router = APIRouter()


@router.get('/', response_model=List[User])
def get_user():
    return UserModel.get_list()


@router.post('/')
def create_user(user: UserCreate):
    print(user.dict())
    return UserModel.create(**user.dict())


@router.post('/login')
def login(user: UserLogin):
    user = UserModel.get_or_none(code=user.code, password=user.password)
    if not user:
        return {
            'status': 400, 'data': None
        }

    user = model_to_dict(user)
    user.pop('password', None)
    return {
        'status': 200, 'data': user
    }
