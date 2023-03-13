from fastapi import FastAPI
from fastapi.testclient import TestClient
from ../models import Employee, Client
from ../main import app
import json


DATA='../dummy-data.json'

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