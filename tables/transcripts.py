from tables.database_engine import DatabaseManager


class TranscriptsRepository(DatabaseManager):
        
    def create_Transcripts(self, requested_by, generated_date):
        query = "INSERT INTO Transcripts(requested_by, generated_date) VALUES (%s,%s)"
        parameter =  requested_by, generated_date
        self.execute_command(query,parameter)  
       
    def get_all(self):
        query = "SELECT * FROM Transcripts"
        self.execute_query(query)
    
    def update_Transcripts(self, requested_by, generated_date, transcript_id):
        query = "UPDATE Transcripts SET requested_by = %s, generated_date =  %s  WHERE transcript_id = %s"
        parameter = ( requested_by, generated_date, transcript_id)
        self.execute_command(query,parameter)
        
    def delete_Transcripts(self, Transcript_id):
        query = "DELETE FROM Transcripts WHERE Transcript_id = %s"
        parameter = str(Transcript_id)
        self.execute_command(query,parameter,True)
        
    def get_by_id(self, Transcript_id ):
        query = "SELECT * FROM Transcripts WHERE Transcript_id = %s"
        parameter = str(Transcript_id)
        fetch_one = True
        self.execute_query(query,parameter,fetch_one,True)
        
ad = Transcripts()

# ad.create_Transcripts('dfsf','2024-08-05 15:30:00')
# ad.update_Transcripts('hello','2024-08-05 15:30:00',1)
# ad.delete_Transcripts('1')
# ad.read_Transcripts()
ad.get_by_id(2) 
# # print(ad.get_by_id('5') )