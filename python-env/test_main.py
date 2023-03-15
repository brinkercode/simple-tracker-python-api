
from fastapi.testclient import TestClient
import json
from main import app
from uuid import UUID, uuid4 
DATA='./dummy-data.json'

def read_in_json():
    with open(DATA) as f:
        data = json.load(f)
    return data

data=read_in_json()

def test_read_main():
    with TestClient(app) as client:
        response = client.get("/employees")
        assert response.status_code == 200
        assert response.json() == data["employees"]

def test_create_employee():
    with TestClient(app) as client:
        response = client.post("/employees", json={"name": "Test", "github": "test"})
        assert response.status_code == 201
        assert isinstance(response.json()["id"], int)
        json_data = json.loads(response.text)
        json_data.pop("id")
        assert json_data == {"name": "Test", "github": "test"}

def test_get_employee():    
    with TestClient(app) as client:
        response = client.get("/employees/1")
        assert response.status_code == 200
        assert response.json() == data["employees"][1]

def test_update_employee():
    with TestClient(app) as client:
        response = client.put("/employees/1", json={"name": "Test", "github": "test"})
        assert response.status_code == 200
        assert isinstance(response.json()["id"], int)
        json_data = json.loads(response.text)
        json_data.pop("id")
        assert json_data == {"employee_id":1,"name": "Test", "github": "test"}

def test_delete_employee():
    with TestClient(app) as client:
        response = client.delete("/employees/1")
        assert response.status_code == 200
        assert response.json() == {"Employee with ID: 1": "Deleted"}

def test_read_main():
    with TestClient(app) as client:
        response = client.get("/clients")
        assert response.status_code == 200
        assert response.json() == data["clients"]

def test_create_client():
    with TestClient(app) as client:
        response = client.post("/clients", json={"name": "Test", "url": "test"})
        assert response.status_code == 201
        assert isinstance(response.json()["id"], int)
        json_data = json.loads(response.text)
        json_data.pop("id")
        assert  json_data == {"name": "Test", "url": "test"}

def test_get_client():    
    with TestClient(app) as client:
        response = client.get("/clients/1")
        assert response.status_code == 200
        assert response.json() == data["clients"][1]

def test_update_client():
    with TestClient(app) as client:
        response = client.put("/clients/1", json={"name": "Test", "url": "test"})
        assert response.status_code == 200
        assert isinstance(response.json()["id"], int)
        json_data = json.loads(response.text)
        json_data.pop("id")
        assert json_data== {"client_id": 1, "name": "Test", "url": "test"}

def test_delete_client():
    with TestClient(app) as client:
        response = client.delete("/clients/1")
        assert response.status_code == 200
        assert response.json() == {"Client with ID: 1": "Deleted"}

# Path: python-env/tests/test_main.py