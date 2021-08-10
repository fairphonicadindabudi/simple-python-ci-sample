from fastapi.testclient import TestClient

from fastapi_addition import app

client = TestClient(app)

def test_read_main():
    response = client.get("/addition?a={}&b={}".format(1, 1))
    assert response.status_code == 200
    assert response.json() == {"result": 2}

    response = client.get("/addition?a={}&b={}".format(-1, 1))
    assert response.status_code == 200
    assert response.json() == {"result": 0}

    response = client.get("/addition?a={}&b={}".format(76, 59))
    assert response.status_code == 200
    assert response.json() == {"result": 135}