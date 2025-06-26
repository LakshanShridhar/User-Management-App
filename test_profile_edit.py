import pytest
from fastapi.testclient import TestClient
from profile_edit import app  # Import the FastAPI app from profile_edit.py

client = TestClient(app)

def test_profile_edit_success():
    """
    Test that profile edit succeeds with correct credentials.
    Assumes a user with email 'Test123@example.com' and password 'correct_password' exists.
    """
    payload = {
        "email": "Test123@example.com",
        "password": "correct_password",
        "first_name": "NewFirst",
        "last_name": "NewLast",
        "interests": "New interests"
    }
    response = client.post("/profile-edit", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Profile updated successfully"}

def test_profile_edit_wrong_email():
    """
    Test that profile edit fails when email is not found.
    """
    payload = {
        "email": "wrong@example.com",
        "password": "correct_password",
        "first_name": "NewFirst",
        "last_name": "NewLast",
        "interests": "New interests"
    }
    response = client.post("/profile-edit", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid credentials"

def test_profile_edit_wrong_password():
    """
    Test that profile edit fails with incorrect password.
    """
    payload = {
        "email": "Test123@example.com",
        "password": "wrong_password",
        "first_name": "NewFirst",
        "last_name": "NewLast",
        "interests": "New interests"
    }
    response = client.post("/profile-edit", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid credentials"