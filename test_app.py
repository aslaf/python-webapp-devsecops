import app
import pytest

def test_home():
    client = app.app.test_client()
    response = client.get("/")

    if response.status_code != 200:
        pytest.fail(f"Expected 200 OK but got {response.status_code}")

    if b"Hello, DevSecOps World!" not in response.data:
        pytest.fail("Response body does not contain expected message")
