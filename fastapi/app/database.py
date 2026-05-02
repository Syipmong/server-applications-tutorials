from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(
    DATABASE_URL,
    # connect_args={
    #     "check_same_thread": False
    # }
)

sessionLocal = sessionmaker(autoflush=False, bind=engine, expire_on_commit=False)

Base = declarative_base()
