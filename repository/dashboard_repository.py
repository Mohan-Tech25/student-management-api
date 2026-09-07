from database.connection import get_connection


class DashboardRepository:

    # ============================================================
    # GET TOTAL STUDENTS
    # ============================================================

    def get_total_students(self):

        with get_connection() as connection:

            cursor = connection.cursor()

            query = """
                SELECT COUNT(*)
                FROM students
            """

            cursor.execute(query)

            total_students = cursor.fetchone()

            cursor.close()

            return total_students


    # ============================================================
    # GET STUDENTS BY DEPARTMENT
    # ============================================================

    def get_students_by_department(self):

        with get_connection() as connection:

            cursor = connection.cursor()

            query = """
                SELECT department, COUNT(*)
                FROM students
                GROUP BY department
                ORDER BY department
            """

            cursor.execute(query)

            department_counts = cursor.fetchall()

            cursor.close()

            return department_counts


    # ============================================================
    # GET AVERAGE AGE
    # ============================================================

    def get_average_age(self):

        with get_connection() as connection:

            cursor = connection.cursor()

            query = """
                SELECT AVG(age)
                FROM students
            """

            cursor.execute(query)

            average_age = cursor.fetchone()

            cursor.close()

            return average_age


    # ============================================================
    # GET OLDEST STUDENT
    # ============================================================

    def get_oldest_student(self):

        with get_connection() as connection:

            cursor = connection.cursor()

            query = """
                SELECT id, name, age
                FROM students
                ORDER BY age DESC
                LIMIT 1
            """

            cursor.execute(query)

            oldest_student = cursor.fetchone()

            cursor.close()

            return oldest_student