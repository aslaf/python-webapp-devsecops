import app

def test_home():
    client = app.app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    assert b"Hello, DevSecOps World!" in response.data
