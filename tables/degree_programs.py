from database_manager import DatabaseManager


class DegreeProgramsRepository(DatabaseManager):
        
    def create_degree_programs(self, degree_program_id, department_id):
        query = "INSERT INTO degree_programs( degree_program_id, department_id) VALUES (%s, %s)"
        parameter = degree_program_id, department_id
        self.execute_command(query,parameter)
       
    def get_all(self):
        query = "SELECT * FROM degree_programs"
        self.execute_query(query)
    
    def update_degree_programs(self, department_id, degree_program_id):
        query = "UPDATE degree_programs SET  department_id =  %s  WHERE degree_program_id = %s"
        parameter = (department_id, degree_program_id)
        self.execute_command(query,parameter)
        
    def delete_degree_programs(self, degree_program_id):
        query = "DELETE FROM degree_programs WHERE degree_program_id = %s"
        parameter = str(degree_program_id)
        self.execute_command(query,parameter,True)
        
    def get_by_id(self, degree_programs_id ):
        query = "SELECT * FROM degree_programs WHERE degree_program_id = %s"
        parameter = (degree_programs_id)
        fetch_one = True
        self.execute_query(query,parameter,fetch_one,True)
        
ad = DegreePrograms()

# ad.create_degree_programs(2,1)
# ad.update_degree_programs(2,2),
# ad.delete_degree_programs(2)
ad.read_degree_programs()
ad.get_by_id(2) 
# # print(ad.get_by_id('5') )