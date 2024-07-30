# import psycopg2
# import glob, os
# from dotenv import load_dotenv, dotenv_values
        
# load_dotenv()
# path_file_dir = r"D:\development\SQL\Scripts\LMS_Scripts"
# connection = psycopg2.connect(database= os.getenv("DATABASE"), user= os.getenv("USER"), password=os.getenv("PASSWORD"), host= os.getenv("HOST") , port=5432)

# print()

# cursor = connection.cursor()


# cursor.execute(("""SELECT table_name FROM (%s).tables
#        WHERE table_schema = 'public'"""),(f"{os.getenv("DATABASE")}"),)
# for table in cursor.fetchall():
#     print(table)

from database_manager import connect

if __name__ == "populate_data.py":
       connect()