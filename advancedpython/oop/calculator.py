class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("sum=",self.a+self.b)

    def sub(self):
        print("diff=",self.a-self.b)
    def mul(self):
        print("product=",self.a*self.b)


o=Calc(10,10)
o.add()
o.sub()
o.mul()