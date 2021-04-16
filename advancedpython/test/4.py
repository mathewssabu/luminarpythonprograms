class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Dog(Animal):
    def __init__(self,breed,name,age):
        super().__init__(name,age)
        self.breed=breed
    def print(self):
        print(self.name,self.age,self.breed)

o=Dog("Jeff",4,"lab")
o.print()
