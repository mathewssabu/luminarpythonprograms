class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Mobile(Parent):
    def mob(self):
        print("i haave mi")

class Child(Mobile):
    def print(self,cname,cage):
        self.cname=cname
        self.cage=cage
        print(self.name,self.age,"\n",self.cname,self.cage)

o=Child("mas",45)
o.print("ash",10)
o.mob()