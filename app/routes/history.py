from fastapi import APIRouter, HTTPException
import json
from ..models import History

router = APIRouter()

# Read in JSON test data
def read_in_json():
    with open(DATA) as f:
        data = json.load(f)
    return data

DATA='./data.json'
data=read_in_json()

# Generate random ID for history
def generate_random_id():
    return len(data["history"]) + 1

# Check if history exists
def _history_exists(history_id: int):
    for history in data["history"]:
        if history["id"] == history_id:
            return True
    return False

# Get all history
@router.get('/history')
async def root():
    return data["history"]

# Get history by ID
@router.get("/history/{history_id}")
async def get_history(history_id: int):
    if not _history_exists(history_id):
        raise HTTPException(status_code=404, detail="history not found")
    for history in data["history"]:
        if history["id"] == history_id:
            return history

# Create new history
@router.post("/history")
async def create_history(history: History):
    history.id = generate_random_id()
    data["history"].append(history.dict())
    return history
