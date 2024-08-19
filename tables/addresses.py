from tables.database_engine import DatabaseManager


class AddressRepository(DatabaseManager):

    def create_address(self, current_address, permanent_address):
        query = "INSERT INTO Addresses(current_address, permanent_address) VALUES (%s, %s)"
        parameter = (current_address, permanent_address)
        return self.execute_command(query,parameter)
        # print('good')

    def get_all(self):
        query = "SELECT * FROM Addresses"
        return self.execute_query(query)
        
    def update_address(self, current_address, permanent_address, address_id):
        # query = f"UPDATE Addresses SET current_address =  %(current_address)s , permanent_address = %(permanent_address)s  WHERE address_id = %(id)s"
        query = "UPDATE Addresses SET current_address =  %s , permanent_address = %s  WHERE address_id = %s"
        parameter = (current_address, permanent_address, address_id)
        self.execute_command(query, parameter)
        # return self.execute_command(query,{"current_address":current_address,"permanent_address":permanent_address,"id":address_id})
        
        

    def delete_address(self, address_id):
        query = "DELETE FROM Addresses WHERE address_id = %s"
        parameter = str(address_id)
        self.execute_command(query,parameter,True)

    def get_by_id(self, address_id):
        query = "SELECT * FROM Addresses WHERE address_id = %s"
        parameter = str(address_id)
        fetch_one =  True
        return self.execute_query(query,parameter,fetch_one,True)

ad = AddressRepository()

# # ad.create_addre