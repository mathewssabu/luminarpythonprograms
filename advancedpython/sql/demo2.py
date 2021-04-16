#step 1 import mysql module
import mysql.connector
#step 2 establish connection
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mathews@123",
    database="pythonfeb",
    auth_plugin="mysql_native_password"

)
#step 3 create cursor object
cursor=db.cursor()
#sql="create table stud(name varchar(50),age int)"
sql="insert into stud(name,age)values('mas',22)"
try:
   cursor.execute(sql)
   db.commit()
except Exception as e:
      print(e.args)
      db.rollback()
#data=cursor.fetchall()
# print(data)
finally:
       db.close()