class College:
    collegename="lt"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,self.age)

    def __str__(self):
        return self.name+str(" ")+str(self.age)

o=College("anu",22)
print(o)