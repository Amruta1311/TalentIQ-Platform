from fastapi.testclient import TestClient
from resume_match.main import app

client = TestClient(app)


def test_match():
    res = client.post("/match", json={
        "resume": "Python ML Engineer",
        "job": "Looking for ML engineer"
    })

    assert res.status_code == 200
    assert "match_score" in res.json()