from fastapi.testclient import TestClient
from main import app
from app.infrastructure.database import Base, engine

client = TestClient(app)


def setup_function(_):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_create_and_get_user():
    response = client.post('/users/', json={'name': 'John', 'email': 'john@example.com'})
    assert response.status_code == 200
    data = response.json()

    resp_get = client.get(f"/users/{data['id']}")
    assert resp_get.status_code == 200
    assert resp_get.json() == data


def test_list_users():
    client.post('/users/', json={'name': 'A', 'email': 'a@example.com'})
    client.post('/users/', json={'name': 'B', 'email': 'b@example.com'})

    resp = client.get('/users/')
    assert resp.status_code == 200
    assert len(resp.json()) == 2


def test_create_user_invalid_email():
    resp = client.post('/users/', json={'name': 'Bad', 'email': 'bademail'})
    assert resp.status_code == 400
