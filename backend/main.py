from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session
from pydantic import BaseModel

from registration import generate_uuid_string
from database import create_db_and_tables, get_session, User

app = FastAPI(title="Idle Number Wars API")

# Create database tables on startup
create_db_and_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for registration request
class UserCreate(BaseModel):
    username: str
    password: str # This will be the UUID from the frontend

@app.get("/api/v1/generate-uuid")
async def get_uuid():
    generated_uuid = generate_uuid_string()
    return {"uuid": generated_uuid}

@app.post("/api/v1/register")
async def register_user(user_data: UserCreate, session: Session = Depends(get_session)):
    # For now, we directly use the provided password (UUID) as hashed_password
    # and skip username validation as per instructions.
    db_user = User(username=user_data.username, hashed_password=user_data.password)
    
    session.add(db_user)
    try:
        session.commit()
        session.refresh(db_user)
    except Exception as e: # Catch potential unique constraint violation or other DB errors
        session.rollback()
        # A more specific error handling for unique username violation could be added here
        # For now, a generic 500 error if something goes wrong.
        raise HTTPException(status_code=500, detail="Could not register user.")
    
    return {"message": "User registered successfully", "user_id": db_user.id}