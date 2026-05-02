from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./my_database.db"
# """postgres://d046b351d083596ca674b5714ca16d50b524dc0ad5f05c03371629bfb6ae42ec:sk_zP7VQvhdvB4pdK-cB_0hp@db.prisma.io:5432/postgres?sslmode=require"""

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

sessionLocal = sessionmaker(autoflush=False, bind=engine, expire_on_commit=False)

Base = declarative_base()
