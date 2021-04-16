import mysql.connector
f=open("employee","r")
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mathews@123",
    database="pythonfeb",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
for lines in f:
    line=lines.rstrip("\n").split(",")
    sql="insert into employee(eid,ename,desig,salary)values(%s,%s,%s,%s)"
    cursor.execute(sql,tuple(line))
    db.commit()
#except Exception as e:
#     print(e.args)
#     db.rollback()
# finally:
db.close()
