class Eg:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvar(self):
        print(self.name,"\n",self.age)

o=Eg("mathews",22)
o.printvar()