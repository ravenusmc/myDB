#This file will check to ensure that the values entered, to create a database have a value

# from database import *
from tables_database import *

class Check_Value():

    def check_value(self, user_database, table_name, value1, data_type_1, value2, data_type_2, value3, 
      data_type_3, value4, data_type_4):
        if value2 == None:
            user_database.single_column_create(table_name, value1, data_type_1)
        if value3 == None: 
            user_database.double_column_create(table_name, value1, data_type_1, value2, data_type_2)
        # if value4 == None:
        #     db.triple_column_create(table_name, value1, data_type_1, value2, data_type_2, value3, data_type_3)
