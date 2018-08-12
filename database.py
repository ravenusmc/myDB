#This file will make the connection to the database

#Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector


class Connection():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                            password='pass',
                            host='localhost',
                            port=3306,
                            database='myDB')
        self.cursor = self.conn.cursor()

    #This method will encrypt the password
    def encrypt_pass(self, password):
        password = password.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return password, hashed

    #This method will insert a new user into the database.
    def insert_user(self, user):
        self._SQL = """insert into users
          (firstname, lastname, email, username, password)
          values
          (%s, %s, %s, %s, %s)"""
        self.cursor.execute(self._SQL, (user.firstname, user.lastname, user.email, user.username, user.password_hashed))
        self.conn.commit()