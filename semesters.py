from database_manager import DatabaseManager


class Semesters(DatabaseManager):
        
    def create_semesters(self, semester_id):
        query = "INSERT INTO Semesters( semester_id) VALUES (%s)"
        parameter = str(semester_id)
        self.execute_command(query,parameter)
       
    def read_semesters(self):
        query = "SELECT * FROM semesters"
        self.execute_query(query)
    
    # def update_semesters(self, semesters_id):
    #     query = "UPDATE semesters SET  =  %s  WHERE semesters_id = %s"
    #     parameter = (semesters_name, semesters_id)
    #     self.execute_command(query,parameter)
        
    def delete_semesters(self, semester_id):
        query = "DELETE FROM semesters WHERE semester_id = %s"
        parameter = str(semester_id)
        self.execute_command(query,parameter)
        
    def get_by_id(self, semesters_id ):
        query = "SELECT * FROM semesters WHERE semester_id = %s"
        parameter = (semesters_id)
        single = True
        self.execute_query(query,parameter,single)
        
ad = Semesters()

# ad.create_semesters(2)
# ad.update_semesters('hello',2)
ad.delete_semesters(2)
# ad.read_semesters()
# ad.get_by_id(2) 
# # print(ad.get_by_id('5') )