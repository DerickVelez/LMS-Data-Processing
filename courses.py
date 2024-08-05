from database_manager import DatabaseManager


class Courses(DatabaseManager):
        
    def create_courses(self, course,course_type):
        query = "INSERT INTO Courses( course, course_type) VALUES ( %s,%s)"
        parameter = ( course, course_type)
        self.execute_command(query,parameter)
    
    def read_courses(self):
        query = "SELECT * FROM Courses"
        self.execute_query(query)
    
    def update_courses(self, course, course_type, courses_id):
        query = "UPDATE Courses SET course =  %s, course_type = %s  WHERE course_id = %s"
        parameter = (course, course_type, courses_id)
        self.execute_command(query,parameter)
         
    def delete_courses(self, course_id):
        query = "DELETE FROM Courses WHERE course_id = %s"
        parameter = str(course_id)
        self.execute_command(query,parameter)
        
    def get_by_id(self, course_id ):
        query = "SELECT * FROM Courses WHERE course_id = %s"
        parameter = str(course_id)
        single = True
        self.execute_query(query,parameter,single)
        
ad = Courses()

# ad.create_courses('dsafa', 'sdsd')
ad.update_courses('sdfs', 'hello',2)
# ad.delete_courses('1')
# ad.read_courses()
# ad.get_by_id('2') 
# # print(ad.get_by_id('5') )