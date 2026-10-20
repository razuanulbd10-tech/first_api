
from fastapi import FastAPI, HTTPException

app = FastAPI(title="My First Classroom API")

# Sample data stored in a Python dictionary
students = {
    "101": {
        "id": "101",
        "name": "Rahim",
        "department": "CSE"
    },
    "102": {
        "id": "102",
        "name": "Nadia",
        "department": "EEE"
    }
}


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI!",
        "status": "Running"
    }


# GET: Retrieve students, optionally filtered by department
@app.get("/students")
def get_students(department: str | None = None):
    result = list(students.values())

    if department:
        result = [
            student
            for student in result
            if student["department"].lower() == department.lower()
        ]

    return {
        "count": len(result),
        "students": result
    }


# GET: Retrieve one student by ID
@app.get("/students/{student_id}")
def get_student(student_id: str):
    student = students.get(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student
