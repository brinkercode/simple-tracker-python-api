from fastapi import FastAPI, HTTPException, Response, status, Request
from models.models import Employee, Client, Contract, History
from fastapi.middleware.cors import CORSMiddleware
import json
import os
import logging
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
logging.basicConfig(level=logging.DEBUG)
app = FastAPI(port=8081)
DATA='./dummy-data.json'

# TODO: add status_codes 404, 400, 201
# TODO: Database agnostic methods


# Middleware
# Change this to your own origins
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8081"
]
# HTTPS only
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

def _employee_exists(employee_id) -> bool:
    for employee in data["employees"]:
        if employee["id"] == employee_id:
            return True
    return False   

@app.post("/employees", status_code=201)
async def create_employee(employee: Employee) -> Employee:
    data["employees"].append(employee)
    return employee

@app.get("/employees/{employee_id}")
async def get_employee(employee_id: int):
    if not _employee_exists(employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    for employee in data["employees"]:
        if employee["id"] == employee_id:
            return employee

@app.put("/employees/{employee_id}")
async def update_employee(employee_id: int, employee: Employee):
    if not _employee_exists(employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"employee_id": employee_id, **employee.dict()}


@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
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

@app.post("/clients", status_code=200)
async def create_client(client: Client, response: Response):
    if client != None:
        data["clients"].append(client)
        return client
    else:
        response.status_code=status.HTTP_400_CLIENT_ERROR
        raise HTTPException(status_code=400, detail="Client Error")

@app.get("/clients/{client_id}", status_code=200)
async def get_client(client_id: int):
    if not _client_exists(client_id):
        raise HTTPException(status_code=404, detail="Client not found")
    else:
        return data['clients'][client_id]

@app.put("/clients/{client_id}", status_code=200)
async def update_client(client_id: int, client: Client, request: Request):
    inbound=await request.json()
    # Problem here as it fetches client automaitcally which includes ID.
    if not _client_exists(client_id):
        raise HTTPException(status_code=404, detail="Client not found.")
    # Using privateAttrs to prevent updating ID but request allows meeting spec.
    elif inbound.get("_id") != None:
        raise HTTPException(status_code=400, detail="Cannot update primary id.")
    else:
        return {"client_id": client_id, **client.dict()}


@app.delete("/clients/{client_id}")
async def delete_client(client_id: int):
    for client in data["clients"]:
        if client["id"] == client_id:
            data["clients"].remove(client)
            return {f"Client with ID: {client_id}": "Deleted"}
    raise HTTPException(status_code=404, detail="Client not found")
# Contracts

@app.get("/contracts")
async def root():
    return data["contracts"]

def _contract_exists(contract_id):
    for contract in data["contracts"]:
        if contract["id"] == contract_id:
            return True
    return False

@app.post("/contracts", status_code=201)
async def create_contract(contract: Contract):
    return contract

@app.get("/contracts/{contract_id}")
async def get_contract(contract_id: int):
    if not _contract_exists(contract_id):
        raise HTTPException(status_code=404, detail="Contract not found")
    for contract in data["contracts"]:
        if contract["id"] == contract_id:
            return {"contract_id": contract}

@app.put("/contracts/{contract_id}")
async def update_contract(contract_id: int, contract: Contract):
    if _contract_exists(contract_id):
        return {"contract_id": contract_id, **contract.dict()}
    return {"contract_id": "Not found"}

@app.delete("/contracts/{contract_id}")
async def delete_contract(contract_id: int):
    for contract in data["contracts"]:
        if contract["id"] == contract_id:
            data["contracts"].remove(contract)
    return {f"Contract with ID: {contract_id}": "Deleted"}

# History

@app.get("/history")
async def root():
    return data["history"]  

def _history_exists(history_id):
    for history in data["history"]:
        if history["id"] == history_id:
            return True
    return False

@app.post("/history", status_code=201)
async def create_history(history: History):
    return history

@app.get("/history/{history_id}")
async def get_history(history_id: int):
    if not _history_exists(history_id):
        raise HTTPException(status_code=404, detail="History not found")
    for history in data["history"]:
        if history["id"] == history_id:
            return history
   
@app.put("/history/{history_id}")
async def update_history(history_id: int, history: History):
    if _history_exists(history_id):
        return {"history_id": history_id, **history.dict()}
    return {"history_id": "Not found"}

@app.delete("/history/{history_id}")
async def delete_history(history_id: int):
    for history in data["history"]:
        if history["id"] == history_id:
            data["history"].remove(history)
    return {f"History with ID: {history_id}": "Deleted"}