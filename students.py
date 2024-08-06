from database_manager import DatabaseManager

class Students(DatabaseManager):

    def create_students(self, current_address_id, permanent_address_id, gender, first_name, middle_name, last_name, cellnumber, email):
        query = "INSERT INTO Students( current_address_id, permanent_address_id, gender, first_name, middle_name, last_name, cellnumber, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        parameter = ( str(current_address_id), str(permanent_address_id), gender, first_name, middle_name, last_name, str(cellnumber), email)
        self.execute_command(query,parameter)

    def read_students(self):
        query = "SELECT * FROM Students"
        self.execute_query(query)

    def update_students(self, Students_name, Students_type, region, province, municipality):
        query = "UPDATE Students SET Students_type =  %s , region = %s, province = %s, municipality = %s WHERE Students_name = %s"
        parameter = (Students_name, Students_type, region, province, municipality)
        self.execute_command(query,parameter)

    def delete_students(self, Students_name):
        query = "DELETE FROM Students WHERE Students_name = %s"
        parameter = Students_name
        self.execute_command(query,parameter)

    def get_by_id(self, Students_name):
        query = "SELECT * FROM Students WHERE Students_name = %s"
        single =  True
        parameter = Students_name
        self.execute_query(query,parameter, single)

ad = Students()

ad.create_students(1,1,'m','jan', 'derick','velez',165465,'sdfas')
# ad.update_students('alkdjf',';lkadj',2)
# ad.delete_students("sdsd")
# # ad.read_students()
# ad.get_by_id("sdsd")