from fastapi import FastAPI
from database import engine, create_employee_table, create_task_table
from models import Employee, Task
 
from database import get_db

from routers import employees, tasks
from sqlalchemy import inspect


# Inicializa la app FastAPI
app = FastAPI()

# Crear las tablas
# models.Base es creado por SQLAlchemy y contiene la definición de las tablas
#models.Base.metadata.create_all(bind=engine)
create_employee_table()
create_task_table()




# Incluir routers / endpoints
app.include_router(employees.router)  # Endpoints relacionados con empleados
app.include_router(tasks.router)      # Endpoints relacionados con tareas

# Endpoint raíz
# http://127.0.0.1:8000/
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API Asignadora de tareas"}


def list_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Tablas:", tables)

list_tables()

