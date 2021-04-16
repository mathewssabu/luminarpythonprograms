class Employee:
    cname="tata"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def putdata(self):
        print("Name=",self.name)
        print("company name=",Employee.cname)
        print("age=",self.age)
        print("salary",self.salary)

o=Employee("Mathews",22,25000)
#o.getdata("Mathews",22,25000)
o.putdata()