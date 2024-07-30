from database_manager import DatabaseManager
    
conn, cur = DatabaseManager.connect()

class DegreeProgram:
    def execute_command(query,parameter):
        try: 
            cur.execute(query,(parameter)) 
            print("command executed successfully")
            
        except(Exception) as error:
            print(error) 
            conn.rollback

        conn.commit()
        cur.close()
        conn.close()
        
    def execute_query(query,parameter=None, single=True):
        try: 
            if single: 
                cur.execute(query,(parameter)) 
                print("query executed successfully")
                data = cur.fetchone()
                print(data)
            else: 
                cur.execute(query,(parameter)) 
                print("query executed successfully")
                data = cur.fetchall()
                print(data)
                
        except(Exception) as error:
            print(error) 
            conn.rollback
        
       
        cur.close()
        conn.close()
        
        
        
query1 = "INSERT INTO Addresses(AddressId,Current_address,permanent_address) VALUES (%s,%s,%s)" 
query2 = "SELECT * FROM Addresses"
parameter1 = (1,2,4)
parameter2 = ('Addresses')
        
dp = DegreeProgram
# dp.execute_command(query1,parameter1)
dp.execute_query(query2)