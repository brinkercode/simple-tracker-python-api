from fastapi import APIRouter, HTTPException
import json
import random
from ..models import Contract

router = APIRouter()

# Read in JSON test data
def read_in_json():
    with open(DATA) as f:
        data = json.load(f)
    return data

DATA='./data.json'
data=read_in_json()

# Check if contract exists
def _contract_exists(contract_id: int):
    for contract in data["contracts"]:
        if contract["id"] == contract_id:
            return True
    return False

# Generate random ID for contract
def generate_random_id():
    return len(data["contracts"]) + 1

# Get all contracts
@router.get("/contracts")
async def get_contracts():
    return data["contracts"]

# Get contract by ID
@router.get("/contracts/{contract_id}")
async def get_contract(contract_id: int):
    if not _contract_exists(contract_id):
        raise HTTPException(status_code=404, detail="Contract not found")
    for contract in data["contracts"]:
        if contract["id"] == contract_id:
            return contract

# Create new contract
@router.post("/contracts")
async def create_contract(contract: Contract):
    contract_id = generate_random_id()
    contract_dict = contract.dict()
    contract_dict["id"] = contract_id
    data["contracts"].append(contract_dict)
    return {"id": contract_id, **contract_dict}

# Update contract by ID
@router.put("/contracts/{contract_id}")
async def update_contract(contract_id: int, contract: Contract):
    if not _contract_exists(contract_id):
        raise HTTPException(status_code=404, detail="Contract not found")
    else:
        for c in data["contracts"]:
            if c["id"] == contract_id:
                c["clientId"] = contract.clientId
                c["type"] = contract.type
                c["startDate"] = contract.startDate
                c["endDate"] = contract.endDate
                c["tech"] = contract.tech
                updated_contract = {"id": contract_id, "clientId": contract.clientId, "type": contract.type, "startDate": contract.startDate, "endDate": contract.endDate, "tech": contract.tech}
                return updated_contract
            return {"Contract with ID: {}".format(contract_id): "Updated"}
                
# Delete contract by ID
@router.delete("/contracts/{contract_id}")
async def delete_contract(contract_id: int):
    if not _contract_exists(contract_id):
        raise HTTPException(status_code=404, detail="Contract not found")
    else:
        for contract in data["contracts"]:
            if contract["id"] == contract_id:
                data["contracts"].remove(contract)
                return {"Contract with ID: {}".format(contract_id): "Deleted"}