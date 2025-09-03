import json
import pytest
from app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get("/")
    assert res.status_code == 200
    body = res.get_json()
    assert body["status"] == "ok"

def test_add_workout_success(client):
    payload = {"workout": "Running", "duration": 30}
    res = client.post("/add_workout", data=json.dumps(payload),
                      content_type="application/json")
    assert res.status_code == 201
    body = res.get_json()
    assert body["ok"] is True
    assert body["data"]["workout"] == "Running"
    assert body["data"]["duration"] == 30

def test_add_workout_validation_error(client):
    # duration not integer
    payload = {"workout": "Cycling", "duration": "thirty"}
    res = client.post("/add_workout", data=json.dumps(payload),
                      content_type="application/json")
    assert res.status_code == 400
    body = res.get_json()
    assert body["ok"] is False
    assert any("duration must be an integer" in e for e in body["errors"])

def test_list_workouts(client):
    client.post("/add_workout", json={"workout": "Yoga", "duration": 20})
    res = client.get("/workouts")
    body = res.get_json()
    assert res.status_code == 200
    assert body["count"] == 1
    assert body["items"][0]["workout"] == "Yoga"
