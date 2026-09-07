from repository.user_repository import StudentRepository


class StudentService:

    def __init__(self):#Initialize the Service object when it is created.

        self.repository = StudentRepository()#Create and store a Repository object.


    def _student_to_dict(self, student):

        return {
            "id": student[0],
            "name": student[1],
            "email": student[2],
            "department": student[3],
            "age": student[4]
        }


    # ============================================================
    # GET ALL STUDENTS SERVICE
    # ============================================================

    def get_students(self):

        students = self.repository.get_all_students()#Ask the Repository to get all students from PostgreSQL.

        result = []#this will hold the list of students in dictionary format.

        for student in students:

            result.append( 
                self._student_to_dict(student)
            )

        return result


    # ============================================================
    # GET STUDENT BY ID SERVICE
    # ============================================================

    def get_student(self, student_id: int):

        student = self.repository.get_student_by_id(student_id)#Ask the Repository to get the student from PostgreSQL.

        if student is None:
            return None

        return self._student_to_dict(student)#if the student is found, convert it to a dictionary and return it.


    # ============================================================
    # CREATE STUDENT SERVICE
    # ============================================================

    def create_student(self, student):

        new_student = self.repository.create_student(student)

        return self._student_to_dict(new_student)


    # ============================================================
    # UPDATE STUDENT SERVICE
    # ============================================================

    def update_student(self, student_id: int, student):

        updated_student = self.repository.update_student(
            student_id,
            student
        )

        if updated_student is None:
            return None

        return self._student_to_dict(updated_student)


    # ============================================================
    # DELETE STUDENT SERVICE
    # ============================================================

    def delete_student(self,    student_id: int):

        deleted_student = self.repository.delete_student(student_id)

        if deleted_student is None:
            return None

        return {
            "id": deleted_student[0],
            "message": "Student deleted successfully"
        }