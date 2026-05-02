from app.database import Base
from sqlalchemy import Column, String, Integer, Boolean
class User(Base):

    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    age = Column(Integer)
    phone = Column(String)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

