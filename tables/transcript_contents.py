from tables.database_engine import DatabaseManager


class TranscriptContentsRepository(DatabaseManager):
        
    def create_transcript_contents(self, student_course_id):
        query = "INSERT INTO transcript_contents(student_course_id) VALUES (%s)"
        parameter = student_course_id
        self.execute_command(query,parameter,True)
       
    def get_all(self):
        query = "SELECT * FROM transcript_contents"
        self.execute_query(query)
    
    def update_transcript_contents(self, student_course_id, transcript_id):
        query = "UPDATE transcript_contents SET  student_course_id =  %s  WHERE transcript_id = %s"
        parameter = (student_course_id, transcript_id)
        self.execute_command(query,parameter)
        
    def delete_transcript_contents(self, student_course_id):
        query = "DELETE FROM transcript_contents WHERE transcript_id = %s"
        parameter = str(student_course_id)
        self.execute_command(query,parameter,True)
        
    def get_by_id(self, transcript_contents_id ):
        query = "SELECT * FROM transcript_contents WHERE transcript_id = %s"
        parameter = (transcript_contents_id)
        fetch_one = True
        self.execute_query(query,parameter,fetch_one,True)
        
ad = TranscriptContentst()

# ad.create_transcript_contents(3)
# ad.update_transcript_contents(3,2)
# ad.delete_transcript_contents(2)
# ad.read_transcript_contents()
ad.get_by_id(2) 
# # print(ad.get_by_id('5') )