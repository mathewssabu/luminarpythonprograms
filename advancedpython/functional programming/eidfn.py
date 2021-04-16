employees={
    1000:{'name':"raj",'age':34,'desig':"ptrainer"},
    1001:{'name':"malik",'age':45,'desig':"data scientist"},
    1002:{'name':"alik",'age':25,'desig':"ai "}
}
def emp_details(**data):
    id=data["eid"]
    prop=data["prop"]
    if(id in employees):
        print(employees[id]["name"])
        print(employees[id][prop])
    else:
        print("id doesnot exist" )



emp_details(eid=1001,prop="desig")