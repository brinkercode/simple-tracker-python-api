from fastapi import APIRouter, HTTPException
import json
import random
from ..models import Client

router = APIRouter()

# Read in JSON test data
def read_in_json():
    with open(DATA) as f:
        data = json.load(f)
    return data

DATA='./data.json'
data=read_in_json()

# Check if client exists
def _client_exists(client_id: int):
    for client in data["clients"]:
        if client["id"] == client_id:
            return True
    return False

# Generate random ID for client
def generate_random_id():
    return len(data["clients"]) + 1

# # Check if required values exist
# def _required_values_exist(client: Client):
#     if not client.name:
#         raise HTTPException(status_code=400, detail="Missing client name")
#     if not client.url:
#         client.url = None
#     return True

# Get all Clients
@router.get("/clients")
async def root():
    return data["clients"]

# Get client by ID
@router.get("/clients/{client_id}")
async def get_client(client_id: int):
    if not _client_exists(client_id):
        raise HTTPException(status_code=404, detail="Client not found")
    for client in data["clients"]:
        if client["id"] == client_id:
            return client

# Create new client
@router.post("/clients")
async def create_client(client: Client):
    client_id = generate_random_id()
    client_dict = client.dict()
    client_dict["id"] = client_id
    data["clients"].append(client_dict)
    return {"id": client_id, **client_dict}

# Update client by ID
@router.put("/clients/{client_id}")
async def update_client(client_id: int, client: Client):
    if not _client_exists(client_id):
        raise HTTPException(status_code=404, detail="Client not found")
    else:
        for c in data["clients"]:
            if c["id"] == client_id:
                c["name"] = client.name
                c["url"] = client.url
                updated_client = {"id": client_id, "name": client.name, "url": client.url}
                return updated_client
    return {"Client with ID: {}".format(client_id): "Updated"}

# Delete client by ID
@router.delete("/clients/{client_id}")
async def delete_client(client_id: int):
    if not _client_exists(client_id):
        raise HTTPException(status_code=404, detail="Client not found")
    for c in data["clients"]:
        if c["id"] == client_id:
            data["clients"].remove(c)
            return {"message": "Client deleted"}
