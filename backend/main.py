from fastapi import FastAPI
from registration import generate_uuid_string

app = FastAPI(title="Universal Math Wars API")


@app.get("/api/v1/generate-uuid")
async def get_uuid():
    generated_uuid = generate_uuid_string()
    return {"uuid": generated_uuid} 