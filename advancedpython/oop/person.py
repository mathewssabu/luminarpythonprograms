class person:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def print(self):
        print("name:",self.a)
        print("age:",self.b)

class student(person):
    def __init__(self,rollno,mark,a,b):
        super().__init__(a,b)
        self.rollno=rollno
        self.mark=mark
    def printv(self):
        print(self.rollno)
        print(self.mark)

o=student(2,100,"name",22)
o.print()
o.printv()