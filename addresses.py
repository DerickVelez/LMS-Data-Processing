from database_manager import DatabaseManager


# conn, cur = DatabaseManager.connect_db()

class Addresses(DatabaseManager):
    # def __init__(self, address_id, current_address, permanent_address ):
    #     self.addresss_id = address_id
    #     self.current_address = current_address
    #     self.permanent_address = permanent_address

    def create_address(self, current_address, permanent_address):
        query = "INSERT INTO Addresses(current_address, permanent_address) VALUES (%s, %s)"
        parameter = (current_address, permanent_address)
        self.execute_command(query,parameter)

    def read_address(self):
        query = "SELECT * FROM Addresses"
        self.execute_query(query)

    def update_address(self, current_address, permanent_address, address_id):
        query = "UPDATE Addresses SE T current_address =  %s , permanent_address = %s WHERE addressid = %s"
        parameter = (current_address, permanent_address, address_id)
        self.execute_command(query,parameter)

    def delete_address(self, address_id):
        query = "DELETE FROM Addresses WHERE address_id = %s"
        parameter = address_id
        self.execute_command(query,parameter)

    def get_by_id(self, address_id):
        query = "SELECT * FROM Addresses WHERE address_id = %s"
        parameter = address_id
        single =  True
        self.execute_query(query,parameter,single)

ad = Addresses()

# ad.create_address("sdsd","dasff")
# ad.update_address('alkdjf',';lkadj',2)

# ad.read_address()
ad.get_by_id('2')