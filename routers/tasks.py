from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
#from .. import models, schemas, database, services
import models
import schemas
import database
from services import get_task_assignments

from models import Employee

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = db.query(models.Task).offset(skip).limit(limit).all()
    return tasks

@router.get("/assignments/{date}")
def get_assignments(date: str, db: Session = Depends(get_db)):
    assignments = get_task_assignments(db, date)
    if not assignments:
        raise HTTPException(status_code=404, detail="No tasks found for this date")
    return assignments

