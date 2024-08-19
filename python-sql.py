import mysql.connector as sql
sql.connect(user='root',host='localhost',passwd='0009',database='yuvan12')

mycon=sql.connect(user='root',host='localhost',passwd='0009',database='yuvan12')
if mycon.is_connected():
    print("GAE")
else:
    print("NOGAE")
