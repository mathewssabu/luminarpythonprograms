import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mathews@123",
    database="pythonfeb",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
sql="update employee set salary=34000 where eid=1003"
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
finally:
    db.close()