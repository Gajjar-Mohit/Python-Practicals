import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mohit",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
print("Table created")