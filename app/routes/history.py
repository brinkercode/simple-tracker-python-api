from fastapi import APIRouter, HTTPException
import json
import random
from ..models import History

router = APIRouter()

# Read in JSON test data
def read_in_json():
    with open(DATA) as f:
        data = json.load(f)
    return data

DATA='./data.json'
data=read_in_json()

# Get all history
@router.get('/history')
async def get_history():
    return data["history"]

# Get employee contract assignment by ID
@router.get('/history/{history_id}')
async def get_history_by_id(history_id: int):
    history = next((h for h in data["history"] if h.id == history_id), None)
    if not history:
        raise HTTPException(status_code=404, detail="History not found")
    return history.dict()

# @router.get('/history/{history_id}')
# async def get_history_by_id(history_id: int):
#     history = next((h for h in data["history"] if h.id == history_id), None)
#     if not history:
#         raise HTTPException(status_code=404, detail="History not found")
#     return history.dict()

# @router.post('/history')
# async def create_history(history: History):
#     client = next((c for c in data["clients"] if c["id"] == history.clientId), None)
#     employee = next((e for e in data["employees"] if e["id"] == history.employeeId), None)
#     contract = next((c for c in data["contracts"] if c["id"] == history.contractId), None)
#     if not all([client, employee, contract]):
#         raise HTTPException(status_code=400, detail="Missing or invalid client, contract, or employee id")
#     history_dict = history.dict()
#     history_dict["clientName"] = client["name"]
#     history_dict["employeeName"] = employee["name"]
#     data["history"].append(history_dict)
#     return history_dict

# @router.put('/history/{history_id}')
# async def update_history(history_id: int, history: History):
#     existing_history = next((h for h in data["history"] if h["id"] == history_id), None)
#     if not existing_history:
#         raise HTTPException(status_code=404, detail="History not found")
#     if history.id:
#         raise HTTPException(status_code=400, detail="Cannot update primary id")
#     client = next((c for c in data["clients"] if c["id"] == history.clientId), None)
#     employee = next((e for e in data["employees"] if e["id"] == history.employeeId), None)
#     contract = next((c for c in data["contracts"] if c["id"] == history.contractId), None)
#     if not all([client, employee, contract]):
#         raise HTTPException(status_code=400, detail="Missing or invalid client, contract, or employee id")
#     history_dict = history.dict()
#     history_dict["clientName"] = client["name"]
#     history_dict["employeeName"] = employee["name"]
#     existing_history.update(history_dict)
#     return existing_history

# @router.delete('/history/{history_id}')
# async def delete_history(history_id: int):
#     existing_history = next((h for h in data["history"] if h["id"] == history_id), None)
#     if not existing_history:
#         raise HTTPException(status_code=404, detail="History not found")
#     data["history"].remove(existing_history)
#     return {"message": "History deleted"}
