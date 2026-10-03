from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_message():
    response = client.get("/api/message")

    assert response.status_code == 200
    assert response.json()["message"] == (
        "Hello from the Azure DevOps Showcase API!"
    )


def test_version():
    response = client.get("/api/version")

    assert response.status_code == 200
    assert response.json()["version"] == "1.0.0"
