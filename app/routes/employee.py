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

DATA='./data.json'
data=read_in_json()

# Generate random ID for user ID
def generate_random_id():
    return random.randint(1, 100000)

# Check if employee exists
def _employee_exists(employee_id: int):
    for employee in data["employees"]:
        if employee["id"] == employee_id:
            return True
    return False

# Check if required values exist
def _required_values_exist(client: Employee):
    if not employee.name:
        raise HTTPException(status_code=400, detail="Missing client name")
    if not employee.github:
        employee.github = None
    return True

# Get all employees
@router.get("/employees")
async def root():
    return data["employees"]

#TODO: Fix bad employee. Missing value should return a 400
# Create employee
@router.post("/employees")
async def create_employee(employee: Employee):
    employee_id = generate_random_id()
    employee_dict = employee.dict()
    employee_dict["id"] = employee_id
    data["employees"].append(employee_dict)
    return {"id": employee_id, **employee_dict}

# Get employee by ID
@router.get("/employees/{employee_id}")
async def get_employee(employee_id: int):
    if not _employee_exists(employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    for employee in data["employees"]:
        if employee["id"] == employee_id:
            return employee

#TODO: Fix illegal update to ID, return 400
# Update employee by ID
@router.put("/employees/{employee_id}")
async def update_employee(employee_id: int, employee: Employee):
    if not _employee_exists(employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    else:
        for emp in data["employees"]:
            if emp["id"] == employee_id:
                emp["name"] = employee.name
                if employee.github:
                    emp["github"] = employee.github
                    _required_values_exist(employee)
                    employee = Employee(**emp)
                    return {"id": employee_id, **employee.dict()}
                else:
                    emp["github"] = "github missing"
                    employee = Employee(**emp)
                    return {"id": employee_id, **employee.dict()}

# Delete employee by ID
@router.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    if not _employee_exists(employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    for employee in data["employees"]:
        if employee["id"] == employee_id:
            data["employees"].remove(employee)
            return {"Employee with ID: {}".format(employee_id): "Deleted"}