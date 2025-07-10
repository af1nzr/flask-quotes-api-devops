import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Quotes API" in response.data

def test_quote(client):
    response = client.get('/quote')
    assert response.status_code == 200
    assert b"quote" in response.data
