import pytest
from fastapi.testclient import TestClient
from change_password import app  # Import the FastAPI app for password change

client = TestClient(app)

def test_change_password_success():
    """
    Test that password change succeeds with correct current password.
    Assumes user with email 'Confident@example.com' and current password 'TheGoat' exists.
    """
    data = {
        "email": "Test123@example.com",
        "current_password": "correct_password",
        "new_password": "correct_password"
    }
    response = client.post("/change-password", json=data)
    assert response.status_code == 200
    assert "Password updated successfully" in response.json().get("message", "")

def test_change_password_wrong_current():
    """
    Test that password change fails with incorrect current password.
    """
    data = {
        "email": "Test123@example.com",
        "current_password": "GreatLife123",
        "new_password": "UltimateLife123"
    }
    response = client.post("/change-password", json=data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect current password"

def test_change_password_nonexistent_email():
    """
    Test that password change fails if the email does not exist.
    """
    data = {
        "email": "FakeEmail123@example.com",
        "current_password": "GreatLife123",
        "new_password": "UltimateLife123"
    }
    response = client.post("/change-password", json=data)
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"