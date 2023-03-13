from fastapi import FastAPI
from models import Employee, Client, Contract
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

import json

app = FastAPI()
DATA='dummy-data.json'

# Middleware
# Change this to your own origins
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]
# app.add_middleware(HTTPSRedirectMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_in_json():
    with open(DATA) as f:
        data = json.load(f)
    return data

data=read_in_json()
# Employees
@app.get("/employees")
async def root():
    return data["employees"]

def _employee_exists(employee_id):
    for employee in data["employees"]:
        if employee["id"] == employee_id:
            return True
    return False   

@app.post("/employees")
async def create_employee(employee: Employee):
    return employee

@app.get("/employees/{employee_id}")
async def get_employee(employee_id: int):
    if _employee_exists(employee_id):
        return {"employee_id": employee}
    return {"employee_id": "Not found"}

@app.put("/employees/{employee_id}")
async def update_employee(employee_id: int, employee: Employee):
    if _employee_exists(employee_id):
        return {"employee_id": employee_id, **employee.dict()}
    return {"employee_id": "Not found"}

@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    # TODO: Add code to delete employee
    for employee in data["employees"]:
        if employee["id"] == employee_id:
            data["employees"].remove(employee)
    return {f"Employee with ID: {employee_id}": "Deleted"}

# Clients
@app.get("/clients")
async def root():
    return data["clients"]

def _client_exists(client_id):
    for client in data["clients"]:
        if client["id"] == client_id:
            return True
    return False

@app.post("/clients")
async def create_client(client: Client):
    return client

@app.get("/clients/{client_id}")
async def get_client(client_id: int):
    if _client_exists(client_id):
        return {"client_id": client}
    return {"client_id": "Not found"}

@app.put("/clients/{client_id}")
async def update_client(client_id: int, client: Client):
    if _client_exists(client_id):
        return {"client_id": client_id, **client.dict()}
    return {"client_id": "Not found"}

@app.delete("/clients/{client_id}")
async def delete_client(client_id: int):
    for client in data["clients"]:
        if clients["id"] == client_id:
            data["clients"].remove(client)
    return {f"Client with ID: {client_id}": "Deleted"}

# Contracts

@app.get("/contracts")
async def root():
    return data["contracts"]

def _contract_exists(contract_id):
    for contract in data["contracts"]:
        if contract["id"] == contract_id:
            return True
    return False

@app.post("/contracts")
async def create_contract(contract: Contract):
    return contract

# TODO: Database agnostic methods


def main():
    uvicorn.run(app, host="")

if __name__ =="__main__":
    main()

# Contracts