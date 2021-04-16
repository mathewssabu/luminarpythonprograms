class Vehicle:
    def __init__(self,model,colour):
        self.model=model
        self.colour=colour

class Bus(Vehicle):
    def print(self):
        print(self.model,self.colour)


a=input("enter model")
b=input("enter colour")
o=Bus(a,b)
o.print()