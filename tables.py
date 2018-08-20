#This file will hold all of the code to handle each users database and tables 

#importing needed files 
import mysql.connector

class Tables():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                            password='pass',
                            host='localhost',
                            port=3306)
        self.cursor = self.conn.cursor()

    def create_database(self, database_name):
        sql = 'CREATE DATABASE ' + database_name
        self.cursor.execute(sql)

    




