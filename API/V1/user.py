from fastapi import APIRouter, HTTPException

from schemas.user_schema import (
    StudentCreate,
    StudentUpdate,
    
)

from Service.user_service import StudentService


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


student_service = StudentService()


# ============================================================
# GET ALL STUDENTS
# ============================================================

@router.get("/")
def get_students():

    return student_service.get_students()


# ============================================================
# GET STUDENT BY ID
# ============================================================

@router.get("/{student_id}")
def get_student(student_id: int):

    student = student_service.get_student(student_id)

    if student is None:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# ============================================================
# CREATE STUDENT
# ============================================================

@router.post("/")
def create_student(student: StudentCreate):

    return student_service.create_student(student)


# ============================================================
# UPDATE STUDENT
# ============================================================

@router.patch("/{student_id}")
def update_student(
    student_id: int,
    student: StudentUpdate
):

    updated_student = student_service.update_student(
        student_id,
        student
    )

    if updated_student is None:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated_student


# ============================================================
# DELETE STUDENT
# ============================================================

@router.delete("/{student_id}")
def delete_student(student_id: int):

    deleted_student = student_service.delete_student(
        student_id
    )

    if deleted_student is None:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return deleted_student