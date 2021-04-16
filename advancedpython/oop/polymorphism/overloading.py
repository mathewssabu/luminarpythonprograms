class Person:
    def show(self,num1):
        self.num1=num1
        print(self.num1)

class Student(Person):
    def show(self,num3,num2):
        self.num3=num3
        self.num2=num2
        print(self.num3,self.num2)
o=Student()
o.show(2)