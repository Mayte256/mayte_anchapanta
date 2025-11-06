import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hola' in response.data

def test_saludo(client):
    response = client.get('/saludo/Mayte')
    assert response.status_code == 200
    assert b'Mayte' in response.data