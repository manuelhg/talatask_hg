from sqlalchemy.orm import Session
from models import Employee, Task
from typing import List
import logging

# Función que verifica si un empleado tiene las habilidades necesarias
def has_required_skills(employee_skills: List[str], task_skills: List[str]) -> bool:
    return set(task_skills).issubset(set(employee_skills))


# Configuración básica de logging
logging.basicConfig(level=logging.INFO)

# Algoritmo para asignar tareas
def assign_tasks(db: Session):
    employees = db.query(Employee).all()
    tasks = db.query(Task).all()
    
    #revisando lo que esta en BD
    #print(f"Tareas: {tasks}")
    #print(f"Empleados: {employees}")

    # Crear un diccionario para almacenar las asignaciones
    assignments = {}

    for task in tasks:
        # Filtrar empleados que están disponibles en la fecha de la tarea
        logging.info("Evaluando tarea: %s", task.title)

        available_employees = [
            # employee for employee in employees
            # if task.date in employee.available_days
            # and employee.availability_hours >= task.duration_hours
            # and has_required_skills(employee.skills.split(','), task.required_skills.split(','))
           
               employee for employee in employees
            if task.date in employee.available_days  # Se asume que available_days es una lista JSON
            and employee.availability_hours >= task.duration_hours
            and has_required_skills(employee.skills, task.required_skills)  # No es necesario el split
        ]
        
        logging.info("Empleados disponibles: %s", available_employees)

        if available_employees:
            # Ordenar por disponibilidad (opcional, para asignar al más disponible)
            available_employees.sort(key=lambda e: e.availability_hours, reverse=True)
            
            # Asignar la tarea al primer empleado disponible
            selected_employee = available_employees[0]

            # Actualizar la disponibilidad horaria del empleado
            selected_employee.availability_hours -= task.duration_hours

            # Registrar la asignación
            if selected_employee.name not in assignments:
                assignments[selected_employee.name] = []
            assignments[selected_employee.name].append(task.title)

            # Actualizar la base de datos
            db.commit()

    return assignments

# Obtener las asignaciones para un día específico
def get_task_assignments(db: Session, date: str):
    tasks = db.query(Task).filter(Task.date == date).all()
    print(f"Tareas para la fecha {date}: {tasks}")
    assignments = assign_tasks(db)
    
    # Crear una lista de tareas asignadas para el día solicitado
    task_assignments = {
        "date": date,
        "assignments": []
    }

    for employee, assigned_tasks in assignments.items():
        task_assignments["assignments"].append({
            "employee": employee,
            "tasks": assigned_tasks
        })

    return task_assignments
