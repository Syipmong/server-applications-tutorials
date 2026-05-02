from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./my_database.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

sessionLocal = sessionmaker(autoflush=False, bind=engine, expire_on_commit=False)

base = declarative_base()
