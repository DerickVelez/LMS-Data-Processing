from database_manager import DatabaseManager


class SectionsRepository(DatabaseManager):
        
    def create_sections(self, section_id, course_id):
        query = "INSERT INTO sections( section_id, course_id) VALUES (%s, %s)"
        parameter = section_id, course_id
        self.execute_command(query,parameter)
       
    def get_all(self):
        query = "SELECT * FROM sections"
        self.execute_query(query)
    
    def update_sections(self, course_id, section_id):
        query = "UPDATE sections SET  course_id =  %s  WHERE section_id = %s"
        parameter = (course_id, section_id)
        self.execute_command(query,parameter)
        
    def delete_sections(self, section_id):
        query = "DELETE FROM sections WHERE section_id = %s"
        parameter = str(section_id)
        self.execute_command(query,parameter,True)
        
    def get_by_id(self, sections_id ):
        query = "SELECT * FROM sections WHERE section_id = %s"
        parameter = (sections_id)
        fetch_one = True
        self.execute_query(query,parameter,fetch_one,True)
        
ad = Sections()

# ad.create_sections(2,1)
# ad.update_sections(2,2)
ad.delete_sections(2)
# ad.read_sections()
ad.get_by_id(2) 
# # print(ad.get_by_id('5') )