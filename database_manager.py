import psycopg2
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

class DatabaseManager:
    def __init__(self):
        self.database = os.getenv("DATABASE")
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.host = os.getenv("HOST")
        self.port = os.getenv('PORT')
        
        
    def connect_db(self):
        conn = None
        cur = None
        try:    
            conn = psycopg2.connect(
                database = self.database,
                user =   self.user,
                password = self.password,
                host=  self.host,
                port = self.port )
            
            print('connection successful.')
            cur= conn.cursor()    
        except(Exception, psycopg2.DatabaseError) as error: 
            print("Error while connecting to Postgresql table.", error)
        return  conn , cur
    
    def execute_command(self, query,parameter):
        conn, cur = self.connect_db()
        try:             
            with conn.cursor() as curs:
                curs.execute(query,(parameter,))
                print("command executed successfully")
                    
        except(Exception) as error:
            print(error) 
            conn.rollback

        conn.commit()
        cur.close()
        conn.close()
        
    def execute_query(self, query,parameter=None, single = False):
        conn, cur = self.connect_db()
        try: 
            if single: 
                with conn.cursor() as curs:
                    curs.execute(query,(parameter,))
                    print("query executed successfully")
                    data = curs.fetchone()
                    print(data)
                        
            else: 
                with conn.cursor() as curs:
                    curs.execute(query,(parameter))
                    print("query executed successfully")
                    data = curs.fetchall()
                    print(data)
                
        except(Exception) as error:
            print(error) 
            conn.rollback
       
        cur.close()
        conn.close()
 