class Parent:#superclass base class or parent class
    pname='arun'
    def m1(self,age):
        self.age=age
        #print(Parent.pname,self.age)
                                                          #single inheritance
class Child(Parent):   #child class derived class
    def m2(self,name,age):
        self.name=name
        self.cage=age
        print("my name is",self.name,self.cage)
        print("my parent name is",Parent.pname,self.age)

o=Child()
o.m1(45)
o.m2("aravi",15)