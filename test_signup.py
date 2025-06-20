import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, get_db
from signup import app

# Use in-memory SQLite for isolated test environment
TEST_DB_URL = "sqlite:///:memory:"

# Create database engine for testing
engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})

# Create session factory bound to the test engine
TestingSessionLocal = sessionmaker(bind=engine)

# Create database schema before running tests
Base.metadata.create_all(bind=engine)

# Provide test database session instead of production one
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Apply dependency override for testing
app.dependency_overrides[get_db] = override_get_db

# Create test client to simulate API requests
client = TestClient(app)

# Verify successful signup with valid data
def test_basic_signup():
    response = client.post(
        "/signup",
        json={
            "email": "test@example.com",
            "password": "securepassword",
            "first_name": "Test",
            "last_name": "User",
            "interests": "Testing"
        }
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "User signed up successfully"}

# Ensure duplicate email returns an error
def test_duplicate_email():
    # First request should succeed
    response1 = client.post(
        "/signup",
        json={
            "email": "dup@example.com",
            "password": "password123",
            "first_name": "Dup",
            "last_name": "User",
            "interests": "Testing"
        }
    )
    assert response1.status_code == 200, response1.text

    # Second request with same email should fail
    response2 = client.post(
        "/signup",
        json={
            "email": "dup@example.com",
            "password": "password456",
            "first_name": "Dup2",
            "last_name": "User2",
            "interests": "Testing2"
        }
    )
    assert response2.status_code == 400, response2.text
    assert "email already registered" in response2.json()["detail"].lower()