from tables.database_engine import DatabaseManager


class DepartmentsRepository(DatabaseManager):
        
    def create_department(self, department_name,department_code):
        query = "INSERT INTO Departments( department_name, department_code) VALUES ( %s,%s)"
        parameter = ( department_name, department_code)
        self.execute_command(query,parameter)
    
    def get_all(self):
        query = "SELECT * FROM Departments"
        self.execute_query(query)
    
    def update_department(self, department_name, department_id):
        query = "UPDATE Departments SET department_name =  %s  WHERE department_id = %s"
        parameter = (department_name, department_id)
        self.execute_command(query,parameter)
        
    def delete_department(self, department_id):
        query = "DELETE FROM Departments WHERE department_id = %s"
        parameter = str(department_id)
        self.execute_command(query,parameter)
        
    def get_by_id(self, department_id ):
        query = "SELECT * FROM Departments WHERE department_id = %s"
        parameter = str(department_id)
        fetch_one = True
        self.execute_query(query,parameter,fetch_one)
        
ad = Departments()


ad.create_department('dsafa', 'sdsd')
# ad.update_department('hello',2)
# ad.delete_department('1')
# ad.read_department()
ad.get_by_id(2) 
# # print(ad.get_by_id('5') )