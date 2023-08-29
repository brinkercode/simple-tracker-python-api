from fastapi import APIRouter, HTTPException
import json
import random
from ..models import Employee

router = APIRouter()

# Read in JSON test data
def read_in_json():
    with open(DATA) as f:
        data = json.load(f)
    return data

DATA = './data.json'
data = read_in_json()

def _employee_exists(employee_id: int):
    for employee in data["employees"]:
        if employee["id"] == employee_id:
            return True
    return False

def generate_random_id():
    return len(data["employees"]) + 1

@router.get("/employees")
async def root():
    return data["employees"]

# Check if required values exist
# def _required_values_exist(client: Employee):
#     if not employee.name:
#         raise HTTPException(status_code=400, detail="Missing client name")
#     if not employee.github:
#         employee.github = None
#     return True

@router.get("/employees/{employee_id}")
async def get_employee(employee_id: int):
    if not _employee_exists(employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    for employee in data["employees"]:
        if employee["id"] == employee_id:
            return employee

# TODO: Fix bad employee. Missing value should return a 400
@router.post("/employees")
async def create_employee(employee: Employee):
    employee_id = generate_random_id()
    employee_dict = employee.dict()
    employee_dict["id"] = employee_id
    data["employees"].append(employee_dict)
    return {"id": employee_id, **employee_dict}

# TODO: Fix illegal update to ID, return 400
@router.put("/employees/{employee_id}")
async def update_employee(employee_id: int, employee: Employee):
    if not _employee_exists(employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    else:
        for emp in data["employees"]:
            if emp["id"] == employee_id:
                emp["name"] = employee.name
                emp["github"] = employee.github
                employee = Employee(**emp)
                return {"id": employee_id, **employee.dict()}
    return {"Employee with ID: {}".format(employee_id): "Updated"}

# Delete employee by ID
@router.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    if not _employee_exists(employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    for employee in data["employees"]:
        if employee["id"] == employee_id:
            data["employees"].remove(employee)
            return {"Employee with ID: {}".format(employee_id): "Deleted"}
