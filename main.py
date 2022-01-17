import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="u590270588_test",
  password="Setupdev@1998",
  database="u590270588_testing"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.close()