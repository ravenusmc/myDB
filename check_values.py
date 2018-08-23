#This file will check to ensure that the values entered, to create a database have a value

# from database import *
from tables_database import *

class Check_Value():

    def check_value(self, user_database, table_name, value1, data_type_1, value2, data_type_2, value3, 
      data_type_3, value4, data_type_4, value5, data_type_5, value6, data_type_6):
        if value2 == None:
            user_database.single_column_create(table_name, value1, data_type_1)
        if value3 == None: 
            user_database.double_column_create(table_name, value1, data_type_1, value2, data_type_2)
        if value4 == None:
            user_database.triple_column_create(table_name, value1, data_type_1, value2, data_type_2, value3, data_type_3)
        if value5 == None:
            user_database.four_column_create(table_name, value1, data_type_1, value2, data_type_2, value3, data_type_3,
                value4, data_type_4)
        if value6 == None: 
            user_database.five_column_create(table_name, value1, data_type_1, value2, data_type_2, value3, data_type_3,
                value4, data_type_4, value5, data_type_5)
        if value6: 
            user_database.six_column_create(table_name, value1, data_type_1, value2, data_type_2, value3, data_type_3,
                value4, data_type_4, value5, data_type_5, value6, data_type_6)

    def check_values_add_to_table(self, user_database, table, value_1, value_2, value_3, value_4, value_5, value_6):
        if value6: 
            