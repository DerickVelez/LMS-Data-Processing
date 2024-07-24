import psycopg2
import glob, os
from dotenv import load_dotenv, dotenv_values
        
load_dotenv()
path_file_dir = r"D:\development\SQL\Scripts\LMS_Scripts"
connection = psycopg2.connect(database= os.getenv("DATABASE"), user= os.getenv("USER"), password=os.getenv("PASSWORD"), host= os.getenv("HOST") , port=5432)

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Filename_Table ( Filename varchar(50));")

try:    
    os.chdir(path_file_dir)
    for file in glob.glob("*.sql"):

        f = open(os.path.join(path_file_dir,file), mode='r')
        content = f.read()    

        checkquery = 'SELECT * FROM Filename_Table WHERE Filename = %s'
        cursor.execute(checkquery,(file,))
        result = cursor.fetchone()
        
        if result is None:
            cursor.execute(content)
            cursor.execute("INSERT INTO Filename_Table(Filename) VALUES (%s)",(file,))
            print(f'{file} finished processing.')
            
        else:
            print(f'{file} is already processed.')  
            
        connection.commit()
        
        
except psycopg2.Error as e:
        print(f"Database error: {e}")
        if connection:
            connection.rollback() 
            
cursor.close()    
connection.close()
    