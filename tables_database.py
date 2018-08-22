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

