from database_manager import DatabaseManager


class StudentEnrollmentCourse(DatabaseManager):
        
    def create_student_enrollment_course(self, student_enrollment_id, course_id):
        query = "INSERT INTO student_enrollment_courses(student_enrollment_id, course_id) VALUES (%s,%s)"
        parameter =  student_enrollment_id, course_id
        self.execute_command(query,parameter)  
       
    def read_student_enrollment_courses(self):
        query = "SELECT * FROM student_enrollment_courses"
        self.execute_query(query)
    
    def update_student_enrollment_courses(self, student_enrollment_id, course_id, student_course_id):
        query = "UPDATE student_enrollment_courses SET student_enrollment_id = %s, course_id =  %s  WHERE student_course_id = %s"
        parameter = ( student_enrollment_id, course_id, student_course_id)
        self.execute_command(query,parameter)
        
    def delete_student_enrollment_courses(self, student_course_id):
        query = "DELETE FROM student_enrollment_courses WHERE student_course_id = %s"
        parameter = str(student_course_id)
        self.execute_command(query,parameter,True)
        
    def get_by_id(self, student_course_id ):
        query = "SELECT * FROM student_enrollment_courses WHERE student_course_id = %s"
        parameter = str(student_course_id)
        fetch_one = True
        self.execute_query(query,parameter,fetch_one,True)
        
ad = StudentEnrollmentCourse()

# ad.create_student_enrollment_course(1,1)
# ad.update_student_enrollment_course('hello','2024-08-05 15:30:00',1)
# ad.delete_student_enrollment_course('1')
ad.read_student_enrollment_courses()
# ad.get_by_id(2) 
# # print(ad.get_by_id('5') )