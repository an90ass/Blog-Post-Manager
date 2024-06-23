import mysql.connector

connection = mysql.connector.connect(
      host="localhost",
      user = "root",
      password = "",
   )
cursor = connection.cursor()
cursor.execute("CREATE DATABASE flask_users")
# cursor.execute("SHOW DATABASES")
# for db in cursor:
#     print(db)