from tables.database_engine import DatabaseManager

class CoursesRepository(DatabaseManager):
        
    def create_courses(self, course,course_type):
        query = "INSERT INTO Courses( course, course_type) VALUES ( %s,%s)"
        parameter = ( course, course_type)
        self.execute_command(query,parameter)
    
    def get_all(self):
        query = "SELECT * FROM Courses"
        self.execute_query(query)
    
    def update_courses(self, course, course_type, courses_id):
        query = "UPDATE Courses SET course =  %s, course_type = %s  WHERE course_id = %s"
        parameter = (course, course_type, courses_id)
        self.execute_command(query,parameter)
         
    def delete_courses(self, course_id):
        query = "DELETE FROM Courses WHERE course_id = %s"
        parameter = str(course_id)
        single = True
        self.execute_command(query,parameter,single)
        
    def get_by_id(self, course_id ):
        query = "SELECT * FROM Courses WHERE course_id = %s"
        parameter = str(course_id)
        fetch_one = True
        self.execute_query(query,parameter,fetch_one)
        
# ad = Co
# 
# nt(ad.get_by_id('5') )