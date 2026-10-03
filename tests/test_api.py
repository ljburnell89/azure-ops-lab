from fastapi.testclient import TestClient

from app.main import app


# Create a reusable in-process client for sending requests to the API.
client = TestClient(app)


def test_health_check():
    # Check that the health endpoint reports the service as healthy.
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_message():
    # Check that the message endpoint returns the expected greeting.
    response = client.get("/api/message")

    assert response.status_code == 200
    assert response.json()["message"] == (
        "Hello from the Azure DevOps Showcase API!"
    )


def test_version():
    # Check that the version endpoint returns the expected API version.
    response = client.get("/api/version")

    assert response.status_code == 200
    assert response.json()["version"] == "1.0.0"
