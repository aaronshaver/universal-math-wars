from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_uuid():
    response = client.get("/api/v1/generate-uuid")
    assert response.status_code == 200
    data = response.json()
    assert "uuid" in data
    assert isinstance(data["uuid"], str)
    # We could add a more specific UUID format check here if needed
    assert len(data["uuid"]) > 0 