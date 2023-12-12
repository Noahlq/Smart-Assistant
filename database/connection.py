import pyodbc 
from dotenv import load_dotenv
import os

class connection:

    def __init__(self):

        load_dotenv('./database.env')
        self.SERVER = os.getenv('SERVER')
        self.DATABASE = os.getenv('DATABASE')
    
        self.cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for SQL Server};Server=' + self.SERVER + ';Database=' + self.DATABASE + ';trusted_connection=yes')

    def __exit__(self, exc_type, exc_value, traceback):
        self.cnxn.close()   
