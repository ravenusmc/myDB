import mysql.connector

database_name = input('Please input name of the database: ')

db1 = mysql.connector.connect(user='ted',
                            password='pass',
                            host='localhost',
                            port=3306)
cursor = db1.cursor()
sql = 'CREATE DATABASE ' + database_name
cursor.execute(sql)

# cursor = conn.cursor()