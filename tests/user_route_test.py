from fastapi.testclient import TestClient
from pydantic import BaseModel

from bms.main import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users/signup",
        json={"username": "wadewilson", "email": "deadpool@marvel.com", "password": "chimichangas4life"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "deadpool@marvel.com"
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"/users/{user_id}")
    
    assert response.status_code == 201
