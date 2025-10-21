from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed":"Gotland",
        "sex":"ewe"
    }



def test_add_sheep():
    test_sheep = {
        "id": 7,
        "name": "Clover",
        "breed": "Merino",
        "sex":"ewe"
    }
    response = client.post("/sheep/", json=test_sheep)
    assert response.status_code == 201
    assert response.json() == test_sheep

def getAllSheep():
    response = client.get("/sheep/")
    assert response.status_code == 200
