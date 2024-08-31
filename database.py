from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



def create_employee_table():
    from models import Employee   
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    if "employees" not in existing_tables:
        Base.metadata.create_all(bind=engine, tables=[Employee.__table__])

def create_task_table():
    from models import Task   
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    if "tasks" not in existing_tables:
        Base.metadata.create_all(bind=engine, tables=[Task.__table__])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    