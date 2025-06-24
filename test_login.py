import pytest
from fastapi.testclient import TestClient
from login import app  # Import the FastAPI app from login.py

# Create a test client that simulates requests to the FastAPI app
client = TestClient(app)

def test_login_success():
    """
    Test that login succeeds with correct email and password.
    Assumes a user with email 'test@example.com' and password 'correct_password' exists in the test DB.
    """
    login_data = {
        "email": "test@example.com",
        "password": "correct_password"
    }
    # Send POST request to /login endpoint with JSON payload
    response = client.post("/login", json=login_data)

    # Assert that the HTTP status code is 200 OK
    assert response.status_code == 200

    # Assert that response message contains 'Welcome back'
    assert "Welcome back" in response.json().get("message", "")

def test_login_wrong_email():
    """
    Test that login fails with an incorrect email.
    """
    login_data = {
        "email": "wrong@example.com",
        "password": "correct_password"
    }
    # POST request with wrong email
    response = client.post("/login", json=login_data)

    # Expect 400 Bad Request due to invalid credentials
    assert response.status_code == 400

    # Response should include 'Invalid credentials' detail
    assert response.json()["detail"] == "Invalid credentials"

def test_login_wrong_password():
    """
    Test that login fails with an incorrect password.
    """
    login_data = {
        "email": "test@example.com",
        "password": "wrong_password"
    }
    # POST request with wrong password
    response = client.post("/login", json=login_data)

    # Expect 400 Bad Request due to invalid credentials
    assert response.status_code == 400

    # Response should include 'Invalid credentials' detail
    assert response.json()["detail"] == "Invalid credentials"