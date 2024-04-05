from fastapi.testclient import TestClient
from pydantic import BaseModel

from ..main import app

client = TestClient(app)


def test_read_main():
    
    response = client.post("/auth/login", json={"username": "string", "password": "string"})
    assert response.status_code == 401
    response = client.post("/auth/login", json={"username": "wadewilson", "password": "chimichangas4life"})
    assert response.status_code == 200
    