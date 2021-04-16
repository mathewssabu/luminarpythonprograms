class Person:
    def set(self,name,age):
        self.name=name
        self.age=age
class Job:
    def setv(self,job,salary):
        self.job=job
        self.salary=salary


class Child(Person,Job):
    def setv1(self,cname,cage):
        self.cname=cname
        self.cage=cage
    def print(self):
        print(self.name,self.age,self.job,self.salary,self.cname,self.cage)

class Mark(Child):
    def setv2(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def printv2(self):
        print("child details:",self.cname,self.cage,"marks",self.m1,self.m2)


o = Mark()
o.set("arun",40)
o.setv("developer",40000)
o.setv1("manu",12)
o.setv2(45,46)
o.print()
o.printv2()


