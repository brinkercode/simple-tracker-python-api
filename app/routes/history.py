# from fastapi import APIRouter, HTTPException
# import json
# import random
# from ..models import History

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
# def _history_exists(contract_id: int):
#     for history in data["history"]:
#         if history["id"] == history_id:
#             return True
#     return False

# @router.get("/history")
# async def root():
#     return data["history"]