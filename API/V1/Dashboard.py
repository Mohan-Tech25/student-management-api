from fastapi import APIRouter

from Service.dashboard_service import DashboardService


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


dashboard_service = DashboardService()


# ============================================================
# TOTAL STUDENTS
# ============================================================

@router.get("/")
def dashboard():

    return dashboard_service.get_total_students()


# ============================================================
# STUDENTS BY DEPARTMENT
# ============================================================

@router.get("/department-count")
def department_count():

    return dashboard_service.get_students_by_department()


# ============================================================
# AVERAGE AGE
# ============================================================

@router.get("/average-age")
def average_age():

    return dashboard_service.get_average_age()


# ============================================================
# OLDEST STUDENT
# ============================================================

@router.get("/oldest-student")
def oldest_student():

    return dashboard_service.get_oldest_student()