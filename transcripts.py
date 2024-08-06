from database_manager import DatabaseManager


class Transcripts(DatabaseManager):
        
    def create_Transcripts(self, semester_id):
        query = "INSERT INTO Transcripts( semester_id) VALUES (%s)"
        parameter = str(semester_id)
        self.execute_command(query,parameter)  
       
    def read_Transcripts(self):
        query = "SELECT * FROM Transcripts"
        self.execute_query(query)
    
    # def update_Transcripts(self, Transcripts_id):
    #     query = "UPDATE Transcripts SET  =  %s  WHERE Transcripts_id = %s"
    #     parameter = (Transcripts_name, Transcripts_id)
    #     self.execute_command(query,parameter)
        
    def delete_Transcripts(self, Transcripts_id):
        query = "DELETE FROM Transcripts WHERE Transcripts_id = %s"
        parameter = str(Transcripts_id)
        self.execute_command(query,parameter)
        
    def get_by_id(self, Transcripts_id ):
        query = "SELECT * FROM Transcripts WHERE Transcripts_id = %s"
        parameter = str(Transcripts_id)
        single = True
        self.execute_query(query,parameter,single)
        
ad = Transcripts()

ad.create_Transcripts(2)
# ad.update_Transcripts('hello',2)
# ad.delete_Transcripts('1')
ad.read_Transcripts()
# ad.get_by_id('2') 
# # print(ad.get_by_id('5') )