import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pass@321'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")

print("db created!")