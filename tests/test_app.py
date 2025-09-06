import sys, os # temporary gambiearra
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import json
from app import app


def test_subscriptions_route():
    client = app.test_client()
    response = client.get("/subscriptions")

    assert response.status_code == 200

    data = json.loads(response.data)
    assert "subscriptions" in data
    assert isinstance(data["subscriptions"], list)
    assert len(data["subscriptions"]) > 0

def test_search_route():
    client = app.test_client()

    response = client.get("/search?q=python")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data["results"]) == 2

    response = client.get("/search")
    data = json.loads(response.data)
    assert data["results"] == []
