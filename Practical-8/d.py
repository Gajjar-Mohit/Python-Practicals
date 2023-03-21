import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mohit"
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE mydatabase")
print('database deleted')
