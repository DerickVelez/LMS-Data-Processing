from database_manager import DatabaseManager


class Semesters(DatabaseManager):
        
    def create_semesters(self, semester_id, year_from, year_to):
        query = "INSERT INTO Semesters( semester_id, year_from, year_to) VALUES (%s, %s, %s)"
        parameter = semester_id, str(year_from), str(year_to)
        self.execute_command(query,parameter)
       
    def read_semesters(self):
        query = "SELECT * FROM semesters"
        self.execute_query(query)
    
    def update_semesters(self, semester_id, year_from, year_to):
        query = "UPDATE semesters SET  year_from =  %s, year_to = %s  WHERE semester_id = %s"
        parameter = (year_from, year_to, semester_id)
        self.execute_command(query,parameter)
        
    def delete_semesters(self, semester_id):
        query = "DELETE FROM semesters WHERE semester_id = %s"
        parameter = str(semester_id)
        self.execute_command(query,parameter,True)
        
    def get_by_id(self, semesters_id ):
        query = "SELECT * FROM semesters WHERE semester_id = %s"
        parameter = (semesters_id)
        fetch_one = True
        self.execute_query(query,parameter,fetch_one,True)
        
ad = Semesters()

ad.create_semesters(1,'1999-12-13','2000-01-25')
# ad.update_semesters('hello',2),
# ad.delete_semesters(2)
# ad.read_semesters()
ad.get_by_id(2) 
# # print(ad.get_by_id('5') )