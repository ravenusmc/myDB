import mysql.connector

# CREATE DATABASE menagerie;

# def executeScriptsFromFile(filename):
    # fd = open(filename, 'r')
    # sqlFile = fd.read()
    # fd.close()
    # sqlCommands = sqlFile.split(';')

    #cursor.execute(command)

    # for command in sqlCommands:
    #     try:
    #         if command.strip() != '':
    #             
    #     except IOError, msg:
    #         print "Command skipped: ", msg

database_name = input('Please input name of the database: ')

f = open("test.sql","w+")
f.write('CREATE DATABASE ' + database_name + ";")
# execfile("test.sql")
#executeScriptsFromFile('test.sql')
fd = open("test.sql", 'r')
sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';')
sqlCommands = sqlFile.split(';')

# Execute every command from the input file
for command in sqlCommands:
  c.execute(command)



#conn = mysql.connector.connect(user='ted',
#                             password='pass',
#                             host='localhost',
#                             port=3306,
#                             database=database_name)
#cursor = conn.cursor()
















































