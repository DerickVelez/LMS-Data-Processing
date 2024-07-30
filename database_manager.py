import psycopg2
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

class DatabaseManager:
    # def __init__(self):
    #     self.dbname = os.getenv("DATABASE")
    #     self.user =  os.getenv("USER")
    #     self.password = os.getenv("PASSWORD")
    #     self.host= os.getenv("HOST") 
    #     self.port = 5432 
        
    def connect():
        try:    
            conn = psycopg2.connect(
                database = os.getenv("DATABASE"),
                user =   os.getenv("USER"),
                password = os.getenv("PASSWORD"),
                host= os.getenv("HOST") ,
                port = 5432 )
            
            print('connection successful.')
            
            cur= conn.cursor()
        except(Exception, psycopg2.DatabaseError) as error: 
            print("Error while connecting to Postgresql table.", error)
            
        return conn, cur
    
    
