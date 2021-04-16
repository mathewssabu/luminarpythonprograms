employees={
    1000:{'name':"raj",'age':34,'desig':"ptrainer"},
    1001:{'name':"malik",'age':45,'desig':"data scientist"}
}
eid=int(input("enter id"))
if(eid in employees):
  print(employees[eid]['name'])
else:
    print("invalid")