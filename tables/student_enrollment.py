from tables.database_engine import DatabaseManager

class StudentEnrollmentRepository(DatabaseManager):

    def create_student_enrollment(self, student_id, degree_program_id, semester_id, institution_name):
        query = "INSERT INTO student_enrollment( student_id, degree_program_id, semester_id, institution_name) VALUES (%s, %s, %s, %s)"
        parameter = (str(student_id), degree_program_id, semester_id, institution_name)
        self.execute_command(query,parameter)

    def get_all(self):
        query = "SELECT * FROM student_enrollment"  
        self.execute_query(query)

    def update_student_enrollment(self, student_id, degree_program_id, semester_id, institution_name, student_enrollment_id):
        query = "UPDATE student_enrollment SET student_id = %s, degree_program_id = %s, semester_id = %s, institution_name= %s WHERE student_enrollment_id = %s"
        parameter = ( student_id, degree_program_id, semester_id, institution_name, student_enrollment_id)
        self.execute_command(query,parameter)

    def delete_student_enrollment(self, student_enrollment_id):
        query = "DELETE FROM student_enrollment WHERE student_enrollment_id = %s"
        parameter = student_enrollment_id
        self.execute_command(query,parameter,True)

    def get_by_id(self, student_enrollment_id):
        query = "SELECT * FROM student_enrollment WHERE student_enrollment_id = %s"
        fetch_one =  True
        parameter = student_enrollment_id
        self.execute_query(query,parameter, fetch_one, True)

ad = StudentEnrollment()

ad.create_student_enrollment(2,2,2, 'fadsf')
# ad.update_student_enrollment(1,1,1,"superhero",1)
# # ad.delete_student_enrollment("sdsd")
# ad.read_student_enrollment()
ad.get_by_id(1)