class Person:
    def set(self,age,name):
        self.age=age
        self.name=name
    def get(self):
       print(self.age,self.name)


ob = Person()
a=input("age")
b=input("name")
ob.set(a,b)
ob.get()