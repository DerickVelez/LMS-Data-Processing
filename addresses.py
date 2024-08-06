from database_manager import DatabaseManager

class Addresses(DatabaseManager):

    def create_address(self, current_address, permanent_address):
        query = "INSERT INTO Addresses(current_address, permanent_address) VALUES (%s, %s)"
        parameter = (current_address, permanent_address)
        self.execute_command(query,parameter)

    def read_address(self):
        query = "SELECT * FROM Addresses"
        self.execute_query(query)

    def update_address(self, current_address, permanent_address, address_id):
        query = "UPDATE Addresses SET current_address =  %s , permanent_address = %s WHERE address_id = %s"
        parameter = (current_address, permanent_address, address_id)
        self.execute_command(query,parameter)

    def delete_address(self, address_id):
        query = "DELETE FROM Addresses WHERE address_id = %s"
        parameter = str(address_id)
        self.execute_command(query,parameter)

    def get_by_id(self, address_id):
        query = "SELECT * FROM Addresses WHERE address_id = %s"
        parameter = str(address_id)
        fetch_one =  True
        self.execute_query(query,parameter,fetch_one)

ad = Addresses()

# ad.create_address("sdsd","dasff")
# ad.update_address('alkdjf',';lkadj',2)
ad.delete_address(4)
# ad.read_address()
# ad.get_by_id(2)