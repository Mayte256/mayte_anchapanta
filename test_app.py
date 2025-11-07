import pytest
from app import app


@pytest.fixture
def client():
    """Configurar cliente de pruebas"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    """Test de la página principal"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Mayte Anchapanta' in response.data
    assert b'CI/CD' in response.data


def test_hello_has_html(client):
    """Test que verifica que retorna HTML"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data
    assert b'<html' in response.data


def test_saludo(client):
    """Test del saludo personalizado"""
    response = client.get('/saludo/Mayte')
    assert response.status_code == 200
    assert b'Mayte' in response.data
    assert b'Hola' in response.data


def test_saludo_different_name(client):
    """Test del saludo con diferentes nombres"""
    response = client.get('/saludo/Juan')
    assert response.status_code == 200
    assert b'Juan' in response.data


def test_health(client):
    """Test del health check"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'OK'
    assert 'message' in data


def test_info(client):
    """Test de la página de información"""
    response = client.get('/info')
    assert response.status_code == 200
    assert b'Mayte Anchapanta' in response.data
    assert b'Proyecto' in response.data


def test_endpoints_exist(client):
    """Test que verifica que todos los endpoints existen"""
    endpoints = ['/', '/saludo/Test', '/health', '/info']
    for endpoint in endpoints:
        response = client.get(endpoint)
        assert response.status_code == 200