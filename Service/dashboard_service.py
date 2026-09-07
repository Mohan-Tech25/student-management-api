from repository.dashboard_repository import DashboardRepository


class DashboardService:

    def __init__(self):

        self.repository = DashboardRepository()


    # ============================================================
    # GET TOTAL STUDENTS
    # ============================================================

    def get_total_students(self):

        total_students = self.repository.get_total_students()

        return {
            "total_students": total_students[0]
        }


    # ============================================================
    # GET STUDENTS BY DEPARTMENT
    # ============================================================

    def get_students_by_department(self):

        department_counts = self.repository.get_students_by_department()

        result = {}

        for department, count in department_counts:

            result[department] = count

        return result


    # ============================================================
    # GET AVERAGE AGE
    # ============================================================

    def get_average_age(self):

        average_age = self.repository.get_average_age()

        return {
            "average_age": float(average_age[0])
        }


    # ============================================================
    # GET OLDEST STUDENT
    # ============================================================

    def get_oldest_student(self):

        oldest_student = self.repository.get_oldest_student()

        if oldest_student is None:
            return None

        return {
            "oldest_student": {
                "id": oldest_student[0],
                "name": oldest_student[1],
                "age": oldest_student[2]
            }
        }