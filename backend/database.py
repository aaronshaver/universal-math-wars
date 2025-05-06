import os
from sqlmodel import create_engine, Session, SQLModel, Field
from sqlalchemy.orm import sessionmaker

# Get database connection details from environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Construct the database URL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLModel User Class
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str # For now, this will store the plain UUID

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True) # echo=True logs SQL queries, useful for debugging

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a DB session
def get_session():
    with Session(engine) as session:
        yield session