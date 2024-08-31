# test_assign_tasks.py

# Importa tus funciones y clases
from typing import List

# Simula las clases Employee y Task, o impórtalas si ya están disponibles en tu proyecto.
class Employee:
    def __init__(self, id, name, skills, availability_hours, available_days):
        self.id = id
        self.name = name
        self.skills = skills
        self.availability_hours = availability_hours
        self.available_days = available_days

class Task:
    def __init__(self, id, title, required_skills, duration_hours, date):
        self.id = id
        self.title = title
        self.required_skills = required_skills
        self.duration_hours = duration_hours
        self.date = date

# Función que verifica si un empleado tiene las habilidades necesarias
def has_required_skills(employee_skills: List[str], task_skills: List[str]) -> bool:
    return set(task_skills).issubset(set(employee_skills))

# Algoritmo para asignar tareas (simulado sin base de datos)
def assign_tasks():
    # Simulación de datos de empleados y tareas
    employees = [
        Employee(id=1, name='Juan Pérez', skills='Python,SQL', availability_hours=40, available_days=['2024-09-18']),
        Employee(id=2, name='Ana Gómez', skills='JavaScript,HTML', availability_hours=30, available_days=['2024-09-18'])
    ]

    tasks = [
        Task(id=1, title='Desarrollar API', required_skills='Python', duration_hours=10, date='2024-09-18'),
        Task(id=2, title='Crear Página Web', required_skills='HTML,JavaScript', duration_hours=5, date='2024-09-18')
    ]
    
    # Crear un diccionario para almacenar las asignaciones
    assignments = {}

    for task in tasks:
        print(f"Evaluando tarea: {task.title}")

        available_employees = [
            employee for employee in employees
            if task.date in employee.available_days
            and employee.availability_hours >= task.duration_hours
            and has_required_skills(employee.skills.split(','), task.required_skills.split(','))
        ]

        print(f"Empleados disponibles para {task.title}: {[emp.name for emp in available_employees]}")

        if available_employees:
            available_employees.sort(key=lambda e: e.availability_hours, reverse=True)
            selected_employee = available_employees[0]
            selected_employee.availability_hours -= task.duration_hours

            if selected_employee.name not in assignments:
                assignments[selected_employee.name] = []
            assignments[selected_employee.name].append(task.title)

    return assignments

# Ejecuta la función de prueba
if __name__ == "__main__":
    assignments = assign_tasks()
    print(f"Asignaciones: {assignments}")
