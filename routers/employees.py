# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# #from models import models
# from models import Employee
# from models import Task
# #from schemas import schemas
# from schemas import Employee
# from schemas import Task
# from schemas import EmployeeCreate
# from schemas import TaskCreate
# from database import Base
# from database import get_db
# from database import SessionLocal

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Employee as ModelEmployee  # Asegúrate de usar el modelo de SQLAlchemy
from schemas import Employee as SchemaEmployee, EmployeeCreate
from database import get_db



router = APIRouter(
    prefix="/employees",
    tags=["employees"]
)

@router.post("/", response_model=SchemaEmployee)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = ModelEmployee(**employee.dict())  # Usa el modelo de SQLAlchemy
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.get("/", response_model=list[SchemaEmployee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    employees = db.query(ModelEmployee).offset(skip).limit(limit).all()  # Usa el modelo de SQLAlchemy
    return employees

# router = APIRouter(
#     prefix="/employees",
#     tags=["employees"]
# )

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/", response_model=Employee)
# def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
#     db_employee = Employee(**employee.dict())
#     db.add(db_employee)
#     db.commit()
#     db.refresh(db_employee)
#     return db_employee

# @router.get("/", response_model=list[Employee])
# def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     employees = db.query(Employee).offset(skip).limit(limit).all()
#     return employees
