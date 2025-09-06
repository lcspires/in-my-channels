import sys, os # temporary gambiearra
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import json
from app import app

def test_search_route():
    client = app.test_client()

    # busca por python deve retornar 2 resultados
    response = client.get("/search?q=python")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data["results"]) == 2

    # busca vazia deve retornar lista vazia
    response = client.get("/search")
    data = json.loads(response.data)
    assert data["results"] == []


