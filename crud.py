
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Student Management API")


# Pydantic model for student data
class Student(BaseModel):
    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    department: str = Field(min_length=1)


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


# HOME ENDPOINT
@app.get("/")
def home():
    return {
        "message": "Welcome to Student Management API!",
        "status": "Running"
    }


# READ: Get all students, optionally filter by department
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


# READ: Get one student by ID
@app.get("/students/{student_id}")
def get_student(student_id: str):
    student = students.get(student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student


# CREATE: Add a new student
@app.post(
    "/students",
    status_code=status.HTTP_201_CREATED
)
def create_student(student: Student):
    if student.id in students:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Student ID already exists"
        )

    students[student.id] = student.model_dump()

    return {
        "message": "Student created successfully",
        "student": students[student.id]
    }


# UPDATE: Replace all student fields
@app.put("/students/{student_id}")
def update_student(student_id: str, student: Student):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    if student.id != student_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student ID in the body must match the URL"
        )

    students[student_id] = student.model_dump()

    return {
        "message": "Student updated successfully",
        "student": students[student_id]
    }


# DELETE: Remove a student
@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }
