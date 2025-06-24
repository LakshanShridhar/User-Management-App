import pytest
from fastapi.testclient import TestClient
from signup import app  # Import the signup FastAPI app

client = TestClient(app)

def test_signup_success():
    """
    Test that signup succeeds with valid data.
    """
    signup_data = {
        "email": "newuser2@example.com",
        "password": "securepassword",
        "first_name": "New",
        "last_name": "User",
        "interests": "Testing"
    }
    response = client.post("/signup", json=signup_data)
    assert response.status_code == 200
    assert "User signed up successfully" in response.json().get("message", "")

def test_signup_duplicate_email():
    """
    Test that signup fails if email is already registered.
    """
    # First signup should succeed
    client.post("/signup", json={
        "email": "dup@example.com",
        "password": "password123",
        "first_name": "Dup",
        "last_name": "User",
        "interests": "Testing"
    })

    # Second signup with same email should fail
    response = client.post("/signup", json={
        "email": "dup@example.com",
        "password": "password456",
        "first_name": "Dup2",
        "last_name": "User2",
        "interests": "Testing2"
    })
    assert response.status_code == 400
    assert "email already registered" in response.json()["detail"].lower()
