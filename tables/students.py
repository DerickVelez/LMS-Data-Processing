from tables.database_engine import DatabaseManager

class StudentsRepository(DatabaseManager):

    def create_students(self, current_address_id, permanent_address_id, gender, first_name, middle_name, last_name, cellnumber, email):
        query = "INSERT INTO Students( current_address_id, permanent_address_id, gender, first_name, middle_name, last_name, cellnumber, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        parameter = ( str(current_address_id), str(permanent_address_id), gender, first_name, middle_name, last_name, str(cellnumber), email)
        self.execute_command(query,parameter)

    def get_all(self):
        query = "SELECT * FROM Students"
        self.execute_query(query)

    def update_students(self, current_address_id, permanent_address_id, gender, first_name, middle_name, last_name, cellnumber, email, student_id):
        query = "UPDATE Students SET current_address_id = %s, permanent_address_id = %s, gender = %s, first_name = %s, middle_name = %s, last_name = %s, cellnumber = %s, email= %s WHERE student_id = %s"
        parameter = (current_address_id, permanent_address_id, gender, first_name, middle_name, last_name, cellnumber, email, student_id)
        self.execute_command(query,parameter)

    def delete_students(self, student_id):
        query = "DELETE FROM Students WHERE student_id = %s"
        parameter = student_id
        self.execute_command(query,parameter,True)

    def get_by_id(self, student_id):
        query = "SELECT * FROM Students WHERE student_id = %s"
        fetch_one =  True
        parameter = student_id
        self.execute_query(query,parameter, fetch_one, True)

ad = Students()

# ad.create_students(1,1,'m','jan', 'derick','velez',165465,'sdfas')
ad.update_students(1,1,'m','jan', 'pogi','velez',165465,'sdfas',1)
# ad.delete_students("sdsd")
ad.read_students()
# ad.get_by_id(1)

