class Person:
    def show(self):

        print("ram")


class Student(Person):
    def show(self):

        print("arun")


o = Student()
o.show()            #student method will run