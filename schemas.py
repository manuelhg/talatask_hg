from pydantic import BaseModel
from typing import List, Optional

class EmployeeCreate(BaseModel):
    name: str
    skills: List[str]
    availability_hours: int
    available_days: List[str]

class TaskCreate(BaseModel):
    title: str
    required_skills: List[str]
    duration_hours: int
    date: str

class Employee(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True

class Task(TaskCreate):
    id: int

    class Config:
        orm_mode = True
