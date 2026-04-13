from typing import Optional

from fastapi import FastAPI, Path

app = FastAPI()
# GET - GET AN INFORMATION
# POST - CREATE SOMETHING NEW
# PUT - UPDATE AN EXISTING RESOURCE
# DELETE - DELETE A RESOURCE

students = {1: {"name": "john", "age": 17, "class": "year 12"}}


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(
        description="The ID of the student you want to view", gt=0, lt=3
    ),
):
    return students[student_id]


@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}
