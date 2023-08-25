# from fastapi import APIRouter, HTTPException
# import json
# from ..models import Client

# router = APIRouter()
# DATA='./data.json'

# def read_in_json():
#     with open(DATA) as f:
#         data = json.load(f)
#     return data

# data=read_in_json()

# @router.get("/clients")
# async def root():
#     return data["clients"]
