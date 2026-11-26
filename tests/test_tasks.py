import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app("testing")
    with app.test_client() as c:
        yield c


def test_list_tasks_empty(client):
    r = client.get("/tasks")
    assert r.status_code == 200
    assert r.get_json() == []


def test_create_task(client):
    r = client.post("/tasks", json={"title": "Write tests"})
    assert r.status_code == 201
    assert "id" in r.get_json()


def test_create_task_missing_title(client):
    r = client.post("/tasks", json={"description": "no title"})
    assert r.status_code == 400


def test_get_task(client):
    created = client.post("/tasks", json={"title": "Task A"}).get_json()
    r = client.get(f"/tasks/{created['id']}")
    assert r.status_code == 200
    assert r.get_json()["title"] == "Task A"


def test_get_task_not_found(client):
    r = client.get("/tasks/9999")
    assert r.status_code == 404


def test_update_task(client):
    created = client.post("/tasks", json={"title": "Task B"}).get_json()
    r = client.put(f"/tasks/{created['id']}", json={"status": "done"})
    assert r.status_code == 200


def test_delete_task(client):
    created = client.post("/tasks", json={"title": "Task C"}).get_json()
    r = client.delete(f"/tasks/{created['id']}")
    assert r.status_code == 200
    assert client.get(f"/tasks/{created['id']}").status_code == 404
