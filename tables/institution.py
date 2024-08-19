from tables.database_engine import DatabaseManager

class InstitutionRepository(DatabaseManager):

    def create_institution(self, institution_name, institution_type, region, province, municipality):
        query = "INSERT INTO Institution(institution_name, institution_type, region, province, municipality) VALUES (%s, %s, %s, %s, %s)"
        parameter = (institution_name, institution_type, region, province, municipality)
        self.execute_command(query,parameter)

    def get_all(self):
        query = "SELECT * FROM Institution"
        self.execute_query(query)

    def update_institution(self, institution_name, institution_type, region, province, municipality):
        query = "UPDATE Institution SET institution_type =  %s , region = %s, province = %s, municipality = %s WHERE institution_name = %s"
        parameter = (institution_name, institution_type, region, province, municipality)
        self.execute_command(query,parameter)

    def delete_institution(self, institution_name):
        query = "DELETE FROM Institution WHERE institution_name = %s"
        parameter = institution_name
        self.execute_command(query,parameter)

    def get_by_name(self, institution_name):
        query = "SELECT * FROM Institution WHERE institution_name = %s"
        fetch_one =  True
        parameter = institution_name
        self.execute_query(query,parameter, fetch_one)

ad = Institution()

ad.create_institution("superhero","dasff",'dsfsd','asdf', 'asdfa')
# ad.update_institution('alkdjf',';lkadj',2)
# ad.delete_institution("sdsd")
# # ad.read_institution()
# ad.get_by_name("sdsd")