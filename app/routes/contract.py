# from fastapi import APIRouter, HTTPException
# import json
# import random
# from ..models import Contract

# router = APIRouter()

# # Read in JSON test data
# def read_in_json():
#     with open(DATA) as f:
#         data = json.load(f)
#     return data

# DATA='./data.json'
# data=read_in_json()

# # Generate random ID for user ID
# def generate_random_id():
#     return random.randint(1, 100000)

# # Check if contract exists
# def _contract_exists(contract_id: int):
#     for contract in data["contracts"]:
#         if contract["id"] == contract_id:
#             return True
#     return False

# # Check if required values exist
# def _required_values_exist(contract: Contract):
#     if not isinstance(contract.clientId, int):
#         raise HTTPException(status_code=400, detail="Missing clientId")
#     if not contract.type:
#         raise HTTPException(status_code=400, detail="Missing contract type")
#     if not contract.startDate:
#         raise HTTPException(status_code=400, detail="Missing contract startDate")
#     if not contract.endDate:
#         raise HTTPException(status_code=400, detail="Missing contract endDate")
#     if not contract.tech:
#         raise HTTPException(status_code=400, detail="Missing contract tech")
#     return True

# # Get all contracts
# @router.get("/contracts")
# async def root():
#     return data["contracts"]

# # Get contract by ID
# @router.get("/contracts/{contract_id}")
# async def get_contract(contract_id: int):
#     if not _contract_exists(contract_id):
#         raise HTTPException(status_code=404, detail="Contract not found")
#     for c in data["contracts"]:
#         if c["id"] == contract_id:
#             return c

# # Create contract
# @router.post("/contracts")
# async def create_contract(contract: Contract):
#     contract_id = generate_random_id()
#     contract_dict = contract.dict()
#     contract_dict = {"id": contract_id, **contract_dict}
#     _required_values_exist(contract)
#     data["contracts"].append(contract_dict)
#     return contract_dict

# # Delete contract by ID
# @router.delete("/contracts/{contract_id}")
# async def delete_contract(contract_id: int):
#     if not _contract_exists(contract_id):
#         raise HTTPException(status_code=404, detail="Contract not found")
#     for c in data["contracts"]:
#         if c["id"] == contract_id:
#             data["contracts"].remove(c)
#             return {"message": "Contract deleted"}