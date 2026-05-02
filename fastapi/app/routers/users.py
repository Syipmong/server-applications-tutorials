from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class UserCreate(BaseModel):
    username: str
    email: str
    phone: str
    age: int
    is_active: bool = True

user_list = []

@router.get('/users/{username}')
def get_user(username: str):
    for user_obj in user_list:
        if username == user_obj.username:
            return {'message': f'{username} found in the list'}
    raise HTTPException(status_code=404, detail="user not found")

@router.post('/users/')
def create_user(user: UserCreate):
    user_list.append(user)
    return {"message": "user created successfully!", "user_data": user}
    
@router.get('/users')
def get_users():
    return {'users': user_list}
