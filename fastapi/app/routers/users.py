from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.database import sessionLocal
from app import models
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserCreate(BaseModel):
    username: str
    email: str
    phone: str
    age: int
    is_active: bool = True


@router.get('/users/{username}')
def get_user(username: str, db: Session = Depends(get_db)):
    for user_obj in db.query(models.User).filter(models.User.username == username).first():
        if user_obj:
            return {'message': f'{username} found in the list'}
    raise HTTPException(status_code=404, detail="user not found")

@router.post('/users/')
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(
        username = user.name,
        age = user.age,
        email = user.email,
        phone = user.phone,
        is_active = user.is_active
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "user created successfully!", "user_data": user}
    
@router.get('/users')
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return {'users': users}
