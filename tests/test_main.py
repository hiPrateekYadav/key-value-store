from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_value():
    response = client.get("/get/test_key")
    assert response.status_code == 404
    assert response.json() == {"detail": "Key not found"}