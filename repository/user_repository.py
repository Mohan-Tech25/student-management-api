from database.connection import get_connection


class StudentRepository:

    # ============================================================
    # GET ALL STUDENTS
    # ============================================================

    def get_all_students(self):

        with get_connection() as connection:

            with connection.cursor() as cursor:

                query = """
                    SELECT id, name, email, department, age
                    FROM students
                    ORDER BY id
                """

                cursor.execute(query)

                students = cursor.fetchall()

                return students


    # ============================================================
    # GET STUDENT BY ID
    # ============================================================

    def get_student_by_id(self, student_id: int):

        with get_connection() as connection:

            with connection.cursor() as cursor:

                query = """
                    SELECT id, name, email, department, age
                    FROM students
                    WHERE id = %s
                """

                cursor.execute(query, (student_id,))

                student = cursor.fetchone()

                return student


    # ============================================================
    # CREATE STUDENT
    # ============================================================

    def create_student(self, student):

        with get_connection() as connection:

            try:

                with connection.cursor() as cursor:

                    query = """
                        INSERT INTO students
                        (name, email, department, age)
                        VALUES (%s, %s, %s, %s)
                        RETURNING id, name, email, department, age
                    """

                    cursor.execute(
                        query,
                        (
                            student.name,
                            student.email,
                            student.department,
                            student.age
                        )
                    )

                    new_student = cursor.fetchone()

                    connection.commit()

                    return new_student

            except Exception:

                connection.rollback()

                raise


    # ============================================================
    # UPDATE STUDENT
    # ============================================================

    def update_student(self, student_id: int, student):

        with get_connection() as connection:

            try:

                with connection.cursor() as cursor:

                    fields = []#to hold the fields to be updated
                    values = []#to hold the values for the fields to be updated

                    if student.name is not None:
                        fields.append("name = %s")
                        values.append(student.name)

                    if student.email is not None:
                        fields.append("email = %s")
                        values.append(student.email)

                    if student.department is not None:
                        fields.append("department = %s")
                        values.append(student.department)

                    if student.age is not None:
                        fields.append("age = %s")
                        values.append(student.age)

                    if not fields:
                        return None

                    values.append(student_id)

                    query = f"""
                        UPDATE students
                        SET {", ".join(fields)}
                        WHERE id = %s
                        RETURNING id, name, email, department, age
                    """

                    cursor.execute(query, tuple(values))

                    updated_student = cursor.fetchone()

                    connection.commit()

                    return updated_student

            except Exception:

                connection.rollback()

                raise


    # ============================================================
    # DELETE STUDENT
    # ============================================================

    def delete_student(self, student_id: int):

        with get_connection() as connection:

            try:

                with connection.cursor() as cursor:

                    query = """
                        DELETE FROM students
                        WHERE id = %s
                        RETURNING id
                    """

                    cursor.execute(query, (student_id,))

                    deleted_student = cursor.fetchone()

                    connection.commit()

                    return deleted_student

            except Exception:

                connection.rollback()

                raise#sends the original error upward to the Service/API instead of hiding it