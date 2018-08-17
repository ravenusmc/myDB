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

    #This method will check to see if the password is in the database. 
    def check(self, username, password):
        #I first encode the password to utf-8
        password = password.encode('utf-8')
        #Creating the query for the database
        query = ("""SELECT * FROM users WHERE username = %s""")
        self.cursor.execute(query, (username,))
        row = self.cursor.fetchone()
        #Here I check to see if the username is in the database.
        if str(row) == 'None':
            flag = False
            not_found = True
            password_no_match = False
        #If the user name is in the database I move here to check if the password
        #is valid.
        else:
            hashed = row[5].encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                flag = True
                not_found = False
                password_no_match = False
            #This is a final catch all area. Basically if the password does not match 
            #the user is not getting in. 
            else:
                flag = False
                not_found = False
                password_no_match = True
        return flag, not_found, password_no_match

    #This method will get the userID from the users table
    def get_user_id(self, username):
        self._SQL = """select user_id from users 
        where username = %s"""
        self.cursor.execute(self._SQL, (username, ))
        row = self.cursor.fetchone()
        user_id = row[0]
        return user_id

    #This method will enter in data into the user_tables
    def data_into_user_tables(self, user_id, table_name):
        self._SQL = """insert into user_tables
          (user_id, tableName)
          values
          (%s, %s)"""
        self.cursor.execute(self._SQL, (user_id, table_name))
        self.conn.commit()
        print('DATA INSERTED')

    #This method will get the tables that apply to each user 
    def get_user_tables(self, user_id):
        self._SQL = """Select tableName from user_tables
        where user_id = %s"""
        self.cursor.execute(self._SQL, (user_id, ))
        rows = self.cursor.fetchall()
        return rows 

    #This method will get the only the table names from the result 
    #returned from the get_user_tables method
    def get_tables_array(self, tables):
        print(len(tables))
        print(tables[1][0])
        tables_list = []
        list_length = len(tables)
        count = 0
        while count < list_length:
            table_name = tables[count][0]
            tables_list.append(table_name)
            count += 1
        return tables_list













