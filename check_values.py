#This file will check to ensure that the values entered, to create a database have a value

from database import *

class Check_Value():

    def check_value(self, table_name, value1, data_type_1, value2, data_type_2, value3, data_type_3, value4, 
        data_type_4):
        db = Connection()
        if value2 == None:
            db.single_column_create(table_name, value1, data_type_1)
        if value3 == None: 
            db.double_column_create(table_name, value1, data_type_1, value2, data_type_2)
        if value4 == None:
            db.triple_column_create(table_name, value1, data_type_1, value2, data_type_2, value3, data_type_3)
