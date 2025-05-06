from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.registration import generate_uuid_string

app = FastAPI(title="Idle Number Wars API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/generate-uuid")
async def get_uuid():
    generated_uuid = generate_uuid_string()
    return {"uuid": generated_uuid}