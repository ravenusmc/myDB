#All of the tables, that the user creates, will be placed underder their specific database 

#Importing files to use in this file.
import mysql.connector

class Tables_DataBases():

    def __init__(self, database_name):
        self.conn = mysql.connector.connect(user='ted',
                            password='pass',
                            host='localhost',
                            port=3306,
                            database=database_name)
        self.cursor = self.conn.cursor()

    #This method will create a new table with a single column
    def single_column_create(self, table_name, value1, data_type_1):
        sql = '''CREATE TABLE ''' + table_name + ''' (
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            ''' + value1 + ' ' + data_type_1 + ' ' + 'NOT NULL' ''' )'''
        print(sql)
        self.cursor.execute(sql)

    #This method will create a new table with a double column
    def double_column_create(self, table_name, value1, data_type_1, value2, data_type_2):
        sql = '''CREATE TABLE ''' + table_name + ''' (
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            ''' + value1 + ' ' + data_type_1 + ' ' + 'NOT NULL,' + '''
            ''' + value2 + ' ' + data_type_2 + ' ' + 'NOT NULL' ''' ) '''
        self.cursor.execute(sql)

    #This method will create a new table with a triple column
    def triple_column_create(self, table_name, value1, data_type_1, value2, data_type_2, value3, data_type_3):
        sql = '''CREATE TABLE ''' + table_name + ''' (
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            ''' + value1 + ' ' + data_type_1 + ' ' + 'NOT NULL,' + '''
            ''' + value2 + ' ' + data_type_2 + ' ' + 'NOT NULL,' + '''
            ''' + value3 + ' ' + data_type_3 + ' ' + 'NOT NULL' + '''
        ) 
       '''
        self.cursor.execute(sql)

    #This method will create a new table with four columns
    def four_column_create(self, table_name, value1, data_type_1, value2, data_type_2, value3, data_type_3,
        value4, data_type_4):
        sql = '''CREATE TABLE ''' + table_name + ''' (
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            ''' + value1 + ' ' + data_type_1 + ' ' + 'NOT NULL,' + '''
            ''' + value2 + ' ' + data_type_2 + ' ' + 'NOT NULL,' + '''
            ''' + value3 + ' ' + data_type_3 + ' ' + 'NOT NULL,' + '''
            ''' + value4 + ' ' + data_type_4 + ' ' + 'NOT NULL' + '''
        ) 
       '''
        self.cursor.execute(sql)

    #This method will create a new table with five columns
    def five_column_create(self, table_name, value1, data_type_1, value2, data_type_2, value3, data_type_3,
                value4, data_type_4, value5, data_type_5):
        sql = '''CREATE TABLE ''' + table_name + ''' (
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            ''' + value1 + ' ' + data_type_1 + ' ' + 'NOT NULL,' + '''
            ''' + value2 + ' ' + data_type_2 + ' ' + 'NOT NULL,' + '''
            ''' + value3 + ' ' + data_type_3 + ' ' + 'NOT NULL,' + '''
            ''' + value4 + ' ' + data_type_4 + ' ' + 'NOT NULL,' + '''
            ''' + value5 + ' ' + data_type_5 + ' ' + 'NOT NULL' + '''
        ) 
       '''
        self.cursor.execute(sql)

    #This method will create a new table with six columns
    def six_column_create(self, table_name, value1, data_type_1, value2, data_type_2, value3, data_type_3,
                value4, data_type_4, value5, data_type_5, value6, data_type_6):
        sql = '''CREATE TABLE ''' + table_name + ''' (
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            ''' + value1 + ' ' + data_type_1 + ' ' + 'NOT NULL,' + '''
            ''' + value2 + ' ' + data_type_2 + ' ' + 'NOT NULL,' + '''
            ''' + value3 + ' ' + data_type_3 + ' ' + 'NOT NULL,' + '''
            ''' + value4 + ' ' + data_type_4 + ' ' + 'NOT NULL,' + '''
            ''' + value5 + ' ' + data_type_5 + ' ' + 'NOT NULL,' + '''
            ''' + value6 + ' ' + data_type_6 + ' ' + 'NOT NULL' + '''
        ) 
       '''
        self.cursor.execute(sql)

    #This method will get the table columns
    def get_table_column_names(self, table_name):
        sql = '''desc ''' + table_name
        test = self.cursor.execute(sql)
        column_names = self.cursor.fetchall()
        return column_names

    #This method will sort out the specific names from the column_names list
    def get_specific_column_names(self, column_names):
        #I start the counter at 1 because I don't need the id name-that's auto generated 
        #by MySQL.
        count = 1
        length_of_column_names_list = len(column_names)
        #Because the column_names list has a whole bunch of attributes in it I only 
        #need the column names so this dictionary will hold that. 
        only_names_dict = {}
        while count < length_of_column_names_list:
            column_name = column_names[count][0]
            only_names_list[column_name] = count
            count += 1
        return only_names_dict

    #This method will add a new entry to the table. 
    def add_table_row(self, table, value_1, value_2, value_3, value_4, value_5, value_6):
        self._SQL = """inser into """ + table + """
        (firstname, lastname, email, username, password)"""

        self.conn.commit()


    # def insert_user(self, user):
    #     self._SQL = """insert into users
    #       (firstname, lastname, email, username, password)
    #       values
    #       (%s, %s, %s, %s, %s)"""
    #     self.cursor.execute(self._SQL, (user.firstname, user.lastname, user.email, user.username, user.password_hashed))
    #     self.conn.commit()















