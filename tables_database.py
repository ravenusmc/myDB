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
            only_names_dict[column_name] = count
            count += 1
        return only_names_dict

    def get_specific_column_names_list(self, column_names):
        count = 0
        length_of_column_names_list = len(column_names)
        #Because the column_names list has a whole bunch of attributes in it I only 
        #need the column names so this dictionary will hold that. 
        only_names_list = []
        while count < length_of_column_names_list:
            column_name = column_names[count][0]
            only_names_list.append(column_name)
            count += 1
        return only_names_list

    def get_column_data(self, table):
        query = ('''select * from ''' + table )
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def get_single_row_data(self, table, id):
        query = ('''select * from ''' + table + ''' where id = %s ''')
        self.cursor.execute(query, (id, ))
        row = self.cursor.fetchone()
        return row

    ##### The below methods will add new entry's to a table ###

    def add_one_row_to_table(self, column_names, table, value_1):
        sql = '''insert into ''' + table + ''' 
        (''' + column_names[1] + ''') 
           values (%s) '''
        self.cursor.execute(sql, (value_1, ))
        self.conn.commit()

    def add_two_row_to_table(self, column_names, table, value_1, value_2):
        sql = '''insert into ''' + table + ''' 
        (''' + column_names[1] + ',' + column_names[2] + ''') 
           values (%s, %s) '''
        self.cursor.execute(sql, (value_1, value_2))
        self.conn.commit()

    def add_three_row_to_table(self, column_names, table, value_1, value_2, value_3):
        sql = '''insert into ''' + table + ''' 
        (''' + column_names[1] + ',' + column_names[2] + ',' + column_names[3] + ''') 
           values (%s, %s, %s) '''
        self.cursor.execute(sql, (value_1, value_2, value_3))
        self.conn.commit()

    def add_four_row_to_table(self, column_names, table, value_1, value_2, value_3, value_4):
        sql = '''insert into ''' + table + ''' 
        (''' + column_names[1] + ',' + column_names[2] + ',' + column_names[3] + ',' + column_names[4] + ''') 
           values (%s, %s, %s, %s) '''
        self.cursor.execute(sql, (value_1, value_2, value_3, value_4))
        self.conn.commit()

    def add_five_row_to_table(self, column_names, table, value_1, value_2, value_3, value_4, value_5):
        sql = '''insert into ''' + table + ''' 
        (''' + column_names[1] + ',' + column_names[2] + ',' + column_names[3] + ',' + column_names[4] + ',' + column_names[5] + ''') 
            values (%s, %s, %s, %s, %s) '''
        self.cursor.execute(sql, (value_1, value_2, value_3, value_4, value_5))
        self.conn.commit()

    def add_six_row_to_table(self, column_names, table, value_1, value_2, value_3, value_4, value_5, value_6):
        sql = '''insert into ''' + table + ''' ( 
           ''' + column_names[1] + ',' + column_names[2] + ',' + column_names[3] + ''' 
           ''' + ',' + column_names[4] + ',' + column_names[5] + ',' + column_names[6] + ''')
           values (%s, %s, %s, %s, %s, %s) '''
        self.cursor.execute(sql, (value_1, value_2, value_3, value_4, value_5, value_6))
        self.conn.commit()

    ##### The below methods will update an entry's to a table ###

    def update_row_one(self, table, only_names_list, edited_row):
        sql = '''update ''' + table + ' ' + '''set ''' +  only_names_list[1] + ''' = %s
        where id = %s '''
        self.cursor.execute(sql, (edited_row.row_one, edited_row.id))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def update_row_two(self, table, only_names_list, edited_row):
        sql = '''update ''' + table + ' ' + '''set ''' +  only_names_list[1] + ''' = %s,
        ''' + only_names_list[2] + ''' = %s where id = %s '''
        self.cursor.execute(sql, (edited_row.row_one, edited_row.row_two, edited_row.id))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def update_row_six(self, table, only_names_list, edited_row):
        sql = '''update ''' + table + ' ' + '''set ''' +  only_names_list[1] + ''' = %s, 
        ''' + only_names_list[2] + ''' = %s, ''' + only_names_list[3] + ''' = %s, 
        ''' + only_names_list[4] + ''' = %s, ''' + only_names_list[5] + ''' = %s, 
        ''' + only_names_list[6] + ''' = %s where id = %s'''
        self.cursor.execute(sql, (edited_row.row_one, edited_row.row_two, edited_row.row_three,
            edited_row.row_four, edited_row.row_five, edited_row.row_six, edited_row.id))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()













