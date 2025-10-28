import pytest
from app import app, add

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client

def test_add_function():
    """Test the standalone add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_home_route(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_health_route(client):
    """Test the health check route."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_add_route(client):
    """Test the add route."""
    response = client.get('/add/10/5')
    assert response.status_code == 200
    assert response.json == {"result": 15}
